# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_created_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ConversationCreatedEvent',
    'Conversation']

class Conversation(BaseModel):
    id: Optional[str] = None
    object: Optional[Literal['realtime.conversation']] = None


class ConversationCreatedEvent(BaseModel):
    type: Literal['conversation.created'] = 'ConversationCreatedEvent'
