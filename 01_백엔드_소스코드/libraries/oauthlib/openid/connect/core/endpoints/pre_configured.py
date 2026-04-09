# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pre_configured.pyc (Python 3.11)

'''
oauthlib.openid.connect.core.endpoints.pre_configured
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various endpoints needed
for providing OpenID Connect servers.
'''
from oauthlib.oauth2.rfc6749.endpoints import AuthorizationEndpoint, IntrospectEndpoint, ResourceEndpoint, RevocationEndpoint, TokenEndpoint
from oauthlib.oauth2.rfc6749.grant_types import AuthorizationCodeGrant as OAuth2AuthorizationCodeGrant, ClientCredentialsGrant, ImplicitGrant as OAuth2ImplicitGrant, ResourceOwnerPasswordCredentialsGrant
from oauthlib.oauth2.rfc8628.grant_types import DeviceCodeGrant
from oauthlib.oauth2.rfc6749.tokens import BearerToken
from grant_types import AuthorizationCodeGrant, HybridGrant, ImplicitGrant, RefreshTokenGrant
from grant_types.dispatchers import AuthorizationCodeGrantDispatcher, AuthorizationTokenGrantDispatcher, ImplicitTokenGrantDispatcher
from tokens import JWTToken
from userinfo import UserInfoEndpoint

class Server(UserInfoEndpoint, RevocationEndpoint, ResourceEndpoint, TokenEndpoint, IntrospectEndpoint, AuthorizationEndpoint):
    '''
    An all-in-one endpoint featuring all four major grant types
    and extension grants.
    '''
    
    def __init__(self, request_validator, token_expires_in, token_generator, refresh_token_generator = (None, None, None), *args, **kwargs):
        '''Construct a new all-grants-in-one server.

        :param request_validator: An implementation of
                                  oauthlib.oauth2.RequestValidator.
        :param token_expires_in: An int or a function to generate a token
                                 expiration offset (in seconds) given a
                                 oauthlib.common.Request object.
        :param token_generator: A function to generate a token from a request.
        :param refresh_token_generator: A function to generate a token from a
                                        request for the refresh token.
        :param kwargs: Extra parameters to pass to authorization-,
                       token-, resource-, and revocation-endpoint constructors.
        '''
        self.auth_grant = OAuth2AuthorizationCodeGrant(request_validator)
        self.implicit_grant = OAuth2ImplicitGrant(request_validator)
        self.password_grant = ResourceOwnerPasswordCredentialsGrant(request_validator)
        self.credentials_grant = ClientCredentialsGrant(request_validator)
        self.refresh_grant = RefreshTokenGrant(request_validator)
        self.openid_connect_auth = AuthorizationCodeGrant(request_validator)
        self.openid_connect_implicit = ImplicitGrant(request_validator)
        self.openid_connect_hybrid = HybridGrant(request_validator)
    # WARNING: Decompyle incomplete
