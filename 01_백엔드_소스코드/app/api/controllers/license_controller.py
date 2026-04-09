# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: license_controller.pyc (Python 3.11)

"""
License Controller - 라이선스 인증 API

외부 사이트(tupastudio) 로그인 기반 프로그램 실행 제어.

Registration in app/__init__.py:
    from app.api.controllers import license_controller_bp
    app.register_blueprint(license_controller_bp, url_prefix='/api/license')
"""
from flask import Blueprint, request, jsonify
import logging
from app.services.license_service import LicenseService
from app.models.license import License
logger = logging.getLogger(__name__)
license_controller_bp = Blueprint('license', __name__)
login = (lambda : try:
if not request.json:
data = { }email = data.get('email', '').strip()password = data.get('password', '')remember_me = data.get('rememberMe', False)if not email or password:
(jsonify({
'success': False,
'error': '이메일과 비밀번호를 입력해주세요.',
'code': 'MISSING_CREDENTIALS' }), 400)result = None.authenticate(email, password)if result['success']:
if remember_me:
saved = LicenseService.save_credentials(email, password)if saved:
logger.info(f'''Credentials saved for {email}''')else:
LicenseService.clear_credentials()(jsonify(result), 200)status_code = 401 if None.get('code') in ('INVALID_CREDENTIALS', 'INVALID_EMAIL', 'INVALID_PASSWORD', 'NO_PASSWORD_SET') else 400(jsonify(result), status_code)except Exception:
e = Nonelogger.error(f'''Login error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
auto_login = (lambda : try:
credentials = LicenseService.load_credentials()if not credentials:
(jsonify({
'success': False,
'hasCredentials': False,
'error': '저장된 로그인 정보가 없습니다.',
'code': 'NO_SAVED_CREDENTIALS' }), 200)(email, password) = Noneresult = LicenseService.authenticate(email, password)result['hasCredentials'] = True(jsonify(result), 200)except Exception:
e = Nonelogger.error(f'''Auto-login error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
logout = (lambda : try:
result = LicenseService.logout()(jsonify(result), 200)except Exception:
e = Nonelogger.error(f'''Logout error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
get_status = (lambda : try:
license_obj = License.get_or_create()license_data = license_obj.to_dict() if license_obj.email else Noneif license_obj.email is not None:
is_authenticated = license_obj.is_valid()has_credentials = LicenseService.has_saved_credentials()(jsonify({
'success': True,
'license': license_data,
'isAuthenticated': is_authenticated,
'hasCredentials': has_credentials }), 200)except Exception:
e = Nonelogger.error(f'''Get status error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
refresh_status = (lambda : try:
result = LicenseService.check_subscription(force_refresh = True)(jsonify(result), 200)except Exception:
e = Nonelogger.error(f'''Refresh status error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
check_subscription = (lambda : try:
force_refresh = request.args.get('force', 'false').lower() == 'true'result = LicenseService.check_subscription(force_refresh = force_refresh)(jsonify(result), 200)except Exception:
e = Nonelogger.error(f'''Check subscription error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
validate_license = (lambda : try:
license_obj = License.get_or_create()if not license_obj.email:
(jsonify({
'valid': False,
'status': 'not_authenticated',
'daysRemaining': 0,
'unlimited': False,
'message': '로그인이 필요합니다.' }), 200)status = None.statusdays_remaining = license_obj.days_remainingunlimited = license_obj.unlimitedif unlimited:
message = '무제한 이용 가능합니다.'valid = Trueelif status == 'active' and days_remaining > 0:
message = f'''구독이 활성화되어 있습니다. (남은 기간: {days_remaining}일)'''valid = Trueelif status == 'expired':
message = '구독이 만료되었습니다. 갱신이 필요합니다.'valid = Falseelif status == 'none':
message = '구독 정보가 없습니다. 구독이 필요합니다.'valid = Falseelse:
message = '알 수 없는 상태입니다.'valid = False(jsonify({
'valid': valid,
'status': status,
'daysRemaining': days_remaining,
'unlimited': unlimited,
'message': message }), 200)except Exception:
e = Nonelogger.error(f'''Validate license error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
session_login = (lambda : try:
if not request.json:
data = { }email = data.get('email', '').strip()password = data.get('password', '')remember_me = data.get('rememberMe', False)if not email or password:
(jsonify({
'success': False,
'error': '이메일과 비밀번호를 입력해주세요.',
'code': 'MISSING_CREDENTIALS' }), 400)device_info = None.get_device_info()device_id = device_info['device_id']device_name = device_info['device_name']result = LicenseService.authenticate_with_session(email, password, device_id, device_name)if result['success']:
if remember_me:
saved = LicenseService.save_credentials(email, password)if saved:
logger.info(f'''Credentials saved for {email}''')else:
LicenseService.clear_credentials()result['device'] = {
'id': device_id,
'name': device_name }(jsonify(result), 200)if None.get('code') == 'SESSION_CONFLICT':
(jsonify(result), 409)if None.get('code') == 'NO_SUBSCRIPTION':
if remember_me:
saved = LicenseService.save_credentials(email, password)if saved:
logger.info(f'''Credentials saved for {email} (NO_SUBSCRIPTION)''')(jsonify(result), 400)status_code = 401 if None.get('code') in ('INVALID_CREDENTIALS', 'INVALID_EMAIL', 'INVALID_PASSWORD', 'NO_PASSWORD_SET') else 400(jsonify(result), status_code)except Exception:
e = Nonelogger.error(f'''Session login error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
kick_other_session = (lambda : try:
if not request.json:
data = { }email = data.get('email', '').strip()password = data.get('password', '')remember_me = data.get('rememberMe', False)if not email or password:
(jsonify({
'success': False,
'error': '이메일과 비밀번호를 입력해주세요.',
'code': 'MISSING_CREDENTIALS' }), 400)device_info = None.get_device_info()device_id = device_info['device_id']device_name = device_info['device_name']result = LicenseService.kick_other_session(email, password, device_id, device_name)if result['success']:
if remember_me:
LicenseService.save_credentials(email, password)else:
LicenseService.clear_credentials()result['device'] = {
'id': device_id,
'name': device_name }(jsonify(result), 200)status_code = 401 if None.get('code') == 'INVALID_CREDENTIALS' else 400(jsonify(result), status_code)except Exception:
e = Nonelogger.error(f'''Kick session error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
kick_other_session_auto = (lambda : try:
credentials = LicenseService.load_credentials()if not credentials:
(jsonify({
'success': False,
'error': '저장된 로그인 정보가 없습니다. 다시 로그인해주세요.',
'code': 'NO_CREDENTIALS' }), 400)(email, password) = Nonedevice_info = LicenseService.get_device_info()device_id = device_info['device_id']device_name = device_info['device_name']result = LicenseService.kick_other_session(email, password, device_id, device_name)if result['success']:
result['device'] = {
'id': device_id,
'name': device_name }(jsonify(result), 200)status_code = 401 if None.get('code') == 'INVALID_CREDENTIALS' else 400(jsonify(result), status_code)except Exception:
e = Nonelogger.error(f'''Kick session auto error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
session_heartbeat = (lambda : try:
if not request.json:
data = { }session_token = data.get('session_token', '')if not session_token:
license_obj = License.get_or_create()session_token = license_obj.session_tokenif not session_token:
(jsonify({
'success': False,
'valid': False,
'error': '세션 토큰이 없습니다.',
'code': 'NO_SESSION' }), 401)result = None.send_heartbeat(session_token)if result.get('kicked'):
license_obj = License.get_or_create()license_obj.clear_session()db = dbimport appdb.session.commit()(jsonify(result), 200)except Exception:
e = Nonelogger.error(f'''Heartbeat error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
session_logout = (lambda : try:
license_obj = License.get_or_create()session_token = license_obj.session_tokenif session_token:
LicenseService.logout_session(session_token)result = LicenseService.logout()(jsonify(result), 200)except Exception:
e = Nonelogger.error(f'''Session logout error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
session_auto_login = (lambda : try:
credentials = LicenseService.load_credentials()if not credentials:
(jsonify({
'success': False,
'hasCredentials': False }), 200)(email, password) = Nonedevice_info = LicenseService.get_device_info()device_id = device_info['device_id']device_name = device_info['device_name']result = LicenseService.authenticate_with_session(email, password, device_id, device_name)result['hasCredentials'] = Trueif result['success']:
result['device'] = {
'id': device_id,
'name': device_name }(jsonify(result), 200)if None.get('code') == 'SESSION_CONFLICT':
(jsonify(result), 409)(None(result), 401)except Exception:
e = Nonelogger.error(f'''Session auto-login error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
get_device_info = (lambda : try:
device_info = LicenseService.get_device_info()(jsonify(device_info), 200)except Exception:
e = Nonelogger.error(f'''Get device info error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
check_version = (lambda : try:
result = LicenseService.check_version()(jsonify(result), 200)except Exception:
e = Nonelogger.error(f'''Version check error: {type(e).__name__}: {str(e)}''')del eNoneNone = del e)()
