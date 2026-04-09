# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_not_found_error.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaNotFoundError']

class BetaNotFoundError(BaseModel):
    type: Literal['not_found_error'] = 'BetaNotFoundError'
