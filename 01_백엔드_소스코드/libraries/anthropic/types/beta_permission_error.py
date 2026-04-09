# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_permission_error.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaPermissionError']

class BetaPermissionError(BaseModel):
    type: Literal['permission_error'] = 'BetaPermissionError'
