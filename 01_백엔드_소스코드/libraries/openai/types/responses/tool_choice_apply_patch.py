# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_choice_apply_patch.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ToolChoiceApplyPatch']

class ToolChoiceApplyPatch(BaseModel):
    type: Literal['apply_patch'] = 'Forces the model to call the apply_patch tool when executing a tool call.'
