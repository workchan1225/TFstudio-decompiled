# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: server_service.pyc (Python 3.11)

'''
서버 관리 서비스

서버 상태 정보 수집 및 재시작 기능을 제공합니다.
'''
import os
import sys
import time
import threading
import logging
from pathlib import Path
from flask import current_app
logger = logging.getLogger(__name__)

class ServerService:
    '''서버 관리 서비스'''
    _backend_process = None
    _frontend_process = None
    get_server_info = (lambda : try:
import psutilexcept ImportError:
logger.warning('psutil not available, returning limited server info')try:
time.time() - server_start_time = current_app.config.get('SERVER_START_TIME', time.time())python_version = sys.version.split()[0]memory = psutil.virtual_memory()memory_usage = {
'used': memory.used,
'total': memory.total,
'percent': memory.percent }cpu_percent = psutil.cpu_percent(interval = 0.1)try:
process_manager = process_managerimport app.utils.process_manageractive_projects = len(process_manager.get_active_projects())try:
passexcept Exception:
e = Nonelogger.warning(f'''Failed to get active projects: {e}''')active_projects = 0try:
e = Nonedel ee = Nonedel etry:
try:
ffmpeg_instances = ffmpeg_instancesimport app.api.controllers.project_controllerffmpeg_processes = len(ffmpeg_instances)try:
passexcept Exception:
e = Nonelogger.warning(f'''Failed to get FFmpeg processes: {e}''')ffmpeg_processes = 0try:
e = Nonedel ee = Nonedel etry:
urls = {
'frontend': 'http://localhost:5173',
'backend': 'http://localhost:5000' }{
'uptime': uptime,
'python_version': python_version,
'memory_usage': memory_usage,
'cpu_percent': cpu_percent,
'active_projects': active_projects,
'ffmpeg_processes': ffmpeg_processes,
'urls': urls }except Exception:
e = Nonelogger.error(f'''Error collecting server info: {e}''')del eNoneNone = del e)()
    schedule_restart = (lambda delay = (0.5,): pass# WARNING: Decompyle incomplete
)()
    kill_processes_on_port = (lambda port, process_name = (None,): try:
import psutilexcept ImportError:
logger.warning('psutil not available')0killed_count = 0try:
for proc in psutil.process_iter([
'pid',
'name']):
if process_name and process_name.lower() not in proc.info['name'].lower():
try:
continueconnections = proc.connections()if connections:
for conn in connections:
if hasattr(conn, 'laddr') and conn.laddr.port == port:
logger.info(f'''Killing process {proc.info['name']} (PID: {proc.info['pid']}) on port {port}''')proc.kill()killed_count += 1try:
continueexcept (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
try:
continuetry:
logger.info(f'''Killed {killed_count} process(es) on port {port}''')killed_countexcept Exception:
e = Nonelogger.error(f'''Error killing processes on port {port}: {e}''')e = Nonedel e0e = Nonedel e)()
    kill_backend_servers = (lambda : ServerService.kill_processes_on_port(5000, 'python'))()
    kill_frontend_servers = (lambda : ServerService.kill_processes_on_port(5173, 'node'))()
    kill_all_servers = (lambda : backend_count = ServerService.kill_backend_servers()frontend_count = ServerService.kill_frontend_servers()backend_count + frontend_count)()
    stop_backend_process = (lambda : pass# WARNING: Decompyle incomplete
)()
    stop_frontend_process = (lambda : pass# WARNING: Decompyle incomplete
)()
    cleanup_all_processes = (lambda :
