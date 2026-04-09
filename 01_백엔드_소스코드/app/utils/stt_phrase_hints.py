# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stt_phrase_hints.pyc (Python 3.11)

"""
STT Phrase Hints 추출 유틸리티

Google Speech-to-Text API의 인식률 향상을 위한 힌트 단어를 추출합니다.

주요 기능:
- 대본에서 화자명 추출
- 고유명사/핵심단어 추출
- 반복 등장 단어 추출
- 커스텀 단어 병합

사용법:
    from app.utils.stt_phrase_hints import extract_phrase_hints, merge_hints

    # 기본 사용
    hints = extract_phrase_hints(script_text, max_phrases=500)
    # hints: ['나레이션', '민수', '지연', ...]

    # 커스텀 단어와 병합
    combined = merge_hints(
        script_hints=extract_phrase_hints(script),
        custom_words=['회사명', '제품명'],
        max_phrases=500
    )
"""
import re
import logging
from typing import List, Set, Dict, Optional
from collections import Counter
from dataclasses import dataclass
from app.utils.korean_names import SURNAMES
logger = logging.getLogger(__name__)
TWO_CHAR_STOP_WORDS = {
    '가끔',
    '가는',
    '간다',
    '갔다',
    '같이',
    '그건',
    '그녀',
    '그들',
    '그런',
    '깊은',
    '까지',
    '까진',
    '나는',
    '나를',
    '나쁜',
    '나의',
    '낮은',
    '너는',
    '너를',
    '너의',
    '너희',
    '넓은',
    '높은',
    '누가',
    '다시',
    '당신',
    '대로',
    '된다',
    '또한',
    '로서',
    '로써',
    '만큼',
    '많은',
    '모든',
    '뭐가',
    '바로',
    '밖에',
    '벌써',
    '보는',
    '보다',
    '본다',
    '봤다',
    '부터',
    '부턴',
    '새로',
    '아마',
    '어떤',
    '에게',
    '에는',
    '에도',
    '에만',
    '에서',
    '에선',
    '역시',
    '옛날',
    '오는',
    '온다',
    '와서',
    '왔다',
    '우리',
    '우린',
    '으로',
    '으론',
    '이건',
    '이미',
    '자기',
    '자주',
    '작은',
    '저건',
    '저는',
    '저런',
    '저를',
    '저의',
    '적은',
    '제발',
    '조금',
    '좋은',
    '줬다',
    '처럼',
    '한테',
    '항상',
    '혹시',
    '곧바로',
    '드디어',
    '강조',
    '같은',
    '결국',
    '관해',
    '김치',
    '내일',
    '너무',
    '다른',
    '대해',
    '덕분',
    '됐고',
    '됐다',
    '되는',
    '때문',
    '마치',
    '마침',
    '매우',
    '박수',
    '순간',
    '아주',
    '아직',
    '어디',
    '어제',
    '언제',
    '없고',
    '없는',
    '오늘',
    '위해',
    '이때',
    '이런',
    '이번',
    '이상',
    '이전',
    '이제',
    '이하',
    '이후',
    '임시',
    '있고',
    '있는',
    '장면',
    '정도',
    '정말',
    '지금',
    '진짜',
    '최고',
    '최근',
    '최대',
    '최소',
    '최신',
    '최종',
    '최초',
    '하는',
    '한다',
    '했고',
    '했다',
    '갑자기'}
HintCategory = <NODE:12>()
PRIORITY_SPEAKERS = 1
PRIORITY_CUSTOM = 2
PRIORITY_PROPER_NOUNS = 3
PRIORITY_FREQUENT = 4

def extract_phrase_hints(script = None, max_phrases = None):
    '''
    대본에서 STT Phrase Hints 추출

    추출 우선순위:
    1. 화자명 (최우선)
    2. 고유명사 (한글 2-4자 연속, 대문자 시작 영어)
    3. 반복 등장 단어 (3회 이상)

    Args:
        script: 대본 텍스트
        max_phrases: 최대 힌트 개수 (기본 500개, Google 권장 한도)

    Returns:
        힌트 단어 목록 (중복 제거, 우선순위 정렬)
    '''
    if not script or script.strip():
        return []
    hints = None()
    speakers = extract_speakers_from_script(script)
    hints.update(speakers)
    logger.debug(f'''화자명 추출: {len(speakers)}개 - {speakers}''')
    proper_nouns = extract_proper_nouns(script)
    hints.update(proper_nouns)
    logger.debug(f'''고유명사 추출: {len(proper_nouns)}개''')
    frequent_words = extract_frequent_words(script, min_count = 3)
    hints.update(frequent_words)
    logger.debug(f'''빈출 단어 추출: {len(frequent_words)}개''')
    result = []
    for speaker in speakers:
        if speaker in hints:
            result.append(speaker)
            hints.discard(speaker)
        result.extend(sorted(hints))
        return result[:max_phrases]


