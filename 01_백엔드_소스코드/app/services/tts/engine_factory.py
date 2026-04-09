# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: engine_factory.pyc (Python 3.11)

'''
TTS 엔진 팩토리

엔진 타입에 따라 적절한 TTS 엔진 인스턴스를 생성합니다.
'''
import logging
from typing import Dict, Any, Optional, Type
from base_tts_engine import BaseTTSEngine, TTSEngineConfig
logger = logging.getLogger(__name__)
SUPPORTED_ENGINES = [
    'chirp3hd',
    'edge',
    'googlecloud',
    'gemini-native',
    'elevenlabs',
    'supertonic']
_engine_registry: Dict[(str, Type[BaseTTSEngine])] = { }

def register_engine(engine_type = None, engine_class = None):
    '''
    엔진 클래스 등록

    Args:
        engine_type: 엔진 타입 문자열
        engine_class: BaseTTSEngine 상속 클래스
    '''
    _engine_registry[engine_type] = engine_class
    logger.debug(f'''[EngineFactory] 엔진 등록됨: {engine_type}''')


def get_tts_engine(engine_type = None, api_key = None, **kwargs):
    """
    엔진 타입에 맞는 TTS 엔진 인스턴스 반환

    Args:
        engine_type: 엔진 타입 ('chirp3hd', 'edge', 'googlecloud', 'gemini-native', 'elevenlabs', 'supertonic')
        api_key: API 키 (필요한 엔진의 경우)
        **kwargs: 엔진별 추가 파라미터

    Returns:
        BaseTTSEngine: TTS 엔진 인스턴스

    Raises:
        ValueError: 지원하지 않는 엔진 타입
    """
    engine_type = engine_type.lower()
    if engine_type not in SUPPORTED_ENGINES:
        raise ValueError(f'''지원하지 않는 엔진 타입: {engine_type}. 지원: {SUPPORTED_ENGINES}''')
# WARNING: Decompyle incomplete


def get_engine_config(engine_type = None):
    '''
    엔진별 기본 설정 반환

    Args:
        engine_type: 엔진 타입

    Returns:
        Dict: 엔진 설정
    '''
    configs = {
        'chirp3hd': {
            'audio_format': 'mp3',
            'sample_rate': 24000,
            'line_folder_name': 'chirp3hd_single',
            'requires_api_key': True,
            'supports_streaming': True },
        'edge': {
            'audio_format': 'mp3',
            'sample_rate': 24000,
            'line_folder_name': 'edge_single',
            'requires_api_key': False,
            'supports_streaming': True },
        'googlecloud': {
            'audio_format': 'mp3',
            'sample_rate': 24000,
            'line_folder_name': 'googlecloud_single',
            'requires_api_key': True,
            'supports_streaming': True },
        'gemini-native': {
            'audio_format': 'wav',
            'sample_rate': 24000,
            'line_folder_name': 'gemini_native_single',
            'requires_api_key': True,
            'supports_streaming': True },
        'qwen3': {
            'audio_format': 'wav',
            'sample_rate': 24000,
            'line_folder_name': 'qwen3_single',
            'requires_api_key': False,
            'supports_streaming': True },
        'elevenlabs': {
            'audio_format': 'mp3',
            'sample_rate': 44100,
            'line_folder_name': 'elevenlabs_single',
            'requires_api_key': True,
            'supports_streaming': True },
        'supertonic': {
            'audio_format': 'wav',
            'sample_rate': 24000,
            'line_folder_name': 'supertonic_single',
            'requires_api_key': False,
            'supports_streaming': False } }
    engine_type = engine_type.lower()
    if engine_type not in configs:
        raise ValueError(f'''지원하지 않는 엔진 타입: {engine_type}''')
    return configs[engine_type]
