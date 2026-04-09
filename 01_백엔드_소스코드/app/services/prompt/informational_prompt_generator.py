# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: informational_prompt_generator.pyc (Python 3.11)

'''
정보성 콘텐츠 스타일 이미지 프롬프트 생성기

4단계 공식 기반:
1. 주체 (Subject): 핵심 대상 + 성격/특징
2. 상황 및 배경 (Action & Environment): 장면 서사, 핵심 내용 전달
3. 스타일 및 매체 (Style & Medium): 사진/유화/3D 렌더링 등
4. 조명 및 분위기 (Lighting & Mood): 장면의 온도와 감정

사용 예시:
- "네온 사인이 가득한 사이버펑크 도시의 비 내리는 거리(배경),
   길가에 버려진 낡은 로봇이 작은 식물을 손에 쥐고 보호하는 모습(주체/상황).
   전체적으로 어둡고 축축한 분위기이며, 네온사인의 핑크색과 하늘색 빛이 로봇의 금속 표면에 반사됨(조명).
   실사 영화의 한 장면 같은 고화질 스타일(스타일)."
'''
import logging
import json
import re
from typing import Optional, Dict, Any
from dataclasses import dataclass
logger = logging.getLogger(__name__)

def _clean_json_response(response_text = None):
