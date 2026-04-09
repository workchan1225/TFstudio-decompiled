# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tts_state_manager.pyc (Python 3.11)

'''
TTSStateManager - TTS 생성 상태 관리 (취소 기능 지원)

싱글톤 패턴으로 프로젝트별 TTS 생성 상태를 관리합니다.
생성 중 취소 요청을 받으면 진행 중인 루프를 중단시킵니다.
'''
import threading
from typing import Set
import logging
logger = logging.getLogger(__name__)

class TTSStateManager:
    pass
# WARNING: Decompyle incomplete


def get_tts_state_manager():
    '''TTSStateManager 싱글톤 인스턴스를 반환합니다.'''
    return TTSStateManager()
