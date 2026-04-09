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
    type: Literal['conversation.item.created'] = 'Returned when a conversation item is created.\n\n    There are several scenarios that produce this event:\n      - The server is generating a Response, which if successful will produce\n        either one or two Items, which will be of type `message`\n        (role `assistant`) or type `function_call`.\n      - The input audio buffer has been committed, either by the client or the\n        server (in `server_vad` mode). The server will take the content of the\n        input audio buffer and add it to a new user message Item.\n      - The client has sent a `conversation.item.create` event to add a new Item\n        to the Conversation.\n    '
    previous_item_id: Optional[str] = None
