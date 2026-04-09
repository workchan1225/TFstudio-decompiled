# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rule_loader.pyc (Python 3.11)

"""
RuleLoader - Single Source of Truth for Style/Historical Rules

All style emphasis keywords, historical context keywords, and category mappings
are loaded from JSON files in the data/ directory.

Usage:
    from app.services.scene.rule_loader import RuleLoader

    # Get style emphasis for a category
    style = RuleLoader.get_style_emphasis('animation_murim')

    # Get historical keywords
    keywords = RuleLoader.get_historical_keywords()

    # Check if a category is historical
    is_historical = RuleLoader.is_historical_style_category('animation_folktale')
"""
import json
import logging
from typing import Dict, List, Set, Optional
from pathlib import Path
logger = logging.getLogger(__name__)

def _resolve_data_dir():
    '''Resolve scene rule data directory for both dev and frozen builds.'''
    
    try:
        get_scene_data_path = get_scene_data_path
        import app.config.paths
        return get_scene_data_path()
    except Exception:
        return 


_DATA_DIR = _resolve_data_dir()

class RuleLoader:
    '''Centralized loader for style and historical rules.'''
    _style_rules_cache: Optional[Dict] = None
    _historical_rules_cache: Optional[Dict] = None
    _load_json = (lambda cls = None, filename = None: filepath = _DATA_DIR / filenametry:
f = open(filepath, 'r', encoding = 'utf-8')try:
None(None, None)with None:
if not None, json.load(f):
try:
try:
Noneexcept FileNotFoundError:
logger.warning(f'''[RuleLoader] {filename} not found at {filepath}, using empty dict''')except json.JSONDecodeError:
logger.error(f'''[RuleLoader] Error parsing {filename} at {filepath}: {e}''')del eNoneNone = del e)()
    _get_style_rules = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    _get_historical_rules = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    get_style_emphasis_keywords = (lambda cls = None: rules = cls._get_style_rules()rules.get('style_emphasis_keywords', { }))()
    get_style_emphasis = (lambda cls = None, visual_category = None:
