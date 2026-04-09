# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''
oauthlib.oauth1.rfc5849.endpoints.base
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for signing and checking OAuth 1.0 RFC 5849 requests.
'''
import time
from oauthlib.common import CaseInsensitiveDict, Request, generate_token
from  import CONTENT_TYPE_FORM_URLENCODED, SIGNATURE_HMAC_SHA1, SIGNATURE_HMAC_SHA256, SIGNATURE_HMAC_SHA512, SIGNATURE_PLAINTEXT, SIGNATURE_RSA_SHA1, SIGNATURE_RSA_SHA256, SIGNATURE_RSA_SHA512, SIGNATURE_TYPE_AUTH_HEADER, SIGNATURE_TYPE_BODY, SIGNATURE_TYPE_QUERY, errors, signature, utils

class BaseEndpoint:
    
    def __init__(self, request_validator, token_generator = (None,)):
