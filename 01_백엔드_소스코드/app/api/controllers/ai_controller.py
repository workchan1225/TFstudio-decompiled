# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ai_controller.pyc (Python 3.11)

"""
AI Controller (Clean Architecture Version)

Handles all AI-related operations: topic generation, outline, script, images, etc.
Replaces v1 ai.py.

Registration in app/__init__.py:
    from app.api.controllers import ai_controller_bp
    app.register_blueprint(ai_controller_bp, url_prefix='/api/ai')

Endpoints (26):
- POST /generate-topic - Generate video topic ideas
- POST /generate-outline - Generate script outline
- POST /generate-script - Generate full script
- POST /generate-character - Generate character image
- POST /generate-images-batch - Generate multiple images
- POST /generate-video - Generate video from script and images
- POST /generate-image-prompt - Generate image prompt from narration
- POST /analyze-script-structure - Analyze script structure
- POST /generate-youtube-metadata - Generate YouTube metadata
- POST /generate-thumbnail - Generate YouTube thumbnail
- POST /generate-thumbnail-advanced - Generate advanced thumbnail with composition
- POST /generate-thumbnail-batch - Batch thumbnail generation for A/B testing
- POST /generate-titles - Generate video titles
- POST /generate-synopses - Generate synopses
- POST /generate-characters-from-synopsis - Generate characters from synopsis
- POST /expand-script - Expand script with more detail
- POST /analyze-characters-from-script - Analyze characters from script
- POST /generate-scene-prompts - Generate scene prompts
- POST /analyze-and-generate-scenes - Integrated scene analysis
- POST /generate-character-reference - Generate character reference image
- POST /generate-scene-images-batch - Generate scene images batch
- POST /generate-scene-image-single - Generate single scene image
- POST /translate-prompt - Translate prompt (KO -> EN)
- POST /calculate-thumbnail-similarity - Calculate similarity between two thumbnails
- POST /detect-duplicate-references - Detect duplicate images in batch
- POST /generate-auxiliary-text - Generate auxiliary/floating text for thumbnails
"""
from flask import Blueprint, request, jsonify
import logging
from datetime import datetime
import uuid
import json
from app.services.ai import get_ai_service
from app.services.title_generation import generate_upload_title_result
from app.services.script_file_service import ScriptFileService
from app.services.script_service import normalize_speaker_tags
from app.services.prompt.constraints.ratio_enforcer import RatioEnforcer
from app.utils.script_text_cleaner import remove_english_annotation_parentheses
from app.utils.script_prompts import create_script_system_prompt, create_script_user_prompt, get_script_response_schema
from app.services.ai.generators.content_generator import INFORMATIONAL_GENRES
from app.utils.shorts_prompts import build_shorts_system_prompt, get_shorts_config, get_genre_shorts_tip, DIALOGUE_START_GENRES
from app.utils.narration_style_guide import TONE_REQUIRED_ENDINGS, TONE_FORBIDDEN_ENDINGS
from app.api.controllers.ai_utils import ensure_chapter_markers, extract_speakers_from_script, ensure_speaker_tags, get_api_key_from_settings, get_model_from_settings, get_recommended_chapter_count, remove_emotion_annotations, remove_all_speaker_tags, replace_unregistered_speakers, extract_title_from_content, smart_split_into_chapters, parse_legacy_script_format, remove_nested_json_array
from app.utils.character_binding_mode import normalize_character_binding_mode
from app.services.scene.genre_context_resolver import resolve_genre_context
from app.services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
import os
import re
import sys
from app.utils.google_sdk import get_legacy_genai, configure_legacy_genai, get_genai_client, get_genai_types, is_new_sdk_available, is_legacy_sdk_available, GOOGLE_SDK_ERROR_MESSAGE, NEW_SDK_ERROR_MESSAGE, LEGACY_SDK_ERROR_MESSAGE
logger = logging.getLogger(__name__)
ai_controller_bp = Blueprint('ai', __name__)
SCRIPT_UPLOAD_TAB_MODEL = 'gemini-2.5-flash'
YOUTUBE_UPLOAD_TAB_THUMBNAIL_EDIT_MODEL = 'gemini-2.5-flash-image'

def _get_google_runtime_api_key(settings = None):
    Settings = Settings
    import app.models.settings
    if not settings:
        pass
    loaded_settings = Settings.get_or_create()
    return get_google_api_key_or_runtime_token(settings = loaded_settings)


def _get_google_runtime_error(settings = None):
    Settings = Settings
    import app.models.settings
    if not settings:
        pass
    loaded_settings = Settings.get_or_create()
    return get_google_configuration_error_message(settings = loaded_settings)


def _create_google_provider(settings = (None,)):
    Settings = Settings
    import app.models.settings
    GoogleProvider = GoogleProvider
    import app.services.ai.google_provider
    if not settings:
        pass
    loaded_settings = Settings.get_or_create()
    api_key = _get_google_runtime_api_key(loaded_settings)
    if not api_key:
        raise ValueError(_get_google_runtime_error(loaded_settings))
    return GoogleProvider(api_key = api_key)


def _safe_stderr_write(message = None):
    '''Write diagnostics without assuming stderr is always writable.'''
    
    try:
        stream = getattr(sys, 'stderr', None)
        if stream and hasattr(stream, 'write'):
            stream.write(message)
            if hasattr(stream, 'flush'):
                stream.flush()
            return None
    except Exception:
        pass

    logger.error(message.rstrip())


def _safe_stderr_print(*, flush, *args):
    '''Print to stderr when available, otherwise fallback to logger.'''
    message = (lambda .0: pass# WARNING: Decompyle incomplete
)(args())
    
    try:
        stream = getattr(sys, 'stderr', None)
        if stream and hasattr(stream, 'write'):
            stream.write(message + '\n')
            if flush and hasattr(stream, 'flush'):
                stream.flush()
            return None
    except Exception:
        pass

    
    try:
        logger.error(message)
        return None
    except Exception:
        return None



def _is_non_empty_value(value = None):
    pass
# WARNING: Decompyle incomplete


def _prefer_non_empty_value(primary, fallback):
    return primary if _is_non_empty_value(primary) else fallback


def _normalize_gender(value = None, fallback = None):
