# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_prompt_composer.pyc (Python 3.11)

'''
ScenePromptComposer - 구조화된 프롬프트 구성 서비스

scene_image_service.py에서 추출됨 (Phase 4 리팩토링)

주요 기능:
- 구조화된 JSON에서 한국어/영어 프롬프트 조합
- 캐릭터 Base Prompt 생성
- 프롬프트 파싱 및 검증
'''
import re
from typing import Dict, List, Any, Optional

class ScenePromptComposer:
    '''구조화된 프롬프트를 조합하고 파싱하는 서비스'''
    build_character_base_prompt = (lambda character = None, language = None: char_name = character.get('name', '캐릭터')if char_name.startswith('@'):
char_name = char_name[1:]if language == 'en':
ScenePromptComposer._build_character_base_prompt_en(character, char_name)None._build_character_base_prompt_ko(character, char_name))()
    _build_character_base_prompt_en = (lambda character = None, char_name = None: gender = character.get('gender', 'unknown')if gender == 'male':
passelif gender == 'female':
passgender_en = 'person'age_range = character.get('ageRange', '')if not character.get('hairstyleEn', ''):
hairstyle_en = character.get('hairstyle', '')if not character.get('primaryOutfitEn', ''):
if not character.get('primaryOutfit', ''):
outfit_en = character.get('clothing', '')if not character.get('accessoriesEn', ''):
accessories_en = character.get('accessories', '')if not character.get('distinctiveFeaturesEn', ''):
distinctive_en = character.get('distinctiveFeatures', '')english_desc = character.get('englishDescription', '')if not character.get('build'):
if not character.get('physique'):
if not character.get('bodyType'):
body_type = ''parts = [
f'''@{char_name}''']if hairstyle_en:
parts.append(f'''with {hairstyle_en}''')parts.append(f'''[HAIR FIXED: {hairstyle_en}]''')parts.append(f'''(hair: {hairstyle_en} - DO NOT CHANGE)''')if outfit_en:
parts.append(f'''wearing {outfit_en}''')parts.append(f'''[OUTFIT FIXED: {outfit_en}]''')parts.append(f'''(outfit: {outfit_en} - MAINTAIN CONSISTENT)''')if accessories_en:
parts.append(f'''with {accessories_en}''')if distinctive_en:
parts.append(distinctive_en)parts.append('[SKIN TONE: consistent across all scenes]')parts.append("CRITICAL: This character's appearance is FIXED. Hair, face, skin tone must remain IDENTICAL in every scene. NO VARIATIONS ALLOWED")', '.join(parts))()
    _build_character_base_prompt_ko = (lambda character = None, char_name = None: age_range = character.get('ageRange', '')hairstyle = character.get('hairstyle', '')if not character.get('primaryOutfit', ''):
outfit = character.get('clothing', '')accessories = character.get('accessories', '')distinctive = character.get('distinctiveFeatures', '')if not character.get('build'):
if not character.get('physique'):
if not character.get('bodyType'):
body_type = ''parts = [
f'''@{char_name}''']gender = character.get('gender', 'unknown')if gender == 'male':
passelif gender == 'female':
passgender_ko = '인물'identity = f'''{age_range} 한국인 {gender_ko}''' if age_range else f'''한국인 {gender_ko}'''if body_type:
identity += f''', {body_type}'''parts.append(identity)if hairstyle:
parts.append(hairstyle)parts.append(f'''[머리스타일 고정: {hairstyle}]''')parts.append(f'''(머리: {hairstyle} - 변경 금지)''')if outfit:
parts.append(outfit)parts.append(f'''[의상 고정: {outfit}]''')parts.append(f'''(의상: {outfit} - 변경 금지)''')if accessories:
parts.append(accessories)if distinctive:
parts.append(distinctive)parts.append('[피부톤: 모든 장면에서 동일하게 유지]')parts.append('필수: 이 캐릭터의 외모는 고정됨. 머리, 얼굴, 피부톤은 모든 장면에서 동일해야 함. 변경 불가')', '.join(parts))()
    compose_prompt_ko = (lambda structured = None: context = structured.get('context', { })subject = structured.get('subject', { })environment = structured.get('environment', { })parts = []setting = context.get('setting', '')era = context.get('era', '')time_of_day = context.get('timeOfDay', '')context_parts = []if era:
if not setting or setting.startswith(era):
context_parts.append(era)if setting:
context_parts.append(setting)if time_of_day:
context_parts.append(time_of_day)if context_parts:
parts.append(', '.join(context_parts))main_action = subject.get('mainAction', '')if main_action:
parts.append(main_action)characters = subject.get('characters', [])for c in characters:
name = c.get('name', '')if name.startswith('@'):
name = name[1:]action = c.get('action', '')emotion = c.get('emotion', '')gaze = c.get('gaze', '')position = c.get('position', '')interaction = c.get('interaction', '')char_desc_parts = []if position:
char_desc_parts.append(f'''{position}에서''')if emotion:
char_desc_parts.append(f'''{emotion}의 표정으로''')if action:
char_desc_parts.append(action)if gaze:
char_desc_parts.append(gaze)if interaction and len(characters) > 1:
char_desc_parts.append(f'''({interaction})''')if char_desc_parts:
parts.append(f'''{name}가 {' '.join(char_desc_parts)}''')location = environment.get('location', '')atmosphere = environment.get('atmosphere', '')lighting = environment.get('lighting', '')if location:
parts.append(location)if atmosphere:
parts.append(f'''{atmosphere} 분위기''')if lighting:
parts.append(lighting)'. '.join(parts) + '.' if parts else '')()
    compose_prompt_en = (lambda structured = None: pass# WARNING: Decompyle incomplete
)()
    parse_structured_prompt = (lambda ai_response = None: structured = ai_response.get('structuredPrompt', { })required_sections = [
'context',
'subject',
'environment']for section in required_sections:
if section not in structured:
structured[section] = { }if 'metadata' not in structured:
structured['metadata'] = { }metadata = structured.get('metadata', { })if not isinstance(metadata, dict):
metadata = { }structured['metadata'] = metadatametadata.setdefault('anchorSentence', '')metadata.setdefault('keyMoment', '')metadata.setdefault('sceneType', 'action')metadata.setdefault('sceneContext', '')metadata.setdefault('sceneContextEn', '')metadata.setdefault('sceneSummary', '')metadata.setdefault('sceneSummaryEn', '')metadata.setdefault('visualCue', '')metadata.setdefault('visualCueEn', '')sentence_range = metadata.get('sentenceRange')if not isinstance(sentence_range, dict):
metadata['sentenceRange'] = {
'start': 0,
'end': 0 }if not ai_response.get('narrationText', ''):
primary_greeting_action = ScenePromptComposer._normalize_structured_greeting_actions(structured, str(''))if primary_greeting_action:
metadata['primaryGreetingAction'] = primary_greeting_actionif 'style' not in structured:
structured['style'] = {
'visualStyle': 'cinematic',
'cinematicKeywords': [
'hyper-realistic',
'8k'] }ScenePromptComposer.backfill_structured_prompt_language_fields(structured)characters = structured.get('subject', { }).get('characters', [])detected_names = characters()character_details = []for char in characters:
character_details.append({
'name': char.get('name', ''),
'action': char.get('action', ''),
'emotion': char.get('emotion', '') })prompt_ko = ScenePromptComposer.compose_prompt_ko(structured)prompt_en = ScenePromptComposer.compose_prompt_en(structured){
'structuredPrompt': structured,
'promptKo': prompt_ko,
'promptEn': prompt_en,
'detectedCharacters': detected_names,
'characterReferenceDetails': character_details })()
    backfill_structured_prompt_language_fields = (lambda structured = None: context = structured.get('context')if not isinstance(context, dict):
context = { }structured['context'] = contextsubject = structured.get('subject')if not isinstance(subject, dict):
subject = { }structured['subject'] = subjectenvironment = structured.get('environment')if not isinstance(environment, dict):
environment = { }structured['environment'] = environmentif context.get('settingEn') and context.get('setting'):
context['settingEn'] = context.get('setting')if subject.get('mainActionEn') and subject.get('mainAction'):
subject['mainActionEn'] = subject.get('mainAction')characters = subject.get('characters')if not isinstance(characters, list):
characters = []subject['characters'] = charactersfor char in characters:
if not isinstance(char, dict):
continueif char.get('nameEn') and char.get('name'):
char['nameEn'] = char.get('name')if char.get('actionEn') and char.get('action'):
char['actionEn'] = char.get('action')if char.get('emotionEn') and char.get('emotion'):
char['emotionEn'] = char.get('emotion')if char.get('gazeEn') and char.get('gaze'):
char['gazeEn'] = char.get('gaze')if char.get('positionEn') and char.get('position'):
char['positionEn'] = char.get('position')if char.get('interactionEn') and char.get('interaction'):
char['interactionEn'] = char.get('interaction')if environment.get('locationEn') and environment.get('location'):
environment['locationEn'] = environment.get('location')if environment.get('lightingEn') and environment.get('lighting'):
environment['lightingEn'] = environment.get('lighting')if environment.get('atmosphereEn') and environment.get('atmosphere'):
environment['atmosphereEn'] = environment.get('atmosphere')metadata = structured.get('metadata')if not isinstance(metadata, dict):
metadata = { }structured['metadata'] = metadataif metadata.get('sceneContextEn') and metadata.get('sceneContext'):
metadata['sceneContextEn'] = metadata.get('sceneContext')if metadata.get('sceneSummaryEn') and metadata.get('sceneSummary'):
metadata['sceneSummaryEn'] = metadata.get('sceneSummary')if metadata.get('visualCueEn') or metadata.get('visualCue'):
metadata['visualCueEn'] = metadata.get('visualCue')NoneNone)()
    _cleanup_action_text = (lambda text = None:
