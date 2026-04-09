# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ssml_utils.pyc (Python 3.11)

'''
SSML 유틸리티

Google Cloud TTS의 SSML(Speech Synthesis Markup Language) 처리를 위한 유틸리티 함수들.
타임포인트 기능을 위한 <mark> 태그 자동 삽입 등을 제공합니다.
'''
import re
from typing import List, Tuple
import logging
logger = logging.getLogger(__name__)

def extract_sentences(text = None):
    '''
    텍스트에서 문장 단위로 분리

    줄바꿈과 문장 부호(마침표, 물음표, 느낌표)를 기준으로 분리합니다.
    Edge TTS와 동일한 방식으로 자막을 분리합니다.

    Args:
        text: 입력 텍스트

    Returns:
        문장 리스트
    '''
    if not text or text.strip():
        return []
    lines = None.strip().split('\n')
    sentences = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        sentence_pattern = '(?<=[.!?。！？])\\s*'
        line_sentences = re.split(sentence_pattern, line)
        line_sentences = line_sentences()
        sentences.extend(line_sentences)
        if not sentences:
            return [
                text.strip()]
        (lambda .0: pass# WARNING: Decompyle incomplete
).debug(f'''문장 분리 결과: {len(sentences)}개''')
        return sentences


def insert_ssml_marks(text = None, sentences = None):
    '''
    텍스트에 SSML <mark> 태그 자동 삽입

    각 문장 앞에 마크를 삽입하여 타임포인트를 추출할 수 있게 합니다.

    Args:
        text: 원본 텍스트
        sentences: 미리 분리된 문장 리스트 (없으면 자동 분리)

    Returns:
        SSML 형식의 문자열

    Example:
        입력: "안녕하세요. 반갑습니다."
        출력: "<speak><mark name=\'s0\'/>안녕하세요. <mark name=\'s1\'/>반갑습니다.</speak>"
    '''
    if not text or text.strip():
        return '<speak></speak>'
# WARNING: Decompyle incomplete


def escape_ssml(text = None):
    '''
    SSML 특수 문자 이스케이프

    Args:
        text: 원본 텍스트

    Returns:
        이스케이프된 텍스트
    '''
    if not text:
        return ''
    text = None.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = text.replace('"', '&quot;')
    text = text.replace("'", '&apos;')
    return text


def insert_ssml_marks_for_speaker(dialogues = None, speaker = None):
    """
    화자별 대사에 SSML 마크 삽입

    Args:
        dialogues: [{'lineIndex': int, 'content': str, ...}, ...]
        speaker: 화자 이름

    Returns:
        (ssml_text, mark_mapping)
        - ssml_text: SSML 형식 텍스트
        - mark_mapping: [{'mark_name': 's0', 'lineIndex': 0, 'content': '...'}, ...]
    """
    if not dialogues:
        return ('<speak></speak>', [])
    ssml_parts = [
        None]
    mark_mapping = []
    for i, dialogue in enumerate(dialogues):
        line_index = dialogue.get('lineIndex', i)
        content = dialogue.get('content', '').strip()
        if not content:
            continue
        mark_name = f'''s{i}'''
        escaped_content = escape_ssml(content)
        ssml_parts.append(f'''<mark name=\'{mark_name}\'/>{escaped_content} ''')
        mark_mapping.append({
            'mark_name': mark_name,
            'lineIndex': line_index,
            'content': content })
        ssml_parts.append('</speak>')
        ssml_text = ''.join(ssml_parts)
        logger.debug(f'''[{speaker}] SSML 생성: {len(mark_mapping)}개 대사''')
        return (ssml_text, mark_mapping)


def parse_speaker_text(text = None):
    '''
    화자:대사 형식의 텍스트 파싱

    Args:
        text: "나레이션: 옛날 옛적에...
민수: 안녕!"

    Returns:
        [{\'speaker\': \'나레이션\', \'text\': \'옛날 옛적에...\'}, ...]
    '''
    if not text or text.strip():
        return []
    lines = None.split('\n')
    segments = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        match = re.match('^(\\[[^\\]]+\\]|[^:\\[\\]]+):\\s*(.*)$', line)
        if match:
            speaker = match.group(1).strip()
            dialogue = match.group(2).strip()
            speaker = re.sub('^\\[|\\]$', '', speaker).strip()
            if dialogue:
                segments.append({
                    'speaker': speaker,
                    'text': dialogue })
            continue
        segments.append({
            'speaker': 'narrator',
            'text': line })
        return segments


