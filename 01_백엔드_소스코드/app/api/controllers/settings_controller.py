# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: settings_controller.pyc (Python 3.11)

"""
Settings Controller (Clean Architecture Version)

Handles settings and API key management.
Replaces v1 settings.py.

Registration in app/__init__.py:
    from app.api.controllers import settings_controller_bp
    app.register_blueprint(settings_controller_bp, url_prefix='/api')
"""
from flask import Blueprint, request, jsonify
import logging
from app import db
from app.models.settings import Settings
from app.services.automation_humanization import normalize_automation_humanization_settings
from app.services.google_auth_service import create_google_tts_client, resolve_google_auth_config
logger = logging.getLogger(__name__)
settings_controller_bp = Blueprint('settings', __name__)
_RUNTIME_DIAGNOSTICS_DISABLED_RESPONSE = {
    'error': 'Diagnostics tools are disabled.' }

def _classify_google_error(e = None):
    '''Google API 에러를 유형별로 분류하여 (error_type, user_message) 반환'''
    err_str = str(e).lower()
    if 'billing' in err_str and 'payment' in err_str and 'billing_disabled' in err_str or 'cloud billing' in err_str:
        return ('billing', '결제가 설정되지 않았습니다. Google Cloud 콘솔에서 결제를 활성화하세요.')
    if None in err_str and 'it is disabled' in err_str and 'service_disabled' in err_str or 'api not enabled' in err_str:
        return ('service_disabled', 'API가 비활성화되어 있습니다. Google Cloud 콘솔에서 해당 API를 활성화하세요.')
    if None in err_str and 'api_key_invalid' in err_str and 'invalid api key' in err_str or 'unauthenticated' in err_str:
        return ('auth', 'API 키가 유효하지 않습니다.')
    if None in err_str and 'permission denied' in err_str or 'forbidden' in err_str:
        return ('permission', '권한이 거부되었습니다. API 키 권한을 확인하세요.')
    if None in err_str or 'resource_exhausted' in err_str:
        return ('quota', '할당량이 초과되었습니다.')
    return (None, str(e))

get_settings = (lambda : try:
settings = Settings.get_or_create()(jsonify(settings.to_dict()), 200)except Exception:
e = Nonelogger.error(f'''Error getting settings: {e}''')del eNoneNone = del e)()
get_automation_humanization_settings = (lambda : try:
settings = Settings.get_or_create()(jsonify({
'automationHumanizationSettings': normalize_automation_humanization_settings(settings.automation_humanization_settings) }), 200)except Exception:
e = Nonelogger.error(f'''Error getting automation humanization settings: {e}''')del eNoneNone = del e)()
update_automation_humanization_settings = (lambda : try:
if not request.json:
data = { }raw_settings = data.get('automationHumanizationSettings') if isinstance(data.get('automationHumanizationSettings'), dict) else datanormalized = normalize_automation_humanization_settings(raw_settings)settings = Settings.get_or_create()settings.automation_humanization_settings = normalizeddb.session.commit()(jsonify({
'automationHumanizationSettings': normalized }), 200)except Exception:
e = Nonelogger.error(f'''Error updating automation humanization settings: {e}''')db.session.rollback()del eNoneNone = del e)()
get_runtime_diagnostics = (lambda : (jsonify(_RUNTIME_DIAGNOSTICS_DISABLED_RESPONSE), 404))()

def _is_valid_key(key = settings_controller_bp.route('/settings/automation-humanization', methods = [
    'GET'])):
    '''마스킹되지 않은 유효한 키인지 확인'''
    if not key:
        return False
    if None in key:
        return False

