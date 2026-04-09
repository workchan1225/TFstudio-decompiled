# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_object.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FileObject']

class FileObject(BaseModel):
    status: Literal[('uploaded', 'processed', 'error')] = 'The `File` object represents a document that has been uploaded to OpenAI.'
    expires_at: Optional[int] = None
    status_details: Optional[str] = None
