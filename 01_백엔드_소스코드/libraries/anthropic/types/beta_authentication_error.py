# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_authentication_error.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaAuthenticationError']

class BetaAuthenticationError(BaseModel):
    type: Literal['authentication_error'] = 'BetaAuthenticationError'
