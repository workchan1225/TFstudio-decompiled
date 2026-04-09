# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: translations.pyc (Python 3.11)

from __future__ import annotations
import logging
from typing import TYPE_CHECKING, Union, Mapping, cast
from typing_extensions import Literal, overload, assert_never
import httpx
from  import _legacy_response
from _types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from _utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from _response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from types.audio import translation_create_params
from _base_client import make_request_options
from types.audio_model import AudioModel
from types.audio.translation import Translation
from types.audio_response_format import AudioResponseFormat
from types.audio.translation_verbose import TranslationVerbose
__all__ = [
    'Translations',
    'AsyncTranslations']
log: 'logging.Logger' = logging.getLogger('openai.audio.transcriptions')

class Translations(SyncAPIResource):
    with_raw_response = (lambda self = None: TranslationsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: TranslationsWithStreamingResponse(self))()
    create = (lambda self = None, *, file: pass)()
    create = (lambda self = None, *, file: pass)()
    create = (lambda self = None, *, file: pass)()
    
    def create(self = None, *, file, model, prompt, response_format, temperature, extra_headers, extra_query, extra_body, timeout):
        """
        Translates audio into English.

        Args:
          file: The audio file object (not file name) translate, in one of these formats: flac,
              mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

          model: ID of the model to use. Only `whisper-1` (which is powered by our open source
              Whisper V2 model) is currently available.

          prompt: An optional text to guide the model's style or continue a previous audio
              segment. The
              [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting)
              should be in English.

          response_format: The format of the output, in one of these options: `json`, `text`, `srt`,
              `verbose_json`, or `vtt`.

          temperature: The sampling temperature, between 0 and 1. Higher values like 0.8 will make the
              output more random, while lower values like 0.2 will make it more focused and
              deterministic. If set to 0, the model will use
              [log probability](https://en.wikipedia.org/wiki/Log_probability) to
              automatically increase the temperature until certain thresholds are hit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({
            'file': file,
            'model': model,
            'prompt': prompt,
            'response_format': response_format,
            'temperature': temperature })
        files = extract_files(cast(Mapping[(str, object)], body), paths = [
            [
                'file']])
    # WARNING: Decompyle incomplete



class AsyncTranslations(AsyncAPIResource):
    with_raw_response = (lambda self = None: AsyncTranslationsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncTranslationsWithStreamingResponse(self))()
    create = (lambda self = None, *, file: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, file: pass# WARNING: Decompyle incomplete
)()
    create = (lambda self = None, *, file: pass# WARNING: Decompyle incomplete
)()
    
    async def create(self = None, *, file, model, prompt, response_format, temperature, extra_headers, extra_query, extra_body, timeout):
        """
        Translates audio into English.

        Args:
          file: The audio file object (not file name) translate, in one of these formats: flac,
              mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

          model: ID of the model to use. Only `whisper-1` (which is powered by our open source
              Whisper V2 model) is currently available.

          prompt: An optional text to guide the model's style or continue a previous audio
              segment. The
              [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting)
              should be in English.

          response_format: The format of the output, in one of these options: `json`, `text`, `srt`,
              `verbose_json`, or `vtt`.

          temperature: The sampling temperature, between 0 and 1. Higher values like 0.8 will make the
              output more random, while lower values like 0.2 will make it more focused and
              deterministic. If set to 0, the model will use
              [log probability](https://en.wikipedia.org/wiki/Log_probability) to
              automatically increase the temperature until certain thresholds are hit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        pass
    # WARNING: Decompyle incomplete



class TranslationsWithRawResponse:
    
    def __init__(self = None, translations = None):
        self._translations = translations
        self.create = _legacy_response.to_raw_response_wrapper(translations.create)



class AsyncTranslationsWithRawResponse:
    
    def __init__(self = None, translations = None):
        self._translations = translations
        self.create = _legacy_response.async_to_raw_response_wrapper(translations.create)



class TranslationsWithStreamingResponse:
    
    def __init__(self = None, translations = None):
        self._translations = translations
        self.create = to_streamed_response_wrapper(translations.create)



class AsyncTranslationsWithStreamingResponse:
    
    def __init__(self = None, translations = None):
        self._translations = translations
        self.create = async_to_streamed_response_wrapper(translations.create)



def _get_response_format_type(response_format = None):
    pass
# WARNING: Decompyle incomplete
