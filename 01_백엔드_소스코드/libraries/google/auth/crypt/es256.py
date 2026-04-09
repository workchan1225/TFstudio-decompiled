# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: es256.pyc (Python 3.11)

'''ECDSA (ES256) verifier and signer that use the ``cryptography`` library.
'''
from cryptography import utils
import cryptography.exceptions as cryptography
from cryptography.hazmat import backends
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature
from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature
import cryptography.x509 as cryptography
from google.auth import _helpers
from google.auth.crypt import base
_CERTIFICATE_MARKER = b'-----BEGIN CERTIFICATE-----'
_BACKEND = backends.default_backend()
_PADDING = padding.PKCS1v15()

class ES256Verifier(base.Verifier):
    '''Verifies ECDSA cryptographic signatures using public keys.

    Args:
        public_key (
                cryptography.hazmat.primitives.asymmetric.ec.ECDSAPublicKey):
            The public key used to verify signatures.
    '''
    
    def __init__(self, public_key):
        self._pubkey = public_key

    verify = (lambda self, message, signature: sig_bytes = _helpers.to_bytes(signature)if len(sig_bytes) != 64:
Falser = int.from_bytes(sig_bytes[:32], byteorder = 'big') if None.is_python_3() else utils.int_from_bytes(sig_bytes[:32], byteorder = 'big')s = int.from_bytes(sig_bytes[32:], byteorder = 'big') if _helpers.is_python_3() else utils.int_from_bytes(sig_bytes[32:], byteorder = 'big')asn1_sig = encode_dss_signature(r, s)message = _helpers.to_bytes(message)try:
self._pubkey.verify(asn1_sig, message, ec.ECDSA(hashes.SHA256()))Trueexcept (ValueError, cryptography.exceptions.InvalidSignature):
False)()
    from_string = (lambda cls, public_key: public_key_data = _helpers.to_bytes(public_key)if _CERTIFICATE_MARKER in public_key_data:
cert = cryptography.x509.load_pem_x509_certificate(public_key_data, _BACKEND)pubkey = cert.public_key()else:
pubkey = serialization.load_pem_public_key(public_key_data, _BACKEND)cls(pubkey))()


class ES256Signer(base.FromServiceAccountMixin, base.Signer):
    '''Signs messages with an ECDSA private key.

    Args:
        private_key (
                cryptography.hazmat.primitives.asymmetric.ec.ECDSAPrivateKey):
            The private key to sign with.
        key_id (str): Optional key ID used to identify this private key. This
            can be useful to associate the private key with its associated
            public key or certificate.
    '''
    
    def __init__(self, private_key, key_id = (None,)):
        self._key = private_key
        self._key_id = key_id

    key_id = (lambda self: self._key_id)()()
    sign = (lambda self, message: message = _helpers.to_bytes(message)asn1_signature = self._key.sign(message, ec.ECDSA(hashes.SHA256()))(r, s) = decode_dss_signature(asn1_signature)r.to_bytes(32, byteorder = 'big') + s.to_bytes(32, byteorder = 'big') if _helpers.is_python_3() else utils.int_to_bytes(r, 32) + utils.int_to_bytes(s, 32))()
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
