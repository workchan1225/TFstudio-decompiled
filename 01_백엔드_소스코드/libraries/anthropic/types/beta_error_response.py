# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_error_response.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from beta_error import BetaError
__all__ = [
    'BetaErrorResponse']

class BetaErrorResponse(BaseModel):
    error: BetaError = 'BetaErrorResponse'
    type: Literal['error'] = None
