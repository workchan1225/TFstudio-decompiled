# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: json_repair.pyc (Python 3.11)

'''
Gemini Vision API 응답의 잘못된 JSON 복구 유틸리티
- trailing comma 제거
- 잘린(truncated) JSON 복구
'''
import json
import re
import logging
logger = logging.getLogger(__name__)

def sanitize_gemini_json(response_text = None):
    '''Gemini 응답에서 JSON 블록을 추출하고 정제'''
    if '```json' in response_text:
        response_text = response_text.split('```json')[1].split('```')[0].strip()
    elif '```' in response_text:
        response_text = response_text.split('```')[1].split('```')[0].strip()
    response_text = re.sub(',\\s*([}\\]])', '\\1', response_text)
    return response_text


def parse_gemini_json(response_text = None):
    '''Gemini 응답 텍스트를 JSON으로 파싱 (자동 복구 포함)'''
    cleaned = sanitize_gemini_json(response_text)
    
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        first_error = None
        logger.warning(f'''JSON 파싱 실패, 복구 시도: {first_error}''')
        repaired = repair_truncated_json(cleaned)
        del first_error
        return None
        except json.JSONDecodeError:
            None, json.loads(repaired)
            raise first_error
        None = None
        del first_error



def repair_truncated_json(text = None):
    '''잘린 JSON 응답을 복구 시도'''
    in_string = False
    escape_next = False
    for ch in text:
        if escape_next:
            escape_next = False
            continue
        if ch == '\\':
            escape_next = True
            continue
        if ch == '"':
            in_string = not in_string
        if in_string:
            text += '"'
    text = re.sub(',\\s*"[^"]*"?\\s*$', '', text)
    text = re.sub(',\\s*$', '', text)
    open_braces = text.count('{') - text.count('}')
    open_brackets = text.count('[') - text.count(']')
    text += ']' * max(0, open_brackets)
    text += '}' * max(0, open_braces)
    text = re.sub(',\\s*([}\\]])', '\\1', text)
    return text
