# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2022-07-22T15:05:59+00:00

from __future__ import annotations

import os

from django.apps import apps
from django.conf import settings
from django.core.asgi import get_asgi_application
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Request
from fastapi.security import HTTPBasicCredentials, HTTPBearer
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "areg.settings")
apps.populate(settings.INSTALLED_APPS)

# migrate the Django models
os.system("python manage.py migrate")

from api.controllers import *

app = FastAPI(
    description="areg",
    version="0.1.0",
    title="areg",
    contact={'email': 'cloudharness@metacell.us'},
    license={'name': 'UNLICENSED'},
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


# init the auth service
from cloudharness_django.services import get_auth_service, init_services

init_services()

# start the kafka event listener
import cloudharness_django.services.events

# enable the Bearer Authentication
security = HTTPBearer()


async def has_access(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Function that is used to validate the token in the case that it requires it
    """
    token = credentials.credentials

    try:
        payload = get_auth_service().get_auth_client().decode_token(token)
    except Exception as e:  # catches any exception
        raise HTTPException(
            status_code=401,
        )


PROTECTED = [Depends(has_access)]

# Operations


@prefix_router.get('/live', response_model=str, tags=['test'])
def live() -> str:
    """
    Test if application is healthy
    """
    return test_controller.live()


@prefix_router.get('/ping', response_model=str, tags=['test'])
def ping() -> str:
    """
    Test the application is up
    """
    return test_controller.ping()


@prefix_router.get('/ready', response_model=str, tags=['test'])
def ready() -> str:
    """
    Test if application is ready
    """
    return test_controller.ready()


app.include_router(prefix_router)

app.mount("/static", StaticFiles(directory=settings.STATIC_ROOT), name="static")
app.mount("/media", StaticFiles(directory=settings.MEDIA_ROOT), name="media")
app.mount("/", get_asgi_application())
