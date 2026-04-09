# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: state_changes.pyc (Python 3.11)

'''State tracking utilities used by :class:`_orm.Session`.'''
from __future__ import annotations
import contextlib
from enum import Enum
from typing import Any
from typing import Callable
from typing import cast
from typing import Iterator
from typing import NoReturn
from typing import Optional
from typing import Tuple
from typing import TypeVar
from typing import Union
from  import exc as sa_exc
from  import util
from util.typing import Literal
_F = TypeVar('_F', bound = Callable[(..., Any)])

class _StateChangeState(Enum):
    pass


class _StateChangeStates(_StateChangeState):
    ANY = 1
    NO_CHANGE = 2
    CHANGE_IN_PROGRESS = 3


class _StateChange:
    '''Supplies state assertion decorators.

    The current use case is for the :class:`_orm.SessionTransaction` class. The
    :class:`_StateChange` class itself is agnostic of the
    :class:`_orm.SessionTransaction` class so could in theory be generalized
    for other systems as well.

    '''
    _next_state: '_StateChangeState' = _StateChangeStates.ANY
    _state: '_StateChangeState' = _StateChangeStates.NO_CHANGE
    _current_fn: 'Optional[Callable[..., Any]]' = None
    
    def _raise_for_prerequisite_state(self = None, operation_name = None, state = None):
        raise sa_exc.IllegalStateChangeError(f'''Can\'t run operation \'{operation_name}()\' when Session is in state {state!r}''', code = 'isce')

    declare_states = (lambda cls = None, prerequisite_states = None, moves_to = classmethod: pass# WARNING: Decompyle incomplete
)()
    _expect_state = (lambda self = None, expected = None: pass# WARNING: Decompyle incomplete
)()
