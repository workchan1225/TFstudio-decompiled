# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: aws.pyc (Python 3.11)

'''AWS Credentials and AWS Signature V4 Request Signer.

This module provides credentials to access Google Cloud resources from Amazon
Web Services (AWS) workloads. These credentials are recommended over the
use of service account credentials in AWS as they do not involve the management
of long-live service account private keys.

AWS Credentials are initialized using external_account arguments which are
typically loaded from the external credentials JSON file.

This module also provides a definition for an abstract AWS security credentials supplier.
This supplier can be implemented to return valid AWS security credentials and an AWS region
and used to create AWS credentials. The credentials will then call the
supplier instead of using pre-defined methods such as calling the EC2 metadata endpoints.

This module also provides a basic implementation of the
`AWS Signature Version 4`_ request signing algorithm.

AWS Credentials use serialized signed requests to the
`AWS STS GetCallerIdentity`_ API that can be exchanged for Google access tokens
via the GCP STS endpoint.

.. _AWS Signature Version 4: https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
.. _AWS STS GetCallerIdentity: https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html
'''
import abc
from dataclasses import dataclass
import hashlib
import hmac
from http.client import client as http_client
import json
import os
import posixpath
import re
from typing import Optional
import urllib
from urllib.parse import urljoin
from google.auth import _helpers
from google.auth import environment_vars
from google.auth import exceptions
from google.auth import external_account
_AWS_ALGORITHM = 'AWS4-HMAC-SHA256'
_AWS_REQUEST_TYPE = 'aws4_request'
_AWS_SECURITY_TOKEN_HEADER = 'x-amz-security-token'
_AWS_DATE_HEADER = 'x-amz-date'
_DEFAULT_AWS_REGIONAL_CREDENTIAL_VERIFICATION_URL = 'https://sts.{region}.amazonaws.com?Action=GetCallerIdentity&Version=2011-06-15'
_IMDSV2_SESSION_TOKEN_TTL_SECONDS = '300'

class RequestSigner(object):
    '''Implements an AWS request signer based on the AWS Signature Version 4 signing
    process.
    https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html
    '''
    
    def __init__(self, region_name):
        '''Instantiates an AWS request signer used to compute authenticated signed
        requests to AWS APIs based on the AWS Signature Version 4 signing process.

        Args:
            region_name (str): The AWS region to use.
        '''
        self._region_name = region_name

    
    def get_request_options(self, aws_security_credentials, url, method, request_payload, additional_headers = ('', { })):
        '''Generates the signed request for the provided HTTP request for calling
        an AWS API. This follows the steps described at:
        https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html

        Args:
            aws_security_credentials (AWSSecurityCredentials): The AWS security credentials.
            url (str): The AWS service URL containing the canonical URI and
                query string.
            method (str): The HTTP method used to call this API.
            request_payload (Optional[str]): The optional request payload if
                available.
            additional_headers (Optional[Mapping[str, str]]): The optional
                additional headers needed for the requested AWS API.

        Returns:
            Mapping[str, str]: The AWS signed request dictionary object.
        '''
        if not additional_headers:
            additional_headers = { }
            uri = urllib.parse.urlparse(url)
            normalized_uri = urllib.parse.urlparse(urljoin(url, posixpath.normpath(uri.path)))
            if uri.hostname or uri.scheme != 'https':
                raise exceptions.InvalidResource('Invalid AWS service URL')
            if not normalized_uri.path:
                header_map = _generate_authentication_header_map(host = uri.hostname, canonical_uri = '/', canonical_querystring = _get_canonical_querystring(uri.query), method = method, region = self._region_name, aws_security_credentials = aws_security_credentials, request_payload = request_payload, additional_headers = additional_headers)
                headers = {
                    'Authorization': header_map.get('authorization_header'),
                    'host': uri.hostname }
                if 'amz_date' in header_map:
                    headers[_AWS_DATE_HEADER] = header_map.get('amz_date')
    # WARNING: Decompyle incomplete



def _get_canonical_querystring(query):
    '''Generates the canonical query string given a raw query string.
    Logic is based on
    https://docs.aws.amazon.com/general/latest/gr/sigv4-create-canonical-request.html

    Args:
        query (str): The raw query string.

    Returns:
        str: The canonical query string.
    '''
    querystring = urllib.parse.parse_qs(query)
    querystring_encoded_map = { }
    for key in querystring:
        quote_key = urllib.parse.quote(key, safe = '-_.~')
        querystring_encoded_map[quote_key] = []
        for item in querystring[key]:
            querystring_encoded_map[quote_key].append(urllib.parse.quote(item, safe = '-_.~'))
            querystring_encoded_map[quote_key].sort()
            sorted_keys = list(querystring_encoded_map.keys())
            sorted_keys.sort()
            querystring_encoded_pairs = []
            for key in sorted_keys:
                for item in querystring_encoded_map[key]:
                    querystring_encoded_pairs.append('{}={}'.format(key, item))
                    return '&'.join(querystring_encoded_pairs)


def _sign(key, msg):
    '''Creates the HMAC-SHA256 hash of the provided message using the provided
    key.

    Args:
        key (str): The HMAC-SHA256 key to use.
        msg (str): The message to hash.

    Returns:
        str: The computed hash bytes.
    '''
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()


