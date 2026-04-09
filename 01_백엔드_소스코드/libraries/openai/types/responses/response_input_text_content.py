# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_input_text_content.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseInputTextContent']

class ResponseInputTextContent(BaseModel):
    type: Literal['input_text'] = 'A text input to the model.'
