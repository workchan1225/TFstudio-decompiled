# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_format_text.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ResponseFormatText']

def ResponseFormatText():
    '''ResponseFormatText'''
    type: "Required[Literal['text']]" = 'Default response format. Used to generate text responses.'

ResponseFormatText = <NODE:27>(ResponseFormatText, 'ResponseFormatText', TypedDict, total = False)
