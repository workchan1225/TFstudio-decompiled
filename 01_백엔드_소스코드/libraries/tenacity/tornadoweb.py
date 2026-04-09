# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tornadoweb.pyc (Python 3.11)

import sys
import typing
from tenacity import BaseRetrying
from tenacity import DoAttempt
from tenacity import DoSleep
from tenacity import RetryCallState
from tornado import gen
if typing.TYPE_CHECKING:
    from tornado.concurrent import Future
_RetValT = typing.TypeVar('_RetValT')

class TornadoRetrying(BaseRetrying):
    pass
# WARNING: Decompyle incomplete
