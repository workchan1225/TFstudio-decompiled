# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from google.cloud.texttospeech import gapic_version as package_version
__version__ = package_version.__version__
from google.cloud.texttospeech_v1.services.text_to_speech.async_client import TextToSpeechAsyncClient
from google.cloud.texttospeech_v1.services.text_to_speech.client import TextToSpeechClient
from google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.async_client import TextToSpeechLongAudioSynthesizeAsyncClient
from google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.client import TextToSpeechLongAudioSynthesizeClient
from google.cloud.texttospeech_v1.types.cloud_tts import AdvancedVoiceOptions, AudioConfig, AudioEncoding, CustomPronunciationParams, CustomPronunciations, CustomVoiceParams, ListVoicesRequest, ListVoicesResponse, MultiSpeakerMarkup, MultispeakerPrebuiltVoice, MultiSpeakerVoiceConfig, SsmlVoiceGender, StreamingAudioConfig, StreamingSynthesisInput, StreamingSynthesizeConfig, StreamingSynthesizeRequest, StreamingSynthesizeResponse, SynthesisInput, SynthesizeSpeechRequest, SynthesizeSpeechResponse, Voice, VoiceCloneParams, VoiceSelectionParams
from google.cloud.texttospeech_v1.types.cloud_tts_lrs import SynthesizeLongAudioMetadata, SynthesizeLongAudioRequest, SynthesizeLongAudioResponse
__all__ = ('TextToSpeechClient', 'TextToSpeechAsyncClient', 'TextToSpeechLongAudioSynthesizeClient', 'TextToSpeechLongAudioSynthesizeAsyncClient', 'AdvancedVoiceOptions', 'AudioConfig', 'CustomPronunciationParams', 'CustomPronunciations', 'CustomVoiceParams', 'ListVoicesRequest', 'ListVoicesResponse', 'MultiSpeakerMarkup', 'MultispeakerPrebuiltVoice', 'MultiSpeakerVoiceConfig', 'StreamingAudioConfig', 'StreamingSynthesisInput', 'StreamingSynthesizeConfig', 'StreamingSynthesizeRequest', 'StreamingSynthesizeResponse', 'SynthesisInput', 'SynthesizeSpeechRequest', 'SynthesizeSpeechResponse', 'Voice', 'VoiceCloneParams', 'VoiceSelectionParams', 'AudioEncoding', 'SsmlVoiceGender', 'SynthesizeLongAudioMetadata', 'SynthesizeLongAudioRequest', 'SynthesizeLongAudioResponse')
