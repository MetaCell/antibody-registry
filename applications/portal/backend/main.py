# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2022-10-24T13:12:56+00:00

from __future__ import annotations

import os
from typing import List, Optional, Union

from django.apps import apps
from django.conf import settings
from django.core.asgi import get_asgi_application
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Request
from fastapi.security import APIKeyCookie, HTTPBasicCredentials, HTTPBearer
from fastapi.staticfiles import StaticFiles
from openapi.models import (
    AddUpdateAntibody,
    Antibody,
    DataInfo,
    FilterRequest,
    PaginatedAntibodies,
)
from starlette.middleware.cors import CORSMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "areg_portal.settings")
apps.populate(settings.INSTALLED_APPS)

# migrate the Django models
os.system("python manage.py migrate")

from api.controllers import *
from cloudharness.auth import decode_token

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

from cloudharness.middleware import get_authentication_token, set_authentication_token


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # retrieve the bearer token from the header
    # and save it for use in the AuthClient
    authorization = request.headers.get('Authorization') or request.cookies.get(
        'kc-access'
    )
    if authorization:
        if "Bearer" in authorization:
            authorization = authorization.split("Bearer ")[1]
        set_authentication_token(authorization)
    return await call_next(request)


if os.environ.get('KUBERNETES_SERVICE_HOST', None):
    # init the auth service when running in/for k8s
    from cloudharness_django.services import get_auth_service, init_services

    init_services()
    # start the kafka event listener when running in/for k8s
    import cloudharness_django.services.events


# enable the Bearer Authentication
# security = APIKeyCookie(name="kc-access") # This works but having issues with dev server
security = HTTPBearer()


async def has_access(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Function that is used to validate the token in the case that it requires it
    """
    if not os.environ.get('KUBERNETES_SERVICE_HOST', None):
        return {}
    token = get_authentication_token()

    try:
        payload = decode_token(token)
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


@prefix_router.post(
    '/antibodies', response_model=None, tags=['antibody']
)
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
    '/antibodies/user',
    response_model=PaginatedAntibodies,
    tags=['antibody'],
    dependencies=PROTECTED,
)
def get_user_antibodies(
    page: Optional[int] = None, size: Optional[int] = None
) -> PaginatedAntibodies:
    """
    List Antibodies
    """
    return antibody_controller.get_user_antibodies(
        page=page,
        size=size,
    )


@prefix_router.get(
    '/antibodies/{antibody_id}', response_model=List[Antibody], tags=['antibody']
)
def get_antibody(antibody_id: int) -> List[Antibody]:
    """
    Get a Antibody
    """
    return antibody_controller.get_antibody(
        antibody_id=antibody_id,
    )


@prefix_router.put(
    '/antibodies/{antibody_id}',
    response_model=None,
    tags=['antibody'],
    dependencies=PROTECTED,
)
def update_antibody(antibody_id: int, body: AddUpdateAntibody = ...) -> None:
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
def delete_antibody(antibody_id: int) -> None:
    """
    Delete a Antibody
    """
    return antibody_controller.delete_antibody(
        antibody_id=antibody_id,
    )


@prefix_router.get('/datainfo', response_model=DataInfo, tags=None)
def get_datainfo() -> DataInfo:

    return api_controller.get_datainfo()


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
