# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _cryptography_rsa.pyc (Python 3.11)

'''RSA verifier and signer that use the ``cryptography`` library.

This is a much faster implementation than the default (in
``google.auth.crypt._python_rsa``), which depends on the pure-Python
``rsa`` library.
'''
import cryptography.exceptions as cryptography
from cryptography.hazmat import backends
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import cryptography.x509 as cryptography
from google.auth import _helpers
from google.auth.crypt import base
_CERTIFICATE_MARKER = b'-----BEGIN CERTIFICATE-----'
_BACKEND = backends.default_backend()
_PADDING = padding.PKCS1v15()
_SHA256 = hashes.SHA256()

class RSAVerifier(base.Verifier):
    '''Verifies RSA cryptographic signatures using public keys.

    Args:
        public_key (
                cryptography.hazmat.primitives.asymmetric.rsa.RSAPublicKey):
            The public key used to verify signatures.
    '''
    
    def __init__(self, public_key):
        self._pubkey = public_key

    verify = (lambda self, message, signature: message = _helpers.to_bytes(message)try:
self._pubkey.verify(signature, message, _PADDING, _SHA256)Trueexcept (ValueError, cryptography.exceptions.InvalidSignature):
False)()
    from_string = (lambda cls, public_key: public_key_data = _helpers.to_bytes(public_key)if _CERTIFICATE_MARKER in public_key_data:
cert = cryptography.x509.load_pem_x509_certificate(public_key_data, _BACKEND)pubkey = cert.public_key()else:
pubkey = serialization.load_pem_public_key(public_key_data, _BACKEND)cls(pubkey))()


class RSASigner(base.FromServiceAccountMixin, base.Signer):
    '''Signs messages with an RSA private key.

    Args:
        private_key (
                cryptography.hazmat.primitives.asymmetric.rsa.RSAPrivateKey):
            The private key to sign with.
        key_id (str): Optional key ID used to identify this private key. This
            can be useful to associate the private key with its associated
            public key or certificate.
    '''
    
    def __init__(self, private_key, key_id = (None,)):
        self._key = private_key
        self._key_id = key_id

    key_id = (lambda self: self._key_id)()()
    sign = (lambda self, message: message = _helpers.to_bytes(message)self._key.sign(message, _PADDING, _SHA256))()
    from_string = (lambda cls, key, key_id = (None,): key = _helpers.to_bytes(key)private_key = serialization.load_pem_private_key(key, password = None, backend = _BACKEND)cls(private_key, key_id = key_id))()
    
    def __getstate__(self):
        '''Pickle helper that serializes the _key attribute.'''
        state = self.__dict__.copy()
        state['_key'] = self._key.private_bytes(encoding = serialization.Encoding.PEM, format = serialization.PrivateFormat.PKCS8, encryption_algorithm = serialization.NoEncryption())
        return state

    
    def __setstate__(self, state):
        '''Pickle helper that deserializes the _key attribute.'''
        state['_key'] = serialization.load_pem_private_key(state['_key'], None)
        self.__dict__.update(state)
