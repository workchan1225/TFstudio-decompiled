# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: identity.pyc (Python 3.11)

from __future__ import annotations
from typing import Any
from typing import cast
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import NoReturn
from typing import Optional
from typing import Set
from typing import Tuple
from typing import TYPE_CHECKING
from typing import TypeVar
import weakref
from  import util as orm_util
from  import exc as sa_exc
if TYPE_CHECKING:
    from _typing import _IdentityKeyType
    from state import InstanceState
_T = TypeVar('_T', bound = Any)
_O = TypeVar('_O', bound = object)

class IdentityMap:
    _modified: 'Set[InstanceState[Any]]' = 'IdentityMap'
    
    def __init__(self = None):
        self._dict = { }
        self._modified = set()
        self._wr = weakref.ref(self)

    
    def _kill(self = None):
        self._add_unpresent = _killed

    
    def all_states(self = None):
        raise NotImplementedError()

    
    def contains_state(self = None, state = None):
        raise NotImplementedError()

    
    def __contains__(self = None, key = None):
        raise NotImplementedError()

    
    def safe_discard(self = None, state = None):
        raise NotImplementedError()

    
    def __getitem__(self = None, key = None):
        raise NotImplementedError()

    
    def get(self = None, key = None, default = None):
        raise NotImplementedError()

    
    def fast_get_state(self = None, key = None):
        raise NotImplementedError()

    
    def keys(self = None):
        return self._dict.keys()

    
    def values(self = None):
        raise NotImplementedError()

    
    def replace(self = None, state = None):
        raise NotImplementedError()

    
    def add(self = None, state = None):
        raise NotImplementedError()

    
    def _fast_discard(self = None, state = None):
        raise NotImplementedError()

    
    def _add_unpresent(self = None, state = None, key = None):
        """optional inlined form of add() which can assume item isn't present
        in the map"""
        self.add(state)

    
    def _manage_incoming_state(self = None, state = None):
        state._instance_dict = self._wr
        if state.modified:
            self._modified.add(state)
            return None

    
    def _manage_removed_state(self = None, state = None):
        del state._instance_dict
        if state.modified:
            self._modified.discard(state)
            return None

    
    def _dirty_states(self = None):
        return self._modified

    
    def check_modified(self = None):
        """return True if any InstanceStates present have been marked
        as 'modified'.

        """
        return bool(self._modified)

    
    def has_key(self = None, key = None):
        return key in self

    
    def __len__(self = None):
        return len(self._dict)



class WeakInstanceDict(IdentityMap):
    _dict: 'Dict[_IdentityKeyType[Any], InstanceState[Any]]' = 'WeakInstanceDict'
    
    def __getitem__(self = None, key = None):
        state = cast('InstanceState[_O]', self._dict[key])
        o = state.obj()
    # WARNING: Decompyle incomplete

    
    def __contains__(self = None, key = None):
        
        try:
            if key in self._dict:
                state = self._dict[key]
                o = state.obj()
            else:
                return False
            return o is not None
        except KeyError:
            return False


    
    def contains_state(self = None, state = None):
        pass
    # WARNING: Decompyle incomplete

    
    def replace(self = None, state = None):
        pass
    # WARNING: Decompyle incomplete

    
    def add(self = None, state = None):
        key = state.key
    # WARNING: Decompyle incomplete

    
    def _add_unpresent(self = None, state = None, key = None):
        self._dict[key] = state
        state._instance_dict = self._wr

    
    def fast_get_state(self = None, key = None):
        return self._dict.get(key)

    
    def get(self = None, key = None, default = None):
        if key not in self._dict:
            return default
    # WARNING: Decompyle incomplete

    
    def items(self = None):
        values = self.all_states()
        result = []
    # WARNING: Decompyle incomplete

    
    def values(self = None):
        values = self.all_states()
        result = []
    # WARNING: Decompyle incomplete

    
    def __iter__(self = None):
        return iter(self.keys())

    
    def all_states(self = None):
        return list(self._dict.values())

    
    def _fast_discard(self = None, state = None):
        key = state.key
    # WARNING: Decompyle incomplete

    
    def discard(self = None, state = None):
        self.safe_discard(state)

    
    def safe_discard(self = None, state = None):
        key = state.key
    # WARNING: Decompyle incomplete



def _killed(state = None, key = None):
    raise sa_exc.InvalidRequestError("Object %s cannot be converted to 'persistent' state, as this identity map is no longer valid.  Has the owning Session been closed?" % orm_util.state_str(state), code = 'lkrp')
