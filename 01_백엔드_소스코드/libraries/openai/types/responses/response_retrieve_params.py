# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_retrieve_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Union
from typing_extensions import Literal, Required, TypedDict
from response_includable import ResponseIncludable
__all__ = [
    'ResponseRetrieveParamsBase',
    'ResponseRetrieveParamsNonStreaming',
    'ResponseRetrieveParamsStreaming']

def ResponseRetrieveParamsBase():
    '''ResponseRetrieveParamsBase'''
    starting_after: 'int' = 'ResponseRetrieveParamsBase'

ResponseRetrieveParamsBase = <NODE:27>(ResponseRetrieveParamsBase, 'ResponseRetrieveParamsBase', TypedDict, total = False)

def ResponseRetrieveParamsNonStreaming():
    '''ResponseRetrieveParamsNonStreaming'''
    stream: 'Literal[False]' = 'ResponseRetrieveParamsNonStreaming'

ResponseRetrieveParamsNonStreaming = <NODE:27>(ResponseRetrieveParamsNonStreaming, 'ResponseRetrieveParamsNonStreaming', ResponseRetrieveParamsBase, total = False)

class ResponseRetrieveParamsStreaming(ResponseRetrieveParamsBase):
    stream: 'Required[Literal[True]]' = 'ResponseRetrieveParamsStreaming'

ResponseRetrieveParams = Union[(ResponseRetrieveParamsNonStreaming, ResponseRetrieveParamsStreaming)]
