# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_tokens.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable, Optional
from typing_extensions import Literal
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _base_client import make_request_options
from types.responses import input_token_count_params
from types.responses.tool_param import ToolParam
from types.shared_params.reasoning import Reasoning
from types.responses.response_input_item_param import ResponseInputItemParam
from types.responses.input_token_count_response import InputTokenCountResponse
__all__ = [
    'InputTokens',
    'AsyncInputTokens']

class InputTokens(SyncAPIResource):
    with_raw_response = (lambda self = None: InputTokensWithRawResponse(self))()
    with_streaming_response = (lambda self = None: InputTokensWithStreamingResponse(self))()
    
    def count(self = None, *, conversation, input, instructions, model, parallel_tool_calls, previous_response_id, reasoning, text, tool_choice, tools, truncation, extra_headers, extra_query, extra_body, timeout):
        """
        Get input token counts

        Args:
          conversation: The conversation that this response belongs to. Items from this conversation are
              prepended to `input_items` for this response request. Input items and output
              items from this response are automatically added to this conversation after this
              response completes.

          input: Text, image, or file inputs to the model, used to generate a response

          instructions: A system (or developer) message inserted into the model's context. When used
              along with `previous_response_id`, the instructions from a previous response
              will not be carried over to the next response. This makes it simple to swap out
              system (or developer) messages in new responses.

          model: Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI offers a
              wide range of models with different capabilities, performance characteristics,
              and price points. Refer to the
              [model guide](https://platform.openai.com/docs/models) to browse and compare
              available models.

          parallel_tool_calls: Whether to allow the model to run tool calls in parallel.

          previous_response_id: The unique ID of the previous response to the model. Use this to create
              multi-turn conversations. Learn more about
              [conversation state](https://platform.openai.com/docs/guides/conversation-state).
              Cannot be used in conjunction with `conversation`.

          reasoning: **gpt-5 and o-series models only** Configuration options for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning).

          text: Configuration options for a text response from the model. Can be plain text or
              structured JSON data. Learn more:

              - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
              - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

          tool_choice: How the model should select which tool (or tools) to use when generating a
              response. See the `tools` parameter to see how to specify which tools the model
              can call.

          tools: An array of tools the model may call while generating a response. You can
              specify which tool to use by setting the `tool_choice` parameter.

          truncation: The truncation strategy to use for the model response. - `auto`: If the input to
              this Response exceeds the model's context window size, the model will truncate
              the response to fit the context window by dropping items from the beginning of
              the conversation. - `disabled` (default): If the input size will exceed the
              context window size for a model, the request will fail with a 400 error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post('/responses/input_tokens', body = maybe_transform({
            'conversation': conversation,
            'input': input,
            'instructions': instructions,
            'model': model,
            'parallel_tool_calls': parallel_tool_calls,
            'previous_response_id': previous_response_id,
            'reasoning': reasoning,
            'text': text,
            'tool_choice': tool_choice,
            'tools': tools,
            'truncation': truncation }, input_token_count_params.InputTokenCountParams), options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = InputTokenCountResponse)



class AsyncInputTokens(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncInputTokensWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncInputTokensWithStreamingResponse(self))()
    
    async def count(self = None, *, conversation, input, instructions, model, parallel_tool_calls, previous_response_id, reasoning, text, tool_choice, tools, truncation, extra_headers, extra_query, extra_body, timeout):
        """
        Get input token counts

        Args:
          conversation: The conversation that this response belongs to. Items from this conversation are
              prepended to `input_items` for this response request. Input items and output
              items from this response are automatically added to this conversation after this
              response completes.

          input: Text, image, or file inputs to the model, used to generate a response

          instructions: A system (or developer) message inserted into the model's context. When used
              along with `previous_response_id`, the instructions from a previous response
              will not be carried over to the next response. This makes it simple to swap out
              system (or developer) messages in new responses.

          model: Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI offers a
              wide range of models with different capabilities, performance characteristics,
              and price points. Refer to the
              [model guide](https://platform.openai.com/docs/models) to browse and compare
              available models.

          parallel_tool_calls: Whether to allow the model to run tool calls in parallel.

          previous_response_id: The unique ID of the previous response to the model. Use this to create
              multi-turn conversations. Learn more about
              [conversation state](https://platform.openai.com/docs/guides/conversation-state).
              Cannot be used in conjunction with `conversation`.

          reasoning: **gpt-5 and o-series models only** Configuration options for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning).

          text: Configuration options for a text response from the model. Can be plain text or
              structured JSON data. Learn more:

              - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
              - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

          tool_choice: How the model should select which tool (or tools) to use when generating a
              response. See the `tools` parameter to see how to specify which tools the model
              can call.

          tools: An array of tools the model may call while generating a response. You can
              specify which tool to use by setting the `tool_choice` parameter.

          truncation: The truncation strategy to use for the model response. - `auto`: If the input to
              this Response exceeds the model's context window size, the model will truncate
              the response to fit the context window by dropping items from the beginning of
              the conversation. - `disabled` (default): If the input size will exceed the
              context window size for a model, the request will fail with a 400 error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        pass
    # WARNING: Decompyle incomplete



class InputTokensWithRawResponse:
    
    def __init__(self = None, input_tokens = None):
        self._input_tokens = input_tokens
        self.count = _legacy_response.to_raw_response_wrapper(input_tokens.count)



class AsyncInputTokensWithRawResponse:
    
    def __init__(self = None, input_tokens = None):
        self._input_tokens = input_tokens
        self.count = _legacy_response.async_to_raw_response_wrapper(input_tokens.count)



class InputTokensWithStreamingResponse:
    
    def __init__(self = None, input_tokens = None):
        self._input_tokens = input_tokens
        self.count = to_streamed_response_wrapper(input_tokens.count)



class AsyncInputTokensWithStreamingResponse:
    
    def __init__(self = None, input_tokens = None):
        self._input_tokens = input_tokens
        self.count = async_to_streamed_response_wrapper(input_tokens.count)
