# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: license_service.pyc (Python 3.11)

'''
License Service - 라이선스 인증 및 구독 상태 관리 서비스
외부 API (tupastudio)와 연동하여 인증 및 구독 확인
'''
import json
import requests
import time
import logging
from typing import Optional, Tuple, Dict, Any
from datetime import datetime
logger = logging.getLogger(__name__)
KEYRING_SERVICE = 'TFstudio'
KEYRING_EMAIL_KEY = 'license_email'
KEYRING_PASSWORD_KEY = 'license_password'

class LicenseService:
    '''라이선스 서비스'''
    API_URL = 'https://second.moducalc.com/api/tupastudio/auth'
    SESSION_API_URL = 'https://second.moducalc.com/api/tupastudio/session'
    CACHE_HOURS = 24
    MAX_RETRIES = 3
    TIMEOUT = 10
    authenticate = (lambda email = None, password = None: db = dbimport appLicense = Licenseimport app.models.licenseif not email or password:
{
'success': False,
'error': '이메일과 비밀번호를 입력해주세요.',
'code': 'MISSING_CREDENTIALS' }for attempt in None(LicenseService.MAX_RETRIES):
response = requests.post(LicenseService.API_URL, json = {
'email': email.strip(),
'password': password }, headers = {
'Content-Type': 'application/json' }, timeout = LicenseService.TIMEOUT)data = response.json()None if response.status_code == 200 and data.get('success') else None, {
'success': True,
'license': license_obj.to_dict(),
'error': None,
'code': None }if response.status_code == 400:
None, {
'success': False,
'error': data.get('error', '잘못된 요청입니다.'),
'code': 'BAD_REQUEST' }if None.status_code == 401:
if '등록되지 않은 이메일' in error_msg:
'INVALID_EMAIL' = data.get('error', '인증에 실패했습니다.')elif '비밀번호가 올바르지 않습니다' in error_msg:
code = 'INVALID_PASSWORD'elif '비밀번호가 설정되지 않았습니다' in error_msg:
code = 'NO_PASSWORD_SET'error_msg = '이 계정은 소셜 로그인으로 가입되었습니다.\n웹사이트에서 비밀번호를 설정해주세요.'else:
code = 'INVALID_CREDENTIALS'data.get('error', '인증에 실패했습니다.'), {
'success': False,
'error': error_msg,
'code': code }if None.status_code >= 500:
if attempt < LicenseService.MAX_RETRIES - 1:
time.sleep(2 ** attempt)continueNone, {
'success': False,
'error': '서버 오류가 발생했습니다. 잠시 후 다시 시도해주세요.',
'code': 'SERVER_ERROR' }None, {
'success': None,
'error': data.get('error', f'''알 수 없는 오류 (HTTP {response.status_code})'''),
'code': 'UNKNOWN_ERROR' }except requests.exceptions.Timeout:
if attempt < LicenseService.MAX_RETRIES - 1:
time.sleep(2 ** attempt)continueNone, {
'success': False,
'error': '서버 응답 시간이 초과되었습니다.',
'code': 'TIMEOUT' }, except requests.exceptions.ConnectionError:
if attempt < LicenseService.MAX_RETRIES - 1:
time.sleep(2 ** attempt)continueNone, {
'success': False,
'error': '서버에 연결할 수 없습니다.\n인터넷 연결을 확인해주세요.',
'code': 'NETWORK_ERROR' }, except requests.exceptions.JSONDecodeError:
None, {
'success': False,
'error': '서버 응답을 처리할 수 없습니다.',
'code': 'PARSE_ERROR' }, except Exception:
logger.error(f'''License authentication error: {type(e).__name__}: {str(e)}''')del e, Nonedel e{
'success': False,
'error': '최대 재시도 횟수를 초과했습니다.',
'code': 'MAX_RETRIES_EXCEEDED' })()
    check_subscription = (lambda force_refresh = None:
