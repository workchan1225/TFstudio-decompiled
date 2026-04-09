# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
TTS 엔진 구현체들

각 TTS 서비스의 BaseTTSEngine 구현체를 제공합니다.

지원 엔진:
- Chirp3 HD: Google Cloud Text-to-Speech
- Edge TTS: Microsoft Edge 무료 TTS
- Google Cloud: Google Cloud Text-to-Speech (표준)
- Gemini Native: Google Gemini 네이티브 TTS
- Qwen3: 로컬 Qwen3 TTS 모델 (API 키 불필요)
- ElevenLabs: ElevenLabs Multilingual v2
- Supertonic: 로컬 ONNX 기반 TTS
'''
__all__ = [
    'Chirp3HDEngine',
    'EdgeEngine',
    'GoogleCloudEngine',
    'GeminiNativeEngine',
    'Qwen3Engine',
    'ElevenLabsEngine',
    'SupertonicEngine']
