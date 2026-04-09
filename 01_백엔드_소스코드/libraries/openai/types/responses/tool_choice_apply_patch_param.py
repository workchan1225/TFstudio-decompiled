# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_choice_apply_patch_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ToolChoiceApplyPatchParam']

def ToolChoiceApplyPatchParam():
    '''ToolChoiceApplyPatchParam'''
    type: "Required[Literal['apply_patch']]" = 'Forces the model to call the apply_patch tool when executing a tool call.'

ToolChoiceApplyPatchParam = <NODE:27>(ToolChoiceApplyPatchParam, 'ToolChoiceApplyPatchParam', TypedDict, total = False)
