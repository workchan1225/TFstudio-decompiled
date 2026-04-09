# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: auto_production_controller.pyc (Python 3.11)

'''
Auto Production Controller - 7개 API 엔드포인트

Blueprint: /api/auto-production
'''
from flask import Blueprint, Response, jsonify, request, stream_with_context
import logging
import json
import re
logger = logging.getLogger(__name__)
auto_production_bp = Blueprint('auto_production', __name__, url_prefix = '/api/auto-production')

def _extract_json(text = None):
    '''AI 응답에서 JSON 추출 (마크다운 코드블록, 불완전 JSON 처리)'''
    if not isinstance(text, str):
        return text
    cleaned = None.sub('```(?:json)?\\s*', '', text).strip()
    cleaned = cleaned.rstrip('`').strip()
    
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    match = re.search('\\{.*\\}', cleaned, re.DOTALL)
    if match:
        
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    candidate = match.group() if match else cleaned
    if candidate.count('"') % 2 != 0:
        candidate += '"'
    open_brackets = candidate.count('[') - candidate.count(']')
    open_braces = candidate.count('{') - candidate.count('}')
    candidate += ']' * max(0, open_brackets)
    candidate += '}' * max(0, open_braces)
    
    try:
        return json.loads(candidate)
    except json.JSONDecodeError:
        pass

    raise ValueError(f'''Failed to parse JSON from AI response: {text[:200]}''')


def _coerce_int(value = None, default = None):
    
    try:
        return int(value)
    except (TypeError, ValueError):
        return 


