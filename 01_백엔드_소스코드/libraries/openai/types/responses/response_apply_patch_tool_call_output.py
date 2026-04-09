# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_apply_patch_tool_call_output.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseApplyPatchToolCallOutput']

class ResponseApplyPatchToolCallOutput(BaseModel):
    type: Literal['apply_patch_call_output'] = 'The output emitted by an apply patch tool call.'
    created_by: Optional[str] = None
    output: Optional[str] = None
