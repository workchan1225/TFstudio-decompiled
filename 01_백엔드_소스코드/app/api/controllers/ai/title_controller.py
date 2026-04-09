# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: title_controller.pyc (Python 3.11)

'''
Title Controller

제목 생성 관련 API 엔드포인트.
- POST /generate-titles: 제목 생성
- POST /generate-creative-titles: 창작 제목 생성

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
    generate_titles = (lambda :
