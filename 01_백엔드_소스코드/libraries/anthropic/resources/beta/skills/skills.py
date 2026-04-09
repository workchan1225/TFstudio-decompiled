# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: skills.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Mapping, Optional, cast
from itertools import chain
import httpx
from  import _legacy_response
from versions import Versions, AsyncVersions, VersionsWithRawResponse, AsyncVersionsWithRawResponse, VersionsWithStreamingResponse, AsyncVersionsWithStreamingResponse
from _types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from _utils import is_given, extract_files, maybe_transform, strip_not_given, deepcopy_minimal, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from pagination import SyncPageCursor, AsyncPageCursor
from types.beta import skill_list_params, skill_create_params
from _base_client import AsyncPaginator, make_request_options
from types.anthropic_beta_param import AnthropicBetaParam
from types.beta.skill_list_response import SkillListResponse
from types.beta.skill_create_response import SkillCreateResponse
from types.beta.skill_delete_response import SkillDeleteResponse
from types.beta.skill_retrieve_response import SkillRetrieveResponse
__all__ = [
    'Skills',
    'AsyncSkills']

class Skills(SyncAPIResource):
    versions = (lambda self = None: Versions(self._client))()
    with_raw_response = (lambda self = None: SkillsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: SkillsWithStreamingResponse(self))()
    
    def create(self = None, *, display_title, files, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Create Skill

        Args:
          display_title: Display title for the skill.

              This is a human-readable label that is not included in the prompt sent to the
              model.

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

    
    def retrieve(self = None, skill_id = None, *, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Get Skill

        Args:
          skill_id: Unique identifier for the skill.

              The format and length of IDs may change over time.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not skill_id:
            raise ValueError(f'''Expected a non-empty value for `skill_id` but received {skill_id!r}''')
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, limit, page, source, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        List Skills

        Args:
          limit: Number of results to return per page.

              Maximum value is 100. Defaults to 20.

          page: Pagination token for fetching a specific page of results.

              Pass the value from a previous response\'s `next_page` field to get the next page
              of results.

          source: Filter skills by source.

              If provided, only skills from the specified source will be returned:

              - `"custom"`: only return user-created skills
              - `"anthropic"`: only return Anthropic-created skills

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def delete(self = None, skill_id = None, *, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete Skill

        Args:
          skill_id: Unique identifier for the skill.

              The format and length of IDs may change over time.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not skill_id:
            raise ValueError(f'''Expected a non-empty value for `skill_id` but received {skill_id!r}''')
    # WARNING: Decompyle incomplete



class AsyncSkills(AsyncAPIResource):
    versions = (lambda self = None: AsyncVersions(self._client))()
    with_raw_response = (lambda self = None: AsyncSkillsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncSkillsWithStreamingResponse(self))()
    
    async def create(self = None, *, display_title, files, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Create Skill

        Args:
          display_title: Display title for the skill.

              This is a human-readable label that is not included in the prompt sent to the
              model.

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

    
    async def retrieve(self = None, skill_id = None, *, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Get Skill

        Args:
          skill_id: Unique identifier for the skill.

              The format and length of IDs may change over time.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self = None, *, limit, page, source, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        List Skills

        Args:
          limit: Number of results to return per page.

              Maximum value is 100. Defaults to 20.

          page: Pagination token for fetching a specific page of results.

              Pass the value from a previous response\'s `next_page` field to get the next page
              of results.

          source: Filter skills by source.

              If provided, only skills from the specified source will be returned:

              - `"custom"`: only return user-created skills
              - `"anthropic"`: only return Anthropic-created skills

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def delete(self = None, skill_id = None, *, betas, extra_headers, extra_query, extra_body, timeout):
        '''
        Delete Skill

        Args:
          skill_id: Unique identifier for the skill.

              The format and length of IDs may change over time.

          betas: Optional header to specify the beta version(s) you want to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class SkillsWithRawResponse:
    
    def __init__(self = None, skills = None):
        self._skills = skills
        self.create = _legacy_response.to_raw_response_wrapper(skills.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(skills.retrieve)
        self.list = _legacy_response.to_raw_response_wrapper(skills.list)
        self.delete = _legacy_response.to_raw_response_wrapper(skills.delete)

    versions = (lambda self = None: VersionsWithRawResponse(self._skills.versions))()


class AsyncSkillsWithRawResponse:
    
    def __init__(self = None, skills = None):
        self._skills = skills
        self.create = _legacy_response.async_to_raw_response_wrapper(skills.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(skills.retrieve)
        self.list = _legacy_response.async_to_raw_response_wrapper(skills.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(skills.delete)

    versions = (lambda self = None: AsyncVersionsWithRawResponse(self._skills.versions))()


class SkillsWithStreamingResponse:
    
    def __init__(self = None, skills = None):
        self._skills = skills
        self.create = to_streamed_response_wrapper(skills.create)
        self.retrieve = to_streamed_response_wrapper(skills.retrieve)
        self.list = to_streamed_response_wrapper(skills.list)
        self.delete = to_streamed_response_wrapper(skills.delete)

    versions = (lambda self = None: VersionsWithStreamingResponse(self._skills.versions))()


class AsyncSkillsWithStreamingResponse:
    
    def __init__(self = None, skills = None):
        self._skills = skills
        self.create = async_to_streamed_response_wrapper(skills.create)
        self.retrieve = async_to_streamed_response_wrapper(skills.retrieve)
        self.list = async_to_streamed_response_wrapper(skills.list)
        self.delete = async_to_streamed_response_wrapper(skills.delete)

    versions = (lambda self = None: AsyncVersionsWithStreamingResponse(self._skills.versions))()
