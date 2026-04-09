# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: runtime_diagnostics_service.pyc (Python 3.11)

'''
Runtime diagnostics and startup validation for EXE-safe deployments.
'''
from __future__ import annotations
import json
import logging
from pathlib import Path
from typing import Any
logger = logging.getLogger(__name__)
_STARTUP_REQUIRED_RESOURCES = {
    'staticPath': 'static resource directory',
    'frontendDistPath': 'frontend dist directory',
    'sceneDataPath': 'scene data directory',
    'assistantDataPath': 'assistant data directory' }

def _path_exists(path = None):
    if path:
        pass
    return bool(path.exists())


def _check_writable(path = None):
    result = {
        'path': str(path),
        'exists': path.exists(),
        'writable': False,
        'error': None }
    
    try:
        path.mkdir(parents = True, exist_ok = True)
        probe_file = path / '.tfstudio_write_probe'
        probe_file.write_text('ok', encoding = 'utf-8')
        probe_file.unlink(missing_ok = True)
        result['exists'] = True
        result['writable'] = True
    except Exception:
        exc = None
        result['error'] = str(exc)
        exc = None
        del exc
    except:
        exc = None
        del exc

    return result


def _resource_payload(path = None):
    return {
        'path': str(path),
        'exists': path.exists(),
        'isFile': path.is_file(),
        'isDir': path.is_dir() }


def _binary_payload(binary_name = None):
    get_bundled_ffmpeg_path = get_bundled_ffmpeg_path
    get_bundled_ffprobe_path = get_bundled_ffprobe_path
    import app.config.paths
    resolve_ffmpeg_binary = resolve_ffmpeg_binary
    resolve_ffprobe_binary = resolve_ffprobe_binary
    import app.utils.ffmpeg_utils
    bundled_path = get_bundled_ffmpeg_path() if binary_name == 'ffmpeg' else get_bundled_ffprobe_path()
    payload = {
        'name': binary_name,
        'bundledPath': str(bundled_path),
        'bundledExists': bundled_path.exists(),
        'resolvedPath': None,
        'source': None,
        'available': False,
        'error': None }
    
    try:
        resolved = resolve_ffmpeg_binary() if binary_name == 'ffmpeg' else resolve_ffprobe_binary()
        payload['resolvedPath'] = resolved.path
        payload['source'] = resolved.source
        payload['available'] = True
    except Exception:
        exc = None
        payload['error'] = str(exc)
        exc = None
        del exc
    except:
        exc = None
        del exc

    return payload


def collect_runtime_diagnostics():
