# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_input_message_item.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from response_input_message_content_list import ResponseInputMessageContentList
__all__ = [
    'ResponseInputMessageItem']

class ResponseInputMessageItem(BaseModel):
    role: Literal[('user', 'system', 'developer')] = 'ResponseInputMessageItem'
    status: Optional[Literal[('in_progress', 'completed', 'incomplete')]] = None
    type: Optional[Literal['message']] = None
