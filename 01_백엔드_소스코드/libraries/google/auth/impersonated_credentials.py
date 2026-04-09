# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: impersonated_credentials.pyc (Python 3.11)

'''Google Cloud Impersonated credentials.

This module provides authentication for applications where local credentials
impersonates a remote service account using `IAM Credentials API`_.

This class can be used to impersonate a service account as long as the original
Credential object has the "Service Account Token Creator" role on the target
service account.

    .. _IAM Credentials API:
        https://cloud.google.com/iam/credentials/reference/rest/
'''
import base64
import copy
from datetime import datetime
from http.client import client as http_client
import json
from google.auth import _exponential_backoff
from google.auth import _helpers
from google.auth import credentials
from google.auth import exceptions
from google.auth import iam
from google.auth import jwt
from google.auth import metrics
from google.oauth2 import _client
_REFRESH_ERROR = 'Unable to acquire impersonated credentials'
_DEFAULT_TOKEN_LIFETIME_SECS = 3600
_GOOGLE_OAUTH2_TOKEN_ENDPOINT = 'https://oauth2.googleapis.com/token'
_TRUST_BOUNDARY_LOOKUP_ENDPOINT = 'https://iamcredentials.{}/v1/projects/-/serviceAccounts/{}/allowedLocations'
_SOURCE_CREDENTIAL_AUTHORIZED_USER_TYPE = 'authorized_user'
_SOURCE_CREDENTIAL_SERVICE_ACCOUNT_TYPE = 'service_account'
_SOURCE_CREDENTIAL_EXTERNAL_ACCOUNT_AUTHORIZED_USER_TYPE = 'external_account_authorized_user'

def _make_iam_token_request(request, principal, headers, body, universe_domain, iam_endpoint_override = (credentials.DEFAULT_UNIVERSE_DOMAIN, None)):
    '''Makes a request to the Google Cloud IAM service for an access token.
    Args:
        request (Request): The Request object to use.
        principal (str): The principal to request an access token for.
        headers (Mapping[str, str]): Map of headers to transmit.
        body (Mapping[str, str]): JSON Payload body for the iamcredentials
            API call.
        iam_endpoint_override (Optiona[str]): The full IAM endpoint override
            with the target_principal embedded. This is useful when supporting
            impersonation with regional endpoints.

    Raises:
        google.auth.exceptions.TransportError: Raised if there is an underlying
            HTTP connection error
        google.auth.exceptions.RefreshError: Raised if the impersonated
            credentials are not available.  Common reasons are
            `iamcredentials.googleapis.com` is not enabled or the
            `Service Account Token Creator` is not assigned
    '''
    if not iam_endpoint_override:
        pass
    iam_endpoint = iam._IAM_ENDPOINT.replace(credentials.DEFAULT_UNIVERSE_DOMAIN, universe_domain).format(principal)
    body = json.dumps(body).encode('utf-8')
    response = request(url = iam_endpoint, method = 'POST', headers = headers, body = body)
    response_body = response.data.decode('utf-8') if hasattr(response.data, 'decode') else response.data
    if response.status != http_client.OK:
        raise exceptions.RefreshError(_REFRESH_ERROR, response_body)
    
    try:
        token_response = json.loads(response_body)
        token = token_response['accessToken']
        expiry = datetime.strptime(token_response['expireTime'], '%Y-%m-%dT%H:%M:%SZ')
        return (token, expiry)
    except (KeyError, ValueError):
        caught_exc = None
        new_exc = exceptions.RefreshError('{}: No access token or invalid expiration in response.'.format(_REFRESH_ERROR), response_body)
        raise new_exc, caught_exc
        caught_exc = None
        del caught_exc



class Credentials(credentials.CredentialsWithTrustBoundary, credentials.Signing, credentials.CredentialsWithQuotaProject, credentials.Scoped):
    pass
# WARNING: Decompyle incomplete


class IDTokenCredentials(credentials.CredentialsWithQuotaProject):
    pass
# WARNING: Decompyle incomplete


def _sign_jwt_request(request, principal, headers, payload, delegates = ([],)):
    '''Makes a request to the Google Cloud IAM service to sign a JWT using a
    service account\'s system-managed private key.
    Args:
        request (Request): The Request object to use.
        principal (str): The principal to request an access token for.
        headers (Mapping[str, str]): Map of headers to transmit.
        payload (Mapping[str, str]): The JWT payload to sign. Must be a
            serialized JSON object that contains a JWT Claims Set.
        delegates (Sequence[str]): The chained list of delegates required
            to grant the final access_token.  If set, the sequence of
            identities must have "Service Account Token Creator" capability
            granted to the prceeding identity.  For example, if set to
            [serviceAccountB, serviceAccountC], the source_credential
            must have the Token Creator role on serviceAccountB.
            serviceAccountB must have the Token Creator on
            serviceAccountC.
            Finally, C must have Token Creator on target_principal.
            If left unset, source_credential must have that role on
            target_principal.

    Raises:
        google.auth.exceptions.TransportError: Raised if there is an underlying
            HTTP connection error
        google.auth.exceptions.RefreshError: Raised if the impersonated
            credentials are not available.  Common reasons are
            `iamcredentials.googleapis.com` is not enabled or the
            `Service Account Token Creator` is not assigned
    '''
    iam_endpoint = iam._IAM_SIGNJWT_ENDPOINT.format(principal)
    body = {
        'delegates': delegates,
        'payload': json.dumps(payload) }
    body = json.dumps(body).encode('utf-8')
    response = request(url = iam_endpoint, method = 'POST', headers = headers, body = body)
    response_body = response.data.decode('utf-8') if hasattr(response.data, 'decode') else response.data
    if response.status != http_client.OK:
        raise exceptions.RefreshError(_REFRESH_ERROR, response_body)
    
    try:
        jwt_response = json.loads(response_body)
        signed_jwt = jwt_response['signedJwt']
        return signed_jwt
    except (KeyError, ValueError):
        caught_exc = None
        new_exc = exceptions.RefreshError('{}: No signed JWT in response.'.format(_REFRESH_ERROR), response_body)
        raise new_exc, caught_exc
        caught_exc = None
        del caught_exc
