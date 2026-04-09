# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_done.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from conversation_item import ConversationItem
__all__ = [
    'ConversationItemDone']

class ConversationItemDone(BaseModel):
    type: Literal['conversation.item.done'] = 'Returned when a conversation item is finalized.\n\n    The event will include the full content of the Item except for audio data, which can be retrieved separately with a `conversation.item.retrieve` event if needed.\n    '
    previous_item_id: Optional[str] = None
