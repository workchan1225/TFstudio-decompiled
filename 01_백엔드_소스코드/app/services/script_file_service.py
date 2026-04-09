# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_file_service.pyc (Python 3.11)

'''
스크립트 파일 관리 서비스

대본을 파일 시스템에 저장하고 관리합니다.
- Step 3 (대본 생성): script_v1.txt로 저장
- Step 4 (대본 확장): script_v2.txt, v3.txt... 버전 관리
'''
import re
from pathlib import Path
from app.utils.file_paths import ProjectPaths
from app.models.project import Project
from app import db
from datetime import datetime
from sqlalchemy.orm.attributes import flag_modified
import logging

def normalize_speaker_tags(script = None):
