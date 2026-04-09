# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: server_controller.pyc (Python 3.11)

'''
서버 관리 API 엔드포인트

서버 상태 조회 및 재시작 기능을 제공합니다.
'''
from flask import Blueprint, jsonify, request
from app.services.server_service import ServerService
import logging
import time
import os
server_controller_bp = Blueprint('server', __name__)
logger = logging.getLogger(__name__)
get_server_status = (lambda : try:
server_info = ServerService.get_server_info()(jsonify(server_info), 200)except Exception:
e = Nonelogger.error(f'''Error getting server status: {e}''')del eNoneNone = del e)()
restart_server = (lambda : try:
logger.info('Server restart requested')ServerService.schedule_restart(delay = 0.5)(jsonify({
'status': 'success',
'message': 'Server restart initiated. Please wait for reconnection.' }), 200)except Exception:
e = Nonelogger.error(f'''Error restarting server: {e}''')del eNoneNone = del e)()
ping_server = (lambda : try:
(jsonify({
'timestamp': int(time.time() * 1000),
'status': 'ok' }), 200)except Exception:
e = Nonelogger.error(f'''Error in ping endpoint: {e}''')del eNoneNone = del e)()
kill_servers = (lambda target: try:
if target == 'backend':
count = ServerService.kill_backend_servers()elif target == 'frontend':
count = ServerService.kill_frontend_servers()elif target == 'all':
count = ServerService.kill_all_servers()else:
(jsonify({
'error': 'Invalid target. Use backend, frontend, or all' }), 400)(None({
'status': 'success',
'killed_count': count,
'message': f'''Killed {count} process(es)''' }), 200)except Exception:
e = Nonelogger.error(f'''Error killing {target} servers: {e}''')del eNoneNone = del e)()
start_servers = (lambda target: try:
if target == 'backend':
success = ServerService.start_backend()elif target == 'frontend':
success = ServerService.start_frontend()else:
(jsonify({
'error': 'Invalid target. Use backend or frontend' }), 400)if None:
(jsonify({
'status': 'success',
'message': f'''{target.capitalize()} server started''' }), 200)(None({
'error': f'''Failed to start {target}''' }), 500)except Exception:
e = Nonelogger.error(f'''Error starting {target} server: {e}''')del eNoneNone = del e)()
resolve_path = (lambda : try:
data = request.get_json()if not data or data.get('url'):
(jsonify({
'error': 'url is required' }), 400)url = None['url']url_clean = url.replace('\\', '/')if url_clean.startswith('/data/'):
url_clean = url_clean[6:]elif url_clean.startswith('data/'):
url_clean = url_clean[5:]if '?' in url_clean:
url_clean = url_clean.split('?')[0]get_data_path = get_data_pathimport app.config.pathsdata_dir = get_data_path()abs_path = os.path.normpath(os.path.join(str(data_dir), url_clean))data_dir_norm = os.path.normpath(str(data_dir))if not abs_path != data_dir_norm and abs_path.startswith(data_dir_norm + os.sep):
(jsonify({
'error': 'Invalid path' }), 400)if not None.path.exists(abs_path):
(jsonify({
'error': 'File not found' }), 404)(None({
'absolutePath': abs_path }), 200)except Exception:
e = Nonelogger.error(f'''Error resolving path: {e}''')del eNoneNone = del e)()
