# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
API Controllers

Thin controllers that handle HTTP request/response and delegate to Use Cases.
Controllers should NOT contain business logic - only:
1. Parse request data
2. Call appropriate Use Case
3. Format response
4. Handle HTTP-specific concerns (status codes, headers)
'''
from app.api.controllers.project_controller import project_controller_bp
from app.api.controllers.settings_controller import settings_controller_bp
from app.api.controllers.media_controller import media_controller_bp
from app.api.controllers.ai_controller import ai_controller_bp
from app.api.controllers.assistant_controller import assistant_controller_bp
from app.api.controllers.tts_controller import tts_controller_bp
from app.api.controllers.bgm_controller import bgm_controller_bp
from app.api.controllers.prompt_templates_controller import prompt_templates_controller_bp
from app.api.controllers.server_controller import server_controller_bp
from app.api.controllers.analytics_controller import analytics_controller_bp
from app.api.controllers.editor_controller import editor_controller_bp
from app.api.controllers.subtitle_presets_controller import subtitle_presets_controller_bp
from app.api.controllers.image_templates_controller import image_templates_controller_bp
from app.api.controllers.script_controller import script_bp
from app.api.controllers.sfx_controller import sfx_controller_bp
from app.api.controllers.license_controller import license_controller_bp
from app.api.controllers.image_composer_controller import image_composer_bp
from app.api.controllers.diagnostics_controller import diagnostics_bp
__all__ = [
    'project_controller_bp',
    'settings_controller_bp',
    'media_controller_bp',
    'ai_controller_bp',
    'assistant_controller_bp',
    'tts_controller_bp',
    'bgm_controller_bp',
    'prompt_templates_controller_bp',
    'server_controller_bp',
    'analytics_controller_bp',
    'editor_controller_bp',
    'subtitle_presets_controller_bp',
    'image_templates_controller_bp',
    'script_bp',
    'sfx_controller_bp',
    'license_controller_bp',
    'image_composer_bp',
    'diagnostics_bp']
