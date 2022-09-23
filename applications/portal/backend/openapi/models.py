# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2022-09-23T16:37:28+00:00

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, conint


class KeyValuePair(BaseModel):
    key: str = Field(..., description='String representation of the key')
    value: str = Field(..., description='String representation of the value')


class Status(Enum):
    CURATED = 'CURATED'
    REJECTED = 'REJECTED'
    QUEUE = 'QUEUE'


class Clonality(Enum):
    unknown = 'unknown'
    cocktail = 'cocktail'
    control = 'control'
    isotype_control = 'isotype control'
    monoclonal = 'monoclonal'
    monoclonal_secondary = 'monoclonal secondary'
    polyclonal = 'polyclonal'
    polyclonal_secondary = 'polyclonal secondary'
    oligoclonal = 'oligoclonal'
    recombinant = 'recombinant'
    recombinant_monoclonal = 'recombinant monoclonal'
    recombinant_monoclonal_secondary = 'recombinant monoclonal secondary'
    recombinant_polyclonal = 'recombinant polyclonal'
    recombinant_polyclonal_secondary = 'recombinant polyclonal secondary'


class CommercialType(Enum):
    commercial = 'commercial'
    non_profit = 'non-profit'
    personal = 'personal'
    other = 'other'


class AbstractAntibody(BaseModel):
    clonality: Optional[Clonality] = Field(
        None,
        description='Can include the following options: Unknown, Cocktail, Control, Isotype Control, Monoclonal, Monoclonal Secondary, Polyclonal, Polyclonal Secondary, Oligoclonal, Recombinant, Recombinant Monoclonal, Recombinant Monoclonal Secondary, Recombinant Polyclonal, Recombinant Polyclonal Secondary',
        example='cocktail',
    )
    epitope: Optional[str] = Field(
        None,
        description='The AA sequence that the antibody reagent binds to',
        example='OTTHUMP00000018992',
    )
    comments: Optional[str] = Field(
        None, description='A free text comment.', example='comment is free text'
    )
    url: Optional[str] = Field(
        None,
        description="Link to more information about the antibody. For personal antibodies this usually lists the the principal investigator's lab website or university affiliation.",
        example='https://www.bdbiosciences.com/en-it/products/reagents/flow-cytometry-reagents/clinical-discovery-research/single-color-antibodies-ruo-gmp/pe-mouse-anti-human-il-8.340510',
    )
    abName: Optional[str] = Field(
        None,
        description='Name provided by the company or the investigator; this does not need to be unique.',
    )
    abTarget: Optional[str] = Field(
        None,
        description='The symbol of the antigen molecule that the antibody was raised against.',
        example='LRKK2',
    )
    catalogNum: str = Field(
        ...,
        description='For company antibodies, the catalog number of the antibody.\nFor personal/other antibodies, an identifier unique to the antibody.',
        example='N176A/35',
    )
    cloneId: Optional[str] = Field(
        None,
        description='The identifier given by the manufacturer or creator of monoclonal antibodies, typically associated with the cell line name.',
        example='N176A/35',
    )
    commercialType: CommercialType = Field(
        ...,
        description='Can include the following: commercial, non-profit, personal, other',
        example='commercial',
    )
    definingCitation: Optional[str] = Field(
        None, description='The manuscript that describes the creation of the antibody. '
    )
    productConjugate: Optional[str] = Field(
        None,
        description='The molecule that the antibody is conjugated to. This is generally used for secondary antibodies but the field is not restricted as there can be various tags on primary antibodies as well. \n',
    )
    productForm: Optional[str] = Field(
        None,
        description='The formulation of the antibody product. Can include: Lyophilized, Affinity purified, Liquid',
    )
    productIsotype: Optional[str] = Field(
        None,
        description='Can include the following: IgG, IgY, IgA, IgM as well as the IgG subtypes',
    )
    sourceOrganism: Optional[str] = Field(
        None,
        description='The organism that the antibody was raised in; common antibodies are raised in goat, rabbit or mouse. Synthetic or bacterial origins can be noted for recombinant antibodies.\n',
        example='mouse',
    )
    targetSpecies: Optional[List[str]] = Field(
        None,
        description='The species associated with the antigen molecule. Multiple species are specified as a comma separated string',
        example='["mouse", "human"]',
    )
    uniprotId: Optional[str] = Field(
        None, description='Protein identifier from UNIPROT\n'
    )
    vendorName: Optional[str] = Field(
        None,
        description='The name of the company or laboratory for commercial antibodies.\nThe principal investigator name for personal/other antibodies.\n',
    )
    applications: Optional[str] = Field(None, description='', example='ELISA, IHC, WB')
    kitContents: Optional[str] = Field(
        None,
        description='',
        example='Sheep polyclonal anti-FSH antibody labeled with acridinium ester. Mouse monoclonal anti-FSH antibody covalently coupled to paramagnetic particles.',
    )


