# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: account.pyc (Python 3.11)

from enum import Enum

class LoginState(Enum):
    SIGN_IN = 'SignIn'
    SIGN_UP = 'SignUp'


class _AccountDescriptor:
    
    def __init__(self, name):
        self.name = name

    
    def __get__(self = None, obj = None, cls = None):
        return obj._account_data.get(self.name)

    
    def __set__(self = None, obj = None, value = None):
        raise AttributeError('Cannot set readonly attribute')



class Account:
    '''Represents an account displayed in a FedCM account list.

    See: https://w3c-fedid.github.io/FedCM/#dictdef-identityprovideraccount
         https://w3c-fedid.github.io/FedCM/#webdriver-accountlist
    '''
    account_id = _AccountDescriptor('accountId')
    email = _AccountDescriptor('email')
    name = _AccountDescriptor('name')
    given_name = _AccountDescriptor('givenName')
    picture_url = _AccountDescriptor('pictureUrl')
    idp_config_url = _AccountDescriptor('idpConfigUrl')
    terms_of_service_url = _AccountDescriptor('termsOfServiceUrl')
    privacy_policy_url = _AccountDescriptor('privacyPolicyUrl')
    login_state = _AccountDescriptor('loginState')
    
    def __init__(self, account_data):
        self._account_data = account_data
