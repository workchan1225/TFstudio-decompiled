# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_cleaner.pyc (Python 3.11)

'''
Text Cleaner

일반 텍스트 정리 유틸리티.
JSON 아티팩트 제거, 공백 정리 등.
'''
import re
from typing import Optional

class TextCleaner:
    '''
    텍스트 정리 클래스

    AI 응답에서 불필요한 문자나 형식 제거.
    '''
    
    def __init__(self):
        '''초기화'''
        pass

    
    def clean_json_artifacts(self = None, text = None):
        '''
        JSON 관련 아티팩트 제거

        마크다운 코드 블록, 이스케이프 문자, JSON 구조 잔재 등 정리.

        Args:
            text: 원본 텍스트

        Returns:
            정리된 텍스트
        '''
        if not text:
            return text
        text = None.sub('^```(?:json|JSON|text|markdown)?\\s*\\n?', '', text, flags = re.MULTILINE)
        text = re.sub('\\n?```\\s*$', '', text, flags = re.MULTILINE)
        text = re.sub('```(?:json|JSON|text|markdown)?\\s*', '', text)
        text = re.sub('\\s*```', '', text)
        text = text.replace('\\n', '\n')
        text = text.replace('\\t', '\t')
        text = text.replace('\\"', '"')
        text = text.replace("\\'", "'")
        text = text.replace('\\\\', '\\')
        text = re.sub('^\\s*\\{\\s*"chapters"\\s*:\\s*\\[\\s*', '', text)
        text = re.sub('\\{\\s*"title"\\s*:\\s*"[^"]*"\\s*,\\s*"content"\\s*:\\s*"', '', text)
        text = re.sub('"\\s*\\}\\s*,\\s*\\{\\s*"title"\\s*:\\s*"[^"]*"\\s*,\\s*"content"\\s*:\\s*"', '\n\n', text)
        text = re.sub('"\\s*\\}\\s*\\]\\s*\\}\\s*$', '', text)
        text = re.sub('"\\s*\\}\\s*\\]\\s*$', '', text)
        text = re.sub('"\\s*\\}\\s*$', '', text)
        text = re.sub('"{2,}', '"', text)
        text = re.sub("'{2,}", "'", text)
        text = re.sub('\\n{3,}', '\n\n', text)
        return text.strip()

    
    def normalize_whitespace(self = None, text = None):
        '''
        공백 정규화

        연속 공백, 탭, 줄바꿈 정리.

        Args:
            text: 원본 텍스트

        Returns:
            정리된 텍스트
        '''
        if not text:
            return text
        text = None.replace('\t', ' ')
        text = re.sub(' {2,}', ' ', text)
        text = re.sub('\\n{3,}', '\n\n', text)
        text = re.sub(' +\\n', '\n', text)
        return text.strip()

    
    def remove_control_characters(self = None, text = None):
        '''
        제어 문자 제거

        눈에 보이지 않는 제어 문자 제거.

        Args:
            text: 원본 텍스트

        Returns:
            정리된 텍스트
        '''
        if not text:
            return text
        text = None.sub('[\\x00-\\x08\\x0b\\x0c\\x0e-\\x1f\\x7f]', '', text)
        return text

    
    def clean_speaker_line(self = None, line = None):
        '''
        화자 라인 정리

        대괄호 내부 공백, 콜론 주변 공백 등 정리.

        Args:
            line: 대본 라인

        Returns:
            정리된 라인
        '''
        if not line:
            return line
        line = None.sub('\\[\\s+', '[', line)
        line = re.sub('\\s+\\]', ']', line)
        line = re.sub('\\]\\s*:', ']:', line)
        line = re.sub(':\\s{2,}', ': ', line)
        return line

    
    def clean_script(self = None, script = None):
        '''
        대본 전체 정리

        모든 정리 작업을 순차적으로 적용.

        Args:
            script: 원본 대본

        Returns:
            정리된 대본
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def truncate_safely(self = None, text = None, max_length = None, suffix = ('...',)):
        '''
        안전하게 텍스트 자르기

        문장 중간에서 자르지 않고 적절한 위치에서 자름.

        Args:
            text: 원본 텍스트
            max_length: 최대 길이
            suffix: 잘린 경우 추가할 접미사

        Returns:
            잘린 텍스트
        '''
        if text or len(text) <= max_length:
            return text
        target_length = None - len(suffix)
        if target_length <= 0:
            return suffix[:max_length]
        truncated = None[:target_length]
        for delimiter in ('. ', '! ', '? ', '。', '\n'):
            last_pos = truncated.rfind(delimiter)
            if last_pos > target_length * 0.5:
                
                return None, truncated[:last_pos + 1] + suffix
            if last_space > target_length * 0.7:
                return truncated[:last_space] + suffix
            return truncated.rfind(' ') + suffix
