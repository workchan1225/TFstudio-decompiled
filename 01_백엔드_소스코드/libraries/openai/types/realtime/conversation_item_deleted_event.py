# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_deleted_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ConversationItemDeletedEvent']

class ConversationItemDeletedEvent(BaseModel):
    type: Literal['conversation.item.deleted'] = "\n    Returned when an item in the conversation is deleted by the client with a\n    `conversation.item.delete` event. This event is used to synchronize the\n    server's understanding of the conversation history with the client's view.\n    "
