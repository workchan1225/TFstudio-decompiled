# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: atomic_media_write.pyc (Python 3.11)

from __future__ import annotations
import os
from pathlib import Path
import tempfile
from contextlib import contextmanager
from typing import Iterator, Union
AudioPathLike = Union[(str, Path)]
_VALIDATED_AUDIO_SUFFIXES = frozenset({
    '.aac',
    '.m4a',
    '.mp3',
    '.ogg',
    '.wav',
    '.flac',
    '.webm'})

def _validate_audio_output(path = None, validate_duration = None):
    if not path.exists():
        raise FileNotFoundError(f'''Atomic audio output not found: {path}''')
    file_size = path.stat().st_size
    if file_size <= 0:
        raise ValueError(f'''Atomic audio output is empty: {path}''')
    if validate_duration or path.suffix.lower() not in _VALIDATED_AUDIO_SUFFIXES:
        return None
    get_audio_duration = get_audio_duration
    import app.utils.vad_utils
    duration = get_audio_duration(str(path))
    if duration <= 0:
        raise ValueError(f'''Atomic audio output has invalid duration: {path}''')

atomic_audio_output = (lambda final_path = None, *, validate_duration: pass# WARNING: Decompyle incomplete
)()

def create_atomic_audio_temp_path(final_path = None):
