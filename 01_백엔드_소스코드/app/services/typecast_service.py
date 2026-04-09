# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typecast_service.pyc (Python 3.11)

'''
Typecast TTS API 서비스 (REST API 사용)
프리미엄 한국어 음성 합성 서비스
'''
import requests
import logging
import json
from typing import Optional, Dict
from pathlib import Path
from app.utils.atomic_media_write import atomic_audio_output
logger = logging.getLogger(__name__)

class TypecastService:
    '''Typecast TTS API 서비스 클래스 (REST API 사용)'''
    BASE_URL = 'https://api.typecast.ai'
    
    def __init__(self = None, api_key = None):
        '''
        Args:
            api_key: Typecast API 키
        '''
        if not api_key:
            raise ValueError('Typecast API key is required')
        self.api_key = api_key
        self.headers = {
            'X-API-KEY': api_key,
            'Content-Type': 'application/json' }
        self.voice_metadata = self._load_voice_metadata()

    
    def _load_voice_metadata(self = None):
        '''Voice 메타데이터 JSON 파일 로드'''
        
        try:
            get_voice_metadata_path = get_voice_metadata_path
            import app.config.paths
            metadata_path = get_voice_metadata_path()
            if not metadata_path.exists():
                logger.warning(f'''Voice 메타데이터 파일이 없습니다: {metadata_path}''')
                return {
                    'voices': { },
                    'name_mappings': { } }
            f = None(metadata_path, 'r', encoding = 'utf-8')
            metadata = json.load(f)
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            logger.info(f'''Voice 메타데이터 로드 완료: {len(metadata.get('voices', { }))}개 voice''')
                            return metadata
                        except Exception:
                            e = None
                            logger.error(f'''Voice 메타데이터 로드 실패: {e}''')
                            del e
                            return None
                            None = 
                            del e





    
    def _detect_language(self = None, voice_name = None):
