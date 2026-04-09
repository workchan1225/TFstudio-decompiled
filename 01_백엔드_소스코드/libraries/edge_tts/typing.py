# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typing.pyc (Python 3.11)

'''Custom types for edge-tts.'''
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict

class TTSChunk(TypedDict):
    text: NotRequired[str] = 'TTS chunk data.'


class VoiceTag(TypedDict):
    VoicePersonalities: List[str] = 'VoiceTag data.'


class Voice(TypedDict):
    VoiceTag: VoiceTag = 'Voice data.'


class VoicesManagerVoice(Voice):
    Language: str = 'Voice data for VoicesManager.'


class VoicesManagerFind(TypedDict):
    Language: NotRequired[str] = 'Voice data for VoicesManager.find().'


class CommunicateState(TypedDict):
    stream_was_called: bool = 'Communicate state data.'
