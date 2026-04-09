# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Script Generation Controllers

대본 생성 API 컨트롤러 모듈

Blueprint 등록:
    from app.api.controllers.script_generation import register_blueprints
    register_blueprints(app)
'''
from flask import Flask

def register_blueprints(app = None):
    '''
    대본 생성 관련 Blueprint 등록

    Args:
        app: Flask 앱 인스턴스
    '''
    reference_bp = reference_bp
    import reference_controller
    script_generation_v2_bp = script_generation_v2_bp
    import v2_controller
    app.register_blueprint(reference_bp, url_prefix = '/api/script-generation/reference')
    app.register_blueprint(script_generation_v2_bp, url_prefix = '/api/script-generation/v2')

__all__ = [
    'register_blueprints']
