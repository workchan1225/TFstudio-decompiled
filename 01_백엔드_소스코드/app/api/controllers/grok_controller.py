# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: grok_controller.pyc (Python 3.11)

'''
Grok Automation Controller

Handles Grok web automation for image-to-video conversion.

Registration in app/__init__.py:
    from app.api.controllers import grok_controller_bp
    app.register_blueprint(grok_controller_bp)

Endpoints (11):
- GET /api/grok/status - Check Grok authentication status
- GET /api/grok/diagnostics - Diagnose Grok login/browser/profile state
- GET /api/grok/generation-status - Check global generation lock status
- POST /api/grok/login - Start Grok login (opens browser, non-blocking)
- POST /api/grok/login/complete - Complete login (save session, close browser)
- POST /api/grok/logout - Logout from Grok
- POST /api/grok/pause - Pause generation (keep browser open for resume)
- GET /api/projects/<project_id>/grok/tasks - List Grok tasks for project
- POST /api/projects/<project_id>/grok/tasks/batch - Create batch tasks
- PUT /api/projects/<project_id>/grok/tasks/<task_id> - Update task status
- DELETE /api/projects/<project_id>/grok/tasks/<task_id> - Cancel/delete task
- POST /api/projects/<project_id>/grok/generate - Start video generation (SSE)
'''
from flask import Blueprint, request, jsonify, Response, current_app
from werkzeug.exceptions import HTTPException
import logging
import json
import os
import re
import threading
from datetime import datetime
from app.models.project import Project
from app.models.grok_automation import GrokAutomationTask, GrokCredentials
from app import db
from app.services.scene.line_index_matcher import normalize_keyword_text_for_matching
from app.utils.ffmpeg_utils import probe_video_has_audio
logger = logging.getLogger(__name__)
_grok_service = None
_generation_state_lock = threading.Lock()
_generation_running = False
_generation_project_id = None
_generation_started_at = None
IN_PROGRESS_GROK_TASK_STATUSES = ('starting', 'uploading', 'processing', 'generating', 'downloading')
RESETTABLE_GROK_TASK_STATUSES = ('failed',) + IN_PROGRESS_GROK_TASK_STATUSES

def _try_acquire_generation_slot(project_id = None):
    '''Try to acquire the singleton Grok generation slot.'''
    global _generation_running, _generation_project_id, _generation_started_at
    _generation_state_lock
    if _generation_running:
        None(None, None)
        return 
    project_id = None
    _generation_started_at = datetime.utcnow()
    None(None, None)
    return (True, None, None)
    with None:
        if not None:
            pass


def _release_generation_slot():
    '''Release the singleton Grok generation slot.'''
    global _generation_running, _generation_project_id, _generation_started_at
    _generation_state_lock
    _generation_running = False
    _generation_project_id = None
    _generation_started_at = None
    None(None, None)
    return None
    with None:
        if not None:
            pass


def _get_generation_slot_snapshot():
    '''Return current singleton generation slot state.'''
    _generation_state_lock
    None(None, None)
    return 
    with None:
        if not None, (_generation_running, _generation_project_id, _generation_started_at):
            pass


def get_grok_service():
    '''Get or create grok service instance (lazy loading).'''
    pass
# WARNING: Decompyle incomplete


def _normalize_grok_video_path(path_value = None):
    '''Normalize stored/video URL paths into data-relative forward-slash form.'''
    if not path_value or isinstance(path_value, str):
        return ''
    normalized = None.replace('\\', '/').strip()
    if not normalized:
        return ''
    if None.startswith('http://') and normalized.startswith('https://') or normalized.startswith('data:'):
        return ''
    if None.startswith('/data/'):
        normalized = normalized[len('/data/'):]
    elif normalized.startswith('data/'):
        normalized = normalized[len('data/'):]
    else:
        normalized = normalized.lstrip('/')
    return normalized


def _normalize_scene_binding_id(scene_id = None, chapter_index = None, scene_index = None):
    if isinstance(scene_id, str) and scene_id.strip():
        return scene_id.strip()
    if None(chapter_index, int) and isinstance(scene_index, int):
        return f'''ch{chapter_index}_sc{scene_index}'''


def _normalize_source_binding_number(value = None):
    if isinstance(value, bool):
        return None
    if None(value, int):
        return value
    if None(value, float) and value.is_integer():
        return int(value)


def _build_scene_source_binding(scene = None, fallback_scene_id = None, fallback_chapter_index = None, fallback_scene_index = ('scene', dict, 'fallback_scene_id', str, 'fallback_chapter_index', int, 'fallback_scene_index', int, 'return', dict)):
