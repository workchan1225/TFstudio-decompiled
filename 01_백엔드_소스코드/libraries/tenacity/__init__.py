# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import dataclasses
import functools
import sys
import threading
import time
import typing as t
import warnings
from abc import ABC, abstractmethod
from concurrent import futures
from  import _utils
from retry import retry_base
from retry import retry_all
from retry import retry_always
from retry import retry_any
from retry import retry_if_exception
from retry import retry_if_exception_type
from retry import retry_if_exception_cause_type
from retry import retry_if_not_exception_type
from retry import retry_if_not_result
from retry import retry_if_result
from retry import retry_never
from retry import retry_unless_exception_type
from retry import retry_if_exception_message
from retry import retry_if_not_exception_message
from nap import sleep
from nap import sleep_using_event
from stop import stop_after_attempt
from stop import stop_after_delay
from stop import stop_before_delay
from stop import stop_all
from stop import stop_any
from stop import stop_never
from stop import stop_when_event_set
from wait import wait_chain
from wait import wait_combine
from wait import wait_exponential
from wait import wait_fixed
from wait import wait_incrementing
from wait import wait_none
from wait import wait_random
from wait import wait_random_exponential
from wait import wait_random_exponential as wait_full_jitter
from wait import wait_exponential_jitter
from before import before_log
from before import before_nothing
from after import after_log
from after import after_nothing
from before_sleep import before_sleep_log
from before_sleep import before_sleep_nothing

try:
    import tornado
except ImportError:
    tornado = None

if t.TYPE_CHECKING:
    import types
    from typing_extensions import Self
    from  import asyncio as tasyncio
    from retry import RetryBaseT
    from stop import StopBaseT
    from wait import WaitBaseT
WrappedFnReturnT = t.TypeVar('WrappedFnReturnT')
WrappedFn = t.TypeVar('WrappedFn', bound = t.Callable[(..., t.Any)])
dataclass_kwargs = { }
if sys.version_info >= (3, 10):
    dataclass_kwargs.update({
        'slots': True })
# WARNING: Decompyle incomplete
