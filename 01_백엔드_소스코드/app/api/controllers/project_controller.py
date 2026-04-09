# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: project_controller.pyc (Python 3.11)

"""
Project Controller (Clean Architecture Version)

Thin controller that handles HTTP concerns and delegates to Use Cases.
This is the primary Projects API controller, replacing the v1 projects.py.

Registration in app/__init__.py:
    from app.api.controllers import project_controller_bp
    app.register_blueprint(project_controller_bp, url_prefix='/api/projects')
"""
from flask import Blueprint, request, jsonify, Response, current_app
from sqlalchemy.orm.attributes import flag_modified
from werkzeug.utils import secure_filename
from werkzeug.exceptions import HTTPException
import logging
import os
import json
import re
import shutil
import uuid
import traceback
import base64
import binascii
from pathlib import Path
from datetime import datetime
from copy import deepcopy
from typing import Optional
import threading
import queue
from app import db
from app.models.project import Project, Character
from app.infrastructure.repositories import SQLAlchemyProjectRepository
from app.application.use_cases import CreateProjectUseCase, GetProjectUseCase, GetAllProjectsUseCase, UpdateProjectUseCase, DeleteProjectUseCase, SetProjectTopicUseCase, SetProjectScriptUseCase
from app.application.dtos import CreateProjectRequest, GetProjectRequest, UpdateProjectRequest, DeleteProjectRequest, SetTopicRequest, SetScriptRequest
from app.application.exceptions import ValidationException, NotFoundException
from app.services.cleanup_service import CleanupService
from app.services.sync_service import SyncService
from app.utils.file_paths import ProjectPaths
from app.utils.process_manager import process_manager
from app.utils.image_storage import save_scene_images_to_files, load_scene_images_with_data, delete_project_scene_images, delete_project_scene_image_paths, delete_project_scene_images_only, scan_character_images_from_disk
from app.utils.uploaded_media_metadata import infer_uploaded_media_source_metadata, is_disallowed_flow_output_media, normalize_uploaded_media_binding_metadata, normalize_uploaded_media_source_metadata
from app.config.paths import get_data_path
logger = logging.getLogger(__name__)
SCENE_LABEL_PATTERNS = (re.compile('ch0*(\\d+)_sc0*(\\d+)', re.IGNORECASE), re.compile('ch0*(\\d+)_0*(\\d+)', re.IGNORECASE), re.compile('chapter0*(\\d+)_scene0*(\\d+)', re.IGNORECASE))
INTRO_LABEL_PATTERN = re.compile('intro_(\\d+)', re.IGNORECASE)
IMAGE_FILE_EXTENSIONS = {
    '.jpeg',
    '.bmp',
    '.gif',
    '.jpg',
    '.png',
    '.webp'}
project_controller_bp = Blueprint('projects', __name__)
ffmpeg_instances = { }

def get_repository():
    '''Get repository instance with current session'''
    return SQLAlchemyProjectRepository(db.session)


def _normalize_scene_split_mode(value = None):
    if value == 'ai' or value == 'local':
        return value


def _normalize_scene_reset_scope(value = None):
    if value == 'all':
        return 'all'
    if None == 'ai' or value == 'local':
        return value


def _normalize_split_variants_payload(value = None):
    if not isinstance(value, dict):
        return { }
    normalized = None
    for mode in ('ai', 'local'):
        raw_variant = value.get(mode)
        if not isinstance(raw_variant, dict):
            continue
        scene_images = raw_variant.get('sceneImages')
        normalized[mode] = {
            'sceneImages': scene_images if isinstance(scene_images, list) else [],
            'sceneSplitSettings': raw_variant.get('sceneSplitSettings'),
            'hasRegisteredToMedia': raw_variant.get('hasRegisteredToMedia') is True,
            'hasSavedToServer': raw_variant.get('hasSavedToServer') is True }
        return normalized


def _build_empty_split_variant_state():
    return {
        'sceneImages': [],
        'sceneSplitSettings': None,
        'hasRegisteredToMedia': False,
        'hasSavedToServer': True }


def _collect_scene_image_paths(scene_images = None):
    if not isinstance(scene_images, list):
        return []
    collected_paths = None
    seen_paths = set()
    for scene in scene_images:
        if not isinstance(scene, dict):
            continue
        image_path = scene.get('imagePath')
        if not isinstance(image_path, str) or image_path.strip():
            continue
        normalized_path = image_path.replace('\\', '/').strip()
        if normalized_path in seen_paths:
            continue
        seen_paths.add(normalized_path)
        collected_paths.append(normalized_path)
        return collected_paths


def _should_delete_scene_files_for_split_mode(mode = None):
    return mode != 'local'


def _should_persist_split_variant(scene_images = None, scene_split_settings = None, has_registered_to_media = None, has_saved_to_server = ('scene_images', list, 'scene_split_settings', object, 'has_registered_to_media', bool, 'has_saved_to_server', bool, 'return', bool)):
