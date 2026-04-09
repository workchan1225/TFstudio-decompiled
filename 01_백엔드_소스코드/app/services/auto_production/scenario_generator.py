# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scenario_generator.pyc (Python 3.11)

'''
Auto Production - Scenario Generator (AI 기반 5가지 구성안 생성)
'''
import json
import logging
import re
from typing import Any, Dict, List
logger = logging.getLogger(__name__)
SCENARIO_STRATEGIES = [
    {
        'title': '정석 구성',
        'tone': '차분하고 체계적',
        'style': '교과서적이고 논리적인 전개' },
    {
        'title': '스토리텔링',
        'tone': '몰입감 있는',
        'style': '이야기 흐름으로 풀어나가는 구성' },
    {
        'title': 'Q&A 문답형',
        'tone': '궁금증 유발',
        'style': '질문과 답변으로 이어지는 구성' },
    {
        'title': '비교/대조',
        'tone': '분석적',
        'style': '대비와 비교를 통한 설명 구성' },
    {
        'title': '감성/공감형',
        'tone': '따뜻한',
        'style': '감정에 호소하며 공감을 이끄는 구성' }]

def generate_scenarios(scenes = None, genre = None, content_format = None):
    '''
    5가지 시나리오 구성안 생성
    Gemini AI를 활용하여 원본 씬을 기반으로 다양한 구성안 제안
    '''
    
    try:
        get_ai_service = get_ai_service
        import app.services.ai.provider_factory
        ai_service = get_ai_service('google')
        scene_texts = (lambda .0: pass# WARNING: Decompyle incomplete
)(enumerate(scenes)())
        prompt = _build_scenario_prompt(scene_texts, genre, content_format)
        response = ai_service.generate_text(prompt = prompt, max_tokens = 8000, response_mime_type = 'application/json')
        scenarios = _parse_scenario_response(response, scenes)
        return scenarios
    except Exception:
        e = None
        logger.error(f'''[ScenarioGenerator] AI generation failed: {e}''')
        del e
        return None
        None = 
        del e



def _build_scenario_prompt(scene_texts = None, genre = None, content_format = None):
    strategies_desc = (lambda .0: pass# WARNING: Decompyle incomplete
)(enumerate(SCENARIO_STRATEGIES)())
    return f'''다음 대본 씬들을 기반으로 5가지 다른 시나리오 구성안을 JSON으로 생성하세요.\n한 번의 응답으로 5개를 모두 반환해야 합니다.\n\n## 원본 씬:\n{scene_texts}\n\n## 장르: {genre}\n## 포맷: {content_format}\n\n## 5가지 구성 전략:\n{strategies_desc}\n\n## 출력 규칙:\n- 정확히 5개의 구성안을 반환하세요.\n- 각 구성안은 제목, 설명, 씬 목록을 포함하세요.\n- Step 2는 "구성 비교" 단계이므로 각 씬 텍스트는 1~2문장, 최대 110자 내외로 간결하게 작성하세요.\n- 원본 대본을 길게 반복하지 말고, 순서/강조점/도입 방식 차이를 중심으로 재구성하세요.\n- scenes는 원본과 비슷한 개수(권장 4~6개)를 유지하세요.\n- 불필요한 서문, 코드블록, 주석 없이 JSON만 반환하세요.\n\n## 출력 JSON 형식:\n{{\n  "scenarios": [\n    {{\n      "index": 0,\n      "title": "구성안 제목",\n      "description": "이 구성의 특징 설명 (1-2문장)",\n      "tone": "톤 한 단어",\n      "estimatedDuration": 150,\n      "scenes": [\n        {{"order": 1, "text": "씬 내용", "imageHint": "이미지 힌트"}}\n      ]\n    }}\n  ]\n}}\n\n각 구성안은 동일한 핵심 내용을 다른 순서, 강조점, 톤으로 재구성하세요.\n씬 수는 원본과 비슷하게 유지하되, 구성에 따라 병합이나 분리가 가능합니다.\n'''


def _extract_json(text = None):
