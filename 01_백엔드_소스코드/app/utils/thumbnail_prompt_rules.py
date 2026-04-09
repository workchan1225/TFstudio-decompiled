# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: thumbnail_prompt_rules.pyc (Python 3.11)

'''
Thumbnail prompt rule presets for wizard generation.

목표:
- 별도 썸네일 샘플 폴더에 의존하지 않고도
  YouTube 클릭형 썸네일 문법을 재사용 가능한 규칙 세트로 운용
- 제목 톤(긴박/일반)에 맞춰 프롬프트 규칙을 자동 선택
'''
from __future__ import annotations
import zlib
from typing import Dict
_URGENT_KEYWORDS = ('위기', '긴급', '급박', '절박', '붕괴', '파산', '추락', '실패', '위험', '마지막', '경고', '충돌', '배신', '도망', '폭로', '반전', '무너', '끝')
_RULE_PROFILES: 'Dict[str, Dict[str, str]]' = {
    'urgent_conflict': {
        'name': '긴박 대치형',
        'expression': '급박한 긴장 표정, 눈동자와 눈썹 변화가 즉시 읽히는 감정',
        'gesture': '상체 전진 + 손/팔 동작이 살아있는 액션 제스처',
        'scene': '충돌 직전의 긴장 장면, 시선이 즉시 인물에게 모이는 배치',
        'composition': '메인 인물 클로즈업 중심, 배경은 단순화해 감정 전달 집중',
        'color': '고대비(짙은 네이비/차콜) + 경고 계열 포인트 컬러로 긴박감 강화',
        'text_color': '메인 텍스트는 강한 대비, 보조 라벨은 톤 다운된 조화 색상 사용',
        'supporting_text': '보조 라벨은 코너 근처 작은 정보태그 형태, 메인 텍스트 대비 작게 유지',
        'focus_guard': '얼굴/눈/손 제스처는 반드시 선명, 배경만 약한 심도 블러 허용',
        'negative': '인물 초점 이탈, 과도한 모션블러, 텍스트 과밀 배치 금지' },
    'urgent_countdown': {
        'name': '카운트다운 경고형',
        'expression': '시간이 촉박한 듯한 절박 표정, 입/시선에서 긴장감 강조',
        'gesture': '시간 압박을 느끼는 손동작(쥔 손, 가리키는 제스처) 중심',
        'scene': '위기 카운트다운 분위기의 배경, 시각적 긴장선 강조',
        'composition': '인물 60-70%, 텍스트 30-40% 비율로 클릭 유도형 레이아웃',
        'color': '딥톤 배경 + 경고색(레드/오렌지/옐로) 포인트를 제한적으로 사용',
        'text_color': '헤드라인/보조텍스트 색상은 같은 계열 안에서 명도만 분리',
        'supporting_text': '보조 라벨은 작은 알림 배지처럼, 살짝 기울여 정보성만 전달',
        'focus_guard': '인물 안면부 선예도 최우선, 배경 대비만 강화하고 인물은 흐리지 않음',
        'negative': '텍스트 중복, 동일 강색 과다 반복, 인물 왜곡 금지' },
    'dramatic_reveal': {
        'name': '반전 드라마형',
        'expression': '충격 직전/직후의 감정이 느껴지는 얼굴, 눈빛 중심 감정 전달',
        'gesture': '어깨/팔 움직임이 보이는 자연스러운 행동 포즈',
        'scene': '반전 단서가 느껴지는 드라마 장면, 인물과 배경의 긴장 대비',
        'composition': '인물 시선 방향과 텍스트 흐름을 연결해 읽기 동선 구성',
        'color': '시네마틱 대비 + 제한된 포인트 컬러로 몰입감 형성',
        'text_color': '메인 텍스트는 고명도, 보조 라벨은 저채도 톤으로 균형 유지',
        'supporting_text': '보조 라벨은 모서리 정보태그(작게)로만 사용',
        'focus_guard': '핵심 인물의 눈/입 표정은 또렷하게 유지',
        'negative': '배경 디테일 과다, 본문보다 큰 보조 라벨, 인물 흐림 금지' },
    'authority_explain': {
        'name': '정보 신뢰형',
        'expression': '집중/설명형 표정, 신뢰감 있는 눈맞춤',
        'gesture': '핵심을 짚는 절제된 손동작, 과장되지 않은 포즈',
        'scene': '정보 전달 맥락이 느껴지는 정돈된 장면',
        'composition': '제목 가독성 우선, 인물과 텍스트 간 충돌 없는 안정 배치',
        'color': '중저채도 기반에 포인트 1-2색만 사용해 정돈된 대비 유지',
        'text_color': '메인/보조 텍스트를 단일 팔레트 내 명도 대비로 구분',
        'supporting_text': '보조 라벨은 작고 간결한 단어형으로 정보 보조만 수행',
        'focus_guard': '얼굴 윤곽과 눈 주변 디테일 선명 유지',
        'negative': '자극 과다 표정, 텍스트 난잡 배치, 채도 과잉 금지' },
    'mystery_curiosity': {
        'name': '호기심 유도형',
        'expression': '의문/긴장감이 섞인 표정, 감정의 여백을 남기는 얼굴',
        'gesture': '시선을 유도하는 측면 제스처(손/몸 방향) 사용',
        'scene': '단서가 보이지만 결론이 숨겨진 분위기의 장면',
        'composition': '여백을 활용해 제목 주목도 확보, 인물 시선과 텍스트 연결',
        'color': '어두운 톤 위 밝은 포인트로 대비를 만들되 과장 색상은 제한',
        'text_color': '메인은 강대비, 보조는 톤다운으로 시각 계층 유지',
        'supporting_text': '작은 코너 라벨로만 배치, 정보 힌트 역할에 한정',
        'focus_guard': '인물 얼굴은 항상 초점 고정, 배경은 필요 시만 블러',
        'negative': '배경 잡요소 과다, 인물보다 큰 텍스트 블록 금지' } }
