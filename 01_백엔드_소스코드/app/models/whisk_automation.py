# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: whisk_automation.pyc (Python 3.11)

'''
Whisk Automation Models

Google Whisk 이미지 합성 도구를 위한 인증 관리 및 작업 추적 모델
'''
from app import db
from datetime import datetime
import uuid

class WhiskCredentials(db.Model):
    '''
    Whisk 인증 정보 (암호화 저장)

    Google 계정을 통한 Whisk 로그인 세션을 관리합니다.
    비밀번호는 저장하지 않으며, 쿠키/세션 데이터만 암호화하여 저장합니다.
    '''
    __tablename__ = 'whisk_credentials'
    id = db.Column(db.Integer, primary_key = True)
    session_data_encrypted = db.Column(db.Text, nullable = True)
    is_authenticated = db.Column(db.Boolean, default = False)
    last_auth_check = db.Column(db.DateTime, nullable = True)
    auth_expires_at = db.Column(db.DateTime, nullable = True)
    account_email = db.Column(db.String(200), nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    
    def to_dict(self):
        '''JSON 직렬화 (민감 데이터 제외)'''
        return {
            'id': self.id,
            'isAuthenticated': self.is_authenticated,
            'lastAuthCheck': self.last_auth_check.isoformat() if self.last_auth_check else None,
            'authExpiresAt': self.auth_expires_at.isoformat() if self.auth_expires_at else None,
            'accountEmail': self.account_email,
            'createdAt': self.created_at.isoformat() if self.created_at else None,
            'updatedAt': self.updated_at.isoformat() if self.updated_at else None }

    
    def mark_authenticated(self = None, email = None):
        '''인증 완료 표시'''
        self.is_authenticated = True
        self.last_auth_check = datetime.utcnow()
        if email:
            self.account_email = email
            return None

    
    def mark_expired(self):
        '''인증 만료 표시'''
        self.is_authenticated = False
        self.session_data_encrypted = None

    
    def clear_session(self):
        '''세션 데이터 삭제'''
        self.session_data_encrypted = None
        self.is_authenticated = False
        self.account_email = None



class WhiskGenerationTask(db.Model):
    '''
    Whisk 자동화 작업 모델 (Grok 패턴)

    프로젝트의 프롬프트를 Whisk를 통해 이미지로 변환하는 작업을 추적합니다.
    '''
    __tablename__ = 'whisk_generation_tasks'
    id = db.Column(db.String(36), primary_key = True, default = (lambda : str(uuid.uuid4())))
    project_id = db.Column(db.String(36), db.ForeignKey('projects.id', ondelete = 'CASCADE'), nullable = False, index = True)
    prompt_id = db.Column(db.String(50), nullable = False)
    chapter_index = db.Column(db.Integer, nullable = False)
    scene_index = db.Column(db.Integer, nullable = False)
    prompt_text = db.Column(db.Text, nullable = False)
    prompt_ko = db.Column(db.Text, nullable = True)
    generated_image_path_1 = db.Column(db.String(500), nullable = True)
    generated_image_path_2 = db.Column(db.String(500), nullable = True)
    status = db.Column(db.String(20), default = 'pending', index = True)
    progress_percent = db.Column(db.Integer, default = 0)
    started_at = db.Column(db.DateTime, nullable = True)
    completed_at = db.Column(db.DateTime, nullable = True)
    error_message = db.Column(db.Text, nullable = True)
    retry_count = db.Column(db.Integer, default = 0)
    max_retries = db.Column(db.Integer, default = 3)
    generation_settings = db.Column(db.JSON, nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    project = db.relationship('Project', backref = db.backref('whisk_tasks', lazy = True, cascade = 'all, delete-orphan'))
    
    def to_dict(self):
        '''JSON 직렬화'''
        pass
    # WARNING: Decompyle incomplete

    
    def start_task(self):
        '''작업 시작'''
        self.status = 'generating'
        self.started_at = datetime.utcnow()
        self.progress_percent = 10

    
    def mark_downloading(self):
        '''다운로드 중 상태로 변경'''
        self.status = 'downloading'
        self.progress_percent = 70

    
    def mark_completed(self = None, image_path_1 = None, image_path_2 = None):
        '''작업 완료'''
        self.status = 'completed'
        self.progress_percent = 100
        self.completed_at = datetime.utcnow()
        if image_path_1:
            self.generated_image_path_1 = image_path_1.replace('\\', '/')
        if image_path_2:
            self.generated_image_path_2 = image_path_2.replace('\\', '/')
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
