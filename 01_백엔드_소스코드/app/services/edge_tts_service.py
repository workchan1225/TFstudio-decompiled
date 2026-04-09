# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: edge_tts_service.pyc (Python 3.11)

'''
EdgeTTSService - Microsoft Edge TTS 서비스

Features:
- 한국어 3개 음성 지원 (SunHi, InJoon, Hyunsu)
- rate/volume/pitch 파라미터 (-100% ~ +100%)
- 자막 생성 (WordBoundary 타임스탬프)
- 긴 텍스트 자동 청킹 (1000자 이상)
- SSE 스트리밍 진행도 지원 (라인별 생성)
'''
import asyncio
import logging
import re
from pathlib import Path
from typing import Dict, Any, List, Generator, Optional
import nest_asyncio
from app.utils.atomic_media_write import atomic_audio_output
from app.utils.ffmpeg_utils import get_ffmpeg_executable
nest_asyncio.apply()
logger = logging.getLogger(__name__)
VOICES_BY_LANGUAGE = {
    'ko-KR': [
        {
            'id': 'ko-KR-SunHiNeural',
            'name': 'SunHi',
            'gender': 'female',
            'description': '자연스럽고 따뜻한 톤' },
        {
            'id': 'ko-KR-InJoonNeural',
            'name': 'InJoon',
            'gender': 'male',
            'description': '안정적이고 진중한 톤' },
        {
            'id': 'ko-KR-HyunsuNeural',
            'name': 'Hyunsu',
            'gender': 'male',
            'description': '친절하고 편안한 톤' }],
    'en-US': [
        {
            'id': 'en-US-AvaNeural',
            'name': 'Ava',
            'gender': 'female',
            'description': 'Friendly and warm' },
        {
            'id': 'en-US-AndrewNeural',
            'name': 'Andrew',
            'gender': 'male',
            'description': 'Professional and clear' },
        {
            'id': 'en-US-EmmaNeural',
            'name': 'Emma',
            'gender': 'female',
            'description': 'Bright and cheerful' }],
    'ja-JP': [
        {
            'id': 'ja-JP-NanamiNeural',
            'name': 'Nanami',
            'gender': 'female',
            'description': '自然で温かい' },
        {
            'id': 'ja-JP-KeitaNeural',
            'name': 'Keita',
            'gender': 'male',
            'description': '落ち着いた' },
        {
            'id': 'ja-JP-AoiNeural',
            'name': 'Aoi',
            'gender': 'female',
            'description': '明るく親しみやすい' }] }
KOREAN_VOICES = VOICES_BY_LANGUAGE['ko-KR']

