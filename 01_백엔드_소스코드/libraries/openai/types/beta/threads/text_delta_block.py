# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_delta_block.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from text_delta import TextDelta
__all__ = [
    'TextDeltaBlock']

class TextDeltaBlock(BaseModel):
    type: Literal['text'] = 'The text content that is part of a message.'
    text: Optional[TextDelta] = None
