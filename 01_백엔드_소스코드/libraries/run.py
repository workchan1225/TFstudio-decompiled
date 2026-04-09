# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: run.pyc (Python 3.11)

import os
import sys
import signal
import atexit
import logging
import threading
import time
from werkzeug.serving import WSGIRequestHandler
logger = logging.getLogger(__name__)
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
os.environ['TORCH_FORCE_WEIGHTS_ONLY_LOAD'] = '0'
os.environ['ORT_LOG_LEVEL'] = '3'

def patch_torch_serialization():
    '''torch.serialization 내부 함수 패치'''
    pass
# WARNING: Decompyle incomplete


def _is_truthy_env(value = None):
    return str(value).strip().lower() in frozenset({'1', 'on', 'yes', 'true'})

if _is_truthy_env(os.environ.get('TFSTUDIO_EAGER_TORCH_PATCH', '0')):
    patch_torch_serialization()
from app.config.runtime_config import apply_pending_data_path
if apply_pending_data_path():
    logger.info('Applied pending data path change')
from app import create_app
app = create_app()

try:
    REQUEST_TIMEOUT_SECONDS = max(14400, int(os.environ.get('TFSTUDIO_REQUEST_TIMEOUT_SEC', '43200')))
except ValueError:
    REQUEST_TIMEOUT_SECONDS = 43200


class CustomRequestHandler(WSGIRequestHandler):
    '''Flask 개발 서버의 요청 타임아웃을 확장 설정

    2시간 이상 걸리는 TTS 생성 및 영상 렌더링 작업을 위해
    충분한 타임아웃 값을 설정합니다.
    '''
    timeout = REQUEST_TIMEOUT_SECONDS


def cleanup_ffmpeg_processes():
    '''서버 종료 시 모든 FFmpeg 프로세스 정리 (자식 프로세스 포함)'''
    pass
# WARNING: Decompyle incomplete


def signal_handler(signum, frame):
    '''시그널 핸들러 - 서버 종료 시 cleanup 실행'''
    logger.info(f'''Received signal {signum}, cleaning up...''')
    cleanup_ffmpeg_processes()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
atexit.register(cleanup_ffmpeg_processes)
if __name__ == '__main__':
    
    try:
        logger.info('Starting Flask server...')
        logger.info(f'''Request timeout set to {REQUEST_TIMEOUT_SECONDS} seconds ({REQUEST_TIMEOUT_SECONDS / 3600:.1f} hours)''')
        SERVER_START_TIME = time.time()
        app.config['SERVER_START_TIME'] = SERVER_START_TIME
        logger.info(f'''Server start time: {SERVER_START_TIME}''')
        if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
            app.app_context()
            from app.services.sync_service import SyncService
            result = SyncService.initialize_project_thumbnails()
            logger.info(f'''Thumbnail initialization: {result}''')
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            app.run(debug = True, host = '127.0.0.1', port = 5000, request_handler = CustomRequestHandler)
                            return None
                        except KeyboardInterrupt:
                            logger.info('Server interrupted by user')
                            cleanup_ffmpeg_processes()
                            return None
                            except Exception:
                                e = None
                                logger.error(f'''Server error: {e}''')
                                cleanup_ffmpeg_processes()
                                raise 
                                e = None
                                del e
                            return None
