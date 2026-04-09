# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parts.pyc (Python 3.11)

from __future__ import annotations
from typing import Mapping, cast
import httpx
from  import _legacy_response
from _types import Body, Query, Headers, NotGiven, FileTypes, not_given
from _utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _base_client import make_request_options
from types.uploads import part_create_params
from types.uploads.upload_part import UploadPart
__all__ = [
    'Parts',
    'AsyncParts']

class Parts(SyncAPIResource):
    with_raw_response = (lambda self = None: PartsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: PartsWithStreamingResponse(self))()
    
    def create(self = None, upload_id = None, *, data, extra_headers, extra_query, extra_body, timeout):
        '''
        Adds a
        [Part](https://platform.openai.com/docs/api-reference/uploads/part-object) to an
        [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object.
        A Part represents a chunk of bytes from the file you are trying to upload.

        Each Part can be at most 64 MB, and you can add Parts until you hit the Upload
        maximum of 8 GB.

        It is possible to add multiple Parts in parallel. You can decide the intended
        order of the Parts when you
        [complete the Upload](https://platform.openai.com/docs/api-reference/uploads/complete).

        Args:
          data: The chunk of bytes for this Part.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not upload_id:
            raise ValueError(f'''Expected a non-empty value for `upload_id` but received {upload_id!r}''')
        body = deepcopy_minimal({
            'data': data })
        files = extract_files(cast(Mapping[(str, object)], body), paths = [
            [
                'data']])
    # WARNING: Decompyle incomplete



class AsyncParts(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncPartsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncPartsWithStreamingResponse(self))()
    
    async def create(self = None, upload_id = None, *, data, extra_headers, extra_query, extra_body, timeout):
        '''
        Adds a
        [Part](https://platform.openai.com/docs/api-reference/uploads/part-object) to an
        [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object.
        A Part represents a chunk of bytes from the file you are trying to upload.

        Each Part can be at most 64 MB, and you can add Parts until you hit the Upload
        maximum of 8 GB.

        It is possible to add multiple Parts in parallel. You can decide the intended
        order of the Parts when you
        [complete the Upload](https://platform.openai.com/docs/api-reference/uploads/complete).

        Args:
          data: The chunk of bytes for this Part.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class PartsWithRawResponse:
    
    def __init__(self = None, parts = None):
        self._parts = parts
        self.create = _legacy_response.to_raw_response_wrapper(parts.create)



class AsyncPartsWithRawResponse:
    
    def __init__(self = None, parts = None):
        self._parts = parts
        self.create = _legacy_response.async_to_raw_response_wrapper(parts.create)



class PartsWithStreamingResponse:
    
    def __init__(self = None, parts = None):
        self._parts = parts
        self.create = to_streamed_response_wrapper(parts.create)



class AsyncPartsWithStreamingResponse:
    
    def __init__(self = None, parts = None):
        self._parts = parts
        self.create = async_to_streamed_response_wrapper(parts.create)
