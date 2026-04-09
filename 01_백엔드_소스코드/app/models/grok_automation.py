# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: grok_automation.pyc (Python 3.11)

'''
Grok Automation Models

이미지 → 비디오 변환을 위한 Grok 웹 자동화 작업 관리 모델
'''
from app import db
from datetime import datetime
import uuid

class GrokAutomationTask(db.Model):
    '''
    Grok 자동화 작업 모델

    프로젝트의 씬 이미지를 Grok을 통해 비디오로 변환하는 작업을 추적합니다.
    '''
    __tablename__ = 'grok_automation_tasks'
    id = db.Column(db.String(36), primary_key = True, default = (lambda : str(uuid.uuid4())))
    project_id = db.Column(db.String(36), db.ForeignKey('projects.id', ondelete = 'CASCADE'), nullable = False, index = True)
    scene_id = db.Column(db.String(50), nullable = False)
    chapter_index = db.Column(db.Integer, nullable = False)
    scene_index = db.Column(db.Integer, nullable = False)
    source_image_path = db.Column(db.String(500), nullable = False)
    prompt = db.Column(db.Text, nullable = True)
    generated_video_path = db.Column(db.String(500), nullable = True)
    generated_video_url = db.Column(db.String(500), nullable = True)
    status = db.Column(db.String(20), default = 'pending', index = True)
    progress_percent = db.Column(db.Integer, default = 0)
    started_at = db.Column(db.DateTime, nullable = True)
    completed_at = db.Column(db.DateTime, nullable = True)
    error_message = db.Column(db.Text, nullable = True)
    retry_count = db.Column(db.Integer, default = 0)
    max_retries = db.Column(db.Integer, default = 3)
    grok_task_id = db.Column(db.String(100), nullable = True)
    video_duration = db.Column(db.Float, nullable = True)
    generation_settings = db.Column(db.JSON, nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    project = db.relationship('Project', backref = db.backref('grok_tasks', lazy = True, cascade = 'all, delete-orphan'))
    
    def to_dict(self):
        '''JSON 직렬화'''
        if not self.generation_settings:
            generation_settings = { }
        source_binding = generation_settings.get('sourceBinding') if isinstance(generation_settings, dict) else { }
        if not isinstance(source_binding, dict):
            source_binding = { }
    # WARNING: Decompyle incomplete

    
    def start_task(self):
        '''작업 시작'''
        self.status = 'starting'
        self.started_at = datetime.utcnow()
        self.progress_percent = 5

    
    def mark_uploading(self):
        '''업로드 단계로 변경'''
        self.status = 'uploading'
        self.progress_percent = 15

    
    def mark_starting_generation(self):
        '''생성 시작 대기 상태로 변경'''
        self.status = 'starting'
        self.progress_percent = 30

    
    def mark_processing(self = None, grok_task_id = None):
        '''Legacy alias for generation-in-progress state.'''
        self.status = 'generating'
        self.progress_percent = 40
        if grok_task_id:
            self.grok_task_id = grok_task_id
            return None

    
    def mark_generating(self = None, progress_percent = None, grok_task_id = None):
        '''영상 생성 진행 상태로 변경'''
        self.status = 'generating'
        self.progress_percent = max(0, min(100, int(progress_percent)))
        if grok_task_id:
            self.grok_task_id = grok_task_id
            return None

    
    def mark_downloading(self = None, video_url = None):
        '''다운로드 중 상태로 변경'''
        self.status = 'downloading'
        self.progress_percent = 85
        if video_url:
            self.generated_video_url = video_url
            return None

    
    def mark_completed(self = None, video_path = None, video_duration = None):
        '''작업 완료'''
        self.status = 'completed'
        self.progress_percent = 100
        self.completed_at = datetime.utcnow()
        self.generated_video_path = video_path.replace('\\', '/') if video_path else None
        if video_duration:
            self.video_duration = video_duration
            return None

    
    def mark_failed(self = None, error_message = None):
        '''작업 실패'''
        self.status = 'failed'
        self.error_message = error_message

    
    def can_retry(self = None):
        '''재시도 가능 여부'''
        return self.retry_count < self.max_retries

    
    def reset_for_retry(self):
        '''재시도를 위한 상태 초기화'''
        self.status = 'pending'
        self.progress_percent = 0
        self.error_message = None
        self.started_at = None
        self.completed_at = None



class GrokCredentials(db.Model):
    '''
    Grok 인증 정보 (암호화 저장)

    X (Twitter) OAuth를 통한 Grok 로그인 세션을 관리합니다.
    비밀번호는 저장하지 않으며, 쿠키/세션 데이터만 암호화하여 저장합니다.
    '''
    __tablename__ = 'grok_credentials'
    id = db.Column(db.Integer, primary_key = True)
    session_data_encrypted = db.Column(db.Text, nullable = True)
    is_authenticated = db.Column(db.Boolean, default = False)
    last_auth_check = db.Column(db.DateTime, nullable = True)
    auth_expires_at = db.Column(db.DateTime, nullable = True)
    account_username = db.Column(db.String(100), nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    
    def to_dict(self):
        '''JSON 직렬화 (민감 데이터 제외)'''
        return {
            'id': self.id,
            'isAuthenticated': self.is_authenticated,
            'lastAuthCheck': self.last_auth_check.isoformat() if self.last_auth_check else None,
            'authExpiresAt': self.auth_expires_at.isoformat() if self.auth_expires_at else None,
            'accountUsername': self.account_username,
            'createdAt': self.created_at.isoformat() if self.created_at else None,
            'updatedAt': self.updated_at.isoformat() if self.updated_at else None }

    
    def mark_authenticated(self = None, username = None):
        '''인증 완료 표시'''
        self.is_authenticated = True
        self.last_auth_check = datetime.utcnow()
        if username:
            self.account_username = username
            return None

    
    def mark_expired(self):
        '''인증 만료 표시'''
        self.is_authenticated = False
        self.session_data_encrypted = None

    
    def clear_session(self):
        '''세션 데이터 삭제'''
        self.session_data_encrypted = None
        self.is_authenticated = False
        self.account_username = None