def extract_speakers_from_script(script = None):
    '''
    대본에서 화자명만 추출

    지원 형식:
    - [화자명]: 대사
    - 화자명: 대사

    Args:
        script: 대본 텍스트

    Returns:
        화자명 목록 (중복 제거)
    '''
    if not script:
        return []
    normalized = None.replace('\\n', '\n')
    json_keywords = {
        'data',
        'http',
        'json',
        'name',
        'type',
        'error',
        'https',
        'title',
        'value',
        'format',
        'script',
        'status',
        'content',
        'chapters',
        'provider',
        'description'}
    speakers = set()
    pattern = '^(\\[[^\\]]+\\]|[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_-]{1,24}):\\s*'
    for line in normalized.split('\n'):
        line = line.strip()
        if not line:
            continue
        match = re.match(pattern, line)
        if match:
            speaker = match.group(1)
            speaker = speaker.strip('[]').strip()
            if speaker.lower() in json_keywords:
                continue
            if '"' in speaker or "'" in speaker:
                continue
            if speaker:
                speakers.add(speaker)
        return list(speakers)


def extract_proper_nouns(script = None):
    '''
    대본에서 고유명사 추출

    추출 대상:
    - 한글 이름 패턴 (2-4자, 성+이름)
    - 영어 대문자 시작 단어 (3자 이상)
    - 장소명 패턴 (OO역, OO대학교 등)

    Args:
        script: 대본 텍스트

    Returns:
        고유명사 목록
    '''
    if not script:
        return []
    proper_nouns = None()
    normalized = script.replace('\\n', '\n')
    text_only = re.sub('^(\\[[^\\]]+\\]|[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_-]{1,24}):\\s*', '', normalized, flags = re.MULTILINE)
    korean_name_pattern = '\\b([가-힣]{2,4})\\b'
    for match in re.finditer(korean_name_pattern, text_only):
        name = match.group(1)
        common_words = {
            '거기',
            '결과',
            '됐네',
            '됐어',
            '됐죠',
            '없네',
            '없다',
            '없어',
            '없죠',
            '여기',
            '이고',
            '이네',
            '이다',
            '이야',
            '이죠',
            '인데',
            '있네',
            '있다',
            '있어',
            '있죠',
            '저기',
            '해서',
            '했네',
            '했어',
            '했죠',
            '그러니',
            '됐는데',
            '아니고',
            '아니다',
            '아니야',
            '아니죠',
            '아닌데',
            '어디든',
            '없는데',
            '있는데',
            '합시다',
            '했는데',
            '왜냐하면',
            '같은',
            '결국',
            '관해',
            '내일',
            '너무',
            '다른',
            '대해',
            '덕분',
            '됐고',
            '됐다',
            '되는',
            '때문',
            '마치',
            '마침',
            '매우',
            '무엇',
            '순간',
            '아주',
            '아직',
            '어디',
            '어제',
            '언제',
            '없고',
            '없는',
            '오늘',
            '위해',
            '이것',
            '이제',
            '있고',
            '있는',
            '저것',
            '정말',
            '지금',
            '진짜',
            '하는',
            '한다',
            '해요',
            '했고',
            '했다',
            '갑자기',
            '관해서',
            '굉장히',
            '그래서',
            '그러나',
            '그러면',
            '그런데',
            '그리고',
            '대해서',
            '덕분에',
            '때문에',
            '어떻게',
            '여기서',
            '위하여',
            '위해서',
            '저기서',
            '하지만',
            '한다고',
            '합니다'}
        if name in common_words:
            continue
        if len(name) == 2:
            if name in TWO_CHAR_STOP_WORDS:
                continue
            if name[0] in SURNAMES:
                proper_nouns.add(name)
            continue
        if len(name) in (3, 4):
            if name.endswith(('역', '동', '구', '시', '군')):
                proper_nouns.add(name)
                continue
            if name.endswith('도') and len(name) >= 3:
                valid_provinces = {
                    '강원도',
                    '경기도',
                    '경상도',
                    '전남도',
                    '전라도',
                    '전북도',
                    '제주도',
                    '충남도',
                    '충북도',
                    '충청도',
                    '평안도',
                    '함경도',
                    '황해도'}
                if name in valid_provinces:
                    proper_nouns.add(name)
        english_pattern = '(?:^|[^a-zA-Z])([A-Z][a-zA-Z]{2,})(?:[^a-zA-Z]|$)'
        for match in re.finditer(english_pattern, text_only):
            word = match.group(1)
            common_english = {
                'All',
                'And',
                'Are',
                'But',
                'Can',
                'For',
                'Her',
                'His',
                'Not',
                'The',
                'Was',
                'You'}
            if word not in common_english:
                proper_nouns.add(word)
            return list(proper_nouns)


