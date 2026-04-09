# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_fixer.pyc (Python 3.11)

'''
Script Fixer

대본 문제 수정 전문 모듈.
google_provider.py에서 분리.

v2.0: 장르별 수정 규칙 시스템 통합
- 드라마 장르: 추상 감정→신체 반응, 대비 강조, 복선 보강, 카타르시스 강화
- 정보 장르: 금지 표현→대체 표현, 추상적 표현 구체화, 리텐션 훅 자동 삽입
'''
import re
import json
from typing import List, Dict, Any, Optional
from constants import get_tone_instruction

try:
    from app.utils.script_genre_prompts import get_genre_fix_prompt, get_genre_type, is_drama_genre, is_info_genre, validate_info_script
    GENRE_FIX_AVAILABLE = True
except ImportError:
    GENRE_FIX_AVAILABLE = False
    print('[ScriptFixer] Warning: Genre fix system not available')


class ScriptFixer:
    '''
    스크립트 수정기

    분석에서 발견된 문제점을 수정.
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

    
    def fix_script_issues(self, script, issues, synopsis = None, tone = None, model = None, use_surgical = (None, None, None, True, None), genre = ('script', str, 'issues', list, 'synopsis', str, 'tone', str, 'model', str, 'use_surgical', bool, 'genre', str, 'return', Dict[(str, Any)]), **kwargs):
        '''
        분석에서 발견된 문제점을 수정한 대본 반환

        수정 전략:
        1. Surgical Fix (우선): 문제 위치만 정확히 수정
        2. 청크 기반 수정 (폴백): 긴 대본의 경우
        3. 단일 수정 (폴백): 짧은 대본의 경우

        v2.0: genre 파라미터로 장르별 수정 규칙 적용
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _surgical_fix(self, script = None, issues = None, gemini_model = None, tone = (None, None), genre = ('script', str, 'issues', list, 'tone', str, 'genre', str, 'return', Dict[(str, Any)])):
        '''Surgical Fix: 문제 위치만 정확히 수정 (v2.0: 장르별 수정 규칙 지원)'''
        fixed_script = script
        replacements = []
        failed_fixes = []
        genre_fix_rules = ''
        if genre and GENRE_FIX_AVAILABLE:
            genre_rules = get_genre_fix_prompt(genre)
            if genre_rules:
                genre_fix_rules = f'''\n**장르별 수정 규칙 ({genre}):**\n{genre_rules}\n'''
                print(f'''[_surgical_fix] Applied genre-specific fix rules for: {genre}''')
        for i, issue in enumerate(issues):
            location = issue.get('location', '')
            if location or len(location) < 5:
                failed_fixes.append(f'''Issue {i + 1}: location too short''')
                continue
            location_pattern = re.escape(location[:30])
            match = re.search(location_pattern, fixed_script)
            if not match:
                failed_fixes.append(f'''Issue {i + 1}: location not found in script''')
                continue
            start_pos = match.start()
            end_pos = match.end()
            line_start = fixed_script.rfind('\n', 0, start_pos)
            if line_start == -1:
                line_start = 0
            else:
                line_start += 1
            next_newline = fixed_script.find('\n', end_pos)
            if next_newline == -1:
                next_newline = len(fixed_script)
            original_sentence = fixed_script[line_start:next_newline]
            tone_instruction = get_tone_instruction(tone)
            fix_prompt = f'''다음 문장에서 문제를 수정해주세요.\n\n**원본 문장:**\n{original_sentence}\n\n**문제점:**\n- 유형: {issue.get('type', '알 수 없음')}\n- 설명: {issue.get('description', '')}\n- 수정 제안: {issue.get('suggestion', '')}\n{tone_instruction}\n**수정 규칙:**\n1. 문장의 의미와 길이를 최대한 유지\n2. 화자 태그가 있으면 그대로 유지\n3. 수정된 문장만 출력 (설명 없이)\n4. **기존 말투/톤을 반드시 유지**\n{genre_fix_rules}\n**수정된 문장:**'''
            response = gemini_model.generate_content(fix_prompt, generation_config = {
                'temperature': 0.1,
                'max_output_tokens': 1024 })
            fixed_sentence = response.text.strip()
            if len(fixed_sentence) < len(original_sentence) * 0.5:
                failed_fixes.append(f'''Issue {i + 1}: fixed sentence too short''')
                continue
            if len(fixed_sentence) > len(original_sentence) * 2:
                failed_fixes.append(f'''Issue {i + 1}: fixed sentence too long''')
                continue
            fixed_script = fixed_script[:line_start] + fixed_sentence + fixed_script[next_newline:]
            replacements.append({
                'original': original_sentence[:50] + '...' if len(original_sentence) > 50 else original_sentence,
                'fixed': fixed_sentence[:50] + '...' if len(fixed_sentence) > 50 else fixed_sentence,
                'issue_type': issue.get('type', '') })
            print(f'''[_surgical_fix] Fixed issue {i + 1}: {issue.get('type', '')}''')
            except Exception:
                e = None
                failed_fixes.append(f'''Issue {i + 1}: API error - {str(e)}''')
                e = None
                del e
                continue
                e = None
                del e
            success = len(replacements) >= len(issues) * 0.5
            if failed_fixes:
                print(f'''[_surgical_fix] Failed fixes: {failed_fixes}''')
        return {
            'success': success,
            'fixedScript': fixed_script,
            'replacements': replacements,
            'failedFixes': failed_fixes }

    
    def _fix_single_script(self, script, issues = None, synopsis = None, gemini_model = None, tone = (None, None), genre = ('script', str, 'issues', list, 'synopsis', str, 'tone', str, 'genre', str, 'return', str)):
        '''단일 대본 수정 (v2.0: 장르별 수정 규칙 지원)'''
        issues_str = (lambda .0: [ f'''{i + 1}. [{issue.get('type', '문제')}]\n   위치: "{issue.get('location', '')[:50]}"\n   문제: {issue.get('description', '')}\n   제안: {issue.get('suggestion', '')}''' for i, issue in .0 ])(enumerate(issues)())
        tone_instruction = get_tone_instruction(tone)
        genre_fix_section = ''
        if genre and GENRE_FIX_AVAILABLE:
            genre_rules = get_genre_fix_prompt(genre)
            if genre_rules:
                genre_fix_section = f'''\n## 장르별 수정 규칙 ({genre}):\n{genre_rules}\n'''
                print(f'''[_fix_single_script] Applied genre-specific fix rules for: {genre}''')
        prompt = f'''다음 대본의 문제점을 수정해주세요.\n\n## 원본 대본:\n{script}\n\n## 수정해야 할 문제:\n{issues_str}\n\n{tone_instruction}\n\n## 수정 규칙:\n1. **문제 문장만 수정하고 나머지는 그대로 유지**\n2. **챕터 구조([챕터 N]) 반드시 유지**\n3. **화자 태그(이름:) 반드시 유지**\n4. **대본 길이를 유지** (±10% 이내)\n5. **톤/말투 유지 (최우선)**\n{genre_fix_section}\n## 수정된 대본 (설명 없이):**'''
        
        try:
            response = gemini_model.generate_content(prompt, generation_config = {
                'temperature': 0.2,
                'max_output_tokens': 50000 })
            return response.text.strip()
        except Exception:
            e = None
            print(f'''[_fix_single_script] Error: {e}''')
            del e
            return None
            None = 
            del e


    
    def _fix_script_in_chunks(self, script, issues, synopsis = None, gemini_model = None, original_chapters = None, tone = (None, None), genre = ('script', str, 'issues', list, 'synopsis', str, 'original_chapters', list, 'tone', str, 'genre', str, 'return', str)):
        '''청크 기반 대본 수정 (v2.0: 장르별 수정 규칙 지원)'''
        pass
    # WARNING: Decompyle incomplete

    
    def _merge_chunks_safely(self = None, chunks = None, chapter_pattern = None):
        '''청크 안전하게 병합'''
        merged = '\n\n'.join(chunks)
        merged = re.sub('\\n{3,}', '\n\n', merged)
        return merged

    
    def _validate_fixed_script(self, original_script = None, fixed_script = None, original_chapters = None, original_speakers = ('original_script', str, 'fixed_script', str, 'original_chapters', list, 'original_speakers', list, 'return', Dict[(str, Any)])):
