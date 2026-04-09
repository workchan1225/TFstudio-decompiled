# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: coreerrors.pyc (Python 3.11)

'''Definitions of common exceptions for :mod:`sympy.core` module. '''

class BaseCoreError(Exception):
    '''Base class for core related exceptions. '''
    pass


class NonCommutativeExpression(BaseCoreError):
    """Raised when expression didn't have commutative property. """
    pass
