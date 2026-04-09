# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_gen_partial_image_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ImageGenPartialImageEvent']

class ImageGenPartialImageEvent(BaseModel):
    type: Literal['image_generation.partial_image'] = 'Emitted when a partial image is available during image generation streaming.'
