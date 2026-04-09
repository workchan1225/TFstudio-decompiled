# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: prompt_section.pyc (Python 3.11)

'''
Prompt Section - 프롬프트 섹션 데이터 구조

프롬프트를 구조화된 섹션으로 분리하여 관리합니다.
각 섹션은 우선순위를 가지며, 토큰 예산 초과 시
낮은 우선순위 섹션부터 절단됩니다.
'''
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Optional, List

class SectionPriority(IntEnum):
    '''섹션 우선순위 (1이 가장 높음, 5가 가장 낮음)'''
    CORE = 1
    CONTINUITY = 2
    STYLE = 3
    NEGATIVE = 4
    OPTIONAL = 5

SECTION_PRIORITIES = {
    'core_context': SectionPriority.CORE,
    'core_subject': SectionPriority.CORE,
    'continuity': SectionPriority.CONTINUITY,
    'style': SectionPriority.STYLE,
    'negative_guidance': SectionPriority.NEGATIVE,
    'optional_enhancers': SectionPriority.OPTIONAL }
PromptSection = <NODE:12>()
PromptSections = <NODE:12>()
