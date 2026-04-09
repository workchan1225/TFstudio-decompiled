# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_output_message_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from response_output_text_param import ResponseOutputTextParam
from response_output_refusal_param import ResponseOutputRefusalParam
__all__ = [
    'ResponseOutputMessageParam',
    'Content']
Content: 'TypeAlias' = Union[(ResponseOutputTextParam, ResponseOutputRefusalParam)]

def ResponseOutputMessageParam():
    '''ResponseOutputMessageParam'''
    type: "Required[Literal['message']]" = 'An output message from the model.'

ResponseOutputMessageParam = <NODE:27>(ResponseOutputMessageParam, 'ResponseOutputMessageParam', TypedDict, total = False)
