# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hybrid.pyc (Python 3.11)

'''
oauthlib.openid.connect.core.grant_types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
import logging
from oauthlib.oauth2.rfc6749.errors import InvalidRequestError
from oauthlib.oauth2.rfc6749.grant_types.authorization_code import AuthorizationCodeGrant as OAuth2AuthorizationCodeGrant
from request_validator import RequestValidator
from base import GrantTypeBase
log = logging.getLogger(__name__)

class HybridGrant(GrantTypeBase):
    pass
# WARNING: Decompyle incomplete
