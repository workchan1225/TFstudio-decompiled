# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: permission_retrieve_response.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'PermissionRetrieveResponse',
    'Data']

class Data(BaseModel):
    project_id: str = '\n    The `checkpoint.permission` object represents a permission for a fine-tuned model checkpoint.\n    '


class PermissionRetrieveResponse(BaseModel):
    object: Literal['list'] = 'PermissionRetrieveResponse'
    first_id: Optional[str] = None
    last_id: Optional[str] = None
