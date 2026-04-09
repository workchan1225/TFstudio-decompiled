# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_create_event_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
from realtime_response_create_params_param import RealtimeResponseCreateParamsParam
__all__ = [
    'ResponseCreateEventParam']

def ResponseCreateEventParam():
    '''ResponseCreateEventParam'''
    response: 'RealtimeResponseCreateParamsParam' = "\n    This event instructs the server to create a Response, which means triggering\n    model inference. When in Server VAD mode, the server will create Responses\n    automatically.\n\n    A Response will include at least one Item, and may have two, in which case\n    the second will be a function call. These Items will be appended to the\n    conversation history by default.\n\n    The server will respond with a `response.created` event, events for Items\n    and content created, and finally a `response.done` event to indicate the\n    Response is complete.\n\n    The `response.create` event includes inference configuration like\n    `instructions` and `tools`. If these are set, they will override the Session's\n    configuration for this Response only.\n\n    Responses can be created out-of-band of the default Conversation, meaning that they can\n    have arbitrary input, and it's possible to disable writing the output to the Conversation.\n    Only one Response can write to the default Conversation at a time, but otherwise multiple\n    Responses can be created in parallel. The `metadata` field is a good way to disambiguate\n    multiple simultaneous Responses.\n\n    Clients can set `conversation` to `none` to create a Response that does not write to the default\n    Conversation. Arbitrary input can be provided with the `input` field, which is an array accepting\n    raw Items and references to existing Items.\n    "

ResponseCreateEventParam = <NODE:27>(ResponseCreateEventParam, 'ResponseCreateEventParam', TypedDict, total = False)
