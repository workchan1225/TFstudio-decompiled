# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shorts_v2_controller.pyc (Python 3.11)

"""
Shorts V2 Controller - 문장 기반 쇼츠 생성 API

Registration in app/__init__.py:
    from app.api.controllers import shorts_v2_controller_bp
    app.register_blueprint(shorts_v2_controller_bp, url_prefix='/api/projects')

Endpoints:
- POST /<project_id>/shorts-v2/index-sentences - 자막에서 문장 인덱스 추출
- GET /<project_id>/shorts-v2/draft - 저장된 드래프트 로드
- POST /<project_id>/shorts-v2/save-draft - 드래프트 저장
- POST /<project_id>/shorts-v2/render - 쇼츠 렌더링 시작
- GET /<project_id>/shorts-v2/jobs/<job_id> - 작업 상태 조회
- GET /<project_id>/shorts-v2/outputs - 생성된 쇼츠 목록
- DELETE /<project_id>/shorts-v2/outputs/<output_id> - 쇼츠 삭제
- POST /<project_id>/shorts-v2/plan-ai - AI 컷 플랜 생성
- POST /<project_id>/shorts-v2/validate-plan - 플랜 검증
"""
from flask import Blueprint, request, jsonify
import logging
import threading
import time
from typing import Optional, Dict, Any
from app.models.project import Project
from app.config.feature_flags import FeatureFlags
shorts_v2_controller_bp = Blueprint('shorts_v2', __name__)
logger = logging.getLogger(__name__)
_job_progress: Dict[(str, Dict[(str, Any)])] = { }
_job_progress_timestamps: Dict[(str, float)] = { }
_job_progress_lock = threading.Lock()
_JOB_PROGRESS_TTL_SECONDS = 1800
_JOB_PROGRESS_MAX_ENTRIES = 500

def _cleanup_job_progress(now = None):
    '''만료된 작업 진행상황 정리'''
    pass
# WARNING: Decompyle incomplete


def _set_job_progress(job_id = None, payload = None):
    '''작업 진행상황 설정'''
    _job_progress_lock
    _cleanup_job_progress()
    _job_progress[job_id] = payload
    _job_progress_timestamps[job_id] = time.time()
    None(None, None)
    return None
    with None:
        if not None:
            pass


def _update_job_progress(job_id = None, updates = None):
    '''작업 진행상황 업데이트'''
    _job_progress_lock
    existing = _job_progress.get(job_id)
# WARNING: Decompyle incomplete


def _get_job_progress(job_id = None):
    '''작업 진행상황 조회'''
    _job_progress_lock
    _cleanup_job_progress()
    payload = _job_progress.get(job_id)
# WARNING: Decompyle incomplete


def _check_feature_enabled():
    '''Feature flag 확인'''
    if not FeatureFlags.is_enabled('SHORTS_V2_ENABLED'):
        return (jsonify({
            'error': 'Shorts V2 기능이 비활성화되어 있습니다.',
            'errorCode': 'FEATURE_DISABLED' }), 403)


def _get_project_or_404(project_id = None):
    '''프로젝트 조회 또는 404'''
    project = Project.query.get(project_id)
    if not project:
        return (None, (jsonify({
            'error': 'Project not found' }), 404))
    return (None, None)

