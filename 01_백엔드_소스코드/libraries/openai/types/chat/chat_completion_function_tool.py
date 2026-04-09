# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_function_tool.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from shared.function_definition import FunctionDefinition
__all__ = [
    'ChatCompletionFunctionTool']

class ChatCompletionFunctionTool(BaseModel):
    type: Literal['function'] = 'A function tool that can be used to generate a response.'
