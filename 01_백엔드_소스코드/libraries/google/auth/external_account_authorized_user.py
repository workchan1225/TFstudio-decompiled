# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: external_account_authorized_user.pyc (Python 3.11)

'''External Account Authorized User Credentials.
This module provides credentials based on OAuth 2.0 access and refresh tokens.
These credentials usually access resources on behalf of a user (resource
owner).

Specifically, these are sourced using external identities via Workforce Identity Federation.

Obtaining the initial access and refresh token can be done through the Google Cloud CLI.

Example credential:
{
  "type": "external_account_authorized_user",
  "audience": "//iam.googleapis.com/locations/global/workforcePools/$WORKFORCE_POOL_ID/providers/$PROVIDER_ID",
  "refresh_token": "refreshToken",
  "token_url": "https://sts.googleapis.com/v1/oauth/token",
  "token_info_url": "https://sts.googleapis.com/v1/instrospect",
  "client_id": "clientId",
  "client_secret": "clientSecret"
}
'''
import datetime
import io
import json
from google.auth import _helpers
from google.auth import credentials
from google.auth import exceptions
from google.oauth2 import sts
from google.oauth2 import utils
_EXTERNAL_ACCOUNT_AUTHORIZED_USER_JSON_TYPE = 'external_account_authorized_user'

class Credentials(credentials.CredentialsWithTokenUri, credentials.ReadOnlyScoped, credentials.CredentialsWithQuotaProject):
    pass
# WARNING: Decompyle incomplete
