# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_url_content_block.pyc (Python 3.11)

from typing_extensions import Literal
from image_url import ImageURL
from _models import BaseModel
__all__ = [
    'ImageURLContentBlock']

class ImageURLContentBlock(BaseModel):
    type: Literal['image_url'] = 'References an image URL in the content of a message.'
