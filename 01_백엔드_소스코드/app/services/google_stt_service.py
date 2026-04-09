# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: google_stt_service.pyc (Python 3.11)

'''
Google Cloud Speech-to-Text 서비스 (단순화 버전)
단어 단위 타임스탬프를 사용한 고정밀 자막 생성

REST API 사용 (Google auth mode에 따라 API 키 또는 Vertex 인증)
'''
import logging
import os
import re
import sys
import base64
import requests
import subprocess
import tempfile
from pathlib import Path
from typing import Optional, List, Dict, Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from app.utils.script_text_cleaner import clean_script_for_subtitle, get_clean_words
from app.utils.ffmpeg_utils import get_ffmpeg_executable, probe_media_duration
from app.services.google_auth_service import build_google_rest_headers, get_google_api_key_or_runtime_token, get_google_configuration_error_message, resolve_google_auth_config
logger = logging.getLogger(__name__)

def log_debug(msg = None):
    '''디버그 로그 출력'''
    print(f'''[GoogleSTT] {msg}''')
    logger.info(msg)

GOOGLE_STT_API_URL = 'https://speech.googleapis.com/v1/speech:recognize'
MAX_SYNC_DURATION = 55
CHUNK_DURATION = 50
SILENCE_PADDING = 1
DEFAULT_STT_API_CHECK_TIMEOUT_SEC = 300
DEFAULT_STT_REQUEST_TIMEOUT_SEC = 1800
_MULTI_SPACE_PATTERN = re.compile('\\s+')
_UNDERSCORE_PATTERN = re.compile('[_\\u2581\\uff3f]+')
_KOREAN_CHAR_SPACE_PATTERN = re.compile('(?<=[\\uAC00-\\uD7AF\\u0030-\\u0039]) (?=[\\uAC00-\\uD7AF\\u0030-\\u0039])')
_DEBUG_STT_CLEANING = True

def _read_positive_float_env(name = None, default = None):
    raw_value = os.getenv(name)
# WARNING: Decompyle incomplete


class STTModel:
    '''
    Google Cloud STT 모델 옵션

    - VIDEO: 다중화자/비디오에 최적, 프리미엄 모델 (인식률 최상, 비용 높음)
    - LATEST_LONG: 긴 콘텐츠(미디어/대화)에 최적, 비용 효율적
    - LATEST_SHORT: 짧은 콘텐츠(명령/검색)에 최적
    - DEFAULT: 기본 모델
    '''
    VIDEO = 'video'
    LATEST_LONG = 'latest_long'
    LATEST_SHORT = 'latest_short'
    DEFAULT = 'default'
    VALID_MODELS = {
        VIDEO,
        LATEST_LONG,
        LATEST_SHORT,
        DEFAULT}
    is_valid = (lambda cls = None, model = None: model in cls.VALID_MODELS)()
    get_default = (lambda cls = None: cls.LATEST_LONG)()


