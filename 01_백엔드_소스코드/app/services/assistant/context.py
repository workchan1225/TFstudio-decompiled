# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: context.pyc (Python 3.11)

'''Route-aware assistant context builders.'''
from __future__ import annotations
import json
import re
from typing import Any
from app.models.project import Project
from app.models.settings import Settings
from app.services.dialogue_line_parser import DialogueLineParser
from app.services.google_auth_service import resolve_google_auth_config
from app.utils.speaker_normalizer import canonicalize_speaker_name
SUPPORTED_ASSISTANT_SCOPES = {
    'tts',
    'audio',
    'global',
    'images',
    'script',
    'unknown',
    'settings',
    'subtitles',
    'thumbnail'}

def resolve_assistant_scope(explicit_scope = None, pathname = None):
