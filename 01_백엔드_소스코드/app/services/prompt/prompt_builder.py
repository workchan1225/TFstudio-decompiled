# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: prompt_builder.pyc (Python 3.11)

'''
프롬프트 빌드 통합 모듈

NanoBanana(Gemini 이미지 생성)에 최적화된 프롬프트 빌드
- 모든 프롬프트 빌드 로직 통합
- 스타일 강조 키워드 자동 적용
- 역사극 한복 자동 적용

NOTE: 현재는 image_template_service.py의 기존 로직을 래핑.
      점진적으로 이 모듈로 마이그레이션 예정.
'''
from typing import Dict, List, Optional
from style_emphasis import apply_style_emphasis, get_style_emphasis, get_face_consistency_prompt
from historical_costume import is_historical_style, build_costume_description

class PromptBuilder:
    '''
    NanoBanana 최적화 프롬프트 빌더

    프롬프트 구조:
    [STYLE PREFIX] [STYLE KEYWORDS]. [Subject/Character]. [Scene/Context].
    [Camera/Lighting]. [Quality Modifiers]. [Constraints/Exclusions].
    '''
    DEFAULT_VARIABLES = {
        'base_prompt',
        'scene_context',
        'style_modifiers',
        'costume_description',
        'character_description'}
    apply_template = (lambda template_str = None, variables = None: if not template_str:
''result = Nonefor key, value in variables.items():
placeholder = f'''{{{key}}}'''if placeholder in result:
result = result.replace(placeholder, str(value) if value else '')import reresult = re.sub('\\{[^}]+\\}', '', result)result = re.sub(',\\s*,', ',', result)result = re.sub('\\s+', ' ', result)result = result.strip(' ,.')result)()
    build_simple_prompt = (lambda base_prompt = None, visual_category = None, include_quality = staticmethod: prompt = apply_style_emphasis(base_prompt, visual_category)if include_quality:
prompt = f'''{prompt}. High-quality, professional composition'''prompt)()
    build_character_prompt = (lambda character = None, style_template = None, include_consistency = staticmethod: name = character.get('name', 'Character')gender = character.get('gender', 'unknown')if gender == 'male':
passelif gender == 'female':
passgender_en = 'person'age_range = character.get('ageRange', '')description = character.get('englishDescription', '')parts = [
f'''@{name}''']base_prompt = ', '.join(parts)prompt = f'''Portrait of {base_prompt}, face focus, detailed features, high-quality 8K portrait'''visual_category = Noneif style_template:
if not style_template.get('visualCategory'):
visual_category = style_template.get('visual_category')if visual_category:
prompt = apply_style_emphasis(prompt, visual_category)if include_consistency:
consistency = get_face_consistency_prompt(include_hairstyle = True)prompt = f'''{prompt}. {consistency}'''prompt)()
    build_scene_prompt = (lambda scene_description = None, characters = None, style_template = staticmethod, cinematic_info = (None, None, None): prompt_parts = []if cinematic_info:
shot_type = cinematic_info.get('shot_type', 'medium shot')camera_angle = cinematic_info.get('camera_angle', 'eye-level')prompt_parts.append(f'''[SHOT: {shot_type.upper()}] [ANGLE: {camera_angle.upper()}]''')if characters:
character_prompts = []for char in characters:
name = char.get('name', 'Character')gender = char.get('gender', 'unknown')if gender == 'male':
passelif gender == 'female':
passgender_en = 'person'age_range = char.get('ageRange', '')if not char.get('hairstyleEn', ''):
hairstyle = char.get('hairstyle', '')if not char.get('primaryOutfitEn', ''):
outfit = char.get('primaryOutfit', '')english_desc = char.get('englishDescription', '')if hairstyle:
parts.append(f'''with {hairstyle}''')if outfit:
parts.append(f'''wearing {outfit}''')character_prompts.append(', '.join(parts))prompt_parts.append('. '.join(character_prompts))prompt_parts.append(f'''Scene: {scene_description}''')if style_template and is_historical_style(style_template):
if not characters:
build_costume_description([], scene_description) = 'man' if english_desc else 'woman'if costume_desc:
prompt_parts.append(costume_desc)prompt = '. '.join(prompt_parts)visual_category = Noneif style_template:
if not style_template.get('visualCategory'):
visual_category = style_template.get('visual_category')if visual_category:
prompt = apply_style_emphasis(prompt, visual_category)if characters:
consistency = get_face_consistency_prompt(include_hairstyle = True)prompt = f'''{prompt}. {consistency}'''prompt)()
    build_non_character_prompt = (lambda concept = None, style_template = None: prompt = conceptvisual_category = Noneif style_template:
if not style_template.get('visualCategory'):
visual_category = style_template.get('visual_category')if visual_category:
prompt = apply_style_emphasis(prompt, visual_category)else:
prompt = f'''{prompt}. High-quality, professional composition'''prompt)()
    build_character_with_repetition = (lambda character = None: name = character.get('name', 'Character')age_range = character.get('ageRange', '')gender = character.get('gender', '')key_feature = ''if character.get('hairstyleEn'):
key_feature = character.get('hairstyleEn')elif character.get('englishDescription'):
desc = character.get('englishDescription', '')if ',' in desc:
key_feature = desc.split(',')[0].strip()else:
key_feature = desc[:40].strip()gender_age = ''if gender and age_range:
if gender == 'male':
passelif gender == 'female':
passgender_en = 'person'gender_age = f'''{age_range} {gender_en}'''elif age_range:
gender_age = age_rangeparts = [
f'''@{name}''']features = []if key_feature:
features.append(key_feature)if gender_age:
features.append(gender_age)features.append('as seen in reference')if features:
parts.append(f'''({', '.join(features)})''')''.join(parts))()
    build_characters_with_repetition = (lambda characters = None:
