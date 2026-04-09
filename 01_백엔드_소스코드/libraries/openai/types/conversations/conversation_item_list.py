# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_list.pyc (Python 3.11)

from typing import List
from typing_extensions import Literal
from _models import BaseModel
from conversation_item import ConversationItem
__all__ = [
    'ConversationItemList']

class ConversationItemList(BaseModel):
    object: Literal['list'] = 'A list of Conversation items.'
