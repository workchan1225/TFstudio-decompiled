# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_deleted_resource.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ConversationDeletedResource']

class ConversationDeletedResource(BaseModel):
    object: Literal['conversation.deleted'] = 'ConversationDeletedResource'
