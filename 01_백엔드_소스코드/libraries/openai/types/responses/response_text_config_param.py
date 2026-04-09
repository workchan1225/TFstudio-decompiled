# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_text_config_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Optional
from typing_extensions import Literal, TypedDict
from response_format_text_config_param import ResponseFormatTextConfigParam
__all__ = [
    'ResponseTextConfigParam']

def ResponseTextConfigParam():
    '''ResponseTextConfigParam'''
    verbosity: "Optional[Literal['low', 'medium', 'high']]" = 'Configuration options for a text response from the model.\n\n    Can be plain\n    text or structured JSON data. Learn more:\n    - [Text inputs and outputs](https://platform.openai.com/docs/guides/text)\n    - [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)\n    '

ResponseTextConfigParam = <NODE:27>(ResponseTextConfigParam, 'ResponseTextConfigParam', TypedDict, total = False)
