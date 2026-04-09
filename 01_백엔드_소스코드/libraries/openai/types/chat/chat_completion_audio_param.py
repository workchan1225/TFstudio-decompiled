# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_audio_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ChatCompletionAudioParam']

def ChatCompletionAudioParam():
    '''ChatCompletionAudioParam'''
    voice: "Required[Union[str, Literal['alloy', 'ash', 'ballad', 'coral', 'echo', 'sage', 'shimmer', 'verse', 'marin', 'cedar']]]" = 'Parameters for audio output.\n\n    Required when audio output is requested with\n    `modalities: ["audio"]`. [Learn more](https://platform.openai.com/docs/guides/audio).\n    '

ChatCompletionAudioParam = <NODE:27>(ChatCompletionAudioParam, 'ChatCompletionAudioParam', TypedDict, total = False)
