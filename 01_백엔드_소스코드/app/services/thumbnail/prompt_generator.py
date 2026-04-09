# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: prompt_generator.pyc (Python 3.11)

'''
Prompt Generator Module (Pipeline Stage 3)
구조화된 프롬프트 자동 생성

Features:
- 5개 요소 기반 구조화된 프롬프트
- 가중치 기반 요소 조합
- 레퍼런스 분석 + 사용자 콘텐츠 통합
- 텍스트 렌더링 최적화 지시문
'''
import logging
from typing import Dict, Any, Optional
from types import ReferenceAnalysisResult, UserContentInput, PromptElements, GeneratedPrompt
logger = logging.getLogger(__name__)

class PromptGenerator:
    '''
    구조화된 프롬프트 생성 서비스

    5개 요소를 가중치 기반으로 조합하여
    AI 이미지 생성에 최적화된 프롬프트를 생성합니다.

    프롬프트 구조:
    [COMPOSITION] | [SUBJECT] | [STYLE_REFERENCE] | [TEXT_SPECIFICATION] | [TECHNICAL_SPECS]
    '''
    ELEMENT_WEIGHTS = {
        'composition': 0.2,
        'subject': 0.25,
        'style_reference': 0.2,
        'text_specification': 0.25,
        'technical_specs': 0.1 }
    
    def __init__(self):
        pass

    
    def generate_prompt(self = None, reference_analysis = None, user_content = None, style_override = (None,)):
        '''
        분석 데이터 기반 프롬프트 생성

        Args:
            reference_analysis: 1단계 분석 결과
            user_content: 2단계 콘텐츠 입력
            style_override: 스타일 직접 지정 (선택)

        Returns:
            GeneratedPrompt: 생성된 프롬프트
        '''
        
        try:
            elements = PromptElements(composition = self._generate_composition(reference_analysis), subject = self._generate_subject(user_content), style_reference = self._generate_style_reference(reference_analysis, style_override), text_specification = self._generate_text_specification(reference_analysis, user_content), technical_specs = self._generate_technical_specs(reference_analysis))
            full_prompt = self._combine_elements(elements)
            return GeneratedPrompt(full_prompt = full_prompt, elements = elements, prompt_length = len(full_prompt))
        except Exception:
            e = None
            logger.error(f'''Prompt generation failed: {e}''', exc_info = True)
            del e
            return None
            None = 
            del e


    
    def _generate_composition(self = None, analysis = None):
        '''구성 요소 생성 (20%)'''
        layout = analysis.layout
        text_coverage = layout.text_coverage_ratio
        is_vertical = layout.is_vertical
        if text_coverage > 0.3:
            base = 'Professional YouTube thumbnail with strong visual hierarchy, text-dominant composition, clear focal point with balanced negative space'
        elif text_coverage > 0.15:
            base = 'Professional YouTube thumbnail with balanced text and visual elements, clean composition with strategic text placement, high-contrast layout for maximum engagement'
        else:
            base = 'Professional YouTube thumbnail with emphasis on subject, minimal text overlay, visual-first composition with strong focal point'
        if is_vertical:
            base += ', vertical format optimized for mobile viewing'
        return base

    
    def _generate_subject(self = None, user_content = None):
        '''피사체 설명 생성 (25%)'''
        subject = user_content.subject_image
        description = subject.description
        mood = subject.mood
        subjects = subject.subjects
        parts = []
        if description:
            parts.append(f'''Subject: {description}''')
        if mood:
            parts.append(f'''mood: {mood}''')
        if subjects:
            parts.append(f'''featuring {', '.join(subjects[:3])}''')
        parts.append('sharp focus, well-lit, professional quality')
        return ', '.join(parts) if parts else 'Subject: professional scene, high quality'

    
    def _generate_style_reference(self = None, analysis = None, style_override = None):
        '''스타일 레퍼런스 생성 (20%)'''
        if style_override:
            return f'''Style: {style_override}'''
        colors = None.color_palette
        primary_color = colors.primary_color
        raw_style = analysis.raw_data.get('style', { })
        overall_style = raw_style.get('overallStyle', '')
        mood = raw_style.get('mood', '')
        style_parts = []
        if overall_style and overall_style != 'Unknown':
            style_parts.append(f'''{overall_style} style''')
        else:
            style_parts.append('professional thumbnail style')
        style_parts.append(f'''with {primary_color} as accent color''')
        if mood and mood != 'Unknown':
            style_parts.append(f'''{mood} atmosphere''')
        style_parts.extend([
            'bold contrasting elements',
            'cinematic lighting',
            'professional color grading',
            'dramatic shadows'])
        return 'Style: ' + ', '.join(style_parts)

    
    def _generate_text_specification(self = None, analysis = None, user_content = None):
        '''텍스트 명세 생성 (25%)'''
        user_text = user_content.additional_text
        style_analysis = analysis.style_analysis
        if not style_analysis.average_font_size:
            font_size = 72
            if not style_analysis.dominant_font_weight:
                font_weight = 'bold'
                parts = []
                if user_text.main_text:
                    parts.append(f'''Large {font_weight} Korean text \'{user_text.main_text}\' at approximately {font_size}px, white color with black stroke effect for readability''')
        if user_text.sub_text:
            parts.append(f'''Secondary text \'{user_text.sub_text}\' in smaller size, positioned complementary to main text''')
        if user_text.cta_text:
            parts.append(f'''Call-to-action text \'{user_text.cta_text}\' with contrasting background for visibility''')
        if hasattr(user_text, 'floating_texts') and user_text.floating_texts:
            for floating in user_text.floating_texts:
                if hasattr(floating, 'text'):
                    text = floating.text
                    position = floating.position
                elif isinstance(floating, dict):
                    text = floating.get('text', '')
                    position = floating.get('position', 'top-left')
                
                if text:
                    position_desc = self._get_position_description(position)
                    parts.append(f'''Auxiliary text \'{text}\' at {position_desc}, smaller supporting text''')
                parts.extend([
                    'clear legibility',
                    'proper character spacing',
                    'anti-aliased text rendering',
                    'high contrast for mobile visibility'])
        return 'Text: ' + ', '.join(parts) if parts else ''

    
    def _get_position_description(self = None, position = None):
        '''플로팅 텍스트 위치를 자연어 설명으로 변환'''
        position_map = {
            'top-left': 'the top-left corner',
            'top-right': 'the top-right corner',
            'bottom-left': 'the bottom-left corner',
            'bottom-right': 'the bottom-right corner',
            'center-left': 'the left side',
            'center-right': 'the right side' }
        return position_map.get(position, 'the corner')

    
    def _generate_technical_specs(self = None, analysis = None):
