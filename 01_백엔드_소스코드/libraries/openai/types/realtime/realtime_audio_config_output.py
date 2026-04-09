# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_audio_config_output.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Literal
from _models import BaseModel
from realtime_audio_formats import RealtimeAudioFormats
__all__ = [
    'RealtimeAudioConfigOutput']

class RealtimeAudioConfigOutput(BaseModel):
    format: Optional[RealtimeAudioFormats] = None
    speed: Optional[float] = None
    voice: Union[(str, Literal[('alloy', 'ash', 'ballad', 'coral', 'echo', 'sage', 'shimmer', 'verse', 'marin', 'cedar')], None)] = None
