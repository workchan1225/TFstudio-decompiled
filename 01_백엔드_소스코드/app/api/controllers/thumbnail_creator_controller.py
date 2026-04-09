# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: thumbnail_creator_controller.pyc (Python 3.11)

'''
Thumbnail Creator Controller
직접 생성 모달용 API 엔드포인트
- 장면 일괄 생성과 동일한 품질의 이미지 생성
- 기존 프로젝트 이미지 선택 기능
'''
import base64
import logging
from pathlib import Path
from flask import Blueprint, Flask, jsonify, request
from app.services.thumbnail.image_generator import get_image_generator
from app.config.paths import get_data_path, get_projects_path
logger = logging.getLogger(__name__)
thumbnail_creator_bp = Blueprint('thumbnail_creator', __name__, url_prefix = '/api/thumbnail-creator')
YOUTUBE_UPLOAD_TAB_THUMBNAIL_MODEL = 'nanobanana'

def init_app(app = None):
    '''Flask 앱에 Blueprint 등록'''
    app.register_blueprint(thumbnail_creator_bp)

generate_image = (lambda : pass# WARNING: Decompyle incomplete
)()
get_existing_images = (lambda : pass# WARNING: Decompyle incomplete
)()

def _url_to_base64(url = None):
    '''URL의 이미지를 base64로 변환'''
    
    try:
        if url.startswith('data:'):
            return url
        if None.startswith('/data/'):
            data_path = get_data_path()
            relative_path = url.replace('/data/', '')
            path = data_path / relative_path
            if path.exists():
                f = open(path, 'rb')
                img_bytes = f.read()
                b64 = base64.b64encode(img_bytes).decode('utf-8')
                
                try:
                    None(None, None)
                    return 
                    with None:
                        if not None, f'''data:image/jpeg;base64,{b64}''':
                            
                            try:
                                
                                try:
                                    if (url.startswith('/') and url.startswith('C:') or url.startswith('D:')) and path.exists():
                                        open(path, 'rb') = Path(url.replace('\\', '/'))
                                        img_bytes = f.read()
                                        b64 = base64.b64encode(img_bytes).decode('utf-8')
                                        
                                        try:
                                            None(None, None)
                                            return 
                                            with None:
                                                if not None, f'''data:image/jpeg;base64,{b64}''':
                                                    
                                                    try:
                                                        
                                                        try:
                                                            if url.startswith('http'):
                                                                import requests
