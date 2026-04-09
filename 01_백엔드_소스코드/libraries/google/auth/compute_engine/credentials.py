# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: credentials.pyc (Python 3.11)

'''Google Compute Engine credentials.

This module provides authentication for an application running on Google
Compute Engine using the Compute Engine metadata server.

'''
import datetime
from google.auth import _helpers
from google.auth import credentials
from google.auth import exceptions
from google.auth import iam
from google.auth import jwt
from google.auth import metrics
from google.auth.compute_engine import _metadata
from google.oauth2 import _client
_TRUST_BOUNDARY_LOOKUP_ENDPOINT = 'https://iamcredentials.{}/v1/projects/-/serviceAccounts/{}/allowedLocations'

class Credentials(credentials.CredentialsWithTrustBoundary, credentials.CredentialsWithUniverseDomain, credentials.CredentialsWithQuotaProject, credentials.Scoped):
    pass
# WARNING: Decompyle incomplete

_DEFAULT_TOKEN_LIFETIME_SECS = 3600
_DEFAULT_TOKEN_URI = 'https://www.googleapis.com/oauth2/v4/token'

class IDTokenCredentials(credentials.CredentialsWithTokenUri, credentials.Signing, credentials.CredentialsWithQuotaProject):
    pass
# WARNING: Decompyle incomplete
