# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chatkit_attachment.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ChatKitAttachment']

class ChatKitAttachment(BaseModel):
    name: str = 'Attachment metadata included on thread items.'
    type: Literal[('image', 'file')] = None
