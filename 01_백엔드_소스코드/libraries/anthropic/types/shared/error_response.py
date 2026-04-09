# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: error_response.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from error_object import ErrorObject
__all__ = [
    'ErrorResponse']

class ErrorResponse(BaseModel):
    error: ErrorObject = 'ErrorResponse'
    type: Literal['error'] = None
