from typing import List

from django.core.paginator import Paginator

from api.repositories import search_repository
from openapi.models import FilterRequest
from openapi.models import Antibody as AntibodyDTO, PaginatedAntibodies
from ..mappers.antibody_mapper import AntibodyMapper


antibody_mapper = AntibodyMapper()


def fts_antibodies(page: int = 0, size: int = 50, search: str = '') -> List[AntibodyDTO]:
    page = page or 0  # required at the moment, issue with default values in main.py-L134
    size = size or 50  # required at the moment, issue with default values in main.py-L134
    antibodies = [antibody_mapper.to_dto(a) for a in search_repository.fts_antibodies(search=search, page=page, size=size)]
    return PaginatedAntibodies(page=int(page), totalElements=len(antibodies), items=antibodies)


def filter_antibodies(body: FilterRequest) -> List[AntibodyDTO]:
    return search_repository.filter_antibodies()
