# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chatkit_thread_assistant_message_item.pyc (Python 3.11)

from typing import List
from typing_extensions import Literal
from _models import BaseModel
from chatkit_response_output_text import ChatKitResponseOutputText
__all__ = [
    'ChatKitThreadAssistantMessageItem']

class ChatKitThreadAssistantMessageItem(BaseModel):
    type: Literal['chatkit.assistant_message'] = 'Assistant-authored message within a thread.'
