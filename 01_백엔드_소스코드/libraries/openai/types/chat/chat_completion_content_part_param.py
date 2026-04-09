# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_content_part_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from chat_completion_content_part_text_param import ChatCompletionContentPartTextParam
from chat_completion_content_part_image_param import ChatCompletionContentPartImageParam
from chat_completion_content_part_input_audio_param import ChatCompletionContentPartInputAudioParam
__all__ = [
    'ChatCompletionContentPartParam',
    'File',
    'FileFile']

def FileFile():
    '''FileFile'''
    filename: 'str' = 'FileFile'

FileFile = <NODE:27>(FileFile, 'FileFile', TypedDict, total = False)

def File():
    '''File'''
    type: "Required[Literal['file']]" = '\n    Learn about [file inputs](https://platform.openai.com/docs/guides/text) for text generation.\n    '

File = <NODE:27>(File, 'File', TypedDict, total = False)
ChatCompletionContentPartParam: 'TypeAlias' = Union[(ChatCompletionContentPartTextParam, ChatCompletionContentPartImageParam, ChatCompletionContentPartInputAudioParam, File)]
