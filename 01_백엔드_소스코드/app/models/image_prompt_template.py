# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_prompt_template.pyc (Python 3.11)

__doc__ = '\nImagePromptTemplate Model\n\n이미지 생성을 위한 프롬프트 템플릿 모델\n- 캐릭터 (character): 등장인물 참조 이미지 생성용\n- 장면 (scene): 장면 이미지 생성용\n- 스타일 (style): 시각적 스타일 프리셋\n- 비캐릭터 (non_character): 텍스트 오버레이, 추상화, 배경 등\n'
import uuid
from datetime import datetime
from  import db

class ImagePromptTemplate(db.Model):
    '''이미지 프롬프트 템플릿 모델'''
    __tablename__ = 'image_prompt_templates'
    id = db.Column(db.String(36), primary_key = True, default = (lambda : str(uuid.uuid4())))
    type = db.Column(db.String(30), nullable = False, index = True)
    name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.Text, nullable = True)
    name_ko = db.Column(db.String(255), nullable = True)
    description_ko = db.Column(db.Text, nullable = True)
    system_prompt = db.Column(db.Text, nullable = False)
    prompt_template = db.Column(db.Text, nullable = True)
    negative_prompt = db.Column(db.Text, nullable = True)
    system_prompt_ko = db.Column(db.Text, nullable = True)
    prompt_template_ko = db.Column(db.Text, nullable = True)
    recommended_genres = db.Column(db.JSON, nullable = True)
    visual_category = db.Column(db.String(30), nullable = True)
    sample_image_url = db.Column(db.String(500), nullable = True)
    parameters = db.Column(db.JSON, nullable = True)
    default_settings = db.Column(db.JSON, nullable = True)
    is_default = db.Column(db.Boolean, default = False)
    is_active = db.Column(db.Boolean, default = True)
    usage_count = db.Column(db.Integer, default = 0)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    
    def __repr__(self):
        return f'''<ImagePromptTemplate {self.name} ({self.type})>'''

    
    def to_dict(self):
        '''템플릿을 딕셔너리로 변환'''
        capabilities = None
        if self.type or str('').strip().lower() == 'style':
            resolve_style_template_capabilities = resolve_style_template_capabilities
            import app.services.scene.style_template_capability_registry
            capabilities = resolve_style_template_capabilities(style_template_id = self.id, visual_category = self.visual_category).to_dict()
    # WARNING: Decompyle incomplete

    get_by_type = (lambda cls = None, template_type = None, active_only = classmethod: query = cls.query.filter_by(type = template_type)if active_only:
query = query.filter_by(is_active = True)query.order_by(cls.is_default.desc(), cls.name).all())()
    get_default = (lambda cls = None, template_type = None: cls.query.filter_by(type = template_type, is_default = True, is_active = True).first())()
    set_default = (lambda cls = None, template_id = None: template = cls.query.get(template_id)if not template:
NoneNone.query.filter_by(type = template.type, is_default = True).update({
'is_default': False })template.is_default = Truedb.session.commit()template)()
    
    def increment_usage(self):
        '''사용 횟수 증가'''
        db.session.commit()

    
    def apply_variables(self = None, variables = None):
        '''템플릿에 변수 적용하여 최종 프롬프트 생성'''
        if not self.prompt_template:
            return self.system_prompt
        result = None.prompt_template
        for key, value in variables.items():
            placeholder = '{' + key + '}'
            if placeholder in result:
                result = result.replace(placeholder, str(value) if value else '')
            return result.strip()


# WARNING: Decompyle incomplete
