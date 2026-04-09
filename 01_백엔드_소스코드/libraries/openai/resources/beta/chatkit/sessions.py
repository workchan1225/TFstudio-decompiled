# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sessions.pyc (Python 3.11)

from __future__ import annotations
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _base_client import make_request_options
from types.beta.chatkit import ChatSessionWorkflowParam, ChatSessionRateLimitsParam, ChatSessionExpiresAfterParam, ChatSessionChatKitConfigurationParam, session_create_params
from types.beta.chatkit.chat_session import ChatSession
from types.beta.chatkit.chat_session_workflow_param import ChatSessionWorkflowParam
from types.beta.chatkit.chat_session_rate_limits_param import ChatSessionRateLimitsParam
from types.beta.chatkit.chat_session_expires_after_param import ChatSessionExpiresAfterParam
from types.beta.chatkit.chat_session_chatkit_configuration_param import ChatSessionChatKitConfigurationParam
__all__ = [
    'Sessions',
    'AsyncSessions']

class Sessions(SyncAPIResource):
    with_raw_response = (lambda self = None: SessionsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: SessionsWithStreamingResponse(self))()
    
    def create(self = None, *, user, workflow, chatkit_configuration, expires_after, rate_limits, extra_headers, extra_query, extra_body, timeout):
        '''
        Create a ChatKit session

        Args:
          user: A free-form string that identifies your end user; ensures this Session can
              access other objects that have the same `user` scope.

          workflow: Workflow that powers the session.

          chatkit_configuration: Optional overrides for ChatKit runtime configuration features

          expires_after: Optional override for session expiration timing in seconds from creation.
              Defaults to 10 minutes.

          rate_limits: Optional override for per-minute request limits. When omitted, defaults to 10.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def cancel(self = None, session_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Cancel a ChatKit session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        if not session_id:
            raise ValueError(f'''Expected a non-empty value for `session_id` but received {session_id!r}''')
    # WARNING: Decompyle incomplete



class AsyncSessions(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncSessionsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncSessionsWithStreamingResponse(self))()
    
    async def create(self = None, *, user, workflow, chatkit_configuration, expires_after, rate_limits, extra_headers, extra_query, extra_body, timeout):
        '''
        Create a ChatKit session

        Args:
          user: A free-form string that identifies your end user; ensures this Session can
              access other objects that have the same `user` scope.

          workflow: Workflow that powers the session.

          chatkit_configuration: Optional overrides for ChatKit runtime configuration features

          expires_after: Optional override for session expiration timing in seconds from creation.
              Defaults to 10 minutes.

          rate_limits: Optional override for per-minute request limits. When omitted, defaults to 10.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def cancel(self = None, session_id = None, *, extra_headers, extra_query, extra_body, timeout):
        '''
        Cancel a ChatKit session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class SessionsWithRawResponse:
    
    def __init__(self = None, sessions = None):
        self._sessions = sessions
        self.create = _legacy_response.to_raw_response_wrapper(sessions.create)
        self.cancel = _legacy_response.to_raw_response_wrapper(sessions.cancel)



class AsyncSessionsWithRawResponse:
    
    def __init__(self = None, sessions = None):
        self._sessions = sessions
        self.create = _legacy_response.async_to_raw_response_wrapper(sessions.create)
        self.cancel = _legacy_response.async_to_raw_response_wrapper(sessions.cancel)



class SessionsWithStreamingResponse:
    
    def __init__(self = None, sessions = None):
        self._sessions = sessions
        self.create = to_streamed_response_wrapper(sessions.create)
        self.cancel = to_streamed_response_wrapper(sessions.cancel)



class AsyncSessionsWithStreamingResponse:
    
    def __init__(self = None, sessions = None):
        self._sessions = sessions
        self.create = async_to_streamed_response_wrapper(sessions.create)
        self.cancel = async_to_streamed_response_wrapper(sessions.cancel)
