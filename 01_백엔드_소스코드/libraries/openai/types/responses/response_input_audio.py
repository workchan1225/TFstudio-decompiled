# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_input_audio.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseInputAudio',
    'InputAudio']

class InputAudio(BaseModel):
    format: Literal[('mp3', 'wav')] = 'InputAudio'


class ResponseInputAudio(BaseModel):
    type: Literal['input_audio'] = 'An audio input to the model.'
