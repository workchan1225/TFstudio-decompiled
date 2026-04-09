# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shorts_analyzer_service.pyc (Python 3.11)

'''
Shorts Analyzer Service

자막 텍스트를 분석하여 YouTube Shorts에 적합한 하이라이트 구간을 추출합니다.
Gemini API를 사용하여 감정/핵심 장면을 자동으로 식별합니다.
'''
import re
import json
import logging
from typing import List, Dict, Any, Optional
from pathlib import Path
from app.models.project import Project
from app.models.settings import Settings
from app.services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
logger = logging.getLogger(__name__)

class ShortsAnalyzerService:
    '''자막 기반 쇼츠 하이라이트 분석 서비스'''
    CRITERIA_TYPES = {
        'emotional': '감정적 장면',
        'key_dialogue': '핵심 대사',
        'climax': '클라이맥스',
        'comedy': '코미디 장면',
        'action': '액션 장면',
        'twist': '반전 장면' }
    parse_srt_subtitles = (lambda srt_content = None: subtitles = []pattern = '(\\d+)\\s*\\n(\\d{2}:\\d{2}:\\d{2},\\d{3})\\s*-->\\s*(\\d{2}:\\d{2}:\\d{2},\\d{3})\\s*\\n((?:(?!\\d+\\s*\\n\\d{2}:\\d{2}:\\d{2}).)+)'matches = re.findall(pattern, srt_content, re.DOTALL)for match in matches:
index = int(match[0])start_time = match[1]end_time = match[2]text = match[3].strip().replace('\n', ' ')subtitles.append({
'index': index,
'start_time': start_time.replace(',', '.'),
'end_time': end_time.replace(',', '.'),
'start_seconds': ShortsAnalyzerService._time_to_seconds(start_time),
'end_seconds': ShortsAnalyzerService._time_to_seconds(end_time),
'text': text })subtitles)()
    parse_ass_subtitles = (lambda ass_content = None: subtitles = []pattern = 'Dialogue:\\s*\\d+,(\\d+:\\d{2}:\\d{2}\\.\\d{2}),(\\d+:\\d{2}:\\d{2}\\.\\d{2}),([^,]*),([^,]*),\\d+,\\d+,\\d+,([^,]*),(.*?)$'lines = ass_content.split('\n')index = 1for line in lines:
match = re.match(pattern, line, re.IGNORECASE)if match:
start_time = match.group(1)end_time = match.group(2)text = match.group(6).strip()text = re.sub('\\{[^}]*\\}', '', text)text = text.replace('\\N', ' ').replace('\\n', ' ')if text:
subtitles.append({
'index': index,
'start_time': start_time,
'end_time': end_time,
'start_seconds': ShortsAnalyzerService._ass_time_to_seconds(start_time),
'end_seconds': ShortsAnalyzerService._ass_time_to_seconds(end_time),
'text': text })index += 1subtitles)()
    _time_to_seconds = (lambda time_str = None: time_str = time_str.replace(',', '.')parts = time_str.split(':')hours = int(parts[0])minutes = int(parts[1])seconds = float(parts[2])hours * 3600 + minutes * 60 + seconds)()
    _ass_time_to_seconds = (lambda time_str = None: parts = time_str.split(':')hours = int(parts[0])minutes = int(parts[1])seconds = float(parts[2])hours * 3600 + minutes * 60 + seconds)()
    _seconds_to_time = (lambda seconds = None: hours = int(seconds // 3600)minutes = int((seconds % 3600) // 60)secs = int(seconds % 60)f'''{hours:02d}:{minutes:02d}:{secs:02d}''')()
    get_subtitles_from_project = (lambda project = None:
