# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reference_content_guard.pyc (Python 3.11)

'''
Reference content/source guard helpers.

레퍼런스 원문은 스타일/구조 분석에만 사용하고,
실제 생성 내용은 선택된 제목/시놉시스와 정렬되도록 검사한다.
'''
from __future__ import annotations
import re
from typing import Any, Dict, Iterable, List
_WORD_RE = re.compile('[A-Za-z0-9가-힣]{2,}')
_STOPWORDS = {
    '가장',
    '그것',
    '대본',
    '대한',
    '되는',
    '또한',
    '바로',
    '분석',
    '영상',
    '위한',
    '이것',
    '정말',
    '제목',
    '주제',
    '통해',
    '그러나',
    '그렇게',
    '그리고',
    '선택된',
    '이렇게',
    '콘텐츠',
    '하지만',
    '합니다',
    '레퍼런스',
    '시놉시스',
    '있습니다',
    '이유'}
_GENERIC_ANCHOR_TOKENS = {
    '결말',
    '고립',
    '교훈',
    '구조',
    '국가',
    '내부',
    '논리',
    '문제',
    '비극',
    '사례',
    '선택',
    '시작',
    '외부',
    '의미',
    '정권',
    '존재',
    '체제',
    '포기',
    '항복',
    '강력한',
    '내부의',
    '아니라',
    '역사적',
    '완전한',
    '외부의',
    '포기한',
    '항복은',
    '경제구조',
    '국민심리',
    '전쟁비용',
    '포기했던',
    '국가정체성',
    '이유'}

def _unique_preserve_order(items = None):
    seen = set()
    result = []
    for item in items:
        if not item:
            value = str('').strip()
            if not value:
                continue
        lowered = value.lower()
        if lowered in seen:
            continue
        seen.add(lowered)
        result.append(value)
        return result


def _normalize_text(text = None):
