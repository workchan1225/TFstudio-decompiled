# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: google_sdk.pyc (Python 3.11)

'''
Google AI SDK 래퍼 유틸리티

개발환경과 EXE 빌드환경에서 일관된 SDK 로딩을 보장합니다.

SDK 구분:
- google-genai (신규 SDK): TTS, 멀티모달 기능용
- google-generativeai (레거시 SDK): 텍스트 생성용 (기존 코드 호환)

Usage:
    from app.utils.google_sdk import (
        get_genai_client,
        get_genai_types,
        get_legacy_genai,
        is_new_sdk_available,
        is_legacy_sdk_available,
        GOOGLE_SDK_ERROR_MESSAGE
    )
'''
import logging
from io import BytesIO
from typing import Optional, Any, Tuple
from app.services.google_auth_service import GOOGLE_AUTH_MODE_VERTEX_AI, GoogleAuthConfig, GoogleAuthValidation, get_google_service_account_credentials, resolve_google_auth_config
logger = logging.getLogger(__name__)
_NEW_SDK_AVAILABLE = False
_LEGACY_SDK_AVAILABLE = False
_LEGACY_SDK_ATTEMPTED = False
_NEW_SDK_CLIENT = None
_NEW_SDK_TYPES = None
_LEGACY_SDK = None
_LEGACY_RUNTIME_MODULE = None
GOOGLE_SDK_ERROR_MESSAGE = 'Google AI SDK가 설치되지 않았습니다. 다음 명령어로 설치하세요: pip install google-genai google-generativeai'
NEW_SDK_ERROR_MESSAGE = 'google-genai SDK가 필요합니다. 설치: pip install google-genai'
LEGACY_SDK_ERROR_MESSAGE = 'google-generativeai SDK가 필요합니다. 설치: pip install google-generativeai'

def _load_new_sdk():
    '''신규 SDK (google-genai) 로드'''
    global _NEW_SDK_CLIENT, _NEW_SDK_TYPES, _NEW_SDK_AVAILABLE, _NEW_SDK_AVAILABLE
    
    try:
        genai = genai
        import google
        types = types
        import google.genai
        _NEW_SDK_CLIENT = genai
        _NEW_SDK_TYPES = types
        _NEW_SDK_AVAILABLE = True
        logger.info('[GoogleSDK] google-genai SDK 로드 완료 (신규)')
        return None
    except ImportError:
        e = None
        logger.debug(f'''[GoogleSDK] google-genai SDK 로드 실패: {e}''')
        _NEW_SDK_AVAILABLE = False
        e = None
        del e
        return None
        e = None
        del e



def _load_legacy_sdk():
    '''레거시 SDK (google-generativeai) 로드'''
    global _LEGACY_SDK_ATTEMPTED, _LEGACY_SDK, _LEGACY_SDK_AVAILABLE, _LEGACY_SDK_AVAILABLE
    if _LEGACY_SDK_ATTEMPTED:
        return None
    _LEGACY_SDK_ATTEMPTED = None
    
    try:
        genai_legacy = generativeai
        import google.generativeai
        _LEGACY_SDK = genai_legacy
        _LEGACY_SDK_AVAILABLE = True
        logger.info('[GoogleSDK] google-generativeai SDK 로드 완료 (레거시)')
        return None
    except ImportError:
        e = None
        logger.debug(f'''[GoogleSDK] google-generativeai SDK 로드 실패: {e}''')
        _LEGACY_SDK_AVAILABLE = False
        e = None
        del e
        return None
        e = None
        del e


_load_new_sdk()

class _LegacyCompatibleImage:
    '''Minimal image wrapper used by legacy call sites.'''
    
    def __init__(self = None, image_bytes = None):
        self._image_bytes = image_bytes

    
    def save(self = None, output_path = None):
        import PIL.Image as PIL
        image = PIL.Image.open(BytesIO(self._image_bytes))
        image.save(output_path)



class _LegacyCompatibleResponse:
    '''Provide legacy-style response attributes over google-genai responses.'''
    
    def __init__(self = None, response = None):
