# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: speaker_normalizer.pyc (Python 3.11)

"""
Speaker Normalizer - 화자명 정규화 및 검증 유틸리티

대본 업로드, 장면 일괄 생성, 캐릭터 분석 등에서 공통으로 사용하는
화자명 정규화 및 메타데이터 필터링 로직을 제공합니다.

주요 기능:
- 화자명 정규화: 유사 표기 통일 (나레이션, 내레이션, narration → 나레이션)
- 자동 화자 alias 정규화: '나레이션1' → '나레이션', '화자1' → '화자'
- 사용자 정의 이름은 숫자/jamo를 포함해도 보존: '1ㅁ' → '1ㅁ', '민수123' → '민수123'
- 메타데이터 필터링: URL, 금액, 키-값 형식 제외

사용법:
    from app.utils.speaker_normalizer import (
        canonicalize_speaker_name,
        is_likely_metadata_speaker_label,
        is_valid_speaker_name
    )

    # 화자명 정규화
    speaker = canonicalize_speaker_name('나레이션1')  # → '나레이션'

    # 메타데이터 여부 확인
    if is_likely_metadata_speaker_label('결제금액', '100,000원'):
        # 메타데이터이므로 화자로 처리하지 않음
        pass

    # 유효한 화자명인지 확인
    if is_valid_speaker_name('민수'):
        # 유효한 화자명
        pass
"""
import re
from typing import List, Optional, Set
NARRATION_ALIASES: Set[str] = {
    'narr',
    'speaker',
    'narrator',
    'narration',
    '나레이션',
    '나레이터',
    '내레이션'}
GENERIC_SPEAKER_ALIASES: Set[str] = {
    '화자',
    '발화자'}
SPEAKER_LETTER_PATTERN = re.compile('[A-Za-z가-힣ㄱ-ㅎㅏ-ㅣ一-龥ぁ-んァ-ヶ]')

def canonicalize_speaker_name(speaker = None):
