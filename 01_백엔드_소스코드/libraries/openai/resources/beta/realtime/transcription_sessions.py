# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcription_sessions.pyc (Python 3.11)

from __future__ import annotations
from typing import List
from typing_extensions import Literal
import httpx
from  import _legacy_response
from _types import NOT_GIVEN, Body, Query, Headers, NotGiven
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from _base_client import make_request_options
from types.beta.realtime import transcription_session_create_params
from types.beta.realtime.transcription_session import TranscriptionSession
__all__ = [
    'TranscriptionSessions',
    'AsyncTranscriptionSessions']

class TranscriptionSessions(SyncAPIResource):
    with_raw_response = (lambda self = None: TranscriptionSessionsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: TranscriptionSessionsWithStreamingResponse(self))()
    
    def create(self = None, *, client_secret, include, input_audio_format, input_audio_noise_reduction, input_audio_transcription, modalities, turn_detection, extra_headers, extra_query, extra_body, timeout):
        '''
        Create an ephemeral API token for use in client-side applications with the
        Realtime API specifically for realtime transcriptions. Can be configured with
        the same session parameters as the `transcription_session.update` client event.

        It responds with a session object, plus a `client_secret` key which contains a
        usable ephemeral API token that can be used to authenticate browser clients for
        the Realtime API.

        Args:
          client_secret: Configuration options for the generated client secret.

          include:
              The set of items to include in the transcription. Current available items are:

              - `item.input_audio_transcription.logprobs`

          input_audio_format: The format of input audio. Options are `pcm16`, `g711_ulaw`, or `g711_alaw`. For
              `pcm16`, input audio must be 16-bit PCM at a 24kHz sample rate, single channel
              (mono), and little-endian byte order.

          input_audio_noise_reduction: Configuration for input audio noise reduction. This can be set to `null` to turn
              off. Noise reduction filters audio added to the input audio buffer before it is
              sent to VAD and the model. Filtering the audio can improve VAD and turn
              detection accuracy (reducing false positives) and model performance by improving
              perception of the input audio.

          input_audio_transcription: Configuration for input audio transcription. The client can optionally set the
              language and prompt for transcription, these offer additional guidance to the
              transcription service.

          modalities: The set of modalities the model can respond with. To disable audio, set this to
              ["text"].

          turn_detection: Configuration for turn detection, ether Server VAD or Semantic VAD. This can be
              set to `null` to turn off, in which case the client must manually trigger model
              response. Server VAD means that the model will detect the start and end of
              speech based on audio volume and respond at the end of user speech. Semantic VAD
              is more advanced and uses a turn detection model (in conjunction with VAD) to
              semantically estimate whether the user has finished speaking, then dynamically
              sets a timeout based on this probability. For example, if user audio trails off
              with "uhhm", the model will score a low probability of turn end and wait longer
              for the user to continue speaking. This can be useful for more natural
              conversations, but may have a higher latency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class AsyncTranscriptionSessions(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncTranscriptionSessionsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncTranscriptionSessionsWithStreamingResponse(self))()
    
    async def create(self = None, *, client_secret, include, input_audio_format, input_audio_noise_reduction, input_audio_transcription, modalities, turn_detection, extra_headers, extra_query, extra_body, timeout):
        '''
        Create an ephemeral API token for use in client-side applications with the
        Realtime API specifically for realtime transcriptions. Can be configured with
        the same session parameters as the `transcription_session.update` client event.

        It responds with a session object, plus a `client_secret` key which contains a
        usable ephemeral API token that can be used to authenticate browser clients for
        the Realtime API.

        Args:
          client_secret: Configuration options for the generated client secret.

          include:
              The set of items to include in the transcription. Current available items are:

              - `item.input_audio_transcription.logprobs`

          input_audio_format: The format of input audio. Options are `pcm16`, `g711_ulaw`, or `g711_alaw`. For
              `pcm16`, input audio must be 16-bit PCM at a 24kHz sample rate, single channel
              (mono), and little-endian byte order.

          input_audio_noise_reduction: Configuration for input audio noise reduction. This can be set to `null` to turn
              off. Noise reduction filters audio added to the input audio buffer before it is
              sent to VAD and the model. Filtering the audio can improve VAD and turn
              detection accuracy (reducing false positives) and model performance by improving
              perception of the input audio.

          input_audio_transcription: Configuration for input audio transcription. The client can optionally set the
              language and prompt for transcription, these offer additional guidance to the
              transcription service.

          modalities: The set of modalities the model can respond with. To disable audio, set this to
              ["text"].

          turn_detection: Configuration for turn detection, ether Server VAD or Semantic VAD. This can be
              set to `null` to turn off, in which case the client must manually trigger model
              response. Server VAD means that the model will detect the start and end of
              speech based on audio volume and respond at the end of user speech. Semantic VAD
              is more advanced and uses a turn detection model (in conjunction with VAD) to
              semantically estimate whether the user has finished speaking, then dynamically
              sets a timeout based on this probability. For example, if user audio trails off
              with "uhhm", the model will score a low probability of turn end and wait longer
              for the user to continue speaking. This can be useful for more natural
              conversations, but may have a higher latency.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class TranscriptionSessionsWithRawResponse:
    
    def __init__(self = None, transcription_sessions = None):
        self._transcription_sessions = transcription_sessions
        self.create = _legacy_response.to_raw_response_wrapper(transcription_sessions.create)



class AsyncTranscriptionSessionsWithRawResponse:
    
    def __init__(self = None, transcription_sessions = None):
        self._transcription_sessions = transcription_sessions
        self.create = _legacy_response.async_to_raw_response_wrapper(transcription_sessions.create)



class TranscriptionSessionsWithStreamingResponse:
    
    def __init__(self = None, transcription_sessions = None):
        self._transcription_sessions = transcription_sessions
        self.create = to_streamed_response_wrapper(transcription_sessions.create)



class AsyncTranscriptionSessionsWithStreamingResponse:
    
    def __init__(self = None, transcription_sessions = None):
        self._transcription_sessions = transcription_sessions
        self.create = async_to_streamed_response_wrapper(transcription_sessions.create)
