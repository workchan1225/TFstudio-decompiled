# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: style_emphasis.pyc (Python 3.11)

__doc__ = '\n스타일 강조 키워드 시스템\n\nNanoBanana 이미지 생성에 최적화된 스타일 강조 키워드\n- 카테고리별 prefix, keywords 제공\n- 프롬프트 앞부분에 스타일 강조 추가\n- 네거티브 표현은 자연어로 프롬프트 내 포함 (NanoBanana 방식)\n\nv1.8.0: RuleLoader를 통한 SSOT(Single Source of Truth) 통합\n- 모든 스타일 규칙은 scene/data/style_rules.json에서 로드\n'
import re
from typing import Dict, Optional
from style_profile_filter import contains_content_leak, sanitize_style_fragments
from app.services.scene.rule_loader import RuleLoader

def _get_style_emphasis_keywords():
    '''RuleLoader를 통해 스타일 강조 키워드 반환'''
    return RuleLoader.get_style_emphasis_keywords()

# WARNING: Decompyle incomplete
