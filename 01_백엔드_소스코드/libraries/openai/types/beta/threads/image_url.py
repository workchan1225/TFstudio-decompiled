# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_url.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ImageURL']

class ImageURL(BaseModel):
    url: str = 'ImageURL'
    detail: Optional[Literal[('auto', 'low', 'high')]] = None
