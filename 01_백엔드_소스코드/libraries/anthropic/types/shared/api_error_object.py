# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: api_error_object.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'APIErrorObject']

class APIErrorObject(BaseModel):
    type: Literal['api_error'] = 'APIErrorObject'
