# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: diagnostics_controller.pyc (Python 3.11)

'''개발자 진단 API 컨트롤러.

설정 화면에서 기능을 내린 상태라 전체 엔드포인트를 비활성화한다.
'''
import logging
from flask import Blueprint, jsonify, request
logger = logging.getLogger(__name__)
diagnostics_bp = Blueprint('diagnostics', __name__)
_DIAGNOSTICS_DISABLED_RESPONSE = {
    'error': 'Diagnostics tools are disabled.' }
_ADMIN_EMAILS = frozenset({
    'dnal6149@naver.com'})
_block_disabled_diagnostics = (lambda : (jsonify(_DIAGNOSTICS_DISABLED_RESPONSE), 404))()

def _is_admin_request():
    '''요청의 X-User-Email 헤더로 관리자 여부 확인.'''
    email = request.headers.get('X-User-Email', '').strip().lower()
    return email in _ADMIN_EMAILS


def _require_admin():
    '''관리자가 아니면 403 반환.'''
    if not _is_admin_request():
        return (jsonify({
            'error': 'Unauthorized' }), 403)

diag_env = (lambda : denied = _require_admin()if denied:
deniedtry:
collect_runtime_diagnostics = collect_runtime_diagnosticsimport app.services.runtime_diagnostics_servicediag = collect_runtime_diagnostics()diag['apiKeys'] = _collect_api_key_info()diag['featureFlags'] = _collect_feature_flags()(jsonify(diag), 200)except Exception:
e = Nonelogger.error(f'''[Diagnostics] env error: {e}''')del eNoneNone = del e)()
diag_tts_status = (lambda : denied = _require_admin()if denied:
deniedtry:
Settings = Settingsimport app.models.settingsis_google_ai_configured = is_google_ai_configuredimport app.services.google_auth_serviceSUPPORTED_ENGINES = SUPPORTED_ENGINESget_engine_config = get_engine_configimport app.services.tts.engine_factorysettings = Settings.get_or_create()engine_key_map = {
'chirp3hd': 'google_api_key',
'edge': None,
'googlecloud': 'google_api_key',
'gemini-native': 'google_api_key',
'elevenlabs': 'elevenlabs_api_key',
'supertonic': None }results = []for engine in SUPPORTED_ENGINES:
config = get_engine_config(engine)key_attr = engine_key_map.get(engine)if key_attr == 'google_api_key':
has_key = is_google_ai_configured(settings = settings)elif key_attr:
passhas_key = Trueresults.append({
'engine': engine,
'format': config['audio_format'],
'sampleRate': config['sample_rate'],
'streaming': config.get('supports_streaming', False),
'requiresKey': bool(key_attr),
'keySet': has_key if key_attr else None,
'ready': has_key })(jsonify(results), 200)except Exception:
e = Nonelogger.error(f'''[Diagnostics] tts-status error: {e}''')del eNoneNone = del e)()
diag_projects = (lambda : denied = _require_admin()if denied:
deniedtry:
Character = CharacterProject = Projectimport app.models.projectprojects = Project.query.order_by(Project.created_at.desc()).limit(50).all()data = projects()total = Project.query.count()stats = {
'total': total,
'byStatus': {
'draft': Project.query.filter_by(status = 'draft').count(),
'in-progress': Project.query.filter_by(status = 'in-progress').count(),
'completed': Project.query.filter_by(status = 'completed').count() },
'totalCharacters': Character.query.count() }(jsonify({
'projects': data,
'stats': stats }), 200)except Exception:
e = Nonelogger.error(f'''[Diagnostics] projects error: {e}''')del eNoneNone = del e)()
diag_project_health = (lambda project_id: denied = _require_admin()if denied:
deniedtry:
_check_project_health = _check_project_healthimport app.cli.commands.debugget_data_path = get_data_pathimport app.config.pathsProject = Projectimport app.models.projectproject = Project.query.get(project_id)if not project:
(jsonify({
'error': f'''Project not found: {project_id}''' }), 404)issues = _check_project_health(project, 'all')(project.title({
'projectId': issues,
'title': None,
'issues': sum,
'totalIssues': (lambda .0: pass# WARNING: Decompyle incomplete
)(issues.values()()) }), 200)
    except Exception:
        e = None
        logger.error(f'''[Diagnostics] project-health error: {e}''')
        del e
        return None
        None = 
        del e

)()
diag_project_health_summary = (lambda : denied = _require_admin()if denied:
deniedtry:
_check_project_health = _check_project_healthimport app.cli.commands.debugProject = Projectimport app.models.projectprojects = Project.query.all()summaries = []for proj in projects:
issues = _check_project_health(proj, 'all')total_issues = (lambda .0: pass# WARNING: Decompyle incomplete
)(issues.values()())
            summaries.append({
                'id': proj.id,
                'title': proj.title,
                'issues': total_issues })
            return (jsonify(summaries), 200)
            except Exception:
                e = None
                logger.error(f'''[Diagnostics] project-health-summary error: {e}''')
                del e
                return None
                None = 
                del e

)()
diag_db_inspect = (lambda project_id:
