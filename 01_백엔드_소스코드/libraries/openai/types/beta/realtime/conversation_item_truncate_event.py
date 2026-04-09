# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_truncate_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ConversationItemTruncateEvent']

class ConversationItemTruncateEvent(BaseModel):
    type: Literal['conversation.item.truncate'] = 'ConversationItemTruncateEvent'
    event_id: Optional[str] = None
