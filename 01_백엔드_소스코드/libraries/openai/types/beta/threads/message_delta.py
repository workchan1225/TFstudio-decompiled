# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_delta.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from message_content_delta import MessageContentDelta
__all__ = [
    'MessageDelta']

class MessageDelta(BaseModel):
    '''The delta containing the fields that have changed on the Message.'''
    content: Optional[List[MessageContentDelta]] = None
    role: Optional[Literal[('user', 'assistant')]] = None
