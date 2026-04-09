# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_generation_controller.pyc (Python 3.11)

'''
Script Generation Controller

대본 생성 관련 API 엔드포인트.
- POST /generate-script: 대본 생성
- POST /generate-script-from-research: 자료 조사 기반 대본 생성

기존 ai_controller.py에서 분리.
'''
from flask import Blueprint, request, jsonify
import logging
from typing import Callable
from app.application.dtos.script_dtos import GenerateScriptRequestDTO, GenerateScriptResponseDTO, ValidationLevel
logger = logging.getLogger(__name__)

def register_routes(bp = None):
    '''
    Blueprint에 라우트 등록

    Args:
        bp: Flask Blueprint 인스턴스
    '''
    generate_script = (lambda :
