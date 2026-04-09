# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: audio.pyc (Python 3.11)

from __future__ import annotations
from speech import Speech, AsyncSpeech, SpeechWithRawResponse, AsyncSpeechWithRawResponse, SpeechWithStreamingResponse, AsyncSpeechWithStreamingResponse
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from translations import Translations, AsyncTranslations, TranslationsWithRawResponse, AsyncTranslationsWithRawResponse, TranslationsWithStreamingResponse, AsyncTranslationsWithStreamingResponse
from transcriptions import Transcriptions, AsyncTranscriptions, TranscriptionsWithRawResponse, AsyncTranscriptionsWithRawResponse, TranscriptionsWithStreamingResponse, AsyncTranscriptionsWithStreamingResponse
__all__ = [
    'Audio',
    'AsyncAudio']

class Audio(SyncAPIResource):
    transcriptions = (lambda self = None: Transcriptions(self._client))()
    translations = (lambda self = None: Translations(self._client))()
    speech = (lambda self = None: Speech(self._client))()
    with_raw_response = (lambda self = None: AudioWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AudioWithStreamingResponse(self))()


class AsyncAudio(AsyncAPIResource):
    transcriptions = (lambda self = None: AsyncTranscriptions(self._client))()
    translations = (lambda self = None: AsyncTranslations(self._client))()
    speech = (lambda self = None: AsyncSpeech(self._client))()
    with_raw_response = (lambda self = None: AsyncAudioWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncAudioWithStreamingResponse(self))()


class AudioWithRawResponse:
    
    def __init__(self = None, audio = None):
        self._audio = audio

    transcriptions = (lambda self = None: TranscriptionsWithRawResponse(self._audio.transcriptions))()
    translations = (lambda self = None: TranslationsWithRawResponse(self._audio.translations))()
    speech = (lambda self = None: SpeechWithRawResponse(self._audio.speech))()


class AsyncAudioWithRawResponse:
    
    def __init__(self = None, audio = None):
        self._audio = audio

    transcriptions = (lambda self = None: AsyncTranscriptionsWithRawResponse(self._audio.transcriptions))()
    translations = (lambda self = None: AsyncTranslationsWithRawResponse(self._audio.translations))()
    speech = (lambda self = None: AsyncSpeechWithRawResponse(self._audio.speech))()


class AudioWithStreamingResponse:
    
    def __init__(self = None, audio = None):
        self._audio = audio

    transcriptions = (lambda self = None: TranscriptionsWithStreamingResponse(self._audio.transcriptions))()
    translations = (lambda self = None: TranslationsWithStreamingResponse(self._audio.translations))()
    speech = (lambda self = None: SpeechWithStreamingResponse(self._audio.speech))()


class AsyncAudioWithStreamingResponse:
    
    def __init__(self = None, audio = None):
        self._audio = audio

    transcriptions = (lambda self = None: AsyncTranscriptionsWithStreamingResponse(self._audio.transcriptions))()
    translations = (lambda self = None: AsyncTranslationsWithStreamingResponse(self._audio.translations))()
    speech = (lambda self = None: AsyncSpeechWithStreamingResponse(self._audio.speech))()
