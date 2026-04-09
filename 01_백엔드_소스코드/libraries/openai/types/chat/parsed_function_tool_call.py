# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parsed_function_tool_call.pyc (Python 3.11)

from typing import Optional
from chat_completion_message_function_tool_call import Function, ChatCompletionMessageFunctionToolCall
__all__ = [
    'ParsedFunctionToolCall',
    'ParsedFunction']

class ParsedFunction(Function):
    parsed_arguments: Optional[object] = None


class ParsedFunctionToolCall(ChatCompletionMessageFunctionToolCall):
    function: ParsedFunction = 'ParsedFunctionToolCall'
