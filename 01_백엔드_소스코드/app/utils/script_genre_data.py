# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_genre_data.pyc (Python 3.11)

__doc__ = '\nScript 장르 데이터 (29개 장르 + 후킹)\n\n각 장르별 상세 프롬프트, 기승전결 구조, 후킹 전략을 포함합니다.\n\n추가된 장르:\n- WAR_MILITARY: 전쟁/밀리터리 드라마 (6.25, 베트남전, 현대 군 이야기)\n- DISASTER_APOCALYPSE: 재난/아포칼립스 (자연재해, 전염병, 생존 이야기)\n'
from typing import Dict, List, Optional
from genre_categories import get_genre_category, get_in_medias_res_type, get_transition_phrase, InMediasResType

def _build_intro_preservation_instruction(genre = None):
