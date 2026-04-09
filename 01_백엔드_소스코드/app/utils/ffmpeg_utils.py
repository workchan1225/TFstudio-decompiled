# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ffmpeg_utils.pyc (Python 3.11)

'''
FFmpeg/FFprobe runtime utilities.

Provides EXE-safe binary resolution, shared subprocess kwargs, and
common ffprobe-based media probing helpers.
'''
from __future__ import annotations
import logging
import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional
logger = logging.getLogger(__name__)

class FFmpegBinaryError(FileNotFoundError):
    '''Raised when the runtime FFmpeg executable cannot be resolved.'''
    pass


class FFprobeBinaryError(FileNotFoundError):
    '''Raised when the runtime FFprobe executable cannot be resolved.'''
    pass

ResolvedBinary = <NODE:12>()
_cached_ffmpeg: 'Optional[ResolvedBinary]' = None
_cached_ffprobe: 'Optional[ResolvedBinary]' = None

def _resolve_binary(binary_name = None):
    
    try:
        get_bundled_ffmpeg_path = get_bundled_ffmpeg_path
        get_bundled_ffprobe_path = get_bundled_ffprobe_path
        resolve_runtime_binary_path = resolve_runtime_binary_path
        import app.config.paths
        if binary_name == 'ffmpeg':
            bundled_path = get_bundled_ffmpeg_path()
        else:
            bundled_path = get_bundled_ffprobe_path()
        (resolved_path, source) = resolve_runtime_binary_path(binary_name, bundled_path)
        return ResolvedBinary(name = binary_name, path = str(resolved_path), source = source)
    except FileNotFoundError:
        exc = None
        if binary_name == 'ffmpeg':
            raise FFmpegBinaryError(str(exc)), exc
        raise FFprobeBinaryError(str(exc)), exc
        exc = None
        del exc
        except ImportError:
            exc = None
            message = f'''{binary_name} resolution failed because app.config.paths is unavailable'''
            if binary_name == 'ffmpeg':
                raise FFmpegBinaryError(message), exc
            raise FFprobeBinaryError(message), exc
            exc = None
            del exc



def resolve_ffmpeg_binary():
    '''Resolve the runtime FFmpeg binary.'''
    pass
# WARNING: Decompyle incomplete


def resolve_ffprobe_binary():
    '''Resolve the runtime FFprobe binary.'''
    pass
# WARNING: Decompyle incomplete


def get_ffmpeg_executable():
    '''Return the resolved FFmpeg executable path.'''
    return resolve_ffmpeg_binary().path


def get_ffprobe_executable():
    '''Return the resolved FFprobe executable path.'''
    return resolve_ffprobe_binary().path


def get_subprocess_kwargs(*, timeout, capture_output, text, check, stdin, encoding, errors):
    '''Shared subprocess kwargs for Windows GUI-safe FFmpeg execution.'''
    kwargs = {
        'capture_output': capture_output,
        'text': text,
        'check': check,
        'stdin': stdin,
        'encoding': encoding,
        'errors': errors }
# WARNING: Decompyle incomplete


def probe_media_duration(media_path = None, *, timeout):
    '''Return media duration in seconds using ffprobe.'''
    pass
# WARNING: Decompyle incomplete


def probe_video_dimensions(video_path = None, *, timeout):
    '''Return video width and height using ffprobe.'''
    pass
# WARNING: Decompyle incomplete


def probe_video_has_audio(video_path = None, *, timeout):
    '''Return whether a video file has at least one audio stream.'''
    pass
# WARNING: Decompyle incomplete


def clear_cache():
    '''Reset cached binary resolution results.'''
    global _cached_ffmpeg, _cached_ffprobe
    _cached_ffmpeg = None
    _cached_ffprobe = None
