# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: summary_text_content.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'SummaryTextContent']

class SummaryTextContent(BaseModel):
    type: Literal['summary_text'] = 'A summary text from the model.'
