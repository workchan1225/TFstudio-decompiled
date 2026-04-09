# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_message_custom_tool_call_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ChatCompletionMessageCustomToolCallParam',
    'Custom']

def Custom():
    '''Custom'''
    name: 'Required[str]' = 'The custom tool that the model called.'

Custom = <NODE:27>(Custom, 'Custom', TypedDict, total = False)

def ChatCompletionMessageCustomToolCallParam():
    '''ChatCompletionMessageCustomToolCallParam'''
    type: "Required[Literal['custom']]" = 'A call to a custom tool created by the model.'

ChatCompletionMessageCustomToolCallParam = <NODE:27>(ChatCompletionMessageCustomToolCallParam, 'ChatCompletionMessageCustomToolCallParam', TypedDict, total = False)
