# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_metadata.pyc (Python 3.11)

from typing import Optional
from datetime import datetime
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FileMetadata']

class FileMetadata(BaseModel):
    type: Literal['file'] = 'FileMetadata'
    downloadable: Optional[bool] = None
