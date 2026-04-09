# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: authorization.pyc (Python 3.11)

'''
oauthlib.oauth1.rfc5849.endpoints.authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for signing and checking OAuth 1.0 RFC 5849 requests.
'''
from urllib.parse import urlencode
from oauthlib.common import add_params_to_uri
from  import errors
from base import BaseEndpoint

class AuthorizationEndpoint(BaseEndpoint):
    '''An endpoint responsible for letting authenticated users authorize access
    to their protected resources to a client.

    Typical use would be to have two views, one for displaying the authorization
    form and one to process said form on submission.

    The first view will want to utilize ``get_realms_and_credentials`` to fetch
    requested realms and useful client credentials, such as name and
    description, to be used when creating the authorization form.

    During form processing you can use ``create_authorization_response`` to
    validate the request, create a verifier as well as prepare the final
    redirection URI used to send the user back to the client.

    See :doc:`/oauth1/validator` for details on which validator methods to implement
    for this endpoint.
    '''
    
    def create_verifier(self, request, credentials):
        '''Create and save a new request token.

        :param request: OAuthlib request.
        :type request: oauthlib.common.Request
        :param credentials: A dict of extra token credentials.
        :returns: The verifier as a dict.
        '''
        verifier = {
            'oauth_token': request.resource_owner_key,
            'oauth_verifier': self.token_generator() }
        verifier.update(credentials)
        self.request_validator.save_verifier(request.resource_owner_key, verifier, request)
        return verifier

    
    def create_authorization_response(self, uri, http_method, body, headers, realms, credentials = ('GET', None, None, None, None)):
