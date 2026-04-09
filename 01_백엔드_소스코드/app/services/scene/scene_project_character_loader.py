# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_project_character_loader.pyc (Python 3.11)

from __future__ import annotations
import json
import logging
from typing import Any, Dict, Iterable, List, Optional
from models.project import Project
from utils.character_name_matcher import normalize_character_name
from utils.file_paths import ProjectPaths
logger = logging.getLogger(__name__)

def _normalize_text(value = None):
