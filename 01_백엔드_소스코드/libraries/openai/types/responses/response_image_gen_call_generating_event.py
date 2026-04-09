# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_image_gen_call_generating_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseImageGenCallGeneratingEvent']

class ResponseImageGenCallGeneratingEvent(BaseModel):
    type: Literal['response.image_generation_call.generating'] = '\n    Emitted when an image generation tool call is actively generating an image (intermediate state).\n    '
