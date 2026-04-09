# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: google_auth_service.pyc (Python 3.11)

'''
Google AI authentication runtime helpers.

This module is the single source of truth for runtime Google auth mode
resolution, validation, and credential loading.
'''
from __future__ import annotations
from dataclasses import dataclass, field
import logging
from pathlib import Path
from typing import Any, Optional
logger = logging.getLogger(__name__)
GOOGLE_AUTH_MODE_API_KEY = 'api_key'
GOOGLE_AUTH_MODE_VERTEX_AI = 'vertex_ai'
GOOGLE_RUNTIME_AUTH_TOKEN = '__TFSTUDIO_GOOGLE_RUNTIME_AUTH__'
DEFAULT_VERTEX_AI_LOCATION = 'us-central1'
GoogleCredentialInfo = <NODE:12>()
GoogleAuthValidation = <NODE:12>()
GoogleAuthConfig = <NODE:12>()

class GoogleAuthValue(str):
    pass
# WARNING: Decompyle incomplete


def _normalize_auth_mode(value = dataclass(frozen = True)):
