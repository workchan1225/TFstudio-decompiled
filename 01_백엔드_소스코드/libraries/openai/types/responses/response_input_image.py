# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_input_image.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseInputImage']

class ResponseInputImage(BaseModel):
    type: Literal['input_image'] = 'An image input to the model.\n\n    Learn about [image inputs](https://platform.openai.com/docs/guides/vision).\n    '
    file_id: Optional[str] = None
    image_url: Optional[str] = None
