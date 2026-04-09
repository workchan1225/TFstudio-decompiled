# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_choice_custom_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ToolChoiceCustomParam']

def ToolChoiceCustomParam():
    '''ToolChoiceCustomParam'''
    type: "Required[Literal['custom']]" = 'Use this option to force the model to call a specific custom tool.'

ToolChoiceCustomParam = <NODE:27>(ToolChoiceCustomParam, 'ToolChoiceCustomParam', TypedDict, total = False)
