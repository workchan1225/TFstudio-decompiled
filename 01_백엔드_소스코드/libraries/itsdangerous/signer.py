# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: signer.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as cabc
import hashlib
import hmac
import typing as t
from encoding import _base64_alphabet
from encoding import base64_decode
from encoding import base64_encode
from encoding import want_bytes
from exc import BadSignature

class SigningAlgorithm:
    '''Subclasses must implement :meth:`get_signature` to provide
    signature generation functionality.
    '''
    
    def get_signature(self = None, key = None, value = None):
        '''Returns the signature for the given key and value.'''
        raise NotImplementedError()

    
    def verify_signature(self = None, key = None, value = None, sig = ('key', 'bytes', 'value', 'bytes', 'sig', 'bytes', 'return', 'bool')):
        '''Verifies the given signature matches the expected
        signature.
        '''
        return hmac.compare_digest(sig, self.get_signature(key, value))



class NoneAlgorithm(SigningAlgorithm):
    '''Provides an algorithm that does not perform any signing and
    returns an empty signature.
    '''
    
    def get_signature(self = None, key = None, value = None):
        return b''



def _lazy_sha1(string = None):
    """Don't access ``hashlib.sha1`` until runtime. FIPS builds may not include
    SHA-1, in which case the import and use as a default would fail before the
    developer can configure something else.
    """
    return hashlib.sha1(string)


class HMACAlgorithm(SigningAlgorithm):
    '''Provides signature generation using HMACs.'''
    default_digest_method: 't.Any' = staticmethod(_lazy_sha1)
    
    def __init__(self = None, digest_method = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_signature(self = None, key = None, value = None):
        mac = hmac.new(key, msg = value, digestmod = self.digest_method)
        return mac.digest()



def _make_keys_list(secret_key = None):
