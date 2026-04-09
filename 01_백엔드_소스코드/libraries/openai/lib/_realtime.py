# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _realtime.pyc (Python 3.11)

from __future__ import annotations
import json
from typing_extensions import override
import httpx
from openai import _legacy_response
from openai._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from openai._utils import maybe_transform, async_maybe_transform
from openai._base_client import make_request_options
from openai.resources.realtime.calls import Calls, AsyncCalls
from openai.types.realtime.realtime_session_create_request_param import RealtimeSessionCreateRequestParam
__all__ = [
    '_Calls',
    '_AsyncCalls']

class _Calls(Calls):
    create = (lambda self = None, *, sdp: pass# WARNING: Decompyle incomplete
)()


class _AsyncCalls(AsyncCalls):
    create = (lambda self = None, *, sdp: pass# WARNING: Decompyle incomplete
)()
