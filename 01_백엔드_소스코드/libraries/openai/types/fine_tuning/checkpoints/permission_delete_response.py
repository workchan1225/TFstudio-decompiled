# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: permission_delete_response.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'PermissionDeleteResponse']

class PermissionDeleteResponse(BaseModel):
    object: Literal['checkpoint.permission'] = 'PermissionDeleteResponse'
