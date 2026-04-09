# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: thumbnail_wizard_controller.pyc (Python 3.11)

'''
Thumbnail Wizard Controller
AI 썸네일 마법사 API - 자동/수동 생성 모드 지원

Endpoints:
- POST /api/thumbnail-wizard/recommend-titles       - 대본 분석 → 제목 10개 + 플로팅 텍스트 추천
- POST /api/thumbnail-wizard/generate-auto          - 원클릭 자동 생성 (3장)
- POST /api/thumbnail-wizard/generate-stream        - SSE 스트리밍 자동 생성 (제목별 진행률)
- GET  /api/thumbnail-wizard/youtube-thumbnail      - YouTube URL에서 썸네일 추출
- GET  /api/thumbnail-wizard/reference-templates    - 번들된 레퍼런스 썸네일 목록
- POST /api/thumbnail-wizard/recommend-scenarios    - 대본 기반 시나리오 추천
- POST /api/thumbnail-wizard/generate-from-scenario - 레퍼런스+시나리오 기반 생성
- GET  /api/thumbnail-wizard/history/<project_id>    - 프로젝트별 생성 기록 조회
- POST /api/thumbnail-wizard/history/<project_id>    - 생성 기록 저장 (이미지 파일 포함)
- DELETE /api/thumbnail-wizard/history/<project_id>/<item_id> - 기록 삭제
'''
from flask import Blueprint, request, jsonify, Response, stream_with_context
import base64
import logging
import json
import os
from pathlib import Path
import re
import time
from typing import Optional, List, Dict, Any, Generator
from app.utils.title_pattern_profile import build_title_style_instruction, get_aggressive_ratio, get_title_style_metadata, normalize_title_style_profile
from app.services.thumbnail.wizard_context_builder import analyze_reference_blueprint_payload, build_thumbnail_generation_policy, resolve_thumbnail_wizard_style_context
from app.services.title_generation import generate_upload_title_result
from app.utils.thumbnail_guard import THUMBNAIL_HOOK_TEXT_MAX_LENGTH, build_reference_exclusion_clause, build_reference_metadata_guard_payload, build_situation_blueprint, sanitize_thumbnail_hook_text, validate_thumbnail_generation
from app.utils.thumbnail_prompt_rules import build_character_focus_prompt_rules
from app.services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
from app.utils.google_sdk import configure_legacy_genai
logger = logging.getLogger(__name__)
thumbnail_wizard_bp = Blueprint('thumbnail_wizard', __name__)
TITLE_RECOMMENDATION_SCRIPT_CHAR_LIMIT = 4200
TITLE_RECOMMENDATION_MAX_RETRY = 1
YOUTUBE_UPLOAD_TAB_THUMBNAIL_MODEL = 'nanobanana2'

def _collect_reference_blueprint(style_reference_bytes = None):
    return analyze_reference_blueprint_payload(style_reference_bytes)


def _build_text_line_break_hint(display_text = None):
