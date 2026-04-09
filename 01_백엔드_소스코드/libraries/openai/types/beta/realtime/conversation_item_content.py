# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_content.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ConversationItemContent']

class ConversationItemContent(BaseModel):
    id: Optional[str] = None
    audio: Optional[str] = None
    text: Optional[str] = None
    transcript: Optional[str] = None
    type: Optional[Literal[('input_text', 'input_audio', 'item_reference', 'text', 'audio')]] = None
