# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_audio_buffer_clear_event_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'InputAudioBufferClearEventParam']

def InputAudioBufferClearEventParam():
    '''InputAudioBufferClearEventParam'''
    event_id: 'str' = 'Send this event to clear the audio bytes in the buffer.\n\n    The server will\n    respond with an `input_audio_buffer.cleared` event.\n    '

InputAudioBufferClearEventParam = <NODE:27>(InputAudioBufferClearEventParam, 'InputAudioBufferClearEventParam', TypedDict, total = False)
