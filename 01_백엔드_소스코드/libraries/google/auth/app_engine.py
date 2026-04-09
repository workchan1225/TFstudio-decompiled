# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: app_engine.pyc (Python 3.11)

'''Google App Engine standard environment support.

This module provides authentication and signing for applications running on App
Engine in the standard environment using the `App Identity API`_.


.. _App Identity API:
    https://cloud.google.com/appengine/docs/python/appidentity/
'''
import datetime
from google.auth import _helpers
from google.auth import credentials
from google.auth import crypt
from google.auth import exceptions

try:
    from google.appengine.api import app_identity
except ImportError:
    app_identity = None


class Signer(crypt.Signer):
    '''Signs messages using the App Engine App Identity service.

    This can be used in place of :class:`google.auth.crypt.Signer` when
    running in the App Engine standard environment.
    '''
    key_id = (lambda self: pass)()
    sign = (lambda self, message: message = _helpers.to_bytes(message)(_, signature) = app_identity.sign_blob(message)signature)()


def get_project_id():
    '''Gets the project ID for the current App Engine application.

    Returns:
        str: The project ID

    Raises:
        google.auth.exceptions.OSError: If the App Engine APIs are unavailable.
    '''
    pass
# WARNING: Decompyle incomplete


class Credentials(credentials.CredentialsWithQuotaProject, credentials.Signing, credentials.Scoped):
    pass
# WARNING: Decompyle incomplete
