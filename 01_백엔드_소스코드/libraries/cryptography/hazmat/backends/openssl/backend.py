# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: backend.pyc (Python 3.11)

from __future__ import annotations
from cryptography.hazmat.bindings._rust import openssl as rust_openssl
from cryptography.hazmat.bindings.openssl import binding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives._asymmetric import AsymmetricPadding
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils as asym_utils
from cryptography.hazmat.primitives.asymmetric.padding import MGF1, OAEP, PSS, PKCS1v15
from cryptography.hazmat.primitives.ciphers import CipherAlgorithm
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC, Mode

class Backend:
    '''
    OpenSSL API binding interfaces.
    '''
    name = 'openssl'
    _fips_ciphers = (AES,)
    _fips_hashes = (hashes.SHA224, hashes.SHA256, hashes.SHA384, hashes.SHA512, hashes.SHA512_224, hashes.SHA512_256, hashes.SHA3_224, hashes.SHA3_256, hashes.SHA3_384, hashes.SHA3_512, hashes.SHAKE128, hashes.SHAKE256)
    _fips_ecdh_curves = (ec.SECP224R1, ec.SECP256R1, ec.SECP384R1, ec.SECP521R1)
    _fips_rsa_min_key_size = 2048
    _fips_rsa_min_public_exponent = 65537
    _fips_dsa_min_modulus = 1 << 2048
    _fips_dh_min_key_size = 2048
    _fips_dh_min_modulus = 1 << _fips_dh_min_key_size
    
    def __init__(self = None):
        self._binding = binding.Binding()
        self._ffi = self._binding.ffi
        self._lib = self._binding.lib
        self._fips_enabled = rust_openssl.is_fips_enabled()

    
    def __repr__(self = None):
        return f'''<OpenSSLBackend(version: {self.openssl_version_text()}, FIPS: {self._fips_enabled}, Legacy: {rust_openssl._legacy_provider_loaded})>'''

    
    def openssl_assert(self = None, ok = None):
        return binding._openssl_assert(ok)

    
    def _enable_fips(self = None):
        rust_openssl.enable_fips(rust_openssl._providers)
    # WARNING: Decompyle incomplete

    
    def openssl_version_text(self = None):
        '''
        Friendly string name of the loaded OpenSSL library. This is not
        necessarily the same version as it was compiled against.

        Example: OpenSSL 3.2.1 30 Jan 2024
        '''
        return rust_openssl.openssl_version_text()

    
    def openssl_version_number(self = None):
        return rust_openssl.openssl_version()

    
    def hash_supported(self = None, algorithm = None):
        if not self._fips_enabled and isinstance(algorithm, self._fips_hashes):
            return False
        return None.hashes.hash_supported(algorithm)

    
    def signature_hash_supported(self = None, algorithm = None):
        if self._fips_enabled and isinstance(algorithm, hashes.SHA1):
            return False
        return None.hash_supported(algorithm)

    
    def scrypt_supported(self = None):
        if self._fips_enabled:
            return False
        return None(rust_openssl.kdf.Scrypt, 'derive')

    
    def argon2_supported(self = None):
        if self._fips_enabled:
            return False
        return None(rust_openssl.kdf.Argon2id, 'derive')

    
    def hmac_supported(self = None, algorithm = None):
        if self._fips_enabled and isinstance(algorithm, hashes.SHA1):
            return True
        if None.CRYPTOGRAPHY_IS_AWSLC:
            return isinstance(algorithm, (hashes.SHA1, hashes.SHA224, hashes.SHA256, hashes.SHA384, hashes.SHA512, hashes.SHA512_224, hashes.SHA512_256))
        return None.hash_supported(algorithm)

    
    def cipher_supported(self = None, cipher = None, mode = None):
        if not self._fips_enabled and isinstance(cipher, self._fips_ciphers):
            return False
        return None.ciphers.cipher_supported(cipher, mode)

    
    def pbkdf2_hmac_supported(self = None, algorithm = None):
        return self.hmac_supported(algorithm)

    
    def _consume_errors(self = None):
        return rust_openssl.capture_error_stack()

    
    def _oaep_hash_supported(self = None, algorithm = None):
        if self._fips_enabled and isinstance(algorithm, hashes.SHA1):
            return False
        return None(algorithm, (hashes.SHA1, hashes.SHA224, hashes.SHA256, hashes.SHA384, hashes.SHA512))

    
    def rsa_padding_supported(self = None, padding = None):