index_sentences = (lambda project_id = None: feature_check = _check_feature_enabled()if feature_check:
feature_check(project, error) = None(project_id)if error:
errortry:
get_shorts_v2_service = get_shorts_v2_serviceimport app.services.shorts_v2_serviceservice = get_shorts_v2_service(project)(sentences, source_hash) = service.index_sentences()jsonify({
'success': True,
'sentences': sentences,
'sourceHash': source_hash })except Exception:
e = Nonelogger.error(f'''[ShortsV2] index_sentences failed: {e}''', exc_info = True)del eNoneNone = del e)()
get_draft = (lambda project_id = None: feature_check = _check_feature_enabled()if feature_check:
feature_check(project, error) = None(project_id)if error:
errortry:
get_shorts_v2_service = get_shorts_v2_serviceimport app.services.shorts_v2_serviceservice = get_shorts_v2_service(project)if not project.shorts_data:
shorts_data = { }jsonify({
'success': True,
'draft': service.load_draft(),
'aiPlan': shorts_data.get('aiPlan'),
'sentences': shorts_data.get('sentenceIndex', []),
'sourceHash': shorts_data.get('source', { }).get('sourceHash') })except Exception:
e = Nonelogger.error(f'''[ShortsV2] get_draft failed: {e}''', exc_info = True)del eNoneNone = del e)()
save_draft = (lambda project_id = None: feature_check = _check_feature_enabled()if feature_check:
feature_check(project, error) = None(project_id)if error:
errorif not None.get_json():
data = { }draft_data = data.get('draft', { })if not draft_data:
(jsonify({
'success': False,
'error': 'draft 데이터가 필요합니다.' }), 400)try:
get_shorts_v2_service = get_shorts_v2_serviceimport app.services.shorts_v2_serviceservice = get_shorts_v2_service(project)selected_ids = draft_data.get('selectedSentenceIds', [])clips = draft_data.get('clips', [])settings = draft_data.get('settings', { })selected_candidate_id = draft_data.get('selectedCandidateId')saved_draft = service.save_draft(selected_ids, clips, settings, selected_candidate_id = selected_candidate_id)jsonify({
'success': True,
'draft': saved_draft })except Exception:
e = Nonelogger.error(f'''[ShortsV2] save_draft failed: {e}''', exc_info = True)del eNoneNone = del e)()
render_shorts = (lambda project_id = None: pass# WARNING: Decompyle incomplete
)()
get_job_status = (lambda project_id = None, job_id = None: feature_check = _check_feature_enabled()if feature_check:
feature_checkprogress = None(job_id)# WARNING: Decompyle incomplete
)()
get_outputs = (lambda project_id = None: feature_check = _check_feature_enabled()if feature_check:
feature_check(project, error) = None(project_id)if error:
errortry:
get_shorts_v2_service = get_shorts_v2_serviceimport app.services.shorts_v2_serviceservice = get_shorts_v2_service(project)outputs = service.get_outputs()source_info = service.get_source_info()jsonify({
'success': True,
'outputs': outputs,
'sourceInfo': source_info })except Exception:
e = Nonelogger.error(f'''[ShortsV2] get_outputs failed: {e}''', exc_info = True)del eNoneNone = del e)()
delete_output = (lambda project_id = None, output_id = None: feature_check = _check_feature_enabled()if feature_check:
feature_check(project, error) = None(project_id)if error:
errortry:
get_shorts_v2_service = get_shorts_v2_serviceimport app.services.shorts_v2_serviceservice = get_shorts_v2_service(project)deleted = service.delete_output(output_id)jsonify({
'success': deleted })except Exception:
e = Nonelogger.error(f'''[ShortsV2] delete_output failed: {e}''', exc_info = True)del eNoneNone = del e)()
plan_ai = (lambda project_id = None: pass# WARNING: Decompyle incomplete
)()
validate_plan = (lambda project_id = None: feature_check = _check_feature_enabled()if feature_check:
feature_check(project, error) = None(project_id)if error:
errorif not None.get_json():
data = { }clips = data.get('clips', [])auto_fix = data.get('autoFix', False)try:
get_shorts_v2_service = get_shorts_v2_serviceimport app.services.shorts_v2_serviceservice = get_shorts_v2_service(project)if not project.shorts_data:
shorts_data = { }sentences = shorts_data.get('sentenceIndex', [])result = service.validate_plan(clips, sentences)if auto_fix and result.get('adjustedClips'):
result['fixedClips'] = result.get('adjustedClips')jsonify(result)except Exception:
e = Nonelogger.error(f'''[ShortsV2] validate_plan failed: {e}''', exc_info = True)del eNoneNone = del e)()
