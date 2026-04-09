# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_text_block.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from beta_text_citation import BetaTextCitation
__all__ = [
    'BetaTextBlock']

class BetaTextBlock(BaseModel):
    type: Literal['text'] = None
