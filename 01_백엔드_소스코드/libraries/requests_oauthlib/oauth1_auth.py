# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: oauth1_auth.pyc (Python 3.11)

import logging
from oauthlib.common import extract_params
from oauthlib.oauth1 import Client, SIGNATURE_HMAC, SIGNATURE_TYPE_AUTH_HEADER
from oauthlib.oauth1 import SIGNATURE_TYPE_BODY
from requests.utils import to_native_string
from requests.auth import AuthBase
CONTENT_TYPE_FORM_URLENCODED = 'application/x-www-form-urlencoded'
CONTENT_TYPE_MULTI_PART = 'multipart/form-data'
log = logging.getLogger(__name__)

class OAuth1(AuthBase):
    '''Signs the request using OAuth 1 (RFC5849)'''
    client_class = Client
    
    def __init__(self, client_key, client_secret, resource_owner_key, resource_owner_secret, callback_uri, signature_method, signature_type, rsa_key, verifier, decoding, client_class, force_include_body = (None, None, None, None, SIGNATURE_HMAC, SIGNATURE_TYPE_AUTH_HEADER, None, None, 'utf-8', None, False), **kwargs):
        
        try:
            signature_type = signature_type.upper()
        except AttributeError:
            pass

    # WARNING: Decompyle incomplete

    
    def __call__(self, r):
        '''Add OAuth parameters to the request.

        Parameters may be included from the body if the content-type is
        urlencoded, if no content type is set a guess is made.
        '''
        log.debug('Signing request %s using client %s', r, self.client)
        content_type = r.headers.get('Content-Type', '')
        if content_type or extract_params(r.body) or self.client.signature_type == SIGNATURE_TYPE_BODY:
            content_type = CONTENT_TYPE_FORM_URLENCODED
        if not isinstance(content_type, str):
            content_type = content_type.decode('utf-8')
        is_form_encoded = CONTENT_TYPE_FORM_URLENCODED in content_type
        if not is_form_encoded:
            log.debug('Including body in call to sign: %s', self.force_include_body)
            if is_form_encoded:
                r.headers['Content-Type'] = CONTENT_TYPE_FORM_URLENCODED
                if not r.body:
                    (r.url, headers, r.body) = self.client.sign(str(r.url), str(r.method), '', r.headers)
                elif self.force_include_body:
                    pass
        r.prepare_headers(headers)
        r.url = to_native_string(r.url)
        log.debug('Updated url: %s', r.url)
        log.debug('Updated headers: %s', headers)
        log.debug('Updated body: %r', r.body)
        return r