get_project_state = (lambda project_id = None: try:
AutoProductionProjectStateService = AutoProductionProjectStateServiceAutoProductionValidationError = AutoProductionValidationErrorimport app.services.auto_production.project_state_servicejsonify(AutoProductionProjectStateService.get_state(project_id))except AutoProductionValidationError:
exc = Nonedel excNoneNone = del excexcept Exception:
e = Nonelogger.error(f'''[AutoProd] State fetch error: {e}''', exc_info = True)del eNoneNone = del e)()
save_project_content = (lambda project_id = None: if not request.get_json():
data = { }try:
AutoProductionContentPayload = AutoProductionContentPayloadAutoProductionProjectStateService = AutoProductionProjectStateServiceAutoProductionValidationError = AutoProductionValidationErrorimport app.services.auto_production.project_state_serviceif not data.get('scenes'):
payload = AutoProductionContentPayload(topic = str(data.get('topic', '')), content_format = str(data.get('contentFormat', 'longform')), genre = str(data.get('genre', '')), tone = str(data.get('tone', '')), speaker_mode = str(data.get('speakerMode', 'single_narrator')), input_mode = str(data.get('inputMode', 'ai')), target_length = _coerce_int(data.get('targetLength'), 180), scenes = [])jsonify(AutoProductionProjectStateService.save_content(project_id, payload))except AutoProductionValidationError:
exc = _coerce_int(data.get('targetLength'), 180)del excNoneNone = del excexcept Exception:
e = str(data.get('inputMode', 'ai'))logger.error(f'''[AutoProd] Content save error: {e}''', exc_info = True)del eNoneNone = del e)()
save_project_scenario = (lambda project_id = None: if not request.get_json():
data = { }try:
AutoProductionConflictError = AutoProductionConflictErrorAutoProductionProjectStateService = AutoProductionProjectStateServiceAutoProductionScenarioPayload = AutoProductionScenarioPayloadAutoProductionValidationError = AutoProductionValidationErrorimport app.services.auto_production.project_state_serviceif not data.get('options') and data.get('scenes'):
payload = AutoProductionScenarioPayload(base_content_fingerprint = str(data.get('baseContentFingerprint', '')), options = [], selected_index = _coerce_int(data.get('selectedIndex'), -1), selected_scenario_id = str(data.get('selectedScenarioId', '')), scenes = [])jsonify(AutoProductionProjectStateService.save_scenario(project_id, payload))except AutoProductionConflictError:
exc = str(data.get('selectedScenarioId', ''))del excNoneNone = del excexcept AutoProductionValidationError:
exc = _coerce_int(data.get('selectedIndex'), -1)del excNoneNone = del excexcept Exception:
e = []logger.error(f'''[AutoProd] Scenario save error: {e}''', exc_info = True)del eNoneNone = del e)()
generate_script = (lambda : data = request.get_json()if not data:
(jsonify({
'error': 'Request body required' }), 400)topic = None.get('topic', '').strip()if not topic:
(jsonify({
'error': 'topic is required' }), 400)genre = None.get('genre', '')content_format = data.get('contentFormat', 'longform')target_length = data.get('targetLength', 180)tone = data.get('tone', '설명체')speaker_mode = data.get('speakerMode', 'single_narrator')speaker_instruction = '1인칭 나레이션 문체로 작성하세요. 화자 태그 없이 나레이션만 작성합니다.' if speaker_mode == 'single_narrator' else '다중 화자 대화 형식으로 작성하세요. 각 씬에 [MC], [전문가] 등 화자 태그를 포함합니다.'try:
get_ai_service = get_ai_serviceimport app.services.ai.provider_factoryai_service = get_ai_service('google')prompt = f'''다음 주제로 {content_format} 영상 대본을 작성하세요.\n\n주제: {topic}\n장르: {genre}\n톤/문체: {tone}\n화자 모드: {speaker_instruction}\n목표 길이: 약 {target_length}초\n\n## 출력 형식 (JSON):\n{{\n  "scenes": [\n    {{"order": 1, "text": "씬 1 나레이션 텍스트"}},\n    {{"order": 2, "text": "씬 2 나레이션 텍스트"}}\n  ]\n}}\n\n- 각 씬은 10~30초 분량 (2~5문장)\n- 자연스러운 한국어 나레이션 문체\n- 도입-전개-결말 구조\n- 반드시 유효한 JSON만 출력하세요.\n'''response = ai_service.generate_text(prompt = prompt, max_tokens = 8000, response_mime_type = 'application/json')result = _extract_json(response)scenes = result.get('scenes', [])for i, scene in enumerate(scenes):
scene['id'] = f'''scene-{i}'''scene.setdefault('order', i + 1)jsonify({
'success': True,
'scenes': scenes })except Exception:
e = Nonelogger.error(f'''[AutoProd] Script generation error: {e}''')del eNoneNone = del e)()
generate_scenarios = (lambda : data = request.get_json()if not data:
(jsonify({
'error': 'Request body required' }), 400)scenes = None.get('scenes', [])if not scenes:
(jsonify({
'error': 'scenes required' }), 400)genre = None.get('genre', '')content_format = data.get('contentFormat', 'longform')try:
gen_scenarios = generate_scenariosimport app.services.auto_production.scenario_generatorscenarios = gen_scenarios(scenes, genre, content_format)jsonify({
'success': True,
'scenarios': scenarios })except Exception:
e = Nonelogger.error(f'''[AutoProd] Scenario generation error: {e}''')del eNoneNone = del e)()
preview_tts = (lambda : data = request.get_json()if not data:
(jsonify({
'error': 'Request body required' }), 400)text = None.get('text', '').strip()engine = data.get('engine', 'edge')voice_name = data.get('voiceName', '')speaking_rate = data.get('speakingRate', 1)if not text:
(jsonify({
'error': 'text is required' }), 400)if not None:
(jsonify({
'error': 'voiceName is required' }), 400)try:
get_tts_engine = get_tts_engineimport app.services.tts.engine_factorytts_engine = get_tts_engine(engine)result = tts_engine.generate(text = text[:200], voice_name = voice_name, speed = speaking_rate, project_id = 'preview')audio_url = result.get('audio_path', '') if isinstance(result, dict) else ''duration = result.get('duration', 0) if isinstance(result, dict) else 0jsonify({
'audioUrl': audio_url,
'duration': duration })except Exception:
e = Nonelogger.error(f'''[AutoProd] TTS preview error: {e}''')del eNoneNone = del e)()
execute_production = (lambda : data = request.get_json()if not data:
(jsonify({
'error': 'Request body required' }), 400)try:
AutoProductionConfig = AutoProductionConfigimport app.services.auto_production.typesAutoProductionOrchestrator = AutoProductionOrchestratorimport app.services.auto_production.orchestratorconfig = AutoProductionConfig.from_request(data)orchestrator = AutoProductionOrchestrator()Response(stream_with_context(orchestrator.execute(config)), content_type = 'text/event-stream', headers = {
'Cache-Control': 'no-cache',
'X-Accel-Buffering': 'no',
'Connection': 'keep-alive' })except Exception:
e = Nonelogger.error(f'''[AutoProd] Execute error: {e}''')del eNoneNone = del e)()
cancel_production = (lambda : data = request.get_json()if not data:
(jsonify({
'error': 'Request body required' }), 400)task_id = None.get('taskId', '')if not task_id:
(jsonify({
'error': 'taskId is required' }), 400)cancellation_registry = cancellation_registryimport app.services.auto_production.cancellationsuccess = cancellation_registry.cancel_task(task_id)jsonify({
'success': success }))()
get_status = (lambda task_id = auto_production_bp.route('/execute', methods = [
    'POST']): ProgressService = ProgressServiceimport app.services.progress_serviceprogress_service = ProgressService()progress = progress_service.get_progress(task_id)# WARNING: Decompyle incomplete
)()
estimate_cost = (lambda : data = request.get_json()if not data:
(jsonify({
'error': 'Request body required' }), 400)scene_count = None.get('sceneCount', 0)tts_engine = data.get('ttsEngine', 'edge')model_type = data.get('modelType', 'standard')resolution = data.get('resolution', 'FHD')include_character = data.get('includeCharacterReference', True)tts_costs = {
'edge': 0,
'gemini-native': 0.5,
'elevenlabs': 1,
'chirp3hd': 0.8,
'supertonic': 0.6,
'googlecloud': 0.3 }image_costs = {
'standard': 1,
'nanobanana2': 1,
'pro': 3 }res_mult = {
'HD': 1,
'FHD': 1,
'2K': 1.5,
'4K': 2 }tts_total = scene_count * tts_costs.get(tts_engine, 0)image_total = scene_count * image_costs.get(model_type, 1) * res_mult.get(resolution, 1)char_extra = scene_count * 0.5 if include_character else 0time_per_scene = 18 if model_type == 'pro' else 13total_time = scene_count * time_per_scene + 10jsonify({
'success': True,
'estimate': {
'ttsCredits': tts_total,
'imageCredits': image_total + char_extra,
'totalCredits': tts_total + image_total + char_extra,
'estimatedTimeMinutes': max(1, round(total_time / 60)),
'breakdown': [
{
'label': 'TTS',
'count': scene_count,
'unitCost': tts_costs.get(tts_engine, 0),
'total': tts_total },
{
'label': '이미지',
'count': scene_count,
'unitCost': image_costs.get(model_type, 1),
'total': image_total }] } }))()
