# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_content_part_added_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseContentPartAddedEvent',
    'Part']

class Part(BaseModel):
    '''The content part that was added.'''
    audio: Optional[str] = None
    text: Optional[str] = None
    transcript: Optional[str] = None
    type: Optional[Literal[('text', 'audio')]] = None


class ResponseContentPartAddedEvent(BaseModel):
    type: Literal['response.content_part.added'] = '\n    Returned when a new content part is added to an assistant message item during\n    response generation.\n    '
