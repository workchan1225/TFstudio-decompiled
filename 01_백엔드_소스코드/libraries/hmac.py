# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hmac.pyc (Python 3.11)

'''HMAC (Keyed-Hashing for Message Authentication) module.

Implements the HMAC algorithm as described by RFC 2104.
'''
import warnings as _warnings

try:
    import _hashlib as _hashopenssl
    compare_digest = _hashopenssl.compare_digest
    _functype = type(_hashopenssl.openssl_sha256)
except ImportError:
    _hashopenssl = None
    _functype = None
    from _operator import _compare_digest as compare_digest

import hashlib as _hashlib
trans_5C = (lambda .0: pass# WARNING: Decompyle incomplete
)(range(256)())
trans_36 = (lambda .0: pass# WARNING: Decompyle incomplete
)(range(256)())
digest_size = None

class HMAC:
    '''RFC 2104 HMAC class.  Also complies with RFC 4231.

    This supports the API for Cryptographic Hash Functions (PEP 247).
    '''
    blocksize = 64
    __slots__ = ('_hmac', '_inner', '_outer', 'block_size', 'digest_size')
    
    def __init__(self, key, msg, digestmod = (None, '')):
        '''Create a new HMAC object.

        key: bytes or buffer, key for the keyed hash object.
        msg: bytes or buffer, Initial input for the hash or None.
        digestmod: A hash name suitable for hashlib.new(). *OR*
                   A hashlib constructor returning a new hash object. *OR*
                   A module supporting PEP 247.

                   Required as of 3.8, despite its position after the optional
                   msg argument.  Passing it as a keyword argument is
                   recommended, though not required for legacy API reasons.
        '''
        if not isinstance(key, (bytes, bytearray)):
            raise TypeError('key: expected bytes or bytearray, but got %r' % type(key).__name__)
        if not digestmod:
            raise TypeError("Missing required argument 'digestmod'.")
        if _hashopenssl and isinstance(digestmod, (str, _functype)):
            
            try:
                self._init_hmac(key, msg, digestmod)
                return None
            except _hashopenssl.UnsupportedDigestmodError:
                self._init_old(key, msg, digestmod)
                return None
                self._init_old(key, msg, digestmod)
                return None


    
    def _init_hmac(self, key, msg, digestmod):
        self._hmac = _hashopenssl.hmac_new(key, msg, digestmod = digestmod)
        self.digest_size = self._hmac.digest_size
        self.block_size = self._hmac.block_size

    
    def _init_old(self, key, msg, digestmod):
        pass
    # WARNING: Decompyle incomplete

    name = (lambda self: if self._hmac:
self._hmac.namef'''{self._inner.name}''')()
    
    def update(self, msg):
