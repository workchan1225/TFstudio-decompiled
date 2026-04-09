# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcriptions.pyc (Python 3.11)

from __future__ import annotations
import logging
from typing import TYPE_CHECKING, List, Union, Mapping, Optional, cast
from typing_extensions import Literal, overload, assert_never
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from _utils import extract_files, required_args, maybe_transform, deepcopy_minimal, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _streaming import Stream, AsyncStream
from types.audio import transcription_create_params
from _base_client import make_request_options
from types.audio_model import AudioModel
from types.audio.transcription import Transcription
from types.audio_response_format import AudioResponseFormat
from types.audio.transcription_include import TranscriptionInclude
from types.audio.transcription_verbose import TranscriptionVerbose
from types.audio.transcription_diarized import TranscriptionDiarized
from types.audio.transcription_stream_event import TranscriptionStreamEvent
from types.audio.transcription_create_response import TranscriptionCreateResponse
__all__ = [
    'Transcriptions',
    'AsyncTranscriptions']
log: 'logging.Logger' = logging.getLogger('openai.audio.transcriptions')

class Transcriptions(SyncAPIResource):
    with_raw_response = (lambda self = None: TranscriptionsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: TranscriptionsWithStreamingResponse(self))()
    create = (lambda self = None, *, file: pass)()
    create = (lambda self = None, *, file: pass)()
    create = (lambda self = None, *, file: pass)()
    create = (lambda self = None, *, file: pass)()
    create = (lambda self = None, *, file: pass)()
    create = (lambda self = None, *, file: pass)()
    create = (lambda self = None, *, file: body = deepcopy_minimal({
'file': file,
'model': model,
'chunking_strategy': chunking_strategy,
'include': include,
'known_speaker_names': known_speaker_names,
'known_speaker_references': known_speaker_references,
'language': language,
'prompt': prompt,
'response_format': response_format,
'stream': stream,
'temperature': temperature,
'timestamp_granularities': timestamp_granularities })files = extract_files(cast(Mapping[(str, object)], body), paths = [
[
'file']])# WARNING: Decompyle incomplete
)()


class AsyncTranscriptions(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncTranscriptionsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncTranscriptionsWithStreamingResponse(self))()
    create = (lambda self = None, *, file: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, file: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, file: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, file: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, file: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, file: pass# WARNING: Decompyle incomplete
)()


class TranscriptionsWithRawResponse:
    
    def __init__(self = None, transcriptions = None):
        self._transcriptions = transcriptions
        self.create = _legacy_response.to_raw_response_wrapper(transcriptions.create)



class AsyncTranscriptionsWithRawResponse:
    
    def __init__(self = None, transcriptions = None):
        self._transcriptions = transcriptions
        self.create = _legacy_response.async_to_raw_response_wrapper(transcriptions.create)



class TranscriptionsWithStreamingResponse:
    
    def __init__(self = None, transcriptions = None):
        self._transcriptions = transcriptions
        self.create = to_streamed_response_wrapper(transcriptions.create)



class AsyncTranscriptionsWithStreamingResponse:
    
    def __init__(self = None, transcriptions = None):
        self._transcriptions = transcriptions
        self.create = async_to_streamed_response_wrapper(transcriptions.create)



def _get_response_format_type(response_format = None):
    pass
# WARNING: Decompyle incomplete
