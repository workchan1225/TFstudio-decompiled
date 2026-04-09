# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: virtual_authenticator.pyc (Python 3.11)

import functools
from base64 import urlsafe_b64decode, urlsafe_b64encode
from enum import Enum
from typing import Any

class Protocol(Enum, str):
    '''Protocol to communicate with the authenticator.'''
    CTAP2 = 'ctap2'
    U2F = 'ctap1/u2f'


class Transport(Enum, str):
    '''Transport method to communicate with the authenticator.'''
    BLE = 'ble'
    USB = 'usb'
    NFC = 'nfc'
    INTERNAL = 'internal'


class VirtualAuthenticatorOptions:
    Protocol = Protocol
    Transport = Transport
    
    def __init__(self, protocol, transport = None, has_resident_key = None, has_user_verification = None, is_user_consenting = (Protocol.CTAP2, Transport.USB, False, False, True, False), is_user_verified = ('protocol', str, 'transport', str, 'has_resident_key', bool, 'has_user_verification', bool, 'is_user_consenting', bool, 'is_user_verified', bool, 'return', None)):
        '''Constructor.

        Initialize VirtualAuthenticatorOptions object.
        '''
        self.protocol = protocol
        self.transport = transport
        self.has_resident_key = has_resident_key
        self.has_user_verification = has_user_verification
        self.is_user_consenting = is_user_consenting
        self.is_user_verified = is_user_verified

    
    def to_dict(self = None):
        return {
            'protocol': self.protocol,
            'transport': self.transport,
            'hasResidentKey': self.has_resident_key,
            'hasUserVerification': self.has_user_verification,
            'isUserConsenting': self.is_user_consenting,
            'isUserVerified': self.is_user_verified }



class Credential:
    
    def __init__(self, credential_id, is_resident_credential, rp_id = None, user_handle = None, private_key = None, sign_count = ('credential_id', bytes, 'is_resident_credential', bool, 'rp_id', str | None, 'user_handle', bytes | None, 'private_key', bytes, 'sign_count', int)):
        '''Constructor. A credential stored in a virtual authenticator.

        https://w3c.github.io/webauthn/#credential-parameters.

        Args:
            credential_id (bytes): Unique base64 encoded string.
            is_resident_credential (bool): Whether the credential is client-side discoverable.
            rp_id (str): Relying party identifier.
            user_handle (bytes): userHandle associated to the credential. Must be Base64 encoded string. Can be None.
            private_key (bytes): Base64 encoded PKCS#8 private key.
            sign_count (int): initial value for a signature counter.
        '''
        self._id = credential_id
        self._is_resident_credential = is_resident_credential
        self._rp_id = rp_id
        self._user_handle = user_handle
        self._private_key = private_key
        self._sign_count = sign_count

    id = (lambda self = None: urlsafe_b64encode(self._id).decode())()
    is_resident_credential = (lambda self = None: self._is_resident_credential)()
    rp_id = (lambda self = None: self._rp_id)()
    user_handle = (lambda self = None: if self._user_handle:
urlsafe_b64encode(self._user_handle).decode())()
    private_key = (lambda self = None: urlsafe_b64encode(self._private_key).decode())()
    sign_count = (lambda self = None: self._sign_count)()
    create_non_resident_credential = (lambda cls, id = None, rp_id = None, private_key = classmethod, sign_count = ('id', bytes, 'rp_id', str, 'private_key', bytes, 'sign_count', int, 'return', 'Credential'): cls(id, False, rp_id, None, private_key, sign_count))()
    create_resident_credential = (lambda cls, id, rp_id = None, user_handle = None, private_key = classmethod, sign_count = ('id', bytes, 'rp_id', str, 'user_handle', bytes | None, 'private_key', bytes, 'sign_count', int, 'return', 'Credential'): cls(id, True, rp_id, user_handle, private_key, sign_count))()
    
    def to_dict(self = None):
        credential_data = {
            'credentialId': self.id,
            'isResidentCredential': self._is_resident_credential,
            'rpId': self.rp_id,
            'privateKey': self.private_key,
            'signCount': self.sign_count }
        if self.user_handle:
            credential_data['userHandle'] = self.user_handle
        return credential_data

    from_dict = (lambda cls = None, data = None: _id = urlsafe_b64decode(f'''{data['credentialId']}==''')is_resident_credential = bool(data['isResidentCredential'])rp_id = data.get('rpId', None)private_key = urlsafe_b64decode(f'''{data['privateKey']}==''')sign_count = int(data['signCount'])user_handle = urlsafe_b64decode(f'''{data['userHandle']}==''') if data.get('userHandle', None) else Nonecls(_id, is_resident_credential, rp_id, user_handle, private_key, sign_count))()
    
    def __str__(self = None):
        return f'''Credential(id={self.id}, is_resident_credential={self.is_resident_credential}, rp_id={self.rp_id},            user_handle={self.user_handle}, private_key={self.private_key}, sign_count={self.sign_count})'''



def required_chromium_based_browser(func):
    '''Decorator to ensure that the client used is a chromium-based browser.'''
    pass
# WARNING: Decompyle incomplete


def required_virtual_authenticator(func):
    '''Decorator to ensure that the function is called with a virtual authenticator.'''
    pass
# WARNING: Decompyle incomplete
