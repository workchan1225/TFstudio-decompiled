# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_choice_function_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ToolChoiceFunctionParam']

def ToolChoiceFunctionParam():
    '''ToolChoiceFunctionParam'''
    type: "Required[Literal['function']]" = 'Use this option to force the model to call a specific function.'

ToolChoiceFunctionParam = <NODE:27>(ToolChoiceFunctionParam, 'ToolChoiceFunctionParam', TypedDict, total = False)
