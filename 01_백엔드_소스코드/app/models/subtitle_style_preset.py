# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: subtitle_style_preset.pyc (Python 3.11)

'''자막 스타일 프리셋 모델 - 프로젝트 독립적으로 저장'''
from datetime import datetime
from app import db

class SubtitleStylePreset(db.Model):
    '''자막 스타일 프리셋 - 모든 프로젝트에서 공유 가능'''
    __tablename__ = 'subtitle_style_presets'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    font_family = db.Column(db.String(100), default = 'Pretendard')
    font_size = db.Column(db.Integer, default = 48)
    font_color = db.Column(db.String(20), default = '#FFFFFF')
    background_color = db.Column(db.String(20), default = '#000000')
    background_opacity = db.Column(db.Float, default = 0.7)
    enable_background = db.Column(db.Boolean, default = True)
    stroke_color = db.Column(db.String(20), default = '#000000')
    stroke_width = db.Column(db.Float, default = 2)
    enable_stroke = db.Column(db.Boolean, default = False)
    position = db.Column(db.String(20), default = 'bottom')
    alignment = db.Column(db.String(20), default = 'center')
    position_x = db.Column(db.Float, default = 50)
    position_y = db.Column(db.Float, default = 90)
    use_custom_position = db.Column(db.Boolean, default = False)
    horizontal_margin = db.Column(db.Float, default = 5)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    
    def to_dict(self):
        '''프론트엔드용 camelCase 딕셔너리 반환'''
        pass
    # WARNING: Decompyle incomplete

    from_dict = (lambda cls = None, data = None: pass# WARNING: Decompyle incomplete
)()
    
    def update_from_dict(self = None, data = None):
        '''camelCase 딕셔너리로 모델 업데이트'''
        if 'name' in data:
            self.name = data['name']
        if 'fontFamily' in data:
            self.font_family = data['fontFamily']
        if 'fontSize' in data:
            self.font_size = data['fontSize']
        if 'fontColor' in data:
            self.font_color = data['fontColor']
        if 'backgroundColor' in data:
            self.background_color = data['backgroundColor']
        if 'backgroundOpacity' in data:
            self.background_opacity = data['backgroundOpacity']
        if 'enableBackground' in data:
            self.enable_background = data['enableBackground']
        if 'strokeColor' in data:
            self.stroke_color = data['strokeColor']
        if 'strokeWidth' in data:
            self.stroke_width = data['strokeWidth']
        if 'enableStroke' in data:
            self.enable_stroke = data['enableStroke']
        if 'position' in data:
            self.position = data['position']
        if 'alignment' in data:
            self.alignment = data['alignment']
        if 'positionX' in data:
            self.position_x = data['positionX']
        if 'positionY' in data:
            self.position_y = data['positionY']
        if 'useCustomPosition' in data:
            self.use_custom_position = data['useCustomPosition']
        if 'horizontalMargin' in data:
            self.horizontal_margin = data['horizontalMargin']
            return None
