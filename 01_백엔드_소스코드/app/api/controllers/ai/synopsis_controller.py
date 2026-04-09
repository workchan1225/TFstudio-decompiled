# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: synopsis_controller.pyc (Python 3.11)

'''
Synopsis Controller

시놉시스/캐릭터 생성 관련 API 엔드포인트.
- POST /generate-synopses: 시놉시스 생성
- POST /generate-characters-from-synopsis: 시놉시스에서 캐릭터 생성
- POST /suggest-character-names: 캐릭터 이름 제안

기존 ai_controller.py에서 분리.
'''
from flask import Blueprint, request, jsonify
import logging
logger = logging.getLogger(__name__)

def register_routes(bp = None):
    '''
    Blueprint에 라우트 등록

    Args:
        bp: Flask Blueprint 인스턴스
    '''
    generate_synopses = (lambda :
