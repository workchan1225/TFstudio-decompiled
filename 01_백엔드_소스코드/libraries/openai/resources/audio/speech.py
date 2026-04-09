# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: speech.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from _utils import maybe_transform, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import StreamedBinaryAPIResponse, AsyncStreamedBinaryAPIResponse, to_custom_streamed_response_wrapper, async_to_custom_streamed_response_wrapper
from types.audio import speech_create_params
from _base_client import make_request_options
from types.audio.speech_model import SpeechModel
__all__ = [
    'Speech',
    'AsyncSpeech']

class Speech(SyncAPIResource):
    with_raw_response = (lambda self = None: SpeechWithRawResponse(self))()
    with_streaming_response = (lambda self = None: SpeechWithStreamingResponse(self))()
    
    def create(self = None, *, input, model, voice, instructions, response_format, speed, stream_format, extra_headers, extra_query, extra_body, timeout):
        '''
        Generates audio from the input text.

        Args:
          input: The text to generate audio for. The maximum length is 4096 characters.

          model:
              One of the available [TTS models](https://platform.openai.com/docs/models#tts):
              `tts-1`, `tts-1-hd`, `gpt-4o-mini-tts`, or `gpt-4o-mini-tts-2025-12-15`.

          voice: The voice to use when generating the audio. Supported voices are `alloy`, `ash`,
              `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`, and
              `verse`. Previews of the voices are available in the
              [Text to speech guide](https://platform.openai.com/docs/guides/text-to-speech#voice-options).

          instructions: Control the voice of your generated audio with additional instructions. Does not
              work with `tts-1` or `tts-1-hd`.

          response_format: The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`,
              `wav`, and `pcm`.

          speed: The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is
              the default.

          stream_format: The format to stream the audio in. Supported formats are `sse` and `audio`.
              `sse` is not supported for `tts-1` or `tts-1-hd`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class AsyncSpeech(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncSpeechWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncSpeechWithStreamingResponse(self))()
    
    async def create(self = None, *, input, model, voice, instructions, response_format, speed, stream_format, extra_headers, extra_query, extra_body, timeout):
        '''
        Generates audio from the input text.

        Args:
          input: The text to generate audio for. The maximum length is 4096 characters.

          model:
              One of the available [TTS models](https://platform.openai.com/docs/models#tts):
              `tts-1`, `tts-1-hd`, `gpt-4o-mini-tts`, or `gpt-4o-mini-tts-2025-12-15`.

          voice: The voice to use when generating the audio. Supported voices are `alloy`, `ash`,
              `ballad`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer`, and
              `verse`. Previews of the voices are available in the
              [Text to speech guide](https://platform.openai.com/docs/guides/text-to-speech#voice-options).

          instructions: Control the voice of your generated audio with additional instructions. Does not
              work with `tts-1` or `tts-1-hd`.

          response_format: The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`,
              `wav`, and `pcm`.

          speed: The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is
              the default.

          stream_format: The format to stream the audio in. Supported formats are `sse` and `audio`.
              `sse` is not supported for `tts-1` or `tts-1-hd`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        '''
        pass
    # WARNING: Decompyle incomplete



class SpeechWithRawResponse:
    
    def __init__(self = None, speech = None):
        self._speech = speech
        self.create = _legacy_response.to_raw_response_wrapper(speech.create)



class AsyncSpeechWithRawResponse:
    
    def __init__(self = None, speech = None):
        self._speech = speech
        self.create = _legacy_response.async_to_raw_response_wrapper(speech.create)



class SpeechWithStreamingResponse:
    
    def __init__(self = None, speech = None):
        self._speech = speech
        self.create = to_custom_streamed_response_wrapper(speech.create, StreamedBinaryAPIResponse)



class AsyncSpeechWithStreamingResponse:
    
    def __init__(self = None, speech = None):
        self._speech = speech
        self.create = async_to_custom_streamed_response_wrapper(speech.create, AsyncStreamedBinaryAPIResponse)