class DataInfo(BaseModel):
    total: conint(ge=0) = Field(
        ..., description='The total number of antibodies in the system'
    )
    lastupdate: date = Field(..., description='')


class AddUpdateAntibody(AbstractAntibody):
    url: str = Field(..., description='')


class FilterRequest(BaseModel):
    contains: Optional[List[KeyValuePair]] = Field(
        None,
        description='Array of key-value pairs, where key represents the column and value the string that should be contained',
    )
    equals: Optional[List[KeyValuePair]] = Field(
        None,
        description='Array of key-value pairs, where key represents the column and value the string that should be equalled to',
    )
    page: Optional[int] = Field(
        None,
        description='Represents the page requested, considering the size parameter',
    )
    size: Optional[int] = Field(
        None, description='Corresponds to the cardinality of antibodies requested'
    )
    search: Optional[str] = Field(
        None, description='The string to use to search for Antibodies'
    )
    endsWith: Optional[List[KeyValuePair]] = Field(
        None,
        description='Array of key-value pairs, where key represents the column and value the string that should be ending with',
    )
    sortOn: Optional[List[KeyValuePair]] = Field(
        None,
        description='Array of key-value pairs, where key represents the column and value the string ascending or descending\n\nOrder in the array, matches with the order of sorting filters, index 0 will be used to sort first',
    )
    startsWith: Optional[List[KeyValuePair]] = Field(
        None,
        description='Array of key-value pairs, where key represents the column and value the string that should be starting with',
    )


class Antibody(AbstractAntibody):
    accession: Optional[str] = Field(
        None,
        description='Thus value is the same as the Antibody identifier for newly added antibodies, different if antibody records have been consolidated or are not unique.\n',
    )
    status: Optional[Status] = Field(
        None, description='Can include: curated, rejected, queue\n'
    )
    feedback: Optional[str] = Field(
        None, description='Feedback to the submitted stored here'
    )
    abId: str = Field(..., description='Antibody identifier')
    catAlt: Optional[str] = Field(
        None,
        description='The alternative catalog numbers for this product, delimited by comma, e.g., 9101S, 9101P, 9191L',
    )
    curateTime: Optional[datetime] = Field(
        None, description='Unix time stamp when the row was last updated'
    )
    curatorComment: Optional[str] = Field(
        None, description='Curator comment about this reagent\n'
    )
    discDate: Optional[str] = Field(
        None,
        description='The date on which the antibody product was found to be discontinued',
    )
    insertTime: datetime = Field(
        ..., description='Unix time stamp when the row was inserted.'
    )
    targetModification: Optional[str] = Field(
        None, description='Any modification to the target protein'
    )
    targetSubregion: Optional[str] = Field(
        None,
        description='The subregion of the target protein that the epitope is contained in',
    )
    vendorId: Optional[int] = Field(None, description='')


class PaginatedAntibodies(BaseModel):
    page: float = Field(..., description='')
    totalElements: int = Field(..., description='')
    items: List[Antibody] = Field(..., description='')
