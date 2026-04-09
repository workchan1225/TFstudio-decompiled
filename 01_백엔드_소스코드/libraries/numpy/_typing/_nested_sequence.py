# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _nested_sequence.pyc (Python 3.11)

'''A module containing the `_NestedSequence` protocol.'''
from __future__ import annotations
from collections.abc import Iterator
from typing import Any, TypeVar, Protocol, runtime_checkable
__all__ = [
    '_NestedSequence']
_T_co = TypeVar('_T_co', covariant = True)

def _NestedSequence():
    '''_NestedSequence'''
    __doc__ = 'A protocol for representing nested sequences.\n\n    Warning\n    -------\n    `_NestedSequence` currently does not work in combination with typevars,\n    *e.g.* ``def func(a: _NestedSequnce[T]) -> T: ...``.\n\n    See Also\n    --------\n    collections.abc.Sequence\n        ABCs for read-only and mutable :term:`sequences`.\n\n    Examples\n    --------\n    .. code-block:: python\n\n        >>> from __future__ import annotations\n\n        >>> from typing import TYPE_CHECKING\n        >>> import numpy as np\n        >>> from numpy._typing import _NestedSequence\n\n        >>> def get_dtype(seq: _NestedSequence[float]) -> np.dtype[np.float64]:\n        ...     return np.asarray(seq).dtype\n\n        >>> a = get_dtype([1.0])\n        >>> b = get_dtype([[1.0]])\n        >>> c = get_dtype([[[1.0]]])\n        >>> d = get_dtype([[[[1.0]]]])\n\n        >>> if TYPE_CHECKING:\n        ...     reveal_locals()\n        ...     # note: Revealed local types are:\n        ...     # note:     a: numpy.dtype[numpy.floating[numpy._typing._64Bit]]\n        ...     # note:     b: numpy.dtype[numpy.floating[numpy._typing._64Bit]]\n        ...     # note:     c: numpy.dtype[numpy.floating[numpy._typing._64Bit]]\n        ...     # note:     d: numpy.dtype[numpy.floating[numpy._typing._64Bit]]\n\n    '
    
    def __len__(self = None):
        '''Implement ``len(self)``.'''
        raise NotImplementedError

    
    def __getitem__(self = None, index = None):
        '''Implement ``self[x]``.'''
        raise NotImplementedError

    
    def __contains__(self = None, x = None):
        '''Implement ``x in self``.'''
        raise NotImplementedError

    
    def __iter__(self = None):
        '''Implement ``iter(self)``.'''
        raise NotImplementedError

    
    def __reversed__(self = None):
        '''Implement ``reversed(self)``.'''
        raise NotImplementedError

    
    def count(self = None, value = None):
        '''Return the number of occurrences of `value`.'''
        raise NotImplementedError

    
    def index(self = None, value = None):
        '''Return the first index of `value`.'''
        raise NotImplementedError


_NestedSequence = <NODE:27>(_NestedSequence, '_NestedSequence', Protocol[_T_co])()
