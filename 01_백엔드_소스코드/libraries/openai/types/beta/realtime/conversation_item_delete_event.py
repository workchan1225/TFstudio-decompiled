# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_delete_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ConversationItemDeleteEvent']

class ConversationItemDeleteEvent(BaseModel):
    type: Literal['conversation.item.delete'] = 'ConversationItemDeleteEvent'
    event_id: Optional[str] = None
