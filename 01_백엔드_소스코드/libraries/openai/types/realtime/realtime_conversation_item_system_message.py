# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_conversation_item_system_message.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeConversationItemSystemMessage',
    'Content']

class Content(BaseModel):
    text: Optional[str] = None
    type: Optional[Literal['input_text']] = None


class RealtimeConversationItemSystemMessage(BaseModel):
    type: Literal['message'] = '\n    A system message in a Realtime conversation can be used to provide additional context or instructions to the model. This is similar but distinct from the instruction prompt provided at the start of a conversation, as system messages can be added at any point in the conversation. For major changes to the conversation\'s behavior, use instructions, but for smaller updates (e.g. "the user is now asking about a different topic"), use system messages.\n    '
    id: Optional[str] = None
    object: Optional[Literal['realtime.item']] = None
    status: Optional[Literal[('completed', 'incomplete', 'in_progress')]] = None
