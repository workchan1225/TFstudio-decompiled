# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_created_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from conversation_item import ConversationItem
__all__ = [
    'ConversationItemCreatedEvent']

class ConversationItemCreatedEvent(BaseModel):
    type: Literal['conversation.item.created'] = 'ConversationItemCreatedEvent'
    previous_item_id: Optional[str] = None
