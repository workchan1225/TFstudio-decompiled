# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_file_content_block.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from image_file import ImageFile
__all__ = [
    'ImageFileContentBlock']

class ImageFileContentBlock(BaseModel):
    type: Literal['image_file'] = '\n    References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.\n    '
