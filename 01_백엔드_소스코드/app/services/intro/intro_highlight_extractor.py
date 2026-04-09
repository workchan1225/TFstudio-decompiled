# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: intro_highlight_extractor.pyc (Python 3.11)

'''
Intro Highlight Extractor - AI 기반 하이라이트 장면 추출

대본에서 후킹력이 높은 장면 3개를 자동 추출합니다.
'''
import json
import logging
from typing import List, Optional
from intro_types import HighlightResult
logger = logging.getLogger(__name__)

class IntroHighlightExtractor:
    '''대본에서 후킹 포인트가 높은 장면을 AI로 추출'''
    EXTRACT_PROMPT = '당신은 YouTube 영상 전문가입니다.\n아래 대본의 장면 목록에서 시청자의 시선을 사로잡을 **후킹력이 가장 높은 장면 3개**를 추출하세요.\n\n후킹력 평가 기준:\n1. 감정적 충격 (반전, 갈등, 눈물)\n2. 호기심 유발 (질문, 의문, 미스터리)\n3. 시각적 임팩트 (액션, 극적 장면)\n4. 공감 (관계, 사랑, 가족)\n\n장면 목록:\n{scenes_text}\n\n반드시 아래 JSON 형식으로 응답하세요:\n```json\n[\n  {{\n    "sceneId": "ch0_sc0",\n    "hookScore": 95,\n    "reason": "추천 이유 (한국어, 1문장)",\n    "suggestedHookText": "이 장면에 어울리는 후킹 텍스트/질문 (한국어)"\n  }}\n]\n```\n상위 3개만 hookScore 내림차순으로 응답하세요.'
    
    def extract_highlights(self = None, scenes = None, api_key = None):
        """
        대본 장면 목록에서 하이라이트 3개 추출

        Args:
            scenes: [{ 'id': 'ch0_sc0', 'chapterIndex': 0, 'sceneIndex': 0, 'narrationText': '...' }]
            api_key: Google API 키 (없으면 Settings에서 조회)

        Returns:
            HighlightResult 목록 (최대 3개)
        """
        if not scenes:
            return []
        scenes_text = None._format_scenes(scenes)
        prompt = self.EXTRACT_PROMPT.format(scenes_text = scenes_text)
        
        try:
            GoogleProvider = GoogleProvider
            import app.services.ai.google_provider
            provider = GoogleProvider(api_key = api_key)
            response = provider.model.generate_content(prompt)
            text = response.text.strip()
            highlights_data = self._parse_response(text)
            results = []
            for item in highlights_data[:3]:
                scene_id = item.get('sceneId', '')
                source_scene = self._find_scene(scenes, scene_id)
                if not source_scene:
                    continue
                results.append(HighlightResult(scene_id = scene_id, chapter_index = source_scene.get('chapterIndex', 0), scene_index = source_scene.get('sceneIndex', 0), narration_text = source_scene.get('narrationText', ''), hook_score = item.get('hookScore', 50), reason = item.get('reason', ''), suggested_hook_text = item.get('suggestedHookText')))
                return sorted(results, key = (lambda x: x.hook_score), reverse = True)
                except Exception:
                    e = None
                    logger.error(f'''[IntroHighlightExtractor] 하이라이트 추출 실패: {e}''')
                    del e
                    return None
                    None = 
                    del e


    
    def _format_scenes(self = None, scenes = None):
        lines = []
        for s in scenes:
            scene_id = s.get('id', f'''ch{s.get('chapterIndex', 0)}_sc{s.get('sceneIndex', 0)}''')
            text = s.get('narrationText', '')[:200]
            lines.append(f'''[{scene_id}] {text}''')
            return '\n'.join(lines)

    
    def _parse_response(self = None, text = None):
        if '```json' in text:
            text = text.split('```json')[1].split('```')[0].strip()
        elif '```' in text:
            text = text.split('```')[1].split('```')[0].strip()
        
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            logger.warning(f'''[IntroHighlightExtractor] JSON 파싱 실패: {text[:200]}''')
            return 


    
    def _find_scene(self = None, scenes = None, scene_id = None):
        for s in scenes:
            sid = s.get('id', f'''ch{s.get('chapterIndex', 0)}_sc{s.get('sceneIndex', 0)}''')
            if sid == scene_id:
                
                return None, s
            return None