_URGENT_PROFILE_IDS = [
    'urgent_conflict',
    'urgent_countdown',
    'dramatic_reveal']
_NORMAL_PROFILE_IDS = [
    'authority_explain',
    'mystery_curiosity',
    'dramatic_reveal']

def _is_urgent_title(title_text = None):
    pass
# WARNING: Decompyle incomplete


def _pick_rule_profile(title_text = None, index = None, urgent_mode = None):
    profile_ids = _URGENT_PROFILE_IDS if urgent_mode else _NORMAL_PROFILE_IDS
    if not profile_ids:
        return _RULE_PROFILES['dramatic_reveal']
    basis = f'''{None}:{index}'''
    selected_index = zlib.crc32(basis.encode('utf-8')) % len(profile_ids)
    return _RULE_PROFILES[profile_ids[selected_index]]


def build_character_focus_prompt_rules(title_text = None, has_character_reference = None, character_name = None, style_source = (0,), index = ('title_text', 'str', 'has_character_reference', 'bool', 'character_name', 'str', 'style_source', 'str', 'index', 'int', 'return', 'Dict[str, str]')):
    '''
    제목/레퍼런스 상태를 기반으로 썸네일 생성용 프롬프트 규칙을 반환.

    Returns:
        {
            subjectType,
            personDescription,
            personExpression,
            personPose,
            sceneDescription,
            additionalRequests,
            referenceNote,
            ruleProfileName,
        }
    '''
    urgent_mode = _is_urgent_title(title_text)
    profile = _pick_rule_profile(title_text = title_text, index = index, urgent_mode = urgent_mode)
    if has_character_reference:
        person_description = f'''{character_name} 중심 인물 클로즈업''' if character_name else '핵심 등장인물 클로즈업'
        subject_type = 'person'
        scene_description = ''
    else:
        person_description = ''
        subject_type = 'scene'
        scene_description = profile['scene']
    style_note = 'YouTube 레퍼런스 썸네일의 텍스트/색감/레이아웃 문법을 우선 참조' if style_source == 'youtube' else '프로젝트 스타일 템플릿 화풍을 유지하면서 인물 감정/행동 중심으로 구성'
    character_note = '캐릭터 레퍼런스 인물의 얼굴 정체성을 유지하고 표정/제스처만 강화' if has_character_reference else '장면 내 인물은 긴장감 있는 표정과 행동 동세를 우선 묘사'
    additional_requests = ' '.join([
        f'''규칙 프로필: {profile['name']}.''',
        f'''구도 규칙: {profile['composition']}.''',
        f'''포커스 규칙: {profile['focus_guard']}.''',
        f'''색상 규칙: {profile['color']}.''',
        f'''텍스트 색상 규칙: {profile['text_color']}.''',
        f'''보조 텍스트 규칙: {profile['supporting_text']}.''',
        f'''금지 규칙: {profile['negative']}.''',
        style_note + '.',
        character_note + '.'])
    return {
        'subjectType': subject_type,
        'personDescription': person_description,
        'personExpression': profile['expression'],
        'personPose': profile['gesture'],
        'sceneDescription': scene_description,
        'additionalRequests': additional_requests,
        'referenceNote': f'''자동 규칙: {profile['name']}''',
        'ruleProfileName': profile['name'] }
