# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: prompt_composer.pyc (Python 3.11)

'''
Prompt Composer - 섹션 기반 프롬프트 조립

여러 소스(컨텍스트, 캐릭터, 스타일 등)에서 정보를 모아
우선순위 기반으로 프롬프트를 조립합니다.

핵심 기능:
- 섹션별 프롬프트 수집
- 신뢰도 기반 충돌 해결
- 토큰 예산 관리
- 최종 프롬프트 생성
'''
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from prompt_section import PromptSection, PromptSections, SectionPriority
from conflict_resolver import DynamicConflictResolver
from budget_manager import BudgetManager
from enhancer_selector import EnhancerSelector, select_best_enhancers
ComposedPrompt = <NODE:12>()

class PromptComposer:
    '''
    섹션 기반 프롬프트 조립기

    여러 분석 결과를 통합하여 최종 프롬프트를 생성합니다.
    '''
    
    def __init__(self = None, token_budget = None, style_template = None, genre = (2000, None, 'default')):
