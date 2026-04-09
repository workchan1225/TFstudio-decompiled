# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_image_gen_call_completed_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseImageGenCallCompletedEvent']

class ResponseImageGenCallCompletedEvent(BaseModel):
    type: Literal['response.image_generation_call.completed'] = '\n    Emitted when an image generation tool call has completed and the final image is available.\n    '
