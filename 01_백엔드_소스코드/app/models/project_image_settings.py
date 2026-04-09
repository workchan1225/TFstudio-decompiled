# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: project_image_settings.pyc (Python 3.11)

'''
ProjectImageSettings Model

프로젝트별 이미지 생성 설정 모델
- 기본 템플릿 선택
- 생성 설정 (엔진, 비율, 해상도)
- 캐릭터 참조 설정
'''
import uuid
from datetime import datetime
from  import db

class ProjectImageSettings(db.Model):
    '''프로젝트 이미지 생성 설정 모델'''
    __tablename__ = 'project_image_settings'
    id = db.Column(db.String(36), primary_key = True, default = (lambda : str(uuid.uuid4())))
    project_id = db.Column(db.String(36), db.ForeignKey('projects.id', ondelete = 'CASCADE'), nullable = False, unique = True, index = True)
    default_style_template_id = db.Column(db.String(36), nullable = True)
    default_character_template_id = db.Column(db.String(36), nullable = True)
    default_scene_template_id = db.Column(db.String(36), nullable = True)
    default_non_character_template_id = db.Column(db.String(36), nullable = True)
    default_engine = db.Column(db.String(30), default = 'nanobanana')
    default_aspect_ratio = db.Column(db.String(10), default = '16:9')
    default_resolution = db.Column(db.String(10), default = 'FHD')
    use_character_reference = db.Column(db.Boolean, default = True)
    character_consistency_strength = db.Column(db.Float, default = 0.8)
    default_content_type = db.Column(db.String(30), default = 'narrative')
    scene_overrides = db.Column(db.JSON, nullable = True)
    character_overrides = db.Column(db.JSON, nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    
    def __repr__(self):
        return f'''<ProjectImageSettings project_id={self.project_id}>'''

    
    def to_dict(self):
        '''설정을 딕셔너리로 변환'''
        pass
    # WARNING: Decompyle incomplete

    get_or_create = (lambda cls = None, project_id = None: settings = cls.query.filter_by(project_id = project_id).first()if not settings:
settings = cls(project_id = project_id)db.session.add(settings)db.session.commit()settings)()
    
    def update_from_dict(self = None, data = None):
        '''딕셔너리에서 설정 업데이트'''
        if 'defaultStyleTemplateId' in data:
            self.default_style_template_id = data['defaultStyleTemplateId']
        if 'defaultCharacterTemplateId' in data:
            self.default_character_template_id = data['defaultCharacterTemplateId']
        if 'defaultSceneTemplateId' in data:
            self.default_scene_template_id = data['defaultSceneTemplateId']
        if 'defaultNonCharacterTemplateId' in data:
            self.default_non_character_template_id = data['defaultNonCharacterTemplateId']
        if 'defaultEngine' in data:
            self.default_engine = data['defaultEngine']
        if 'defaultAspectRatio' in data:
            self.default_aspect_ratio = data['defaultAspectRatio']
        if 'defaultResolution' in data:
            self.default_resolution = data['defaultResolution']
        if 'useCharacterReference' in data:
            self.use_character_reference = data['useCharacterReference']
        if 'characterConsistencyStrength' in data:
            self.character_consistency_strength = data['characterConsistencyStrength']
        if 'defaultContentType' in data:
            self.default_content_type = data['defaultContentType']
        if 'sceneOverrides' in data:
            self.scene_overrides = data['sceneOverrides']
        if 'characterOverrides' in data:
            self.character_overrides = data['characterOverrides']
        db.session.commit()
        return self

    
    def set_scene_override(self = None, scene_id = None, style_template_id = None, custom_modifiers = (None, None)):
        '''장면별 오버라이드 설정'''
        pass
    # WARNING: Decompyle incomplete

    
    def set_character_override(self = None, character_name = None, style_template_id = None, custom_modifiers = (None, None)):
        '''캐릭터별 오버라이드 설정'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_effective_style_template_id(self = None, scene_id = None, character_name = None):
