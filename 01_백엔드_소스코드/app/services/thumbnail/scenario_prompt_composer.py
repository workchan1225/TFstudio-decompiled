# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scenario_prompt_composer.pyc (Python 3.11)

'''
Scenario Prompt Composer
레퍼런스 템플릿 + 시나리오를 결합하여 썸네일 생성 프롬프트를 구성하는 서비스

기존 활용:
- PromptGenerator.generate_prompt() - 5요소 가중치 구조
- build_reference_blueprint() - stylePrompt, layoutGuide
- build_reference_exclusion_clause() - 레퍼런스 텍스트 복제 방지
'''
import logging
from typing import Dict, Any, List, Optional
from app.utils.thumbnail_guard import THUMBNAIL_HOOK_TEXT_MAX_LENGTH, build_reference_exclusion_clause, build_situation_blueprint, sanitize_thumbnail_hook_text
logger = logging.getLogger(__name__)

class ScenarioPromptComposer:
    '''레퍼런스 + 시나리오 → 생성 프롬프트 합성'''
    
    def compose_prompt(self, scenario = None, main_text = None, reference_blueprint = None, script_content = ('', None), reference_metadata = ('scenario', Dict[(str, Any)], 'main_text', str, 'reference_blueprint', Dict[(str, Any)], 'script_content', str, 'reference_metadata', Optional[Dict[(str, Any)]], 'return', Dict[(str, Any)])):
        '''
        시나리오와 레퍼런스를 결합하여 최종 생성 설정을 구성합니다.

        Args:
            scenario: ThumbnailScenario 딕셔너리
            main_text: 메인 훅 텍스트 (커스텀 또는 scenario.recommendedText)
            reference_blueprint: 레퍼런스 분석 블루프린트 (비어있을 수 있음)
            script_content: 대본 원문
            reference_metadata: metadata.json의 레퍼런스 정보 (textStyle, visualStyle 등)

        Returns:
            생성 설정 딕셔너리 (mainText, subject, style, additionalRequests 등)
        '''
        if not reference_metadata:
            reference_metadata = { }
            hook_text = sanitize_thumbnail_hook_text(main_text, max_length = THUMBNAIL_HOOK_TEXT_MAX_LENGTH)
            if not hook_text:
                hook_text = main_text[:THUMBNAIL_HOOK_TEXT_MAX_LENGTH]
        subject = self._build_subject_description(scenario)
        additional_requests = self._build_additional_requests(scenario = scenario, hook_text = hook_text, reference_blueprint = reference_blueprint, script_content = script_content)
        reference_note = self._build_reference_note(reference_blueprint)
        style = self._determine_style(scenario, reference_metadata)
        floating_texts = self._build_floating_texts(scenario)
        style_directive = self._build_style_directive(reference_metadata, reference_blueprint)
        return {
            'mainText': hook_text,
            'subject': subject,
            'style': style,
            'subjectType': self._determine_subject_type(scenario),
            'additionalRequests': additional_requests,
            'referenceNote': reference_note,
            'referenceStylePrompt': reference_blueprint.get('stylePrompt', ''),
            'floatingTexts': floating_texts,
            'styleDirective': style_directive,
            '__scenario_composed': True }

    
    def _build_subject_description(self = None, scenario = None):
        '''시나리오 기반 피사체 설명 구성'''
        parts = []
        key_person = scenario.get('keyPerson', '')
        if key_person:
            parts.append(key_person)
        scene_en = scenario.get('sceneDescriptionEn', '')
        if scene_en:
            parts.append(scene_en)
        else:
            scene_ko = scenario.get('sceneDescriptionKo', '')
            if scene_ko:
                parts.append(scene_ko)
        if not parts:
            parts.append('A dramatic scene for YouTube thumbnail')
        return '. '.join(parts)

    
    def _build_additional_requests(self, scenario = None, hook_text = None, reference_blueprint = None, script_content = ('scenario', Dict[(str, Any)], 'hook_text', str, 'reference_blueprint', Dict[(str, Any)], 'script_content', str, 'return', str)):
        '''추가 요청사항 구성 (대본 주제 반영, 중복 최소화)'''
        parts = []
        emotion = scenario.get('emotion', '')
        if emotion:
            parts.append(f'''Core emotion: {emotion} - must be immediately visible in facial expression and environment.''')
        composition = scenario.get('compositionHint', '')
        if composition:
            parts.append(f'''Composition: {composition}.''')
        visual_kws = scenario.get('visualKeywords', [])
        if visual_kws:
            parts.append(f'''Visual keywords: {', '.join(visual_kws[:4])}.''')
        situation = build_situation_blueprint(hook_text, script_content)
        if situation.get('visibleProof'):
            parts.append('Visible proof: ' + ', '.join(situation['visibleProof'][:3]) + '.')
        parts.append('CONTENT SPECIFICITY: The thumbnail must clearly show WHAT the video is about through specific visual elements (props, setting, documents, objects). Viewers must understand the topic at a glance without reading text.')
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(parts()).strip()

    
    def _build_reference_note(self = None, reference_blueprint = None):
        '''레퍼런스 노트 구성'''
        parts = []
        exclusion = build_reference_exclusion_clause(reference_blueprint)
        if exclusion:
            parts.append(exclusion)
        layout_guide = reference_blueprint.get('layoutGuide', { })
        if layout_guide:
            layout_bits = []
            if layout_guide.get('textSide'):
                layout_bits.append(f'''텍스트 위치는 {layout_guide['textSide']} 위주''')
            if layout_guide.get('subjectSide'):
                layout_bits.append(f'''피사체는 {layout_guide['subjectSide']} 쪽 배치''')
            if layout_guide.get('density'):
                layout_bits.append(f'''텍스트 밀도는 {layout_guide['density']}''')
            if layout_bits:
                parts.append('레퍼런스 레이아웃 규칙: ' + ', '.join(layout_bits) + '.')
        return ' '.join(parts).strip()

    
    def _determine_style(self = None, scenario = None, reference_metadata = None):
        '''스타일 결정 (metadata 우선, 시나리오 폴백)'''
        pass
    # WARNING: Decompyle incomplete

    
    def _determine_subject_type(self = None, scenario = None):
        '''시나리오 기반 subject 타입 결정'''
        pass
    # WARNING: Decompyle incomplete

    
    def _build_style_directive(self = None, reference_metadata = None, reference_blueprint = None):
        '''
        metadata.json + blueprint에서 구체적인 스타일 지시서를 생성합니다.
        이것이 AI 이미지 생성의 핵심 스타일 가이드가 됩니다.
        '''
        reference_metadata = self._extract_reference_grammar_metadata(reference_metadata)
        if not reference_metadata:
            return ''
        parts = None
        if not reference_metadata.get('grammarHints', { }):
            grammar_hints = { }
            visual_style = reference_metadata.get('visualStyle', '')
            if visual_style:
                parts.append(f'''Visual style: {visual_style}''')
        grammar_summary = reference_metadata.get('grammarSummary', '')
        if grammar_summary:
            parts.append(f'''Grammar summary: {grammar_summary}''')
        text_style = reference_metadata.get('textStyle', { })
        if text_style:
            ts_parts = []
            lines = text_style.get('lines', 2)
            ts_parts.append(f'''{lines} lines of large bold text''')
            color_names = text_style.get('colorNames', '')
            highlight_colors = text_style.get('highlightColors', [])
            if color_names:
                ts_parts.append(f'''text colors: {color_names}''')
            elif highlight_colors:
                ts_parts.append(f'''highlight colors: {', '.join(highlight_colors)}''')
            color_rule = text_style.get('colorRule', '')
            if color_rule:
                ts_parts.append(f'''COLOR RULE: {color_rule}''')
            font_size = text_style.get('fontSize', '')
            if font_size:
                ts_parts.append(f'''font size: {font_size}''')
            font_weight = text_style.get('fontWeight', 'bold')
            ts_parts.append(f'''font weight: {font_weight}''')
            position = text_style.get('position', 'top-full-width')
            position_map = {
                'top-full-width': 'text spans full width at TOP of image',
                'bottom-full-width': 'text spans full width at BOTTOM of image',
                'left-vertical': 'text runs vertically on LEFT side',
                'top-and-bottom': 'text at both TOP and BOTTOM' }
            ts_parts.append(position_map.get(position, f'''text position: {position}'''))
            outline_color = text_style.get('outlineColor', '')
            has_outline = text_style.get('hasOutline', True)
            if outline_color:
                ts_parts.append(f'''text outline: {outline_color}''')
            elif has_outline:
                ts_parts.append('with dark outline/stroke for contrast')
            parts.append(f'''Text styling: {', '.join(ts_parts)}''')
        composition = reference_metadata.get('composition', '')
        if composition:
            parts.append(f'''Layout composition: {composition}''')
        if grammar_hints.get('subjectWeight'):
            parts.append(f'''Subject weight: {grammar_hints['subjectWeight']}''')
        if grammar_hints.get('layout'):
            parts.append(f'''Layout grammar: {grammar_hints['layout']}''')
        if grammar_hints.get('hookStructure'):
            parts.append(f'''Hook structure: {grammar_hints['hookStructure']}''')
        if grammar_hints.get('evidencePattern'):
            parts.append(f'''Visual evidence pattern: {grammar_hints['evidencePattern']}''')
        mood = reference_metadata.get('mood', '')
        if mood:
            parts.append(f'''Mood/atmosphere: {mood}''')
        style_prompt = reference_blueprint.get('stylePrompt', '')
        if style_prompt:
            cleaned = str(style_prompt).replace('{base_prompt}', '').strip()
            if cleaned:
                parts.append(f'''Style DNA: {cleaned}''')
        return ' | '.join(parts)

    
    def _build_floating_texts(self = None, scenario = None):
        '''시나리오 키워드 기반 플로팅 텍스트 생성'''
        emotion = scenario.get('emotion', '')
        if not emotion:
            return []
        emotion_badges = {
            '충격': {
                'text': None,
                'bg': '#FF0000',
                'color': '#FFFFFF' },
            '분노': {
                'text': '분노 폭발',
                'bg': '#FF4500',
                'color': '#FFFFFF' },
            '슬픔': {
                'text': '눈물 주의',
                'bg': '#4169E1',
                'color': '#FFFFFF' },
            '공포': {
                'text': '소름 주의',
                'bg': '#8B0000',
                'color': '#FFFFFF' },
            '감동': {
                'text': '감동 실화',
                'bg': '#FFD700',
                'color': '#000000' },
            '놀라움': {
                'text': '깜짝 반전',
                'bg': '#FF6347',
                'color': '#FFFFFF' } }
        badge_info = emotion_badges.get(emotion)
        if not badge_info:
            return []
        return [
            {
                'text': None['text'],
                'position': 'top-right',
                'backgroundColor': badge_info['bg'],
                'textColor': badge_info['color'],
                'style': 'bold',
                'size': 'small',
                'rotationDeg': -5,
                'purpose': 'supporting' }]

    
    def _extract_reference_grammar_metadata(self = None, reference_metadata = None):
