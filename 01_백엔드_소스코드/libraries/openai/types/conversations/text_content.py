# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_content.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'TextContent']

class TextContent(BaseModel):
    type: Literal['text'] = 'A text content.'
