# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: credentials.pyc (Python 3.11)

'''OAuth 2.0 Credentials.

This module provides credentials based on OAuth 2.0 access and refresh tokens.
These credentials usually access resources on behalf of a user (resource
owner).

Specifically, this is intended to use access tokens acquired using the
`Authorization Code grant`_ and can refresh those tokens using a
optional `refresh token`_.

Obtaining the initial access and refresh token is outside of the scope of this
module. Consult `rfc6749 section 4.1`_ for complete details on the
Authorization Code grant flow.

.. _Authorization Code grant: https://tools.ietf.org/html/rfc6749#section-1.3.1
.. _refresh token: https://tools.ietf.org/html/rfc6749#section-6
.. _rfc6749 section 4.1: https://tools.ietf.org/html/rfc6749#section-4.1
'''
from datetime import datetime
import io
import json
import logging
import warnings
from google.auth import _cloud_sdk
from google.auth import _helpers
from google.auth import credentials
from google.auth import exceptions
from google.auth import metrics
from google.oauth2 import reauth
_LOGGER = logging.getLogger(__name__)
_GOOGLE_OAUTH2_TOKEN_ENDPOINT = 'https://oauth2.googleapis.com/token'
_GOOGLE_OAUTH2_TOKEN_INFO_ENDPOINT = 'https://oauth2.googleapis.com/tokeninfo'

class Credentials(credentials.CredentialsWithQuotaProject, credentials.ReadOnlyScoped):
    pass
# WARNING: Decompyle incomplete


class UserAccessTokenCredentials(credentials.CredentialsWithQuotaProject):
    pass
# WARNING: Decompyle incomplete
