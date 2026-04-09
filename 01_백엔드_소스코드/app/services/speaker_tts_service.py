# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: speaker_tts_service.pyc (Python 3.11)

'''
Speaker-based TTS Service (화자별 TTS 분리 생성 서비스)

대본에서 화자별 대사를 추출하고, 각 화자에 다른 음성을 할당하여
TTS를 생성한 후, 원본 순서대로 병합하는 서비스.
'''
import os
import re
import sys
import logging
import tempfile
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor, as_completed
from app.utils.atomic_media_write import atomic_audio_output
from app.utils.script_text_cleaner import remove_parenthetical_directions
from app.utils.audio_silence_utils import detect_all_silence_regions
from app.utils.sequence_alignment import validate_and_fix_segment_overlaps, enforce_minimum_segment_duration
from app.utils.ffmpeg_utils import get_ffmpeg_executable, get_ffprobe_executable
from app.services.dialogue_line_parser import DialogueLineParser
logger = logging.getLogger(__name__)
DEFAULT_MERGED_SUBTITLE_MIN_DURATION = 0.7
EXACT_TIMING_SUBTITLE_MIN_DURATION = 0.05
EXACT_TIMING_SUBTITLE_MIN_GAP = 0.001
DialogueLine = <NODE:12>()
SpeakerDialogue = <NODE:12>()

class SpeakerTTSService:
    '''화자별 TTS 분리 생성 서비스'''
    PARALLEL_SETTINGS = {
        'edge-tts': {
            'max_workers': 8,
            'delay': 0 },
        'google-tts': {
            'max_workers': 12,
            'delay': 0.1 },
        'google-tts-chirp3': {
            'max_workers': 3,
            'delay': 0.3 },
        'gemini-tts': {
            'max_workers': 3,
            'delay': 0.3 },
        'gemini-native-tts': {
            'max_workers': 1,
            'delay': 0 },
        'typecast': {
            'max_workers': 4,
            'delay': 0.5 },
        'elevenlabs': {
            'max_workers': 4,
            'delay': 0.3 },
        'qwen3': {
            'max_workers': 1,
            'delay': 0 },
        'supertonic-tts': {
            'max_workers': 1,
            'delay': 0 },
        'web-tts': {
            'max_workers': 1,
            'delay': 0 } }
    DEFAULT_PARALLEL = {
        'max_workers': 3,
        'delay': 0.5 }
    _get_ffmpeg_exe = (lambda : get_ffmpeg_executable())()
    _get_ffprobe_exe = (lambda : get_ffprobe_executable())()
    JSON_KEYWORDS = {
        'data',
        'http',
        'json',
        'name',
        'type',
        'error',
        'https',
        'title',
        'value',
        'format',
        'script',
        'status',
        'content',
        'chapters',
        'provider',
        'description'}
    CHAPTER_MARKER_PATTERNS = [
        re.compile('^챕터\\s*\\d+$', re.IGNORECASE),
        re.compile('^chapter\\s*\\d+$', re.IGNORECASE),
        re.compile('^\\d+장$', re.IGNORECASE),
        re.compile('^장\\s*\\d+$', re.IGNORECASE),
        re.compile('^part\\s*\\d+$', re.IGNORECASE),
        re.compile('^파트\\s*\\d+$', re.IGNORECASE),
        re.compile('^챕터$', re.IGNORECASE),
        re.compile('^chapter$', re.IGNORECASE),
        re.compile('^파트$', re.IGNORECASE),
        re.compile('^part$', re.IGNORECASE)]
    MALFORMED_SPEAKER_TAG_PATTERN = re.compile('\\[([^\\]\\r\\n:]{1,24})\\s*:\\s*')
    is_chapter_marker = (lambda speaker = None: s = speaker.strip()for pattern in SpeakerTTSService.CHAPTER_MARKER_PATTERNS:
if pattern.match(s):
TrueFalse)()
    _looks_like_recoverable_speaker_label = (lambda label = None:
