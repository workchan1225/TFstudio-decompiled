# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tokens.pyc (Python 3.11)

'''
authlib.openid.connect.core.tokens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains methods for adding JWT tokens to requests.
'''
from oauthlib.oauth2.rfc6749.tokens import TokenBase, get_token_from_header, random_token_generator

class JWTToken(TokenBase):
    __slots__ = ('request_validator', 'token_generator', 'refresh_token_generator', 'expires_in')
    
    def __init__(self, request_validator, token_generator, expires_in, refresh_token_generator = (None, None, None, None)):
