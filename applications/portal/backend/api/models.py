from django.db import models
from django.db.models import Q
from django.db.models import Transform, CharField
from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.indexes import GinIndex


from areg_portal.settings import ANTIBODY_NAME_MAX_LEN, ANTIBODY_TARGET_MAX_LEN, VENDOR_MAX_LEN, \
    ANTIBODY_CATALOG_NUMBER_MAX_LEN, ANTIBODY_CLONALITY_MAX_LEN, \
    ANTIBODY_CLONE_ID_MAX_LEN, ANTIGEN_ENTREZ_ID_MAX_LEN, ANTIGEN_UNIPROT_ID_MAX_LEN, STATUS_MAX_LEN, \
    ANTIBODY_PRODUCT_ISOTYPE_MAX_LEN, ANTIBODY_PRODUCT_CONJUGATE_MAX_LEN, ANTIBODY_PRODUCT_FORM_MAX_LEN, \
    ANTIBODY_TARGET_MODIFICATION_MAX_LEN, ANTIBODY_TARGET_SUBREGION_MAX_LEN, ANTIBODY_DEFINING_CITATION_MAX_LEN, \
    ANTIBODY_ID_MAX_LEN, ANTIBODY_CAT_ALT_MAX_LEN, VENDOR_COMMERCIAL_TYPE_MAX_LEN, ANTIBODY_TARGET_EPITOPE_MAX_LEN, \
    VENDOR_NIF_MAX_LEN, ANTIBODY_TARGET_SPECIES_MAX_LEN, ANTIBODY_DISC_DATE_MAX_LEN, \
    URL_MAX_LEN


@CharField.register_lookup
class Normalize(Transform):
    lookup_name = 'normalize'

    def as_sql(self, compiler, connection):
        lhs, params = compiler.compile(self.lhs)
        return (f"UPPER(regexp_replace({lhs}, '[^a-zA-Z0-9]', '', 'g'))", params)


@CharField.register_lookup
class NormalizeRelaxed(Transform):
    lookup_name = 'normalize_relaxed'

    def as_sql(self, compiler, connection):
        lhs, params = compiler.compile(self.lhs)
        return (f"UPPER(regexp_replace({lhs}, '[^a-zA-Z0-9,]', '', 'g'))", params)


@CharField.register_lookup
class SplitOnComma(Transform):
    lookup_name = 'comma_split'

    def as_sql(self, compiler, connection):
        lhs, params = compiler.compile(self.lhs)
        return (f"regexp_replace({lhs}, '[, ]', ' ', 'g')", params)


class CommercialType(models.TextChoices):
    COMMERCIAL = 'commercial', 'commercial'
    PERSONAL = 'personal', 'personal'
    NON_PROFIT = 'non-profit', 'non-profit'
    OTHER = 'other', 'other'


class AntibodyClonality(models.TextChoices):
    UNKNOWN = 'unknown', 'Unknown'
    COCKTAIL = 'cocktail', 'Cocktail'
    CONTROL = 'control', 'Control'
    ISOTYPE_CONTROL = 'isotype control', 'Isotype Control'
    MONOCLONAL = 'monoclonal', 'Monoclonal'
    MONOCLONAL_SECONDARY = 'monoclonal secondary', 'Monoclonal Secondary'
    POLYCLONAL = 'polyclonal', 'Polyclonal'
    POLYCLONAL_SECONDARY = 'polyclonal secondary', 'Polyclonal Secondary'
    OLIGOCLONAL = 'oligoclonal', 'Oligoclonal'
    RECOMBINANT = 'recombinant', 'Recombinant'
    RECOMBINANT_MONOCLONAL = 'recombinant monoclonal', 'Recombinant Monoclonal'
    RECOMBINANT_MONOCLONAL_SECONDARY = 'recombinant monoclonal secondary', 'Recombinant Monoclonal Secondary'
    RECOMBINANT_POLYCLONAL = 'recombinant polyclonal', 'Recombinant Polyclonal'
    RECOMBINANT_POLYCLONAL_SECONDARY = 'recombinant polyclonal secondary', 'Recombinant Polyclonal Secondary'


class STATUS(models.TextChoices):
    CURATED = 'CURATED', 'Curated'
    REJECTED = 'REJECTED', 'Rejected'
    QUEUE = 'QUEUE', 'Queued'


class Vendor(models.Model):
    name = models.CharField(max_length=VENDOR_MAX_LEN, db_column='vendor', db_index=True)
    nif_id = models.CharField(max_length=VENDOR_NIF_MAX_LEN, db_column='nif_id', null=True)

    def __str__(self):
        return self.name


class VendorSynonym(models.Model):
    name = models.CharField(max_length=VENDOR_MAX_LEN, db_index=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, db_index=True)


class Specie(models.Model):
    name = models.CharField(max_length=ANTIBODY_TARGET_SPECIES_MAX_LEN, unique=True)


class VendorDomain(models.Model):
    base_url = models.URLField(unique=True, max_length=URL_MAX_LEN, null=True, db_column='domain_name', db_index=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.RESTRICT, null=True, db_column='vendor_id', db_index=True)
    is_domain_visible = models.BooleanField(default=True, db_column='link')
    status = models.CharField(
        max_length=STATUS_MAX_LEN,
        choices=STATUS.choices,
        default=STATUS.QUEUE, db_index=True
    )

    def __str__(self):
        return self.base_url


