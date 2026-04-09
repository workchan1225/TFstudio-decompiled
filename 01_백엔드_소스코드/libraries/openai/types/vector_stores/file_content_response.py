# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_content_response.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
__all__ = [
    'FileContentResponse']

class FileContentResponse(BaseModel):
    text: Optional[str] = None
    type: Optional[str] = None
