# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_transcription_session_create_request_param.pyc (Python 3.11)

from __future__ import annotations
from typing import List
from typing_extensions import Literal, Required, TypedDict
from realtime_transcription_session_audio_param import RealtimeTranscriptionSessionAudioParam
__all__ = [
    'RealtimeTranscriptionSessionCreateRequestParam']

def RealtimeTranscriptionSessionCreateRequestParam():
    '''RealtimeTranscriptionSessionCreateRequestParam'''
    include: "List[Literal['item.input_audio_transcription.logprobs']]" = 'Realtime transcription session object configuration.'

RealtimeTranscriptionSessionCreateRequestParam = <NODE:27>(RealtimeTranscriptionSessionCreateRequestParam, 'RealtimeTranscriptionSessionCreateRequestParam', TypedDict, total = False)
