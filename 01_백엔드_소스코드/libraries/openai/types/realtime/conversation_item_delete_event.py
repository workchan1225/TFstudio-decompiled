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
    type: Literal['conversation.item.delete'] = 'Send this event when you want to remove any item from the conversation\n    history.\n\n    The server will respond with a `conversation.item.deleted` event,\n    unless the item does not exist in the conversation history, in which case the\n    server will respond with an error.\n    '
    event_id: Optional[str] = None
