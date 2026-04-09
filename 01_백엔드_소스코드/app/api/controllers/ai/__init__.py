# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

"""
AI Controllers Package

도메인별로 분할된 AI 컨트롤러 모듈.
기존 ai_controller.py의 2457줄+ 코드를 도메인별로 분리.

구조:
- script_generation_controller: 대본 생성 (generate-script, generate-script-from-research)
- script_expansion_controller: 대본 확장 (expand-script)
- title_controller: 제목 생성 (generate-titles, generate-creative-titles)
- synopsis_controller: 시놉시스/캐릭터 (generate-synopses, generate-characters-from-synopsis)
- scene_controller: 씬 분석/생성 (미래 추가)

사용법:
    from app.api.controllers.ai import ai_bp
    app.register_blueprint(ai_bp, url_prefix='/api/ai')
"""
from flask import Blueprint
ai_bp = Blueprint('ai_v2', __name__)
from script_generation_controller import register_routes as register_script_generation
from script_expansion_controller import register_routes as register_script_expansion
from title_controller import register_routes as register_titles
from synopsis_controller import register_routes as register_synopsis
register_script_generation(ai_bp)
register_script_expansion(ai_bp)
register_titles(ai_bp)
register_synopsis(ai_bp)
__all__ = [
    'ai_bp']
