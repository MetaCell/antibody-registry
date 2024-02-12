from datetime import datetime
from typing import List, Union

from cloudharness import log
from api.models import Antibody
from api.services.user_service import UnrecognizedUser, get_current_user_id


from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, FileResponse

from api.services import antibody_service
from api.utilities.exceptions import AntibodyDataException

from openapi.models import AddAntibody as AddAntibodyDTO, PaginatedAntibodies
from openapi.models import UpdateAntibody as UpdateAntibodyDTO
from openapi.models import Antibody as AntibodyDTO


def get_antibodies(page: int, size: int, updated_from: datetime, updated_to: datetime) -> PaginatedAntibodies:
    if page is None:
        page = 1
    if size is None:
        size = 50
    if page < 1:
        raise HTTPException(status_code=400, detail="Pages start at 1")
    if size < 1:
        raise HTTPException(status_code=400, detail="Size must be greater than 0")
    try:
        return antibody_service.get_antibodies(int(page), int(size), updated_from, updated_to)
    except ValueError:
        raise HTTPException(status_code=400, detail="Page and size must be integers")


def get_user_id() -> str:
    try:
        return get_current_user_id()
    except UnrecognizedUser:
        raise HTTPException(status_code=401, detail="Unrecognized user")


def get_user_antibodies(page: int = 1, size: int = 50) -> PaginatedAntibodies:
    return antibody_service.get_user_antibodies(get_current_user_id(), page, size)


def create_antibody(body: AddAntibodyDTO) -> Union[AntibodyDTO, JSONResponse]:
    try:
        return antibody_service.create_antibody(body, get_user_id())
    except AntibodyDataException as e:
        raise HTTPException(status_code=400, detail=dict(
            name=e.field_name, value=e.field_value))
    except antibody_service.DuplicatedAntibody as e:
        return JSONResponse(status_code=409, content=jsonable_encoder(e.antibody))
    except Exception as e:
        log.error("Error creating antibody: %s", e, exc_info=True)
        from pprint import pprint
        pprint(body.dict())
        raise e


def get_antibody(antibody_id: int) -> List[AntibodyDTO]:
    return antibody_service.get_antibody(antibody_id)


def update_user_antibody(accession_number: str, body: UpdateAntibodyDTO) -> AntibodyDTO:
    try:
        return antibody_service.update_antibody(get_user_id(), accession_number, body)
    except AntibodyDataException as e:
        raise HTTPException(status_code=400, detail=dict(
            name=e.field_name, value=e.field_value))


def delete_antibody(antibody_id: str) -> None:
    #FIXME this must be protected
    return antibody_service.delete_antibody(antibody_id)

def get_by_accession(accession_number: int) -> AntibodyDTO:
    try:
        return antibody_service.get_antibody_by_accession(accession_number)
    except Antibody.DoesNotExist as e:
        raise HTTPException(status_code=404, detail=e.message)


def get_antibodies_export():
    from api.services.export_service import generate_antibodies_csv_file
    fname = "/tmp/antibodies_export.csv"
    generate_antibodies_csv_file(fname)
    return FileResponse(fname, filename="antibodies_export.csv")