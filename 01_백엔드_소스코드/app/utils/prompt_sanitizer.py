# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: prompt_sanitizer.pyc (Python 3.11)

__doc__ = '\n프롬프트 정화 유틸리티\n\n이미지 생성 프롬프트에서 정책 위반 가능성이 있는 표현을 완화합니다.\n- 얼굴/눈 영역의 피/피눈물/핏발 표현 제거\n- 폭력적 표현 완화\n- 정책 위반 키워드 감지\n- 눈물 색상 명확화 (붉은색/피 방지)\n'
import re
from typing import Tuple, List
FACE_BLOOD_PATTERNS_KO = [
    '핏발\\s*선\\s*눈',
    '피눈물',
    '피\\s*묻은\\s*얼굴',
    '피\\s*범벅\\s*얼굴',
    '피\\s*흘리는\\s*눈',
    '눈에서\\s*피',
    '입에서\\s*피',
    '코피',
    '피\\s*튀는\\s*얼굴']
FACE_BLOOD_PATTERNS_EN = [
    'bloodshot\\s*eyes?',
    'blood\\s*tears?',
    'blood\\s*on\\s*face',
    'bloody\\s*face',
    'blood\\s*from\\s*eyes?',
    'bleeding\\s*eyes?',
    'blood\\s*dripping\\s*from\\s*face',
    'blood-stained\\s*face',
    'bloody\\s*tears?',
    'nosebleed',
    'bloody\\s*eyes?']
REPLACEMENTS_KO = {
    '핏발\\s*선\\s*눈': '지친 눈',
    '피눈물': '눈물',
    '피\\s*묻은\\s*얼굴': '창백한 얼굴',
    '피\\s*범벅\\s*얼굴': '창백한 얼굴',
    '피\\s*흘리는\\s*눈': '지친 눈',
    '코피': '지친 표정' }
REPLACEMENTS_EN = {
    'bloodshot\\s*eyes?': 'tired eyes',
    'blood\\s*tears?': 'tears',
    'blood\\s*on\\s*face': 'pale face',
    'bloody\\s*face': 'pale face',
    'blood\\s*from\\s*eyes?': 'tears',
    'bleeding\\s*eyes?': 'tired eyes',
    'blood-stained\\s*face': 'pale face',
    'bloody\\s*tears?': 'tears',
    'nosebleed': 'tired expression',
    'bloody\\s*eyes?': 'tired eyes' }
POLICY_VIOLATION_KEYWORDS = [
    'gore',
    'gory',
    'dismember',
    'decapitat',
    'mutilat',
    'torture',
    'torturing',
    'graphic violence',
    'nude',
    'naked',
    'explicit',
    'sexual',
    'self-harm',
    'suicide',
    '고어',
    '잔인한',
    '처형',
    '고문',
    '성인']
TEARS_PATTERNS_KO = [
    '눈물',
    '울[었으면고]',
    '울음',
    '흐느끼',
    '통곡',
    '오열',
    '눈시울',
    '눈가[가에]']
TEARS_PATTERNS_EN = [
    '\\btears?\\b',
    '\\bcrying\\b',
    '\\bsobbing\\b',
    '\\bweeping\\b',
    '\\btearful\\b',
    '\\bteary\\b',
    '\\btear-filled\\b',
    '\\btear[\\s-]?drop']
TEARS_ENHANCEMENT_KO = {
    '(?<!맑[고은])\\s*눈물\\s*방울': '맑은 눈물 방울' }
TEARS_ENHANCEMENT_EN = {
    '(?<!clear\\s)(?<!transparent\\s)(?<!wet\\s)(?<!glistening\\s)\\btears\\b(?!\\s+of\\s+joy)': 'clear transparent wet tears reflecting light naturally',
    '(?<!clear\\s)(?<!transparent\\s)\\btear\\b(?!\\s+of\\s+joy)': 'clear transparent wet tear',
    '\\bteardrops?\\b': 'clear wet teardrops' }
TEARS_NEGATIVE_ADDITIONS = [
    'blood tears',
    'red tears',
    'bloody tears',
    'crimson tears',
    'pink tears',
    'red-tinted tears',
    'blood from eyes',
    'bleeding eyes',
    'red liquid from eyes',
    'dark tears',
    'black tears',
    'colored tears',
    'white tears',
    'opaque tears',
    'milky tears',
    'cloudy tears',
    'solid tears',
    'thick tears',
    'creamy tears',
    'pale tears',
    'glowing tears',
    'luminous tears',
    'bright white tears']

