# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_block.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from text_citation import TextCitation
__all__ = [
    'TextBlock']

class TextBlock(BaseModel):
    type: Literal['text'] = None
