# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_input_image_content.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseInputImageContent']

class ResponseInputImageContent(BaseModel):
    type: Literal['input_image'] = 'An image input to the model.\n\n    Learn about [image inputs](https://platform.openai.com/docs/guides/vision)\n    '
    detail: Optional[Literal[('low', 'high', 'auto')]] = None
    file_id: Optional[str] = None
    image_url: Optional[str] = None
