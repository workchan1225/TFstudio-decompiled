# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: error_object.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
__all__ = [
    'ErrorObject']

class ErrorObject(BaseModel):
    message: str = None
    type: str = None
