# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_generate_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict
from image_model import ImageModel
__all__ = [
    'ImageGenerateParamsBase',
    'ImageGenerateParamsNonStreaming',
    'ImageGenerateParamsStreaming']

def ImageGenerateParamsBase():
    '''ImageGenerateParamsBase'''
    user: 'str' = 'ImageGenerateParamsBase'

ImageGenerateParamsBase = <NODE:27>(ImageGenerateParamsBase, 'ImageGenerateParamsBase', TypedDict, total = False)

def ImageGenerateParamsNonStreaming():
    '''ImageGenerateParamsNonStreaming'''
    stream: 'Optional[Literal[False]]' = 'ImageGenerateParamsNonStreaming'

ImageGenerateParamsNonStreaming = <NODE:27>(ImageGenerateParamsNonStreaming, 'ImageGenerateParamsNonStreaming', ImageGenerateParamsBase, total = False)

class ImageGenerateParamsStreaming(ImageGenerateParamsBase):
    stream: 'Required[Literal[True]]' = 'ImageGenerateParamsStreaming'

ImageGenerateParams = Union[(ImageGenerateParamsNonStreaming, ImageGenerateParamsStreaming)]
