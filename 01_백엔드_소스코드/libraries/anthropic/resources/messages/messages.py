# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: messages.pyc (Python 3.11)

from __future__ import annotations
import warnings
from typing import Union, Iterable, Optional
from functools import partial
from typing_extensions import Literal, overload
import httpx
from  import _legacy_response
from types import ThinkingConfigParam, message_create_params, message_count_tokens_params
from batches import Batches, AsyncBatches, BatchesWithRawResponse, AsyncBatchesWithRawResponse, BatchesWithStreamingResponse, AsyncBatchesWithStreamingResponse
from _types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from _utils import is_given, required_args, maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _constants import DEFAULT_TIMEOUT, MODEL_NONSTREAMING_TOKENS
from _streaming import Stream, AsyncStream
from _base_client import make_request_options
from lib.streaming import MessageStreamManager, AsyncMessageStreamManager
from types.message import Message
from types.model_param import ModelParam
from types.message_param import MessageParam
from types.metadata_param import MetadataParam
from types.text_block_param import TextBlockParam
from types.tool_union_param import ToolUnionParam
from types.tool_choice_param import ToolChoiceParam
from types.message_tokens_count import MessageTokensCount
from types.thinking_config_param import ThinkingConfigParam
from types.raw_message_stream_event import RawMessageStreamEvent
from types.message_count_tokens_tool_param import MessageCountTokensToolParam
__all__ = [
    'Messages',
    'AsyncMessages']
DEPRECATED_MODELS = {
    'claude-1.3': 'November 6th, 2024',
    'claude-1.3-100k': 'November 6th, 2024',
    'claude-instant-1.1': 'November 6th, 2024',
    'claude-instant-1.1-100k': 'November 6th, 2024',
    'claude-instant-1.2': 'November 6th, 2024',
    'claude-3-sonnet-20240229': 'July 21st, 2025',
    'claude-3-opus-20240229': 'January 5th, 2026',
    'claude-2.1': 'July 21st, 2025',
    'claude-2.0': 'July 21st, 2025',
    'claude-3-7-sonnet-latest': 'February 19th, 2026',
    'claude-3-7-sonnet-20250219': 'February 19th, 2026' }

class Messages(SyncAPIResource):
    batches = (lambda self = None: Batches(self._client))()
    with_raw_response = (lambda self = None: MessagesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: MessagesWithStreamingResponse(self))()
    create = (lambda self = None, *, max_tokens: pass)()
    create = (lambda self = None, *, max_tokens: pass)()
    create = (lambda self = None, *, max_tokens: pass)()
    create = (lambda self = None, *, max_tokens:
