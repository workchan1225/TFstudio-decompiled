# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: informational_background_grounding.pyc (Python 3.11)

"""Background grounding rules for informational image generation.

Keep environment selection tied to the scene's own narrative context instead
of drifting into a generic placeholder backdrop.
"""
from __future__ import annotations
import re
from typing import Iterable, Optional
INDOOR_TOKENS = ('room', 'living room', 'bedroom', 'kitchen', 'hallway', 'corridor', 'office', 'meeting room', 'conference room', 'classroom', 'library', 'lab', 'laboratory', 'hospital', 'clinic', 'control room', 'studio', 'shop', 'store', 'cafe', 'restaurant', 'apartment', 'house', 'home', 'courtroom', 'warehouse', 'factory', '실내', '방', '거실', '침실', '주방', '부엌', '복도', '사무실', '회의실', '교실', '도서관', '연구실', '병원', '진료실', '통제실', '스튜디오', '매장', '카페', '식당', '아파트', '집', '법정', '창고', '공장')
OUTDOOR_TOKENS = ('street', 'road', 'alley', 'sidewalk', 'rooftop', 'parking lot', 'park', 'forest', 'mountain', 'beach', 'shore', 'river', 'field', 'harbor', 'station', 'platform', 'outdoor', 'outside', 'sky', 'desert', 'plaza', '광장', '야외', '실외', '거리', '도로', '골목', '인도', '옥상', '주차장', '공원', '숲', '산', '해변', '강', '들판', '항구', '역', '플랫폼', '하늘')
TIME_CUE_MAP = (('dawn', ('dawn', 'sunrise', '새벽', '동틀녘', '이른 아침')), ('morning', ('morning', '오전', '아침')), ('daytime', ('noon', 'midday', 'afternoon', 'daytime', '낮', '오후', '한낮')), ('evening', ('evening', 'sunset', 'dusk', '저녁', '해질녘', '노을')), ('night', ('night', 'midnight', 'late night', '밤', '심야', '야간')))
WEATHER_CUE_MAP = (('storm / severe weather', ('storm', 'typhoon', 'hurricane', 'thunder', 'lightning', '폭풍', '태풍', '폭우', '천둥', '번개')), ('rain / wet conditions', ('rain', 'rainy', 'drizzle', 'shower', '비', '비오는', '빗물', '장대비')), ('snow / freezing conditions', ('snow', 'snowy', 'blizzard', 'ice', '얼음', '눈', '눈보라', '한파')), ('fog / haze / smoke', ('fog', 'mist', 'haze', 'smoke', 'smoky', '안개', '연무', '연기', '자욱')), ('heat / dry glare', ('heatwave', 'scorching', 'blazing sun', '폭염', '열기', '강한 햇빛')), ('flood / standing water', ('flood', 'flooded', 'waterlogged', '침수', '홍수', '물이 차오른')), ('fire / burn aftermath', ('fire', 'burning', 'flame', 'ember', '화재', '불길', '불타는')))
HAZARD_EVENT_TOKENS = ('warning', 'alert', 'emergency', 'danger', 'risk', 'evacuation', 'crisis', 'disaster', 'accident', 'collapse', 'infection', 'outbreak', 'panic', '경보', '주의보', '긴급', '비상', '위험', '재난', '사고', '대피', '붕괴', '감염', '확산', '패닉')
CONTEXTUAL_WORKFLOW_TOKENS = ('analysis', 'investigation', 'research', 'monitoring', 'briefing', 'lecture', 'class', 'meeting', 'diagnosis', 'treatment', 'broadcast', 'news', 'presentation', 'report', 'training', 'study', 'planning', '분석', '조사', '연구', '모니터링', '브리핑', '강의', '수업', '회의', '진단', '치료', '방송', '뉴스', '발표', '보고', '훈련', '공부', '계획')

def _normalize_scene_text(value = None):
