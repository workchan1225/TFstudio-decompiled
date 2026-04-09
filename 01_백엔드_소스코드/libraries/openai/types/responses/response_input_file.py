# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_input_file.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseInputFile']

class ResponseInputFile(BaseModel):
    type: Literal['input_file'] = 'A file input to the model.'
    file_data: Optional[str] = None
    file_id: Optional[str] = None
    file_url: Optional[str] = None
    filename: Optional[str] = None