def create_ssml_with_prosody(text = None, rate = None, pitch = None, volume = (1, '0st', 'medium')):
    '''
    음성 속성이 포함된 SSML 생성

    Args:
        text: 텍스트
        rate: 속도 (0.25 ~ 4.0)
        pitch: 피치 ("-10st" ~ "+10st" 또는 "x-low", "low", "medium", "high", "x-high")
        volume: 볼륨 ("silent", "x-soft", "soft", "medium", "loud", "x-loud")

    Returns:
        SSML 텍스트
    '''
    sentences = extract_sentences(text)
    if not sentences:
        return '<speak></speak>'
    rate_percent = f'''{None(rate * 100)}%'''
    ssml_parts = [
        '<speak>']
    ssml_parts.append(f'''<prosody rate=\'{rate_percent}\' pitch=\'{pitch}\' volume=\'{volume}\'>''')
    for i, sentence in enumerate(sentences):
        escaped_sentence = escape_ssml(sentence)
        ssml_parts.append(f'''<mark name=\'s{i}\'/>{escaped_sentence} ''')
        ssml_parts.append('</prosody>')
        ssml_parts.append('</speak>')
        return ''.join(ssml_parts)


def create_ssml_with_breaks(sentences = None, break_time = None):
    '''
    문장 사이에 휴지(break)가 포함된 SSML 생성

    Args:
        sentences: 문장 리스트
        break_time: 휴지 시간 (예: "500ms", "1s")

    Returns:
        SSML 텍스트
    '''
    if not sentences:
        return '<speak></speak>'
    ssml_parts = [
        None]
    for i, sentence in enumerate(sentences):
        escaped_sentence = escape_ssml(sentence)
        ssml_parts.append(f'''<mark name=\'s{i}\'/>{escaped_sentence}''')
        if i < len(sentences) - 1:
            ssml_parts.append(f'''<break time=\'{break_time}\'/>''')
        ssml_parts.append('</speak>')
        return ''.join(ssml_parts)


def validate_ssml(ssml_text = None):
    '''
    SSML 유효성 검사

    Args:
        ssml_text: 검사할 SSML 텍스트

    Returns:
        (is_valid, error_message)
    '''
    if not ssml_text:
        return (False, 'SSML 텍스트가 비어 있습니다')
    if not None.strip().startswith('<speak>'):
        return (False, 'SSML은 <speak>로 시작해야 합니다')
    if not None.strip().endswith('</speak>'):
        return (False, 'SSML은 </speak>로 끝나야 합니다')
    
    try:
        
        ElementTree
        ET.fromstring(ssml_text)
        return (True, '')
    except ET.ParseError:
        None = None
        del e
        return None
        None = 
        del e



def clean_text_for_tts(text = None):
    '''
    TTS용 텍스트 정리

    불필요한 공백, 특수 문자 등을 정리합니다.

    Args:
        text: 원본 텍스트

    Returns:
        정리된 텍스트
    '''
    if not text:
        return ''
    text = None.sub('\\s+', ' ', text)
    text = text.strip()
    text = re.sub('https?://\\S+', '', text)
    text = re.sub('\\S+@\\S+', '', text)
    text = re.sub('[.!?]{2,}', '.', text)
    return text.strip()


def wrap_english_with_lang_tag(text = None):
    '''
    영어 부분을 SSML <lang> 태그로 감싸기 (Google TTS Standard/Neural2용)

    한글 텍스트에 포함된 영어 단어/문장을 감지하여 <lang xml:lang="en-US">로 감쌉니다.
    이를 통해 Google TTS가 영어 부분을 올바르게 발음합니다.

    ⚠️ SSML 특수문자(&, <, >, ", \')도 자동으로 이스케이프합니다.
    ⚠️ 기존 SSML 태그는 보존됩니다.

    Args:
        text: 원본 텍스트

    Returns:
        <lang> 태그가 적용된 SSML-safe 텍스트

    Example:
        입력: "안녕하세요 Hello World 입니다"
        출력: "안녕하세요 <lang xml:lang="en-US">Hello World</lang> 입니다"
    '''
    pass
# WARNING: Decompyle incomplete


def wrap_english_with_sub_tag(text = None):
    '''
    영어를 한글 발음으로 대체 (Chirp 3 HD용 - <lang> 태그 미지원)

    Chirp 3 HD는 <lang> 태그를 지원하지 않으므로,
    등록된 약어/단어에 대해 <sub> 태그로 한글 발음을 지정합니다.

    Args:
        text: 원본 텍스트

    Returns:
        <sub> 태그가 적용된 텍스트

    Example:
        입력: "AI 기술과 FBI 수사관"
        출력: "<sub alias="에이아이">AI</sub> 기술과 <sub alias="에프비아이">FBI</sub> 수사관"
    '''
    pass
# WARNING: Decompyle incomplete


def detect_mixed_korean_english(text = None):
