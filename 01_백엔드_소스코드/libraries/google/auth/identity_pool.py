# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: identity_pool.pyc (Python 3.11)

'''Identity Pool Credentials.

This module provides credentials to access Google Cloud resources from on-prem
or non-Google Cloud platforms which support external credentials (e.g. OIDC ID
tokens) retrieved from local file locations or local servers. This includes
Microsoft Azure and OIDC identity providers (e.g. K8s workloads registered with
Hub with Hub workload identity enabled).

These credentials are recommended over the use of service account credentials
in on-prem/non-Google Cloud platforms as they do not involve the management of
long-live service account private keys.

Identity Pool Credentials are initialized using external_account
arguments which are typically loaded from an external credentials file or
an external credentials URL.

This module also provides a definition for an abstract subject token supplier.
This supplier can be implemented to return a valid OIDC or SAML2.0 subject token
and used to create Identity Pool credentials. The credentials will then call the
supplier instead of using pre-defined methods such as reading a local file or
calling a URL.
'''

try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

import abc
import base64
import json
import os
from typing import NamedTuple
from google.auth import _helpers
from google.auth import exceptions
from google.auth import external_account
from google.auth.transport import _mtls_helper

def SubjectTokenSupplier():
    '''SubjectTokenSupplier'''
    __doc__ = 'Base class for subject token suppliers. This can be implemented with custom logic to retrieve\n    a subject token to exchange for a Google Cloud access token when using Workload or\n    Workforce Identity Federation. The identity pool credential does not cache the subject token,\n    so caching logic should be added in the implementation.\n    '
    get_subject_token = (lambda self, context, request: raise NotImplementedError(''))()

SubjectTokenSupplier = <NODE:27>(SubjectTokenSupplier, 'SubjectTokenSupplier', metaclass = abc.ABCMeta)

class _TokenContent(NamedTuple):
    location: str = 'Models the token content response from file and url internal suppliers.\n        Attributes:\n            content (str): The string content of the file or URL response.\n            location (str): The location the content was retrieved from. This will either be a file location or a URL.\n    '


class _FileSupplier(SubjectTokenSupplier):
    ''' Internal implementation of subject token supplier which supports reading a subject token from a file.'''
    
    def __init__(self, path, format_type, subject_token_field_name):
        self._path = path
        self._format_type = format_type
        self._subject_token_field_name = subject_token_field_name

    get_subject_token = (lambda self, context, request: if not os.path.exists(self._path):
raise exceptions.RefreshError("File '{}' was not found.".format(self._path))file_obj = open(self._path, 'r', encoding = 'utf-8')token_content = _TokenContent(file_obj.read(), self._path)None(None, None))()


class _UrlSupplier(SubjectTokenSupplier):
    ''' Internal implementation of subject token supplier which supports retrieving a subject token by calling a URL endpoint.'''
    
    def __init__(self, url, format_type, subject_token_field_name, headers):
        self._url = url
        self._format_type = format_type
        self._subject_token_field_name = subject_token_field_name
        self._headers = headers

    get_subject_token = (lambda self, context, request: response = request(url = self._url, method = 'GET', headers = self._headers)response_body = response.data.decode('utf-8') if hasattr(response.data, 'decode') else response.dataif response.status != 200:
raise exceptions.RefreshError('Unable to retrieve Identity Pool subject token', response_body)token_content = _TokenContent(response_body, self._url)_parse_token_data(token_content, self._format_type, self._subject_token_field_name))()


class _X509Supplier(SubjectTokenSupplier):
    '''Internal supplier for X509 workload credentials. This class is used internally and always returns an empty string as the subject token.'''
    
    def __init__(self, trust_chain_path, leaf_cert_callback):
        self._trust_chain_path = trust_chain_path
        self._leaf_cert_callback = leaf_cert_callback

    get_subject_token = (lambda self, context, request: crypto = cryptoimport OpenSSLleaf_cert = crypto.load_certificate(crypto.FILETYPE_PEM, self._leaf_cert_callback())trust_chain = self._read_trust_chain()cert_chain = []cert_chain.append(_X509Supplier._encode_cert(leaf_cert))# WARNING: Decompyle incomplete
)()
    
    def _read_trust_chain(self):
        crypto = crypto
        import OpenSSL
        certificate_trust_chain = []
    # WARNING: Decompyle incomplete

    
    def _encode_cert(cert):
        crypto = crypto
        import OpenSSL
        return base64.b64encode(crypto.dump_certificate(crypto.FILETYPE_ASN1, cert)).decode('utf-8')



def _parse_token_data(token_content, format_type, subject_token_field_name = ('text', None)):
    if format_type == 'text':
        token = token_content.content
    else:
        
        try:
            response_data = json.loads(token_content.content)
            token = response_data[subject_token_field_name]
        except (KeyError, ValueError):
            raise exceptions.RefreshError("Unable to parse subject_token from JSON file '{}' using key '{}'".format(token_content.location, subject_token_field_name))

        if not token:
            raise exceptions.RefreshError('Missing subject_token in the credential_source file')
        return token


class Credentials(external_account.Credentials):
    pass
# WARNING: Decompyle incomplete
