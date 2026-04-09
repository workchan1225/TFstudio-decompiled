# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_file.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ImageFile']

class ImageFile(BaseModel):
    file_id: str = 'ImageFile'
    detail: Optional[Literal[('auto', 'low', 'high')]] = None
