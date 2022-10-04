import logging
from timeit import default_timer as timer

from keycloak.exceptions import KeycloakAuthenticationError

from cloudharness.auth import AuthClient


def timed_class_method(message):
    def wrapper(method):
        def wrapped(*args, **kwargs):
            start = timer()
            res = method(*args, **kwargs)
            end = timer()
            logging.info(f"{message} ({end - start} seconds)")
            return res

        return wrapped

    return wrapper


def refresh_keycloak_client(method):
    def wrapped(*args, **kwargs):
        self = args[0]
        try:
            res = method(*args, **kwargs)
        except KeycloakAuthenticationError:
            self.keycloak_admin = AuthClient().get_admin_client()
            res = method(*args, **kwargs)
        return res

    return wrapped
