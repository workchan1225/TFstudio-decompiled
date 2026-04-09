# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: external_account.pyc (Python 3.11)

'''External Account Credentials.

This module provides credentials that exchange workload identity pool external
credentials for Google access tokens. This facilitates accessing Google Cloud
Platform resources from on-prem and non-Google Cloud platforms (e.g. AWS,
Microsoft Azure, OIDC identity providers), using native credentials retrieved
from the current environment without the need to copy, save and manage
long-lived service account credentials.

Specifically, this is intended to use access tokens acquired using the GCP STS
token exchange endpoint following the `OAuth 2.0 Token Exchange`_ spec.

.. _OAuth 2.0 Token Exchange: https://tools.ietf.org/html/rfc8693
'''
import abc
import copy
from dataclasses import dataclass
import datetime
import functools
import io
import json
import re
from google.auth import _helpers
from google.auth import credentials
from google.auth import exceptions
from google.auth import impersonated_credentials
from google.auth import metrics
from google.oauth2 import sts
from google.oauth2 import utils
_EXTERNAL_ACCOUNT_JSON_TYPE = 'external_account'
_STS_GRANT_TYPE = 'urn:ietf:params:oauth:grant-type:token-exchange'
_STS_REQUESTED_TOKEN_TYPE = 'urn:ietf:params:oauth:token-type:access_token'
_CLOUD_RESOURCE_MANAGER = 'https://cloudresourcemanager.googleapis.com/v1/projects/'
_DEFAULT_TOKEN_URL = 'https://sts.{universe_domain}/v1/token'
SupplierContext = <NODE:12>()

def Credentials():
    '''Credentials'''
    pass
# WARNING: Decompyle incomplete

Credentials = <NODE:27>(Credentials, 'Credentials', credentials.Scoped, credentials.CredentialsWithQuotaProject, credentials.CredentialsWithTokenUri, metaclass = abc.ABCMeta)
