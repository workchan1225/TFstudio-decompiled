# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_conversation_item_assistant_message.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeConversationItemAssistantMessage',
    'Content']

class Content(BaseModel):
    audio: Optional[str] = None
    text: Optional[str] = None
    transcript: Optional[str] = None
    type: Optional[Literal[('output_text', 'output_audio')]] = None


class RealtimeConversationItemAssistantMessage(BaseModel):
    type: Literal['message'] = 'An assistant message item in a Realtime conversation.'
    id: Optional[str] = None
    object: Optional[Literal['realtime.item']] = None
    status: Optional[Literal[('completed', 'incomplete', 'in_progress')]] = None
