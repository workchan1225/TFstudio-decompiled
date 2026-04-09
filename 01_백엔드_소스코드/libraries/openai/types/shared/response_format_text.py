# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_format_text.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseFormatText']

class ResponseFormatText(BaseModel):
    type: Literal['text'] = 'Default response format. Used to generate text responses.'
