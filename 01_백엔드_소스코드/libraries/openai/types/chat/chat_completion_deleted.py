# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_deleted.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ChatCompletionDeleted']

class ChatCompletionDeleted(BaseModel):
    object: Literal['chat.completion.deleted'] = 'ChatCompletionDeleted'
