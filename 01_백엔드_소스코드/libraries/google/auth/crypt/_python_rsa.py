# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _python_rsa.pyc (Python 3.11)

'''Pure-Python RSA cryptography implementation.

Uses the ``rsa``, ``pyasn1`` and ``pyasn1_modules`` packages
to parse PEM files storing PKCS#1 or PKCS#8 keys as well as
certificates. There is no support for p12 files.
'''
from __future__ import absolute_import
import io
from pyasn1.codec.der import decoder
from pyasn1_modules import pem
from pyasn1_modules.rfc2459 import Certificate
from pyasn1_modules.rfc5208 import PrivateKeyInfo
import rsa
from google.auth import _helpers
from google.auth import exceptions
from google.auth.crypt import base
_POW2 = (128, 64, 32, 16, 8, 4, 2, 1)
_CERTIFICATE_MARKER = b'-----BEGIN CERTIFICATE-----'
_PKCS1_MARKER = ('-----BEGIN RSA PRIVATE KEY-----', '-----END RSA PRIVATE KEY-----')
_PKCS8_MARKER = ('-----BEGIN PRIVATE KEY-----', '-----END PRIVATE KEY-----')
_PKCS8_SPEC = PrivateKeyInfo()

def _bit_list_to_bytes(bit_list):
    '''Converts an iterable of 1s and 0s to bytes.

    Combines the list 8 at a time, treating each group of 8 bits
    as a single byte.

    Args:
        bit_list (Sequence): Sequence of 1s and 0s.

    Returns:
        bytes: The decoded bytes.
    '''
    num_bits = len(bit_list)
    byte_vals = bytearray()
    for start in range(0, num_bits, 8):
        curr_bits = bit_list[start:start + 8]
        char_val = (lambda .0: pass# WARNING: Decompyle incomplete
)(zip(_POW2, curr_bits)())
        byte_vals.append(char_val)
        return bytes(byte_vals)


class RSAVerifier(base.Verifier):
    '''Verifies RSA cryptographic signatures using public keys.

    Args:
        public_key (rsa.key.PublicKey): The public key used to verify
            signatures.
    '''
    
    def __init__(self, public_key):
        self._pubkey = public_key

    verify = (lambda self, message, signature: message = _helpers.to_bytes(message)try:
rsa.pkcs1.verify(message, signature, self._pubkey)except (ValueError, rsa.pkcs1.VerificationError):
False)()
    from_string = (lambda cls, public_key: public_key = _helpers.to_bytes(public_key)is_x509_cert = _CERTIFICATE_MARKER in public_keyif is_x509_cert:
der = rsa.pem.load_pem(public_key, 'CERTIFICATE')(asn1_cert, remaining) = decoder.decode(der, asn1Spec = Certificate())if remaining != b'':
raise exceptions.InvalidValue('Unused bytes', remaining)cert_info = asn1_cert['tbsCertificate']['subjectPublicKeyInfo']key_bytes = _bit_list_to_bytes(cert_info['subjectPublicKey'])pubkey = rsa.PublicKey.load_pkcs1(key_bytes, 'DER')else:
pubkey = rsa.PublicKey.load_pkcs1(public_key, 'PEM')cls(pubkey))()


class RSASigner(base.FromServiceAccountMixin, base.Signer):
    '''Signs messages with an RSA private key.

    Args:
        private_key (rsa.key.PrivateKey): The private key to sign with.
        key_id (str): Optional key ID used to identify this private key. This
            can be useful to associate the private key with its associated
            public key or certificate.
    '''
    
    def __init__(self, private_key, key_id = (None,)):
        self._key = private_key
        self._key_id = key_id

    key_id = (lambda self: self._key_id)()()
    sign = (lambda self, message: message = _helpers.to_bytes(message)rsa.pkcs1.sign(message, self._key, 'SHA-256'))()
    from_string = (lambda cls, key, key_id = (None,): key = _helpers.from_bytes(key)(marker_id, key_bytes) = pem.readPemBlocksFromFile(io.StringIO(key), _PKCS1_MARKER, _PKCS8_MARKER)if marker_id == 0:
private_key = rsa.key.PrivateKey.load_pkcs1(key_bytes, format = 'DER')elif marker_id == 1:
(key_info, remaining) = decoder.decode(key_bytes, asn1Spec = _PKCS8_SPEC)if remaining != b'':
raise exceptions.InvalidValue('Unused bytes', remaining)private_key_info = key_info.getComponentByName('privateKey')private_key = rsa.key.PrivateKey.load_pkcs1(private_key_info.asOctets(), format = 'DER')else:
raise exceptions.MalformedError('No key could be detected.')cls(private_key, key_id = key_id))()
