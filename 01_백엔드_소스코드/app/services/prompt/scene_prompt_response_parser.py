# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_prompt_response_parser.pyc (Python 3.11)

'''
Helpers for parsing and validating scene prompt model responses.
'''
import re
from typing import Any, Dict

def extract_scene_prompt_json_text(response = None):
    '''
    LLM 응답에서 JSON 텍스트 블록을 추출한다.

    - ```json ... ``` 우선 처리
    - ``` ... ``` 일반 코드블록 처리
    - 마지막으로 중괄호 블록 탐색
    '''
    json_str = response
    if '```json' in response:
        parts = response.split('```json', 1)
        if len(parts) > 1:
            json_part = parts[1]
            if '```' in json_part:
                json_str = json_part.split('```', 1)[0].strip()
            else:
                json_str = json_part.strip()
        elif '```' in response:
            parts = response.split('```', 1)
            if len(parts) > 1:
                json_part = parts[1]
                if '```' in json_part:
                    json_str = json_part.split('```', 1)[0].strip()
                else:
                    json_str = json_part.strip()
    json_match = re.search('\\{[\\s\\S]*\\}', json_str, re.DOTALL)
    if not json_match:
        raise ValueError('No JSON found in AI response')
    return json_match.group()


def inspect_prompt_ko_quality(prompt_ko = None, narration_text = None):
