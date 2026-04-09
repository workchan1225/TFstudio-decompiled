# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: images_response.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from image import Image
from _models import BaseModel
__all__ = [
    'ImagesResponse',
    'Usage',
    'UsageInputTokensDetails',
    'UsageOutputTokensDetails']

class UsageInputTokensDetails(BaseModel):
    text_tokens: int = 'The input tokens detailed information for the image generation.'


class UsageOutputTokensDetails(BaseModel):
    text_tokens: int = 'The output token details for the image generation.'


class Usage(BaseModel):
    total_tokens: int = 'For `gpt-image-1` only, the token usage information for the image generation.'
    output_tokens_details: Optional[UsageOutputTokensDetails] = None


class ImagesResponse(BaseModel):
    created: int = 'The response from the image generation endpoint.'
    background: Optional[Literal[('transparent', 'opaque')]] = None
    data: Optional[List[Image]] = None
    output_format: Optional[Literal[('png', 'webp', 'jpeg')]] = None
    quality: Optional[Literal[('low', 'medium', 'high')]] = None
    size: Optional[Literal[('1024x1024', '1024x1536', '1536x1024')]] = None
    usage: Optional[Usage] = None
