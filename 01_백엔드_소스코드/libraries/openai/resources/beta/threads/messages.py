# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: messages.pyc (Python 3.11)

from __future__ import annotations
import typing_extensions
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
from _base_client import AsyncPaginator, make_request_options
from types.beta.threads import message_list_params, message_create_params, message_update_params
from types.beta.threads.message import Message
from types.shared_params.metadata import Metadata
from types.beta.threads.message_deleted import MessageDeleted
from types.beta.threads.message_content_part_param import MessageContentPartParam
__all__ = [
    'Messages',
    'AsyncMessages']

class Messages(SyncAPIResource):
    with_raw_response = (lambda self = None: MessagesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: MessagesWithStreamingResponse(self))()
    create = (lambda self = None, thread_id = None, *, content, role: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()
    retrieve = (lambda self = None, message_id = None, *, thread_id, extra_headers: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')if not message_id:
raise ValueError(f'''Expected a non-empty value for `message_id` but received {message_id!r}''')# WARNING: Decompyle incomplete
)()
    update = (lambda self = None, message_id = None, *, thread_id, metadata: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')if not message_id:
raise ValueError(f'''Expected a non-empty value for `message_id` but received {message_id!r}''')# WARNING: Decompyle incomplete
)()
    list = (lambda self = None, thread_id = None, *, after, before: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()
    delete = (lambda self = None, message_id = None, *, thread_id, extra_headers: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')if not message_id:
raise ValueError(f'''Expected a non-empty value for `message_id` but received {message_id!r}''')# WARNING: Decompyle incomplete
)()


class AsyncMessages(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncMessagesWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncMessagesWithStreamingResponse(self))()
    create = (lambda self = None, thread_id = None, *, content, role: pass# WARNING: Decompyle incomplete
)()
    retrieve = (lambda self = None, message_id = None, *, thread_id, extra_headers: pass# WARNING: Decompyle incomplete
)()
    update = (lambda self = None, message_id = None, *, thread_id, metadata: pass# WARNING: Decompyle incomplete
)()
    list = (lambda self = None, thread_id = None, *, after, before: if not thread_id:
raise ValueError(f'''Expected a non-empty value for `thread_id` but received {thread_id!r}''')# WARNING: Decompyle incomplete
)()
    delete = (lambda self = None, message_id = None, *, thread_id, extra_headers: pass# WARNING: Decompyle incomplete
)()


class MessagesWithRawResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.create = _legacy_response.to_raw_response_wrapper(messages.create)
        self.retrieve = _legacy_response.to_raw_response_wrapper(messages.retrieve)
        self.update = _legacy_response.to_raw_response_wrapper(messages.update)
        self.list = _legacy_response.to_raw_response_wrapper(messages.list)
        self.delete = _legacy_response.to_raw_response_wrapper(messages.delete)



class AsyncMessagesWithRawResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.create = _legacy_response.async_to_raw_response_wrapper(messages.create)
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(messages.retrieve)
        self.update = _legacy_response.async_to_raw_response_wrapper(messages.update)
        self.list = _legacy_response.async_to_raw_response_wrapper(messages.list)
        self.delete = _legacy_response.async_to_raw_response_wrapper(messages.delete)



class MessagesWithStreamingResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.create = to_streamed_response_wrapper(messages.create)
        self.retrieve = to_streamed_response_wrapper(messages.retrieve)
        self.update = to_streamed_response_wrapper(messages.update)
        self.list = to_streamed_response_wrapper(messages.list)
        self.delete = to_streamed_response_wrapper(messages.delete)



class AsyncMessagesWithStreamingResponse:
    
    def __init__(self = None, messages = None):
        self._messages = messages
        self.create = async_to_streamed_response_wrapper(messages.create)
        self.retrieve = async_to_streamed_response_wrapper(messages.retrieve)
        self.update = async_to_streamed_response_wrapper(messages.update)
        self.list = async_to_streamed_response_wrapper(messages.list)
        self.delete = async_to_streamed_response_wrapper(messages.delete)
