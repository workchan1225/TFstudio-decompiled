# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_content_part_image_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ChatCompletionContentPartImageParam',
    'ImageURL']

def ImageURL():
    '''ImageURL'''
    detail: "Literal['auto', 'low', 'high']" = 'ImageURL'

ImageURL = <NODE:27>(ImageURL, 'ImageURL', TypedDict, total = False)

def ChatCompletionContentPartImageParam():
    '''ChatCompletionContentPartImageParam'''
    type: "Required[Literal['image_url']]" = 'Learn about [image inputs](https://platform.openai.com/docs/guides/vision).'

ChatCompletionContentPartImageParam = <NODE:27>(ChatCompletionContentPartImageParam, 'ChatCompletionContentPartImageParam', TypedDict, total = False)
