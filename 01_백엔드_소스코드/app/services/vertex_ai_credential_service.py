# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vertex_ai_credential_service.pyc (Python 3.11)

'''
Vertex AI 서비스 계정 자격 증명 관리 서비스

서비스 계정 JSON 파일의 검증, 저장, 삭제를 담당합니다.
'''
import json
import logging
import os
import shutil
from pathlib import Path
from typing import Optional
from app.config.paths import get_data_path
logger = logging.getLogger(__name__)
REQUIRED_FIELDS = {
    'type',
    'project_id',
    'private_key',
    'client_email'}
CREDENTIALS_DIR_NAME = 'credentials'

def _get_credentials_dir():
    '''자격 증명 저장 디렉토리 경로 반환'''
    cred_dir = get_data_path() / CREDENTIALS_DIR_NAME
    cred_dir.mkdir(parents = True, exist_ok = True)
    return cred_dir


def validate_service_account_json(data = None):
    '''서비스 계정 JSON 데이터 유효성 검증

    Args:
        data: 파싱된 JSON 딕셔너리

    Returns:
        유효하면 True

    Raises:
        ValueError: 필수 필드 누락 또는 잘못된 형식
    '''
    if not isinstance(data, dict):
        raise ValueError('유효한 JSON 객체가 아닙니다.')
    missing = REQUIRED_FIELDS - set(data.keys())
    if missing:
        raise ValueError(f'''필수 필드가 누락되었습니다: {', '.join(sorted(missing))}''')
    if data.get('type') != 'service_account':
        raise ValueError(f'''type 필드가 "service_account"이어야 합니다. (현재: {data.get('type')})''')
    if not data.get('private_key', '').startswith('-----BEGIN'):
        raise ValueError('private_key 형식이 올바르지 않습니다.')
    if '@' not in data.get('client_email', ''):
        raise ValueError('client_email 형식이 올바르지 않습니다.')
    return True


def save_credential_file(file_content = None, filename = None):
    '''서비스 계정 JSON 파일을 안전하게 저장

    Args:
        file_content: JSON 파일 바이너리 내용
        filename: 원본 파일명

    Returns:
        저장된 파일의 절대 경로 (forward slash)

    Raises:
        ValueError: JSON 파싱 실패 또는 검증 실패
    '''
    
    try:
        data = json.loads(file_content.decode('utf-8'))
    except (json.JSONDecodeError, UnicodeDecodeError):
        e = None
        raise ValueError(f'''JSON 파일을 파싱할 수 없습니다: {e}''')
        e = None
        del e

    validate_service_account_json(data)
    cred_dir = _get_credentials_dir()
    for existing in cred_dir.glob('service-account-*.json'):
        existing.unlink()
        logger.info(f'''[VertexAI] Removed old credential: {existing.name}''')
        except OSError:
            e = None
            logger.warning(f'''[VertexAI] Failed to remove old credential: {e}''')
            e = None
            del e
            continue
            e = None
            del e
        safe_name = f'''service-account-{os.path.basename(filename)}'''
        dest_path = cred_dir / safe_name
        f = open(dest_path, 'w', encoding = 'utf-8')
        json.dump(data, f, indent = 2)
        None(None, None)
    with None:
        if not None:
            pass
    saved_path = str(dest_path).replace('\\', '/')
    logger.info(f'''[VertexAI] Credential saved: {safe_name} (project: {data.get('project_id')})''')
    return saved_path


def delete_credential_file(path = None):
    '''자격 증명 파일 삭제

    Args:
        path: 삭제할 파일 경로

    Returns:
        삭제 성공 여부
    '''
    if not path:
        return False
    file_path = None(path)
    if not file_path.exists():
        logger.warning(f'''[VertexAI] Credential file not found: {path}''')
        return False
    cred_dir = None()
    
    try:
        file_path.resolve().relative_to(cred_dir.resolve())
    except ValueError:
        logger.error(f'''[VertexAI] Refusing to delete file outside credentials dir: {path}''')
        return False

    
    try:
        file_path.unlink()
        logger.info(f'''[VertexAI] Credential deleted: {path}''')
        return True
    except OSError:
        e = None
        logger.error(f'''[VertexAI] Failed to delete credential: {e}''')
        e = None
        del e
        return False
        e = None
        del e



def get_credential_info(path = None):
    '''자격 증명 파일에서 안전한 정보만 추출

    Args:
        path: JSON 파일 경로

    Returns:
        project_id, client_email 등 비민감 정보 딕셔너리, 없으면 None
    '''
    if not path:
        return None
    file_path = None(path)
    if not file_path.exists():
        return None
    
    try:
        f = open(file_path, 'r', encoding = 'utf-8')
        data = json.load(f)
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        return {
                            'projectId': data.get('project_id', ''),
                            'clientEmail': data.get('client_email', ''),
                            'type': data.get('type', ''),
                            'fileName': file_path.name }
                    except Exception:
                        e = None
                        logger.error(f'''[VertexAI] Failed to read credential info: {e}''')
                        e = None
                        del e
                        return None
                        e = None
                        del e
