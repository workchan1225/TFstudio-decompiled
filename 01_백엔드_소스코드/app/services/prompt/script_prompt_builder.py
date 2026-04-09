# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_prompt_builder.pyc (Python 3.11)

'''
ScriptPromptBuilder - 대본 생성 프롬프트 빌더

모든 제약 조건(Constraint)을 통합하여 최종 프롬프트를 생성.
장르, 톤, 비율, 캐릭터 등 설정값을 강제 적용.
'''
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from constraints import ToneEnforcer, RatioEnforcer, SchemaEnforcer, CharacterEnforcer, HumanTouchEnforcer, HumanTouchConfig
ScriptPromptConfig = <NODE:12>()

class ScriptPromptBuilder:
    '''
    대본 생성 프롬프트 빌더

    클린 아키텍처 원칙:
    - 제약 조건 시스템으로 설정값 강제 적용
    - 모듈화된 프롬프트 섹션 조합
    - 테스트 가능한 구조
    '''
    
    def __init__(self):
        self.tone_enforcer = ToneEnforcer()
        self.ratio_enforcer = RatioEnforcer()
        self.schema_enforcer = SchemaEnforcer()
        self.character_enforcer = CharacterEnforcer()
        self.human_touch_enforcer = HumanTouchEnforcer()

    
    def build_system_prompt(self = None, config = None):
        '''
        시스템 프롬프트 빌드

        구조:
        1. 역할 및 핵심 규칙
        2. 제약 조건 (톤, 비율, 스키마, 캐릭터)
        3. 장르 가이드 (외부에서 주입)
        4. 검증 체크리스트

        Args:
            config: 프롬프트 설정

        Returns:
            완성된 시스템 프롬프트
        '''
        parts = []
        parts.append(self._build_role_section(config))
        parts.append(self._build_constraints_section(config))
        if config.story_elements:
            parts.append(self._build_story_elements_section(config))
        parts.append(self._build_validation_section(config))
        return '\n\n'.join(filter(None, parts))

    
    def _build_role_section(self = None, config = None):
        '''역할 및 핵심 규칙 섹션'''
        content_desc = '유튜브 쇼츠' if config.content_format == 'shorts' else '유튜브 대본'
        return f'''# 당신은 전문 {content_desc} 작가입니다.\n\n다음 규칙을 따라 JSON 형식의 대본을 생성하세요.\n\n## 핵심 규칙\n\n1. **JSON만 출력**: 마크다운 코드블록(```) 없이 순수 JSON만\n2. **챕터 수**: 정확히 **{config.chapter_count}개**\n3. **총 분량**: 약 **{config.target_length}자**\n4. **언어**: {config.language}\n5. **톤/문체**: **{config.tone}** (어미 일관성 필수!)\n6. **나레이션 비율**: **{config.narration_ratio}%**\n\n---'''

    
    def _build_constraints_section(self = None, config = None):
        '''제약 조건 섹션 (강제 적용)'''
        sections = []
        sections.append('# [CONSTRAINTS] 강제 적용 규칙\n')
        sections.append(self.tone_enforcer.build_enforcement_prompt(config.tone))
        sections.append(self.ratio_enforcer.build_enforcement_prompt(narration_ratio = config.narration_ratio, chapter_count = config.chapter_count, speaker_tag_mode = config.speaker_tag_mode, target_length = config.target_length))
        sections.append(self.schema_enforcer.build_enforcement_prompt(chapter_count = config.chapter_count, include_characters = len(config.characters) > 0, include_title = True))
        if config.characters:
            sections.append(self.character_enforcer.build_enforcement_prompt(characters = config.characters, include_narrator = True, genre = config.genre))
        else:
            sections.append(self.character_enforcer.build_speaker_tag_rules())
        sections.append(self.character_enforcer.build_parenthetical_removal_rules())
        if config.human_touch:
            sections.append(self.human_touch_enforcer.build_enforcement_prompt(level = config.human_touch.level, personal_experience = config.human_touch.personal_experience, creator_opinion = config.human_touch.creator_opinion, educational_goal = config.human_touch.educational_goal, chapter_count = config.chapter_count))
        return '\n'.join(sections)

    
    def _build_story_elements_section(self = None, config = None):
        '''스토리 요소 강화 섹션'''
        if not config.story_elements:
            return ''
        element_descriptions = {
            'viral-hook': None,
            'cliffhanger': '다음 내용이 궁금해지는 긴장감 있는 엔딩',
            'emotional-rollercoaster': '감정의 기복이 큰 전개',
            'relatable-moments': '시청자가 공감할 수 있는 상황',
            'plot-twist': '예상치 못한 반전',
            'tension-buildup': '점진적으로 고조되는 긴장감',
            'memorable-character': '기억에 남는 인상적인 캐릭터',
            'unique-setting': '신선하고 독특한 배경 설정',
            'comment-bait': '댓글을 유도하는 논쟁적/공감 포인트',
            'share-worthy': '공유하고 싶은 감동/충격 요소',
            'satisfying-ending': '속 시원한 사이다 결말',
            'rewatchable': '다시 보고 싶은 복선/디테일' }
        elements = []
        for elem in config.story_elements:
            desc = element_descriptions.get(elem, elem)
            elements.append(f'''- **{elem}**: {desc}''')
            return f'''\n## [STORY ELEMENTS] 스토리 요소 강화\n\n선택된 요소를 대본에 반드시 포함하세요:\n\n{chr(10).join(elements)}\n\n### 적용 가이드\n\n각 요소를 자연스럽게 스토리에 녹여내세요.\n강제로 삽입하지 말고, 흐름에 맞게 배치하세요.\n'''

    
    def _build_validation_section(self = None, config = None):
        '''검증 체크리스트 섹션'''
        tone_config = self.tone_enforcer.get_config(config.tone)
        forbidden_sample = ', '.join(tone_config.forbidden_endings[:3]) if tone_config else '해당 없음'
        return f'''\n## [VALIDATION] 출력 전 검증 체크리스트\n\nJSON 출력 전 다음을 확인하세요:\n\n### 구조 검증\n- [ ] chapters 배열이 정확히 **{config.chapter_count}개**인가?\n- [ ] 모든 chapter에 title과 content가 있는가?\n- [ ] 마크다운 코드블록(```)을 사용하지 않았는가?\n\n### 톤 검증\n- [ ] 모든 나레이션이 **{config.tone}** 어미를 사용하는가?\n- [ ] 금지 어미 (~{forbidden_sample}...) 사용하지 않았는가?\n- [ ] 어미가 일관되게 유지되는가?\n\n### 비율 검증\n- [ ] 나레이션/대사 비율이 약 **{config.narration_ratio}:{100 - config.narration_ratio}**인가?\n\n### 캐릭터 검증\n- [ ] 허용되지 않은 화자 태그가 없는가?\n- [ ] 괄호 지문 (웃으며), (놀라며) 사용하지 않았는가?\n\n---\n⛔ 위 검증 항목 중 실패한 것이 있으면 해당 부분을 수정하세요.\n'''

    
    def build_user_prompt(self = None, config = None, genre_prompt = None, additional_instructions = ('', '')):
        '''
        사용자 프롬프트 빌드 (시놉시스 + 장르 + 추가 지침)

        Args:
            config: 프롬프트 설정
            genre_prompt: 장르별 프롬프트 (GenreRegistry에서 가져옴)
            additional_instructions: 추가 지침

        Returns:
            사용자 프롬프트
        '''
        parts = []
        if config.synopsis:
            parts.append(f'''## 시놉시스\n\n{config.synopsis}\n\n---''')
        if genre_prompt:
            parts.append(f'''## 장르 가이드\n\n{genre_prompt}\n\n---''')
        if config.characters:
            char_info = self._format_characters(config.characters)
            parts.append(f'''## 등장인물\n\n{char_info}\n\n---''')
        if additional_instructions:
            parts.append(f'''## 추가 지침\n\n{additional_instructions}\n\n---''')
        parts.append(f'''## 생성 요청\n\n위 시놉시스를 바탕으로 **{config.chapter_count}개 챕터**의 대본을 생성하세요.\n총 **{config.target_length}자** 분량, **{config.tone}** 문체로 작성하세요.\n\nJSON 형식으로 응답하세요. (마크다운 코드블록 없이!)\n''')
        return '\n\n'.join(parts)

    
    def _format_characters(self = None, characters = None):
        '''캐릭터 정보 포맷팅'''
        if not characters:
            return '등장인물 없음'
        lines = None
        for i, char in enumerate(characters, 1):
            name = char.get('name', f'''캐릭터{i}''')
            uid = char.get('uniqueId', chr(64 + i))
            appearance = char.get('appearance', '정보 없음')
            profile = char.get('profile', '')
            lines.append(f'''**{i}. {name}** (ID: {uid})''')
            lines.append(f'''   - 외모: {appearance}''')
            if profile:
                lines.append(f'''   - 역할: {profile}''')
            lines.append('')
            return '\n'.join(lines)

    
    def build_combined_prompt(self = None, config = None, genre_prompt = None, additional_instructions = ('', '')):
        '''
        시스템 + 사용자 프롬프트 통합 빌드

        Args:
            config: 프롬프트 설정
            genre_prompt: 장르별 프롬프트
            additional_instructions: 추가 지침

        Returns:
            통합 프롬프트
        '''
        system = self.build_system_prompt(config)
        user = self.build_user_prompt(config, genre_prompt, additional_instructions)
        return f'''{system}\n\n---\n\n{user}'''

    
    def validate_generated_content(self = None, content = None, config = None):
        '''
        생성된 콘텐츠 검증

        Args:
            content: 생성된 대본 텍스트
            config: 프롬프트 설정

        Returns:
            검증 결과 딕셔너리
        '''
        results = {
            'is_valid': True,
            'tone': None,
            'ratio': None,
            'characters': None,
            'human_touch': None,
            'overall_score': 1 }
        tone_result = self.tone_enforcer.validate_tone_consistency(content, config.tone)
        results['tone'] = tone_result
        if not tone_result['is_consistent']:
            results['is_valid'] = False
        ratio_result = self.ratio_enforcer.validate_ratio(content, config.narration_ratio)
        results['ratio'] = ratio_result
        if not ratio_result['is_valid']:
            results['is_valid'] = False
        if config.characters:
            allowed_speakers = config.characters()
            char_result = self.character_enforcer.validate_speakers(content, allowed_speakers)
            results['characters'] = char_result
            if not char_result['is_valid']:
                results['is_valid'] = False
        if config.human_touch:
            ht_result = self.human_touch_enforcer.validate_human_touch(content, config.human_touch.level)
            results['human_touch'] = ht_result
        scores = []
        if results['tone']:
            scores.append(results['tone'].get('score', 1))
        if results['ratio']:
            deviation = results['ratio'].get('deviation', 0)
            scores.append(max(0, 1 - deviation / 100))
        if results['characters']:
            violation_count = len(results['characters'].get('violations', []))
            scores.append(1 if violation_count == 0 else max(0, 1 - violation_count / 10))
        if results['human_touch']:
            scores.append(results['human_touch'].get('score', 100) / 100)
        results['overall_score'] = sum(scores) / len(scores) if scores else 1
        return results
