# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_controller.pyc (Python 3.11)

'''
Script Controller - 대본 분석 API 엔드포인트
'''
from flask import Blueprint, request, jsonify
from app.services.script_analyzer_service import ScriptAnalyzerService
script_bp = Blueprint('scripts', __name__, url_prefix = '/api/scripts')
analyze_script = (lambda : try:
data = request.get_json()if not data:
(jsonify({
'success': False,
'error': '요청 데이터가 없습니다.' }), 400)script = None.get('script', '')mode = data.get('mode', 'extract_speakers')speaker_balance = data.get('speaker_balance')default_speaker = data.get('default_speaker', '나레이션')if not script or script.strip():
(jsonify({
'success': False,
'error': '분석할 대본이 없습니다.' }), 400)service = None()result = service.analyze_and_convert(script, mode, speaker_balance = speaker_balance, default_speaker = default_speaker)if result['success']:
(jsonify(result), 200)(None(result), 500)except ValueError:
e = Nonedel eNoneNone = del eexcept Exception:
e = Noneprint(f'''[ScriptController] Error in analyze_script: {e}''')del eNoneNone = del e)()
