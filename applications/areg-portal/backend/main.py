# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2022-09-19T15:36:02+00:00

from __future__ import annotations

import os
from typing import List, Optional

from django.apps import apps
from django.conf import settings
from django.core.asgi import get_asgi_application
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Path, Request
from fastapi.security import HTTPBasicCredentials, HTTPBearer
from fastapi.staticfiles import StaticFiles
from openapi.models import (
    AddUpdateAntibody,
    Antibody,
    FilterRequest,
    PaginatedAntibodies,
)
from starlette.middleware.cors import CORSMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "areg_portal.settings")
apps.populate(settings.INSTALLED_APPS)

# migrate the Django models
os.system("python manage.py migrate")

from api.controllers import *

app = FastAPI(
    title="SciCrunch Antibody Registry API",
    version="1.0.0",
    description="Antibody Registry API",
    debug=settings.DEBUG,
)


prefix_router = APIRouter(prefix="/api")


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from cloudharness.middleware import set_authentication_token


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # retrieve the bearer token from the header
    # and save it for use in the AuthClient
    authorization = request.headers.get('Authorization')
    if authorization:
        set_authentication_token(authorization)

    return await call_next(request)


if os.environ.get('KUBERNETES_SERVICE_HOST', None):
    # init the auth service when running in/for k8s
    from cloudharness_django.services import get_auth_service, init_services

    init_services()
    # start the kafka event listener when running in/for k8s
    import cloudharness_django.services.events

# enable the Bearer Authentication
security = HTTPBearer()


async def has_access(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Function that is used to validate the token in the case that it requires it
    """
    if not os.environ.get('KUBERNETES_SERVICE_HOST', None):
        return {}
    token = credentials.credentials

    try:
        payload = get_auth_service().get_auth_client().decode_token(token)
    except Exception as e:  # catches any exception
        raise HTTPException(
            status_code=401,
        )


PROTECTED = [Depends(has_access)]

# Operations


@prefix_router.get('/antibodies', response_model=PaginatedAntibodies, tags=['antibody'])
def get_antibodies(
    page: Optional[int] = None, size: Optional[int] = None
) -> PaginatedAntibodies:
    """
    List Antibodies
    """
    return antibody_controller.get_antibodies(
        page=page,
        size=size,
    )


@prefix_router.post('/antibodies', response_model=None, tags=['antibody'])
def create_antibody(body: AddUpdateAntibody) -> None:
    """
    Create a Antibody
    """
    return antibody_controller.create_antibody(
        body=body,
    )


@prefix_router.get(
    '/antibodies/search', response_model=PaginatedAntibodies, tags=['search']
)
def fts_antibodies(
    page: Optional[int] = None, size: Optional[int] = None, search: Optional[str] = None
) -> PaginatedAntibodies:
    """
    Full text search on Antibodies
    """
    return search_controller.fts_antibodies(
        page=page,
        size=size,
        search=search,
    )


@prefix_router.post(
    '/antibodies/search', response_model=List[Antibody], tags=['search']
)
def filter_antibodies(body: FilterRequest) -> List[Antibody]:
    """
    Search on Antibodies with custom filters
    """
    return search_controller.filter_antibodies(
        body=body,
    )


@prefix_router.get(
    '/antibodies/{antibody_id}', response_model=Antibody, tags=['antibody']
)
def get_antibody(antibody_id: str = Path(..., alias='antibodyId')) -> Antibody:
    """
    Get a Antibody
    """
    return antibody_controller.get_antibody(
        antibody_id=antibody_id,
    )


@prefix_router.put('/antibodies/{antibody_id}', response_model=None, tags=['antibody'])
def update_antibody(
    antibody_id: str = Path(..., alias='antibodyId'), body: AddUpdateAntibody = ...
) -> None:
    """
    Update a Antibody
    """
    return antibody_controller.update_antibody(
        antibody_id=antibody_id,
        body=body,
    )


@prefix_router.delete(
    '/antibodies/{antibody_id}', response_model=None, tags=['antibody']
)
def delete_antibody(antibody_id: str = Path(..., alias='antibodyId')) -> None:
    """
    Delete a Antibody
    """
    return antibody_controller.delete_antibody(
        antibody_id=antibody_id,
    )


@prefix_router.post('/ingest', response_model=None, tags=['ingest'])
def ingest(body: str) -> None:
    """
    Ingest antibody's csv data into the database
    """
    return ingest_controller.ingest(
        body=body,
    )


@prefix_router.get('/live', response_model=str, tags=['test'])
def live() -> str:
    """
    Checks if application is healthy
    """
    return test_controller.live()


@prefix_router.get('/ping', response_model=str, tags=['test'])
def ping() -> str:
    """
    Checks if application is up
    """
    return test_controller.ping()


@prefix_router.get('/ready', response_model=str, tags=['test'])
def ready() -> str:
    """
    Checks if application is ready to take requests
    """
    return test_controller.ready()


app.include_router(prefix_router)

app.mount("/static", StaticFiles(directory=settings.STATIC_ROOT), name="static")
app.mount("/media", StaticFiles(directory=settings.MEDIA_ROOT), name="media")
app.mount("/", get_asgi_application())
