# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_truncated_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ConversationItemTruncatedEvent']

class ConversationItemTruncatedEvent(BaseModel):
    type: Literal['conversation.item.truncated'] = "\n    Returned when an earlier assistant audio message item is truncated by the\n    client with a `conversation.item.truncate` event. This event is used to\n    synchronize the server's understanding of the audio with the client's playback.\n\n    This action will truncate the audio and remove the server-side text transcript\n    to ensure there is no text in the context that hasn't been heard by the user.\n    "
