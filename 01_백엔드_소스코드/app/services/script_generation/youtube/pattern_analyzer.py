# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pattern_analyzer.pyc (Python 3.11)

'''
YouTube Script Pattern Analyzer

YouTube 대본의 구조적/심리학적 패턴을 분석하는 서비스
'''
import json
import re
import logging
from typing import Dict, Any
from datetime import datetime
from types import YouTubeReferenceAnalysis, AnalyzePatternResult, DetectedTone
from reference_blueprint import build_reference_blueprint
logger = logging.getLogger(__name__)

class PatternAnalyzer:
    '''
    대본 패턴 분석기

    YouTube 자막에서 구조적 패턴, 심리학적 패턴,
    기승전결 구조를 분석합니다.
    '''
    
    def __init__(self = None, genai = None, model = None):
        '''
        Args:
            genai: Google Generative AI 인스턴스
            model: Gemini 모델 인스턴스
        '''
        self.genai = genai
        self.model = model

    
    def analyze(self = None, transcript = None, video_info = None):
        '''
        대본 패턴 종합 분석

        구조적 패턴, 심리학적 패턴, 기승전결을 분석하여
        레퍼런스 대본 생성에 활용할 수 있는 형태로 반환합니다.

        Args:
            transcript: 자막 전문
            video_info: 영상 정보 (videoId, title, duration 등)

        Returns:
            AnalyzePatternResult: 분석 결과
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _build_analysis_prompt(self = None, transcript = None, video_info = None):
        '''분석 프롬프트 생성'''
        max_transcript_length = 15000
        if len(transcript) > max_transcript_length:
            half = max_transcript_length // 2
            transcript_for_analysis = transcript[:half] + '\n\n... (중간 생략) ...\n\n' + transcript[-half:]
        else:
            transcript_for_analysis = transcript
        return f'''당신은 유튜브 콘텐츠 분석 전문가이자 영상 기획 컨설턴트입니다.\n\n다음 유튜브 영상의 자막을 분석하여 대본 패턴과 성공 요인을 추출해주세요.\n\n## 영상 정보\n- 제목: {video_info.get('title', '알 수 없음')}\n- 길이: {video_info.get('duration', 0):.0f}초 ({video_info.get('duration', 0) / 60:.1f}분)\n\n## 자막 내용\n{transcript_for_analysis}\n\n## 분석 요청\n\n다음 JSON 형식으로 분석 결과를 출력해주세요.\n반드시 유효한 JSON 형식이어야 합니다.\n\n```json\n{{\n  "structuralPattern": {{\n    "introduction": {{\n      "ratio": 15,\n      "summary": "도입부 요약 (1-2문장)",\n      "hooks": ["후킹 요소 1", "후킹 요소 2", "후킹 요소 3"]\n    }},\n    "development": {{\n      "ratio": 50,\n      "mainPoints": ["핵심 포인트 1", "핵심 포인트 2", "핵심 포인트 3"],\n      "transitions": ["전환 문구 1", "전환 문구 2"]\n    }},\n    "climax": {{\n      "ratio": 20,\n      "peakMoment": "클라이맥스 순간 설명",\n      "tensionBuilders": ["긴장감 요소 1", "긴장감 요소 2"]\n    }},\n    "conclusion": {{\n      "ratio": 15,\n      "callToAction": "CTA 내용 (있는 경우)",\n      "closingHooks": ["마무리 후킹 1", "마무리 후킹 2"]\n    }}\n  }},\n  "psychologicalPattern": {{\n    "curiosityTriggers": ["호기심 유발 요소 1", "호기심 유발 요소 2", "호기심 유발 요소 3"],\n    "emotionalBeats": [\n      {{"emotion": "surprise", "trigger": "트리거 설명", "intensity": 8}},\n      {{"emotion": "curiosity", "trigger": "트리거 설명", "intensity": 7}}\n    ],\n    "retentionHooks": [\n      {{"type": "question", "content": "훅 내용"}},\n      {{"type": "promise", "content": "훅 내용"}},\n      {{"type": "tease", "content": "훅 내용"}}\n    ]\n  }},\n  "narrativeStructure": {{\n    "ki": {{"content": "기 내용 요약", "purpose": "도입 목적"}},\n    "seung": {{"content": "승 내용 요약", "development": "전개 방식"}},\n    "jeon": {{"content": "전 내용 요약", "twist": "반전/전환 포인트"}},\n    "gyeol": {{"content": "결 내용 요약", "resolution": "해결/마무리 방식"}}\n  }},\n  "keyPoints": [\n    {{"content": "핵심 포인트 1", "importance": "high", "category": "fact"}},\n    {{"content": "핵심 포인트 2", "importance": "medium", "category": "opinion"}},\n    {{"content": "핵심 포인트 3", "importance": "medium", "category": "example"}}\n  ],\n  "detectedTone": {{\n    "primary": "주요 톤/문체 (예: 소설체, 강연체, 대화체, 다큐체, 예능체)",\n    "secondary": "부가 톤 (선택, 예: 미스터리)",\n    "formality": "formal 또는 casual 또는 mixed",\n    "emotion": "neutral 또는 dramatic 또는 informative 또는 humorous",\n    "description": "이 대본의 톤/문체에 대한 한 줄 설명"\n  }},\n  "retentionAnalysis": {{\n    "dropOffRisks": [\n      {{"position": "20%", "reason": "이탈 위험 요인", "severity": "medium"}},\n      {{"position": "60%", "reason": "이탈 위험 요인", "severity": "low"}}\n    ],\n    "engagementPeaks": [\n      {{"position": "5%", "reason": "몰입 피크 요인", "intensity": 9}},\n      {{"position": "80%", "reason": "몰입 피크 요인", "intensity": 8}}\n    ],\n    "reEngagementTechniques": ["재참여 기법 1", "재참여 기법 2"],\n    "avgRetentionScore": 75\n  }},\n  "hookTiming": {{\n    "openingHook": {{\n      "timing": "0-15초",\n      "type": "질문형",\n      "content": "오프닝 훅 내용",\n      "effectiveness": 8\n    }},\n    "midHooks": [\n      {{"timing": "30%", "type": "예고형", "content": "중반 훅 내용"}},\n      {{"timing": "60%", "type": "반전형", "content": "중반 훅 내용"}}\n    ],\n    "closingHook": {{\n      "timing": "마지막 30초",\n      "type": "CTA형",\n      "content": "마무리 훅 내용",\n      "effectiveness": 7\n    }},\n    "hookDensity": "medium",\n    "effectivenessScore": 78\n  }},\n  "contentCategory": {{\n    "primary": "주 카테고리 (교육/엔터테인먼트/뉴스/리뷰/브이로그/스토리텔링/다큐)",\n    "secondary": "부 카테고리",\n    "subGenre": "세부 장르 (미스터리/로맨스/역사/과학/심리 등)",\n    "targetAudience": "타겟 오디언스 설명 (예: 20-30대 직장인, 역사에 관심 있는 시청자)",\n    "contentStyle": "콘텐츠 스타일 (설명형/스토리형/리스트형/대화형/인터뷰형)"\n  }},\n  "titleOptimization": {{\n    "hookWords": ["훅 키워드 1", "훅 키워드 2", "훅 키워드 3"],\n    "emotionTriggers": ["감정 트리거 1", "감정 트리거 2"],\n    "curiosityGaps": ["호기심 갭 문구 1", "호기심 갭 문구 2"],\n    "powerWords": ["파워 워드 1", "파워 워드 2"],\n    "suggestedFormats": [\n      "[숫자] + [키워드]형: 예) \'3가지 충격적인 사실\'",\n      "[질문]형: 예) \'왜 ~인가?\'",\n      "[반전]형: 예) \'알고보니 ~였다\'"\n    ],\n    "thumbnailScenes": ["썸네일 추천 장면 1", "썸네일 추천 장면 2", "썸네일 추천 장면 3"]\n  }},\n  "paceAnalysis": {{\n    "overallPace": "slow 또는 medium 또는 fast",\n    "informationDensity": "low 또는 medium 또는 high",\n    "topicChanges": [\n      {{"position": "20%", "from": "이전 주제", "to": "다음 주제", "transition": "전환 방식"}},\n      {{"position": "50%", "from": "이전 주제", "to": "다음 주제", "transition": "전환 방식"}}\n    ],\n    "energyLevels": [\n      {{"position": "0%", "level": 7, "description": "에너지 설명"}},\n      {{"position": "50%", "level": 9, "description": "에너지 설명"}},\n      {{"position": "100%", "level": 6, "description": "에너지 설명"}}\n    ],\n    "pacingStyle": "페이스 스타일 (점진적 상승/롤러코스터/일정 유지/클라이맥스 집중)",\n    "recommendedAdjustments": ["페이스 조정 제안 1", "페이스 조정 제안 2"]\n  }},\n  "confidence": 85\n}}\n```\n\n## 분석 지침\n\n### 기본 분석\n\n1. **구조적 패턴 (structuralPattern)**\n   - ratio: 각 섹션이 전체 대본에서 차지하는 비율 (%). 합계는 100이어야 함\n   - hooks: 시청자를 끌어당기는 요소들\n   - transitions: 주제나 섹션을 전환하는 문구들\n   - tensionBuilders: 긴장감을 높이는 요소들\n\n2. **심리학적 패턴 (psychologicalPattern)**\n   - curiosityTriggers: 호기심을 유발하는 요소 (질문, 미완성 정보, 반전 예고 등)\n   - emotionalBeats: 감정 변화 포인트\n     - emotion: surprise, curiosity, fear, joy, sadness, anger, anticipation, frustration, relief, tension, excitement, empathy, nostalgia, shock, hope\n     - intensity: 1-10 스케일\n   - retentionHooks: 시청 유지를 위한 훅\n     - type: question(질문), promise(약속), tease(힌트), cliffhanger(절벽), callback(콜백)\n\n3. **기승전결 (narrativeStructure)**\n   - ki (기): 문제 제기, 상황 설정, 관심 유발\n   - seung (승): 배경 설명, 정보 전달, 깊이 있는 탐구\n   - jeon (전): 반전, 새로운 관점, 핵심 메시지\n   - gyeol (결): 결론, 교훈, 행동 촉구\n\n4. **핵심 포인트 (keyPoints)**\n   - importance: high, medium, low\n   - category: fact(사실), opinion(의견), example(예시), transition(전환)\n\n5. **톤/문체 감지 (detectedTone)**\n   - primary: 소설체, 강연체, 대화체, 다큐체, 예능체, 뉴스체\n   - formality: formal(격식체), casual(비격식체), mixed(혼합)\n   - emotion: neutral, dramatic, informative, humorous\n\n### 고도화 분석 (v2)\n\n6. **리텐션 분석 (retentionAnalysis)**\n   - dropOffRisks: 시청자 이탈 위험 지점 (position: 비율, severity: high/medium/low)\n   - engagementPeaks: 몰입도 피크 지점\n   - reEngagementTechniques: 재참여 유도 기법들\n   - avgRetentionScore: 예상 평균 리텐션 점수 (1-100)\n\n7. **훅 타이밍 분석 (hookTiming)**\n   - openingHook: 첫 30초 내 훅 (timing, type, content, effectiveness 1-10)\n   - midHooks: 중반부 훅들 (위치, 타입, 내용)\n   - closingHook: 마무리 훅 (다음 영상 유도, CTA 등)\n   - hookDensity: 훅 밀도 (low/medium/high)\n   - effectivenessScore: 전체 훅 효과 점수 (1-100)\n\n8. **콘텐츠 카테고리 (contentCategory)**\n   - primary: 교육, 엔터테인먼트, 뉴스, 리뷰, 브이로그, 스토리텔링, 다큐\n   - secondary: 부 카테고리\n   - subGenre: 미스터리, 로맨스, 역사, 과학, 심리, 범죄, 공포 등\n   - targetAudience: 구체적인 타겟 오디언스 설명\n   - contentStyle: 설명형, 스토리형, 리스트형, 대화형, 인터뷰형\n\n9. **제목/썸네일 최적화 (titleOptimization)**\n   - hookWords: 제목에 사용된/사용 가능한 훅 키워드\n   - emotionTriggers: 감정을 자극하는 단어들\n   - curiosityGaps: 호기심 갭을 만드는 문구들\n   - powerWords: 클릭을 유도하는 파워 워드\n   - suggestedFormats: 효과적인 제목 포맷 제안\n   - thumbnailScenes: 썸네일에 적합한 장면/순간 제안\n\n10. **페이스 분석 (paceAnalysis)**\n    - overallPace: 전체 속도감 (slow/medium/fast)\n    - informationDensity: 정보 밀도 (low/medium/high)\n    - topicChanges: 주제 변화 포인트들 (position, from, to, transition)\n    - energyLevels: 에너지 레벨 타임라인 (position, level 1-10, description)\n    - pacingStyle: 점진적 상승, 롤러코스터, 일정 유지, 클라이맥스 집중 등\n    - recommendedAdjustments: 페이스 개선을 위한 제안\n\n## 주의사항\n- 실제 자막 내용을 기반으로 분석하세요\n- 추측이나 가정을 최소화하세요\n- 자막에서 찾을 수 없는 요소는 빈 배열([])로 표시하세요\n- 반드시 유효한 JSON만 출력하세요\n- 고도화 분석은 가능한 한 구체적으로 작성하세요\n'''

    
    def _parse_analysis_response(self = None, response_text = None):
        '''AI 응답에서 JSON 추출 및 파싱'''
        json_match = re.search('```json\\s*([\\s\\S]*?)\\s*```', response_text)
        if json_match:
            json_str = json_match.group(1)
        else:
            json_str = response_text.strip()
        
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            e = None
            logger.warning(f'''JSON parse error, attempting repair: {e}''')
            repair_json = repair_json
            import json_repair
            repaired = repair_json(json_str)
            del e
            return None
            except Exception:
                None, json.loads(repaired), repair_error = None
                logger.error(f'''JSON repair also failed: {repair_error}''')
                del repair_error
                del e
                return None
                None = 
                del repair_error
            e = None
            del e


    
    def _get_default_analysis(self = None):
        '''분석 실패 시 기본값'''
        return {
            'structuralPattern': {
                'introduction': {
                    'ratio': 15,
                    'summary': '',
                    'hooks': [] },
                'development': {
                    'ratio': 50,
                    'mainPoints': [],
                    'transitions': [] },
                'climax': {
                    'ratio': 20,
                    'peakMoment': '',
                    'tensionBuilders': [] },
                'conclusion': {
                    'ratio': 15,
                    'callToAction': '',
                    'closingHooks': [] } },
            'psychologicalPattern': {
                'curiosityTriggers': [],
                'emotionalBeats': [],
                'retentionHooks': [] },
            'narrativeStructure': {
                'ki': {
                    'content': '',
                    'purpose': '' },
                'seung': {
                    'content': '',
                    'development': '' },
                'jeon': {
                    'content': '',
                    'twist': '' },
                'gyeol': {
                    'content': '',
                    'resolution': '' } },
            'keyPoints': [],
            'detectedTone': {
                'primary': '대화체',
                'secondary': '',
                'formality': 'mixed',
                'emotion': 'neutral',
                'description': '톤 분석 실패로 기본값 적용' },
            'retentionAnalysis': {
                'dropOffRisks': [],
                'engagementPeaks': [],
                'reEngagementTechniques': [],
                'avgRetentionScore': 50 },
            'hookTiming': {
                'openingHook': {
                    'timing': '',
                    'type': '',
                    'content': '',
                    'effectiveness': 0 },
                'midHooks': [],
                'closingHook': {
                    'timing': '',
                    'type': '',
                    'content': '',
                    'effectiveness': 0 },
                'hookDensity': 'medium',
                'effectivenessScore': 50 },
            'contentCategory': {
                'primary': '',
                'secondary': '',
                'subGenre': '',
                'targetAudience': '',
                'contentStyle': '' },
            'titleOptimization': {
                'hookWords': [],
                'emotionTriggers': [],
                'curiosityGaps': [],
                'powerWords': [],
                'suggestedFormats': [],
                'thumbnailScenes': [] },
            'paceAnalysis': {
                'overallPace': 'medium',
                'informationDensity': 'medium',
                'topicChanges': [],
                'energyLevels': [],
                'pacingStyle': '',
                'recommendedAdjustments': [] },
            'confidence': 30 }
