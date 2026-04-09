# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_generation_prompt_preparation.pyc (Python 3.11)

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional
from scene_decision import build_scene_decision_prompt_blocks, scene_decision_actor_presence_mode, update_scene_decision_style_context
from scene_cast_orchestration import format_scene_cast_diagnostics
from scene_identity_context import extract_scene_registered_character_names, extract_scene_resolved_character_ids
from scene_prompt_assembly import build_scene_prompt_assembly
_INFO_EVENT_MARKERS = ('태풍', '폭우', '홍수', '지진', '화재', '파도', '바다', '도시', '면적', '강수량', '밀리미터', '기온', '기후', '확률', '통계', '숫자', '데이터', '그래프', '지도', '구조', '위험', '피해', '인프라', '재난', '기압', 'storm', 'typhoon', 'rainfall', 'flood', 'earthquake', 'fire', 'ocean', 'city', 'area', 'millimeter', 'temperature', 'climate', 'probability', 'statistics', 'data', 'graph', 'map', 'infrastructure', 'risk', 'damage')
_HUMAN_SUBJECT_MARKERS = ('@', '그는', '그녀', '남성', '여성', '인물', '사람', '학생', '교수', '의사', '환자', '직원', '가족', '시민', 'worker', 'person', 'people', 'woman', 'man', 'teacher', 'doctor', 'patient', 'family', 'citizen')
_PRESENTER_MARKERS = ('발표', '진행자', '해설자', '강연', '인터뷰', '브리핑', '설명하는 인물', 'presenter', 'host', 'reporter', 'anchor', 'speaker', 'lecturer', 'briefing', 'interview')
_HUMAN_ACTION_MARKERS = ('걷', '달리', '안아', '붙잡', '가리키', '말하', '표정', '응시', '손', '서 있', '앉아', 'walking', 'running', 'embracing', 'holding', 'pointing', 'speaking', 'looking', 'standing', 'sitting')
_EVENT_ENVIRONMENT_MARKERS = ('태풍', '폭우', '홍수', '화재', '연기', '바다', '파도', '도시', '건물', '구조', '거리', '실내', '전시', '박물관', '유물', '도자기', '창문', '창밖', '하늘', '강수량', '면적', '수치', '통계', '확률', '위험', '피해', '재난', '지표', '화면', '모니터', '차트', '그래프', '지도', '문서', '데이터', 'storm', 'typhoon', 'rainfall', 'flood', 'fire', 'smoke', 'ocean', 'wave', 'city', 'building', 'structure', 'street', 'interior', 'exhibit', 'museum', 'artifact', 'pottery', 'window', 'skyline', 'statistics', 'probability', 'risk', 'damage', 'disaster', 'monitor', 'screen', 'chart', 'graph', 'map', 'document', 'data')
_NO_HUMAN_SUBJECT_LOCK = '[NO HUMAN SUBJECT LOCK: Keep this scene focused on the event, environment, object, or evidence surface itself. Do NOT add a presenter, narrator, bystander, generic person, or default stickman/human figure unless the narration explicitly requires a visible person.]'
_DEFAULT_ANONYMOUS_HUMAN_ROLES = ('resident', 'worker', 'student', 'family member', 'patient', 'citizen', 'rescuer')
_SEVERE_WEATHER_MARKERS = ('태풍', '폭풍', '폭우', '강풍', '호우', '침수', '홍수', '해일', '파도', 'storm', 'typhoon', 'hurricane', 'severe weather', 'heavy rain', 'flood', 'flooded', 'wind', 'gale', 'downpour', 'surge', 'wave')
_INDOOR_VIEWPOINT_MARKERS = ('실내', '집 안', '거실', '방 안', '창문 너머', '창밖으로', '사무실', '통제실', '교실', '박물관', '전시장', 'gallery', 'museum', 'office', 'control room', 'classroom', 'living room', 'bedroom', 'inside', 'indoors', 'interior', 'apartment', 'house')
_PUBLIC_EXTERIOR_MARKERS = ('도시', '도심', '거리', '도로', '교량', '다리', '강변', '제방', '항구', '해안', '건물', '빌딩', '인프라', 'street', 'road', 'bridge', 'riverfront', 'harbor', 'shore', 'coast', 'city', 'urban', 'building', 'infrastructure', 'seawall')
_COASTAL_EXTERIOR_MARKERS = ('바다', '해안', '해변', '항구', '방파제', 'shore', 'coast', 'ocean', 'sea', 'harbor', 'seawall', 'waterfront')
SceneKeywordTextPreparationResult = <NODE:12>()
SceneGenerationPromptPreparationResult = <NODE:12>()

def _contains_any(text = None, markers = dataclass):
    pass
# WARNING: Decompyle incomplete


def _build_scene_focus_text(*, scene, structured_prompt_dict, narration_raw):
    if not narration_raw and scene.get('promptEn', '') and scene.get('imagePrompt', ''):
        parts = [
            str('').strip(),
            str('').strip(),
            str('').strip()]
        if isinstance(structured_prompt_dict, dict):
            for section_key in ('metadata', 'context', 'environment', 'subject'):
                section = structured_prompt_dict.get(section_key)
                if not isinstance(section, dict):
                    continue
                for value in section.values():
                    if isinstance(value, str) and value.strip():
                        parts.append(value.strip())
                    if section_key == 'subject':
                        characters = section.get('characters')
                        if isinstance(characters, list):
                            for character in characters[:2]:
                                if not isinstance(character, dict):
                                    continue
                                for field in ('name', 'action', 'actionEn', 'gaze', 'gazeEn', 'position', 'positionEn'):
                                    value = character.get(field)
                                    if isinstance(value, str) and value.strip():
                                        parts.append(value.strip())
                                    return (lambda .0: pass# WARNING: Decompyle incomplete
)(parts())


def _selected_character_name_appears_in_text(scene_characters = None, text = None):
    if not text:
        lowered = str('').lower()
        if not lowered:
            return False
        if not None:
            for character in []:
                if not isinstance(character, dict):
                    continue
                if not character.get('name'):
                    name = str('').strip()
                    if not name:
                        continue
                normalized_name = name.lower()
                if normalized_name in lowered:
                    return True
                condensed = None.replace(' ', '')
                if condensed and condensed in lowered.replace(' ', ''):
                    return True
                return False


def _scene_text_has_human_focus(text = None, scene_characters = None):
