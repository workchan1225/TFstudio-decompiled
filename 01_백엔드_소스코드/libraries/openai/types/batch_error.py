# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batch_error.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
__all__ = [
    'BatchError']

class BatchError(BaseModel):
    code: Optional[str] = None
    line: Optional[int] = None
    message: Optional[str] = None
    param: Optional[str] = None
