# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: costume_guide_loader.pyc (Python 3.11)

'''
CostumeGuideLoader - 장르/시대별 복장 가이드 데이터 로더

GENRE_COSTUME_GUIDE 데이터를 JSON에서 로드하고 캐싱합니다.
기존 SceneImageService._get_costume_guide() 로직을 대체합니다.
'''
import json
import logging
import threading
from pathlib import Path
from typing import Optional
logger = logging.getLogger(__name__)

class CostumeGuideLoader:
    pass
# WARNING: Decompyle incomplete


def get_costume_guide(genre = None, gender = None, period_setting = None):
    '''장르와 성별에 맞는 복장 가이드 반환

    CostumeGuideLoader.get_costume_guide()의 단축 함수
    '''
    return CostumeGuideLoader.get_costume_guide(genre, gender, period_setting)
