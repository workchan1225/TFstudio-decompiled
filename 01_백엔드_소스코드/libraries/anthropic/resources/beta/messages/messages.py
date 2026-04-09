# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: messages.pyc (Python 3.11)

from __future__ import annotations
import inspect
import warnings
from typing import TYPE_CHECKING, List, Type, Union, Iterable, Optional, cast
from functools import partial
from itertools import chain
from typing_extensions import Literal, overload
import httpx
import pydantic
from  import _legacy_response
from batches import Batches, AsyncBatches, BatchesWithRawResponse, AsyncBatchesWithRawResponse, BatchesWithStreamingResponse, AsyncBatchesWithStreamingResponse
from _types import NOT_GIVEN, Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from _utils import is_given, required_args, maybe_transform, strip_not_given, async_maybe_transform
from _compat import cached_property
from _models import TypeAdapter
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from lib.tools import BetaToolRunner, BetaAsyncToolRunner, BetaStreamingToolRunner, BetaAsyncStreamingToolRunner
from _constants import DEFAULT_TIMEOUT, MODEL_NONSTREAMING_TOKENS
from _streaming import Stream, AsyncStream
from types.beta import BetaThinkingConfigParam, message_create_params, message_count_tokens_params
from _base_client import make_request_options
from lib.streaming import BetaMessageStreamManager, BetaAsyncMessageStreamManager
from messages.messages import DEPRECATED_MODELS
from types.model_param import ModelParam
from lib._parse._response import ResponseFormatT, parse_response
from lib._parse._transform import transform_schema
from types.beta.beta_message import BetaMessage
from lib.tools._beta_functions import BetaRunnableTool, BetaAsyncRunnableTool
from types.anthropic_beta_param import AnthropicBetaParam
from types.beta.beta_message_param import BetaMessageParam
from types.beta.beta_metadata_param import BetaMetadataParam
from types.beta.parsed_beta_message import ParsedBetaMessage
from types.beta.beta_text_block_param import BetaTextBlockParam
from types.beta.beta_tool_union_param import BetaToolUnionParam
from types.beta.beta_tool_choice_param import BetaToolChoiceParam
from lib.tools._beta_compaction_control import CompactionControl
from types.beta.beta_output_config_param import BetaOutputConfigParam
from types.beta.beta_message_tokens_count import BetaMessageTokensCount
from types.beta.beta_thinking_config_param import BetaThinkingConfigParam
from types.beta.beta_json_output_format_param import BetaJSONOutputFormatParam
from types.beta.beta_raw_message_stream_event import BetaRawMessageStreamEvent
from types.beta.beta_context_management_config_param import BetaContextManagementConfigParam
from types.beta.beta_request_mcp_server_url_definition_param import BetaRequestMCPServerURLDefinitionParam
if TYPE_CHECKING:
    from _client import Anthropic, AsyncAnthropic
__all__ = [
    'Messages',
    'AsyncMessages']

