# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_named_tool_choice_custom_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ChatCompletionNamedToolChoiceCustomParam',
    'Custom']

def Custom():
    '''Custom'''
    name: 'Required[str]' = 'Custom'

Custom = <NODE:27>(Custom, 'Custom', TypedDict, total = False)

def ChatCompletionNamedToolChoiceCustomParam():
    '''ChatCompletionNamedToolChoiceCustomParam'''
    type: "Required[Literal['custom']]" = 'Specifies a tool the model should use.\n\n    Use to force the model to call a specific custom tool.\n    '

ChatCompletionNamedToolChoiceCustomParam = <NODE:27>(ChatCompletionNamedToolChoiceCustomParam, 'ChatCompletionNamedToolChoiceCustomParam', TypedDict, total = False)
