# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_message_function_tool_call.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ChatCompletionMessageFunctionToolCall',
    'Function']

class Function(BaseModel):
    name: str = 'The function that the model called.'


class ChatCompletionMessageFunctionToolCall(BaseModel):
    type: Literal['function'] = 'A call to a function tool created by the model.'
