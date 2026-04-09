# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_conversation_item_user_message.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeConversationItemUserMessage',
    'Content']

class Content(BaseModel):
    audio: Optional[str] = None
    detail: Optional[Literal[('auto', 'low', 'high')]] = None
    image_url: Optional[str] = None
    text: Optional[str] = None
    transcript: Optional[str] = None
    type: Optional[Literal[('input_text', 'input_audio', 'input_image')]] = None


class RealtimeConversationItemUserMessage(BaseModel):
    type: Literal['message'] = 'A user message item in a Realtime conversation.'
    id: Optional[str] = None
    object: Optional[Literal['realtime.item']] = None
    status: Optional[Literal[('completed', 'incomplete', 'in_progress')]] = None
