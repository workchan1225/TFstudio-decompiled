# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stash.pyc (Python 3.11)

from __future__ import annotations
from typing import Any
from typing import cast
from typing import Generic
from typing import TypeVar
__all__ = [
    'Stash',
    'StashKey']
T = TypeVar('T')
D = TypeVar('D')

def StashKey():
    '''StashKey'''
    __doc__ = '``StashKey`` is an object used as a key to a :class:`Stash`.\n\n    A ``StashKey`` is associated with the type ``T`` of the value of the key.\n\n    A ``StashKey`` is unique and cannot conflict with another key.\n\n    .. versionadded:: 7.0\n    '
    __slots__ = ()

StashKey = <NODE:27>(StashKey, 'StashKey', Generic[T])

class Stash:
    '''``Stash`` is a type-safe heterogeneous mutable mapping that
    allows keys and value types to be defined separately from
    where it (the ``Stash``) is created.

    Usually you will be given an object which has a ``Stash``, for example
    :class:`~pytest.Config` or a :class:`~_pytest.nodes.Node`:

    .. code-block:: python

        stash: Stash = some_object.stash

    If a module or plugin wants to store data in this ``Stash``, it creates
    :class:`StashKey`\\s for its keys (at the module level):

    .. code-block:: python

        # At the top-level of the module
        some_str_key = StashKey[str]()
        some_bool_key = StashKey[bool]()

    To store information:

    .. code-block:: python

        # Value type must match the key.
        stash[some_str_key] = "value"
        stash[some_bool_key] = True

    To retrieve the information:

    .. code-block:: python

        # The static type of some_str is str.
        some_str = stash[some_str_key]
        # The static type of some_bool is bool.
        some_bool = stash[some_bool_key]

    .. versionadded:: 7.0
    '''
    __slots__ = ('_storage',)
    
    def __init__(self = None):
        self._storage = { }

    
    def __setitem__(self = None, key = None, value = None):
        '''Set a value for key.'''
        self._storage[key] = value

    
    def __getitem__(self = None, key = None):
        """Get the value for key.

        Raises ``KeyError`` if the key wasn't set before.
        """
        return cast(T, self._storage[key])

    
    def get(self = None, key = None, default = None):
        """Get the value for key, or return default if the key wasn't set
        before."""
        
        try:
            return self[key]
        except KeyError:
            return 


    
    def setdefault(self = None, key = None, default = None):
        '''Return the value of key if already set, otherwise set the value
        of key to default and return default.'''
        
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return 


    
    def __delitem__(self = None, key = None):
        """Delete the value for key.

        Raises ``KeyError`` if the key wasn't set before.
        """
        del self._storage[key]

    
    def __contains__(self = None, key = None):
        '''Return whether key was set.'''
        return key in self._storage

    
    def __len__(self = None):
        '''Return how many items exist in the stash.'''
        return len(self._storage)
