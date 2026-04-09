# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: license.pyc (Python 3.11)

'''
License Model - 라이선스 인증 및 구독 상태 관리
외부 API (tupastudio)와 연동하여 구독 상태를 확인하고 캐싱
'''
from app import db
from datetime import datetime, timedelta

class License(db.Model):
    '''라이선스 모델 (단일 레코드)'''
    __tablename__ = 'license'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), nullable = True)
    user_id = db.Column(db.Integer, nullable = True)
    status = db.Column(db.String(20), default = 'none')
    expires_at = db.Column(db.DateTime, nullable = True)
    days_remaining = db.Column(db.Integer, default = 0)
    total_days = db.Column(db.Integer, default = 0)
    started_at = db.Column(db.DateTime, nullable = True)
    auth = db.Column(db.Boolean, default = False)
    unlimited = db.Column(db.Boolean, default = False)
    last_verified_at = db.Column(db.DateTime, nullable = True)
    cached_response = db.Column(db.JSON, nullable = True)
    session_token = db.Column(db.String(64), nullable = True)
    device_id = db.Column(db.String(64), nullable = True)
    device_name = db.Column(db.String(100), nullable = True)
    last_heartbeat_at = db.Column(db.DateTime, nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    
    def to_dict(self):
        '''라이선스 정보를 딕셔너리로 변환'''
        pass
    # WARNING: Decompyle incomplete

    
    def is_valid(self = None):