def _get_signing_key(key, date_stamp, region_name, service_name):
    """Calculates the signing key used to calculate the signature for
    AWS Signature Version 4 based on:
    https://docs.aws.amazon.com/general/latest/gr/sigv4-calculate-signature.html

    Args:
        key (str): The AWS secret access key.
        date_stamp (str): The '%Y%m%d' date format.
        region_name (str): The AWS region.
        service_name (str): The AWS service name, eg. sts.

    Returns:
        str: The signing key bytes.
    """
    k_date = _sign(('AWS4' + key).encode('utf-8'), date_stamp)
    k_region = _sign(k_date, region_name)
    k_service = _sign(k_region, service_name)
    k_signing = _sign(k_service, 'aws4_request')
    return k_signing


def _generate_authentication_header_map(host, canonical_uri, canonical_querystring, method, region, aws_security_credentials, request_payload, additional_headers = ('', { })):
    '''Generates the authentication header map needed for generating the AWS
    Signature Version 4 signed request.

    Args:
        host (str): The AWS service URL hostname.
        canonical_uri (str): The AWS service URL path name.
        canonical_querystring (str): The AWS service URL query string.
        method (str): The HTTP method used to call this API.
        region (str): The AWS region.
        aws_security_credentials (AWSSecurityCredentials): The AWS security credentials.
        request_payload (Optional[str]): The optional request payload if
            available.
        additional_headers (Optional[Mapping[str, str]]): The optional
            additional headers needed for the requested AWS API.

    Returns:
        Mapping[str, str]: The AWS authentication header dictionary object.
            This contains the x-amz-date and authorization header information.
    '''
    service_name = host.split('.')[0]
    current_time = _helpers.utcnow()
    amz_date = current_time.strftime('%Y%m%dT%H%M%SZ')
    date_stamp = current_time.strftime('%Y%m%d')
    full_headers = { }
# WARNING: Decompyle incomplete

AwsSecurityCredentials = <NODE:12>()

def AwsSecurityCredentialsSupplier():
    '''AwsSecurityCredentialsSupplier'''
    __doc__ = 'Base class for AWS security credential suppliers. This can be implemented with custom logic to retrieve\n    AWS security credentials to exchange for a Google Cloud access token. The AWS external account credential does\n    not cache the AWS security credentials, so caching logic should be added in the implementation.\n    '
    get_aws_security_credentials = (lambda self, context, request: raise NotImplementedError(''))()
    get_aws_region = (lambda self, context, request: raise NotImplementedError(''))()

AwsSecurityCredentialsSupplier = <NODE:27>(AwsSecurityCredentialsSupplier, 'AwsSecurityCredentialsSupplier', metaclass = abc.ABCMeta)

class _DefaultAwsSecurityCredentialsSupplier(AwsSecurityCredentialsSupplier):
    '''Default implementation of AWS security credentials supplier. Supports retrieving
    credentials and region via EC2 metadata endpoints and environment variables.
    '''
    
    def __init__(self, credential_source):
        self._region_url = credential_source.get('region_url')
        self._security_credentials_url = credential_source.get('url')
        self._imdsv2_session_token_url = credential_source.get('imdsv2_session_token_url')

    get_aws_security_credentials = (lambda self, context, request: env_aws_access_key_id = os.environ.get(environment_vars.AWS_ACCESS_KEY_ID)env_aws_secret_access_key = os.environ.get(environment_vars.AWS_SECRET_ACCESS_KEY)env_aws_session_token = os.environ.get(environment_vars.AWS_SESSION_TOKEN)if env_aws_access_key_id and env_aws_secret_access_key:
AwsSecurityCredentials(env_aws_access_key_id, env_aws_secret_access_key, env_aws_session_token)imdsv2_session_token = None._get_imdsv2_session_token(request)role_name = self._get_metadata_role_name(request, imdsv2_session_token)credentials = self._get_metadata_security_credentials(request, role_name, imdsv2_session_token)AwsSecurityCredentials(credentials.get('AccessKeyId'), credentials.get('SecretAccessKey'), credentials.get('Token')))()
    get_aws_region = (lambda self, context, request: env_aws_region = os.environ.get(environment_vars.AWS_REGION)# WARNING: Decompyle incomplete
)()
    
    def _get_imdsv2_session_token(self, request):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_metadata_security_credentials(self, request, role_name, imdsv2_session_token):
        '''Retrieves the AWS security credentials required for signing AWS
        requests from the AWS metadata server.

        Args:
            request (google.auth.transport.Request): A callable used to make
                HTTP requests.
            role_name (str): The AWS role name required by the AWS metadata
                server security_credentials endpoint in order to return the
                credentials.
            imdsv2_session_token (str): The AWS IMDSv2 session token to be added as a
                header in the requests to AWS metadata endpoint.

        Returns:
            Mapping[str, str]: The AWS metadata server security credentials
                response.

        Raises:
            google.auth.exceptions.RefreshError: If an error occurs while
                retrieving the AWS security credentials.
        '''
        headers = {
            'Content-Type': 'application/json' }
    # WARNING: Decompyle incomplete

    
    def _get_metadata_role_name(self, request, imdsv2_session_token):
        '''Retrieves the AWS role currently attached to the current AWS
        workload by querying the AWS metadata server. This is needed for the
        AWS metadata server security credentials endpoint in order to retrieve
        the AWS security credentials needed to sign requests to AWS APIs.

        Args:
            request (google.auth.transport.Request): A callable used to make
                HTTP requests.
            imdsv2_session_token (str): The AWS IMDSv2 session token to be added as a
                header in the requests to AWS metadata endpoint.

        Returns:
            str: The AWS role name.

        Raises:
            google.auth.exceptions.RefreshError: If an error occurs while
                retrieving the AWS role name.
        '''
        pass
    # WARNING: Decompyle incomplete



class Credentials(external_account.Credentials):
    pass
# WARNING: Decompyle incomplete