def sanitize_face_blood_expressions(prompt = None, language = None):
    """
    프롬프트에서 얼굴/눈 영역의 피 관련 표현을 완화합니다.

    Args:
        prompt: 원본 프롬프트
        language: 'ko', 'en', 또는 'auto' (자동 감지)

    Returns:
        정화된 프롬프트
    """
    result = prompt
    if language == 'auto':
        has_korean = bool(re.search('[가-힣]', prompt))
        has_english = bool(re.search('[a-zA-Z]', prompt))
    else:
        has_korean = language == 'ko'
        has_english = language == 'en'
    if has_korean:
        for pattern, replacement in REPLACEMENTS_KO.items():
            result = re.sub(pattern, replacement, result, flags = re.IGNORECASE)
            for pattern in FACE_BLOOD_PATTERNS_KO:
                if pattern not in REPLACEMENTS_KO:
                    result = re.sub(pattern, '', result, flags = re.IGNORECASE)
                if has_english:
                    for pattern, replacement in REPLACEMENTS_EN.items():
                        result = re.sub(pattern, replacement, result, flags = re.IGNORECASE)
                        for pattern in FACE_BLOOD_PATTERNS_EN:
                            if pattern not in REPLACEMENTS_EN:
                                result = re.sub(pattern, '', result, flags = re.IGNORECASE)
                            result = re.sub(',\\s*,', ',', result)
                            result = re.sub('\\s+', ' ', result)
                            result = result.strip(' ,')
                            return result


def check_policy_violation_risk(prompt = None):
    '''
    프롬프트의 정책 위반 위험성을 검사합니다.

    Args:
        prompt: 검사할 프롬프트

    Returns:
        (위험 여부, 감지된 키워드 목록)
    '''
    prompt_lower = prompt.lower()
    detected = []
    for keyword in POLICY_VIOLATION_KEYWORDS:
        if keyword.lower() in prompt_lower:
            detected.append(keyword)
        return (len(detected) > 0, detected)


def get_policy_violation_message(error_message = None):
    '''
    에러 메시지에서 정책 위반 관련 내용을 감지하고
    사용자 친화적인 메시지를 반환합니다.

    Args:
        error_message: 원본 에러 메시지

    Returns:
        사용자 친화적인 에러 메시지
    '''
    pass
# WARNING: Decompyle incomplete


def detect_tears_in_prompt(prompt = None):
    '''
    프롬프트에 눈물 관련 표현이 있는지 감지합니다.

    Args:
        prompt: 검사할 프롬프트

    Returns:
        눈물 표현 포함 여부
    '''
    for pattern in TEARS_PATTERNS_KO:
        if re.search(pattern, prompt, re.IGNORECASE):
            return True
        for pattern in TEARS_PATTERNS_EN:
            if re.search(pattern, prompt, re.IGNORECASE):
                return True
            return False


def enhance_tears_clarity(prompt = None, language = None):
    """
    눈물 포함 프롬프트에 색상 명확성을 추가합니다.
    이미지 생성 AI가 눈물을 붉은색/피로 렌더링하는 것을 방지합니다.

    Args:
        prompt: 원본 프롬프트
        language: 'ko', 'en', 또는 'auto' (자동 감지)

    Returns:
        Tuple[str, str]: (향상된 프롬프트, 추가할 네거티브 프롬프트)
    """
    result = prompt
    negative_additions = ''
    has_tears = detect_tears_in_prompt(prompt)
    if not has_tears:
        return (result, negative_additions)
    if None == 'auto':
        has_korean = bool(re.search('[가-힣]', prompt))
        has_english = bool(re.search('[a-zA-Z]', prompt))
    else:
        has_korean = language == 'ko'
        has_english = language == 'en'
    already_clear_ko = bool(re.search('맑[고은]|투명[한]', prompt))
    already_clear_en = bool(re.search('clear|transparent|crystal', prompt, re.IGNORECASE))
    if not has_korean and already_clear_ko:
        for pattern, replacement in TEARS_ENHANCEMENT_KO.items():
            result = re.sub(pattern, replacement, result)
            if not has_english and already_clear_en:
                for pattern, replacement in TEARS_ENHANCEMENT_EN.items():
                    result = re.sub(pattern, replacement, result, flags = re.IGNORECASE)
                    negative_additions = ', '.join(TEARS_NEGATIVE_ADDITIONS)
                    print('[PromptSanitizer] Tears detected, adding clarity enhancement and negative prompt')
                    return (result, negative_additions)


def sanitize_prompt_for_image_generation(prompt = None, return_negative = None):
    '''
    이미지 생성을 위해 프롬프트를 전체적으로 정화합니다.

    Args:
        prompt: 원본 프롬프트
        return_negative: 추가 네거티브 프롬프트 반환 여부

    Returns:
        Tuple[str, str]: (정화된 프롬프트, 추가 네거티브 프롬프트)
        return_negative=False일 경우 하위 호환성을 위해 str만 반환
    '''
    result = sanitize_face_blood_expressions(prompt)
    (result, tears_negative) = enhance_tears_clarity(result)
    (is_risky, keywords) = check_policy_violation_risk(result)
    if is_risky:
        print(f'''[PromptSanitizer] Warning: Potentially risky keywords detected: {keywords}''')
    if return_negative:
        return (result, tears_negative)


def sanitize_prompt_simple(prompt = None):
    '''
    하위 호환성을 위한 단순 정화 함수.
    네거티브 프롬프트 없이 정화된 프롬프트만 반환합니다.
    '''
    (result, _) = sanitize_prompt_for_image_generation(prompt, return_negative = True)
    return result

# WARNING: Decompyle incomplete
