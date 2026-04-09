# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: content_generator.pyc (Python 3.11)

'''
Content Generator

제목, 시놉시스, 기본 대본 생성 전문 모듈.
google_provider.py에서 분리.

v2.1: Google Search Grounding 기능 추가 (정보/교양 카테고리 할루시네이션 방지)
'''
import logging
import re
import time
from typing import List, Dict, Any, Optional
from app.utils.genre_prompt_enhancer import get_genre_specific_prompt_enhancement
logger = logging.getLogger(__name__)
from app.utils.content_type_enhancer import get_content_type_enhancement, get_content_type_structure_guide
from app.utils.script_genre_data import get_title_strategy, get_genre_data, get_hooking_data
from app.utils.creative_title_enhancer import build_creative_title_prompt, get_diversity_instruction
from app.utils.title_pattern_profile import build_title_style_instruction, get_aggressive_ratio, normalize_title_items, normalize_title_style_profile
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

class ContentGenerator:
    '''
    콘텐츠 생성기

    제목, 시놉시스, 기본 대본 생성 담당.
    '''
    
    def __init__(self, genai, model):
        '''
        초기화

        Args:
            genai: Google Generative AI 인스턴스
            model: 기본 Gemini 모델
        '''
        self.genai = genai
        self.model = model

    
    def _call_with_retry(self = None, model = None, prompt_text = None, max_retries = (1,)):
        '''Google API 호출 (500 에러 시 1회 재시도)'''
        last_error = None
        for attempt in range(max_retries + 1):
            response = model.generate_content(prompt_text)
            
            return None, response.text
            except Exception:
                e = None
                error_str = str(e)
                if '500' in error_str and attempt < max_retries:
                    logger.warning(f'''500 에러 발생, {attempt + 1}회 재시도 중...''')
                    time.sleep(2)
                    e = None
                    del e
                    continue
                raise last_error
                e = None
                del e
            raise last_error

    
    def _call_with_grounding(self = None, model = None, prompt_text = None, max_retries = (1,)):
        '''
        Google Search Grounding을 사용한 API 호출

        정보/교양/뉴스 카테고리에서 할루시네이션 방지를 위해
        웹 검색 결과를 기반으로 응답을 생성합니다.

        Args:
            model: Gemini 모델
            prompt_text: 프롬프트 텍스트
            max_retries: 최대 재시도 횟수

        Returns:
            생성된 텍스트 (grounding 메타데이터 포함 가능)
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
        return genre.upper() in INFORMATIONAL_GENRES

    
    def generate_topics(self = None, prompt = None, count = None, **kwargs):
        '''Generate video topic ideas using Gemini'''
        
        try:
            prompt_text = f'''당신은 유튜브 콘텐츠 전문가입니다.\n다음 주제에 대한 유튜브 영상 아이디어를 {count}개 제안해주세요: {prompt}\n\n각 아이디어는 한 줄로 작성하고, 번호를 매겨주세요.'''
            content = self._call_with_retry(self.model, prompt_text)
            topics = content.split('\n')()
            topics = topics()
            return topics[:count]
        except Exception:
            e = None
            logger.error(f'''generate_topics error: {e}''')
            del e
            return None
            None = 
            del e


    
    def generate_outline(self = None, topic = None, **kwargs):
        '''Generate script outline using Gemini'''
        
        try:
            prompt_text = f'''당신은 영상 기획 전문가입니다.\n다음 주제로 유튜브 영상 대본 개요를 작성해주세요.\n인트로, 본문, 아웃트로 구조로 작성하고, 각 섹션에서 다룰 내용을 상세히 설명해주세요:\n\n{topic}'''
            return self._call_with_retry(self.model, prompt_text)
        except Exception:
            e = None
            logger.error(f'''generate_outline error: {e}''')
            e = None
            del e
            return ''
            e = None
            del e


    
    def generate_script(self = None, outline = None, duration_minutes = None, **kwargs):
        '''Generate full video script using Gemini'''
        
        try:
            prompt_text = f'''당신은 전문 영상 작가입니다.\n다음 개요를 바탕으로 약 {duration_minutes}분 분량의 영상 대본을 작성해주세요.\n각 씬을 \'[씬 1]\', \'[씬 2]\' 형식으로 구분하고, 자연스러운 나레이션 형태로 작성하세요:\n\n{outline}'''
            return self._call_with_retry(self.model, prompt_text)
        except Exception:
            e = None
            logger.error(f'''generate_script error: {e}''')
            e = None
            del e
            return ''
            e = None
            del e


    TITLE_RESPONSE_SCHEMA = {
        'type': 'object',
        'properties': {
            'titles': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'title': {
                            'type': 'string' },
                        'description': {
                            'type': 'string' } },
                    'required': [
                        'title',
                        'description'] } } },
        'required': [
            'titles'] }
    
    def generate_titles(self, topic, genre, language, tone = None, count = None, content_type = None, subgenre = (10, None, None, None), model = ('topic', str, 'genre', str, 'language', str, 'tone', str, 'count', int, 'content_type', str, 'subgenre', str, 'model', str, 'return', List[Dict[(str, str)]]), **kwargs):
        '''Generate trending video titles (단일 호출, JSON 모드)'''
        import json
    # WARNING: Decompyle incomplete

    
    def generate_creative_titles(self, existing_titles, topic, genre = None, content_type = None, language = None, count = ('', '', None, '한국어', 10, None), model = ('existing_titles', list, 'topic', str, 'genre', str, 'content_type', str, 'language', str, 'count', int, 'model', str, 'return', List[Dict[(str, str)]]), **kwargs):
        '''Generate creative titles based on existing ones (단일 호출, JSON 모드)'''
        import json
        
        try:
            (title_style_profile, title_style_mix) = normalize_title_style_profile(kwargs.get('title_style_profile'), kwargs.get('title_style_mix'))
            title_style_instruction = build_title_style_instruction(title_style_profile, title_style_mix, context = 'script_titles', genre = genre)
            aggressive_ratio = get_aggressive_ratio(title_style_profile, title_style_mix)
            style_prompt_pack = self._build_style_prompt_pack(aggressive_ratio, count, genre = genre)
            style_rules = style_prompt_pack['distribution']
            style_lexicon_rules = style_prompt_pack['lexicon']
            style_self_check = style_prompt_pack['self_check']
            title_length_rule = style_prompt_pack['length_rule']
            style_power_terms = style_prompt_pack['power_terms']
            style_tone_examples = style_prompt_pack['tone_examples']
            is_shorts_context = self._is_shorts_title_context(content_type, topic, kwargs.get('content_format'))
            shorts_style_rules = self._build_shorts_title_rules(is_shorts_context, aggressive_ratio)
            if aggressive_ratio >= 70:
                temperature = 1.15 if is_shorts_context else 1.1
            elif aggressive_ratio <= 35:
                temperature = 0.7
            elif is_shorts_context:
                pass
            
            temperature = 0.85
            if is_shorts_context:
                max_output_tokens = 16384
            elif aggressive_ratio >= 70:
                max_output_tokens = 12288
            else:
                max_output_tokens = 8192
            existing_title_texts = self._normalize_existing_titles(existing_titles, limit = 10)
            existing_list = (lambda .0: [ f'''- {t}''' for t in .0 ])(existing_title_texts())
            if not existing_list:
                existing_list = '- (기존 제목 없음)'
            if aggressive_ratio >= 70:
                transform_strategy = '\n## 변형 전략 (자극형)\n1. 반전/정보 갭: 결론을 숨기고 궁금증 유발\n2. 감정 폭발: 분노, 배신, 복수 키워드 추가\n3. 대사 인용: 충격적인 대사 그대로 인용\n4. 긴박감: 시간 제한, 마지막 기회 프레임'
                hook_delta_rule = '기존 제목보다 후킹 강도를 확실히 높이고 열린 결말 구조를 유지합니다'
            elif aggressive_ratio <= 35:
                transform_strategy = '\n## 변형 전략 (균형형)\n1. 정보 가치 강조: 핵심 내용 명확히 전달\n2. 공감 요소 추가: 생활 밀착형 표현\n3. 신뢰 구축: 과장 최소화, 팩트 기반'
                hook_delta_rule = '과장 강화보다 정보 전달력/신뢰도를 우선하고 자극 표현은 최소화합니다'
            else:
                transform_strategy = '\n## 변형 전략 (혼합형)\n1. 후킹 + 신뢰: 호기심 유발하되 과장 절제\n2. 감정/공감: 몰입도 높이되 진정성 유지\n3. 정보/구조: 구체적 정보와 클릭 동기 균형'
                hook_delta_rule = '절반 정도는 후킹을 강화하고, 나머지는 정보/공감형으로 안정적으로 변형합니다'
            if not genre and content_type:
                prompt = []['기존 제목들을 기반으로 더 창의적인 제목 '][f'''{count}''']['개를 JSON으로 생성하세요.\n\n## 기존 제목\n'][f'''{existing_list}''']['\n\n## 컨텍스트\n장르: '][f'''{'일반'}''']['\n콘텐츠 타입: '][f'''{'일반'}''']['\n언어: '][f'''{language}''']['\n\n'][f'''{title_style_instruction}''']['\n\n## 스타일 배치 규칙 (반드시 충족)\n'][f'''{style_rules}''']['\n\n## 스타일별 어휘 가이드\n'][f'''{style_lexicon_rules}''']['\n\n## 강도 단어 규칙\n'][f'''{style_power_terms}''']['\n\n## 스타일 기준 예시 톤\n'][f'''{style_tone_examples}''']['\n\n'][f'''{shorts_style_rules}''']['\n\n## 생성 절차 (내부 점검 후 출력)\n'][f'''{style_self_check}''']['\n\n'][f'''{transform_strategy}''']['\n\n## 필수 규칙\n- 제목: '][f'''{title_length_rule}''']['\n- 설명: 50자 이내 (변형 의도 설명)\n- 동일 패턴/종결어 반복 금지\n- 같은 시작 단어 2회 이상 금지\n- '][f'''{hook_delta_rule}''']['\n- JSON의 titles 배열은 정확히 '][f'''{count}''']([]['기존 제목들을 기반으로 더 창의적인 제목 '][f'''{count}''']['개를 JSON으로 생성하세요.\n\n## 기존 제목\n'][f'''{existing_list}''']['\n\n## 컨텍스트\n장르: '][f'''{'일반'}''']['\n콘텐츠 타입: '][f'''{'일반'}''']['\n언어: '][f'''{language}''']['\n\n'][f'''{title_style_instruction}''']['\n\n## 스타일 배치 규칙 (반드시 충족)\n'][f'''{style_rules}''']['\n\n## 스타일별 어휘 가이드\n'][f'''{style_lexicon_rules}''']['\n\n## 강도 단어 규칙\n'][f'''{style_power_terms}''']['\n\n## 스타일 기준 예시 톤\n'][f'''{style_tone_examples}''']['\n\n'][f'''{shorts_style_rules}''']['\n\n## 생성 절차 (내부 점검 후 출력)\n'][f'''{style_self_check}''']['\n\n'][f'''{transform_strategy}''']['\n\n## 필수 규칙\n- 제목: '][f'''{title_length_rule}''']['\n- 설명: 50자 이내 (변형 의도 설명)\n- 동일 패턴/종결어 반복 금지\n- 같은 시작 단어 2회 이상 금지\n- '][f'''{hook_delta_rule}''']['\n- JSON의 titles 배열은 정확히 '][f'''{count}''']['개'])
                if not model:
                    gemini_model = self.genai.GenerativeModel('gemini-2.5-flash', generation_config = {
                        'temperature': temperature,
                        'max_output_tokens': max_output_tokens,
                        'response_mime_type': 'application/json',
                        'response_schema': self.TITLE_RESPONSE_SCHEMA })
                    response = gemini_model.generate_content(prompt)
                    if not response.text:
                        response_text = ''.strip()
                        if not response_text:
                            logger.warning('generate_creative_titles: Empty response from API')
                            return []
                        result = []['기존 제목들을 기반으로 더 창의적인 제목 '][f'''{count}''']['개를 JSON으로 생성하세요.\n\n## 기존 제목\n'][f'''{existing_list}''']['\n\n## 컨텍스트\n장르: '][f'''{'일반'}''']['\n콘텐츠 타입: '][f'''{'일반'}''']['\n언어: '][f'''{language}''']['\n\n'][f'''{title_style_instruction}''']['\n\n## 스타일 배치 규칙 (반드시 충족)\n'][f'''{style_rules}''']['\n\n## 스타일별 어휘 가이드\n'][f'''{style_lexicon_rules}''']['\n\n## 강도 단어 규칙\n'][f'''{style_power_terms}''']['\n\n## 스타일 기준 예시 톤\n'][f'''{style_tone_examples}''']['\n\n'][f'''{shorts_style_rules}''']['\n\n## 생성 절차 (내부 점검 후 출력)\n'][f'''{style_self_check}''']['\n\n'][f'''{transform_strategy}''']['\n\n## 필수 규칙\n- 제목: '][f'''{title_length_rule}''']['\n- 설명: 50자 이내 (변형 의도 설명)\n- 동일 패턴/종결어 반복 금지\n- 같은 시작 단어 2회 이상 금지\n- '][f'''{hook_delta_rule}''']['\n- JSON의 titles 배열은 정확히 '].loads(response_text)
                        titles = result.get('titles', [])
                        seen = set()
                        normalized = []
                        for item in titles:
                            title = str(item.get('title', '')).strip()
                            if len(title) < 4:
                                continue
                            key = re.sub('\\s+', '', title).lower()
                            if key in seen:
                                continue
                            seen.add(key)
                            normalized.append({
                                'title': title,
                                'description': str(item.get('description', ''))[:50] })
                            if len(normalized) >= count:
                                []['기존 제목들을 기반으로 더 창의적인 제목 '][f'''{count}''']['개를 JSON으로 생성하세요.\n\n## 기존 제목\n'][f'''{existing_list}''']['\n\n## 컨텍스트\n장르: '][f'''{'일반'}''']['\n콘텐츠 타입: '][f'''{'일반'}''']['\n언어: '][f'''{language}''']['\n\n'][f'''{title_style_instruction}''']['\n\n## 스타일 배치 규칙 (반드시 충족)\n'][f'''{style_rules}''']['\n\n## 스타일별 어휘 가이드\n'][f'''{style_lexicon_rules}''']['\n\n## 강도 단어 규칙\n'][f'''{style_power_terms}''']['\n\n## 스타일 기준 예시 톤\n'][f'''{style_tone_examples}''']['\n\n'][f'''{shorts_style_rules}''']['\n\n## 생성 절차 (내부 점검 후 출력)\n'][f'''{style_self_check}''']['\n\n'][f'''{transform_strategy}''']['\n\n## 필수 규칙\n- 제목: '][f'''{title_length_rule}''']['\n- 설명: 50자 이내 (변형 의도 설명)\n- 동일 패턴/종결어 반복 금지\n- 같은 시작 단어 2회 이상 금지\n- '][f'''{hook_delta_rule}''']
                            
                            return normalized
                            except Exception:
                                e = []['기존 제목들을 기반으로 더 창의적인 제목 '][f'''{count}''']['개를 JSON으로 생성하세요.\n\n## 기존 제목\n'][f'''{existing_list}''']['\n\n## 컨텍스트\n장르: '][f'''{'일반'}''']['\n콘텐츠 타입: '][f'''{'일반'}''']['\n언어: '][f'''{language}''']['\n\n'][f'''{title_style_instruction}''']['\n\n## 스타일 배치 규칙 (반드시 충족)\n'][f'''{style_rules}''']['\n\n## 스타일별 어휘 가이드\n'][f'''{style_lexicon_rules}''']['\n\n## 강도 단어 규칙\n'][f'''{style_power_terms}''']['\n\n## 스타일 기준 예시 톤\n'][f'''{style_tone_examples}''']['\n\n'][f'''{shorts_style_rules}''']['\n\n## 생성 절차 (내부 점검 후 출력)\n'][f'''{style_self_check}''']['\n\n'][f'''{transform_strategy}''']['\n\n## 필수 규칙\n- 제목: '][f'''{title_length_rule}''']
                                logger.error(f'''generate_creative_titles error: {e}''')
                                del e
                                return None
                                None = 
                                del e


    
    def generate_synopses(self, title, genre, language, tone, count = None, content_type = None, subgenre = None, model = (5, None, None, None, True), parallel = ('title', str, 'genre', str, 'language', str, 'tone', str, 'count', int, 'content_type', str, 'subgenre', str, 'model', str, 'parallel', bool, 'return', List[str]), **kwargs):
        '''Generate multiple synopses for selected title (병렬 생성 지원)'''
        ThreadPoolExecutor = ThreadPoolExecutor
        as_completed = as_completed
        import concurrent.futures
        
        try:
            if model:
                gemini_model = self.genai.GenerativeModel(model)
            else:
                gemini_model = self.model
            genre_enhancement = get_genre_specific_prompt_enhancement(genre = genre, step = 'synopsis', content_type = content_type, subgenre = subgenre)
            content_type_enhancement = get_content_type_enhancement(content_type = content_type, step = 'synopsis') if content_type else ''
            structure_guide = get_content_type_structure_guide(content_type) if content_type else None
            (specificity_requirements, format_example) = self._get_synopsis_specificity_requirements(content_type, structure_guide)
            genre_data = get_genre_data(genre)
            success_formula = genre_data.get('success_formula', { }) if genre_data else { }
            emotional_arc = success_formula.get('emotional_arc', '')
            if parallel and count > 1:
                return self._generate_synopses_parallel(gemini_model, title, genre, content_type, language, tone, count, content_type_enhancement, genre_enhancement, specificity_requirements, format_example, emotional_arc)
            prompt_text = None._build_synopsis_prompt(title, genre, content_type, language, tone, count, content_type_enhancement, genre_enhancement, specificity_requirements, format_example, emotional_arc)
            response = gemini_model.generate_content(prompt_text)
            content = response.text
            return self._parse_synopses(content, count)
        except Exception:
            e = None
            logger.error(f'''generate_synopses error: {e}''')
            del e
            return None
            None = 
            del e


    
    def _generate_synopses_parallel(self, gemini_model, title, genre, content_type, language, tone, count, content_type_enhancement, genre_enhancement = None, specificity_requirements = None, format_example = None, emotional_arc = ('title', str, 'genre', str, 'content_type', str, 'language', str, 'tone', str, 'count', int, 'content_type_enhancement', str, 'genre_enhancement', str, 'specificity_requirements', str, 'format_example', str, 'emotional_arc', str, 'return', List[str])):
        '''병렬로 시놉시스 생성 (각각 다른 접근 방식)'''
        pass
    # WARNING: Decompyle incomplete

    
    def expand_script(self, script = None, language = None, target_multiplier = None, focus_areas = (None,), model = ('script', str, 'language', str, 'target_multiplier', float, 'focus_areas', List[str], 'model', str, 'return', str), **kwargs):
        '''Expand script with more detail and length'''
        
        try:
            if model:
                gemini_model = self.genai.GenerativeModel(model)
            else:
                gemini_model = self.model
            focus_instructions = (lambda .0: [ f'''- {area}''' for area in .0 ])(focus_areas())
            prompt_text = f'''당신은 전문 영상 작가입니다. 다음 대본을 {target_multiplier}배로 확장해주세요.\n\n원본 대본:\n{script}\n\n확장 중점 사항:\n{focus_instructions}\n\n요구사항:\n- 원본의 서사 구조와 핵심 메시지 유지\n- 구체적인 예시와 설명 추가\n- 자연스러운 전환 문장 강화\n- 도입부와 마무리 더욱 풍부하게\n- {language}로 자연스럽게 작성\n- 단순 반복이 아닌 실질적인 내용 추가\n\n확장된 대본만 출력하고, 다른 설명은 추가하지 마세요.'''
            response = gemini_model.generate_content(prompt_text)
            return response.text
        except Exception:
            e = None
            logger.error(f'''expand_script error: {e}''')
            e = None
            del e
            return ''
            e = None
            del e


    
    def _is_shorts_title_context(self = None, content_type = None, topic = None, content_format = (None,)):
        '''쇼츠/숏폼 제목 생성 맥락인지 판별합니다.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _build_shorts_title_rules(self = None, is_shorts_context = None, aggressive_ratio = None):
        '''쇼츠 맥락에서 추가로 적용할 제목 규칙을 반환합니다.'''
        if not is_shorts_context:
            return ''
        if None >= 70:
            return '## 쇼츠 최적화 규칙\n- 첫 12자 이내에 강한 단어 또는 강한 갈등 단서를 배치\n- 가능한 한 군더더기 조사/부사를 줄여 짧고 단단하게 작성\n- 제목이 너무 설명형이면 질문형/대조형으로 재작성'
        if None <= 35:
            return '## 쇼츠 최적화 규칙\n- 첫 14자 안에서 주제/대상을 명확히 제시\n- 정보형 문장 구조를 유지하되 리듬감 있게 짧게 작성\n- 과장어보다 핵심 단어(대상/문제/방법)를 우선 배치'
        return '## 쇼츠 최적화 규칙\n- 초반 12~14자에서 후킹 단서와 정보 단서를 동시에 제시\n- 자극형과 정보형 제목이 번갈아 나오도록 배열\n- 동일 문장 패턴이 2회 이상 연속되지 않게 조정'

    
    def _build_style_prompt_pack(self = None, aggressive_ratio = None, count = None, genre = ('',)):
