# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_session_file_upload.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
__all__ = [
    'ChatSessionFileUpload']

class ChatSessionFileUpload(BaseModel):
    enabled: bool = 'Upload permissions and limits applied to the session.'
    max_file_size: Optional[int] = None
    max_files: Optional[int] = None
