# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_audio_input_turn_detection.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'RealtimeAudioInputTurnDetection',
    'ServerVad',
    'SemanticVad']

class ServerVad(BaseModel):
    type: Literal['server_vad'] = '\n    Server-side voice activity detection (VAD) which flips on when user speech is detected and off after a period of silence.\n    '
    create_response: Optional[bool] = None
    idle_timeout_ms: Optional[int] = None
    interrupt_response: Optional[bool] = None
    prefix_padding_ms: Optional[int] = None
    silence_duration_ms: Optional[int] = None
    threshold: Optional[float] = None


class SemanticVad(BaseModel):
    type: Literal['semantic_vad'] = '\n    Server-side semantic turn detection which uses a model to determine when the user has finished speaking.\n    '
    create_response: Optional[bool] = None
    eagerness: Optional[Literal[('low', 'medium', 'high', 'auto')]] = None
    interrupt_response: Optional[bool] = None

RealtimeAudioInputTurnDetection: TypeAlias = Annotated[(Union[(ServerVad, SemanticVad, None)], PropertyInfo(discriminator = 'type'))]
