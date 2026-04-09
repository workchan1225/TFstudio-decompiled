# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_url_delta.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ImageURLDelta']

class ImageURLDelta(BaseModel):
    detail: Optional[Literal[('auto', 'low', 'high')]] = None
    url: Optional[str] = None
