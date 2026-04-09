# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: v2_controller.pyc (Python 3.11)

'''
Unified script generation V2 controller.
'''
from __future__ import annotations
import logging
from flask import Blueprint, jsonify, request
from app.services.script_generation_v2 import ScriptGenerationV2Request, ScriptGenerationV2Service
logger = logging.getLogger(__name__)
script_generation_v2_bp = Blueprint('script_generation_v2', __name__)
PROMPT_VERSION = getattr(ScriptGenerationV2Service, 'PROMPT_VERSION', 'script-gen-v2.1')
generate_script_v2 = (lambda : if not request.get_json(silent = True):
data = { }try:
service = ScriptGenerationV2Service()generation_request = ScriptGenerationV2Request.from_dict(data)result = service.generate(generation_request)status_code = 200 if result.success else 400logger.info('[ScriptGenerationV2Controller] mode=%s success=%s', generation_request.mode.value, result.success)(jsonify(result.to_dict()), status_code)except ValueError:
exc = Nonelogger.warning('[ScriptGenerationV2Controller] validation error: %s', exc)if not str(exc):
del excNonestr(exc) = Falsedel excexcept Exception:
logger.exception('[ScriptGenerationV2Controller] unhandled error'))()
