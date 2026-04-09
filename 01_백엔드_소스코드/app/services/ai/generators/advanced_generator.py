# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: advanced_generator.pyc (Python 3.11)

'''
Advanced Generator

고급 대본 생성 기능 전문 모듈.
google_provider.py에서 분리.

v2.0: 장르별 확장 프롬프트 시스템 통합
- 드라마 장르: 6단계 서사 구조 기반 확장
- 정보 장르: 리텐션 훅 및 금지 표현 검출 기반 확장

v2.1: Google Search Grounding 통합
- 정보/교양/뉴스 카테고리: 웹 검색 기반 사실 확인으로 할루시네이션 방지
'''
import os
import re
import json
import time
import typing_extensions
from typing import Dict, Any, List, Optional
from constants import get_tone_instruction
INFORMATIONAL_GENRES = {
    'TECH',
    'SPACE',
    'HEALTH',
    'NATURE',
    'ECONOMY',
    'FINANCE',
    'SCIENCE',
    'POLITICS',
    'BIOGRAPHY',
    'ECONOMICS',
    'LIFE_TIPS',
    'PSYCHOLOGY',
    'DOCUMENTARY',
    'MONEY_SENSE',
    'NEWS_REPORT',
    'ENCYCLOPEDIA',
    'LIFE_CHOICES',
    'INFORMATIONAL',
    'SOCIAL_ISSUES',
    'KNOWLEDGE_BITE',
    'LIFE_KNOWLEDGE',
    'OFFICE_SURVIVAL',
    'RELATIONSHIP_EQ',
    'REVIEW_ANALYSIS',
    'NATURAL_DISASTER'}
DRAMA_GENRES = {
    'COMEDY',
    'HORROR',
    'HYBRID',
    'MUHYUP',
    'MYSTERY',
    'REVENGE',
    'DRAMATIC',
    'MUNCHKIN',
    'THRILLER',
    'TOUCHING',
    'CONFESSION',
    'CONSPIRACY',
    'HISTORICAL',
    'SF_FANTASY',
    'TRUE_STORY',
    'YOUTH_DRAMA',
    'HEARTWARMING',
    'LIFE_LESSONS',
    'LIFE_CHALLENGE',
    'NATIONAL_PRIDE',
    'JOSEON_FOLKTALE',
    'DISASTER_APOCALYPSE'}

try:
    from app.utils.script_genre_prompts import get_genre_expansion_prompt, get_genre_type, is_drama_genre, is_info_genre
    GENRE_PROMPT_AVAILABLE = True
except ImportError:
    GENRE_PROMPT_AVAILABLE = False
    print('[AdvancedGenerator] Warning: Genre prompt system not available')


try:
    from app.utils.drama_expansion_rules import build_expansion_guidelines, build_plot_beats_prompt, build_forbidden_list_prompt, get_chapter_plot_beat
    from app.utils.emotion_body_reactions import build_reaction_prompt, extract_used_reactions
    EXPANSION_RULES_AVAILABLE = True
    print('[AdvancedGenerator] v2.2: Drama expansion rules and emotion library loaded')
except ImportError:
    e = None
    EXPANSION_RULES_AVAILABLE = False
    print(f'''[AdvancedGenerator] Warning: Expansion rules not available: {e}''')
    e = None
    del e
except:
    e = None
    del e


class SubtitleItem(typing_extensions.TypedDict):
    text: str = 'SubtitleItem'


