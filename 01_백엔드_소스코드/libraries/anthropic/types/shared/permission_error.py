# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: permission_error.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'PermissionError']

class PermissionError(BaseModel):
    type: Literal['permission_error'] = 'PermissionError'
