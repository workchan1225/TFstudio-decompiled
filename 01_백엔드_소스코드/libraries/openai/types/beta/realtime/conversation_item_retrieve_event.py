# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_retrieve_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ConversationItemRetrieveEvent']

class ConversationItemRetrieveEvent(BaseModel):
    type: Literal['conversation.item.retrieve'] = 'ConversationItemRetrieveEvent'
    event_id: Optional[str] = None
