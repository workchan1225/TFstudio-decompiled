# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: character_analyzer_service.pyc (Python 3.11)

'''
CharacterAnalyzerService - 대본 캐릭터 분석 서비스

대본에서 등장인물을 분석하여 추출하는 서비스입니다.
SceneImageService에서 분리됨 (Phase 2 리팩토링)
'''
import re
import json
import time
from typing import List, Dict, Optional, Any, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from costume_guide_loader import get_costume_guide
from app.services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
from app.utils.speaker_normalizer import is_valid_speaker_name as _is_valid_speaker_name_util, canonicalize_speaker_name as _canonicalize_speaker_name_util

try:
    from json_repair import repair_json as repair_broken_json
except ImportError:
    repair_broken_json = None


class CharacterAnalyzerService:
    '''대본 캐릭터 분석 서비스'''
    _GENDER_COSTUME_STYLE_PATTERNS = {
        'male': (re.compile('남성\\s*:\\s*(.*?)(?:(?:\\s*/\\s*)?여성\\s*:|$)'), re.compile('male\\s*:\\s*(.*?)(?:(?:\\s*/\\s*)?female\\s*:|$)', re.IGNORECASE)),
        'female': (re.compile('여성\\s*:\\s*(.*?)(?:(?:\\s*/\\s*)?남성\\s*:|$)'), re.compile('female\\s*:\\s*(.*?)(?:(?:\\s*/\\s*)?male\\s*:|$)', re.IGNORECASE)) }
    _get_status_costume = (lambda social_status = None, period = None, gender = staticmethod: pass# WARNING: Decompyle incomplete
)()
    _get_age_appearance_hint = (lambda age_range = None: if not age_range:
age_lower = ''.lower()age_num = 30nums = re.findall('\\d+', age_lower)if nums:
age_num = int(nums[0])if age_num <= 10 and '아이' in age_lower or '유아' in age_lower:
'- 동글동글하고 통통한 볼\n- 맑고 큰 눈동자\n- 작은 체구\n- 앳되고 순수한 인상'if None <= 19 and '10대' in age_lower or '청소년' in age_lower:
'- 어딘가 앳된 얼굴\n- 맑은 피부\n- 날씬하거나 아직 덜 자란 체형\n- 호기심 많은 표정'if None <= 29 or '20대' in age_lower:
'- 탄력 있고 매끈한 피부\n- 활력 있는 표정\n- 군살 없는 체형\n- 젊고 생기 넘치는 인상'if None <= 39 or '30대' in age_lower:
'- 성숙한 인상\n- 단단하고 자리잡은 체격\n- 자신감 있는 눈빛\n- 책임감 있는 분위기'if None <= 49 or '40대' in age_lower:
'- 잔잔한 잔주름 시작\n- 중후한 인상\n- 안정된 체격\n- 연륜이 느껴지는 눈빛'if None <= 59 or '50대' in age_lower:
'- 눈가와 이마에 주름\n- 흰머리 섞임\n- 중후하고 무게감 있는 체격\n- 노련한 인상'if None <= 69 or '60대' in age_lower:
'- 깊은 주름\n- 흰머리가 많음\n- 마른 체형 또는 복부 비만\n- 지혜로운 눈빛')()
    _get_role_hint = (lambda role = None, personality = None: if not role:
role_lower = ''.lower()if not personality:
personality_lower = ''.lower()role_hints = {
'주인공': '- 강한 존재감과 눈에 띄는 외모\n- 자신감 있는 표정',
'적대자': '- 날카롭고 차가운 인상\n- 위협적인 분위기',
'조력자': '- 믿음직한 인상\n- 따뜻한 눈빛',
'멘토': '- 지혜로운 인상\n- 노련한 분위기',
'신비로운존재': '- 초월적이고 신비로운 분위기\n- 인간을 넘어선 고고한 인상',
'조연': '- 자연스럽고 평범한 인상' }personality_hints = {
'온화': '- 부드러운 눈매와 미소',
'권위': '- 날카로운 눈빛과 굳은 표정',
'호기심': '- 반짝이는 눈동자와 밝은 표정',
'신비': '- 깊고 알 수 없는 눈빛',
'엄격': '- 굳은 표정과 냉정한 인상',
'다정': '- 따뜻한 미소와 부드러운 인상',
'냉정': '- 감정 없는 듯한 무표정',
'쾌활': '- 밝은 미소와 활기찬 인상' }result = []for key, hint in role_hints.items():
if key in role_lower:
result.append(hint)for key, hint in personality_hints.items():
if key in personality_lower:
result.append(hint)if result:
'\n'.join(result)f'''{role} 역할에 맞는 인상\n- {personality} 성격이 드러나는 표정''')()
    _infer_period_hint_from_script = (lambda script_text = None: pass# WARNING: Decompyle incomplete
)()
    _contains_keyword = (lambda text = None, keyword = None:
