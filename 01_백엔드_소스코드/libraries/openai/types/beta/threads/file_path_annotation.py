# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_path_annotation.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FilePathAnnotation',
    'FilePath']

class FilePath(BaseModel):
    file_id: str = 'FilePath'


class FilePathAnnotation(BaseModel):
    type: Literal['file_path'] = "\n    A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.\n    "
