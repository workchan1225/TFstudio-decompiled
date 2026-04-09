# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: completions.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, overload
import httpx
from  import _legacy_response
from types import completion_create_params
from _types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from _utils import required_args, maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _streaming import Stream, AsyncStream
from _base_client import make_request_options
from types.completion import Completion
from types.chat.chat_completion_stream_options_param import ChatCompletionStreamOptionsParam
__all__ = [
    'Completions',
    'AsyncCompletions']

class Completions(SyncAPIResource):
    with_raw_response = (lambda self = None: CompletionsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: CompletionsWithStreamingResponse(self))()
    create = (lambda self = None, *, model: pass)()
    create = (lambda self = None, *, model: pass)()
    create = (lambda self = None, *, model: pass)()
    create = (lambda self = None, *, model: pass# WARNING: Decompyle incomplete
)()


class AsyncCompletions(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncCompletionsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncCompletionsWithStreamingResponse(self))()
    create = (lambda self = None, *, model: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, model: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, model: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, model: pass# WARNING: Decompyle incomplete
)()


class CompletionsWithRawResponse:
    
    def __init__(self = None, completions = None):
        self._completions = completions
        self.create = _legacy_response.to_raw_response_wrapper(completions.create)



class AsyncCompletionsWithRawResponse:
    
    def __init__(self = None, completions = None):
        self._completions = completions
        self.create = _legacy_response.async_to_raw_response_wrapper(completions.create)



class CompletionsWithStreamingResponse:
    
    def __init__(self = None, completions = None):
        self._completions = completions
        self.create = to_streamed_response_wrapper(completions.create)



class AsyncCompletionsWithStreamingResponse:
    
    def __init__(self = None, completions = None):
        self._completions = completions
        self.create = async_to_streamed_response_wrapper(completions.create)
