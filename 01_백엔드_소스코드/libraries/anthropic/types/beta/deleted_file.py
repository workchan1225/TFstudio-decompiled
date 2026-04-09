# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: deleted_file.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'DeletedFile']

class DeletedFile(BaseModel):
    id: str = 'DeletedFile'
    type: Optional[Literal['file_deleted']] = None
