# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_message_tool_call.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from chat_completion_message_custom_tool_call import ChatCompletionMessageCustomToolCall
from chat_completion_message_function_tool_call import Function, ChatCompletionMessageFunctionToolCall
__all__ = [
    'Function',
    'ChatCompletionMessageToolCallUnion']
ChatCompletionMessageToolCallUnion: TypeAlias = Annotated[(Union[(ChatCompletionMessageFunctionToolCall, ChatCompletionMessageCustomToolCall)], PropertyInfo(discriminator = 'type'))]
ChatCompletionMessageToolCall: TypeAlias = ChatCompletionMessageFunctionToolCall
