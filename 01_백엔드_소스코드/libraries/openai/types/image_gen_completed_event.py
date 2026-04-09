# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_gen_completed_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ImageGenCompletedEvent',
    'Usage',
    'UsageInputTokensDetails']

class UsageInputTokensDetails(BaseModel):
    text_tokens: int = 'The input tokens detailed information for the image generation.'


class Usage(BaseModel):
    total_tokens: int = '\n    For the GPT image models only, the token usage information for the image generation.\n    '


class ImageGenCompletedEvent(BaseModel):
    usage: Usage = 'Emitted when image generation has completed and the final image is available.'