class Messages(SyncAPIResource):
    batches = (lambda self = None: Batches(self._client))()
    with_raw_response = (lambda self = None: MessagesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: MessagesWithStreamingResponse(self))()
    create = (lambda self = None, *, max_tokens: pass)()
    create = (lambda self = None, *, max_tokens: pass)()
    create = (lambda self = None, *, max_tokens: pass)()
    create = (lambda self = None, *, max_tokens: validate_output_format(output_format)if stream and is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
timeout = self._client._calculate_nonstreaming_timeout(max_tokens, MODEL_NONSTREAMING_TOKENS.get(model, None))if model in DEPRECATED_MODELS:
warnings.warn(f'''The model \'{model}\' is deprecated and will reach end-of-life on {DEPRECATED_MODELS[model]}.\nPlease migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.''', DeprecationWarning, stacklevel = 3)# WARNING: Decompyle incomplete
)()
    
    def parse(self = None, *, max_tokens, messages, model, container, context_management, mcp_servers, metadata, output_config, output_format, service_tier, stop_sequences, stream, system, temperature, thinking, tool_choice, tools, top_k, top_p, betas, extra_headers, extra_query, extra_body, timeout):
        pass
    # WARNING: Decompyle incomplete

    tool_runner = (lambda self = None, *, max_tokens: pass)()
    tool_runner = (lambda self = None, *, max_tokens: pass)()
    tool_runner = (lambda self = None, *, max_tokens: pass)()
    
    def tool_runner(self = None, *, max_tokens, messages, model, tools, compaction_control, max_iterations, container, context_management, mcp_servers, metadata, output_config, output_format, service_tier, stop_sequences, stream, system, temperature, top_k, top_p, thinking, tool_choice, betas, extra_headers, extra_query, extra_body, timeout):
        '''Create a Message stream'''
        if model in DEPRECATED_MODELS:
            warnings.warn(f'''The model \'{model}\' is deprecated and will reach end-of-life on {DEPRECATED_MODELS[model]}.\nPlease migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.''', DeprecationWarning, stacklevel = 3)
    # WARNING: Decompyle incomplete

    
    def stream(self = None, *, max_tokens, messages, model, container, context_management, mcp_servers, metadata, output_config, output_format, service_tier, stop_sequences, system, temperature, thinking, tool_choice, tools, top_k, top_p, betas, extra_headers, extra_query, extra_body, timeout):
        if model in DEPRECATED_MODELS:
            warnings.warn(f'''The model \'{model}\' is deprecated and will reach end-of-life on {DEPRECATED_MODELS[model]}.\nPlease migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.''', DeprecationWarning, stacklevel = 3)
    # WARNING: Decompyle incomplete

    
    def count_tokens(self = None, *, messages, model, context_management, mcp_servers, output_config, output_format, system, thinking, tool_choice, tools, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Count the number of tokens in a Message.

        The Token Count API can be used to count the number of tokens in a Message,
        including tools, images, and documents, without creating it.

        Learn more about token counting in our
        [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

        Args:
          messages: Input messages.

              Our models are trained to operate on alternating `user` and `assistant`
              conversational turns. When creating a new `Message`, you specify the prior
              conversational turns with the `messages` parameter, and the model then generates
              the next `Message` in the conversation. Consecutive `user` or `assistant` turns
              in your request will be combined into a single turn.

              Each input message must be an object with a `role` and `content`. You can
              specify a single `user`-role message, or you can include multiple `user` and
              `assistant` messages.

              If the final message uses the `assistant` role, the response content will
              continue immediately from the content in that message. This can be used to
              constrain part of the model\'s response.

              Example with a single `user` message:

              ```json
              [{ "role": "user", "content": "Hello, Claude" }]
              ```

              Example with multiple conversational turns:

              ```json
              [
                { "role": "user", "content": "Hello there." },
                { "role": "assistant", "content": "Hi, I\'m Claude. How can I help you?" },
                { "role": "user", "content": "Can you explain LLMs in plain English?" }
              ]
              ```

              Example with a partially-filled response from Claude:

              ```json
              [
                {
                  "role": "user",
                  "content": "What\'s the Greek name for Sun? (A) Sol (B) Helios (C) Sun"
                },
                { "role": "assistant", "content": "The best answer is (" }
              ]
              ```

              Each input message `content` may be either a single `string` or an array of
              content blocks, where each block has a specific `type`. Using a `string` for
              `content` is shorthand for an array of one content block of type `"text"`. The
              following input messages are equivalent:

              ```json
              { "role": "user", "content": "Hello, Claude" }
              ```

              ```json
              { "role": "user", "content": [{ "type": "text", "text": "Hello, Claude" }] }
              ```

              See [input examples](https://docs.claude.com/en/api/messages-examples).

              Note that if you want to include a
              [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the
              top-level `system` parameter — there is no `"system"` role for input messages in
              the Messages API.

              There is a limit of 100,000 messages in a single request.

          model: The model that will complete your prompt.

See
              [models](https://docs.anthropic.com/en/docs/models-overview) for additional
              details and options.

          context_management: Context management configuration.

              This allows you to control how Claude manages context across multiple requests,
              such as whether to clear function results or not.

          mcp_servers: MCP servers to be utilized in this request

          output_config: Configuration options for the model\'s output. Controls aspects like how much
              effort the model puts into its response.

          output_format: A schema to specify Claude\'s output format in responses.

          system: System prompt.

              A system prompt is a way of providing context and instructions to Claude, such
              as specifying a particular goal or role. See our
              [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

          thinking: Configuration for enabling Claude\'s extended thinking.

              When enabled, responses include `thinking` content blocks showing Claude\'s
              thinking process before the final answer. Requires a minimum budget of 1,024
              tokens and counts towards your `max_tokens` limit.

              See
              [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)
              for details.

          tool_choice: How the model should use the provided tools. The model can use a specific tool,
              any available tool, decide by itself, or not use tools at all.

          tools: Definitions of tools that the model may use.

              If you include `tools` in your API request, the model may return `tool_use`
              content blocks that represent the model\'s use of those tools. You can then run
              those tools using the tool input generated by the model and then optionally
              return results back to the model using `tool_result` content blocks.

              There are two types of tools: **client tools** and **server tools**. The
              behavior described below applies to client tools. For
              [server tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview#server-tools),
              see their individual documentation as each has its own behavior (e.g., the
              [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)).

              Each tool definition includes:

              - `name`: Name of the tool.
              - `description`: Optional, but strongly-recommended description of the tool.
              - `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the
                tool `input` shape that the model will produce in `tool_use` output content
                blocks.

              For example, if you defined `tools` as:

              ```json
              [
                {
                  "name": "get_stock_price",
                  "description": "Get the current stock price for a given ticker symbol.",
                  "input_schema": {
                    "type": "object",
                    "properties": {
                      "ticker": {
                        "type": "string",
                        "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
                      }
                    },
                    "required": ["ticker"]
                  }
                }
              ]
              ```

              And then asked the model "What\'s the S&P 500 at today?", the model might produce
              `tool_use` content blocks in the response like this:

              ```json
              [
                {
                  "type": "tool_use",
                  "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
                  "name": "get_stock_price",
                  "input": { "ticker": "^GSPC" }
                }
              ]
              ```

              You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an
              input, and return the following back to the model in a subsequent `user`
              message:

              ```json
              [
                {
                  "type": "tool_result",
                  "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
                  "content": "259.75 USD"
                }
              ]
              ```

              Tools can be used for workflows that include running client-side tools and
              functions, or more generally whenever you want the model to produce a particular
              JSON structure of output.

              See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class AsyncMessages(AsyncAPIResource):
    batches = (lambda self = None: AsyncBatches(self._client))()
    with_raw_response = (lambda self = None: AsyncMessagesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncMessagesWithStreamingResponse(self))()
    create = (lambda self = None, *, max_tokens: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, max_tokens: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, max_tokens: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, max_tokens: pass# WARNING: Decompyle incomplete
)()
    
    async def parse(self = None, *, max_tokens, messages, model, container, context_management, mcp_servers, metadata, output_config, output_format, service_tier, stop_sequences, stream, system, temperature, thinking, tool_choice, tools, top_k, top_p, betas, extra_headers, extra_query, extra_body, timeout):
        pass
    # WARNING: Decompyle incomplete

    tool_runner = (lambda self = None, *, max_tokens: pass)()
    tool_runner = (lambda self = None, *, max_tokens: pass)()
    tool_runner = (lambda self = None, *, max_tokens: pass)()
    
    def tool_runner(self = None, *, max_tokens, messages, model, tools, compaction_control, max_iterations, container, context_management, mcp_servers, metadata, output_config, output_format, service_tier, stop_sequences, stream, system, temperature, top_k, top_p, thinking, tool_choice, betas, extra_headers, extra_query, extra_body, timeout):
        '''Create a Message stream'''
        if model in DEPRECATED_MODELS:
            warnings.warn(f'''The model \'{model}\' is deprecated and will reach end-of-life on {DEPRECATED_MODELS[model]}.\nPlease migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.''', DeprecationWarning, stacklevel = 3)
    # WARNING: Decompyle incomplete

    
    def stream(self = None, *, max_tokens, messages, model, metadata, output_config, output_format, container, context_management, mcp_servers, service_tier, stop_sequences, system, temperature, thinking, tool_choice, tools, top_k, top_p, betas, extra_headers, extra_query, extra_body, timeout):
        if model in DEPRECATED_MODELS:
            warnings.warn(f'''The model \'{model}\' is deprecated and will reach end-of-life on {DEPRECATED_MODELS[model]}.\nPlease migrate to a newer model. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.''', DeprecationWarning, stacklevel = 3)
    # WARNING: Decompyle incomplete

    
    async def count_tokens(self = None, *, messages, model, context_management, mcp_servers, output_config, output_format, system, thinking, tool_choice, tools, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Count the number of tokens in a Message.

        The Token Count API can be used to count the number of tokens in a Message,
        including tools, images, and documents, without creating it.

        Learn more about token counting in our
        [user guide](https://docs.claude.com/en/docs/build-with-claude/token-counting)

        Args:
          messages: Input messages.

              Our models are trained to operate on alternating `user` and `assistant`
              conversational turns. When creating a new `Message`, you specify the prior
              conversational turns with the `messages` parameter, and the model then generates
              the next `Message` in the conversation. Consecutive `user` or `assistant` turns
              in your request will be combined into a single turn.

              Each input message must be an object with a `role` and `content`. You can
              specify a single `user`-role message, or you can include multiple `user` and
              `assistant` messages.

              If the final message uses the `assistant` role, the response content will
              continue immediately from the content in that message. This can be used to
              constrain part of the model\'s response.

              Example with a single `user` message:

              ```json
              [{ "role": "user", "content": "Hello, Claude" }]
              ```

              Example with multiple conversational turns:

              ```json
              [
                { "role": "user", "content": "Hello there." },
                { "role": "assistant", "content": "Hi, I\'m Claude. How can I help you?" },
                { "role": "user", "content": "Can you explain LLMs in plain English?" }
              ]
              ```

              Example with a partially-filled response from Claude:

              ```json
              [
                {
                  "role": "user",
                  "content": "What\'s the Greek name for Sun? (A) Sol (B) Helios (C) Sun"
                },
                { "role": "assistant", "content": "The best answer is (" }
              ]
              ```

              Each input message `content` may be either a single `string` or an array of
              content blocks, where each block has a specific `type`. Using a `string` for
              `content` is shorthand for an array of one content block of type `"text"`. The
              following input messages are equivalent:

              ```json
              { "role": "user", "content": "Hello, Claude" }
              ```

              ```json
              { "role": "user", "content": [{ "type": "text", "text": "Hello, Claude" }] }
              ```

              See [input examples](https://docs.claude.com/en/api/messages-examples).

              Note that if you want to include a
              [system prompt](https://docs.claude.com/en/docs/system-prompts), you can use the
              top-level `system` parameter — there is no `"system"` role for input messages in
              the Messages API.

              There is a limit of 100,000 messages in a single request.

          model: The model that will complete your prompt.

See
              [models](https://docs.anthropic.com/en/docs/models-overview) for additional
              details and options.

          context_management: Context management configuration.

              This allows you to control how Claude manages context across multiple requests,
              such as whether to clear function results or not.

          mcp_servers: MCP servers to be utilized in this request

          output_config: Configuration options for the model\'s output. Controls aspects like how much
              effort the model puts into its response.

          output_format: A schema to specify Claude\'s output format in responses.

          system: System prompt.

              A system prompt is a way of providing context and instructions to Claude, such
              as specifying a particular goal or role. See our
              [guide to system prompts](https://docs.claude.com/en/docs/system-prompts).

          thinking: Configuration for enabling Claude\'s extended thinking.

              When enabled, responses include `thinking` content blocks showing Claude\'s
              thinking process before the final answer. Requires a minimum budget of 1,024
              tokens and counts towards your `max_tokens` limit.

              See
              [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)
              for details.

          tool_choice: How the model should use the provided tools. The model can use a specific tool,
              any available tool, decide by itself, or not use tools at all.

          tools: Definitions of tools that the model may use.

              If you include `tools` in your API request, the model may return `tool_use`
              content blocks that represent the model\'s use of those tools. You can then run
              those tools using the tool input generated by the model and then optionally
              return results back to the model using `tool_result` content blocks.

              There are two types of tools: **client tools** and **server tools**. The
              behavior described below applies to client tools. For
              [server tools](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview#server-tools),
              see their individual documentation as each has its own behavior (e.g., the
              [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool)).

              Each tool definition includes:

              - `name`: Name of the tool.
              - `description`: Optional, but strongly-recommended description of the tool.
              - `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the
                tool `input` shape that the model will produce in `tool_use` output content
                blocks.

              For example, if you defined `tools` as:

              ```json
              [
                {
                  "name": "get_stock_price",
                  "description": "Get the current stock price for a given ticker symbol.",
                  "input_schema": {
                    "type": "object",
                    "properties": {
                      "ticker": {
                        "type": "string",
                        "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
                      }
                    },
                    "required": ["ticker"]
                  }
                }
              ]
              ```

              And then asked the model "What\'s the S&P 500 at today?", the model might produce
              `tool_use` content blocks in the response like this:

              ```json
              [
                {
                  "type": "tool_use",
                  "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
                  "name": "get_stock_price",
                  "input": { "ticker": "^GSPC" }
                }
              ]
              ```

              You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an
              input, and return the following back to the model in a subsequent `user`
              message:

              ```json
              [
                {
                  "type": "tool_result",
                  "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
                  "content": "259.75 USD"
                }
              ]
              ```

              Tools can be used for workflows that include running client-side tools and
              functions, or more generally whenever you want the model to produce a particular
              JSON structure of output.

              See our [guide](https://docs.claude.com/en/docs/tool-use) for more details.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class MessagesWithRawResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.create = _legacy_response.to_raw_response_wrapper(messages.create)
        self.count_tokens = _legacy_response.to_raw_response_wrapper(messages.count_tokens)

    batches = (lambda self = None: BatchesWithRawResponse(self._messages.batches))()


class AsyncMessagesWithRawResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.create = _legacy_response.async_to_raw_response_wrapper(messages.create)
        self.count_tokens = _legacy_response.async_to_raw_response_wrapper(messages.count_tokens)

    batches = (lambda self = None: AsyncBatchesWithRawResponse(self._messages.batches))()


class MessagesWithStreamingResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.create = to_streamed_response_wrapper(messages.create)
        self.count_tokens = to_streamed_response_wrapper(messages.count_tokens)

    batches = (lambda self = None: BatchesWithStreamingResponse(self._messages.batches))()


class AsyncMessagesWithStreamingResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.create = async_to_streamed_response_wrapper(messages.create)
        self.count_tokens = async_to_streamed_response_wrapper(messages.count_tokens)

    batches = (lambda self = None: AsyncBatchesWithStreamingResponse(self._messages.batches))()


def validate_output_format(output_format = None):
    if inspect.isclass(output_format) or issubclass(output_format, pydantic.BaseModel):
        raise TypeError('You tried to pass a `BaseModel` class to `beta.messages.create()`; You must use `beta.messages.parse()` instead')
    return None
