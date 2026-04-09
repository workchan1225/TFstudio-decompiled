# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tone_validator.pyc (Python 3.11)

'''
톤/어미 일관성 검증 모듈

대본 생성 후 선택된 톤에 맞는 어미가 일관되게 사용되었는지 검증합니다.
혼용된 어미가 있으면 경고를 반환합니다.
'''
import re
from typing import Dict, List, Tuple, Optional
from app.utils.narration_style_guide import TONE_REQUIRED_ENDINGS, TONE_FORBIDDEN_ENDINGS

def extract_narration_lines(text = None):
    '''
    텍스트에서 나레이션 라인만 추출

    Args:
        text: 대본 텍스트

    Returns:
        나레이션 라인 목록
    '''
    narration_pattern = '\\[?나레이션\\]?:\\s*(.+?)(?=\\n\\[|\\n$|$)'
    matches = re.findall(narration_pattern, text, re.MULTILINE | re.DOTALL)
    narrations = []
    for match in matches:
        lines = match.strip().split('\n')
        for line in lines:
            line = line.strip()
            if not line and line.startswith('['):
                narrations.append(line)
            return narrations


def extract_sentence_endings(text = None):
    '''
    텍스트에서 종결 어미 추출

    Args:
        text: 검증할 텍스트

    Returns:
        List of (sentence, ending) tuples
    '''
    narrations = extract_narration_lines(text)
    results = []
    for narration in narrations:
        sentences = re.split('(?<=[.!?。！？])\\s*', narration)
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 5:
                continue
            ending = extract_ending(sentence)
            if ending:
                results.append((sentence, ending))
            return results


def extract_ending(sentence = None):
