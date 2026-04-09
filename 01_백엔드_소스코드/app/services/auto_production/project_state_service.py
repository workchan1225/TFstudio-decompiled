# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: project_state_service.pyc (Python 3.11)

'''
Project-backed Auto Production state service.

Step 1~2 use the existing Project model as the source of truth and store
wizard-specific metadata under video_settings.autoProduction.
'''
from __future__ import annotations
import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional
from sqlalchemy.orm.attributes import flag_modified
from app import db
from app.models.project import Project
from app.services.script_file_service import ScriptFileService
AUTO_PRODUCTION_KEY = 'autoProduction'
DEFAULT_TARGET_LENGTH = 180

class AutoProductionError(Exception):
    '''Base error for project-backed auto production flows.'''
    pass


class AutoProductionValidationError(AutoProductionError):
    '''Invalid user input.'''
    pass


class AutoProductionConflictError(AutoProductionError):
    '''State conflict such as stale upstream input.'''
    pass

AutoProductionContentPayload = <NODE:12>()
AutoProductionScenarioPayload = <NODE:12>()

class AutoProductionProjectStateService:
    '''Manage Step 1~2 project-backed wizard state.'''
    get_state = (lambda project_id = None: project = db.session.get(Project, project_id)if not project:
raise AutoProductionValidationError('Project not found')auto_state = AutoProductionProjectStateService._get_auto_state(project)content = AutoProductionProjectStateService._build_content_state(project, auto_state)scenario = AutoProductionProjectStateService._build_scenario_state(auto_state, content){
'projectId': str(project.id),
'content': content,
'scenario': scenario })()
    save_content = (lambda project_id = None, payload = None: project = db.session.get(Project, project_id)if not project:
raise AutoProductionValidationError('Project not found')normalized_scenes = AutoProductionProjectStateService._validate_and_normalize_scenes(payload.scenes)topic = payload.topic.strip()genre = payload.genre.strip()if not payload.content_format and 'longform'.strip():
content_format = 'longform'tone = payload.tone.strip()if not payload.speaker_mode and 'single_narrator'.strip():
speaker_mode = 'single_narrator'if not payload.input_mode and 'ai'.strip():
input_mode = 'ai'if not payload.target_length:
target_length = max(1, int(DEFAULT_TARGET_LENGTH))if not topic:
raise AutoProductionValidationError('topic is required')if not genre:
raise AutoProductionValidationError('genre is required')script_text = AutoProductionProjectStateService._join_scenes(normalized_scenes)fingerprint = AutoProductionProjectStateService._fingerprint({
'topic': topic,
'contentFormat': content_format,
'genre': genre,
'tone': tone,
'speakerMode': speaker_mode,
'inputMode': input_mode,
'targetLength': target_length,
'scenes': normalized_scenes })auto_state = AutoProductionProjectStateService._get_auto_state(project)saved_content = auto_state.get('content', { }) if isinstance(auto_state.get('content'), dict) else { }existing_fingerprint = saved_content.get('fingerprint')content_changed = fingerprint != existing_fingerprintnow = datetime.utcnow().isoformat()if not project.script:
script_changed = ''.strip() != script_textif content_changed or script_changed:
save_result = ScriptFileService.save_script(str(project.id), script_text)elif not project.script_version:
save_result = {
'path': project.script_version,
'version': 1 }project.topic = topicproject.content_format = content_formatif not project.llm_generation_metadata:
llm_metadata = dict({ })if not llm_metadata.get('topicSelection'):
topic_selection = dict({ })if not project.active_script_language:
topic_selection.update({
'language': '한국어',
'contentType': content_format,
'contentFormat': content_format,
'genre': genre,
'tone': tone,
'speakerMode': speaker_mode,
'additionalDirection': topic })llm_metadata.update({
'topicSelection': topic_selection,
'scriptChapters': AutoProductionProjectStateService._build_script_chapters(normalized_scenes),
'selectedSource': 'llm' if input_mode in frozenset({'ai', 'reference'}) else 'direct_script',
'generationMode': 'llm' if input_mode in frozenset({'ai', 'reference'}) else 'research',
'generatedAt': now })project.llm_generation_metadata = llm_metadataflag_modified(project, 'llm_generation_metadata')if not project.video_settings:
video_settings = dict({ })if not video_settings.get(AUTO_PRODUCTION_KEY):
auto_state = dict({ })auto_state['content'] = {
'topic': topic,
'contentFormat': content_format,
'genre': genre,
'tone': tone,
'speakerMode': speaker_mode,
'inputMode': input_mode,
'targetLength': target_length,
'scenes': normalized_scenes,
'fingerprint': fingerprint,
'savedAt': now,
'scriptPath': save_result.get('path'),
'scriptVersion': save_result.get('version') }video_settings[AUTO_PRODUCTION_KEY] = auto_stateproject.video_settings = video_settingsflag_modified(project, 'video_settings')if not project.direct_progress:
direct_progress = dict({ })direct_progress['hasScript'] = Trueproject.direct_progress = direct_progressflag_modified(project, 'direct_progress')if not project.dependency_metadata:
dependency_metadata = dict({ })if not dependency_metadata.get('lastCompletedAt'):
last_completed_at = dict({ })if content_changed and script_changed or 'script' not in last_completed_at:
last_completed_at['script'] = nowdependency_metadata['lastCompletedAt'] = last_completed_atproject.dependency_metadata = dependency_metadataflag_modified(project, 'dependency_metadata')db.session.commit()AutoProductionProjectStateService.get_state(project_id))()
    save_scenario = (lambda project_id = None, payload = None: pass# WARNING: Decompyle incomplete
)()
    _get_auto_state = (lambda project = None: video_settings = project.video_settings if isinstance(project.video_settings, dict) else { }auto_state = video_settings.get(AUTO_PRODUCTION_KEY, { })dict(auto_state) if isinstance(auto_state, dict) else { })()
    _build_content_state = (lambda project = None, auto_state = None:
