# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: key.pyc (Python 3.11)

'''RSA key generation code.

Create new keys with the newkeys() function. It will give you a PublicKey and a
PrivateKey object.

Loading and saving keys requires the pyasn1 module. This module is imported as
late as possible, such that other functionality will remain working in absence
of pyasn1.

.. note::

    Storing public and private keys via the `pickle` module is possible.
    However, it is insecure to load a key from an untrusted source.
    The pickle module is not secure against erroneous or maliciously
    constructed data. Never unpickle data received from an untrusted
    or unauthenticated source.

'''
import threading
import typing
import warnings
import rsa.prime as rsa
import rsa.pem as rsa
import rsa.common as rsa
import rsa.randnum as rsa
import rsa.core as rsa
DEFAULT_EXPONENT = 65537
T = typing.TypeVar('T', bound = 'AbstractKey')

class AbstractKey:
    '''Abstract superclass for private and public keys.'''
    __slots__ = ('n', 'e', 'blindfac', 'blindfac_inverse', 'mutex')
    
    def __init__(self = None, n = None, e = None):
        self.n = n
        self.e = e
        self.blindfac = -1
        self.blindfac_inverse = -1
        self.mutex = threading.Lock()

    _load_pkcs1_pem = (lambda cls = None, keyfile = None: pass)()
    _load_pkcs1_der = (lambda cls = None, keyfile = None: pass)()
    
    def _save_pkcs1_pem(self = None):
        '''Saves the key in PKCS#1 PEM format, implement in a subclass.

        :returns: the PEM-encoded key.
        :rtype: bytes
        '''
        pass

    
    def _save_pkcs1_der(self = None):
        '''Saves the key in PKCS#1 DER format, implement in a subclass.

        :returns: the DER-encoded key.
        :rtype: bytes
        '''
        pass

    load_pkcs1 = (lambda cls = None, keyfile = None, format = classmethod: methods = {
'PEM': cls._load_pkcs1_pem,
'DER': cls._load_pkcs1_der }method = cls._assert_format_exists(format, methods)method(keyfile))()
    _assert_format_exists = (lambda file_format = None, methods = None: try:
methods[file_format]except KeyError:
ex = Noneformats = ', '.join(sorted(methods.keys()))raise ValueError(f'''Unsupported format: {file_format!r}, try one of {formats!s}'''), exex = Nonedel ex)()
    
    def save_pkcs1(self = None, format = None):
        """Saves the key in PKCS#1 DER or PEM format.

        :param format: the format to save; 'PEM' or 'DER'
        :type format: str
        :returns: the DER- or PEM-encoded key.
        :rtype: bytes
        """
        methods = {
            'PEM': self._save_pkcs1_pem,
            'DER': self._save_pkcs1_der }
        method = self._assert_format_exists(format, methods)
        return method()

    
    def blind(self = None, message = None):
        '''Performs blinding on the message.

        :param message: the message, as integer, to blind.
        :param r: the random number to blind with.
        :return: tuple (the blinded message, the inverse of the used blinding factor)

        The blinding is such that message = unblind(decrypt(blind(encrypt(message))).

        See https://en.wikipedia.org/wiki/Blinding_%28cryptography%29
        '''
        (blindfac, blindfac_inverse) = self._update_blinding_factor()
        blinded = message * pow(blindfac, self.e, self.n) % self.n
        return (blinded, blindfac_inverse)

    
    def unblind(self = None, blinded = None, blindfac_inverse = None):
        """Performs blinding on the message using random number 'blindfac_inverse'.

        :param blinded: the blinded message, as integer, to unblind.
        :param blindfac: the factor to unblind with.
        :return: the original message.

        The blinding is such that message = unblind(decrypt(blind(encrypt(message))).

        See https://en.wikipedia.org/wiki/Blinding_%28cryptography%29
        """
        return blindfac_inverse * blinded % self.n

    
    def _initial_blinding_factor(self = None):
        for _ in range(1000):
            blind_r = rsa.randnum.randint(self.n - 1)
            if rsa.prime.are_relatively_prime(self.n, blind_r):
                
                return None, blind_r
            raise RuntimeError('unable to find blinding factor')

    
    def _update_blinding_factor(self = None):
        """Update blinding factors.

        Computing a blinding factor is expensive, so instead this function
        does this once, then updates the blinding factor as per section 9
        of 'A Timing Attack against RSA with the Chinese Remainder Theorem'
        by Werner Schindler.
        See https://tls.mbed.org/public/WSchindler-RSA_Timing_Attack.pdf

        :return: the new blinding factor and its inverse.
        """
        self.mutex
        if self.blindfac < 0:
            self.blindfac = self._initial_blinding_factor()
            self.blindfac_inverse = rsa.common.inverse(self.blindfac, self.n)
        else:
            self.blindfac = pow(self.blindfac, 2, self.n)
            self.blindfac_inverse = pow(self.blindfac_inverse, 2, self.n)
        None(None, None)
        return 
        with None:
            if not None, (self.blindfac, self.blindfac_inverse):
                pass



