# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_text_config.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from response_format_text_config import ResponseFormatTextConfig
__all__ = [
    'ResponseTextConfig']

class ResponseTextConfig(BaseModel):
    '''Configuration options for a text response from the model.

    Can be plain
    text or structured JSON data. Learn more:
    - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
    - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
    '''
    format: Optional[ResponseFormatTextConfig] = None
    verbosity: Optional[Literal[('low', 'medium', 'high')]] = None
