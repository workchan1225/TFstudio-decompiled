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
    type: Literal['conversation.item.create'] = '\n    Add a new Item to the Conversation\'s context, including messages, function\n    calls, and function call responses. This event can be used both to populate a\n    "history" of the conversation and to add new items mid-stream, but has the\n    current limitation that it cannot populate assistant audio messages.\n\n    If successful, the server will respond with a `conversation.item.created`\n    event, otherwise an `error` event will be sent.\n    '
    event_id: Optional[str] = None
    previous_item_id: Optional[str] = None
