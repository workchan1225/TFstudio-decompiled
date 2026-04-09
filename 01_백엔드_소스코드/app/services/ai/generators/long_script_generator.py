# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: long_script_generator.pyc (Python 3.11)

'''
장편 대본 생성기

Gemini 2.5 Flash를 사용하여 1회 API 호출로 최대 40,000자 대본 생성.
논리적 일관성(캐릭터, 복선, 톤)을 유지하는 것이 핵심.

특징:
- 1회 API 호출로 전체 대본 생성
- Gemini 2.5 Flash의 높은 출력 토큰 한도(32,000) 활용
- 프롬프트 내에서 전체 구조 설계 → 챕터별 작성
- 장르 기반 프롬프트 적용
'''
import re
import time
import logging
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass, field
from app.utils.long_script_prompts import build_long_script_system_prompt, build_long_script_user_prompt
from app.utils.script_length_calculator import validate_script_length, get_length_info, MAX_CHARS
from app.services.prompt.constraints.tone_dampening_enforcer import ToneDampeningEnforcer
logger = logging.getLogger(__name__)
GenerationProgress = <NODE:12>()
GenerationResult = <NODE:12>()

class LongScriptGenerator:
    '''
    장편 대본 생성기

    Gemini 2.5 Flash를 사용하여 1회 호출로 장편 대본을 생성합니다.
    '''
    MODEL_NAME = 'gemini-2.5-flash'
    MAX_RETRIES = 2
    RETRY_DELAY = 3
    
    def __init__(self, genai):
        '''
        초기화

        Args:
            genai: google.generativeai 모듈
        '''
        self.genai = genai
        self._dampening_enforcer = ToneDampeningEnforcer()

    
    def _get_model(self = None, genre = None):
        '''
        Gemini 2.5 Flash 모델 반환

        Args:
            genre: 장르 코드 (톤 완화 레벨에 따라 temperature 조정)

        Returns:
            GenerativeModel 인스턴스
        '''
        base_temperature = 0.9
        if genre and self._dampening_enforcer.is_enabled():
            temperature = self._dampening_enforcer.get_temperature_override(genre, base_temperature)
            logger.info(f'''[LongScriptGenerator] 톤 완화 적용: {genre} -> temperature={temperature}''')
        else:
            temperature = base_temperature
        return self.genai.GenerativeModel(self.MODEL_NAME, generation_config = {
            'temperature': temperature,
            'top_p': 0.95,
            'top_k': 64,
            'max_output_tokens': 32000 })

    
    def generate_full_script(self, title, synopsis, genre, chapter_count, target_chars, characters, tone = None, additional_context = None, progress_callback = None, speaker_tag_mode = (None, 'neutral', None, None, 'with_tags', 50), narration_ratio = ('title', str, 'synopsis', str, 'genre', str, 'chapter_count', int, 'target_chars', int, 'characters', Optional[List[Dict]], 'tone', str, 'additional_context', Optional[str], 'progress_callback', Optional[Callable[([
        GenerationProgress], None)]], 'speaker_tag_mode', str, 'narration_ratio', int, 'return', GenerationResult)):
        """
        전체 대본 생성 (1회 API 호출)

        Args:
            title: 작품 제목
            synopsis: 시놉시스
            genre: 장르 코드
            chapter_count: 챕터 수 (5~8)
            target_chars: 목표 글자수 (최대 40,000)
            characters: 캐릭터 목록
            tone: 톤 설정
            additional_context: 추가 컨텍스트
            progress_callback: 진행 상황 콜백
            speaker_tag_mode: 화자 태그 모드 ('with_tags' | 'without_tags')
            narration_ratio: 나레이션/대사 비율 (0-100, 기본 50)

        Returns:
            GenerationResult
        """
        (is_valid, error_msg) = validate_script_length(target_chars)
        if not is_valid:
            return GenerationResult(success = False, script = '', chapters = [], total_chars = 0, chapter_count = 0, error = error_msg)
        if None < 5 or chapter_count > 8:
            return GenerationResult(success = False, script = '', chapters = [], total_chars = 0, chapter_count = 0, error = f'''챕터 수는 5~8 사이여야 합니다: {chapter_count}''')
        None._update_progress(progress_callback, GenerationProgress(status = 'preparing', progress = 0.1, message = '프롬프트 준비 중...', target_chars = target_chars))
        system_prompt = build_long_script_system_prompt(genre = genre, chapter_count = chapter_count, target_chars = target_chars, characters = characters, tone = tone, additional_context = additional_context, speaker_tag_mode = speaker_tag_mode, narration_ratio = narration_ratio)
        user_prompt = build_long_script_user_prompt(title = title, synopsis = synopsis, target_chars = target_chars, chapter_count = chapter_count)
        logger.info(f'''[LongScriptGenerator] 대본 생성 시작: {title}, {target_chars:,}자, {chapter_count}챕터''')
        logger.info('[LongScriptGenerator] prompt prepared: system_chars=%s user_chars=%s', len(system_prompt), len(user_prompt))
        self._update_progress(progress_callback, GenerationProgress(status = 'generating', progress = 0.2, message = 'Gemini 2.5 Flash로 대본 생성 중...', target_chars = target_chars))
        
        try:
            script_text = self._call_gemini_with_retry(system_prompt, user_prompt, progress_callback, target_chars, genre = genre)
        except Exception:
            e = None
            logger.error(f'''[LongScriptGenerator] API 호출 실패: {e}''')
            del e
            return None
            None = 
            del e

        self._update_progress(progress_callback, GenerationProgress(status = 'generating', progress = 0.9, message = '대본 파싱 중...', generated_chars = len(script_text), target_chars = target_chars))
        chapters = self._parse_script(script_text, chapter_count)
        total_chars = (lambda .0: pass# WARNING: Decompyle incomplete
)(chapters())
        warnings = []
        char_ratio = total_chars / target_chars if target_chars > 0 else 0
        if char_ratio < 0.9:
            shortage = target_chars - total_chars
            warnings.append(f'''⚠️ 생성된 대본이 목표보다 {shortage:,}자 부족합니다. (목표: {target_chars:,}자, 실제: {total_chars:,}자, 달성률: {char_ratio * 100:.1f}%)''')
        elif char_ratio < 0.95:
            warnings.append(f'''생성된 대본이 목표에 근접합니다. (목표: {target_chars:,}자, 실제: {total_chars:,}자, 달성률: {char_ratio * 100:.1f}%)''')
        self._update_progress(progress_callback, GenerationProgress(status = 'completed', progress = 1, message = '대본 생성 완료', generated_chars = total_chars, target_chars = target_chars))
        logger.info(f'''[LongScriptGenerator] 대본 생성 완료: {total_chars:,}자, {len(chapters)}챕터''')
        return GenerationResult(success = True, script = script_text, chapters = chapters, total_chars = total_chars, chapter_count = len(chapters), warnings = warnings if warnings else None)

    
    def _call_gemini_with_retry(self, system_prompt = None, user_prompt = None, progress_callback = None, target_chars = (None, 0, None), genre = ('system_prompt', str, 'user_prompt', str, 'progress_callback', Optional[Callable], 'target_chars', int, 'genre', str, 'return', str)):
        '''
        Gemini API 호출 (재시도 포함)

        Args:
            system_prompt: 시스템 프롬프트
            user_prompt: 사용자 프롬프트
            progress_callback: 진행 상황 콜백
            target_chars: 목표 글자수
            genre: 장르 코드 (톤 완화용)

        Returns:
            생성된 대본 텍스트
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _parse_script(self = None, script_text = None, expected_chapters = None):
        '''
        대본 텍스트를 챕터별로 파싱

        Args:
            script_text: 전체 대본 텍스트
            expected_chapters: 예상 챕터 수

        Returns:
            챕터 목록 [{"title": str, "content": str, "characterCount": int, ...}, ...]
        '''
        chapters = []
        chapter_pattern = '#{1,2}\\s*챕터\\s*(\\d+)[:\\s]+(.+?)(?=\\n)'
        matches = list(re.finditer(chapter_pattern, script_text))
        if not matches:
            alt_pattern = '\\*{0,2}챕터\\s*(\\d+)\\*{0,2}[.:\\s]+(.+?)(?=\\n)'
            matches = list(re.finditer(alt_pattern, script_text))
        if not matches:
            logger.warning('[LongScriptGenerator] 챕터 파싱 실패, 전체를 하나의 챕터로 처리')
            return [
                {
                    'title': '전체 대본',
                    'content': script_text.strip(),
                    'characterCount': len(script_text.strip()),
                    'estimatedTime': (len(script_text.strip()) / 700) * 60,
                    'index': 0 }]
        for i, match in None(matches):
            chapter_num = int(match.group(1))
            chapter_title = match.group(2).strip()
            start_pos = match.end()
            if i + 1 < len(matches):
                end_pos = matches[i + 1].start()
            else:
                end_pos = len(script_text)
            content = script_text[start_pos:end_pos].strip()
            content = re.sub('^---+$', '', content, flags = re.MULTILINE).strip()
            chapters.append({
                'title': chapter_title,
                'content': content,
                'characterCount': len(content),
                'estimatedTime': (len(content) / 700) * 60,
                'index': chapter_num - 1 })
            chapters.sort(key = (lambda x: x['index']))
            return chapters

    
    def _update_progress(self = None, callback = None, progress = None):
        '''진행 상황 콜백 호출'''
        if callback:
            
            try:
                callback(progress)
                return None
            except Exception:
                e = None
                logger.warning(f'''[LongScriptGenerator] 진행 상황 콜백 오류: {e}''')
                e = None
                del e
                return None
                e = None
                del e
                return None




def create_long_script_generator(api_key = dataclass):
    '''
    LongScriptGenerator 인스턴스 생성 헬퍼

    Args:
        api_key: Google API 키

    Returns:
        LongScriptGenerator 인스턴스
    '''
    configure_legacy_genai = configure_legacy_genai
    import app.utils.google_sdk
    return LongScriptGenerator(configure_legacy_genai(api_key))
