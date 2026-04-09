# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: title_pattern_profile.pyc (Python 3.11)

__doc__ = '\nTitle pattern profile utilities.\n\naaa.txt의 CTR 패턴(미완성 정보, 계층 대비, 시간 압박, 통념 파괴, 비밀 프레임)을\n공통 규칙으로 정규화하여 여러 제목 생성 흐름에서 재사용합니다.\n'
from __future__ import annotations
import re
from typing import Any, Dict, List, Literal, Tuple
TitleStyleProfile = Literal[('balanced', 'aggressive', 'hybrid')]
DEFAULT_TITLE_STYLE_PROFILE: 'TitleStyleProfile' = 'hybrid'
DEFAULT_TITLE_STYLE_MIX = 50
_VALID_PROFILES = {
    'hybrid',
    'balanced',
    'aggressive'}
# WARNING: Decompyle incomplete