class EdgeTTSService:
    '''Edge TTS 생성 서비스'''
    MAX_CHUNK_CHARS = 1000
    CHUNK_THRESHOLD = 1500
    get_voices = (lambda language = None: VOICES_BY_LANGUAGE.get(language, KOREAN_VOICES))()
    _split_text_into_chunks = (lambda text = None, max_chars = None: sentence_pattern = '(?<=[.!?。！？])\\s*'sentences = re.split(sentence_pattern, text.strip())sentences = sentences()chunks = []current_chunk = ''for sentence in sentences:
if len(current_chunk) + len(sentence) + 1 <= max_chars:
if current_chunk:
current_chunk += ' ' + sentencecontinuecurrent_chunk = sentencecontinueif current_chunk:
chunks.append(current_chunk)if len(sentence) > max_chars:
words = sentence.split()current_chunk = ''for word in words:
if len(current_chunk) + len(word) + 1 <= max_chars:
if current_chunk:
current_chunk += ' ' + wordcontinuecurrent_chunk = wordcontinueif current_chunk:
chunks.append(current_chunk)current_chunk = wordcurrent_chunk = sentenceif current_chunk:
chunks.append(current_chunk)chunks)()
    format_rate = (lambda rate = None: if rate >= 0:
f'''+{rate}%'''f'''{None}%''')()
    format_volume = (lambda volume = None: if volume >= 0:
f'''+{volume}%'''f'''{None}%''')()
    format_pitch = (lambda pitch = None: if pitch >= 0:
f'''+{pitch}Hz'''f'''{None}Hz''')()
    generate_speech_async = (lambda text, voice_id, output_path = None, rate = None, volume = staticmethod, pitch = (0, 0, 0, False), generate_subtitles = ('text', str, 'voice_id', str, 'output_path', str, 'rate', int, 'volume', int, 'pitch', int, 'generate_subtitles', bool, 'return', Dict[(str, Any)]): pass# WARNING: Decompyle incomplete
)()
    generate_speech = (lambda text, voice_id, output_path = None, rate = None, volume = staticmethod, pitch = (0, 0, 0, False), generate_subtitles = ('text', str, 'voice_id', str, 'output_path', str, 'rate', int, 'volume', int, 'pitch', int, 'generate_subtitles', bool, 'return', Dict[(str, Any)]): asyncio.run(EdgeTTSService.generate_speech_async(text, voice_id, output_path, rate, volume, pitch, generate_subtitles)))()
    generate_speech_for_dialogue_async = (lambda text, voice_id = None, output_path = None, rate = staticmethod, volume = (0, 0, 0), pitch = ('text', str, 'voice_id', str, 'output_path', str, 'rate', int, 'volume', int, 'pitch', int, 'return', Dict[(str, Any)]): pass# WARNING: Decompyle incomplete
)()
    generate_speech_for_dialogue = (lambda text, voice_id = None, output_path = None, rate = staticmethod, volume = (0, 0, 0), pitch = ('text', str, 'voice_id', str, 'output_path', str, 'rate', int, 'volume', int, 'pitch', int, 'return', Dict[(str, Any)]): asyncio.run(EdgeTTSService.generate_speech_for_dialogue_async(text, voice_id, output_path, rate, volume, pitch)))()
    _group_words_to_sentences = (lambda word_timings = None, original_text = None: if not word_timings:
[]segments = Nonefor i, timing in enumerate(word_timings):
start_sec = timing['offset'] / 1000duration_sec = timing['duration'] / 1000end_sec = start_sec + duration_secsegments.append({
'index': i,
'start': round(start_sec, 3),
'end': round(end_sec, 3),
'text': timing['text'],
'duration': round(duration_sec, 3) })segments)()
    generate_speech_with_word_timing_async = (lambda text, voice_id = None, output_path = None, rate = staticmethod, volume = (0, 0, 0), pitch = ('text', str, 'voice_id', str, 'output_path', str, 'rate', int, 'volume', int, 'pitch', int, 'return', Dict[(str, Any)]): pass# WARNING: Decompyle incomplete
)()
    generate_speech_with_word_timing = (lambda text, voice_id = None, output_path = None, rate = staticmethod, volume = (0, 0, 0), pitch = ('text', str, 'voice_id', str, 'output_path', str, 'rate', int, 'volume', int, 'pitch', int, 'return', Dict[(str, Any)]): text_len = len(text)if text_len >= EdgeTTSService.CHUNK_THRESHOLD:
logger.info(f'''[EdgeTTS] Long text detected ({text_len} chars), using chunked generation''')EdgeTTSService._generate_speech_chunked(text, voice_id, output_path, rate, volume, pitch)None.run(EdgeTTSService.generate_speech_with_word_timing_async(text, voice_id, output_path, rate, volume, pitch)))()
    _generate_speech_chunked = (lambda text, voice_id = None, output_path = None, rate = staticmethod, volume = (0, 0, 0), pitch = ('text', str, 'voice_id', str, 'output_path', str, 'rate', int, 'volume', int, 'pitch', int, 'return', Dict[(str, Any)]): import osimport subprocessimport sys# WARNING: Decompyle incomplete
)()
    generate_speech_line_by_line_streaming = (lambda text, voice_id, output_path, rate, volume, pitch = None, silence_duration = None, line_output_dir = staticmethod, parallel = (0, 0, 0, 0.3, None, True, 5), max_workers = ('text', str, 'voice_id', str, 'output_path', str, 'rate', int, 'volume', int, 'pitch', int, 'silence_duration', float, 'line_output_dir', Optional[str], 'parallel', bool, 'max_workers', int, 'return', Generator[(Dict, None, None)]): pass# WARNING: Decompyle incomplete
)()
