# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_service.pyc (Python 3.11)

'''
ScriptService - 스크립트 파일 관리 서비스
'''
import os
import re
from pathlib import Path
from typing import Dict, Any, Optional
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from sqlalchemy.orm.attributes import flag_modified
from app.models.project import Project
from app.utils.file_paths import ProjectPaths
from app.utils.speaker_normalizer import canonicalize_speaker_name, is_likely_metadata_speaker_label
from app import db

def repair_broken_chapter_markers(script = None):
    '''
    깨진 챕터 마커를 복구합니다.

    지원 복구 형식:
    - [챕터1]: 제목  -> [챕터 1: 제목]
    - [chapter2]: title -> [chapter 2: title]
    - [1장]: 제목 -> [1장: 제목]
    - [챕터1: 제목] -> [챕터 1: 제목] (공백 정리)
    '''
    pass
# WARNING: Decompyle incomplete


def merge_speaker_tag_only_lines(script = None):
    '''
    [화자]: 단독 줄 + 다음 대사 줄 패턴을 [화자]: 대사 한 줄로 병합
    '''
    pass
# WARNING: Decompyle incomplete


def normalize_speaker_tags(script = None):
    '''
    화자 태그 정규화: [AI
아
테
나] → [AI 아테나]
    대괄호 안의 줄바꿈을 공백으로 치환하고 여러 공백을 하나로 정리

    추가 처리:
    - [
화자명]: → [화자명]: (줄바꿈으로 분리된 태그 복구)
    - [화자명: → [화자명]: (닫는 괄호 누락 수정)
    - 줄 중간의 [화자명: 도 복구
    - 인라인 화자 태그를 줄 시작으로 분리
    '''
    pass
# WARNING: Decompyle incomplete


class ScriptService:
    '''
    스크립트 파일 관리 서비스

    책임:
    - 스크립트 파일 업로드
    - 스크립트 텍스트 저장
    - 기존 스크립트 파일 정리
    - 진행 상태 업데이트
    '''
    upload_script = (lambda project = None, file = None, text = staticmethod: pass# WARNING: Decompyle incomplete
)()
    _clear_existing_scripts = (lambda paths = None: scripts_dir = paths.scripts_dir()if scripts_dir.exists():
for old_file in scripts_dir.glob('*'):
if old_file.is_file():
os.remove(old_file)print(f'''[ScriptService] Deleted old script: {old_file}''')continueexcept Exception:
e = Noneprint(f'''[ScriptService] Error deleting old script {old_file}: {e}''')e = Nonedel econtinuee = Nonedel eNoneNone)()
    _handle_file_upload = (lambda project = None, file = None, paths = staticmethod:
