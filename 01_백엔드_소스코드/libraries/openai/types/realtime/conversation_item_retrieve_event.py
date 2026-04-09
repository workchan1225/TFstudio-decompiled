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
    type: Literal['conversation.item.retrieve'] = "\n    Send this event when you want to retrieve the server's representation of a specific item in the conversation history. This is useful, for example, to inspect user audio after noise cancellation and VAD.\n    The server will respond with a `conversation.item.retrieved` event,\n    unless the item does not exist in the conversation history, in which case the\n    server will respond with an error.\n    "
    event_id: Optional[str] = None
