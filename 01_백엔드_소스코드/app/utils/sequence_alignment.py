# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sequence_alignment.pyc (Python 3.11)

'''
시퀀스 정렬 알고리즘

STT 대본 동기화를 위한 시퀀스 정렬 알고리즘들
- Enhanced DTW (Dynamic Time Warping)
- 앵커 기반 분할 정렬
- 타이밍 보간
'''
import logging
from typing import List, Dict, Tuple, Optional, Any
from dataclasses import dataclass
from enum import Enum
from app.utils.korean_text_utils import korean_similarity
logger = logging.getLogger(__name__)

class AlignmentType(Enum):
    '''정렬 타입'''
    MATCH = 'match'
    INSERT = 'insert'
    DELETE = 'delete'

AlignedWord = <NODE:12>()
STTWord = <NODE:12>()
SENTENCE_END_PUNCTUATION = '.?!。？！'
CLAUSE_PUNCTUATION = ',;:，；：'
PUNCTUATION_PAUSE_CONFIG = {
    'sentence_end': {
        'expected_pause': 0.25,
        'extension_boost': 0.08,
        'anticipation_boost': 0.05 },
    'clause': {
        'expected_pause': 0.12,
        'extension_boost': 0.04,
        'anticipation_boost': 0.02 },
    'none': {
        'expected_pause': 0.05,
        'extension_boost': 0,
        'anticipation_boost': 0 } }

def _get_segment_punctuation_type(segment_text = None):
    """
    세그먼트 텍스트의 마지막 구두점 타입을 반환

    Args:
        segment_text: 세그먼트 텍스트

    Returns:
        'sentence_end', 'clause', 또는 'none'
    """
    text = segment_text.strip()
    if not text:
        return 'none'
    last_char = None[-1]
    if last_char in SENTENCE_END_PUNCTUATION:
        return 'sentence_end'
    if None in CLAUSE_PUNCTUATION:
        return 'clause'


def _get_punctuation_adjusted_params(segment_text = None, base_anticipation = None, base_extension = None):
    '''
    구두점 타입에 따라 조정된 anticipation/extension 값 반환

    Args:
        segment_text: 세그먼트 텍스트
        base_anticipation: 기본 anticipation 값
        base_extension: 기본 extension 값

    Returns:
        (adjusted_anticipation, adjusted_extension)
    '''
    punct_type = _get_segment_punctuation_type(segment_text)
    config = PUNCTUATION_PAUSE_CONFIG.get(punct_type, PUNCTUATION_PAUSE_CONFIG['none'])
    adjusted_extension = base_extension + config['extension_boost']
    adjusted_anticipation = base_anticipation + config['anticipation_boost']
    return (adjusted_anticipation, adjusted_extension)


def _chunked_dtw_align(script_words, stt_words, gap_penalty_script = None, gap_penalty_stt = None, similarity_threshold = None, chunk_size = ('script_words', List[str], 'stt_words', List['STTWord'], 'gap_penalty_script', float, 'gap_penalty_stt', float, 'similarity_threshold', float, 'chunk_size', int, 'return', List['AlignedWord'])):
    '''
    대용량 입력을 앵커 기반 적응적 청킹으로 분할하여 DTW 정렬

    개선된 알고리즘:
    - 선형 분할 대신 **앵커 기반 분할** 사용
    - 앵커가 부족하면 **비율 기반 보조 앵커** 생성
    - 청크 경계에서 **타임스탬프 연속성** 보장

    Args:
        script_words: 대본 단어 리스트
        stt_words: STT 단어 리스트
        gap_penalty_script: 대본 갭 페널티
        gap_penalty_stt: STT 갭 페널티
        similarity_threshold: 유사도 임계값
        chunk_size: 청크 크기 (최대 구간 크기)

    Returns:
        정렬된 단어 리스트
    '''
    import gc
    n = len(script_words)
    m = len(stt_words)
    logger.info(f'''[Adaptive Chunked DTW] Input: {n} script words, {m} STT words''')
    anchors = _find_chunk_anchors(script_words, stt_words, chunk_size)
    if not anchors:
        logger.warning('[Adaptive Chunked DTW] No anchors found, creating ratio-based anchors')
        anchors = _create_ratio_based_anchors(n, m, chunk_size)
    logger.info(f'''[Adaptive Chunked DTW] Using {len(anchors)} anchors for chunking''')
    result = []
    prev_script_end = 0
    prev_stt_end = 0
    prev_end_time = 0
# WARNING: Decompyle incomplete


