# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: prime.pyc (Python 3.11)

'''Numerical functions related to primes.

Implementation based on the book Algorithm Design by Michael T. Goodrich and
Roberto Tamassia, 2002.
'''
import rsa.common as rsa
import rsa.randnum as rsa
__all__ = [
    'getprime',
    'are_relatively_prime']

def gcd(p = None, q = None):
    '''Returns the greatest common divisor of p and q

    >>> gcd(48, 180)
    12
    '''
    pass
# WARNING: Decompyle incomplete


def get_primality_testing_rounds(number = None):
    '''Returns minimum number of rounds for Miller-Rabing primality testing,
    based on number bitsize.

    According to NIST FIPS 186-4, Appendix C, Table C.3, minimum number of
    rounds of M-R testing, using an error probability of 2 ** (-100), for
    different p, q bitsizes are:
      * p, q bitsize: 512; rounds: 7
      * p, q bitsize: 1024; rounds: 4
      * p, q bitsize: 1536; rounds: 3
    See: http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf
    '''
    bitsize = rsa.common.bit_size(number)
    if bitsize >= 1536:
        return 3
    if None >= 1024:
        return 4
    if None >= 512:
        return 7


def miller_rabin_primality_testing(n = None, k = None):
    """Calculates whether n is composite (which is always correct) or prime
    (which theoretically is incorrect with error probability 4**-k), by
    applying Miller-Rabin primality testing.

    For reference and implementation example, see:
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

    :param n: Integer to be tested for primality.
    :type n: int
    :param k: Number of rounds (witnesses) of Miller-Rabin testing.
    :type k: int
    :return: False if the number is composite, True if it's probably prime.
    :rtype: bool
    """
    if n < 2:
        return False
    d = None - 1
    r = 0
# WARNING: Decompyle incomplete


def is_prime(number = None):
    '''Returns True if the number is prime, and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(42)
    False
    >>> is_prime(41)
    True
    '''
    if number < 10:
        return number in frozenset({2, 3, 5, 7})
    if not None & 1:
        return False
    k = None(number)
    return miller_rabin_primality_testing(number, k + 1)


def getprime(nbits = None):
    """Returns a prime number that can be stored in 'nbits' bits.

    >>> p = getprime(128)
    >>> is_prime(p-1)
    False
    >>> is_prime(p)
    True
    >>> is_prime(p+1)
    False

    >>> from rsa import common
    >>> common.bit_size(p) == 128
    True
    """
    pass
# WARNING: Decompyle incomplete


def are_relatively_prime(a = None, b = None):
    '''Returns True if a and b are relatively prime, and False if they
    are not.

    >>> are_relatively_prime(2, 3)
    True
    >>> are_relatively_prime(2, 4)
    False
    '''
    d = gcd(a, b)
    return d == 1

if __name__ == '__main__':
    print('Running doctests 1000x or until failure')
    import doctest
    for count in range(1000):
        (failures, tests) = doctest.testmod()
        if failures:
            pass
        elif count % 100 == 0 and count:
            print('%i times' % count)
        print('Doctests done')
        return None
        return None
