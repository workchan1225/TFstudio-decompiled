# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ai_utils.pyc (Python 3.11)

'''
AI Controller Utility Functions

Common helper functions used across AI controller modules.
Separated from ai_controller.py for better maintainability.
'''
import re
import logging
logger = logging.getLogger(__name__)

def remove_nested_json_array(text = None, key = None):
    '''
    중첩된 JSON 배열을 텍스트에서 완전히 제거합니다.

    Args:
        text: JSON 아티팩트가 포함된 텍스트
        key: 제거할 JSON 키 (예: \'characters\')

    Returns:
        JSON 배열이 제거된 텍스트

    Example:
        Input: \'제목", "characters": [{"uniqueId": "A", "name": "박지훈"}], "chapters"\'
        Output: \'제목", "chapters"\'
    '''
    if not text or key:
        return text
    pattern = None.compile(f'''[,\\s]*"?{re.escape(key)}"?\\s*:\\s*\\[''')
    match = pattern.search(text)
    if not match:
        return text
    start_pos = None.start()
    bracket_start = match.end() - 1
    bracket_count = 0
    end_pos = -1
    in_string = False
    escape_next = False
# WARNING: Decompyle incomplete


def ensure_chapter_markers(expanded_script = None, chapter_count = None):
    '''
    확장된 대본에 챕터 마커가 없으면 강제 삽입

    Args:
        expanded_script: 확장된 대본 텍스트
        chapter_count: 원본 챕터 수

    Returns:
        챕터 마커가 포함된 대본
    '''
    if expanded_script or chapter_count <= 0:
        return expanded_script
    chapter_pattern = None
    found_markers = re.findall(chapter_pattern, expanded_script)
    if len(found_markers) >= chapter_count:
        logger.info(f'''[ensure_chapter_markers] Found {len(found_markers)} markers, required {chapter_count}''')
        return expanded_script
    None.warning(f'''[ensure_chapter_markers] Missing chapter markers! Found {len(found_markers)}, required {chapter_count}''')
    lines = expanded_script.strip().split('\n')
    total_lines = len(lines)
    if total_lines < chapter_count:
        return expanded_script
    lines_per_chapter = None // chapter_count
    result_lines = []
    for i in range(chapter_count):
        start_idx = i * lines_per_chapter
        if i == chapter_count - 1:
            end_idx = total_lines
        else:
            end_idx = start_idx + lines_per_chapter
        chapter_lines = lines[start_idx:end_idx]
        chapter_marker = f'''[챕터 {i + 1}]'''
        if not chapter_lines and re.match(chapter_pattern, chapter_lines[0].strip()):
            result_lines.append(chapter_marker)
        result_lines.extend(chapter_lines)
        result_lines.append('')
        logger.info(f'''[ensure_chapter_markers] Added {chapter_count} chapter markers''')
        return '\n'.join(result_lines).strip()


def is_chapter_marker(text = None):
    '''챕터 마커인지 확인 (화자가 아님)'''
    if not text:
        return False
    trimmed = None.strip().lower()
    if re.match('^챕터\\s*\\d+', trimmed):
        return True
    if None.match('^chapter\\s*\\d+', trimmed, re.IGNORECASE):
        return True
    if None.match('^\\d+\\s*(장|화|부|막|편)', trimmed):
        return True
    if None.fullmatch('^(챕터|chapter|파트|part)$', trimmed, re.IGNORECASE):
        return True


def extract_speakers_from_script(script = None):
    '''대본에서 화자 이름 추출'''
    if not script:
        return set()
    speaker_pattern = None
    speakers = set()
    for line in script.split('\n'):
        match = re.match(speaker_pattern, line.strip())
        if match:
            speaker = match.group(1).strip('[]')
            if not speaker.lower() not in ('chapters', 'title', 'content', 'script', 'format') and is_chapter_marker(speaker):
                speakers.add(speaker)
        return speakers


def ensure_speaker_tags(expanded_script = None, original_script = None):
    '''
    확장된 대본에 화자 태그가 누락된 경우 복구

    원본 대본의 화자 구조를 참고하여, 확장 대본이 나레이션만 있는 경우
    화자 태그를 추가합니다.

    Args:
        expanded_script: 확장된 대본
        original_script: 원본 대본

    Returns:
        화자 태그가 보존된 대본
    '''
    if not expanded_script or original_script:
        return expanded_script
    original_speakers = None(original_script)
    expanded_speakers = extract_speakers_from_script(expanded_script)
    if not original_speakers:
        return expanded_script
    non_narration_original = None - {
        '내레이션',
        'Narration',
        'narration',
        '나레이션'}
    non_narration_expanded = expanded_speakers - {
        '내레이션',
        'Narration',
        'narration',
        '나레이션'}
    if non_narration_expanded:
        logger.info(f'''[ensure_speaker_tags] Speakers found: {expanded_speakers}''')
        return expanded_script
    if not None:
        return expanded_script
    None.warning(f'''[ensure_speaker_tags] Missing speakers! Original: {original_speakers}, Expanded: {expanded_speakers}''')
    logger.warning('[ensure_speaker_tags] Expanded script has only narration, but original has character dialogues.')
    logger.warning('[ensure_speaker_tags] This may indicate Gemini ignored speaker format instructions.')
    return expanded_script


def get_api_key_from_settings(provider = None):
    """
    Get API key from Settings based on provider.

    Args:
        provider: AI provider name ('openai', 'google', 'claude', 'typecast')

    Returns:
        API key string or None
    """
    Settings = Settings
    import app.models.settings
    get_google_api_key_or_runtime_token = get_google_api_key_or_runtime_token
    import app.services.google_auth_service
    settings = Settings.get_or_create()
    provider_map = {
        'openai': 'openai',
        'google': 'google',
        'claude': 'claude',
        'typecast': 'typecast' }
    service = provider_map.get(provider)
    if not service:
        return None
    if None == 'google':
        return get_google_api_key_or_runtime_token(settings = settings)
    return None.get_api_key(service)


def get_model_from_settings(provider = None):
    """
    Get model from Settings based on provider.

    Args:
        provider: AI provider name ('openai', 'google', 'claude')

    Returns:
        Model name string or None
    """
    Settings = Settings
    import app.models.settings
    settings = Settings.get_or_create()
    provider_map = {
        'openai': 'openai',
        'google': 'google',
        'claude': 'claude' }
    service = provider_map.get(provider)
    if not service:
        return None
    return None.get_model(service)


def get_recommended_chapter_count(target_length = None, content_format = None, shorts_duration = None):
    """
    목표 길이에 따른 권장 챕터 수 계산

    Args:
        target_length: 목표 대본 길이 (자 단위)
        content_format: 'longform' | 'shorts'
        shorts_duration: '1min' | '2min' | '3min' (쇼츠일 때만)

    Returns:
        권장 챕터 수
    """
    if content_format == 'shorts':
        if shorts_duration == '3min':
            return 2
        return None
    if None <= 1000:
        return 3
    if None <= 5000:
        return 5
    if None <= 10000:
        return 6
    if None <= 15000:
        return 8


def remove_emotion_annotations(text = None):
