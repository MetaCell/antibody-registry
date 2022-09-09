# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2022-09-08T10:35:52+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Clonality(Enum):
    Unknown = 'Unknown'
    Cocktail = 'Cocktail'
    Control = 'Control'
    IsotypeControl = 'IsotypeControl'
    Monoclonal = 'Monoclonal'
    MonoclonalSecondary = 'MonoclonalSecondary'
    Polyclonal = 'Polyclonal'
    PolyclonalSecondary = 'PolyclonalSecondary'
    Oligoclonal = 'Oligoclonal'
    Recombinant = 'Recombinant'
    RecombinantMonoclonal = 'RecombinantMonoclonal'
    RecombinantMonoclonalSecondary = 'RecombinantMonoclonalSecondary'
    RecombinantPolyclonal = 'RecombinantPolyclonal'
    RecombinantPolyclonalSecondary = 'RecombinantPolyclonalSecondary'


class CommercialType(Enum):
    commercial = 'commercial'
    non_profit = 'non-profit'
    personal = 'personal'
    other = 'other'


class ProductForm(Enum):
    Lyophilized = 'Lyophilized'
    AffinityPurified = 'AffinityPurified'
    Liquid = 'Liquid'


class AbstractAntibody(BaseModel):
    clonality: Optional[Clonality] = Field(
        None,
        description='Can include the following options: Unknown, Cocktail, Control, Isotype Control, Monoclonal, Monoclonal Secondary, Polyclonal, Polyclonal Secondary, Oligoclonal, Recombinant, Recombinant Monoclonal, Recombinant Monoclonal Secondary, Recombinant Polyclonal, Recombinant Polyclonal Secondary',
    )
    epitope: Optional[str] = Field(
        None, description='The AA sequence that the antibody reagent binds to'
    )
    comments: Optional[str] = Field(None, description='A free text comment.')
    url: str = Field(
        ...,
        description="Link to more information about the antibody. For personal antibodies this usually lists the the principal investigator's lab website or university affiliation.",
    )
    abName: Optional[str] = Field(
        None,
        description='Name provided by the company or the investigator; this does not need to be unique.',
    )
    abTarget: Optional[str] = Field(
        None,
        description='The symbol of the antigen molecule that the antibody was raised against.',
    )
    catalogNum: str = Field(
        ...,
        description='For company antibodies, the catalog number of the antibody.\nFor personal/other antibodies, an identifier unique to the antibody.',
    )
    cloneId: Optional[str] = Field(
        None,
        description='The identifier given by the manufacturer or creator of monoclonal antibodies, typically associated with the cell line name.',
    )
    commercialType: CommercialType = Field(
        ...,
        description='Can include the following: commercial, non-profit, personal, other',
    )
    definingCitation: Optional[str] = Field(
        None, description='The manuscript that describes the creation of the antibody. '
    )
    productConjugate: Optional[str] = Field(
        None,
        description='The molecule that the antibody is conjugated to. This is generally used for secondary antibodies but the field is not restricted as there can be various tags on primary antibodies as well. \n',
    )
    productForm: Optional[ProductForm] = Field(
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
    )
    targetSpecies: Optional[str] = Field(
        None, description='The species associated with the antigen molecule.'
    )
    uniprotId: Optional[str] = Field(
        None, description='Protein identifier from UNIPROT\n'
    )
    vendorName: Optional[str] = Field(
        None,
        description='The name of the company or laboratory for company antibodies.\nThe principal investigator name for personal/other antibodies.\n',
    )


class Status(Enum):
    Curated = 'Curated'
    Rejected = 'Rejected'
    Queue = 'Queue'


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
    abTargetEntrezGid: Optional[str] = Field(
        None,
        description='Gene identifier for the gene that is associated with the protein target',
    )
    catAlt: Optional[str] = Field(
        None,
        description='The alternative catalog numbers for this product, delimited by comma, e.g., 9101S, 9101P, 9191L',
    )
    curateTime: datetime = Field(
        ..., description='Unix time stamp when the row was last updated'
    )
    curatorComment: Optional[str] = Field(
        None, description='Curator comment about this reagent\n'
    )
    discDate: Optional[datetime] = Field(
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


class AddUpdateAntibody(AbstractAntibody):
    pass


class KeyValuePair(BaseModel):
    key: str = Field(..., description='String representation of the key')
    value: str = Field(..., description='String representation of the value')


class PaginatedAntibodies(BaseModel):
    page: float = Field(..., description='')
    totalElements: int = Field(..., description='')
    items: List[Antibody] = Field(..., description='')


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
