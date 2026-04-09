# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_cancel_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseCancelEvent']

class ResponseCancelEvent(BaseModel):
    type: Literal['response.cancel'] = "Send this event to cancel an in-progress response.\n\n    The server will respond\n    with a `response.done` event with a status of `response.status=cancelled`. If\n    there is no response to cancel, the server will respond with an error. It's safe\n    to call `response.cancel` even if no response is in progress, an error will be\n    returned the session will remain unaffected.\n    "
    event_id: Optional[str] = None
    response_id: Optional[str] = None
