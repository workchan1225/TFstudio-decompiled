# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base_genre.pyc (Python 3.11)

'''
BaseGenre - 장르 기본 추상 클래스

모든 장르가 상속해야 하는 추상 클래스.
장르별 특화 프롬프트, 성공 공식, 스토리 구조 등을 정의.
'''
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum

class GenreCategory(Enum, str):
    '''장르 카테고리'''
    DRAMA = 'drama'
    INFO = 'info'
    DOCU = 'docu'
    NEWS = 'news'
    VARIETY = 'variety'

GenreSuccessFormula = <NODE:12>()

class BaseGenre(ABC):
    '''
    장르 기본 추상 클래스

    모든 장르 클래스는 이 클래스를 상속하고
    필수 프로퍼티와 메서드를 구현해야 함.
    '''
    code = (lambda self = None: pass)()()
    name = (lambda self = None: pass)()()
    category = (lambda self = None: pass)()()
    definition = (lambda self = None: pass)()()
    tone_style = (lambda self = None: pass)()()
    required_elements = (lambda self = None: pass)()()
    success_formula = (lambda self = None: GenreSuccessFormula(emotional_arc = '일상 → 갈등 → 해결 → 여운', key_elements = self.required_elements, pov = '3인칭 전지적 작가 시점', target_audience = '40~60대'))()
    synopsis_structure = (lambda self = None: {
'기': [
'상황 설정',
'인물 소개'],
'승': [
'갈등 발생',
'문제 심화'],
'전': [
'클라이맥스',
'반전'],
'결': [
'해결',
'여운'] })()
    image_prompt_style = (lambda self = None: '포토리얼리스틱, 한국 드라마 스타일')()
    recommended_tone = (lambda self = None: '소설체')()
    recommended_narration_ratio = (lambda self = None: 50)()
    
    def build_genre_prompt(self = None):
        '''
        장르 프롬프트 빌드

        기본 구현 제공, 필요시 오버라이드 가능.

        Returns:
            장르별 특화 프롬프트 문자열
        '''
        elements_str = (lambda .0: [ f'''    {i + 1}. {elem}''' for i, elem in .0 ])(enumerate(self.required_elements)())
        return f'''\n## 장르: {self.name} ({self.code})\n\n### 핵심 개념\n{self.definition}\n\n### 톤 & 스타일\n{self.tone_style}\n\n### 필수 요소\n{elements_str}\n\n### 흥행 공식\n- **감정선**: {self.success_formula.emotional_arc}\n- **시점**: {self.success_formula.pov}\n- **타겟**: {self.success_formula.target_audience}\n\n### 이미지 스타일\n{self.image_prompt_style}\n\n---\n⚠️ 위 요소들을 대본에 반드시 포함하세요.\n'''

    
    def build_expansion_prompt(self = None, chapter_count = None):
        '''
        대본 확장용 프롬프트 빌드 (고도화 v2.0)

        Args:
            chapter_count: 챕터 수

        Returns:
            확장용 프롬프트 (금지 사항 + 문장력 가이드 포함)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_hooking_prompt(self = None):
        '''
        인트로 후킹 프롬프트 (선택적 오버라이드)

        Returns:
            후킹 프롬프트
        '''
        if not self.success_formula.hook_psychology:
            return ''
        return f'''{self.name})\n- **심리적 원리**: {self.success_formula.hook_psychology}\n- 시청자의 호기심을 자극하는 강력한 오프닝 필수\n'''

    
    def to_dict(self = None):
        '''장르 정보를 딕셔너리로 변환'''
        return {
            'code': self.code,
            'name': self.name,
            'category': self.category.value,
            'definition': self.definition,
            'toneStyle': self.tone_style,
            'requiredElements': self.required_elements,
            'recommendedTone': self.recommended_tone,
            'recommendedNarrationRatio': self.recommended_narration_ratio }
