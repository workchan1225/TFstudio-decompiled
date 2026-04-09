# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _auth.pyc (Python 3.11)

'''GRPCAuthMetadataPlugins for standard authentication.'''
import inspect
from typing import Any, Optional
import grpc

def _sign_request(callback = None, token = None, error = None):
    metadata = (('authorization', 'Bearer {}'.format(token)),)
    callback(metadata, error)


class GoogleCallCredentials(grpc.AuthMetadataPlugin):
    _credentials: Any = 'Metadata wrapper for GoogleCredentials from the oauth2client library.'
    
    def __init__(self = None, credentials = None):
        self._credentials = credentials
        self._is_jwt = 'additional_claims' in inspect.getfullargspec(credentials.get_access_token).args

    
    def __call__(self = None, context = None, callback = None):
        
        try:
            if self._is_jwt:
                access_token = self._credentials.get_access_token(additional_claims = {
                    'aud': context.service_url }).access_token
            else:
                access_token = self._credentials.get_access_token().access_token
            _sign_request(callback, access_token, None)
            return None
        except Exception:
            exception = None
            _sign_request(callback, None, exception)
            exception = None
            del exception
            return None
            exception = None
            del exception




class AccessTokenAuthMetadataPlugin(grpc.AuthMetadataPlugin):
    _access_token: str = 'Metadata wrapper for raw access token credentials.'
    
    def __init__(self = None, access_token = None):
        self._access_token = access_token

    
    def __call__(self = None, context = None, callback = None):
        _sign_request(callback, self._access_token, None)
