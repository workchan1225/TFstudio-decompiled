# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: authentication_error.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'AuthenticationError']

class AuthenticationError(BaseModel):
    type: Literal['authentication_error'] = 'AuthenticationError'
