# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_apply_patch_tool_call.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'ResponseApplyPatchToolCall',
    'Operation',
    'OperationCreateFile',
    'OperationDeleteFile',
    'OperationUpdateFile']

class OperationCreateFile(BaseModel):
    type: Literal['create_file'] = 'Instruction describing how to create a file via the apply_patch tool.'


class OperationDeleteFile(BaseModel):
    type: Literal['delete_file'] = 'Instruction describing how to delete a file via the apply_patch tool.'


class OperationUpdateFile(BaseModel):
    type: Literal['update_file'] = 'Instruction describing how to update a file via the apply_patch tool.'

Operation: TypeAlias = Annotated[(Union[(OperationCreateFile, OperationDeleteFile, OperationUpdateFile)], PropertyInfo(discriminator = 'type'))]

class ResponseApplyPatchToolCall(BaseModel):
    type: Literal['apply_patch_call'] = 'A tool call that applies file diffs by creating, deleting, or updating files.'
    created_by: Optional[str] = None
