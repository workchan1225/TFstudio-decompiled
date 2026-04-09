# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: embeddings.pyc (Python 3.11)

from __future__ import annotations
import array
import base64
from typing import Union, Iterable, cast
from typing_extensions import Literal
import httpx
from  import _legacy_response
from types import embedding_create_params
from _types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from _utils import is_given, maybe_transform
from _compat import cached_property
from _extras import numpy as np, has_numpy
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _base_client import make_request_options
from types.embedding_model import EmbeddingModel
from types.create_embedding_response import CreateEmbeddingResponse
__all__ = [
    'Embeddings',
    'AsyncEmbeddings']

class Embeddings(SyncAPIResource):
    with_raw_response = (lambda self = None: EmbeddingsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: EmbeddingsWithStreamingResponse(self))()
    
    def create(self = None, *, input, model, dimensions, encoding_format, user, extra_headers, extra_query, extra_body, timeout):
        '''
        Creates an embedding vector representing the input text.

        Args:
          input: Input text to embed, encoded as a string or array of tokens. To embed multiple
              inputs in a single request, pass an array of strings or array of token arrays.
              The input must not exceed the max input tokens for the model (8192 tokens for
              all embedding models), cannot be an empty string, and any array must be 2048
              dimensions or less.
              [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
              for counting tokens. In addition to the per-input token limit, all embedding
              models enforce a maximum of 300,000 tokens summed across all inputs in a single
              request.

          model: ID of the model to use. You can use the
              [List models](https://platform.openai.com/docs/api-reference/models/list) API to
              see all of your available models, or see our
              [Model overview](https://platform.openai.com/docs/models) for descriptions of
              them.

          dimensions: The number of dimensions the resulting output embeddings should have. Only
              supported in `text-embedding-3` and later models.

          encoding_format: The format to return the embeddings in. Can be either `float` or
              [`base64`](https://pypi.org/project/pybase64/).

          user: A unique identifier representing your end-user, which can help OpenAI to monitor
              and detect abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#end-user-ids).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class AsyncEmbeddings(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncEmbeddingsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncEmbeddingsWithStreamingResponse(self))()
    
    async def create(self = None, *, input, model, dimensions, encoding_format, user, extra_headers, extra_query, extra_body, timeout):
        '''
        Creates an embedding vector representing the input text.

        Args:
          input: Input text to embed, encoded as a string or array of tokens. To embed multiple
              inputs in a single request, pass an array of strings or array of token arrays.
              The input must not exceed the max input tokens for the model (8192 tokens for
              all embedding models), cannot be an empty string, and any array must be 2048
              dimensions or less.
              [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken)
              for counting tokens. In addition to the per-input token limit, all embedding
              models enforce a maximum of 300,000 tokens summed across all inputs in a single
              request.

          model: ID of the model to use. You can use the
              [List models](https://platform.openai.com/docs/api-reference/models/list) API to
              see all of your available models, or see our
              [Model overview](https://platform.openai.com/docs/models) for descriptions of
              them.

          dimensions: The number of dimensions the resulting output embeddings should have. Only
              supported in `text-embedding-3` and later models.

          encoding_format: The format to return the embeddings in. Can be either `float` or
              [`base64`](https://pypi.org/project/pybase64/).

          user: A unique identifier representing your end-user, which can help OpenAI to monitor
              and detect abuse.
              [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#end-user-ids).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class EmbeddingsWithRawResponse:
    
    def __init__(self = None, embeddings = None):
        self._embeddings = embeddings
        self.create = _legacy_response.to_raw_response_wrapper(embeddings.create)



class AsyncEmbeddingsWithRawResponse:
    
    def __init__(self = None, embeddings = None):
        self._embeddings = embeddings
        self.create = _legacy_response.async_to_raw_response_wrapper(embeddings.create)



class EmbeddingsWithStreamingResponse:
    
    def __init__(self = None, embeddings = None):
        self._embeddings = embeddings
        self.create = to_streamed_response_wrapper(embeddings.create)



class AsyncEmbeddingsWithStreamingResponse:
    
    def __init__(self = None, embeddings = None):
        self._embeddings = embeddings
        self.create = async_to_streamed_response_wrapper(embeddings.create)
