# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: prompt_optimizer.pyc (Python 3.11)

'''
Prompt Optimizer Module (Pipeline Stage 4)
AI 기반 프롬프트 최적화

Features:
- Gemini Pro 기반 의미론적 분석
- 가중치 자동 조정
- 한국어 텍스트 렌더링 최적화
- 반복적 개선 (최대 3회)
'''
import logging
import json
import re
from typing import Dict, Any, Optional, List
from types import GeneratedPrompt, OptimizationResult, OptimizationAnalysis, OptimizationIteration
logger = logging.getLogger(__name__)

class PromptOptimizer:
    '''
    AI 기반 프롬프트 최적화 서비스

    Gemini Pro를 활용하여 프롬프트를 분석하고
    반복적으로 개선합니다.
    '''
    DEFAULT_ITERATIONS = 3
    DEFAULT_TEMPERATURE = 0.7
    
    def __init__(self):
        self._model = None

    
    def _get_model(self):
        '''Lazy load Gemini model'''
        pass
    # WARNING: Decompyle incomplete

    
    def optimize_prompt(self = None, prompt = None, iterations = None):
        '''
        프롬프트 최적화 수행

        Args:
            prompt: 초기 프롬프트
            iterations: 최적화 반복 횟수 (기본 3)

        Returns:
            OptimizationResult: 최적화 결과
        '''
        if not iterations:
            pass
        iterations = self.DEFAULT_ITERATIONS
        iteration_history = []
        current_prompt = prompt
        model = self._get_model()
    # WARNING: Decompyle incomplete

    
    def _optimize_iteration(self = None, model = None, prompt = None, iteration = ('model', Any, 'prompt', str, 'iteration', int, 'return', Optional[Dict[(str, Any)]])):
        '''단일 최적화 반복'''
        
        try:
            instruction = f'''당신은 텍스트-이미지 생성 AI 프롬프트 최적화 전문가입니다.\n\n다음 프롬프트를 분석하고 최적화하세요:\n\n[원본 프롬프트]\n{prompt}\n\n다음 기준으로 개선하세요:\n1. 의미론적 명확성: 모호한 표현을 구체적으로 변경\n2. 우선순위 정렬: 중요도에 따라 요소 재배치\n3. 기술적 정확성: AI가 잘 이해하는 용어 사용\n4. 텍스트 렌더링: 한글 폰트 호환성과 자간 최적화\n5. 중복 제거: 불필요한 반복 제거\n\n반복 #{iteration}: 이전 개선사항을 반영하여 추가 개선\n\n응답 형식 (JSON만):\n{{\n  "analysis": {{\n    "clarity_score": 0-100,\n    "technical_accuracy": 0-100,\n    "issues_found": ["문제1", "문제2"]\n  }},\n  "optimized_prompt": "최적화된 프롬프트",\n  "improvements": ["개선1", "개선2"]\n}}\n\nJSON만 응답하세요.'''
            response = model.generate_content(instruction, generation_config = {
                'temperature': self.DEFAULT_TEMPERATURE,
                'top_p': 0.95,
                'max_output_tokens': 1500 })
            return self._parse_json_response(response.text)
        except Exception:
            e = None
            logger.error(f'''Optimization iteration {iteration} failed: {e}''')
            e = None
            del e
            return None
            e = None
            del e


    
    def _final_analysis(self = None, model = None, prompt = None):
        '''최종 프롬프트 분석'''
        
        try:
            instruction = f'''다음 이미지 생성 프롬프트를 평가하세요:\n\n{prompt}\n\n다음 항목을 JSON으로 평가하세요:\n- clarity_score: 명확성 (0-100)\n- technical_accuracy: 기술적 정확성 (0-100)\n- text_rendering_optimization: 텍스트 렌더링 최적화 (0-100)\n- overall_confidence: 전체 신뢰도 (0-100)\n- korean_optimization_notes: 한국어 최적화 관련 노트\n- recommendations: 추가 권장사항 배열\n\n응답 형식 (JSON만):\n{{\n  "clarity_score": 85,\n  "technical_accuracy": 90,\n  "text_rendering_optimization": 88,\n  "overall_confidence": 88,\n  "korean_optimization_notes": "한글 폰트는 sans-serif 권장, 자간 넓게 설정",\n  "recommendations": ["권장사항1", "권장사항2"]\n}}\n\nJSON만 응답하세요.'''
            response = model.generate_content(instruction, generation_config = {
                'temperature': 0.5,
                'max_output_tokens': 800 })
            result = self._parse_json_response(response.text)
            if result:
                return OptimizationAnalysis(clarity_score = result.get('clarity_score', 75), technical_accuracy = result.get('technical_accuracy', 75), text_rendering_optimization = result.get('text_rendering_optimization', 75), overall_confidence = result.get('overall_confidence', 75), korean_optimization_notes = result.get('korean_optimization_notes', ''), recommendations = result.get('recommendations', []))
        except Exception:
            e = None
            logger.error(f'''Final analysis failed: {e}''')
            e = None
            del e
        except:
            e = None
            del e

        return OptimizationAnalysis()

    
    def _parse_json_response(self = None, response_text = None):
        '''JSON 응답 파싱'''
        
        try:
            text = response_text.strip()
            if '```json' in text:
                text = text.split('```json')[1].split('```')[0].strip()
            elif '```' in text:
                text = text.split('```')[1].split('```')[0].strip()
            json_match = re.search('\\{.*\\}', text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            return None.loads(text)
        except json.JSONDecodeError:
            e = None
            logger.error(f'''Failed to parse JSON response: {e}''')
            e = None
            del e
            return None
            e = None
            del e


    
    def _create_passthrough_result(self = None, prompt = None):
        '''패스스루 결과 (최적화 스킵)'''
        return OptimizationResult(original_prompt = prompt, optimized_prompt = prompt, iteration_history = [], analysis = OptimizationAnalysis(clarity_score = 75, technical_accuracy = 75, text_rendering_optimization = 75, overall_confidence = 75, korean_optimization_notes = '최적화가 스킵되었습니다', recommendations = []))

    
    def skip_optimization(self = None, prompt = None):
        '''최적화 스킵 (사용자 선택)'''
        return self._create_passthrough_result(prompt)

    
    def apply_korean_optimizations(self = None, prompt = None):
        '''한국어 텍스트 렌더링 최적화 규칙 적용'''
        korean_rules = [
            ('Korean text', 'Korean text with sans-serif font style'),
            ('Hangul', 'Hangul (Korean characters) without decomposition'),
            ('character spacing', 'wide character spacing for Korean readability')]
        optimized = prompt
        for old, new in korean_rules:
            if old in optimized and new not in optimized:
                optimized = optimized.replace(old, new)
            if (lambda .0: pass# WARNING: Decompyle incomplete
)(prompt()):
                optimized += ' | Korean text rendering: use NFC normalization, maintain character integrity'
        return optimized


_optimizer_instance: Optional[PromptOptimizer] = None

def get_prompt_optimizer():
    '''PromptOptimizer 싱글톤 인스턴스 반환'''
    pass
# WARNING: Decompyle incomplete
