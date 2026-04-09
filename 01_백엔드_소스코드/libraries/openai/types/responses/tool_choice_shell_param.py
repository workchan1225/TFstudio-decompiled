# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_choice_shell_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ToolChoiceShellParam']

def ToolChoiceShellParam():
    '''ToolChoiceShellParam'''
    type: "Required[Literal['shell']]" = 'Forces the model to call the shell tool when a tool call is required.'

ToolChoiceShellParam = <NODE:27>(ToolChoiceShellParam, 'ToolChoiceShellParam', TypedDict, total = False)
