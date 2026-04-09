# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_content_part_input_audio_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ChatCompletionContentPartInputAudioParam',
    'InputAudio']

def InputAudio():
    '''InputAudio'''
    format: "Required[Literal['wav', 'mp3']]" = 'InputAudio'

InputAudio = <NODE:27>(InputAudio, 'InputAudio', TypedDict, total = False)

def ChatCompletionContentPartInputAudioParam():
    '''ChatCompletionContentPartInputAudioParam'''
    type: "Required[Literal['input_audio']]" = 'Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).'

ChatCompletionContentPartInputAudioParam = <NODE:27>(ChatCompletionContentPartInputAudioParam, 'ChatCompletionContentPartInputAudioParam', TypedDict, total = False)
