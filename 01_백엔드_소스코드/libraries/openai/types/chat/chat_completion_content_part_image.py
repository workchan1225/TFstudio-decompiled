# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_content_part_image.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ChatCompletionContentPartImage',
    'ImageURL']

class ImageURL(BaseModel):
    url: str = 'ImageURL'
    detail: Optional[Literal[('auto', 'low', 'high')]] = None


class ChatCompletionContentPartImage(BaseModel):
    type: Literal['image_url'] = 'Learn about [image inputs](https://platform.openai.com/docs/guides/vision).'
