# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: supertonic_tts_service.pyc (Python 3.11)

'''
Supertonic ONNX TTS service.

Provides a stable wrapper for local Supertonic inference with:
- text normalization
- safe chunking
- chunk-level quality checks with retry
- natural pause merge
'''
from __future__ import annotations
import importlib.util as importlib
import logging
import os
import re
import subprocess
import sys
import tempfile
import threading
from pathlib import Path
from types import ModuleType
from typing import Dict, List, Tuple
from unicodedata import normalize
import numpy as np
import soundfile as sf
from app.config.paths import get_supertonic_helper_path, get_supertonic_onnx_path, get_supertonic_voice_styles_path
from app.utils.atomic_media_write import atomic_audio_output
from app.utils.ffmpeg_utils import get_ffmpeg_executable
logger = logging.getLogger(__name__)

class SupertonicTTSService:
    '''Local Supertonic ONNX inference service.'''
    AVAILABLE_LANGS = {
        'en',
        'es',
        'fr',
        'ko',
        'pt'}
    DEFAULT_VOICE = 'F1'
    DEFAULT_SPEED = 1
    DEFAULT_TOTAL_STEP = 10
    DEFAULT_PAUSE_DURATION = 0.22
    DEFAULT_MAX_CHUNK_KO = 110
    DEFAULT_MAX_CHUNK_OTHER = 240
    RECOVERY_SUBCHUNK_PAUSE = 0.06
    RETRY_SPEED_DECAY = 0.04
    MAX_TOTAL_STEP = 24
    _init_lock = threading.Lock()
    _helper_module: 'ModuleType | None' = None
    _tts_runtime = None
    _style_cache: 'Dict[str, object]' = { }
    _onnx_dir: 'Path | None' = None
    _voice_style_dir: 'Path | None' = None
    
    def __init__(self):
        self._ensure_runtime_loaded()

    
    def preprocess_text(self = None, text = None, language = None):
        '''Normalize user text for stable TTS inference.'''
        if not text:
            return ''
        normalized_text = None('NFKC', text)
        normalized_text = normalized_text.replace('\r\n', '\n').replace('\r', '\n')
        normalized_text = normalized_text.replace('\t', ' ')
        normalized_text = normalized_text.replace('—', '-').replace('–', '-')
        normalized_text = re.sub('[\\u2600-\\u27BF\\U0001F300-\\U0001FAFF]', '', normalized_text)
        normalized_text = re.sub('[\\u200B-\\u200D\\uFEFF]', '', normalized_text)
        if language or 'ko'.strip().lower().startswith('ko'):
            normalized_text = self._normalize_numbers_for_korean(normalized_text)
        normalized_text = re.sub('\\s+', ' ', normalized_text).strip()
        if not normalized_text and re.search('[.!?。！？]$', normalized_text):
            normalized_text += '.'
        return normalized_text

    _normalize_numbers_for_korean = (lambda text = None: if not text:
texttry:
normalize_numbers_for_chirp3 = normalize_numbers_for_chirp3import app.utils.number_to_koreannormalize_numbers_for_chirp3(text)except Exception:
exc = Nonelogger.warning('[Supertonic] Korean number normalization skipped: %s', exc)del excNoneNone = del exc)()
    
    def split_text_safe(self = None, text = None, lang = None, max_chunk_chars = ('ko', None)):
        '''Split text safely by sentence boundaries with max length guard.'''
        if not text:
            return []
        limit = None
        if not limit:
            limit = self.DEFAULT_MAX_CHUNK_KO if lang == 'ko' else self.DEFAULT_MAX_CHUNK_OTHER
        if len(text) <= limit:
            return [
                text]
        sentence_parts = None.split('(?<=[.!?。！？,，;；])\\s+', text)
        chunks = []
        current = ''
        for part in sentence_parts:
            sentence = part.strip()
            if not sentence:
                continue
            if len(sentence) > limit:
                words = sentence.split(' ')
                tmp = ''
                for word in words:
                    if len(word) > limit:
                        if tmp:
                            chunks.append(tmp)
                            tmp = ''
                        chunks.extend(self._split_overlong_piece(word, limit))
                        continue
                    add_len = len(word) + 1 if tmp else 0
                    if len(tmp) + add_len <= limit:
                        tmp = f'''{tmp} {word}'''.strip()
                        continue
                    if tmp:
                        chunks.append(tmp)
                    tmp = word
                    if tmp:
                        chunks.append(tmp)
                continue
            add_len = len(sentence) + 1 if current else 0
            if len(current) + add_len <= limit:
                current = f'''{current} {sentence}'''.strip()
                continue
            if current:
                chunks.append(current)
            current = sentence
            if current:
                chunks.append(current)
        return chunks()

    _split_overlong_piece = (lambda piece = None, limit = None: if not piece:
[]if None(piece) <= limit:
[
piece]result = Nonestart = 0length = len(piece)# WARNING: Decompyle incomplete
)()
    
    def generate_speech_with_timing(self, text, output_path, voice_id, language, speed = None, total_step = None, pause_duration = None, max_chunk_chars = (DEFAULT_VOICE, 'ko', DEFAULT_SPEED, DEFAULT_TOTAL_STEP, DEFAULT_PAUSE_DURATION, None, 2), max_retries = ('text', 'str', 'output_path', 'str', 'voice_id', 'str', 'language', 'str', 'speed', 'float', 'total_step', 'int', 'pause_duration', 'float', 'max_chunk_chars', 'int | None', 'max_retries', 'int', 'return', 'Dict')):
        '''Generate speech and return subtitle-like chunk timing segments.'''
        lang = language if language in self.AVAILABLE_LANGS else 'ko'
        processed = self.preprocess_text(text, language = lang)
        if not processed:
            return {
                'status': 'error',
                'message': 'Text is empty' }
    # WARNING: Decompyle incomplete

    
    def _synthesize_chunk_with_recovery(self, chunk, lang, style, speed = None, total_step = None, sample_rate = None, max_retries = ('chunk', 'str', 'lang', 'str', 'speed', 'float', 'total_step', 'int', 'sample_rate', 'int', 'max_retries', 'int', 'return', 'List[Tuple[str, np.ndarray, float]]')):
        
        try:
            (chunk_audio, chunk_duration) = self._synthesize_chunk_with_retry(chunk = chunk, lang = lang, style = style, speed = speed, total_step = total_step, sample_rate = sample_rate, max_retries = max_retries)
            return [
                (chunk, chunk_audio, chunk_duration)]
        except Exception:
            primary_error = None
            fallback_limit = max(35, min(80, int(len(chunk) * 0.6)))
            fallback_chunks = self.split_text_safe(chunk, lang = lang, max_chunk_chars = fallback_limit)
            if len(fallback_chunks) <= 1:
                raise RuntimeError(str(primary_error))
            logger.warning('[Supertonic] Chunk recovery split triggered: len=%s, parts=%s', len(chunk), len(fallback_chunks))
            recovered_segments = []
            recovery_speed = max(0.82, speed * 0.95)
            recovery_steps = min(self.MAX_TOTAL_STEP, total_step + 2)
            for fallback_chunk in fallback_chunks:
                (sub_audio, sub_duration) = self._synthesize_chunk_with_retry(chunk = fallback_chunk, lang = lang, style = style, speed = recovery_speed, total_step = recovery_steps, sample_rate = sample_rate, max_retries = max(max_retries, 2))
                recovered_segments.append((fallback_chunk, sub_audio, sub_duration))
                del primary_error
                return None
                None = 
                del primary_error


    
    def _synthesize_chunk_with_retry(self, chunk, lang, style, speed = None, total_step = None, sample_rate = None, max_retries = ('chunk', 'str', 'lang', 'str', 'speed', 'float', 'total_step', 'int', 'sample_rate', 'int', 'max_retries', 'int', 'return', 'Tuple[np.ndarray, float]')):
        runtime = self.__class__._tts_runtime
    # WARNING: Decompyle incomplete

    _trim_edge_silence = (lambda audio = None, sample_rate = None: if audio.size == 0:
audiothreshold = Nonenon_silent = np.where(np.abs(audio) > threshold)[0]if non_silent.size == 0:
np.zeros(max(1, int(sample_rate * 0.2)), dtype = np.float32)pad = None(sample_rate * 0.01)start = max(0, int(non_silent[0]) - pad)end = min(audio.size, int(non_silent[-1]) + pad)audio[start:end])()
    _is_audio_valid = (lambda audio = None, sample_rate = None, text = staticmethod, lang = ('ko', 1), speed = ('audio', 'np.ndarray', 'sample_rate', 'int', 'text', 'str', 'lang', 'str', 'speed', 'float', 'return', 'bool'): if audio.size < int(sample_rate * 0.12):
Falsepeak = float(np.max(np.abs(audio))) if None.size else 0rms = float(np.sqrt(np.mean(audio ** 2))) if audio.size else 0if peak < 0.0001 or rms < 5e-05:
Falsesilence_threshold = None(0.0002, peak * 0.015)silence_ratio = float(np.mean(np.abs(audio) < silence_threshold))if silence_ratio > 0.975:
Falseduration = None(audio) / sample_ratelongest_silence = SupertonicTTSService._max_silence_run_seconds(audio, sample_rate, silence_threshold)if duration >= 1 and longest_silence > min(1.2, duration * 0.55):
Falsecompact = None.sub('\\s+', '', text)char_count = len(compact)normalized_speed = max(0.8, min(1.2, speed))sec_per_char = 0.045 if lang == 'ko' else 0.03min_duration = max(0.2, char_count * sec_per_char / normalized_speed)if char_count >= 8 and duration < min_duration:
False)()
    _max_silence_run_seconds = (lambda audio = None, sample_rate = None, threshold = staticmethod: if audio.size == 0:
0silent = None.abs(audio) < thresholdif not np.any(silent):
0max_run = Nonecurrent_run = 0for is_silent in silent:
if is_silent:
current_run += 1if current_run > max_run:
max_run = current_runcontinuecurrent_run = 0max_run / sample_rate)()
    
    def _write_output_audio(self = None, audio = None, sample_rate = None, output_path = ('audio', 'np.ndarray', 'sample_rate', 'int', 'output_path', 'str', 'return', 'str')):
        out_path = Path(output_path)
        out_path.parent.mkdir(parents = True, exist_ok = True)
        atomic_output_path = atomic_audio_output(out_path)
        if out_path.suffix.lower() == '.wav':
            sf.write(atomic_output_path, audio, sample_rate)
            None(None, None)
            return 
        tmp.name = None.NamedTemporaryFile(suffix = '.wav', delete = False)
        None(None, None)

    
    def _convert_wav_to_target(self = None, wav_path = None, output_path = None):
        ffmpeg_exe = get_ffmpeg_executable()
        cmd = [
            ffmpeg_exe,
            '-y',
            '-i',
            wav_path]
        suffix = Path(output_path).suffix.lower()
        if suffix == '.mp3':
            cmd.extend([
                '-acodec',
                'libmp3lame',
                '-b:a',
                '192k',
                output_path])
        else:
            cmd.append(output_path)
        run_kwargs = {
            'capture_output': True,
            'text': True,
            'encoding': 'utf-8',
            'errors': 'replace',
            'stdin': subprocess.DEVNULL }
        if sys.platform == 'win32':
            run_kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW
    # WARNING: Decompyle incomplete

    
    def _get_voice_style(self = None, voice_id = None):
        if not voice_id:
            pass
        key = self.DEFAULT_VOICE.strip().upper()
        if key in self.__class__._style_cache:
            return self.__class__._style_cache[key]
        helper = None.__class__._helper_module
        style_dir = self.__class__._voice_style_dir
    # WARNING: Decompyle incomplete

    
    def _ensure_runtime_loaded(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _load_helper_module(self = None):
        path = get_supertonic_helper_path()
        if not path.exists():
            raise RuntimeError(f'''Supertonic helper.py not found: {path}''')
        spec = importlib.util.spec_from_file_location('supertonic_helper_local', str(path))
        if not spec or spec.loader:
            raise RuntimeError(f'''Failed to load Supertonic helper module spec: {path}''')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    
    def _resolve_onnx_dir(self = None):
        path = get_supertonic_onnx_path()
        if (path / 'tts.json').exists() and (path / 'vocoder.onnx').exists():
            return path
        raise None(f'''Supertonic ONNX directory not found or incomplete: {path}''')

    
    def _resolve_voice_style_dir(self = None):
        path = get_supertonic_voice_styles_path()
        if (path / f'''{self.DEFAULT_VOICE}.json''').exists():
            return path
        raise None(f'''Supertonic voice_styles directory not found or incomplete: {path}''')
