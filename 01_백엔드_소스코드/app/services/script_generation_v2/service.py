# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: service.pyc (Python 3.11)

'''
Unified script generation service for upload-tab V2 flows.
'''
from __future__ import annotations
import json
import logging
import re
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Tuple
from app.api.controllers.ai_utils import get_api_key_from_settings, get_model_from_settings, remove_all_speaker_tags, remove_emotion_annotations, replace_unregistered_speakers, smart_split_into_chapters
from app.services.ai import get_ai_service
from app.services.ai.response_parser import ChapterExtractor, ScriptNormalizer, TextCleaner
from app.services.google_auth_service import get_google_configuration_error_message
from app.services.script_service import normalize_speaker_tags
from app.services.script_generation.modes.reference_mode import ReferenceMode
from app.services.script_generation.types import ScriptConfig
from app.utils.script_prompts import create_script_system_prompt, create_script_user_prompt, get_script_response_schema
from app.utils.shorts_prompts import build_shorts_system_prompt, get_genre_shorts_tip, get_shorts_config
from app.utils.script_text_cleaner import remove_english_annotation_parentheses
from app.services.ai.generators.long_script_generator import create_long_script_generator
from prompting import PromptSection, PromptSpec
from types import ScriptChapterV2, ScriptGenerationMode, ScriptGenerationV2Request, ScriptGenerationV2Response, build_warning
from validation import GenerationValidator
logger = logging.getLogger(__name__)
SCRIPT_UPLOAD_TAB_GENERATION_MODEL = 'gemini-2.5-flash'
StandardProfile = <NODE:12>()

class ScriptGenerationV2Service:
    PROMPT_VERSION = 'script-gen-v2.1'
    
    def __init__(self = None, *, ai_service_factory, api_key_resolver, model_resolver, long_script_generator_factory, reference_mode_factory):
        self.ai_service_factory = ai_service_factory
        self.api_key_resolver = api_key_resolver
        self.model_resolver = model_resolver
        self.long_script_generator_factory = long_script_generator_factory
        self.reference_mode_factory = reference_mode_factory
        self.chapter_extractor = ChapterExtractor()
        self.normalizer = ScriptNormalizer()
        self.text_cleaner = TextCleaner()
        self.validator = GenerationValidator()

    
    def generate(self = None, request = None):
