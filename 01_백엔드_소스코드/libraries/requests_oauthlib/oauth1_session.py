# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: oauth1_session.pyc (Python 3.11)

from urllib.parse import urlparse
import logging
from oauthlib.common import add_params_to_uri
from oauthlib.common import urldecode as _urldecode
from oauthlib.oauth1 import SIGNATURE_HMAC, SIGNATURE_RSA, SIGNATURE_TYPE_AUTH_HEADER
import requests
from  import OAuth1
log = logging.getLogger(__name__)

def urldecode(body):
    '''Parse query or json to python dictionary'''
    
    try:
        return _urldecode(body)
    except Exception:
        import json
        return 



class TokenRequestDenied(ValueError):
    pass
# WARNING: Decompyle incomplete


class TokenMissing(ValueError):
    pass
# WARNING: Decompyle incomplete


class VerifierMissing(ValueError):
    pass


class OAuth1Session(requests.Session):
    pass
# WARNING: Decompyle incomplete
