# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: apply_patch_tool.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ApplyPatchTool']

class ApplyPatchTool(BaseModel):
    type: Literal['apply_patch'] = 'Allows the assistant to create, delete, or update files using unified diffs.'
