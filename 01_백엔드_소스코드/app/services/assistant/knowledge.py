# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: knowledge.pyc (Python 3.11)

'''Deterministic search over the assistant knowledge catalog.'''
from __future__ import annotations
import json
import logging
import re
from pathlib import Path
from typing import Any
from seed import ASSISTANT_KNOWLEDGE_SEED
logger = logging.getLogger(__name__)
_CATALOG_CACHE: 'dict[str, Any] | None' = None
_CATALOG_PATH = Path(__file__).resolve().parent / 'data' / 'assistant_knowledge_catalog.json'

def _normalize_string(value = None):
