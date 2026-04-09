# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: google_tts_service.pyc (Python 3.11)

'''
Google Cloud TTS 서비스 (Standard + WaveNet + Neural2 + Chirp3-HD 지원)
고품질 한국어/영어 음성 합성 서비스

지원 음성 타입:
- Standard: 기본 음성
- WaveNet: 고품질 딥러닝 음성
- Neural2: 최신 뉴럴 음성 (SSML <mark> 태그로 타임포인트 지원)
- Chirp3-HD: 최고품질 30가지 스타일 음성 (타임포인트 미지원)
- SSE 스트리밍 진행도 지원 (라인별 생성)
'''
import logging
import os
import subprocess
import sys
import tempfile
import shutil
import threading
from pathlib import Path
from typing import Optional, Dict, List, Generator
from app.utils.atomic_media_write import atomic_audio_output
from app.utils.ssml_utils import wrap_english_with_lang_tag
from app.utils.ffmpeg_utils import get_ffmpeg_executable
from app.services.google_auth_service import create_google_tts_client, get_google_configuration_error_message
logger = logging.getLogger(__name__)

try:
    from google.cloud import texttospeech_v1 as texttospeech
    GOOGLE_TTS_AVAILABLE = True
except ImportError:
    GOOGLE_TTS_AVAILABLE = False
    logger.warning('google-cloud-texttospeech 라이브러리가 설치되지 않았습니다.')


