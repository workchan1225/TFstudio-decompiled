# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: completions.pyc (Python 3.11)

from __future__ import annotations
import inspect
from typing import Dict, List, Type, Union, Iterable, Optional, cast
from functools import partial
from typing_extensions import Literal, overload
import httpx
import pydantic
from  import _legacy_response
from messages import Messages, AsyncMessages, MessagesWithRawResponse, AsyncMessagesWithRawResponse, MessagesWithStreamingResponse, AsyncMessagesWithStreamingResponse
from _types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from _utils import required_args, maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _streaming import Stream, AsyncStream
from pagination import SyncCursorPage, AsyncCursorPage
from types.chat import ChatCompletionAudioParam, completion_list_params, completion_create_params, completion_update_params
from _base_client import AsyncPaginator, make_request_options
from lib._parsing import ResponseFormatT, validate_input_tools as _validate_input_tools, parse_chat_completion as _parse_chat_completion, type_to_response_format_param as _type_to_response_format
from lib.streaming.chat import ChatCompletionStreamManager, AsyncChatCompletionStreamManager
from types.shared.chat_model import ChatModel
from types.chat.chat_completion import ChatCompletion
from types.shared_params.metadata import Metadata
from types.shared.reasoning_effort import ReasoningEffort
from types.chat.chat_completion_chunk import ChatCompletionChunk
from types.chat.parsed_chat_completion import ParsedChatCompletion
from types.chat.chat_completion_deleted import ChatCompletionDeleted
from types.chat.chat_completion_audio_param import ChatCompletionAudioParam
from types.chat.chat_completion_message_param import ChatCompletionMessageParam
from types.chat.chat_completion_tool_union_param import ChatCompletionToolUnionParam
from types.chat.chat_completion_stream_options_param import ChatCompletionStreamOptionsParam
from types.chat.chat_completion_prediction_content_param import ChatCompletionPredictionContentParam
from types.chat.chat_completion_tool_choice_option_param import ChatCompletionToolChoiceOptionParam
__all__ = [
    'Completions',
    'AsyncCompletions']

