# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_image_gen_call_partial_image_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseImageGenCallPartialImageEvent']

class ResponseImageGenCallPartialImageEvent(BaseModel):
    type: Literal['response.image_generation_call.partial_image'] = 'Emitted when a partial image is available during image generation streaming.'
