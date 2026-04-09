# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_cancel_event_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ResponseCancelEventParam']

def ResponseCancelEventParam():
    '''ResponseCancelEventParam'''
    response_id: 'str' = "Send this event to cancel an in-progress response.\n\n    The server will respond\n    with a `response.done` event with a status of `response.status=cancelled`. If\n    there is no response to cancel, the server will respond with an error. It's safe\n    to call `response.cancel` even if no response is in progress, an error will be\n    returned the session will remain unaffected.\n    "

ResponseCancelEventParam = <NODE:27>(ResponseCancelEventParam, 'ResponseCancelEventParam', TypedDict, total = False)
