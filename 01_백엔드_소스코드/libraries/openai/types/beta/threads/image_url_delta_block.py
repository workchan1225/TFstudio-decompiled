# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_url_delta_block.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from image_url_delta import ImageURLDelta
__all__ = [
    'ImageURLDeltaBlock']

class ImageURLDeltaBlock(BaseModel):
    type: Literal['image_url'] = 'References an image URL in the content of a message.'
    image_url: Optional[ImageURLDelta] = None