# TODO: Update according to https://github.com/MetaCell/scicrunch-antibody-registry/issues/65
class Gene(models.Model):
    symbol = models.CharField(max_length=ANTIBODY_TARGET_MAX_LEN, db_column='ab_target', null=True, db_index=True)
    entrez_id = models.CharField(unique=False, max_length=ANTIGEN_ENTREZ_ID_MAX_LEN, db_column='ab_target_entrez_gid',
                                 null=True, db_index=True)
    uniprot_id = models.CharField(unique=False, max_length=ANTIGEN_UNIPROT_ID_MAX_LEN, null=True, db_index=True)

    def __str__(self):
        return self.entrez_id


class Antibody(models.Model):
    # todo: make sure autoincrement is functional with incremental ingestion
    ix = models.AutoField(primary_key=True, unique=True, null=False)
    # todo: In the context, is a bit strange to have nullable antibody name
    ab_name = models.CharField(max_length=ANTIBODY_NAME_MAX_LEN, null=True, db_index=True)
    ab_id = models.IntegerField(db_index=True)
    accession = models.CharField(max_length=ANTIBODY_ID_MAX_LEN)
    commercial_type = models.CharField(
        max_length=VENDOR_COMMERCIAL_TYPE_MAX_LEN,
        choices=CommercialType.choices,
        default=CommercialType.OTHER,
        null=True
    )
    # This user id maps the users in keycloak
    uid = models.CharField(max_length=256, null=True, db_index=True)
    # Maps to old users -- used only for migration purpose
    uid_legacy = models.IntegerField(null=True)
    catalog_num = models.CharField(max_length=ANTIBODY_CATALOG_NUMBER_MAX_LEN, null=True, db_index=True)
    cat_alt = models.CharField(max_length=ANTIBODY_CAT_ALT_MAX_LEN, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.RESTRICT, null=True)
    url = models.URLField(max_length=URL_MAX_LEN, null=True)
    antigen = models.ForeignKey(Gene, on_delete=models.RESTRICT, db_column='antigen_id', null=True)
    species = models.ManyToManyField(Specie, db_column='target_species', related_name="targets",
                                     through='AntibodySpecies')
    subregion = models.CharField(max_length=ANTIBODY_TARGET_SUBREGION_MAX_LEN, db_column='target_subregion', null=True)
    modifications = models.CharField(max_length=ANTIBODY_TARGET_MODIFICATION_MAX_LEN, db_column='target_modification',
                                     null=True)
    epitope = models.CharField(max_length=ANTIBODY_TARGET_EPITOPE_MAX_LEN, null=True)
    source_organism = models.ForeignKey(Specie, on_delete=models.RESTRICT, related_name="source", null=True)
    clonality = models.CharField(
        max_length=ANTIBODY_CLONALITY_MAX_LEN,
        choices=AntibodyClonality.choices,
        default=AntibodyClonality.UNKNOWN,
    )
    clone_id = models.CharField(max_length=ANTIBODY_CLONE_ID_MAX_LEN, null=True)
    product_isotype = models.CharField(max_length=ANTIBODY_PRODUCT_ISOTYPE_MAX_LEN, null=True)
    product_conjugate = models.CharField(max_length=ANTIBODY_PRODUCT_CONJUGATE_MAX_LEN, null=True)
    defining_citation = models.CharField(max_length=ANTIBODY_DEFINING_CITATION_MAX_LEN, null=True)
    product_form = models.CharField(max_length=ANTIBODY_PRODUCT_FORM_MAX_LEN, null=True)
    comments = models.TextField(null=True)
    applications = models.TextField(null=True)
    kit_contents = models.TextField(null=True)
    feedback = models.TextField(null=True)
    curator_comment = models.TextField(null=True)
    disc_date = models.CharField(max_length=ANTIBODY_DISC_DATE_MAX_LEN, null=True)
    status = models.CharField(
        max_length=STATUS_MAX_LEN,
        choices=STATUS.choices,
        default=STATUS.QUEUE,
        db_index=True
    )
    insert_time = models.DateTimeField(auto_now_add=True, db_index=True)
    curate_time = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f"{self.catalog_num} #({self.cat_alt})"

    class Meta:
        constraints = [
            models.CheckConstraint(check=~Q(status='curated') | (Q(status='curated') &
                                                                 Q(catalog_num__isnull=False) &
                                                                 Q(ab_name__isnull=False) &
                                                                 Q(ab_name__exact='') &
                                                                 Q(vendor__isnull=False)),
                                   name='curated_constraints'),
        ]
        indexes = [
            GinIndex(SearchVector('catalog_num__normalize', config='english'), name='catalog_num_fts_idx'),
            GinIndex(SearchVector('cat_alt__normalize_relaxed__comma_split', config='english'), name='cat_alt_fts_idx'),
        ]


class AntibodySpecies(models.Model):
    antibody = models.ForeignKey(Antibody, on_delete=models.CASCADE, db_index=True)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE, db_index=True)



