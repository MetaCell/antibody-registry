from typing import List
from functools import reduce
import re
from api.utilities.functions import catalog_number_chunked

from django.conf import settings
from django.db.models import F, Value
from django.db.models.functions import Length, Concat, Coalesce
from django.contrib.postgres.search import SearchVectorField, SearchRank, SearchQuery, SearchVector, SearchHeadline, SearchRank

from ..models import STATUS, Antibody, AntibodySearch

MIN_CATALOG_RANKING = 0.0  # TODO validate the proper ranking value
MAX_SEARCH_RESULTS = settings.LIMIT_NUM_RESULTS

def flat(l):
    return [item for sublist in l for item in sublist]


def fts_by_catalog_number(search: str):
    search = catalog_number_chunked(search, fill=" & ")

    search_query = SearchQuery(search, search_type='raw')

    vector = SearchVector('catalog_num_search', config='simple')
    catalog_num_match = (
        Antibody.objects.annotate(
            search=vector,
            ranking=SearchRank(vector, search_query, normalization=Value(1)))
        .filter(search=search_query, status=STATUS.CURATED, ranking__gte=MIN_CATALOG_RANKING)
    )
    # if we match catalog_num or cat_alt, we return those results without looking for other fields
    # as the match is a perfect match or a prefix match depending on the search word,
    # sorting the normalized catalog_num by length and returning the smallest
    count = catalog_num_match.count()
    if count >= 1:
        return catalog_num_match.order_by('-ranking'), count
    return None


def fts_antibodies(page: int = 0, size: int = settings.LIMIT_NUM_RESULTS, search: str = '') -> List[Antibody]:
    # According to https://github.com/MetaCell/scicrunch-antibody-registry/issues/52
    # Match the calalog number (make sure to treat the cat_alt field the same way)
    # If the catalog number is not matched, then return records if the query matches any visible or invisible field.
    #
    # In the case that the cat num is not matched,
    # primary ranking:
    # + Additional desirata3: if the name, clone ID, vendor name, match the search string, rank result
    #   higher than other field matches.
    # + Additional desirata: use the number of citations as part of the sorting function
    #   (the higher the citations, the higher the rank)
    # + Additional desirata2: if the record contains string in the "disc_date" field, then downgrade
    #   the result (put on bottom of result set)

    # preparing two search terms, one for catalog_num, the other for normal search.

    # search only allows alphanumeric characters and spaces
    cat_search = fts_by_catalog_number(re.sub(r'[^\w\s]', '', search))

    if cat_search:
        return cat_search
    
    return fts_others_search(page, size, search)
    
    


def fts_others_search(page: int = 0, size: int = settings.LIMIT_NUM_RESULTS, search: str = ''):
    search_query = SearchQuery(search)
    # According to https://github.com/MetaCell/scicrunch-antibody-registry/issues/52
    # If the catalog number is not matched, then return records if the query matches any visible or invisible field.

    ranking = SearchRank(F("search_vector"), search_query)

    # highlight_cols = flat((F(f), Value(' ')) for f in search_col_names)[:-1]

    offset = (page - 1) * size
    subfields_search = AntibodySearch.objects.annotate(
        ranking=ranking,
    ).filter(search_vector=search_query)

    count = subfields_search.count()

    if count == 0:
        return [], 0

    if count > settings.LIMIT_NUM_RESULTS:
        ids = [a.ix for a  in subfields_search[offset: size + offset]]
        return Antibody.objects.filter(ix__in=ids, disc_date__isnull=True).select_related('vendor'), count
    
    def sort_fn(x: AntibodySearch):
        ranking = -x.ranking
        if x.defining_citation:
            ranking -= x.defining_citation / 100
        
        if x.disc_date:
            ranking += 1000
        return ranking
    
    ids = [a.ix for a in sorted((a for a  in subfields_search),key=sort_fn)][offset: size + offset]
    return Antibody.objects.filter(ix__in=ids).select_related('vendor'), count


