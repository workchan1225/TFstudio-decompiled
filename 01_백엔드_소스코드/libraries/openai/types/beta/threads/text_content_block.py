# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_content_block.pyc (Python 3.11)

from typing_extensions import Literal
from text import Text
from _models import BaseModel
__all__ = [
    'TextContentBlock']

class TextContentBlock(BaseModel):
    type: Literal['text'] = 'The text content that is part of a message.'
