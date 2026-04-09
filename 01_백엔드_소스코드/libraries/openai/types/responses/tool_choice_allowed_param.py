# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_choice_allowed_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ToolChoiceAllowedParam']

def ToolChoiceAllowedParam():
    '''ToolChoiceAllowedParam'''
    type: "Required[Literal['allowed_tools']]" = 'Constrains the tools available to the model to a pre-defined set.'

ToolChoiceAllowedParam = <NODE:27>(ToolChoiceAllowedParam, 'ToolChoiceAllowedParam', TypedDict, total = False)
