# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_output_item_done_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from conversation_item import ConversationItem
__all__ = [
    'ResponseOutputItemDoneEvent']

class ResponseOutputItemDoneEvent(BaseModel):
    type: Literal['response.output_item.done'] = 'Returned when an Item is done streaming.\n\n    Also emitted when a Response is\n    interrupted, incomplete, or cancelled.\n    '