class GoogleTTSService:
    '''Google Cloud Text-to-Speech 서비스 클래스 (Standard + WaveNet + Neural2 + Chirp3-HD 지원)'''
    MAX_TEXT_BYTES = 4500
    STANDARD_VOICES = {
        'ko-KR': [
            {
                'name': 'ko-KR-Standard-A',
                'gender': 'female',
                'description': '여성 A - 표준 음성' },
            {
                'name': 'ko-KR-Standard-B',
                'gender': 'female',
                'description': '여성 B - 표준 음성' },
            {
                'name': 'ko-KR-Standard-C',
                'gender': 'male',
                'description': '남성 C - 표준 음성' },
            {
                'name': 'ko-KR-Standard-D',
                'gender': 'male',
                'description': '남성 D - 표준 음성' }],
        'en-US': [
            {
                'name': 'en-US-Standard-A',
                'gender': 'male',
                'description': 'Male A - Standard voice' },
            {
                'name': 'en-US-Standard-B',
                'gender': 'male',
                'description': 'Male B - Standard voice' },
            {
                'name': 'en-US-Standard-C',
                'gender': 'female',
                'description': 'Female C - Standard voice' },
            {
                'name': 'en-US-Standard-D',
                'gender': 'male',
                'description': 'Male D - Standard voice' },
            {
                'name': 'en-US-Standard-E',
                'gender': 'female',
                'description': 'Female E - Standard voice' },
            {
                'name': 'en-US-Standard-F',
                'gender': 'female',
                'description': 'Female F - Standard voice' },
            {
                'name': 'en-US-Standard-G',
                'gender': 'female',
                'description': 'Female G - Standard voice' },
            {
                'name': 'en-US-Standard-H',
                'gender': 'female',
                'description': 'Female H - Standard voice' },
            {
                'name': 'en-US-Standard-I',
                'gender': 'male',
                'description': 'Male I - Standard voice' },
            {
                'name': 'en-US-Standard-J',
                'gender': 'male',
                'description': 'Male J - Standard voice' }],
        'ja-JP': [
            {
                'name': 'ja-JP-Standard-A',
                'gender': 'female',
                'description': '女性 A - 標準音声' },
            {
                'name': 'ja-JP-Standard-B',
                'gender': 'female',
                'description': '女性 B - 標準音声' },
            {
                'name': 'ja-JP-Standard-C',
                'gender': 'male',
                'description': '男性 C - 標準音声' },
            {
                'name': 'ja-JP-Standard-D',
                'gender': 'male',
                'description': '男性 D - 標準音声' }],
        'zh-CN': [
            {
                'name': 'zh-CN-Standard-A',
                'gender': 'female',
                'description': '女性 A - 标准语音' },
            {
                'name': 'zh-CN-Standard-B',
                'gender': 'male',
                'description': '男性 B - 标准语音' },
            {
                'name': 'zh-CN-Standard-C',
                'gender': 'male',
                'description': '男性 C - 标准语音' },
            {
                'name': 'zh-CN-Standard-D',
                'gender': 'female',
                'description': '女性 D - 标准语音' }] }
    NEURAL2_VOICES = {
        'ko-KR': [
            {
                'name': 'ko-KR-Neural2-A',
                'gender': 'female',
                'description': '여성 A - 차분하고 전문적인' },
            {
                'name': 'ko-KR-Neural2-B',
                'gender': 'female',
                'description': '여성 B - 밝고 친근한' },
            {
                'name': 'ko-KR-Neural2-C',
                'gender': 'male',
                'description': '남성 C - 깊고 안정적인' }],
        'en-US': [
            {
                'name': 'en-US-Neural2-A',
                'gender': 'male',
                'description': 'Male A - Deep and professional' },
            {
                'name': 'en-US-Neural2-C',
                'gender': 'female',
                'description': 'Female C - Warm and friendly' },
            {
                'name': 'en-US-Neural2-D',
                'gender': 'male',
                'description': 'Male D - Clear and energetic' },
            {
                'name': 'en-US-Neural2-E',
                'gender': 'female',
                'description': 'Female E - Calm and authoritative' },
            {
                'name': 'en-US-Neural2-F',
                'gender': 'female',
                'description': 'Female F - Bright and cheerful' },
            {
                'name': 'en-US-Neural2-G',
                'gender': 'female',
                'description': 'Female G - Soft and soothing' },
            {
                'name': 'en-US-Neural2-H',
                'gender': 'female',
                'description': 'Female H - Professional narrator' },
            {
                'name': 'en-US-Neural2-I',
                'gender': 'male',
                'description': 'Male I - Casual and friendly' },
            {
                'name': 'en-US-Neural2-J',
                'gender': 'male',
                'description': 'Male J - Mature and wise' }],
        'ja-JP': [
            {
                'name': 'ja-JP-Neural2-B',
                'gender': 'female',
                'description': '女性 B - 明るく親しみやすい' },
            {
                'name': 'ja-JP-Neural2-C',
                'gender': 'male',
                'description': '男性 C - 落ち着いた' },
            {
                'name': 'ja-JP-Neural2-D',
                'gender': 'male',
                'description': '男性 D - 若々しい' }],
        'zh-CN': [
            {
                'name': 'zh-CN-Neural2-A',
                'gender': 'female',
                'description': '女性 A - 自然流畅' },
            {
                'name': 'zh-CN-Neural2-B',
                'gender': 'male',
                'description': '男性 B - 沉稳专业' },
            {
                'name': 'zh-CN-Neural2-C',
                'gender': 'male',
                'description': '男性 C - 清晰有力' },
            {
                'name': 'zh-CN-Neural2-D',
                'gender': 'female',
                'description': '女性 D - 温暖亲切' }] }
    WAVENET_VOICES = {
        'ko-KR': [
            {
                'name': 'ko-KR-Wavenet-A',
                'gender': 'female',
                'description': '여성 A - 자연스러운 음색' },
            {
                'name': 'ko-KR-Wavenet-B',
                'gender': 'female',
                'description': '여성 B - 부드러운 톤' },
            {
                'name': 'ko-KR-Wavenet-C',
                'gender': 'male',
                'description': '남성 C - 중후한 목소리' },
            {
                'name': 'ko-KR-Wavenet-D',
                'gender': 'male',
                'description': '남성 D - 명확한 발음' }],
        'en-US': [
            {
                'name': 'en-US-Wavenet-A',
                'gender': 'male',
                'description': 'Male A - Natural baritone' },
            {
                'name': 'en-US-Wavenet-B',
                'gender': 'male',
                'description': 'Male B - Warm and steady' },
            {
                'name': 'en-US-Wavenet-C',
                'gender': 'female',
                'description': 'Female C - Clear and bright' },
            {
                'name': 'en-US-Wavenet-D',
                'gender': 'male',
                'description': 'Male D - Confident tone' },
            {
                'name': 'en-US-Wavenet-E',
                'gender': 'female',
                'description': 'Female E - Soft and gentle' },
            {
                'name': 'en-US-Wavenet-F',
                'gender': 'female',
                'description': 'Female F - Expressive' },
            {
                'name': 'en-US-Wavenet-G',
                'gender': 'female',
                'description': 'Female G - Youthful energy' },
            {
                'name': 'en-US-Wavenet-H',
                'gender': 'female',
                'description': 'Female H - Professional' },
            {
                'name': 'en-US-Wavenet-I',
                'gender': 'male',
                'description': 'Male I - Casual friendly' },
            {
                'name': 'en-US-Wavenet-J',
                'gender': 'male',
                'description': 'Male J - Deep and calm' }],
        'ja-JP': [
            {
                'name': 'ja-JP-Wavenet-A',
                'gender': 'female',
                'description': '女性 A - 落ち着いた声' },
            {
                'name': 'ja-JP-Wavenet-B',
                'gender': 'female',
                'description': '女性 B - 明るい声' },
            {
                'name': 'ja-JP-Wavenet-C',
                'gender': 'male',
                'description': '男性 C - 穏やかな声' },
            {
                'name': 'ja-JP-Wavenet-D',
                'gender': 'male',
                'description': '男性 D - はっきりした声' }],
        'zh-CN': [
            {
                'name': 'zh-CN-Wavenet-A',
                'gender': 'female',
                'description': '女性 A - 温柔清晰' },
            {
                'name': 'zh-CN-Wavenet-B',
                'gender': 'male',
                'description': '男性 B - 稳重大气' },
            {
                'name': 'zh-CN-Wavenet-C',
                'gender': 'male',
                'description': '男性 C - 年轻活力' },
            {
                'name': 'zh-CN-Wavenet-D',
                'gender': 'female',
                'description': '女性 D - 亲切自然' }] }
    CHIRP3_HD_VOICES = {
        'ko-KR': [
            {
                'name': 'ko-KR-Chirp3-HD-Aoede',
                'gender': 'female',
                'description': '따뜻하고 부드러운' },
            {
                'name': 'ko-KR-Chirp3-HD-Kore',
                'gender': 'female',
                'description': '밝고 명확한' },
            {
                'name': 'ko-KR-Chirp3-HD-Leda',
                'gender': 'female',
                'description': '우아하고 세련된' },
            {
                'name': 'ko-KR-Chirp3-HD-Zephyr',
                'gender': 'female',
                'description': '경쾌하고 활기찬' },
            {
                'name': 'ko-KR-Chirp3-HD-Achernar',
                'gender': 'female',
                'description': '청아하고 맑은' },
            {
                'name': 'ko-KR-Chirp3-HD-Autonoe',
                'gender': 'female',
                'description': '차분하고 신뢰감' },
            {
                'name': 'ko-KR-Chirp3-HD-Callirrhoe',
                'gender': 'female',
                'description': '유려하고 감성적' },
            {
                'name': 'ko-KR-Chirp3-HD-Despina',
                'gender': 'female',
                'description': '밝고 친근한' },
            {
                'name': 'ko-KR-Chirp3-HD-Erinome',
                'gender': 'female',
                'description': '깊고 풍부한' },
            {
                'name': 'ko-KR-Chirp3-HD-Gacrux',
                'gender': 'female',
                'description': '또렷하고 명료한' },
            {
                'name': 'ko-KR-Chirp3-HD-Laomedeia',
                'gender': 'female',
                'description': '고급스럽고 우아한' },
            {
                'name': 'ko-KR-Chirp3-HD-Pulcherrima',
                'gender': 'female',
                'description': '아름답고 섬세한' },
            {
                'name': 'ko-KR-Chirp3-HD-Sulafat',
                'gender': 'female',
                'description': '부드럽고 온화한' },
            {
                'name': 'ko-KR-Chirp3-HD-Vindemiatrix',
                'gender': 'female',
                'description': '성숙하고 안정적' },
            {
                'name': 'ko-KR-Chirp3-HD-Charon',
                'gender': 'male',
                'description': '깊고 안정적인' },
            {
                'name': 'ko-KR-Chirp3-HD-Puck',
                'gender': 'male',
                'description': '친근하고 활기찬' },
            {
                'name': 'ko-KR-Chirp3-HD-Fenrir',
                'gender': 'male',
                'description': '힘있고 강렬한' },
            {
                'name': 'ko-KR-Chirp3-HD-Orus',
                'gender': 'male',
                'description': '신뢰감있고 차분한' },
            {
                'name': 'ko-KR-Chirp3-HD-Schedar',
                'gender': 'male',
                'description': '세련되고 따뜻한' },
            {
                'name': 'ko-KR-Chirp3-HD-Achird',
                'gender': 'male',
                'description': '명료하고 또렷한' },
            {
                'name': 'ko-KR-Chirp3-HD-Algenib',
                'gender': 'male',
                'description': '부드럽고 친절한' },
            {
                'name': 'ko-KR-Chirp3-HD-Algieba',
                'gender': 'male',
                'description': '중후하고 진중한' },
            {
                'name': 'ko-KR-Chirp3-HD-Alnilam',
                'gender': 'male',
                'description': '밝고 에너지있는' },
            {
                'name': 'ko-KR-Chirp3-HD-Enceladus',
                'gender': 'male',
                'description': '차분하고 지적인' },
            {
                'name': 'ko-KR-Chirp3-HD-Iapetus',
                'gender': 'male',
                'description': '깊고 무게감있는' },
            {
                'name': 'ko-KR-Chirp3-HD-Rasalgethi',
                'gender': 'male',
                'description': '따뜻하고 포근한' },
            {
                'name': 'ko-KR-Chirp3-HD-Sadachbia',
                'gender': 'male',
                'description': '밝고 긍정적인' },
            {
                'name': 'ko-KR-Chirp3-HD-Sadaltager',
                'gender': 'male',
                'description': '신뢰감있는 전문가' },
            {
                'name': 'ko-KR-Chirp3-HD-Umbriel',
                'gender': 'male',
                'description': '부드럽고 차분한' },
            {
                'name': 'ko-KR-Chirp3-HD-Zubenelgenubi',
                'gender': 'male',
                'description': '독특하고 개성있는' }],
        'en-US': [
            {
                'name': 'en-US-Chirp3-HD-Aoede',
                'gender': 'female',
                'description': 'Warm and soft' },
            {
                'name': 'en-US-Chirp3-HD-Kore',
                'gender': 'female',
                'description': 'Bright and clear' },
            {
                'name': 'en-US-Chirp3-HD-Leda',
                'gender': 'female',
                'description': 'Elegant and refined' },
            {
                'name': 'en-US-Chirp3-HD-Zephyr',
                'gender': 'female',
                'description': 'Lively and energetic' },
            {
                'name': 'en-US-Chirp3-HD-Achernar',
                'gender': 'female',
                'description': 'Clear and pure' },
            {
                'name': 'en-US-Chirp3-HD-Autonoe',
                'gender': 'female',
                'description': 'Calm and trustworthy' },
            {
                'name': 'en-US-Chirp3-HD-Callirrhoe',
                'gender': 'female',
                'description': 'Flowing and emotional' },
            {
                'name': 'en-US-Chirp3-HD-Despina',
                'gender': 'female',
                'description': 'Bright and friendly' },
            {
                'name': 'en-US-Chirp3-HD-Erinome',
                'gender': 'female',
                'description': 'Deep and rich' },
            {
                'name': 'en-US-Chirp3-HD-Gacrux',
                'gender': 'female',
                'description': 'Distinct and articulate' },
            {
                'name': 'en-US-Chirp3-HD-Laomedeia',
                'gender': 'female',
                'description': 'Luxurious and elegant' },
            {
                'name': 'en-US-Chirp3-HD-Pulcherrima',
                'gender': 'female',
                'description': 'Beautiful and delicate' },
            {
                'name': 'en-US-Chirp3-HD-Sulafat',
                'gender': 'female',
                'description': 'Soft and gentle' },
            {
                'name': 'en-US-Chirp3-HD-Vindemiatrix',
                'gender': 'female',
                'description': 'Mature and stable' },
            {
                'name': 'en-US-Chirp3-HD-Charon',
                'gender': 'male',
                'description': 'Deep and stable' },
            {
                'name': 'en-US-Chirp3-HD-Puck',
                'gender': 'male',
                'description': 'Friendly and lively' },
            {
                'name': 'en-US-Chirp3-HD-Fenrir',
                'gender': 'male',
                'description': 'Powerful and intense' },
            {
                'name': 'en-US-Chirp3-HD-Orus',
                'gender': 'male',
                'description': 'Trustworthy and calm' },
            {
                'name': 'en-US-Chirp3-HD-Schedar',
                'gender': 'male',
                'description': 'Refined and warm' },
            {
                'name': 'en-US-Chirp3-HD-Achird',
                'gender': 'male',
                'description': 'Clear and distinct' },
            {
                'name': 'en-US-Chirp3-HD-Algenib',
                'gender': 'male',
                'description': 'Soft and kind' },
            {
                'name': 'en-US-Chirp3-HD-Algieba',
                'gender': 'male',
                'description': 'Rich and dignified' },
            {
                'name': 'en-US-Chirp3-HD-Alnilam',
                'gender': 'male',
                'description': 'Bright and energetic' },
            {
                'name': 'en-US-Chirp3-HD-Enceladus',
                'gender': 'male',
                'description': 'Calm and intellectual' },
            {
                'name': 'en-US-Chirp3-HD-Iapetus',
                'gender': 'male',
                'description': 'Deep and weighty' },
            {
                'name': 'en-US-Chirp3-HD-Rasalgethi',
                'gender': 'male',
                'description': 'Warm and cozy' },
            {
                'name': 'en-US-Chirp3-HD-Sadachbia',
                'gender': 'male',
                'description': 'Bright and positive' },
            {
                'name': 'en-US-Chirp3-HD-Sadaltager',
                'gender': 'male',
                'description': 'Professional expert' },
            {
                'name': 'en-US-Chirp3-HD-Umbriel',
                'gender': 'male',
                'description': 'Soft and calm' },
            {
                'name': 'en-US-Chirp3-HD-Zubenelgenubi',
                'gender': 'male',
                'description': 'Unique and distinctive' }] }
    
    def __init__(self = None, api_key = None):
        '''
        Args:
            api_key: Google Cloud API 키 또는 runtime token
        '''
        if not GOOGLE_TTS_AVAILABLE:
            raise ImportError('google-cloud-texttospeech 라이브러리가 필요합니다. pip install google-cloud-texttospeech')
        self.api_key = api_key
        self._client = None
        self._client_lock = threading.Lock()

    _decode_subprocess_output = (lambda value = None: if isinstance(value, bytes):
value.decode('utf-8', errors = 'ignore')if None(value, str):
value# WARNING: Decompyle incomplete
)()
    _build_stream_error_event = (lambda message = None, error_code = None, hint = staticmethod: event = {
'type': 'error',
'message': message,
'error_code': error_code }if hint:
event['hint'] = hintevent)()
    
    def _build_stream_error_from_message(self = None, message = None, line_index = None):
        '''오류 메시지를 사용자 표시용 SSE 에러 이벤트로 정규화.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _build_stream_error_from_exception(self = None, error = None):
