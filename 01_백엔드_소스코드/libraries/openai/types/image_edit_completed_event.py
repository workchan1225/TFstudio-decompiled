# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_edit_completed_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ImageEditCompletedEvent',
    'Usage',
    'UsageInputTokensDetails']

class UsageInputTokensDetails(BaseModel):
    text_tokens: int = 'The input tokens detailed information for the image generation.'


class Usage(BaseModel):
    total_tokens: int = '\n    For the GPT image models only, the token usage information for the image generation.\n    '


class ImageEditCompletedEvent(BaseModel):
    usage: Usage = 'Emitted when image editing has completed and the final image is available.'