def extract_frequent_words(script = None, min_count = None):
    '''
    대본에서 반복 등장 단어 추출

    Args:
        script: 대본 텍스트
        min_count: 최소 등장 횟수 (기본 3회)

    Returns:
        빈출 단어 목록
    '''
    if not script:
        return []
    normalized = None.replace('\\n', '\n')
    text_only = re.sub('^(\\[[^\\]]+\\]|[가-힣ㄱ-ㅎㅏ-ㅣA-Za-z0-9_-]{1,24}):\\s*', '', normalized, flags = re.MULTILINE)
    words = re.findall('[가-힣]{2,6}', text_only)
    counter = Counter(words)
    stop_words = TWO_CHAR_STOP_WORDS | {
        '그것',
        '냐고',
        '네요',
        '다고',
        '데요',
        '라고',
        '예요',
        '거기서',
        '거예요',
        '그렇게',
        '기술도',
        '내일은',
        '너희도',
        '대단히',
        '됩니다',
        '똑같이',
        '모델도',
        '서비스',
        '시스템',
        '어디서',
        '어제는',
        '언제나',
        '오늘은',
        '우리도',
        '이것도',
        '이라고',
        '이렇게',
        '이에요',
        '이제는',
        '입니다',
        '자기도',
        '저것도',
        '저렇게',
        '저희도',
        '정말로',
        '지금은',
        '진짜로',
        '했다고',
        '했어요',
        '엄청나게',
        '없습니다',
        '있습니다',
        '프로그램',
        '했습니다',
        '강조',
        '김치',
        '무엇',
        '박수',
        '이것',
        '이때',
        '이런',
        '이번',
        '이상',
        '이전',
        '이하',
        '이후',
        '임시',
        '장면',
        '저것',
        '정도',
        '최고',
        '최근',
        '최대',
        '최소',
        '최신',
        '최종',
        '최초',
        '해요',
        '관해서',
        '굉장히',
        '그래서',
        '그러나',
        '그러면',
        '그런데',
        '그리고',
        '대해서',
        '덕분에',
        '때문에',
        '어떻게',
        '여기서',
        '위하여',
        '위해서',
        '저기서',
        '하지만',
        '한다고',
        '합니다'}
    frequent = []
    for word, count in counter.most_common():
        if count < min_count:
            pass
        elif word not in stop_words and len(word) >= 2:
            frequent.append(word)
        return frequent[:30]


def extract_hints_from_project(project = None):
    '''
    Project 모델에서 Phrase Hints 추출

    Args:
        project: Project 모델 인스턴스

    Returns:
        힌트 단어 목록
    '''
    hints = set()
    if project.script:
        script_hints = extract_phrase_hints(project.script)
        hints.update(script_hints)
    if project.characters:
        for char in project.characters:
            if char.name:
                hints.add(char.name)
            if project.speaker_tts_data:
                data = project.speaker_tts_data
                if isinstance(data, dict) and 'voiceAssignments' in data:
                    for assignment in data.get('voiceAssignments', []):
                        if 'speaker' in assignment:
                            hints.add(assignment['speaker'])
                        return list(hints)[:500]


