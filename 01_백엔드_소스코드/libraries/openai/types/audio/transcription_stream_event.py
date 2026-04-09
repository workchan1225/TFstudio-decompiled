# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_stream_event.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from transcription_text_done_event import TranscriptionTextDoneEvent
from transcription_text_delta_event import TranscriptionTextDeltaEvent
from transcription_text_segment_event import TranscriptionTextSegmentEvent
__all__ = [
    'TranscriptionStreamEvent']
TranscriptionStreamEvent: TypeAlias = Annotated[(Union[(TranscriptionTextSegmentEvent, TranscriptionTextDeltaEvent, TranscriptionTextDoneEvent)], PropertyInfo(discriminator = 'type'))]
