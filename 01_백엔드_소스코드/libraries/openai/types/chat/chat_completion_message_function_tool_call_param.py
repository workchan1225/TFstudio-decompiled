# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_message_function_tool_call_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ChatCompletionMessageFunctionToolCallParam',
    'Function']

def Function():
    '''Function'''
    name: 'Required[str]' = 'The function that the model called.'

Function = <NODE:27>(Function, 'Function', TypedDict, total = False)

def ChatCompletionMessageFunctionToolCallParam():
    '''ChatCompletionMessageFunctionToolCallParam'''
    type: "Required[Literal['function']]" = 'A call to a function tool created by the model.'

ChatCompletionMessageFunctionToolCallParam = <NODE:27>(ChatCompletionMessageFunctionToolCallParam, 'ChatCompletionMessageFunctionToolCallParam', TypedDict, total = False)
