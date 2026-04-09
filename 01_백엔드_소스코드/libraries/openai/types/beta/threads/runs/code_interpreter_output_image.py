# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: code_interpreter_output_image.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'CodeInterpreterOutputImage',
    'Image']

class Image(BaseModel):
    file_id: Optional[str] = None


class CodeInterpreterOutputImage(BaseModel):
    type: Literal['image'] = 'CodeInterpreterOutputImage'
    image: Optional[Image] = None
