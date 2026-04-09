# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_named_tool_choice_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ChatCompletionNamedToolChoiceParam',
    'Function']

def Function():
    '''Function'''
    name: 'Required[str]' = 'Function'

Function = <NODE:27>(Function, 'Function', TypedDict, total = False)

def ChatCompletionNamedToolChoiceParam():
    '''ChatCompletionNamedToolChoiceParam'''
    type: "Required[Literal['function']]" = 'Specifies a tool the model should use.\n\n    Use to force the model to call a specific function.\n    '

ChatCompletionNamedToolChoiceParam = <NODE:27>(ChatCompletionNamedToolChoiceParam, 'ChatCompletionNamedToolChoiceParam', TypedDict, total = False)
