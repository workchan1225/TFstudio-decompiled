# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: prompt_template.pyc (Python 3.11)

from app import db
from datetime import datetime

class PromptTemplate(db.Model):
    '''프롬프트 템플릿 모델

    관리자가 AI 생성을 위한 프롬프트 템플릿을 관리합니다.
    - topic: 주제 생성
    - outline: 개요 생성
    - script: 대본 생성
    - image: 이미지 생성
    '''
    __tablename__ = 'prompt_templates'
    id = db.Column(db.String(36), primary_key = True)
    type = db.Column(db.String(20), nullable = False)
    name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.Text)
    system_prompt = db.Column(db.Text, nullable = False)
    user_prompt_template = db.Column(db.Text)
    parameters = db.Column(db.JSON)
    is_default = db.Column(db.Boolean, default = False)
    is_active = db.Column(db.Boolean, default = True)
    usage_count = db.Column(db.Integer, default = 0)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'name': self.name,
            'description': self.description,
            'systemPrompt': self.system_prompt,
            'userPromptTemplate': self.user_prompt_template,
            'parameters': { },
            'isDefault': self.is_default,
            'isActive': self.is_active,
            'usageCount': self.usage_count,
            'createdAt': self.created_at.isoformat() if self.parameters or self.created_at else None,
            'updatedAt': self.updated_at.isoformat() if self.updated_at else None }

    get_default_template = (lambda template_type: PromptTemplate.query.filter_by(type = template_type, is_default = True, is_active = True).first())()
    get_active_templates = (lambda template_type: PromptTemplate.query.filter_by(type = template_type, is_active = True).order_by(PromptTemplate.is_default.desc(), PromptTemplate.updated_at.desc()).all())()
    
    def increment_usage(self):
        '''사용 횟수를 증가시킵니다'''
        db.session.commit()
