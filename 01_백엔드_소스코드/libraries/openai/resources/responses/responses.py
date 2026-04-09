# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: responses.pyc (Python 3.11)

from __future__ import annotations
from copy import copy
from typing import Any, List, Type, Union, Iterable, Optional, cast
from functools import partial
from typing_extensions import Literal, overload
import httpx
from  import _legacy_response
from _types import NOT_GIVEN, Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from _utils import is_given, maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from input_items import InputItems, AsyncInputItems, InputItemsWithRawResponse, AsyncInputItemsWithRawResponse, InputItemsWithStreamingResponse, AsyncInputItemsWithStreamingResponse
from _streaming import Stream, AsyncStream
from lib._tools import PydanticFunctionTool, ResponsesPydanticFunctionTool
from input_tokens import InputTokens, AsyncInputTokens, InputTokensWithRawResponse, AsyncInputTokensWithRawResponse, InputTokensWithStreamingResponse, AsyncInputTokensWithStreamingResponse
from _base_client import make_request_options
from types.responses import response_create_params, response_compact_params, response_retrieve_params
from lib._parsing._responses import TextFormatT, parse_response, type_to_text_format_param as _type_to_text_format_param
from types.responses.response import Response
from types.responses.tool_param import ToolParam, ParseableToolParam
from types.shared_params.metadata import Metadata
from types.shared_params.reasoning import Reasoning
from types.responses.parsed_response import ParsedResponse
from lib.streaming.responses._responses import ResponseStreamManager, AsyncResponseStreamManager
from types.responses.compacted_response import CompactedResponse
from types.responses.response_includable import ResponseIncludable
from types.shared_params.responses_model import ResponsesModel
from types.responses.response_input_param import ResponseInputParam
from types.responses.response_prompt_param import ResponsePromptParam
from types.responses.response_stream_event import ResponseStreamEvent
from types.responses.response_input_item_param import ResponseInputItemParam
from types.responses.response_text_config_param import ResponseTextConfigParam
__all__ = [
    'Responses',
    'AsyncResponses']

class Responses(SyncAPIResource):
    input_items = (lambda self = None: InputItems(self._client))()
    input_tokens = (lambda self = None: InputTokens(self._client))()
    with_raw_response = (lambda self = None: ResponsesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: ResponsesWithStreamingResponse(self))()
    create = (lambda self = None, *, background: pass)()
    create = (lambda self = None, *, stream: pass)()
    create = (lambda self = None, *, stream: pass)()
    
    def create(self = None, *, background, conversation, include, input, instructions, max_output_tokens, max_tool_calls, metadata, model, parallel_tool_calls, previous_response_id, prompt, prompt_cache_key, prompt_cache_retention, reasoning, safety_identifier, service_tier, store, stream, stream_options, temperature, text, tool_choice, tools, top_logprobs, top_p, truncation, user, extra_headers, extra_query, extra_body, timeout):
        pass
    # WARNING: Decompyle incomplete

    stream = (lambda self = None, *, response_id: pass)()
    stream = (lambda self = None, *, input: pass)()
    
    def stream(self = None, *, response_id, input, model, background, text_format, tools, conversation, include, instructions, max_output_tokens, max_tool_calls, metadata, parallel_tool_calls, previous_response_id, prompt, prompt_cache_key, prompt_cache_retention, reasoning, safety_identifier, service_tier, store, stream_options, temperature, text, tool_choice, top_logprobs, top_p, truncation, user, starting_after, extra_headers, extra_query, extra_body, timeout):
        pass
    # WARNING: Decompyle incomplete

    
    def parse(self = None, *, text_format, background, conversation, include, input, instructions, max_output_tokens, max_tool_calls, metadata, model, parallel_tool_calls, previous_response_id, prompt, prompt_cache_key, prompt_cache_retention, reasoning, safety_identifier, service_tier, store, stream, stream_options, temperature, text, tool_choice, tools, top_logprobs, top_p, truncation, user, verbosity, extra_headers, extra_query, extra_body, timeout):
        pass
    # WARNING: Decompyle incomplete

    retrieve = (lambda self = None, response_id = None, *, include, include_obfuscation: pass)()
    retrieve = (lambda self = None, response_id = None, *, stream, include: pass)()
    retrieve = (lambda self = None, response_id = None, *, stream, include: pass)()
    retrieve = (lambda self = None, response_id = None, *, stream, include: pass)()
    retrieve = (lambda self = None, response_id = None, *, stream, include: pass)()
    retrieve = (lambda self = None, response_id = None, *, stream, include: pass)()
    
    def retrieve(self = None, response_id = None, *, include, include_obfuscation, starting_after, stream, extra_headers, extra_query, extra_body, timeout):
