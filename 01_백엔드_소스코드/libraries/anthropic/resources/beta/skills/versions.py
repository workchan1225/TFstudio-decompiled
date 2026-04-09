# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: versions.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Mapping, Optional, cast
from itertools import chain
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from _utils import is_given, extract_files, maybe_transform, strip_not_given, deepcopy_minimal, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncPageCursor, AsyncPageCursor
from _base_client import AsyncPaginator, make_request_options
from types.beta.skills import version_list_params, version_create_params
from types.anthropic_beta_param import AnthropicBetaParam
from types.beta.skills.version_list_response import VersionListResponse
from types.beta.skills.version_create_response import VersionCreateResponse
from types.beta.skills.version_delete_response import VersionDeleteResponse
from types.beta.skills.version_retrieve_response import VersionRetrieveResponse
__all__ = [
    'Versions',
    'AsyncVersions']

class Versions(SyncAPIResource):
    with_raw_response = (lambda self = None: VersionsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: VersionsWithStreamingResponse(self))()
    
    def create(self = None, skill_id = None, *, files, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Create Skill Version

        Args:
          skill_id: Unique identifier for the skill.

              The format and length of IDs may change over time.

          files: Files to upload for the skill.

              All files must be in the same top-level directory and must include a SKILL.md
              file at the root of that directory.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not skill_id:
            raise ValueError(f'''Expected a non-empty value for `skill_id` but received {skill_id!r}''')
    # WARNING: Decompyle incomplete

    
    def retrieve(self = None, version = None, *, skill_id, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Get Skill Version

        Args:
          skill_id: Unique identifier for the skill.

              The format and length of IDs may change over time.

          version: Version identifier for the skill.

              Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not skill_id:
            raise ValueError(f'''Expected a non-empty value for `skill_id` but received {skill_id!r}''')
        if not version:
            raise ValueError(f'''Expected a non-empty value for `version` but received {version!r}''')
    # WARNING: Decompyle incomplete

    
    def list(self = None, skill_id = None, *, limit, page, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        List Skill Versions

        Args:
          skill_id: Unique identifier for the skill.

              The format and length of IDs may change over time.

          limit: Number of items to return per page.

              Defaults to `20`. Ranges from `1` to `1000`.

          page: Optionally set to the `next_page` token from the previous response.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not skill_id:
            raise ValueError(f'''Expected a non-empty value for `skill_id` but received {skill_id!r}''')
    # WARNING: Decompyle incomplete

    
    def delete(self = None, version = None, *, skill_id, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete Skill Version

        Args:
          skill_id: Unique identifier for the skill.

              The format and length of IDs may change over time.

          version: Version identifier for the skill.

              Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not skill_id:
            raise ValueError(f'''Expected a non-empty value for `skill_id` but received {skill_id!r}''')
        if not version:
            raise ValueError(f'''Expected a non-empty value for `version` but received {version!r}''')
    # WARNING: Decompyle incomplete



class AsyncVersions(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncVersionsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncVersionsWithStreamingResponse(self))()
    
    async def create(self = None, skill_id = None, *, files, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Create Skill Version

        Args:
          skill_id: Unique identifier for the skill.

              The format and length of IDs may change over time.

          files: Files to upload for the skill.

              All files must be in the same top-level directory and must include a SKILL.md
              file at the root of that directory.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def retrieve(self = None, version = None, *, skill_id, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Get Skill Version

        Args:
          skill_id: Unique identifier for the skill.

              The format and length of IDs may change over time.

          version: Version identifier for the skill.

              Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, skill_id = None, *, limit, page, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        List Skill Versions

        Args:
          skill_id: Unique identifier for the skill.

              The format and length of IDs may change over time.

          limit: Number of items to return per page.

              Defaults to `20`. Ranges from `1` to `1000`.

          page: Optionally set to the `next_page` token from the previous response.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not skill_id:
            raise ValueError(f'''Expected a non-empty value for `skill_id` but received {skill_id!r}''')
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, version = None, *, skill_id, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete Skill Version

        Args:
          skill_id: Unique identifier for the skill.

              The format and length of IDs may change over time.

          version: Version identifier for the skill.

              Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class VersionsWithRawResponse:
    
    def __init__(self = None, versions = None):
        self._versions = versions
        self.create = _legacy_response.to_raw_response_wrapper(versions.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(versions.retrieve)
        self.list = _legacy_response.to_raw_response_wrapper(versions.list)
        self.delete = _legacy_response.to_raw_response_wrapper(versions.delete)



class AsyncVersionsWithRawResponse:
    
    def __init__(self = None, versions = None):
        self._versions = versions
        self.create = _legacy_response.async_to_raw_response_wrapper(versions.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(versions.retrieve)
        self.list = _legacy_response.async_to_raw_response_wrapper(versions.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(versions.delete)



class VersionsWithStreamingResponse:
    
    def __init__(self = None, versions = None):
        self._versions = versions
        self.create = to_streamed_response_wrapper(versions.create)
        self.retrieve = to_streamed_response_wrapper(versions.retrieve)
        self.list = to_streamed_response_wrapper(versions.list)
        self.delete = to_streamed_response_wrapper(versions.delete)



class AsyncVersionsWithStreamingResponse:
    
    def __init__(self = None, versions = None):
        self._versions = versions
        self.create = async_to_streamed_response_wrapper(versions.create)
        self.retrieve = async_to_streamed_response_wrapper(versions.retrieve)
        self.list = async_to_streamed_response_wrapper(versions.list)
        self.delete = async_to_streamed_response_wrapper(versions.delete)
