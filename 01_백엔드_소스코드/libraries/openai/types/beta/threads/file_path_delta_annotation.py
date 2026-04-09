# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_path_delta_annotation.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FilePathDeltaAnnotation',
    'FilePath']

class FilePath(BaseModel):
    file_id: Optional[str] = None


class FilePathDeltaAnnotation(BaseModel):
    type: Literal['file_path'] = "\n    A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.\n    "
    end_index: Optional[int] = None
    file_path: Optional[FilePath] = None
    start_index: Optional[int] = None
    text: Optional[str] = None