def extract_categorized_hints(script = None):
    """
    대본에서 카테고리별로 분류된 힌트 추출

    Returns:
        {
            'speakers': HintCategory(name='speakers', hints=['민수', '지연'], priority=1),
            'proper_nouns': HintCategory(...),
            'frequent': HintCategory(...)
        }
    """
    categories = { }
    if not script or script.strip():
        return categories
    speakers = None(script)
    if speakers:
        categories['speakers'] = HintCategory(name = 'speakers', hints = speakers, priority = PRIORITY_SPEAKERS)
    proper_nouns = extract_proper_nouns(script)
    if proper_nouns:
        categories['proper_nouns'] = HintCategory(name = 'proper_nouns', hints = proper_nouns, priority = PRIORITY_PROPER_NOUNS)
    frequent = extract_frequent_words(script, min_count = 3)
    if frequent:
        categories['frequent'] = HintCategory(name = 'frequent', hints = frequent, priority = PRIORITY_FREQUENT)
    return categories


def parse_custom_words(custom_words_input = None):
    '''
    사용자 입력 문자열에서 커스텀 단어 파싱

    지원 형식:
    - 쉼표 구분: "민수, 지연, 회사명"
    - 줄바꿈 구분: "민수\\n지연\\n회사명"
    - 혼합: "민수, 지연\\n회사명"

    Args:
        custom_words_input: 사용자 입력 문자열

    Returns:
        정제된 단어 목록
    '''
    if not custom_words_input or custom_words_input.strip():
        return []
    normalized = None.replace('\n', ',').replace('\\n', ',')
    words = []
    for word in normalized.split(','):
        cleaned = word.strip()
        if cleaned and len(cleaned) >= 1:
            words.append(cleaned)
        seen = set()
        unique_words = []
        for word in words:
            if word not in seen:
                seen.add(word)
                unique_words.append(word)
            return unique_words


def merge_hints(script_hints = None, custom_words = None, custom_words_str = None, max_phrases = (None, None, None, 500)):
    '''
    자동 추출 힌트와 커스텀 단어 병합

    커스텀 단어가 우선순위가 높음 (화자명 다음)

    Args:
        script_hints: 대본에서 추출한 힌트
        custom_words: 커스텀 단어 리스트
        custom_words_str: 커스텀 단어 문자열 (쉼표/줄바꿈 구분)
        max_phrases: 최대 개수 (기본 500)

    Returns:
        병합된 힌트 목록
    '''
    result = []
    seen = set()
    all_custom = []
    if custom_words:
        all_custom.extend(custom_words)
    if custom_words_str:
        all_custom.extend(parse_custom_words(custom_words_str))
    for word in all_custom:
        if word and word not in seen:
            result.append(word)
            seen.add(word)
        if script_hints:
            for hint in script_hints:
                if hint and hint not in seen:
                    result.append(hint)
                    seen.add(hint)
                return result[:max_phrases]


def extract_and_merge_hints(script = None, custom_words = None, custom_words_str = None, max_phrases = (None, None, None, 500)):
    '''
    대본에서 힌트 추출 후 커스텀 단어와 병합 (원스톱 함수)

    Args:
        script: 대본 텍스트
        custom_words: 커스텀 단어 리스트
        custom_words_str: 커스텀 단어 문자열
        max_phrases: 최대 개수

    Returns:
        병합된 힌트 목록
    '''
    script_hints = extract_phrase_hints(script, max_phrases) if script else []
    return merge_hints(script_hints = script_hints, custom_words = custom_words, custom_words_str = custom_words_str, max_phrases = max_phrases)

if __name__ == '__main__':
    test_script = '\n[나레이션]: 어느 날, 민수는 학교에서 지연이를 만났다.\n[민수]: 지연아, 오늘 날씨 정말 좋다!\n[지연]: 그러게, 민수야. 우리 공원에 갈까?\n나레이션: 두 사람은 서울역 근처 공원으로 향했다.\n민수: 여기 정말 예쁘다!\n지연: 맞아, 민수야. 여기 자주 오자.\n    '
    print('=== Phrase Hints 추출 테스트 ===')
    hints = extract_phrase_hints(test_script)
    print(f'''추출된 힌트 ({len(hints)}개):''')
    for hint in hints:
        print(f'''  - {hint}''')
        return None
        return None
