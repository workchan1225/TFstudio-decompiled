# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_allowed_tool_choice_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
from chat_completion_allowed_tools_param import ChatCompletionAllowedToolsParam
__all__ = [
    'ChatCompletionAllowedToolChoiceParam']

def ChatCompletionAllowedToolChoiceParam():
    '''ChatCompletionAllowedToolChoiceParam'''
    type: "Required[Literal['allowed_tools']]" = 'Constrains the tools available to the model to a pre-defined set.'

ChatCompletionAllowedToolChoiceParam = <NODE:27>(ChatCompletionAllowedToolChoiceParam, 'ChatCompletionAllowedToolChoiceParam', TypedDict, total = False)
