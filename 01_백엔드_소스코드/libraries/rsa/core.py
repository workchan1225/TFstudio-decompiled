# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: core.pyc (Python 3.11)

'''Core mathematical operations.

This is the actual core RSA implementation, which is only defined
mathematically on integers.
'''

def assert_int(var = None, name = None):
    if isinstance(var, int):
        return None
    raise None(f'''{name!s} should be an integer, not {var.__class__!s}''')


def encrypt_int(message = None, ekey = None, n = None):
    """Encrypts a message using encryption key 'ekey', working modulo n"""
    assert_int(message, 'message')
    assert_int(ekey, 'ekey')
    assert_int(n, 'n')
    if message < 0:
        raise ValueError('Only non-negative numbers are supported')
    if message > n:
        raise OverflowError('The message %i is too long for n=%i' % (message, n))
    return pow(message, ekey, n)


def decrypt_int(cyphertext = None, dkey = None, n = None):
    """Decrypts a cypher text using the decryption key 'dkey', working modulo n"""
    assert_int(cyphertext, 'cyphertext')
    assert_int(dkey, 'dkey')
    assert_int(n, 'n')
    message = pow(cyphertext, dkey, n)
    return message
