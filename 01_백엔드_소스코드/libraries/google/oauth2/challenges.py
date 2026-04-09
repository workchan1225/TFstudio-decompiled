# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: challenges.pyc (Python 3.11)

''' Challenges for reauthentication.
'''
import abc
import base64
import getpass
import sys
from google.auth import _helpers
from google.auth import exceptions
from google.oauth2 import webauthn_handler_factory
from google.oauth2.webauthn_types import AuthenticationExtensionsClientInputs, GetRequest, PublicKeyCredentialDescriptor
REAUTH_ORIGIN = 'https://accounts.google.com'
SAML_CHALLENGE_MESSAGE = 'Please run `gcloud auth login` to complete reauthentication with SAML.'
WEBAUTHN_TIMEOUT_MS = 120000

def get_user_password(text):
    '''Get password from user.

    Override this function with a different logic if you are using this library
    outside a CLI.

    Args:
        text (str): message for the password prompt.

    Returns:
        str: password string.
    '''
    return getpass.getpass(text)


def ReauthChallenge():
    '''ReauthChallenge'''
    __doc__ = 'Base class for reauth challenges.'
    name = (lambda self: raise NotImplementedError('name property must be implemented'))()()
    is_locally_eligible = (lambda self: raise NotImplementedError('is_locally_eligible property must be implemented'))()()
    obtain_challenge_input = (lambda self, metadata: raise NotImplementedError('obtain_challenge_input method must be implemented'))()

ReauthChallenge = <NODE:27>(ReauthChallenge, 'ReauthChallenge', metaclass = abc.ABCMeta)

class PasswordChallenge(ReauthChallenge):
    """Challenge that asks for user's password."""
    name = (lambda self: 'PASSWORD')()
    is_locally_eligible = (lambda self: True)()
    obtain_challenge_input = (lambda self, unused_metadata: passwd = get_user_password('Please enter your password:')if not passwd:
passwd = ' '{
'credential': passwd })()


class SecurityKeyChallenge(ReauthChallenge):
    """Challenge that asks for user's security key touch."""
    name = (lambda self: 'SECURITY_KEY')()
    is_locally_eligible = (lambda self: True)()
    obtain_challenge_input = (lambda self, metadata: pass# WARNING: Decompyle incomplete
)()
    
    def _obtain_challenge_input_webauthn(self, metadata, webauthn_handler):
        sk = metadata.get('securityKey')
    # WARNING: Decompyle incomplete

    
    def _unpadded_urlsafe_b64recode(self, s):
        '''Converts standard b64 encoded string to url safe b64 encoded string
        with no padding.'''
        b = base64.urlsafe_b64decode(s)
        return base64.urlsafe_b64encode(b).decode().rstrip('=')



class SamlChallenge(ReauthChallenge):
    '''Challenge that asks the users to browse to their ID Providers.

    Currently SAML challenge is not supported. When obtaining the challenge
    input, exception will be raised to instruct the users to run
    `gcloud auth login` for reauthentication.
    '''
    name = (lambda self: 'SAML')()
    is_locally_eligible = (lambda self: True)()
    
    def obtain_challenge_input(self, metadata):
        raise exceptions.ReauthSamlChallengeFailError(SAML_CHALLENGE_MESSAGE)


AVAILABLE_CHALLENGES = (SecurityKeyChallenge(), PasswordChallenge(), SamlChallenge())()
