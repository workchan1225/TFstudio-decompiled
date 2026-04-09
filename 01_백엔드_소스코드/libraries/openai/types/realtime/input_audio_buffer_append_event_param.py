# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_audio_buffer_append_event_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'InputAudioBufferAppendEventParam']

def InputAudioBufferAppendEventParam():
    '''InputAudioBufferAppendEventParam'''
    event_id: 'str' = 'Send this event to append audio bytes to the input audio buffer.\n\n    The audio\n    buffer is temporary storage you can write to and later commit. A "commit" will create a new\n    user message item in the conversation history from the buffer content and clear the buffer.\n    Input audio transcription (if enabled) will be generated when the buffer is committed.\n\n    If VAD is enabled the audio buffer is used to detect speech and the server will decide\n    when to commit. When Server VAD is disabled, you must commit the audio buffer\n    manually. Input audio noise reduction operates on writes to the audio buffer.\n\n    The client may choose how much audio to place in each event up to a maximum\n    of 15 MiB, for example streaming smaller chunks from the client may allow the\n    VAD to be more responsive. Unlike most other client events, the server will\n    not send a confirmation response to this event.\n    '

InputAudioBufferAppendEventParam = <NODE:27>(InputAudioBufferAppendEventParam, 'InputAudioBufferAppendEventParam', TypedDict, total = False)
