# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_invalid_request_error.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaInvalidRequestError']

class BetaInvalidRequestError(BaseModel):
    type: Literal['invalid_request_error'] = 'BetaInvalidRequestError'
