# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tts_controller.pyc (Python 3.11)

"""
TTS Controller (Clean Architecture Version)

Handles all TTS (Text-to-Speech) operations including:
- Typecast TTS
- Google Cloud TTS
- Gemini TTS
- Web TTS
- Speaker-based TTS (multi-speaker dialogue)

Replaces v1 tts.py.

Registration in app/__init__.py:
    from app.api.controllers import tts_controller_bp
    app.register_blueprint(tts_controller_bp, url_prefix='/api/tts')

Endpoints (21):
- GET /voices - Get available voices (Typecast)
- POST /generate - Generate TTS audio (Typecast)
- GET /jobs/<job_id> - Check TTS job status
- POST /estimate-cost - Estimate TTS cost
- GET /voices/<voice_id> - Get voice details
- POST /estimate-duration - Estimate audio duration
- POST /generate-subtitle - Generate subtitles from script
- POST /generate-web-tts - Generate Web TTS audio
- GET /google-voices - Get Google Cloud TTS voices
- POST /generate-google-cloud-tts - Generate Google Cloud TTS
- POST /preview-google-cloud-tts - Preview Google Cloud TTS
- GET /gemini-voices - Get Gemini TTS voices
- GET /gemini-presets - Get Gemini TTS presets
- POST /generate-gemini-tts - Generate Gemini TTS
- POST /preview-gemini-tts - Preview Gemini TTS
- POST /parse-speakers - Parse speakers from script
- POST /generate-speaker-tts - Generate speaker-based TTS
- POST /merge-speaker-audios - Merge speaker audio files
- POST /save-speaker-tts-data - Save speaker TTS data
- POST /generate-single-dialogue - Generate single dialogue TTS
- POST /concat-speaker-audios - Concatenate speaker audios
- POST /generate-google-tts-with-timepoints - Generate Google TTS with timepoints (NEW)
"""
from flask import Blueprint, request, jsonify, Response, stream_with_context, current_app
from typing import Any, Callable, Dict, List, Optional
from pathlib import Path
import math
import os
import re
import sys
import subprocess
import uuid
import json
import logging
import requests
from datetime import datetime
from sqlalchemy.orm.attributes import flag_modified
from app.utils.file_naming import generate_audio_filename
from app.utils.script_text_cleaner import clean_script_for_subtitle
from app.utils.subtitle_layer_utils import update_or_add_subtitle_layer
from app.utils.audio_silence_utils import detect_leading_silence, detect_trailing_silence
from app.utils.ffmpeg_utils import get_ffmpeg_executable, probe_media_duration
from app.services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
tts_controller_bp = Blueprint('tts', __name__)

def _generate_srt_from_segments(segments = None):
    '''
    subtitle_segments 리스트를 SRT 자막 형식 문자열로 변환

    Args:
        segments: [{"text": "...", "start": 0.0, "end": 5.0, ...}, ...]

    Returns:
        SRT format string
    '''
    
    def _seconds_to_srt_time(seconds = None):
        '''초를 SRT 타임스탬프 형식(HH:MM:SS,mmm)으로 변환'''
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds - int(seconds)) * 1000)
        return f'''{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}'''

    srt_lines = []
    for i, seg in enumerate(segments, start = 1):
        start_time = seg.get('start', 0)
        end_time = seg.get('end', start_time + 1)
        text = seg.get('text', '').strip()
        if not text:
            continue
        srt_lines.append(str(i))
        srt_lines.append(f'''{_seconds_to_srt_time(start_time)} --> {_seconds_to_srt_time(end_time)}''')
        srt_lines.append(text)
        srt_lines.append('')
        return '\n'.join(srt_lines)

TYPECAST_SPLIT_DEFAULT_MAX_CHARS = 25
TYPECAST_SPLIT_DEFAULT_MIN_CHARS = 10
TYPECAST_SPLIT_DEFAULT_PUNCTUATION_MAX_CHARS = 40
TYPECAST_EDGE_SILENCE_THRESHOLD_DB = -38
TYPECAST_EDGE_SILENCE_MIN_DURATION = 0.03
TYPECAST_EDGE_SILENCE_PADDING = 0.015
TYPECAST_EDGE_SILENCE_MIN_SPEECH = 0.08
TYPECAST_SPLIT_COMMA_PATTERN = re.compile('[^,，、]+[,，、]?')
TYPECAST_SENTENCE_END_CHARS = '.?!。？！'
TYPECAST_CJK_SENTENCE_END_CHARS = '。？！'
TYPECAST_SENTENCE_END_PATTERN = re.compile('[.?!。？！]')
TYPECAST_CONNECTIVE_ENDING_PATTERN = re.compile('(?:.(?:으며|지만|는데|인데|은데|으니까|니까|아서|어서|해서|워서|봐서|으면서|면서|거나|든지|도록|으면|으니|하게|되게)|.(?:고|며)|(?:^(?:하면|되면|하니|되니|하게|되게)$))$')
TYPECAST_PARTICLE_ENDING_PATTERN = re.compile('(?:에서|으로|에게|한테|부터|까지|마저|조차|처럼|만큼|로서|로써|에게서|한테서|보다|[은는이가을를에의와과도만])$')

def _is_korean_text(text = None):
    if not text:
        return False
    korean_chars = None.findall('[\\uAC00-\\uD7AF\\u1100-\\u11FF\\u3130-\\u318F]', text)
    total_chars = len(re.sub('\\s+', '', text))
    if total_chars == 0:
        return False
    return None(korean_chars) / total_chars >= 0.5


def _score_typecast_clause_boundary(word = None):
    if not word:
        return 0
    if None.search('[,，、]$', word):
        return 10
    if None.search(word):
        return 7
    if None.search(word):
        return 3


def _find_best_typecast_split_index(words = None, max_chars = None):
    if len(words) <= 1:
        return -1
    min_chars = None.floor(max_chars * 0.6)
    best_index = -1
    best_score = -1
    best_length = 0
    accumulated = ''
    for index, word in enumerate(words):
        test_str = f'''{accumulated} {word}'''.strip() if accumulated else word
        if len(test_str) > max_chars:
            pass
        else:
            accumulated = test_str
            if len(accumulated) < min_chars:
                continue
            score = _score_typecast_clause_boundary(word)
            if (score > best_score or score == best_score) and len(accumulated) > best_length:
                best_index = index
                best_score = score
                best_length = len(accumulated)
    return best_index if best_score > 0 else -1


def _split_typecast_by_characters(text = None, max_chars = None):
    pass
# WARNING: Decompyle incomplete


def _split_typecast_segment_by_words_greedy(words = None, segment = None, max_length = None):
