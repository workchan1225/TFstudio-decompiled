# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_deleted.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'MessageDeleted']

class MessageDeleted(BaseModel):
    object: Literal['thread.message.deleted'] = 'MessageDeleted'
