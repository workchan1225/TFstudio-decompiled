# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _typing.pyc (Python 3.11)

from typing import TypeVar, Protocol
T = TypeVar('T')

class RingElement(Protocol):
    '''A ring element.

    Must support ``+``, ``-``, ``*``, ``**`` and ``-``.
    '''
    
    def __add__(self = None, other = None):
        pass

    
    def __sub__(self = None, other = None):
        pass

    
    def __mul__(self = None, other = None):
        pass

    
    def __pow__(self = None, other = None):
        pass

    
    def __neg__(self = None):
        pass
