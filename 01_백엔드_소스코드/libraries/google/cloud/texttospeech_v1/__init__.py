# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from google.cloud.texttospeech_v1 import gapic_version as package_version
__version__ = package_version.__version__
from services.text_to_speech import TextToSpeechAsyncClient, TextToSpeechClient
from services.text_to_speech_long_audio_synthesize import TextToSpeechLongAudioSynthesizeAsyncClient, TextToSpeechLongAudioSynthesizeClient
from types.cloud_tts import AdvancedVoiceOptions, AudioConfig, AudioEncoding, CustomPronunciationParams, CustomPronunciations, CustomVoiceParams, ListVoicesRequest, ListVoicesResponse, MultiSpeakerMarkup, MultispeakerPrebuiltVoice, MultiSpeakerVoiceConfig, SsmlVoiceGender, StreamingAudioConfig, StreamingSynthesisInput, StreamingSynthesizeConfig, StreamingSynthesizeRequest, StreamingSynthesizeResponse, SynthesisInput, SynthesizeSpeechRequest, SynthesizeSpeechResponse, Voice, VoiceCloneParams, VoiceSelectionParams
from types.cloud_tts_lrs import SynthesizeLongAudioMetadata, SynthesizeLongAudioRequest, SynthesizeLongAudioResponse
__all__ = ('TextToSpeechAsyncClient', 'TextToSpeechLongAudioSynthesizeAsyncClient', 'AdvancedVoiceOptions', 'AudioConfig', 'AudioEncoding', 'CustomPronunciationParams', 'CustomPronunciations', 'CustomVoiceParams', 'ListVoicesRequest', 'ListVoicesResponse', 'MultiSpeakerMarkup', 'MultiSpeakerVoiceConfig', 'MultispeakerPrebuiltVoice', 'SsmlVoiceGender', 'StreamingAudioConfig', 'StreamingSynthesisInput', 'StreamingSynthesizeConfig', 'StreamingSynthesizeRequest', 'StreamingSynthesizeResponse', 'SynthesisInput', 'SynthesizeLongAudioMetadata', 'SynthesizeLongAudioRequest', 'SynthesizeLongAudioResponse', 'SynthesizeSpeechRequest', 'SynthesizeSpeechResponse', 'TextToSpeechClient', 'TextToSpeechLongAudioSynthesizeClient', 'Voice', 'VoiceCloneParams', 'VoiceSelectionParams')
