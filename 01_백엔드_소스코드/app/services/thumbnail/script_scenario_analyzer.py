# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_scenario_analyzer.pyc (Python 3.11)

'''
Script Scenario Analyzer
대본을 분석하여 썸네일용 시나리오(인물/상황/감정/텍스트)를 추천하는 서비스

기존 활용:
- build_situation_blueprint() (thumbnail_guard.py) - 위협/갈등 키워드 매칭
- Gemini API 호출 패턴 (GoogleProvider)
'''
import json
import logging
import os
import re
from typing import List, Dict, Any, Optional
from app.services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
logger = logging.getLogger(__name__)

class ScriptScenarioAnalyzer:
    '''대본 분석 → 썸네일 시나리오 추천'''
    
    def analyze_script_for_scenarios(self, script_content = None, project_title = None, genre = None, count = ('', '', 5, 'descriptive'), hook_style = ('script_content', str, 'project_title', str, 'genre', str, 'count', int, 'hook_style', str, 'return', List[Dict[(str, Any)]])):
        """
        대본을 분석하여 썸네일 시나리오를 추천합니다.

        Args:
            script_content: 대본 전체 텍스트
            project_title: 프로젝트 제목 (optional)
            genre: 장르 힌트 (optional)
            count: 추천할 시나리오 수
            hook_style: 'short' (단답형 ~10자) 또는 'descriptive' (설명형 ~20자)

        Returns:
            List[ThumbnailScenario] - 추천 시나리오 목록
        """
        excerpt = self._build_script_excerpt(script_content, max_chars = 5000)
        prompt = self._build_analysis_prompt(excerpt = excerpt, project_title = project_title, genre = genre, count = count, hook_style = hook_style)
        result = self._call_gemini(prompt)
        scenarios = self._parse_scenarios(result, count)
        if not scenarios:
            raise ValueError('Gemini 응답에서 시나리오를 파싱할 수 없습니다. 다시 시도해 주세요.')
        return scenarios

    
    def _build_script_excerpt(self = None, script_content = None, max_chars = None):
        '''대본을 축약하여 Gemini 입력용으로 최적화'''
        if len(script_content) <= max_chars:
            return script_content
        part_size = None // 5
        front = script_content[:part_size * 2]
        mid_start = len(script_content) // 2 - part_size // 2
        middle = script_content[mid_start:mid_start + part_size]
        back = script_content[-part_size:]
        return f'''{front}\n\n[... 중략 ...]\n\n{middle}\n\n[... 중략 ...]\n\n{back}'''

    
    def _build_analysis_prompt(self, excerpt = None, project_title = None, genre = None, count = ('descriptive',), hook_style = ('excerpt', str, 'project_title', str, 'genre', str, 'count', int, 'hook_style', str, 'return', str)):
        '''Gemini 분석 프롬프트 생성'''
        title_hint = f'''\n프로젝트 제목: "{project_title}"''' if project_title else ''
        genre_hint = f'''\n장르 힌트: {genre}''' if genre else ''
        if hook_style == 'short':
            hook_length_guide = '6-14자'
            hook_examples = '✅ 올바른 예시 (단답형 ~10자):\n- "전부 거짓이었다"  (8자)\n- "이거 실화야?!"  (8자)\n- "아버지 무너졌다"  (7자)\n- "진작 알았으면..."  (8자)\n- "소름 돋는 반전"  (7자)'
        else:
            hook_length_guide = '15-35자'
            hook_examples = '✅ 올바른 예시 (설명형 YouTube 스타일, 서사/스토리텔링 톤):\n- "세상에서 가장 믿었던 아들이... 날 버리고 도망갔다?!"  (26자)\n- "떠난 줄 알았던 아들이... 20년 만에 나타났다"  (22자)\n- "직원 무시하다 회사 날려먹은 사장... 실화입니다"  (24자)\n- "소액 투자했더니... 36년 후 10배가 됐다"  (20자)\n- "전문가들이 경고한 태풍... 결국 현실이 됐다"  (22자)\n\n핵심: 마침표(.) 대신 말줄임표(...), 물음표(?!), 감탄부호(!) 사용\n문장을 \'셋업... 펀치라인\' 2파트 구조로 작성\n뉴스 요약이 아닌 이야기꾼 톤으로 작성'
        return f'''당신은 유튜브 썸네일 시나리오 전문가입니다.\n아래 대본을 분석하여 가장 임팩트 있는 썸네일 시나리오 {count}개를 추천하세요.\n\n각 시나리오는 시청자의 클릭을 유도하는 강렬한 한 장면을 포착합니다.\n{title_hint}{genre_hint}\n\n=== 대본 ===\n{excerpt}\n=== 대본 끝 ===\n\n다음 JSON 형식으로 정확히 {count}개의 시나리오를 반환하세요:\n```json\n{{\n  "scenarios": [\n    {{\n      "scenarioId": "sc-1",\n      "keyPerson": "핵심 인물 설명 (예: 70대 아버지, 30대 직장인 여성)",\n      "situation": "시청자가 \'이거 봐야겠다\'고 느끼는 1-2줄 상황 설명. 구체적이고 드라마틱하게. ✅ 좋은 예: \'투자금 3억이 하루만에 사라졌다 — 전문가도 예측 못한 결과\' ❌ 나쁜 예: \'경제 위기에 대한 이야기\'",\n      "emotion": "핵심 감정 1단어 (예: 충격, 분노, 슬픔, 공포, 감동, 놀라움)",\n      "sceneDescriptionKo": "썸네일 이미지에 들어갈 장면 설명 (한국어, 2-3문장)",\n      "sceneDescriptionEn": "Thumbnail scene description in English for AI image generation (2-3 sentences, vivid and specific)",\n      "recommendedText": "{hook_length_guide} 훅 문장",\n      "visualKeywords": ["시각적 키워드 3-5개"],\n      "compositionHint": "구도 힌트 (예: 인물 클로즈업 + 텍스트 상단)",\n      "impactScore": 0.9,\n      "scriptQuote": "대본에서 이 시나리오의 근거가 되는 원문 인용 (1-2문장)"\n    }}\n  ]\n}}\n```\n\n=== recommendedText 작성 규칙 (매우 중요) ===\n\nrecommendedText는 유튜브 썸네일에 크게 들어가는 "훅 문장"입니다.\n반드시 {hook_length_guide} 범위로 작성하세요.\n\n{hook_examples}\n\n❌ 틀린 예시 (절대 금지):\n- "[챕터 1: 익숙한 경고, 낯선 위협]" → 대본 챕터 제목 그대로 복사 금지\n- "여러분, 여름의 문턱에서 우리는..." → 대본 내레이션 문장 복사 금지\n- "태풍의 메커니즘과 한반도 기후 변화에 대하여" → 설명문 복사 금지\n\n핵심 원칙:\n1. 대본 문장을 절대 그대로 복사하지 않는다\n2. {hook_length_guide} 범위의 서사/스토리텔링 톤 문장을 창작한다\n3. "셋업... 펀치라인" 2파트 구조 사용 (말줄임표 ... 로 연결)\n4. 질문형("~했다고?!"), 반전형("~인 줄 알았는데..."), 서사형("~이... ~했다") 중 택1\n5. 인물을 구체적으로 지칭한다 (아버지, 직원, 의사 등 - "주인공" 금지)\n6. 연도, 날짜, 기관명, 챕터 번호를 포함하지 않는다\n7. "~입니다", "~합니다" 같은 존댓말 종결어미 금지 (구어체/감탄체 사용)\n8. 마침표(.) 대신 말줄임표(...), 물음표(?!), 감탄부호(!) 사용\n\n기타 규칙:\n- impactScore는 클릭 유도력 기준 0.0-1.0 (가장 높은 것부터 정렬)\n- sceneDescriptionEn은 AI 이미지 생성용이므로 구체적이고 생생하게\n- 각 시나리오는 서로 다른 장면/감정을 다루어야 함\n\nJSON만 반환하세요.'''

    
    def _call_gemini(self = None, prompt = None):
        '''Gemini API 호출'''
        Settings = Settings
        import app.models.settings
        configure_legacy_genai = configure_legacy_genai
        import app.utils.google_sdk
        app_settings = Settings.get_or_create()
        google_api_key = get_google_api_key_or_runtime_token(settings = app_settings)
        if not google_api_key:
            raise ValueError(get_google_configuration_error_message(settings = app_settings))
        genai = configure_legacy_genai(google_api_key)
        model_chain = [
            ('gemini-2.5-pro', 90),
            ('gemini-2.5-flash', 60)]
        last_error = None
        for model_name, timeout_sec in model_chain:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt, request_options = {
                'timeout': timeout_sec }, generation_config = {
                'max_output_tokens': 8192,
                'temperature': 0.7 })
            
            return None, response.text.strip()
            except Exception:
                logger.warning(f'''[ScenarioAnalyzer] {model_name} failed: {e}''')
                e = None
                e = None
                del e
                continue
                e = None
                del e
            if not last_error:
                raise ValueError('All Gemini models failed')

    
    def _parse_scenarios(self = None, result_text = None, count = None):
        '''Gemini 응답 JSON 파싱 (잘린 JSON 복구 포함)'''
        cleaned = re.sub('^```(?:json)?\\s*', '', result_text, flags = re.IGNORECASE)
        cleaned = re.sub('\\s*```$', '', cleaned).strip()
        
        try:
            parsed = json.loads(cleaned)
        except json.JSONDecodeError:
            parsed = self._recover_truncated_json(cleaned)

        scenarios = parsed.get('scenarios', [])
        result = []
        for i, sc in enumerate(scenarios[:count]):
            sc.get('scenarioId', f'''sc-{i + 1}''')({
                'scenarioId': str(sc.get('keyPerson', '')).strip(),
                'keyPerson': str(sc.get('situation', '')).strip(),
                'situation': str(sc.get('emotion', '')).strip(),
                'emotion': str(sc.get('sceneDescriptionKo', '')).strip(),
                'sceneDescriptionKo': str(sc.get('sceneDescriptionEn', '')).strip(),
                'sceneDescriptionEn': str(sc.get('recommendedText', '')).strip()[:35],
                'recommendedText': (lambda .0: [ str(k) for k in .0 ]),
                'visualKeywords': sc.get('visualKeywords', [])()[:5],
                'compositionHint': str(sc.get('compositionHint', '')).strip(),
                'impactScore': min(1, max(0, float(sc.get('impactScore', 0.5)))),
                'scriptQuote': str(sc.get('scriptQuote', '')).strip()[:200] })
            result.sort(key = (lambda x: x['impactScore']), reverse = True)
            return result

    
    def _recover_truncated_json(self = None, text = None):
