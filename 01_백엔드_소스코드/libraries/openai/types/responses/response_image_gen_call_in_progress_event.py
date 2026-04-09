# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_image_gen_call_in_progress_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseImageGenCallInProgressEvent']

class ResponseImageGenCallInProgressEvent(BaseModel):
    type: Literal['response.image_generation_call.in_progress'] = 'Emitted when an image generation tool call is in progress.'