class PublicKey(AbstractKey):
    """Represents a public RSA key.

    This key is also known as the 'encryption key'. It contains the 'n' and 'e'
    values.

    Supports attributes as well as dictionary-like access. Attribute access is
    faster, though.

    >>> PublicKey(5, 3)
    PublicKey(5, 3)

    >>> key = PublicKey(5, 3)
    >>> key.n
    5
    >>> key['n']
    5
    >>> key.e
    3
    >>> key['e']
    3

    """
    __slots__ = ()
    
    def __getitem__(self = None, key = None):
        return getattr(self, key)

    
    def __repr__(self = None):
        return 'PublicKey(%i, %i)' % (self.n, self.e)

    
    def __getstate__(self = None):
        '''Returns the key as tuple for pickling.'''
        return (self.n, self.e)

    
    def __setstate__(self = None, state = None):
        '''Sets the key from tuple.'''
        (self.n, self.e) = state
        AbstractKey.__init__(self, self.n, self.e)

    
    def __eq__(self = None, other = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __ne__(self = None, other = None):
        return not (self == other)

    
    def __hash__(self = None):
        return hash((self.n, self.e))

    _load_pkcs1_der = (lambda cls = None, keyfile = None: decoder = decoderimport pyasn1.codec.derAsnPubKey = AsnPubKeyimport rsa.asn1(priv, _) = decoder.decode(keyfile, asn1Spec = AsnPubKey())cls(n = int(priv['modulus']), e = int(priv['publicExponent'])))()
    
    def _save_pkcs1_der(self = None):
        '''Saves the public key in PKCS#1 DER format.

        :returns: the DER-encoded public key.
        :rtype: bytes
        '''
        encoder = encoder
        import pyasn1.codec.der
        AsnPubKey = AsnPubKey
        import rsa.asn1
        asn_key = AsnPubKey()
        asn_key.setComponentByName('modulus', self.n)
        asn_key.setComponentByName('publicExponent', self.e)
        return encoder.encode(asn_key)

    _load_pkcs1_pem = (lambda cls = None, keyfile = None: der = rsa.pem.load_pem(keyfile, 'RSA PUBLIC KEY')cls._load_pkcs1_der(der))()
    
    def _save_pkcs1_pem(self = None):
        '''Saves a PKCS#1 PEM-encoded public key file.

        :return: contents of a PEM-encoded file that contains the public key.
        :rtype: bytes
        '''
        der = self._save_pkcs1_der()
        return rsa.pem.save_pem(der, 'RSA PUBLIC KEY')

    load_pkcs1_openssl_pem = (lambda cls = None, keyfile = None: der = rsa.pem.load_pem(keyfile, 'PUBLIC KEY')cls.load_pkcs1_openssl_der(der))()
    load_pkcs1_openssl_der = (lambda cls = None, keyfile = None: OpenSSLPubKey = OpenSSLPubKeyimport rsa.asn1decoder = decoderimport pyasn1.codec.deruniv = univimport pyasn1.type(keyinfo, _) = decoder.decode(keyfile, asn1Spec = OpenSSLPubKey())if keyinfo['header']['oid'] != univ.ObjectIdentifier('1.2.840.113549.1.1.1'):
raise TypeError('This is not a DER-encoded OpenSSL-compatible public key')cls._load_pkcs1_der(keyinfo['key'][1:]))()


class PrivateKey(AbstractKey):
    """Represents a private RSA key.

    This key is also known as the 'decryption key'. It contains the 'n', 'e',
    'd', 'p', 'q' and other values.

    Supports attributes as well as dictionary-like access. Attribute access is
    faster, though.

    >>> PrivateKey(3247, 65537, 833, 191, 17)
    PrivateKey(3247, 65537, 833, 191, 17)

    exp1, exp2 and coef will be calculated:

    >>> pk = PrivateKey(3727264081, 65537, 3349121513, 65063, 57287)
    >>> pk.exp1
    55063
    >>> pk.exp2
    10095
    >>> pk.coef
    50797

    """
    __slots__ = ('d', 'p', 'q', 'exp1', 'exp2', 'coef')
    
    def __init__(self, n, e = None, d = None, p = None, q = ('n', int, 'e', int, 'd', int, 'p', int, 'q', int, 'return', None)):
        AbstractKey.__init__(self, n, e)
        self.d = d
        self.p = p
        self.q = q
        self.exp1 = int(d % (p - 1))
        self.exp2 = int(d % (q - 1))
        self.coef = rsa.common.inverse(q, p)

    
    def __getitem__(self = None, key = None):
        return getattr(self, key)

    
    def __repr__(self = None):
        return 'PrivateKey(%i, %i, %i, %i, %i)' % (self.n, self.e, self.d, self.p, self.q)

    
    def __getstate__(self = None):
        '''Returns the key as tuple for pickling.'''
        return (self.n, self.e, self.d, self.p, self.q, self.exp1, self.exp2, self.coef)

    
    def __setstate__(self = None, state = None):
        '''Sets the key from tuple.'''
        (self.n, self.e, self.d, self.p, self.q, self.exp1, self.exp2, self.coef) = state
        AbstractKey.__init__(self, self.n, self.e)

    
    def __eq__(self = None, other = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __ne__(self = None, other = None):
        return not (self == other)

    
    def __hash__(self = None):
        return hash((self.n, self.e, self.d, self.p, self.q, self.exp1, self.exp2, self.coef))

    
    def blinded_decrypt(self = None, encrypted = None):
        '''Decrypts the message using blinding to prevent side-channel attacks.

        :param encrypted: the encrypted message
        :type encrypted: int

        :returns: the decrypted message
        :rtype: int
        '''
        (blinded, blindfac_inverse) = self.blind(encrypted)
        s1 = pow(blinded, self.exp1, self.p)
        s2 = pow(blinded, self.exp2, self.q)
        h = (s1 - s2) * self.coef % self.p
        decrypted = s2 + self.q * h
        return self.unblind(decrypted, blindfac_inverse)

    
    def blinded_encrypt(self = None, message = None):
        '''Encrypts the message using blinding to prevent side-channel attacks.

        :param message: the message to encrypt
        :type message: int

        :returns: the encrypted message
        :rtype: int
        '''
        (blinded, blindfac_inverse) = self.blind(message)
        encrypted = rsa.core.encrypt_int(blinded, self.d, self.n)
        return self.unblind(encrypted, blindfac_inverse)

    _load_pkcs1_der = (lambda cls = None, keyfile = None: decoder = decoderimport pyasn1.codec.der(priv, _) = decoder.decode(keyfile)if priv[0] != 0:
raise ValueError('Unable to read this file, version %s != 0' % priv[0])as_ints = map(int, priv[1:6])# WARNING: Decompyle incomplete
)()
    
    def _save_pkcs1_der(self = None):
        '''Saves the private key in PKCS#1 DER format.

        :returns: the DER-encoded private key.
        :rtype: bytes
        '''
        pass
    # WARNING: Decompyle incomplete

    _load_pkcs1_pem = (lambda cls = None, keyfile = None: der = rsa.pem.load_pem(keyfile, b'RSA PRIVATE KEY')cls._load_pkcs1_der(der))()
    
    def _save_pkcs1_pem(self = None):
        '''Saves a PKCS#1 PEM-encoded private key file.

        :return: contents of a PEM-encoded file that contains the private key.
        :rtype: bytes
        '''
        der = self._save_pkcs1_der()
        return rsa.pem.save_pem(der, b'RSA PRIVATE KEY')



def find_p_q(nbits = None, getprime_func = None, accurate = None):
    '''Returns a tuple of two different primes of nbits bits each.

    The resulting p * q has exactly 2 * nbits bits, and the returned p and q
    will not be equal.

    :param nbits: the number of bits in each of p and q.
    :param getprime_func: the getprime function, defaults to
        :py:func:`rsa.prime.getprime`.

        *Introduced in Python-RSA 3.1*

    :param accurate: whether to enable accurate mode or not.
    :returns: (p, q), where p > q

    >>> (p, q) = find_p_q(128)
    >>> from rsa import common
    >>> common.bit_size(p * q)
    256

    When not in accurate mode, the number of bits can be slightly less

    >>> (p, q) = find_p_q(128, accurate=False)
    >>> from rsa import common
    >>> common.bit_size(p * q) <= 256
    True
    >>> common.bit_size(p * q) > 240
    True

    '''
    pass
# WARNING: Decompyle incomplete


def calculate_keys_custom_exponent(p = None, q = None, exponent = None):
    """Calculates an encryption and a decryption key given p, q and an exponent,
    and returns them as a tuple (e, d)

    :param p: the first large prime
    :param q: the second large prime
    :param exponent: the exponent for the key; only change this if you know
        what you're doing, as the exponent influences how difficult your
        private key can be cracked. A very common choice for e is 65537.
    :type exponent: int

    """
    phi_n = (p - 1) * (q - 1)
    
    try:
        d = rsa.common.inverse(exponent, phi_n)
    except rsa.common.NotRelativePrimeError:
        ex = None
        raise rsa.common.NotRelativePrimeError(exponent, phi_n, ex.d, msg = 'e (%d) and phi_n (%d) are not relatively prime (divider=%i)' % (exponent, phi_n, ex.d)), ex
        ex = None
        del ex

    if exponent * d % phi_n != 1:
        raise ValueError('e (%d) and d (%d) are not mult. inv. modulo phi_n (%d)' % (exponent, d, phi_n))
    return (exponent, d)


def calculate_keys(p = None, q = None):
    '''Calculates an encryption and a decryption key given p and q, and
    returns them as a tuple (e, d)

    :param p: the first large prime
    :param q: the second large prime

    :return: tuple (e, d) with the encryption and decryption exponents.
    '''
    return calculate_keys_custom_exponent(p, q, DEFAULT_EXPONENT)


def gen_keys(nbits = None, getprime_func = None, accurate = None, exponent = (True, DEFAULT_EXPONENT)):
    """Generate RSA keys of nbits bits. Returns (p, q, e, d).

    Note: this can take a long time, depending on the key size.

    :param nbits: the total number of bits in ``p`` and ``q``. Both ``p`` and
        ``q`` will use ``nbits/2`` bits.
    :param getprime_func: either :py:func:`rsa.prime.getprime` or a function
        with similar signature.
    :param exponent: the exponent for the key; only change this if you know
        what you're doing, as the exponent influences how difficult your
        private key can be cracked. A very common choice for e is 65537.
    :type exponent: int
    """
    (p, q) = find_p_q(nbits // 2, getprime_func, accurate)
    
    try:
        (e, d) = calculate_keys_custom_exponent(p, q, exponent = exponent)
    except ValueError:
        pass

    continue
    return (p, q, e, d)


def newkeys(nbits = None, accurate = None, poolsize = None, exponent = (True, 1, DEFAULT_EXPONENT)):
    """Generates public and private keys, and returns them as (pub, priv).

    The public key is also known as the 'encryption key', and is a
    :py:class:`rsa.PublicKey` object. The private key is also known as the
    'decryption key' and is a :py:class:`rsa.PrivateKey` object.

    :param nbits: the number of bits required to store ``n = p*q``.
    :param accurate: when True, ``n`` will have exactly the number of bits you
        asked for. However, this makes key generation much slower. When False,
        `n`` may have slightly less bits.
    :param poolsize: the number of processes to use to generate the prime
        numbers. If set to a number > 1, a parallel algorithm will be used.
        This requires Python 2.6 or newer.
    :param exponent: the exponent for the key; only change this if you know
        what you're doing, as the exponent influences how difficult your
        private key can be cracked. A very common choice for e is 65537.
    :type exponent: int

    :returns: a tuple (:py:class:`rsa.PublicKey`, :py:class:`rsa.PrivateKey`)

    The ``poolsize`` parameter was added in *Python-RSA 3.1* and requires
    Python 2.6 or newer.

    """
    pass
# WARNING: Decompyle incomplete

__all__ = [
    'PublicKey',
    'PrivateKey',
    'newkeys']
if __name__ == '__main__':
    import doctest
    
    try:
        for count in range(100):
            (failures, tests) = doctest.testmod()
            if failures:
                pass
            elif count % 10 == 0 or count or count == 1:
                print('%i times' % count)
            print('Doctests done')
            return None
            except KeyboardInterrupt:
                print('Aborted')
                return None
            return None
