# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tts.pyc (Python 3.11)

'''TTS 엔진 상태 CLI 명령.'''
import click
from app.cli import with_app_context
from app.cli.formatters import output, status_line
_ENGINE_KEY_MAP = {
    'chirp3hd': ('google', 'google_api_key'),
    'edge': (None, None),
    'googlecloud': ('google', 'google_api_key'),
    'gemini-native': ('google', 'google_api_key'),
    'elevenlabs': ('elevenlabs', 'elevenlabs_api_key'),
    'supertonic': (None, None) }
tts_group = (lambda : pass)()
tts_engines = (lambda ctx:
