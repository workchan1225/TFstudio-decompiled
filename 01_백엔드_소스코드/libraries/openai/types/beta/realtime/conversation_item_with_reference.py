# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_with_reference.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ConversationItemWithReference',
    'Content']

class Content(BaseModel):
    id: Optional[str] = None
    audio: Optional[str] = None
    text: Optional[str] = None
    transcript: Optional[str] = None
    type: Optional[Literal[('input_text', 'input_audio', 'item_reference', 'text')]] = None


class ConversationItemWithReference(BaseModel):
    id: Optional[str] = None
    arguments: Optional[str] = None
    call_id: Optional[str] = None
    content: Optional[List[Content]] = None
    name: Optional[str] = None
    object: Optional[Literal['realtime.item']] = None
    output: Optional[str] = None
    role: Optional[Literal[('user', 'assistant', 'system')]] = None
    status: Optional[Literal[('completed', 'incomplete', 'in_progress')]] = None
    type: Optional[Literal[('message', 'function_call', 'function_call_output', 'item_reference')]] = None
