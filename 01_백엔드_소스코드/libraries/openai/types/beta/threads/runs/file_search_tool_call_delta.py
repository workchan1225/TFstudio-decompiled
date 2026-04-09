# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_search_tool_call_delta.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FileSearchToolCallDelta']

class FileSearchToolCallDelta(BaseModel):
    type: Literal['file_search'] = 'FileSearchToolCallDelta'
    id: Optional[str] = None
