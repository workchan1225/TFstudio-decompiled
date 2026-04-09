# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: korean_pos_analyzer.pyc (Python 3.11)

'''한국어 품사 분석 유틸리티 - kiwipiepy 기반

핵심 단어 텍스트에서 명사만 추출하기 위한 품사 분석기.
형용사, 동사, 부사를 필터링하여 이미지에 적합한 키워드만 허용.
'''
from functools import lru_cache
from typing import List, Tuple

try:
    from kiwipiepy import Kiwi
    _kiwi = Kiwi()
    KIWI_AVAILABLE = True
except ImportError:
    _kiwi = None
    KIWI_AVAILABLE = False

NOUN_TAGS = {
    'NR',
    'SN',
    'NNG',
    'NNP'}
SUFFIX_TAGS = {
    'XSA',
    'XSN',
    'XSV'}
REJECT_TAGS = {
    'VA',
    'VV',
    'VX',
    'ETM',
    'MAG',
    'MAJ'}
PARTICLE_TAGS = {
    'JC',
    'JX',
    'JKB',
    'JKC',
    'JKG',
    'JKO',
    'JKQ',
    'JKS',
    'JKV'}
ENDING_TAGS = {
    'EC',
    'EF',
    'EP',
    'ETM',
    'ETN'}
analyze_pos = (lambda text = None: if not KIWI_AVAILABLE or text:
()result = None.tokenize(text)(lambda .0: pass# WARNING: Decompyle incomplete
)(result())
)()

def _is_rejected_pos(pos = None):
