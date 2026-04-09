# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: custom_style_template_store.pyc (Python 3.11)

'''
Persistent store for custom style templates.

Custom style templates are mirrored into an AppData JSON manifest so they can
survive reinstall/reset workflows and be user-managed outside the DB.
'''
from __future__ import annotations
import json
import logging
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple
from app import db
from app.config.paths import get_custom_style_templates_manifest_path
from app.models.image_prompt_template import ImagePromptTemplate
logger = logging.getLogger(__name__)

class CustomStyleTemplateStore:
    '''Bidirectional sync between DB custom styles and AppData JSON manifest.'''
    SCHEMA_VERSION = 1
    _manifest_path = (lambda cls = None: get_custom_style_templates_manifest_path())()
    _empty_manifest = (lambda cls = None: {
'version': cls.SCHEMA_VERSION,
'updatedAt': datetime.now(timezone.utc).isoformat(),
'templates': [] })()
    _parse_datetime = (lambda value = None: if not value:
datetime.min# WARNING: Decompyle incomplete
)()
    _to_int = (lambda value = None, default = None: try:
int(value)except (TypeError, ValueError):
)()
    _to_bool = (lambda value = None, default = None: if isinstance(value, bool):
value# WARNING: Decompyle incomplete
)()
    _normalize_prompt_template = (lambda prompt_template = None: if not prompt_template:
text = str('').replace('\r\n', '\n').replace('\r', '\n').strip()if not text:
'{base_prompt}'text = None.sub('\\n{3,}', '\n\n', text)text = re.sub('[ \\t]{2,}', ' ', text)if text.lstrip().startswith('{base_prompt}'):
textif None in text:
text = text.replace('{base_prompt}', '').strip(', \n')if text:
'{base_prompt}\n\n' + text)()
    _normalize_template_dict = (lambda cls = None, template = None: if not isinstance(template, dict):
{ }# WARNING: Decompyle incomplete
)()
    _load_manifest = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    _write_manifest = (lambda cls = None, templates = None: pass# WARNING: Decompyle incomplete
)()
    _build_index = (lambda cls = None, templates = None: result = { }for item in templates:
normalized = cls._normalize_template_dict(item)if not normalized:
continuetemplate_id = normalized['id']existing = result.get(template_id)if existing and cls._parse_datetime(existing.get('updatedAt')) > cls._parse_datetime(normalized.get('updatedAt')):
continueresult[template_id] = normalizedresult)()
    upsert_template_dict = (lambda cls = None, template = None: normalized = cls._normalize_template_dict(template)if not normalized:
Falsemanifest = None._load_manifest()index = cls._build_index(manifest.get('templates', []))template_id = normalized['id']existing = index.get(template_id)if existing and cls._parse_datetime(existing.get('updatedAt')) > cls._parse_datetime(normalized.get('updatedAt')):
Falseindex[template_id] = Nonecls._write_manifest(list(index.values()))True)()
    upsert_from_model = (lambda cls = None, model = None: if model and model.type != 'style' or model.visual_category != 'custom':
FalseNone.upsert_template_dict(model.to_dict()))()
    remove_template = (lambda cls = None, template_id = None:
