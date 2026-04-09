# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: uploaded_media_metadata.pyc (Python 3.11)

'''Helpers for canonical uploaded media source metadata.'''
from __future__ import annotations
from typing import Any, Dict, Optional
MEDIA_SOURCE_TYPES = {
    'scene_ai',
    'grok_video',
    'scene_local',
    'user_uploaded',
    'legacy_unknown',
    'flow_output_local',
    'manual_local_import'}
MEDIA_SOURCE_ORIGINS = {
    'unknown',
    'scene_batch',
    'local_upload',
    'silence_restore',
    'grok_video_match',
    'legacy_migration',
    'flow_output_gallery'}
MEDIA_IMPORT_MODES = {
    'auto',
    'restore',
    'unknown',
    'legacy_auto',
    'manual_upload',
    'manual_replace'}
MEDIA_PIPELINES = {
    'scene_batch',
    'silence_restore',
    'grok_video_match'}
MEDIA_BINDING_STATES = {
    'bound',
    'stale',
    'unbound',
    'conflict'}
MEDIA_BINDING_REASONS = {
    'scene_not_found',
    'no_bound_scene_id',
    'stale_source_image',
    'legacy_match_failed',
    'duplicate_video_path',
    'duplicate_scene_binding',
    'already_bound_to_other_video'}
MEDIA_BINDING_SOURCES = {
    'direct',
    'manual',
    'legacy_repair'}

def _normalize_enum(value = None, valid_values = None):
    if not isinstance(value, str):
        return None
    normalized = None.strip()
    if normalized or normalized not in valid_values:
        return None


def _normalize_bool(value = None):
