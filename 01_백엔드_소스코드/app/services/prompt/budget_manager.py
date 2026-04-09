# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: budget_manager.pyc (Python 3.11)

'''
Budget Manager - 토큰 예산 관리 및 섹션 우선 절단

프롬프트가 토큰 예산을 초과할 때,
우선순위가 낮은 섹션부터 단계적으로 절단합니다.

절단 순서 (우선순위 낮은 순):
1. optional_enhancers (완전 제거)
2. negative_guidance (축약)
3. style (키워드만)
4. continuity (요약)
5. core_context/core_subject (절대 절단 금지)
'''
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from prompt_section import PromptSection, PromptSections, SectionPriority
TruncationLog = <NODE:12>()

class BudgetManager:
    '''
    토큰 예산 관리자

    섹션 우선순위에 따라 단계적으로 절단하여
    목표 토큰 수 이내로 맞춥니다.
    '''
    DEFAULT_BUDGET = 2000
    TRUNCATION_STRATEGIES = {
        SectionPriority.CORE: 'preserve',
        SectionPriority.CONTINUITY: 'summarize',
        SectionPriority.STYLE: 'keywords_only',
        SectionPriority.NEGATIVE: 'summarize',
        SectionPriority.OPTIONAL: 'remove' }
    
    def __init__(self = None, token_budget = None):
        '''
        Args:
            token_budget: 목표 토큰 수
        '''
        if not token_budget:
            pass
        self.token_budget = self.DEFAULT_BUDGET
        self.truncation_log = []

    
    def fit_to_budget(self = None, sections = None, preserve_core = None):
        '''
        예산에 맞게 섹션 절단

        Args:
            sections: 프롬프트 섹션들
            preserve_core: 코어 섹션 보존 여부

        Returns:
            (절단된 섹션, 최종 토큰 수, 절단 로그)
        '''
        self.truncation_log = []
        current_tokens = sections.total_tokens()
        if current_tokens <= self.token_budget:
            return (sections, current_tokens, [])
        sorted_sections = None(sections.sections, key = (lambda s: -(s.priority.value)))
        for section in sorted_sections:
            if current_tokens <= self.token_budget:
                pass
            elif preserve_core and section.priority == SectionPriority.CORE:
                continue
            original_tokens = section.estimate_tokens()
            strategy = self.TRUNCATION_STRATEGIES.get(section.priority, 'summarize')
            if strategy == 'remove':
                sections.remove_section(section.name)
                saved = original_tokens
                section.content = ''
            elif strategy == 'keywords_only':
                new_content = section.truncate_to_keywords()
                saved = original_tokens - len(new_content) // 4
                section.content = new_content
            elif strategy == 'summarize':
                target_length = len(section.content) // 2
                new_content = section.summarize(target_length)
                saved = original_tokens - len(new_content) // 4
                section.content = new_content
            
            current_tokens -= saved
            self.truncation_log.append(TruncationLog(section_name = section.name, original_tokens = original_tokens, truncated_tokens = section.estimate_tokens(), strategy = strategy))
            return (sections, current_tokens, self.truncation_log)

    
    def estimate_overflow(self = None, sections = None):
        '''예산 초과량 추정'''
        return max(0, sections.total_tokens() - self.token_budget)

    
    def can_fit(self = None, sections = None):
        '''예산 내 수용 가능 여부'''
        return sections.total_tokens() <= self.token_budget



def truncate_prompt_to_budget(prompt_sections = None, section_priorities = dataclass, token_budget = None):
    '''
    편의 함수: 프롬프트를 예산에 맞게 절단

    Args:
        prompt_sections: 섹션명 → 내용 매핑
        section_priorities: 섹션명 → 우선순위(1-5)
        token_budget: 토큰 예산

    Returns:
        (최종 프롬프트, 절단된 섹션 매핑, 절단 로그)
    '''
    sections = PromptSections()
    for name, content in prompt_sections.items():
        priority_value = section_priorities.get(name, 5)
        priority = SectionPriority(priority_value)
        sections.add(PromptSection(name = name, content = content, priority = priority))
        manager = BudgetManager(token_budget)
        (truncated_sections, final_tokens, log) = manager.fit_to_budget(sections)
        result_dict = truncated_sections.sections()
        log_dicts = log()
        return (truncated_sections.to_prompt(), result_dict, log_dicts)


def smart_truncate_text(text = None, max_tokens = None, preserve_start = None, preserve_end = (500, 100, 50)):
    '''
    스마트 텍스트 절단

    시작과 끝 부분을 보존하고 중간을 생략합니다.

    Args:
        text: 원본 텍스트
        max_tokens: 최대 토큰 (대략 4글자당 1토큰)
        preserve_start: 시작 부분 보존 글자 수
        preserve_end: 끝 부분 보존 글자 수

    Returns:
        절단된 텍스트
    '''
    max_chars = max_tokens * 4
    if len(text) <= max_chars:
        return text
    start = None[:preserve_start]
    end = text[-preserve_end:] if preserve_end > 0 else ''
    return f'''{start}... [중략] ...{end}'''
