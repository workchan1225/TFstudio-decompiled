# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _convertions.pyc (Python 3.11)

'''
A set of methods retained from np.compat module that
are still used across codebase.
'''
__all__ = [
    'asunicode',
    'asbytes']

def asunicode(s):
    if isinstance(s, bytes):
        return s.decode('latin1')
    return None(s)


def asbytes(s):
    if isinstance(s, bytes):
        return s
    return None(s).encode('latin1')
