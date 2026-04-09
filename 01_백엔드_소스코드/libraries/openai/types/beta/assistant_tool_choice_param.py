# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: assistant_tool_choice_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
from assistant_tool_choice_function_param import AssistantToolChoiceFunctionParam
__all__ = [
    'AssistantToolChoiceParam']

def AssistantToolChoiceParam():
    '''AssistantToolChoiceParam'''
    function: 'AssistantToolChoiceFunctionParam' = 'Specifies a tool the model should use.\n\n    Use to force the model to call a specific tool.\n    '

AssistantToolChoiceParam = <NODE:27>(AssistantToolChoiceParam, 'AssistantToolChoiceParam', TypedDict, total = False)
