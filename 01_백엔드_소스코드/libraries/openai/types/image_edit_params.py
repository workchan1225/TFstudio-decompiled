# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_edit_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict
from _types import FileTypes, SequenceNotStr
from image_model import ImageModel
__all__ = [
    'ImageEditParamsBase',
    'ImageEditParamsNonStreaming',
    'ImageEditParamsStreaming']

def ImageEditParamsBase():
    '''ImageEditParamsBase'''
    user: 'str' = 'ImageEditParamsBase'

ImageEditParamsBase = <NODE:27>(ImageEditParamsBase, 'ImageEditParamsBase', TypedDict, total = False)

def ImageEditParamsNonStreaming():
    '''ImageEditParamsNonStreaming'''
    stream: 'Optional[Literal[False]]' = 'ImageEditParamsNonStreaming'

ImageEditParamsNonStreaming = <NODE:27>(ImageEditParamsNonStreaming, 'ImageEditParamsNonStreaming', ImageEditParamsBase, total = False)

class ImageEditParamsStreaming(ImageEditParamsBase):
    stream: 'Required[Literal[True]]' = 'ImageEditParamsStreaming'

ImageEditParams = Union[(ImageEditParamsNonStreaming, ImageEditParamsStreaming)]
