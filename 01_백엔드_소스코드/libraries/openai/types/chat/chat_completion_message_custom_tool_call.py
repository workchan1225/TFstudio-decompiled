# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_message_custom_tool_call.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ChatCompletionMessageCustomToolCall',
    'Custom']

class Custom(BaseModel):
    name: str = 'The custom tool that the model called.'


class ChatCompletionMessageCustomToolCall(BaseModel):
    type: Literal['custom'] = 'A call to a custom tool created by the model.'