class AdvancedGenerator:
    '''
    고급 대본 생성기

    시놉시스 기반 확장, 자료 기반 생성, 타임스탬프 자막 생성 등 담당.
    '''
    
    def __init__(self = None, genai = None, model = None, audio_model_name = ('gemini-2.5-flash',)):
        '''
        초기화

        Args:
            genai: Google Generative AI 인스턴스
            model: 기본 Gemini 모델
            audio_model_name: 오디오 분석용 모델 이름
        '''
        self.genai = genai
        self.model = model
        self.audio_model_name = audio_model_name

    
    def _call_with_retry(self = None, model = None, prompt_text = None, generation_config = (None, 1), max_retries = ('prompt_text', str, 'max_retries', int)):
        '''Google API 호출 (500 에러 시 1회 재시도)'''
        last_error = None
        for attempt in range(max_retries + 1):
            if generation_config:
                response = model.generate_content(prompt_text, generation_config = generation_config)
            else:
                response = model.generate_content(prompt_text)
            
            return None, response
            except Exception:
                e = None
                error_str = str(e)
                if '500' in error_str and attempt < max_retries:
                    print(f'''[AdvancedGenerator] 500 에러 발생, {attempt + 1}회 재시도 중...''')
                    time.sleep(2)
                    e = None
                    del e
                    continue
                raise last_error
                e = None
                del e
            raise last_error

    
    def _call_with_grounding(self = None, model = None, prompt_text = None, generation_config = (None, 1), max_retries = ('prompt_text', str, 'max_retries', int)):
        '''
        Google Search Grounding을 사용한 API 호출

        정보/교양/뉴스 카테고리에서 할루시네이션 방지를 위해
        웹 검색 결과를 기반으로 응답을 생성합니다.

        Args:
            model: Gemini 모델
            prompt_text: 프롬프트 텍스트
            generation_config: 생성 설정
            max_retries: 최대 재시도 횟수

        Returns:
            생성된 응답 (grounding 메타데이터 포함 가능)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def should_use_grounding(self = None, genre = None):
        '''
        해당 장르에서 웹 검색 grounding을 사용해야 하는지 확인

        Args:
            genre: 장르 코드

        Returns:
            True면 grounding 사용, False면 일반 호출
        '''
        if not genre:
            return False
        return None.upper() in INFORMATIONAL_GENRES

    
    def get_genre_category(self = None, genre = None):
        """
        장르의 카테고리 반환

        Args:
            genre: 장르 코드

        Returns:
            'drama', 'info', 'review', 'news' 중 하나
        """
        if not genre:
            return 'drama'
        genre_upper = None.upper()
        if genre_upper in DRAMA_GENRES:
            return 'drama'
        if None in frozenset({'POLITICS', 'NEWS_REPORT', 'SOCIAL_ISSUES'}):
            return 'news'
        if None in frozenset({'REVIEW_ANALYSIS'}):
            return 'review'
        if None in INFORMATIONAL_GENRES:
            return 'info'

    
    def get_category_specific_expansion_rules(self = None, genre = None):
        '''
        카테고리별 확장 규칙 반환

        드라마/정보/뉴스/리뷰 카테고리에 맞는 확장 지침을 생성합니다.

        Args:
            genre: 장르 코드

        Returns:
            카테고리별 확장 규칙 문자열
        '''
        category = self.get_genre_category(genre)
        if category == 'drama':
            return '\n## ★★★ 드라마 카테고리 확장 규칙 (v2.0 고도화) ★★★\n\n### 절대 금지 사항 (도돌이표 현상 방지)\n\n1. **구간 통째 반복 금지**:\n   - 전문가 상담/조언 구간은 대본 전체에서 **1회만**\n   - 갈등/대면 구간은 **점층적으로 1~2회만**\n   - 해방/치유/결말 구간은 **마지막 챕터에만**\n   - ❌ 이미 상담 받은 후 다시 상담실로 돌아가는 묘사\n   - ❌ 이미 해결된 갈등을 다시 현재 진행형으로 묘사\n\n2. **서사 타임라인 보호**:\n   - 인물의 심리적 여정을 **선형적으로** 전개\n   - 무지/평화 → 갈등/고통 → 탐색/상담 → 결심/행동 → 해방/치유 → 성장/여운\n   - ❌ 이미 "해방 단계"에 진입한 인물을 다시 "고통 단계"로 묘사\n   - ❌ 같은 깨달음을 여러 챕터에서 반복\n\n3. **비유/은유 관리**:\n   - 핵심 비유(거미줄, 독 한 방울 등)는 대본 전체에서 **1회만** 사용\n   - 각 챕터는 **서로 다른 비유**로 감정을 전달\n   - 도입부 비유를 결말부에서 "회수"할 때만 재사용 허용\n\n### 서사 확장 원칙\n1. **감정 몰입 강화**: 캐릭터의 내면 독백, 신체 반응 상세 묘사\n2. **복선/반전 강화**: 작은 단서들을 대화와 묘사에 자연스럽게 심기\n3. **대화 비중 유지**: 나레이션 30-50%, 대사 50-70%\n4. **감각적 트리거**: 향기, 소리, 촉감 등 프루스트 현상 활용\n\n### 감정 묘사 규칙\n- ❌ 추상적: "슬펐다", "화가 났다", "절망했다"\n- ✅ 구체적: "손가락 끝이 하얗게 질릴 정도로 주먹을 쥐었다"\n- ✅ 감각적: "매일 밤 천장을 바라보며 잠 못 이루었다"\n- ❌ 같은 감정을 다른 단어로 반복 (절망 → 낙담 → 좌절)\n- ✅ 감정의 발전 (절망 → 분노 → 결심 → 행동)\n\n### 대화 확장 포인트\n- 캐릭터 성격이 드러나는 말투 유지\n- 갈등 장면에서 짧은 대사로 긴장감 고조\n- 화해/감동 장면에서 진심어린 대사 확장\n'
        if None == 'news':
            return '\n## ★★★ 뉴스/시사 카테고리 확장 규칙 ★★★\n\n### 객관성 강화\n1. **5W1H 명확화**: 누가, 무엇을, 언제, 어디서, 왜, 어떻게 구체화\n2. **역피라미드 구조**: 중요도 순으로 정보 배치\n3. **출처/근거 명시**: 통계, 전문가 의견 등 신뢰성 확보\n4. **양측 시각 제시**: 한쪽 편향 금지, 균형 잡힌 관점\n\n### 나레이션 비율\n- 나레이션 80-100%, 대사/인용 0-20%\n\n### 금지 사항\n- 감정적 서술, 주관적 의견 과다\n- 드라마틱한 갈등 구조, 복선/반전\n- "충격", "경악" 등 자극적 표현 과다 사용\n\n### 권장 구조\n1. 리드 (핵심 정보 먼저)\n2. 배경/맥락 설명\n3. 구체적 사례/데이터\n4. 전문가 의견/반응\n5. 향후 전망/시사점\n'
        if None == 'review':
            return '\n## ★★★ 리뷰/분석 카테고리 확장 규칙 ★★★\n\n### 분석 확장 원칙\n1. **평가 기준 명시**: 어떤 기준으로 평가하는지 먼저 제시\n2. **장단점 균형**: 장점만 또는 단점만 나열 금지\n3. **구체적 근거**: 추상적 평가 금지, 구체적 사례로 뒷받침\n4. **비교 분석**: 유사 대상과의 비교로 맥락 제공\n\n### 나레이션 비율\n- 나레이션 70-90%, 인용/대화 10-30%\n\n### 구조 가이드\n1. 개요/소개 (무엇을 리뷰하는지)\n2. 평가 기준 제시\n3. 장점 분석 (구체적 근거와 함께)\n4. 단점 분석 (공정하게)\n5. 비교 분석 (유사 대상과)\n6. 총평 및 추천 (누구에게 적합한지)\n\n### 금지 사항\n- "최고", "최악" 등 극단적 표현\n- 근거 없는 주관적 평가\n- 드라마틱한 서사 구조\n'

    
    def expand_script_from_synopsis(self, synopsis, current_script, language, target_length, focus_areas, model, chapter_count, chapter_target_length, chapter_info, genre = None, narration_ratio = None, speaker_tag_mode = None, tone = (None, 6, None, None, None, 50, 'with_tags', None, None), human_touch_settings = ('synopsis', str, 'current_script', str, 'language', str, 'target_length', int, 'focus_areas', list[str], 'model', str, 'chapter_count', int, 'chapter_target_length', int, 'chapter_info', list, 'genre', str, 'narration_ratio', int, 'speaker_tag_mode', str, 'tone', str, 'human_touch_settings', dict, 'return', dict), **kwargs):
        '''시놉시스를 기준으로 대본을 확장 생성 (JSON 구조화된 응답 반환)'''
        build_expansion_complete_style_prompt = build_expansion_complete_style_prompt
        SENTENCE_FLOW_GUIDE = SENTENCE_FLOW_GUIDE
        TONE_FORBIDDEN_ENDINGS = TONE_FORBIDDEN_ENDINGS
        TONE_REQUIRED_ENDINGS = TONE_REQUIRED_ENDINGS
        import app.utils.narration_style_guide
    # WARNING: Decompyle incomplete

    
    def _build_narration_ratio_instruction(self = None, speaker_tag_mode = None, narration_ratio = None, genre = (None,)):
        '''나레이션/대사 비율 지침 생성'''
        if speaker_tag_mode == 'without_tags':
            if genre and genre.upper() in INFORMATIONAL_GENRES:
                return '\n★★★★★ 객관적 해설 모드 (정보/교양/다큐) ★★★★★\n- 화자 태그([나레이션]:, [캐릭터명]:)를 사용하지 않습니다.\n- "우리"/"인류" 시점으로 작성합니다: "우리가 알고 있는...", "인류는...", "우리의 존재..."\n- 철학적 질문과 과학적 경이감 중심으로 서술합니다.\n\n❌ 개인 경험 표현 절대 금지:\n- "저는", "제가", "제 경험상", "개인적으로", "솔직히 저는" 사용 금지\n- "저도 예전에", "제가 느끼기에" 등 1인칭 경험담 형식 금지\n- "나는", "내가" 등 1인칭 시점 금지\n\n✅ 권장 표현:\n- "우리가 당연하게 여기던 것이 사실은..."\n- "인류는 이 충격적인 사실을 통해..."\n- "이것이 우리에게 던지는 질문은..."\n- "만약 이런 일이 실제로 일어난다면, 우리는..."\n'
            return None
        if None <= 10:
            return f'''\n★★★★★ 대사만 사용 (나레이션 {narration_ratio}% 이하) ★★★★★\n- [나레이션]: 태그 사용을 최소화하거나 금지합니다.\n- 거의 모든 내용을 캐릭터 대사([캐릭터이름]:)로 전달합니다.\n- 10줄 중 9줄 이상은 캐릭터 대사여야 합니다.\n'''
        if None < 30:
            return f'''\n★★★★★ 대사 중심 (나레이션 {narration_ratio}%, 대사 {100 - narration_ratio}%) ★★★★★\n- 대사가 압도적으로 많아야 합니다.\n- 나레이션은 꼭 필요한 장면 전환에만 1-2문장 사용합니다.\n- 10줄 중 7-8줄은 [캐릭터이름]: 태그여야 합니다.\n'''
        if None <= 50:
            return f'''\n★★★★★ 균형형 (나레이션 {narration_ratio}%, 대사 {100 - narration_ratio}%) ★★★★★\n- 나레이션과 대사를 비슷한 비율로 사용합니다.\n- 상황 묘사는 [나레이션]:, 캐릭터 감정/생각은 대사로 표현합니다.\n- [나레이션]:과 [캐릭터이름]:이 번갈아 나타납니다.\n'''
        if None <= 70:
            return f'''\n★★★★★ 나레이션 우세 (나레이션 {narration_ratio}%, 대사 {100 - narration_ratio}%) ★★★★★\n- 나레이션이 좀 더 많지만 대사도 적절히 사용합니다.\n- 스토리 설명은 [나레이션]:, 핵심 순간에는 대사를 삽입합니다.\n- 10줄 중 6-7줄은 [나레이션]: 태그입니다.\n'''
        if None < 90:
            return f'''\n★★★★★ 나레이션 중심 (나레이션 {narration_ratio}%, 대사 {100 - narration_ratio}%) ★★★★★\n- 나레이션이 주를 이룹니다.\n- 대사는 임팩트 있는 핵심 순간에만 1-2줄 사용합니다.\n- 대부분 [나레이션]: 태그로 서술합니다.\n'''
        return f'''{narration_ratio}%) ★★★★★\n- 모든 내용을 [나레이션]: 태그로만 작성합니다.\n- 캐릭터 대사 태그([캐릭터명]:)를 거의 사용하지 않습니다.\n- 다큐멘터리/소설 낭독 스타일로 전개합니다.\n'''

    INTRO_TRANSITION_PATTERNS = [
        '모든\\s*것은.*돌아간다',
        '모든\\s*것은.*시작',
        '이야기는.*시작',
        '어떻게\\s*이런',
        '1년\\s*전',
        '며칠\\s*전',
        '몇\\s*주\\s*전',
        '몇\\s*달\\s*전',
        '몇\\s*년\\s*전',
        '그\\s*시작은',
        '시간을.*되돌려',
        '처음부터.*시작',
        '이\\s*모든\\s*것의\\s*시작',
        '그날의\\s*오해',
        '사건의\\s*발단',
        '이\\s*사건.*시작']
    
    def _extract_intro_section(self = None, chapter_content = None):
        '''
        첫 챕터에서 인트로(티저) 섹션을 추출

        In Medias Res 구조:
        - 티저 부분: 첫 부분 (클라이맥스/충격 장면)
        - 전환 문구: "모든 것은 ~ 돌아간다" 등
        - 본편: 나머지

        Args:
            chapter_content: 첫 챕터 내용

        Returns:
            (intro_section, remaining_content) 또는 (None, chapter_content)
        '''
        if not chapter_content:
            return (None, chapter_content)
    # WARNING: Decompyle incomplete

    
    def _get_first_chapter_content(self = None, script_text = None, chapter_info = None):
        '''
        대본에서 첫 챕터 내용만 추출

        Args:
            script_text: 전체 대본 텍스트
            chapter_info: 챕터 정보 목록 (선택)

        Returns:
            첫 챕터 내용
        '''
        if not script_text:
            return ''
        chapter_pattern = None
        parts = re.split(chapter_pattern, script_text)
        if len(parts) >= 2:
            return parts[1].strip() if len(parts[1].strip()) > 0 else parts[0].strip()
        return None.strip()

    
    def _restore_intro(self = None, original_intro = None, expanded_content = None):
        '''
        확장된 첫 챕터에 원본 인트로를 강제 복원

        전략:
        1. 확장된 내용에서 AI가 생성한 인트로 부분 제거
        2. 원본 인트로를 앞에 추가
        3. 나머지 확장된 내용 유지

        Args:
            original_intro: 원본 인트로 (전환 문구 포함)
            expanded_content: 확장된 첫 챕터 내용

        Returns:
            인트로가 복원된 첫 챕터 내용
        '''
        if not original_intro:
            print('[IntroPreservation] 원본 인트로 없음 - 복원 건너뜀')
            return expanded_content
        if not None:
            print('[IntroPreservation] 확장된 내용 없음 - 원본 인트로만 반환')
            return original_intro
        None(f'''[IntroPreservation] 원본 인트로 길이: {len(original_intro)}자''')
        print(f'''[IntroPreservation] 확장된 내용 길이: {len(expanded_content)}자''')
    # WARNING: Decompyle incomplete

    
    def _build_intro_preservation_prompt(self = None, intro_section = None):
        '''
        인트로 보존 지시 프롬프트 생성

        Args:
            intro_section: 보존할 인트로 섹션

        Returns:
            인트로 보존 지시 프롬프트
        '''
        if not intro_section:
            return ''
        return f'''{intro_section}\n---인트로 끝---\n\n⚠️ 위 인트로의 대사, 나레이션, 전환 문구를 절대 변경하지 마세요!\n'''

    
    def _build_expansion_prompt(self, synopsis, current_script, chapter_structure, chapter_titles, chapter_count, chapter_target_length, target_length, focus_instructions, genre_expansion_prompt, narration_ratio_instruction, character_list_str, first_speaker, speaker_examples, drama_style_guide, effective_tone, TONE_REQUIRED_ENDINGS = None, TONE_FORBIDDEN_ENDINGS = None, human_touch_settings = None, genre = (None, None, 'with_tags'), speaker_tag_mode = ('synopsis', str, 'current_script', str, 'chapter_structure', str, 'chapter_titles', list, 'chapter_count', int, 'chapter_target_length', int, 'target_length', int, 'focus_instructions', str, 'genre_expansion_prompt', str, 'narration_ratio_instruction', str, 'character_list_str', str, 'first_speaker', str, 'speaker_examples', str, 'drama_style_guide', str, 'effective_tone', str, 'TONE_REQUIRED_ENDINGS', dict, 'TONE_FORBIDDEN_ENDINGS', dict, 'human_touch_settings', dict, 'genre', str, 'speaker_tag_mode', str, 'return', str)):
        '''확장 프롬프트 빌드'''
        pass
    # WARNING: Decompyle incomplete

    
    def generate_timestamped_transcript(self = None, audio_path = None, language = None, offset_ms = ('ko', 0)):
        '''
        Gemini 2.0 Flash Exp를 사용하여 오디오에서 고정밀 싱크 자막 생성

        Args:
            audio_path: 오디오 파일 경로
            language: 언어 코드 (기본값: "ko")
            offset_ms: 타임스탬프 오프셋 (밀리초 단위, 음수면 앞당김)

        Returns:
            [{\'start\': float, \'end\': float, \'text\': str}, ...]
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def generate_script_from_research(self, research_content, content_format, genre = None, speaker_mode = None, shorts_length = None, tone = ('longform', 'INFORMATIONAL', 'with_tags', '2min', '설명체', None), model = ('research_content', str, 'content_format', str, 'genre', str, 'speaker_mode', str, 'shorts_length', str, 'tone', str, 'model', str, 'return', dict), **kwargs):
        """
        자료 조사 내용을 기반으로 대본 생성 (할루시네이션 최소화)

        Args:
            research_content: 사용자가 제공한 자료 조사 내용
            content_format: 'longform' | 'shorts'
            genre: 장르 코드
            speaker_mode: 'with_tags' | 'without_tags'
            shorts_length: 쇼츠 길이 ('1min' | '2min' | '3min')
            tone: 톤/문체
            model: 사용할 Gemini 모델 (None이면 기본 모델)

        Returns:
            {
                'success': bool,
                'script': str,
                'chapters': list,
                'title': str,
                'extracted_topics': list,
                'metadata': dict
            }
        """
        
        try:
            create_research_script_system_prompt = create_research_script_system_prompt
            create_research_script_user_prompt = create_research_script_user_prompt
            preprocess_research_content = preprocess_research_content
            import app.utils.research_script_prompts
            if model:
                gemini_model = self.genai.GenerativeModel(model)
            else:
                gemini_model = self.model
            content_info = preprocess_research_content(research_content)
            if content_format == 'shorts':
                shorts_config = {
                    '1min': {
                        'target_length': 420,
                        'chapter_count': 1,
                        'narration_ratio': 80 },
                    '2min': {
                        'target_length': 840,
                        'chapter_count': 1,
                        'narration_ratio': 75 },
                    '3min': {
                        'target_length': 1260,
                        'chapter_count': 2,
                        'narration_ratio': 70 } }
                config = shorts_config.get(shorts_length, shorts_config['2min'])
                target_length = config['target_length']
                chapter_count = config['chapter_count']
                narration_ratio = config['narration_ratio']
            else:
                word_count = content_info['word_count']
                if word_count < 500:
                    target_length = 2000
                    chapter_count = 3
                elif word_count < 1500:
                    target_length = 4000
                    chapter_count = 5
                else:
                    target_length = 6000
                    chapter_count = 6
                narration_ratio = 70
            system_prompt = create_research_script_system_prompt(content_format = content_format, genre = genre, speaker_mode = speaker_mode, shorts_length = shorts_length, tone = tone, chapter_count = chapter_count, target_length = target_length, narration_ratio = narration_ratio)
            user_prompt = create_research_script_user_prompt(research_content = research_content, additional_instructions = kwargs.get('additional_instructions'))
            estimated_output_tokens = int(target_length * 0.5) + 1000
            max_output_tokens = max(50000, min(65536, estimated_output_tokens))
            print(f'''[AdvancedGenerator] Generating script from research ({content_format}, {genre})''')
            print(f'''[AdvancedGenerator] Research content: {content_info['word_count']} chars, {len(content_info['sections'])} sections''')
            print(f'''[AdvancedGenerator] max_output_tokens: {max_output_tokens}''')
            response = gemini_model.generate_content([
                system_prompt,
                user_prompt], generation_config = {
                'temperature': 0.7,
                'top_p': 0.9,
                'max_output_tokens': max_output_tokens })
            response_text = response.text.strip()
            if response_text.startswith('```'):
                response_text = re.sub('^```\\w*\\n?', '', response_text)
                response_text = re.sub('\\n?```$', '', response_text)
            
            try:
                result = json.loads(response_text)
                
                try:
                    pass
                except json.JSONDecodeError:
                    e = None
                    print(f'''[AdvancedGenerator] JSON parse error: {e}''')
                    json_match = re.search('\\{[\\s\\S]*\\}', response_text)
                    if json_match:
                        result = json.loads(json_match.group())
                    else:
                        raise ValueError(f'''Invalid JSON response: {response_text[:500]}''')
                    
                    try:
                        e = None
                        del e
                    e = None
                    del e
                    try:
                        title = result.get('title', '자료 기반 대본')
                        chapters = result.get('chapters', [])
                        extracted_topics = result.get('extracted_topics', [])
                        script_parts = []
                        for i, chapter in enumerate(chapters):
                            chapter_title = chapter.get('title', f'''파트 {i + 1}''')
                            chapter_content = chapter.get('content', '')
                            script_parts.append(f'''### {chapter_title}\n\n{chapter_content}''')
                            full_script = '\n\n'.join(script_parts)
                            enriched_chapters = []
                            for chapter in chapters:
                                content = chapter.get('content', '')
                                enriched_chapters.append({
                                    'title': chapter.get('title', ''),
                                    'content': content,
                                    'characterCount': len(content),
                                    'estimatedTime': round(len(content) / 200, 1),
                                    'speakers': self._extract_speakers_from_script(content) })
                                return {
                                    'success': True,
                                    'script': full_script,
                                    'title': title,
                                    'chapters': enriched_chapters,
                                    'extracted_topics': extracted_topics,
                                    'metadata': {
                                        'source_word_count': content_info['word_count'],
                                        'source_sections': len(content_info['sections']),
                                        'content_format': content_format,
                                        'genre': genre,
                                        'generation_mode': 'research' } }
                                except Exception:
                                    e = None
                                    print(f'''[AdvancedGenerator] Error in generate_script_from_research: {e}''')
                                    import traceback
                                    traceback.print_exc()
                                    del e
                                    return None
                                    None = 
                                    del e





    
    def _extract_speakers_from_script(self = None, script = None):
        '''대본에서 화자 이름 추출'''
        if not script:
            return []
        speaker_pattern = None
        speakers = set()
        for line in script.split('\n'):
            match = re.match(speaker_pattern, line.strip())
            if match:
                speaker = match.group(1)
                if speaker.startswith('[') and speaker.endswith(']'):
                    speaker = speaker[1:-1]
                if speaker.lower() not in ('chapters', 'title', 'content', 'script', 'format'):
                    speakers.add(speaker)
            return list(speakers)

    
    def _extract_speaker_examples(self = None, script = None, speakers = None):
        '''각 화자별 대사 예시 추출 (최대 2개씩)'''
        if not script or speakers:
            return ''
        examples = None
        for speaker in speakers:
            pattern = f'''^\\[?{re.escape(speaker)}\\]?:\\s*(.+)$'''
            matches = re.findall(pattern, script, re.MULTILINE)
            if matches:
                sample_dialogues = matches[:2]
                for dialogue in sample_dialogues:
                    if len(dialogue) > 50:
                        dialogue = dialogue[:50] + '...'
                    examples.append(f'''{speaker}: {dialogue}''')
                    if examples:
                        return '\n'.join(examples)
                    return None

    
    def _parse_timestamp_to_seconds(self = None, timestamp = None):
        '''HH:MM:SS,mmm 또는 HH:MM:SS.mmm 포맷을 초(float)로 변환'''
        
        try:
            timestamp = timestamp.replace('.', ',')
            parts = timestamp.split(',')
            time_parts = parts[0].split(':')
            s = int(time_parts[2])
            m = int(time_parts[1])
            h = int(time_parts[0])
            ms = int(parts[1]) if len(parts) > 1 else 0
            return h * 3600 + m * 60 + s + ms / 1000
        except Exception:
            return 0


    
    def _remove_parenthetical_directions(self = None, content = None):
        '''괄호 지문 및 부연설명 괄호 제거 (확장된 패턴)'''
        long_stage_direction_patterns = [
            '\\([가-힣A-Za-z0-9\\s,\\.·、~\\-]{10,100}(?:했다|쳤다|났다|갔다|왔다|섰다|앉았다|말했다|외쳤다|물었다|대답했다|중얼거렸다|속삭였다|소리쳤다)\\)\\s*',
            '\\([가-힣A-Za-z0-9\\s,\\.·、~\\-]{10,100}(?:으며|하며|면서|하면서)\\)\\s*',
            '\\([가-힣A-Za-z0-9\\s,\\.·、~\\-]{10,100}(?:하고|라고|며고)\\)\\s*',
            '^\\s*\\([가-힣A-Za-z0-9\\s,\\.·、~\\-]{15,150}\\)\\s*']
        for pattern in long_stage_direction_patterns:
            content = re.sub(pattern, '', content, flags = re.MULTILINE)
            stage_direction_patterns = [
                '\\((?:혼잣말로|속으로|조용히|천천히|급히|빠르게|느리게|작게|크게|낮게|높게|부드럽게|단호하게|차갑게|따뜻하게)\\)',
                '\\([가-힣\\s]{1,15}(?:표정으로|목소리로|눈으로|얼굴로|어조로|말투로|투로)\\)',
                '\\([가-힣\\s]{1,30}(?:으며|며|면서|하며|하면서)\\)',
                '\\([가-힣\\s]{1,20}고\\)',
                '\\((?:한숨|웃음|침묵|기침|신음|미소|눈물|탄식|고개를 끄덕이며|고개를 저으며)\\)',
                '\\((?:잠시 후|잠시|잠깐|사이|beat|pause)\\)',
                '\\((?:softly|loudly|whispers|shouts|sighs|laughs|cries|smiles|nods|shakes head)\\)',
                '\\([가-힣]{1,6}(?:하며|하고|하면서|으며|며)\\)',
                '\\((?:웃으며|놀라며|화내며|슬퍼하며|기뻐하며|걱정하며|당황하며|긴장하며)\\)']
            for pattern in stage_direction_patterns:
                content = re.sub(pattern, '', content, flags = re.IGNORECASE)
                action_keywords = '(?:앉아|서서|일어나|걸어|뛰어|눕|들며|내려|올려|닦으며|고쳐|바라보며|돌아보며|쳐다보며|향해|소리|목소리로|외쳤다|말했다|중얼|속삭)'
                content = re.sub(f'''\\([가-힣A-Za-z0-9\\s,\\.·、~\\-]*{action_keywords}[가-힣A-Za-z0-9\\s,\\.·、~\\-]*\\)\\s*''', '', content)
                english_bracket_patterns = [
                    '([가-힣]+)\\s*\\([A-Za-z][A-Za-z\\s\\-\\.,\\\'\\"0-9]*\\)',
                    '([가-힣]+)\\s*\\([A-Z][A-Z\\.]{0,10}\\)',
                    '([가-힣]+)\\s*\\([A-Z][a-zA-Z\\s\\-\\.,\\\'\\"0-9]{2,50}\\)']
                for pattern in english_bracket_patterns:
                    content = re.sub(pattern, '\\1', content)
                    content = re.sub('([가-힣]+\\s*(?:단어|감정|요소|방법|것들|사항|내용|종류|유형))\\s*\\([가-힣\\s,、·]+\\)', '\\1', content)
                    content = re.sub('\\(([가-힣\\s]{1,10})\\)', (lambda m: '' if not (lambda .0: pass# WARNING: Decompyle incomplete
)(m.group(1)()) else m.group(0)
), content)
                    content = re.sub('([가-힣]+)\\s*\\((약?\\s*[\\d,\\.]+\\s*[가-힣%]+(?:\\s+[가-힣]+)?)\\)', '\\1 \\2', content)
                    content = re.sub('  +', ' ', content)
                    content = re.sub('\\n\\s*\\n\\s*\\n', '\n\n', content)
                    return content

    
    def _normalize_chapter_title(self = None, title = None, original_title = None):
