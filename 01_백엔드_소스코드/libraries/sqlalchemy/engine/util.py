# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from __future__ import annotations
import typing
from typing import Any
from typing import Callable
from typing import Optional
from typing import TypeVar
from  import exc
from  import util
from util._has_cy import HAS_CYEXTENSION
from util.typing import Protocol
from util.typing import Self
if not typing.TYPE_CHECKING or HAS_CYEXTENSION:
    from _py_util import _distill_params_20
    from _py_util import _distill_raw_params
else:
    from sqlalchemy.cyextension.util import _distill_params_20
    from sqlalchemy.cyextension.util import _distill_raw_params
_C = TypeVar('_C', bound = Callable[([], Any)])

def connection_memoize(key = None):
    '''Decorator, memoize a function in a connection.info stash.

    Only applicable to functions which take no arguments other than a
    connection.  The memo will be stored in ``connection.info[key]``.
    '''
    pass
# WARNING: Decompyle incomplete


class _TConsSubject(Protocol):
    _trans_context_manager: 'Optional[TransactionalContext]' = '_TConsSubject'


class TransactionalContext:
    '''Apply Python context manager behavior to transaction objects.

    Performs validation to ensure the subject of the transaction is not
    used if the transaction were ended prematurely.

    '''
    _trans_subject: 'Optional[_TConsSubject]' = ('_outer_trans_ctx', '_trans_subject', '__weakref__')
    
    def _transaction_is_active(self = None):
        raise NotImplementedError()

    
    def _transaction_is_closed(self = None):
        raise NotImplementedError()

    
    def _rollback_can_be_called(self = None):
        """indicates the object is in a state that is known to be acceptable
        for rollback() to be called.

        This does not necessarily mean rollback() will succeed or not raise
        an error, just that there is currently no state detected that indicates
        rollback() would fail or emit warnings.

        It also does not mean that there's a transaction in progress, as
        it is usually safe to call rollback() even if no transaction is
        present.

        .. versionadded:: 1.4.28

        """
        raise NotImplementedError()

    
    def _get_subject(self = None):
        raise NotImplementedError()

    
    def commit(self = None):
        raise NotImplementedError()

    
    def rollback(self = None):
        raise NotImplementedError()

    
    def close(self = None):
        raise NotImplementedError()

    _trans_ctx_check = (lambda cls = None, subject = None: trans_context = subject._trans_context_managerif not trans_context or trans_context._transaction_is_active():
raise exc.InvalidRequestError("Can't operate on closed transaction inside context manager.  Please complete the context manager before emitting further commands.")None)()
    
    def __enter__(self = None):
        subject = self._get_subject()
        trans_context = subject._trans_context_manager
        self._outer_trans_ctx = trans_context
        self._trans_subject = subject
        subject._trans_context_manager = self
        return self

    
    def __exit__(self = None, type_ = None, value = None, traceback = ('type_', 'Any', 'value', 'Any', 'traceback', 'Any', 'return', 'None')):
        subject = getattr(self, '_trans_subject', None)
    # WARNING: Decompyle incomplete
