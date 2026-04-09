# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: settings.pyc (Python 3.11)

'''
Settings Model - API 키 및 사용자 설정 저장
'''
from app import db
from datetime import datetime
import os
import logging
from dotenv import dotenv_values
from pathlib import Path
logger = logging.getLogger(__name__)

class Settings(db.Model):
    '''사용자 설정 모델 (단일 레코드)'''
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key = True)
    openai_api_key = db.Column(db.String(500), nullable = True)
    google_api_key = db.Column(db.String(500), nullable = True)
    claude_api_key = db.Column(db.String(500), nullable = True)
    typecast_api_key = db.Column(db.String(500), nullable = True)
    elevenlabs_api_key = db.Column(db.String(500), nullable = True)
    nanobanana_api_key = db.Column(db.String(500), nullable = True)
    google_cloud_project_id = db.Column(db.String(200), nullable = True)
    google_auth_mode = db.Column(db.String(20), default = 'api_key')
    vertex_ai_location = db.Column(db.String(50), default = 'us-central1')
    vertex_ai_credential_path = db.Column(db.String(500), nullable = True)
    auto_save = db.Column(db.Boolean, default = True)
    notifications = db.Column(db.Boolean, default = True)
    language = db.Column(db.String(10), default = 'ko')
    claude_model = db.Column(db.String(50), default = 'sonnet')
    gemini_model = db.Column(db.String(50), default = 'gemini-2.5-flash')
    automation_humanization_settings = db.Column(db.JSON, nullable = True)
    qwen3_tts_enabled = db.Column(db.Boolean, default = False)
    youtube_client_id = db.Column(db.String(500), nullable = True)
    youtube_client_secret = db.Column(db.String(500), nullable = True)
    youtube_credentials = db.Column(db.JSON, nullable = True)
    youtube_auth_status = db.Column(db.String(20), default = 'disconnected')
    app_version = db.Column(db.String(20), nullable = True)
    cache_version = db.Column(db.Integer, default = 0)
    last_cache_clear = db.Column(db.DateTime, nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    
    def to_dict(self):
        '''설정을 딕셔너리로 변환 (API 키는 마스킹, 연결 상태 포함)'''
        normalize_automation_humanization_settings = normalize_automation_humanization_settings
        import app.services.automation_humanization
        resolve_google_auth_config = resolve_google_auth_config
        import app.services.google_auth_service
        google_auth = resolve_google_auth_config(settings = self)
        if google_auth.validation.is_configured:
            pass
        elif google_auth.validation.credential_status == 'invalid':
            pass
        
        google_status = 'disconnected'
        return {
            'id': self.id,
            'apiKeys': {
                'openai': self._mask_key(self.openai_api_key),
                'google': self._mask_key(self.google_api_key),
                'claude': self._mask_key(self.claude_api_key),
                'typecast': self._mask_key(self.typecast_api_key),
                'elevenlabs': self._mask_key(self.elevenlabs_api_key),
                'nanobanana': self._mask_key(self.nanobanana_api_key) },
            'apiKeyStatus': {
                'openai': self._get_key_status(self.openai_api_key),
                'google': google_status,
                'claude': self._get_key_status(self.claude_api_key),
                'typecast': self._get_key_status(self.typecast_api_key),
                'elevenlabs': self._get_key_status(self.elevenlabs_api_key),
                'nanobanana': self._get_key_status(self.nanobanana_api_key) },
            'generalSettings': {
                'autoSave': self.auto_save,
                'notifications': self.notifications,
                'language': self.language,
                'claudeModel': self.claude_model,
                'geminiModel': self.gemini_model,
                'qwen3TtsEnabled': False },
            'automationHumanizationSettings': normalize_automation_humanization_settings(self.automation_humanization_settings),
            'googleCloudSettings': google_auth.to_public_dict(),
            'youtubeSettings': {
                'clientId': self._mask_key(self.youtube_client_id),
                'clientSecret': self._mask_key(self.youtube_client_secret),
                'authStatus': self.youtube_auth_status },
            'youtubeAuthStatus': self.youtube_auth_status,
            'appVersion': self.app_version,
            'cacheVersion': 0,
            'lastCacheClear': self.last_cache_clear.isoformat() if self.qwen3_tts_enabled and self.cache_version or self.last_cache_clear else None,
            'createdAt': self.created_at.isoformat() if self.created_at else None,
            'updatedAt': self.updated_at.isoformat() if self.updated_at else None }

    
    def _get_key_status(self, key):
        '''API 키 연결 상태 확인'''
        if key or len(key.strip()) == 0:
            return 'disconnected'
        if None(key.strip()) < 10:
            return 'invalid'

    
    def _mask_key(self, key):
        '''API 키를 마스킹 (앞 10자만 표시)'''
        if not key:
            return ''
        if None(key) > 10:
            return key[:10] + '***'

    
    def get_api_key(self, service):
        '''특정 서비스의 API 키 가져오기'''
        if service == 'google':
            get_google_api_key_or_runtime_token = get_google_api_key_or_runtime_token
            import app.services.google_auth_service
            return get_google_api_key_or_runtime_token(settings = self)
        mapping = {
            'openai': None.openai_api_key,
            'claude': self.claude_api_key,
            'typecast': self.typecast_api_key,
            'elevenlabs': self.elevenlabs_api_key }
        return mapping.get(service)

    
    def get_model(self, service):