class GoogleSTTService:
    '''
    Google Cloud Speech-to-Text 서비스

    단어 단위 타임스탬프를 추출하여 정확한 자막 싱크를 생성합니다.
    '''
    SUPPORTED_LANGUAGES = {
        'ko': 'ko-KR',
        'ko-KR': 'ko-KR',
        'en': 'en-US',
        'en-US': 'en-US',
        'ja': 'ja-JP',
        'ja-JP': 'ja-JP',
        'zh': 'cmn-Hans-CN',
        'zh-CN': 'cmn-Hans-CN' }
    
    def __init__(self = None, api_key = None):
        '''
        Args:
            api_key: Google auth snapshot 값 또는 runtime token (없으면 Settings에서 로드)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_request_headers(self = None):
        return build_google_rest_headers(auth_config = self._auth_config)

    
    def check_api_availability(self = None, language = None):
        '''
        Google STT API 가용성 확인 (TTS 생성 전 사전 검증)

        최소한의 무음 오디오로 API 호출하여 인증/활성화 상태 확인.
        실제 비용은 거의 발생하지 않음 (15초 단위 청구).

        Args:
            language: 언어 코드 (기본값: "ko")

        Returns:
            {
                \'available\': bool,
                \'error_code\': str | None,  # STT_API_DISABLED, STT_API_KEY_INVALID 등
                \'message\': str,
                \'help_url\': str | None
            }
        '''
        import struct
        language_code = self.SUPPORTED_LANGUAGES.get(language, 'ko-KR')
        sample_rate = 16000
        duration_sec = 0.5
        num_samples = int(sample_rate * duration_sec)
        silence_pcm = b'\x00\x00' * num_samples
        wav_header = struct.pack('<4sI4s4sIHHIIHH4sI', b'RIFF', 36 + len(silence_pcm), b'WAVE', b'fmt ', 16, 1, 1, sample_rate, sample_rate * 2, 2, 16, b'data', len(silence_pcm))
        wav_data = wav_header + silence_pcm
        audio_base64 = base64.b64encode(wav_data).decode('utf-8')
        config = {
            'languageCode': language_code,
            'enableWordTimeOffsets': False,
            'encoding': 'LINEAR16',
            'sampleRateHertz': sample_rate,
            'audioChannelCount': 1 }
        request_body = {
            'config': config,
            'audio': {
                'content': audio_base64 } }
        check_timeout_sec = _read_positive_float_env('TFSTUDIO_GOOGLE_STT_CHECK_TIMEOUT_SEC', DEFAULT_STT_API_CHECK_TIMEOUT_SEC)
        
        try:
            log_debug('[STT Check] API 가용성 확인 중...')
            response = requests.post(GOOGLE_STT_API_URL, json = request_body, headers = self._get_request_headers(), timeout = check_timeout_sec)
            if response.status_code == 200:
                log_debug('[STT Check] API 사용 가능')
                return {
                    'available': True,
                    'error_code': None,
                    'message': 'Google STT API 사용 가능',
                    'help_url': None }
            error_data = None.json().get('error', { })
            error_msg = error_data.get('message', response.text)
            log_debug(f'''[STT Check] API 오류: {error_msg}''')
            if 'API key not valid' in error_msg:
                return {
                    'available': False,
                    'error_code': 'STT_API_KEY_INVALID',
                    'message': 'Google API 키가 유효하지 않습니다. Settings에서 확인해주세요.',
                    'help_url': 'https://console.cloud.google.com/apis/credentials' }
            if None in error_msg or 'disabled' in error_msg.lower():
                return {
                    'available': False,
                    'error_code': 'STT_API_DISABLED',
                    'message': 'Cloud Speech-to-Text API가 활성화되지 않았습니다. Google Cloud Console에서 활성화해주세요.',
                    'help_url': 'https://console.cloud.google.com/apis/library/speech.googleapis.com' }
            if None in error_msg.lower():
                return {
                    'available': False,
                    'error_code': 'STT_QUOTA_EXCEEDED',
                    'message': 'Google STT API 할당량이 초과되었습니다.',
                    'help_url': 'https://console.cloud.google.com/apis/api/speech.googleapis.com/quotas' }
            return {
                'available': None,
                'error_code': 'STT_API_ERROR',
                'message': f'''Google STT API 오류: {error_msg}''',
                'help_url': None }
        except requests.exceptions.Timeout:
            log_debug('[STT Check] API 타임아웃')
            return 
            except Exception:
                log_debug(f'''[STT Check] 예외 발생: {e}''')
                del e
                return None
                None = 
                del e


    
    def transcribe_audio(self, audio_path, language, phrase_hints = None, model = None, use_enhanced = None, boost = ('ko', None, None, True, 20, None), progress_callback = ('audio_path', str, 'language', str, 'phrase_hints', Optional[List[str]], 'model', Optional[str], 'use_enhanced', bool, 'boost', float, 'progress_callback', Optional[Callable[([
        int,
        str], None)]], 'return', Dict)):
        '''
        오디오 파일에서 단어 단위 타임스탬프 추출

        Args:
            audio_path: 오디오 파일 경로
            language: 언어 코드 (기본값: "ko")
            phrase_hints: 인식률 향상을 위한 힌트 단어 목록 (화자명, 고유명사 등)
            model: STT 모델 (video, latest_long, latest_short, default)
            use_enhanced: Enhanced 모델 사용 여부 (기본 True)
            boost: Phrase hints 부스트 값 (1.0-20.0, 기본 20.0)
            progress_callback: 진행률 콜백 (progress: int, message: str)

        Returns:
            {
                \'status\': \'success\' | \'error\',
                \'words\': [{\'word\': str, \'start\': float, \'end\': float, \'confidence\': float}],
                \'full_text\': str,
                \'duration\': float,
                \'message\': str
            }
        '''
        
        try:
            log_debug(f'''Transcribing: {audio_path}''')
            if not Path(audio_path).exists():
                return {
                    'status': 'error',
                    'error_code': 'STT_AUDIO_NOT_FOUND',
                    'message': f'''오디오 파일을 찾을 수 없습니다: {audio_path}''',
                    'words': [],
                    'full_text': '' }
            language_code = None.SUPPORTED_LANGUAGES.get(language, language)
            log_debug(f'''Language: {language_code}''')
            duration = self._get_audio_duration(audio_path)
            log_debug(f'''Audio duration: {duration:.2f}s''')
            if progress_callback:
                progress_callback(10, '오디오 분석 중...')
            if duration > MAX_SYNC_DURATION:
                log_debug(f'''오디오가 {MAX_SYNC_DURATION}초 초과, 청크 분할 처리''')
                return self._transcribe_chunked(audio_path, language_code, duration, phrase_hints, model = model, use_enhanced = use_enhanced, boost = boost, progress_callback = progress_callback)
            if None:
                progress_callback(20, '오디오 변환 중...')
            flac_path = self._convert_to_flac(audio_path, add_silence = True)
            
            try:
                if progress_callback:
                    progress_callback(40, 'Google STT 처리 중...')
                result = self._call_stt_api(flac_path, language_code, phrase_hints, model = model, use_enhanced = use_enhanced, boost = boost)
                if result['status'] == 'error':
                    os.unlink(flac_path)
                    return result
                
                try:
                    return None
                    
                    try:
                        
                        try:
                            words = result['words']
                            for word in words:
                                word['start'] = max(0, word['start'] - SILENCE_PADDING)
                                word['end'] = max(0, word['end'] - SILENCE_PADDING)
                                if progress_callback:
                                    progress_callback(80, '처리 완료')
                            os.unlink(flac_path)
                            return {
                                'status': 'success',
                                'words': words,
                                'full_text': result['full_text'],
                                'duration': duration,
                                'message': f'''{len(words)}개 단어 인식 완료''' }
                            
                            try:
                                return None
                                
                                try:
                                    os.unlink(flac_path)
                                    
                                    try:
                                        pass
                                    except Exception:
                                        e = None
                                        logger.exception('Transcription failed')
                                        del e
                                        return None
                                        None = 
                                        del e









    
    def generate_srt(self, audio_path, output_path, language, max_chars_per_segment, max_duration_per_segment, phrase_hints = None, model = None, use_enhanced = None, boost = (None, 'ko', 25, 5, None, None, True, 20, None), progress_callback = ('audio_path', str, 'output_path', str, 'language', str, 'max_chars_per_segment', int, 'max_duration_per_segment', float, 'phrase_hints', Optional[List[str]], 'model', Optional[str], 'use_enhanced', bool, 'boost', float, 'progress_callback', Optional[Callable[([
        int,
        str], None)]], 'return', Dict)):
        """
        오디오에서 SRT 자막 파일 생성

        Args:
            audio_path: 오디오 파일 경로
            output_path: SRT 출력 경로 (없으면 자동 생성)
            language: 언어 코드
            max_chars_per_segment: 세그먼트당 최대 글자 수
            max_duration_per_segment: 세그먼트당 최대 지속 시간 (초)
            phrase_hints: 인식률 향상을 위한 힌트 단어 목록
            model: STT 모델 (video, latest_long, latest_short, default)
            use_enhanced: Enhanced 모델 사용 여부 (기본 True)
            boost: Phrase hints 부스트 값 (1.0-20.0, 기본 20.0)
            progress_callback: 진행률 콜백

        Returns:
            {
                'status': 'success' | 'error',
                'srt_path': str,
                'segments': list,
                'message': str
            }
        """
        pass
    # WARNING: Decompyle incomplete

    
    def _convert_to_flac(self = None, audio_path = None, add_silence = None):
        '''오디오를 16kHz mono FLAC으로 변환'''
        temp_file = tempfile.NamedTemporaryFile(suffix = '.flac', delete = False)
        temp_path = temp_file.name
        temp_file.close()
    # WARNING: Decompyle incomplete

    
    def _get_audio_duration(self = None, audio_path = None):
        '''오디오 파일 길이 확인 (초)'''
        return probe_media_duration(audio_path)

    
    def _call_stt_api(self, flac_path, language_code = None, phrase_hints = None, model = None, use_enhanced = (None, None, True, 20), boost = ('flac_path', str, 'language_code', str, 'phrase_hints', Optional[List[str]], 'model', Optional[str], 'use_enhanced', bool, 'boost', float, 'return', Dict)):
