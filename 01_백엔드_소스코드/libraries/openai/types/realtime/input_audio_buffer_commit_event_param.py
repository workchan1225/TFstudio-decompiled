# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_audio_buffer_commit_event_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'InputAudioBufferCommitEventParam']

def InputAudioBufferCommitEventParam():
    '''InputAudioBufferCommitEventParam'''
    event_id: 'str' = '\n    Send this event to commit the user input audio buffer, which will create a  new user message item in the conversation. This event will produce an error  if the input audio buffer is empty. When in Server VAD mode, the client does  not need to send this event, the server will commit the audio buffer  automatically.\n\n    Committing the input audio buffer will trigger input audio transcription  (if enabled in session configuration), but it will not create a response  from the model. The server will respond with an `input_audio_buffer.committed` event.\n    '

InputAudioBufferCommitEventParam = <NODE:27>(InputAudioBufferCommitEventParam, 'InputAudioBufferCommitEventParam', TypedDict, total = False)
