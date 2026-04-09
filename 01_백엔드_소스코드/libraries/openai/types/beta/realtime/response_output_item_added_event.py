# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_output_item_added_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from conversation_item import ConversationItem
__all__ = [
    'ResponseOutputItemAddedEvent']

class ResponseOutputItemAddedEvent(BaseModel):
    type: Literal['response.output_item.added'] = 'ResponseOutputItemAddedEvent'
