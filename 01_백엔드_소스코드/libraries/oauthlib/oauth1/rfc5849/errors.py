# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: errors.pyc (Python 3.11)

'''
oauthlib.oauth1.rfc5849.errors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Error used both by OAuth 1 clients and provicers to represent the spec
defined error responses for all four core grant types.
'''
from oauthlib.common import add_params_to_uri, urlencode

class OAuth1Error(Exception):
    pass
# WARNING: Decompyle incomplete


class InsecureTransportError(OAuth1Error):
    error = 'insecure_transport_protocol'
    description = 'Only HTTPS connections are permitted.'


class InvalidSignatureMethodError(OAuth1Error):
    error = 'invalid_signature_method'


class InvalidRequestError(OAuth1Error):
    error = 'invalid_request'


class InvalidClientError(OAuth1Error):
    error = 'invalid_client'
