# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: oauth2_session.pyc (Python 3.11)

import logging
from oauthlib.common import generate_token, urldecode
from oauthlib.oauth2 import WebApplicationClient, InsecureTransportError
from oauthlib.oauth2 import LegacyApplicationClient
from oauthlib.oauth2 import TokenExpiredError, is_secure_transport
import requests
log = logging.getLogger(__name__)

class TokenUpdated(Warning):
    pass
# WARNING: Decompyle incomplete


class OAuth2Session(requests.Session):
    pass
# WARNING: Decompyle incomplete
