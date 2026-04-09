# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: character_binding_mode.pyc (Python 3.11)

'''Utilities for scene character binding mode handling.'''
from typing import Final
DEFAULT_CHARACTER_BINDING_MODE: Final[str] = 'auto'
VALID_CHARACTER_BINDING_MODES: Final[set[str]] = {
    'auto',
    'detected_only',
    'local_upload_first'}

def normalize_character_binding_mode(value = None):
