# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: custom_tool_input_format.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict
__all__ = [
    'CustomToolInputFormat',
    'Text',
    'Grammar']

def Text():
    '''Text'''
    type: "Required[Literal['text']]" = 'Unconstrained free-form text.'

Text = <NODE:27>(Text, 'Text', TypedDict, total = False)

def Grammar():
    '''Grammar'''
    type: "Required[Literal['grammar']]" = 'A grammar defined by the user.'

Grammar = <NODE:27>(Grammar, 'Grammar', TypedDict, total = False)
CustomToolInputFormat: 'TypeAlias' = Union[(Text, Grammar)]
