# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_expansion_controller.pyc (Python 3.11)

'''
Script Expansion Controller

대본 확장 관련 API 엔드포인트.
- POST /expand-script: 대본 확장

기존 ai_controller.py에서 분리.
'''
from flask import Blueprint, request, jsonify
import logging
from app.application.dtos.script_dtos import ExpandScriptRequestDTO, ValidationLevel
logger = logging.getLogger(__name__)

def register_routes(bp = None):
    '''
    Blueprint에 라우트 등록

    Args:
        bp: Flask Blueprint 인스턴스
    '''
    expand_script = (lambda :
