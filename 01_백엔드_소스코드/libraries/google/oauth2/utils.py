# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

'''OAuth 2.0 Utilities.

This module provides implementations for various OAuth 2.0 utilities.
This includes `OAuth error handling`_ and
`Client authentication for OAuth flows`_.

OAuth error handling
--------------------
This will define interfaces for handling OAuth related error responses as
stated in `RFC 6749 section 5.2`_.
This will include a common function to convert these HTTP error responses to a
:class:`google.auth.exceptions.OAuthError` exception.


Client authentication for OAuth flows
-------------------------------------
We introduce an interface for defining client authentication credentials based
on `RFC 6749 section 2.3.1`_. This will expose the following
capabilities:

    * Ability to support basic authentication via request header.
    * Ability to support bearer token authentication via request header.
    * Ability to support client ID / secret authentication via request body.

.. _RFC 6749 section 2.3.1: https://tools.ietf.org/html/rfc6749#section-2.3.1
.. _RFC 6749 section 5.2: https://tools.ietf.org/html/rfc6749#section-5.2
'''
import abc
import base64
import enum
import json
from google.auth import exceptions

class ClientAuthType(enum.Enum):
    basic = 1
    request_body = 2


class ClientAuthentication(object):
    '''Defines the client authentication credentials for basic and request-body
    types based on https://tools.ietf.org/html/rfc6749#section-2.3.1.
    '''
    
    def __init__(self, client_auth_type, client_id, client_secret = (None,)):
        '''Instantiates a client authentication object containing the client ID
        and secret credentials for basic and response-body auth.

        Args:
            client_auth_type (google.oauth2.oauth_utils.ClientAuthType): The
                client authentication type.
            client_id (str): The client ID.
            client_secret (Optional[str]): The client secret.
        '''
        self.client_auth_type = client_auth_type
        self.client_id = client_id
        self.client_secret = client_secret



def OAuthClientAuthHandler():
    '''OAuthClientAuthHandler'''
    pass
# WARNING: Decompyle incomplete

OAuthClientAuthHandler = <NODE:27>(OAuthClientAuthHandler, 'OAuthClientAuthHandler', metaclass = abc.ABCMeta)

def handle_error_response(response_body):
    '''Translates an error response from an OAuth operation into an
    OAuthError exception.

    Args:
        response_body (str): The decoded response data.

    Raises:
        google.auth.exceptions.OAuthError
    '''
    
    try:
        error_components = []
        error_data = json.loads(response_body)
        error_components.append('Error code {}'.format(error_data['error']))
        if 'error_description' in error_data:
            error_components.append(': {}'.format(error_data['error_description']))
        if 'error_uri' in error_data:
            error_components.append(' - {}'.format(error_data['error_uri']))
        error_details = ''.join(error_components)
    except (KeyError, ValueError):
        error_details = response_body

    raise exceptions.OAuthError(error_details, response_body)
