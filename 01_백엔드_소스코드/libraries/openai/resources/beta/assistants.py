# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: assistants.pyc (Python 3.11)

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
from pagination import SyncCursorPage, AsyncCursorPage
from types.beta import assistant_list_params, assistant_create_params, assistant_update_params
from _base_client import AsyncPaginator, make_request_options
from types.beta.assistant import Assistant
from types.shared.chat_model import ChatModel
from types.beta.assistant_deleted import AssistantDeleted
from types.shared_params.metadata import Metadata
from types.shared.reasoning_effort import ReasoningEffort
from types.beta.assistant_tool_param import AssistantToolParam
from types.beta.assistant_response_format_option_param import AssistantResponseFormatOptionParam
__all__ = [
    'Assistants',
    'AsyncAssistants']

class Assistants(SyncAPIResource):
    with_raw_response = (lambda self = None: AssistantsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AssistantsWithStreamingResponse(self))()
    
    def create(self = None, *, model, description, instructions, metadata, name, reasoning_effort, response_format, temperature, tool_resources, tools, top_p, extra_headers, extra_query, extra_body, timeout):
        '''
        Create an assistant with a model and instructions.

        Args:
          model: ID of the model to use. You can use the
              [List models](https://platform.openai.com/docs/api-reference/models/list) API to
              see all of your available models, or see our
              [Model overview](https://platform.openai.com/docs/models) for descriptions of
              them.

          description: The description of the assistant. The maximum length is 512 characters.

          instructions: The system instructions that the assistant uses. The maximum length is 256,000
              characters.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          name: The name of the assistant. The maximum length is 256 characters.

          reasoning_effort: Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`.
              Reducing reasoning effort can result in faster responses and fewer tokens used
              on reasoning in a response.

              - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported
                reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool
                calls are supported for all reasoning values in gpt-5.1.
              - All models before `gpt-5.1` default to `medium` reasoning effort, and do not
                support `none`.
              - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
              - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

          response_format: Specifies the format that the model must output. Compatible with
              [GPT-4o](https://platform.openai.com/docs/models#gpt-4o),
              [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4),
              and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

          tool_resources: A set of resources that are used by the assistant\'s tools. The resources are
              specific to the type of tool. For example, the `code_interpreter` tool requires
              a list of file IDs, while the `file_search` tool requires a list of vector store
              IDs.

          tools: A list of tool enabled on the assistant. There can be a maximum of 128 tools per
              assistant. Tools can be of types `code_interpreter`, `file_search`, or
              `function`.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or temperature but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def retrieve(self = None, assistant_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieves an assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not assistant_id:
            raise ValueError(f'''Expected a non-empty value for `assistant_id` but received {assistant_id!r}''')
    # WARNING: Decompyle incomplete

    
    def update(self = None, assistant_id = None, *, description, instructions, metadata, model, name, reasoning_effort, response_format, temperature, tool_resources, tools, top_p, extra_headers, extra_query, extra_body, timeout):
        '''Modifies an assistant.

        Args:
          description: The description of the assistant.

        The maximum length is 512 characters.

          instructions: The system instructions that the assistant uses. The maximum length is 256,000
              characters.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          model: ID of the model to use. You can use the
              [List models](https://platform.openai.com/docs/api-reference/models/list) API to
              see all of your available models, or see our
              [Model overview](https://platform.openai.com/docs/models) for descriptions of
              them.

          name: The name of the assistant. The maximum length is 256 characters.

          reasoning_effort: Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`.
              Reducing reasoning effort can result in faster responses and fewer tokens used
              on reasoning in a response.

              - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported
                reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool
                calls are supported for all reasoning values in gpt-5.1.
              - All models before `gpt-5.1` default to `medium` reasoning effort, and do not
                support `none`.
              - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
              - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

          response_format: Specifies the format that the model must output. Compatible with
              [GPT-4o](https://platform.openai.com/docs/models#gpt-4o),
              [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4),
              and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

          tool_resources: A set of resources that are used by the assistant\'s tools. The resources are
              specific to the type of tool. For example, the `code_interpreter` tool requires
              a list of file IDs, while the `file_search` tool requires a list of vector store
              IDs.

          tools: A list of tool enabled on the assistant. There can be a maximum of 128 tools per
              assistant. Tools can be of types `code_interpreter`, `file_search`, or
              `function`.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or temperature but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not assistant_id:
            raise ValueError(f'''Expected a non-empty value for `assistant_id` but received {assistant_id!r}''')
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, after, before, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''Returns a list of assistants.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              starting with obj_foo, your subsequent call can include before=obj_foo in order
              to fetch the previous page of the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def delete(self = None, assistant_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete an assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not assistant_id:
            raise ValueError(f'''Expected a non-empty value for `assistant_id` but received {assistant_id!r}''')
    # WARNING: Decompyle incomplete



class AsyncAssistants(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncAssistantsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncAssistantsWithStreamingResponse(self))()
    
    async def create(self = None, *, model, description, instructions, metadata, name, reasoning_effort, response_format, temperature, tool_resources, tools, top_p, extra_headers, extra_query, extra_body, timeout):
        '''
        Create an assistant with a model and instructions.

        Args:
          model: ID of the model to use. You can use the
              [List models](https://platform.openai.com/docs/api-reference/models/list) API to
              see all of your available models, or see our
              [Model overview](https://platform.openai.com/docs/models) for descriptions of
              them.

          description: The description of the assistant. The maximum length is 512 characters.

          instructions: The system instructions that the assistant uses. The maximum length is 256,000
              characters.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          name: The name of the assistant. The maximum length is 256 characters.

          reasoning_effort: Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`.
              Reducing reasoning effort can result in faster responses and fewer tokens used
              on reasoning in a response.

              - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported
                reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool
                calls are supported for all reasoning values in gpt-5.1.
              - All models before `gpt-5.1` default to `medium` reasoning effort, and do not
                support `none`.
              - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
              - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

          response_format: Specifies the format that the model must output. Compatible with
              [GPT-4o](https://platform.openai.com/docs/models#gpt-4o),
              [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4),
              and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

          tool_resources: A set of resources that are used by the assistant\'s tools. The resources are
              specific to the type of tool. For example, the `code_interpreter` tool requires
              a list of file IDs, while the `file_search` tool requires a list of vector store
              IDs.

          tools: A list of tool enabled on the assistant. There can be a maximum of 128 tools per
              assistant. Tools can be of types `code_interpreter`, `file_search`, or
              `function`.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or temperature but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve(self = None, assistant_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Retrieves an assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def update(self = None, assistant_id = None, *, description, instructions, metadata, model, name, reasoning_effort, response_format, temperature, tool_resources, tools, top_p, extra_headers, extra_query, extra_body, timeout):
        '''Modifies an assistant.

        Args:
          description: The description of the assistant.

        The maximum length is 512 characters.

          instructions: The system instructions that the assistant uses. The maximum length is 256,000
              characters.

          metadata: Set of 16 key-value pairs that can be attached to an object. This can be useful
              for storing additional information about the object in a structured format, and
              querying for objects via API or the dashboard.

              Keys are strings with a maximum length of 64 characters. Values are strings with
              a maximum length of 512 characters.

          model: ID of the model to use. You can use the
              [List models](https://platform.openai.com/docs/api-reference/models/list) API to
              see all of your available models, or see our
              [Model overview](https://platform.openai.com/docs/models) for descriptions of
              them.

          name: The name of the assistant. The maximum length is 256 characters.

          reasoning_effort: Constrains effort on reasoning for
              [reasoning models](https://platform.openai.com/docs/guides/reasoning). Currently
              supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`.
              Reducing reasoning effort can result in faster responses and fewer tokens used
              on reasoning in a response.

              - `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported
                reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool
                calls are supported for all reasoning values in gpt-5.1.
              - All models before `gpt-5.1` default to `medium` reasoning effort, and do not
                support `none`.
              - The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
              - `xhigh` is supported for all models after `gpt-5.1-codex-max`.

          response_format: Specifies the format that the model must output. Compatible with
              [GPT-4o](https://platform.openai.com/docs/models#gpt-4o),
              [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4),
              and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

              Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured
              Outputs which ensures the model will match your supplied JSON schema. Learn more
              in the
              [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

              Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

          tool_resources: A set of resources that are used by the assistant\'s tools. The resources are
              specific to the type of tool. For example, the `code_interpreter` tool requires
              a list of file IDs, while the `file_search` tool requires a list of vector store
              IDs.

          tools: A list of tool enabled on the assistant. There can be a maximum of 128 tools per
              assistant. Tools can be of types `code_interpreter`, `file_search`, or
              `function`.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or temperature but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, after, before, limit, order, extra_headers, extra_query, extra_body, timeout):
        '''Returns a list of assistants.

        Args:
          after: A cursor for use in pagination.

        `after` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              ending with obj_foo, your subsequent call can include after=obj_foo in order to
              fetch the next page of the list.

          before: A cursor for use in pagination. `before` is an object ID that defines your place
              in the list. For instance, if you make a list request and receive 100 objects,
              starting with obj_foo, your subsequent call can include before=obj_foo in order
              to fetch the previous page of the list.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 20.

          order: Sort order by the `created_at` timestamp of the objects. `asc` for ascending
              order and `desc` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, assistant_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete an assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class AssistantsWithRawResponse:
    
    def __init__(self = None, assistants = None):
        self._assistants = assistants
        self.create = _legacy_response.to_raw_response_wrapper(assistants.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(assistants.retrieve)
        self.update = _legacy_response.to_raw_response_wrapper(assistants.update)
        self.list = _legacy_response.to_raw_response_wrapper(assistants.list)
        self.delete = _legacy_response.to_raw_response_wrapper(assistants.delete)



class AsyncAssistantsWithRawResponse:
    
    def __init__(self = None, assistants = None):
        self._assistants = assistants
        self.create = _legacy_response.async_to_raw_response_wrapper(assistants.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(assistants.retrieve)
        self.update = _legacy_response.async_to_raw_response_wrapper(assistants.update)
        self.list = _legacy_response.async_to_raw_response_wrapper(assistants.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(assistants.delete)



class AssistantsWithStreamingResponse:
    
    def __init__(self = None, assistants = None):
        self._assistants = assistants
        self.create = to_streamed_response_wrapper(assistants.create)
        self.retrieve = to_streamed_response_wrapper(assistants.retrieve)
        self.update = to_streamed_response_wrapper(assistants.update)
        self.list = to_streamed_response_wrapper(assistants.list)
        self.delete = to_streamed_response_wrapper(assistants.delete)



class AsyncAssistantsWithStreamingResponse:
    
    def __init__(self = None, assistants = None):
        self._assistants = assistants
        self.create = async_to_streamed_response_wrapper(assistants.create)
        self.retrieve = async_to_streamed_response_wrapper(assistants.retrieve)
        self.update = async_to_streamed_response_wrapper(assistants.update)
        self.list = async_to_streamed_response_wrapper(assistants.list)
        self.delete = async_to_streamed_response_wrapper(assistants.delete)
