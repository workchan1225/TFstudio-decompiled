# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from model import Model
from usage import Usage
from _models import BaseModel
from stop_reason import StopReason
from content_block import ContentBlock, ContentBlock
__all__ = [
    'Message']

class Message(BaseModel):
    role: Literal['assistant'] = 'Message'
    stop_reason: Optional[StopReason] = None
    usage: Usage = None