class Completions(SyncAPIResource):
    messages = (lambda self = None: Messages(self._client))()
    with_raw_response = (lambda self = None: CompletionsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: CompletionsWithStreamingResponse(self))()
    
    def parse(self = None, *, messages, model, audio, response_format, frequency_penalty, function_call, functions, logit_bias, logprobs, max_completion_tokens, max_tokens, metadata, modalities, n, parallel_tool_calls, prediction, presence_penalty, prompt_cache_key, prompt_cache_retention, reasoning_effort, safety_identifier, seed, service_tier, stop, store, stream_options, temperature, tool_choice, tools, top_logprobs, top_p, user, verbosity, web_search_options, extra_headers, extra_query, extra_body, timeout):
        '''Wrapper over the `client.chat.completions.create()` method that provides richer integrations with Python specific types
        & returns a `ParsedChatCompletion` object, which is a subclass of the standard `ChatCompletion` class.

        You can pass a pydantic model to this method and it will automatically convert the model
        into a JSON schema, send it to the API and parse the response content back into the given model.

        This method will also automatically parse `function` tool calls if:
        - You use the `openai.pydantic_function_tool()` helper method
        - You mark your tool schema with `"strict": True`

        Example usage:
        ```py
        from pydantic import BaseModel
        from openai import OpenAI


        class Step(BaseModel):
            explanation: str
            output: str


        class MathResponse(BaseModel):
            steps: List[Step]
            final_answer: str


        client = OpenAI()
        completion = client.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are a helpful math tutor."},
                {"role": "user", "content": "solve 8x + 31 = 2"},
            ],
            response_format=MathResponse,
        )

        message = completion.choices[0].message
        if message.parsed:
            print(message.parsed.steps)
            print("answer: ", message.parsed.final_answer)
        ```
        '''
        pass
    # WARNING: Decompyle incomplete

    create = (lambda self = None, *, messages: pass)()
    create = (lambda self = None, *, messages: pass)()
    create = (lambda self = None, *, messages: pass)()
    create = (lambda self = None, *, messages: validate_response_format(response_format)# WARNING: Decompyle incomplete
)()
    
    def retrieve(self = None, completion_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''Get a stored chat completion.

        Only Chat Completions that have been created with
        the `store` parameter set to `true` will be returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not completion_id:
            raise ValueError(f'''Expected a non-empty value for `completion_id` but received {completion_id!r}''')
        return self._get(f'''/chat/completions/{completion_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = ChatCompletion)

    
    def update(self = None, completion_id = None, *, metadata, extra_headers, extra_query, extra_body, timeout):
        '''Modify a stored chat completion.

        Only Chat Completions that have been created
        with the `store` parameter set to `true` can be modified. Currently, the only
        supported modification is to update the `metadata` field.

        Args:
          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not completion_id:
            raise ValueError(f'''Expected a non-empty value for `completion_id` but received {completion_id!r}''')
        return self._post(f'''/chat/completions/{completion_id}''', body = maybe_transform({
            'metadata': metadata }, completion_update_params.CompletionUpdateParams), options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = ChatCompletion)

    
    def list(self = None, *, after, limit, metadata, model, order, extra_headers, extra_query, extra_body, timeout):
        '''List stored Chat Completions.

        Only Chat Completions that have been stored with
        the `store` parameter set to `true` will be returned.

        Args:
          after: Identifier for the last chat completion from the previous pagination request.

          limit: Number of Chat Completions to retrieve.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          model: The model used to generate the Chat Completions.

          order: Sort order for Chat Completions by timestamp. Use `asc` for ascending order or
              `desc` for descending order. Defaults to `asc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        return self._get_api_list('/chat/completions', page = SyncCursorPage[ChatCompletion], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit,
            'metadata': metadata,
            'model': model,
            'order': order }, completion_list_params.CompletionListParams)), model = ChatCompletion)

    
    def delete(self = None, completion_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''Delete a stored chat completion.

        Only Chat Completions that have been created
        with the `store` parameter set to `true` can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not completion_id:
            raise ValueError(f'''Expected a non-empty value for `completion_id` but received {completion_id!r}''')
        return self._delete(f'''/chat/completions/{completion_id}''', options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout), cast_to = ChatCompletionDeleted)

    
    def stream(self = None, *, messages, model, audio, response_format, frequency_penalty, function_call, functions, logit_bias, logprobs, max_completion_tokens, max_tokens, metadata, modalities, n, parallel_tool_calls, prediction, presence_penalty, prompt_cache_key, prompt_cache_retention, reasoning_effort, safety_identifier, seed, service_tier, stop, store, stream_options, temperature, tool_choice, tools, top_logprobs, top_p, user, verbosity, web_search_options, extra_headers, extra_query, extra_body, timeout):
        '''Wrapper over the `client.chat.completions.create(stream=True)` method that provides a more granular event API
        and automatic accumulation of each delta.

        This also supports all of the parsing utilities that `.parse()` does.

        Unlike `.create(stream=True)`, the `.stream()` method requires usage within a context manager to prevent accidental leakage of the response:

        ```py
        with client.chat.completions.stream(
            model="gpt-4o-2024-08-06",
            messages=[...],
        ) as stream:
            for event in stream:
                if event.type == "content.delta":
                    print(event.delta, flush=True, end="")
        ```

        When the context manager is entered, a `ChatCompletionStream` instance is returned which, like `.create(stream=True)` is an iterator. The full list of events that are yielded by the iterator are outlined in [these docs](https://github.com/openai/openai-python/blob/main/helpers.md#chat-completions-events).

        When the context manager exits, the response will be closed, however the `stream` instance is still available outside
        the context manager.
        '''
        pass
    # WARNING: Decompyle incomplete



class AsyncCompletions(AsyncAPIResource):
    messages = (lambda self = None: AsyncMessages(self._client))()
    with_raw_response = (lambda self = None: AsyncCompletionsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncCompletionsWithStreamingResponse(self))()
    
    async def parse(self = None, *, messages, model, audio, response_format, frequency_penalty, function_call, functions, logit_bias, logprobs, max_completion_tokens, max_tokens, metadata, modalities, n, parallel_tool_calls, prediction, presence_penalty, prompt_cache_key, prompt_cache_retention, reasoning_effort, safety_identifier, seed, service_tier, stop, store, stream_options, temperature, tool_choice, tools, top_logprobs, top_p, user, verbosity, web_search_options, extra_headers, extra_query, extra_body, timeout):
        '''Wrapper over the `client.chat.completions.create()` method that provides richer integrations with Python specific types
        & returns a `ParsedChatCompletion` object, which is a subclass of the standard `ChatCompletion` class.

        You can pass a pydantic model to this method and it will automatically convert the model
        into a JSON schema, send it to the API and parse the response content back into the given model.

        This method will also automatically parse `function` tool calls if:
        - You use the `openai.pydantic_function_tool()` helper method
        - You mark your tool schema with `"strict": True`

        Example usage:
        ```py
        from pydantic import BaseModel
        from openai import AsyncOpenAI


        class Step(BaseModel):
            explanation: str
            output: str


        class MathResponse(BaseModel):
            steps: List[Step]
            final_answer: str


        client = AsyncOpenAI()
        completion = await client.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are a helpful math tutor."},
                {"role": "user", "content": "solve 8x + 31 = 2"},
            ],
            response_format=MathResponse,
        )

        message = completion.choices[0].message
        if message.parsed:
            print(message.parsed.steps)
            print("answer: ", message.parsed.final_answer)
        ```
        '''
        pass
    # WARNING: Decompyle incomplete

    create = (lambda self = None, *, messages: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, messages: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, messages: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, messages: pass# WARNING: Decompyle incomplete
)()
    
    async def retrieve(self = None, completion_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''Get a stored chat completion.

        Only Chat Completions that have been created with
        the `store` parameter set to `true` will be returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def update(self = None, completion_id = None, *, metadata, extra_headers, extra_query, extra_body, timeout):
        '''Modify a stored chat completion.

        Only Chat Completions that have been created
        with the `store` parameter set to `true` can be modified. Currently, the only
        supported modification is to update the `metadata` field.

        Args:
          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, after, limit, metadata, model, order, extra_headers, extra_query, extra_body, timeout):
        '''List stored Chat Completions.

        Only Chat Completions that have been stored with
        the `store` parameter set to `true` will be returned.

        Args:
          after: Identifier for the last chat completion from the previous pagination request.

          limit: Number of Chat Completions to retrieve.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          model: The model used to generate the Chat Completions.

          order: Sort order for Chat Completions by timestamp. Use `asc` for ascending order or
              `desc` for descending order. Defaults to `asc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        return self._get_api_list('/chat/completions', page = AsyncCursorPage[ChatCompletion], options = make_request_options(extra_headers = extra_headers, extra_query = extra_query, extra_body = extra_body, timeout = timeout, query = maybe_transform({
            'after': after,
            'limit': limit,
            'metadata': metadata,
            'model': model,
            'order': order }, completion_list_params.CompletionListParams)), model = ChatCompletion)

    
    async def delete(self = None, completion_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''Delete a stored chat completion.

        Only Chat Completions that have been created
        with the `store` parameter set to `true` can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def stream(self = None, *, messages, model, audio, response_format, frequency_penalty, function_call, functions, logit_bias, logprobs, max_completion_tokens, max_tokens, metadata, modalities, n, parallel_tool_calls, prediction, presence_penalty, prompt_cache_key, prompt_cache_retention, reasoning_effort, safety_identifier, seed, service_tier, stop, store, stream_options, temperature, tool_choice, tools, top_logprobs, top_p, user, verbosity, web_search_options, extra_headers, extra_query, extra_body, timeout):
        '''Wrapper over the `client.chat.completions.create(stream=True)` method that provides a more granular event API
        and automatic accumulation of each delta.

        This also supports all of the parsing utilities that `.parse()` does.

        Unlike `.create(stream=True)`, the `.stream()` method requires usage within a context manager to prevent accidental leakage of the response:

        ```py
        async with client.chat.completions.stream(
            model="gpt-4o-2024-08-06",
            messages=[...],
        ) as stream:
            async for event in stream:
                if event.type == "content.delta":
                    print(event.delta, flush=True, end="")
        ```

        When the context manager is entered, an `AsyncChatCompletionStream` instance is returned which, like `.create(stream=True)` is an async iterator. The full list of events that are yielded by the iterator are outlined in [these docs](https://github.com/openai/openai-python/blob/main/helpers.md#chat-completions-events).

        When the context manager exits, the response will be closed, however the `stream` instance is still available outside
        the context manager.
        '''
        _validate_input_tools(tools)
    # WARNING: Decompyle incomplete



class CompletionsWithRawResponse:
    
    def __init__(self = None, completions = None):
        self._completions = completions
        self.parse = _legacy_response.to_raw_response_wrapper(completions.parse)
        self.create = _legacy_response.to_raw_response_wrapper(completions.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(completions.retrieve)
        self.update = _legacy_response.to_raw_response_wrapper(completions.update)
        self.list = _legacy_response.to_raw_response_wrapper(completions.list)
        self.delete = _legacy_response.to_raw_response_wrapper(completions.delete)

    messages = (lambda self = None: MessagesWithRawResponse(self._completions.messages))()


class AsyncCompletionsWithRawResponse:
    
    def __init__(self = None, completions = None):
        self._completions = completions
        self.parse = _legacy_response.async_to_raw_response_wrapper(completions.parse)
        self.create = _legacy_response.async_to_raw_response_wrapper(completions.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(completions.retrieve)
        self.update = _legacy_response.async_to_raw_response_wrapper(completions.update)
        self.list = _legacy_response.async_to_raw_response_wrapper(completions.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(completions.delete)

    messages = (lambda self = None: AsyncMessagesWithRawResponse(self._completions.messages))()


class CompletionsWithStreamingResponse:
    
    def __init__(self = None, completions = None):
        self._completions = completions
        self.parse = to_streamed_response_wrapper(completions.parse)
        self.create = to_streamed_response_wrapper(completions.create)
        self.retrieve = to_streamed_response_wrapper(completions.retrieve)
        self.update = to_streamed_response_wrapper(completions.update)
        self.list = to_streamed_response_wrapper(completions.list)
        self.delete = to_streamed_response_wrapper(completions.delete)

    messages = (lambda self = None: MessagesWithStreamingResponse(self._completions.messages))()


class AsyncCompletionsWithStreamingResponse:
    
    def __init__(self = None, completions = None):
        self._completions = completions
        self.parse = async_to_streamed_response_wrapper(completions.parse)
        self.create = async_to_streamed_response_wrapper(completions.create)
        self.retrieve = async_to_streamed_response_wrapper(completions.retrieve)
        self.update = async_to_streamed_response_wrapper(completions.update)
        self.list = async_to_streamed_response_wrapper(completions.list)
        self.delete = async_to_streamed_response_wrapper(completions.delete)

    messages = (lambda self = None: AsyncMessagesWithStreamingResponse(self._completions.messages))()


def validate_response_format(response_format = None):
    if inspect.isclass(response_format) or issubclass(response_format, pydantic.BaseModel):
        raise TypeError('You tried to pass a `BaseModel` class to `chat.completions.create()`; You must use `chat.completions.parse()` instead')
    return None
