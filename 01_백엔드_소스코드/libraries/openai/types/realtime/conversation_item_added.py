# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_added.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from conversation_item import ConversationItem
__all__ = [
    'ConversationItemAdded']

class ConversationItemAdded(BaseModel):
    type: Literal['conversation.item.added'] = 'Sent by the server when an Item is added to the default Conversation.\n\n    This can happen in several cases:\n    - When the client sends a `conversation.item.create` event.\n    - When the input audio buffer is committed. In this case the item will be a user message containing the audio from the buffer.\n    - When the model is generating a Response. In this case the `conversation.item.added` event will be sent when the model starts generating a specific Item, and thus it will not yet have any content (and `status` will be `in_progress`).\n\n    The event will include the full content of the Item (except when model is generating a Response) except for audio data, which can be retrieved separately with a `conversation.item.retrieve` event if necessary.\n    '
    previous_item_id: Optional[str] = None
