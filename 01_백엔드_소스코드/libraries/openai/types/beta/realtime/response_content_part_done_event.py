# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_content_part_done_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseContentPartDoneEvent',
    'Part']

class Part(BaseModel):
    audio: Optional[str] = None
    text: Optional[str] = None
    transcript: Optional[str] = None
    type: Optional[Literal[('text', 'audio')]] = None


class ResponseContentPartDoneEvent(BaseModel):
    type: Literal['response.content_part.done'] = 'ResponseContentPartDoneEvent'
