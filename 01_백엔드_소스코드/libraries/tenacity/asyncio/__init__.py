# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import functools
import sys
import typing as t
import tenacity
from tenacity import AttemptManager
from tenacity import BaseRetrying
from tenacity import DoAttempt
from tenacity import DoSleep
from tenacity import RetryCallState
from tenacity import RetryError
from tenacity import after_nothing
from tenacity import before_nothing
from tenacity import _utils
from retry import RetryBaseT
from retry import retry_all
from retry import retry_any
from retry import retry_if_exception
from retry import retry_if_result
from retry import RetryBaseT as SyncRetryBaseT
if t.TYPE_CHECKING:
    from tenacity.stop import StopBaseT
    from tenacity.wait import WaitBaseT
WrappedFnReturnT = t.TypeVar('WrappedFnReturnT')
WrappedFn = t.TypeVar('WrappedFn', bound = t.Callable[(..., t.Awaitable[t.Any])])

def _portable_async_sleep(seconds = None):
