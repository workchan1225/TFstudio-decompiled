# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_create_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from conversation_item import ConversationItem
__all__ = [
    'ConversationItemCreateEvent']

class ConversationItemCreateEvent(BaseModel):
    type: Literal['conversation.item.create'] = 'ConversationItemCreateEvent'
    event_id: Optional[str] = None
    previous_item_id: Optional[str] = None