update_settings = (lambda : try:
data = request.jsonsettings = Settings.get_or_create()if 'apiKeys' in data:
api_keys = data['apiKeys']if 'openai' in api_keys and _is_valid_key(api_keys['openai']):
settings.openai_api_key = api_keys['openai']logger.info(f'''OpenAI key updated: {api_keys['openai'][:10]}***''')if 'google' in api_keys and _is_valid_key(api_keys['google']):
settings.google_api_key = api_keys['google']logger.info(f'''Google key updated: {api_keys['google'][:10]}***''')if 'claude' in api_keys and _is_valid_key(api_keys['claude']):
settings.claude_api_key = api_keys['claude']logger.info(f'''Claude key updated: {api_keys['claude'][:10]}***''')if 'typecast' in api_keys and _is_valid_key(api_keys['typecast']):
settings.typecast_api_key = api_keys['typecast']logger.info(f'''Typecast key updated: {api_keys['typecast'][:10]}***''')if 'elevenlabs' in api_keys and _is_valid_key(api_keys['elevenlabs']):
settings.elevenlabs_api_key = api_keys['elevenlabs']logger.info(f'''ElevenLabs key updated: {api_keys['elevenlabs'][:10]}***''')if 'nanobanana' in api_keys and _is_valid_key(api_keys['nanobanana']):
settings.nanobanana_api_key = api_keys['nanobanana']logger.info(f'''Nanobanana key updated: {api_keys['nanobanana'][:10]}***''')if 'generalSettings' in data:
gen_settings = data['generalSettings']if 'autoSave' in gen_settings:
settings.auto_save = gen_settings['autoSave']if 'notifications' in gen_settings:
settings.notifications = gen_settings['notifications']if 'language' in gen_settings:
settings.language = gen_settings['language']if 'claudeModel' in gen_settings:
settings.claude_model = gen_settings['claudeModel']if 'geminiModel' in gen_settings:
settings.gemini_model = gen_settings['geminiModel']if 'qwen3TtsEnabled' in gen_settings:
settings.qwen3_tts_enabled = gen_settings['qwen3TtsEnabled']logger.info(f'''Qwen3 TTS enabled: {gen_settings['qwen3TtsEnabled']}''')if 'automationHumanizationSettings' in data:
settings.automation_humanization_settings = normalize_automation_humanization_settings(data.get('automationHumanizationSettings'))if 'googleCloudSettings' in data:
gc_settings = data['googleCloudSettings']if 'projectId' in gc_settings:
settings.google_cloud_project_id = gc_settings['projectId']logger.info(f'''Google Cloud Project ID updated: {gc_settings['projectId']}''')if 'authMode' in gc_settings:
mode = gc_settings['authMode']if mode in ('api_key', 'vertex_ai'):
settings.google_auth_mode = modelogger.info(f'''Google auth mode updated: {mode}''')if 'vertexAiLocation' in gc_settings:
settings.vertex_ai_location = gc_settings['vertexAiLocation']logger.info(f'''Vertex AI location updated: {gc_settings['vertexAiLocation']}''')if 'youtubeSettings' in data:
yt_settings = data['youtubeSettings']credentials_changed = Falsehas_client_id = 'clientId' in yt_settingshas_client_secret = 'clientSecret' in yt_settingsif has_client_id:
passraw_client_id = str('').strip() if not yt_settings.get('clientId', '') else ''if has_client_secret:
passraw_client_secret = str('').strip() if not yt_settings.get('clientSecret', '') else ''valid_client_id = _is_valid_key(raw_client_id)valid_client_secret = _is_valid_key(raw_client_secret)if has_client_id and has_client_secret and valid_client_id != valid_client_secret:
(jsonify({
'error': 'YouTube 클라이언트 ID와 시크릿은 함께 업데이트해야 합니다.' }), 400)if None and has_client_secret and valid_client_id and valid_client_secret:
if settings.youtube_client_id != raw_client_id or settings.youtube_client_secret != raw_client_secret:
settings.youtube_client_id = raw_client_idsettings.youtube_client_secret = raw_client_secretcredentials_changed = Truelogger.info(f'''YouTube Client ID updated: {raw_client_id[:20]}***''')logger.info('YouTube Client Secret updated')if credentials_changed:
logger.info('YouTube client ID/secret updated without clearing existing YouTube account tokens (multi-account compatibility).')db.session.commit()try:
settings.save_to_env()logger.info('Settings saved to database and .env file')try:
passexcept Exception:
env_error = Nonelogger.warning(f'''Failed to save to .env file: {env_error}''')try:
env_error = Nonedel env_errorenv_error = Nonedel env_errortry:
(jsonify(settings.to_dict()), 200)except Exception:
e = Nonelogger.error(f'''Error updating settings: {e}''')db.session.rollback()del eNoneNone = del e)()
get_api_key = (lambda service: try:
db.session.expire_all()settings = Settings.get_or_create()api_key = settings.get_api_key(service)if not api_key:
(jsonify({
'error': f'''{service} API key not found''' }), 404)(None({
'apiKey': api_key }), 200)except Exception:
e = Nonelogger.error(f'''Error getting API key: {e}''')del eNoneNone = del e)()
test_connection = (lambda service: try:
db.session.expire_all()settings = Settings.get_or_create()if service == 'qwen3':
try:
Qwen3TTSService = Qwen3TTSServiceimport app.services.qwen3_tts_serviceresult = Qwen3TTSService.is_available()if result.get('available'):
gpu_info = f''' (GPU: {result.get('gpu_name')})''' if result.get('gpu_available') else ' (CPU 모드)'(jsonify({
'status': 'success',
'message': f'''Qwen3 TTS 사용 가능{gpu_info}''',
'details': result }), 200)(None({
'status': 'failed',
'message': result.get('message', 'Qwen3 TTS 패키지 미설치'),
'details': result }), 400)except ImportError:
ie = Nonelogger.error(f'''Qwen3 TTS import error: {ie}''')try:
del ieNoneNone = del ietry:
if service != 'google':
api_key = settings.get_api_key(service)if not api_key:
(jsonify({
'error': f'''{service} API key not found''' }), 404)if None, (jsonify({
'status': 'failed',
'message': 'Qwen3 TTS 서비스 로드 실패',
'error': str(ie) }), 400) == 'openai':
try:
OpenAI = OpenAIimport openaiclient = OpenAI(api_key = api_key)models = client.models.list()model_count = len(list(models))logger.info(f'''OpenAI connection successful, found {model_count} models''')(jsonify({
'status': 'success',
'message': f'''OpenAI 연결 성공 (모델 {model_count}개 확인)''' }), 200)except Exception:
openai_error = Nonelogger.error(f'''OpenAI test failed: {type(openai_error).__name__}: {openai_error}''')raise openai_erroropenai_error = Nonedel openai_errortry:
if service == 'google':
auth_config = resolve_google_auth_config(settings = settings)auth_mode = auth_config.auth_modechecks = []if not auth_config.validation.is_configured:
checks.append({
'service': 'google_auth',
'label': 'Google 인증 설정',
'status': 'failed',
'error_type': 'config',
'message': auth_config.validation.message })(jsonify({
'status': 'failed',
'authMode': auth_mode,
'missingFields': list(auth_config.validation.missing_fields),
'checks': checks,
'message': auth_config.validation.message }), 400)gemini_ok = Nonetry:
get_genai_client = get_genai_clientimport app.utils.google_sdkclient = get_genai_client()list(client.models.list())checks.append({
'service': 'gemini' if auth_mode == 'api_key' else 'vertex_ai',
'label': 'Google AI Studio (Gemini)' if auth_mode == 'api_key' else 'Vertex AI (서비스 계정)',
'status': 'success',
'message': '연결 성공' if auth_mode == 'api_key' else f'''연결 성공 (프로젝트: {auth_config.project_id}, 리전: {auth_config.location})''' })gemini_ok = Truetry:
passexcept Exception:
gemini_err = None(error_type, error_msg) = _classify_google_error(gemini_err)checks.append({
'service': 'gemini' if auth_mode == 'api_key' else 'vertex_ai',
'label': 'Google AI Studio (Gemini)' if auth_mode == 'api_key' else 'Vertex AI (서비스 계정)',
'status': 'failed',
'error_type': error_type,
'message': error_msg })try:
gemini_err = Nonedel gemini_errgemini_err = Nonedel gemini_errtry:
try:
texttospeech = texttospeech_v1import google.cloud(tts_client, _) = create_google_tts_client(texttospeech_module = texttospeech, settings = settings)tts_client.list_voices(request = {
'language_code': 'ko-KR' })checks.append({
'service': 'cloud_tts',
'label': 'Google Cloud TTS',
'status': 'success',
'message': '연결 성공' })try:
passexcept ImportError:
checks.append({
'service': 'cloud_tts',
'label': 'Google Cloud TTS',
'status': 'failed',
'error_type': 'library',
'message': 'google-cloud-texttospeech 라이브러리가 설치되지 않았습니다.' })try:
passexcept Exception:
tts_err = None(error_type, error_msg) = _classify_google_error(tts_err)checks.append({
'service': 'cloud_tts',
'label': 'Google Cloud TTS',
'status': 'failed',
'error_type': error_type,
'message': error_msg })try:
tts_err = Nonedel tts_errtts_err = Nonedel tts_errtry:
if gemini_ok:
(jsonify({
'status': 'success',
'authMode': auth_mode,
'missingFields': list(auth_config.validation.missing_fields),
'checks': checks,
'message': 'Google 연결 완료' }), 200)(None({
'status': 'failed',
'authMode': auth_mode,
'missingFields': list(auth_config.validation.missing_fields),
'checks': checks,
'message': 'Google 연결 실패' }), 400)try:
if service == 'claude':
Anthropic = Anthropicimport anthropicclient = Anthropic(api_key = api_key)message = client.messages.create(model = 'claude-sonnet-4-5-20250929', max_tokens = 10, messages = [
{
'role': 'user',
'content': 'test' }])(jsonify({
'status': 'success',
'message': 'Claude connection successful' }), 200)if None == 'typecast':
(jsonify({
'status': 'success',
'message': 'Typecast API key found' }), 200)if None == 'elevenlabs':
import requestsresponse = requests.get('https://api.elevenlabs.io/v2/voices?page_size=1', headers = {
'xi-api-key': api_key }, timeout = 10)if response.status_code >= 400:
detail_message = response.text[:500]error_type = 'unknown'try:
error_payload = response.json()detail = error_payload.get('detail', { }) if isinstance(error_payload, dict) else { }status = detail.get('status') if isinstance(detail, dict) else Nonemessage = detail.get('message') if isinstance(detail, dict) else Noneif message:
detail_message = messageif status == 'missing_permissions':
error_type = 'permission'elif response.status_code in (401, 403):
error_type = 'auth'elif response.status_code == 429:
error_type = 'quota'try:
passexcept Exception:
if response.status_code in (401, 403):
error_type = 'auth'elif response.status_code == 429:
error_type = 'quota'try:
passtry:
(jsonify({
'status': 'failed',
'message': f'''ElevenLabs connection failed ({response.status_code})''',
'error': detail_message,
'checks': [
{
'service': 'elevenlabs',
'label': 'ElevenLabs API',
'status': 'failed',
'error_type': error_type,
'message': 'API 키에 voices_read 권한이 없습니다. ElevenLabs 키 권한에서 voices_read를 허용해주세요.' if error_type == 'permission' else detail_message }] }), 400)try:
(jsonify({
'status': 'success',
'message': 'ElevenLabs connection successful',
'checks': [
{
'service': 'elevenlabs',
'label': 'ElevenLabs API',
'status': 'success',
'message': '연결 성공 (voices_read 권한 확인 완료)' }] }), 200)try:
(jsonify({
'error': f'''Unknown service: {service}''' }), 400)except Exception:
e = Nonelogger.error(f'''Connection test failed for {service}: {e}''')del eNoneNone = del e)()
get_version = (lambda : try:
import jsonget_base_path = get_base_pathimport app.config.pathsversion_file = get_base_path() / 'version.json'if version_file.exists():
f = open(version_file, 'r', encoding = 'utf-8')version_info = json.load(f)try:
None(None, None)with None:
if not None:
try:
try:
passversion_info = {
'version': '0.0.0-dev',
'name': 'TFstudio',
'cacheVersion': 0 }(jsonify(version_info), 200)except Exception:
e = Nonelogger.error(f'''Error getting version info: {e}''')del eNoneNone = del e)()
get_download_info = (lambda :
