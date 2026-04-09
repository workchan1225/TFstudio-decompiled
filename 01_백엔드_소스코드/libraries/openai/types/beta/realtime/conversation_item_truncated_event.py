# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_truncated_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ConversationItemTruncatedEvent']

class ConversationItemTruncatedEvent(BaseModel):
    type: Literal['conversation.item.truncated'] = 'ConversationItemTruncatedEvent'