def _find_chunk_anchors(script_words = None, stt_words = None, max_chunk_size = None, min_similarity = (0.6,)):
    '''
    청킹을 위한 앵커 포인트 찾기

    max_chunk_size 간격마다 가장 유사한 단어쌍을 앵커로 선택

    Returns:
        [(script_idx, stt_idx), ...] 앵커 리스트
    '''
    n = len(script_words)
    m = len(stt_words)
    if n == 0 or m == 0:
        return []
    anchors = None
    target_anchors = max(n // max_chunk_size, 2)
    for i in range(1, target_anchors + 1):
        script_pos = int(i * n / (target_anchors + 1))
        expected_stt_pos = int(script_pos * m / n)
        search_range = max(20, m // target_anchors * 2)
        best_sim = 0
        best_script_idx = script_pos
        best_stt_idx = expected_stt_pos
        for si in range(max(0, script_pos - 5), min(n, script_pos + 6)):
            script_word = script_words[si]
            for sj in range(max(0, expected_stt_pos - search_range), min(m, expected_stt_pos + search_range)):
                sim = korean_similarity(script_word, stt_words[sj].word)
                if sim > best_sim:
                    best_sim = sim
                    best_script_idx = si
                    best_stt_idx = sj
                if best_sim >= min_similarity:
                    if anchors:
                        (prev_script, prev_stt) = anchors[-1]
                        if best_script_idx > prev_script and best_stt_idx > prev_stt:
                            anchors.append((best_script_idx, best_stt_idx))
                            logger.debug(f'''[Anchor] Found: script[{best_script_idx}] ↔ stt[{best_stt_idx}] (sim={best_sim:.2f})''')
                        continue
                    anchors.append((best_script_idx, best_stt_idx))
                    logger.debug(f'''[Anchor] Found: script[{best_script_idx}] ↔ stt[{best_stt_idx}] (sim={best_sim:.2f})''')
        return anchors


def _create_ratio_based_anchors(n = None, m = None, max_chunk_size = None):
    '''
    비율 기반 보조 앵커 생성 (앵커를 찾지 못했을 때 폴백)

    단, 선형 분할이 아닌 누적 비율 방식 사용
    '''
    anchors = []
    num_chunks = max(n // max_chunk_size, m // max_chunk_size, 2)
    for i in range(1, num_chunks):
        ratio = i / num_chunks
        script_idx = int(n * ratio)
        stt_idx = int(m * ratio)
        anchors.append((script_idx, stt_idx))
        return anchors


def _ensure_chunk_continuity(chunk_aligned, prev_end_time = None, stt_words = None, stt_start = None, stt_end = ('chunk_aligned', List['AlignedWord'], 'prev_end_time', float, 'stt_words', List['STTWord'], 'stt_start', int, 'stt_end', int, 'return', List['AlignedWord'])):
    '''
    청크 경계에서 타임스탬프 연속성 보장

    문제: 청크의 첫 단어 시작 시간이 이전 청크 끝보다 훨씬 이른 경우
    해결: 청크 내 타임스탬프를 적절히 조정 (단, STT 범위를 벗어나지 않도록)

    Args:
        chunk_aligned: 정렬된 청크
        prev_end_time: 이전 청크의 마지막 타임스탬프
        stt_words: 전체 STT 단어 리스트
        stt_start: 현재 청크의 STT 시작 인덱스
        stt_end: 현재 청크의 STT 끝 인덱스

    Returns:
        조정된 청크
    '''
    if not chunk_aligned:
        return chunk_aligned
    chunk_start_time = None
    chunk_end_time = None
# WARNING: Decompyle incomplete


def _direct_dtw_align(script_words = None, stt_words = None, gap_penalty_script = None, gap_penalty_stt = (0.6, 0.4, 0.3), similarity_threshold = ('script_words', List[str], 'stt_words', List['STTWord'], 'gap_penalty_script', float, 'gap_penalty_stt', float, 'similarity_threshold', float, 'return', List['AlignedWord'])):
    '''
    직접 DTW 정렬 (청크용 - 크기 제한 없음)

    enhanced_dtw_align의 실제 DTW 로직만 분리
    '''
    pass
# WARNING: Decompyle incomplete


def enhanced_dtw_align(script_words, stt_words = None, gap_penalty_script = None, gap_penalty_stt = None, similarity_threshold = (0.6, 0.4, 0.3, 150), max_segment_size = ('script_words', List[str], 'stt_words', List[STTWord], 'gap_penalty_script', float, 'gap_penalty_stt', float, 'similarity_threshold', float, 'max_segment_size', int, 'return', List[AlignedWord])):
    '''
    Enhanced DTW (Dynamic Time Warping) 기반 시퀀스 정렬

    동적 프로그래밍을 사용하여 대본과 STT 단어 시퀀스를 최적 정렬

    Args:
        script_words: 대본 단어 리스트
        stt_words: STT 단어 리스트 (타이밍 정보 포함)
        gap_penalty_script: 대본 단어 건너뛰기 페널티 (DELETE)
        gap_penalty_stt: STT 단어 건너뛰기 페널티 (INSERT)
        similarity_threshold: 매칭으로 인정하는 최소 유사도
        max_segment_size: DTW 최대 세그먼트 크기 (메모리 보호)

    Returns:
        정렬된 단어 리스트
    '''
    pass
# WARNING: Decompyle incomplete


def interpolate_missing_timings(aligned_words = None, total_duration = None, max_word_duration = None, avg_chars_per_second = (2, 4)):
