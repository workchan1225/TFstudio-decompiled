# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_api_error.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaAPIError']

class BetaAPIError(BaseModel):
    type: Literal['api_error'] = 'BetaAPIError'
