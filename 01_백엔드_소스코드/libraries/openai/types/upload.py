# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: upload.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from file_object import FileObject
__all__ = [
    'Upload']

class Upload(BaseModel):
    status: Literal[('pending', 'completed', 'cancelled', 'expired')] = 'The Upload object can accept byte chunks in the form of Parts.'
    file: Optional[FileObject] = None
