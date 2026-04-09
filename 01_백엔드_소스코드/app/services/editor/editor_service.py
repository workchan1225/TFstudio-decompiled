# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: editor_service.pyc (Python 3.11)

'''
Editor Service

Handles saving/loading editor state and video rendering commands.
'''
import os
import sys
import json
import subprocess
import threading
import re
from pathlib import Path
from app import db
from app.models.project import Project
from sqlalchemy.orm.attributes import flag_modified
from datetime import datetime
_render_status = { }
_render_status_timestamps = { }
_MAX_RENDER_STATUS_ENTRIES = 100
_QUOTE_PATTERN = re.compile('^["\\\'""]+|["\'""]+$')

def _cleanup_old_render_status():
    '''오래된 render status 항목 정리 (LRU 방식)'''
    if len(_render_status) <= _MAX_RENDER_STATUS_ENTRIES:
        return None
    sorted_projects = None(_render_status_timestamps.items(), key = (lambda x: x[1]))
    to_remove = len(_render_status) - _MAX_RENDER_STATUS_ENTRIES // 2
    for project_id, _ in sorted_projects[:to_remove]:
        status = _render_status.get(project_id, { })
        if status.get('status') == 'rendering':
            continue
        _render_status.pop(project_id, None)
        _render_status_timestamps.pop(project_id, None)
        return None


def _clean_text_quotes(text = None):
    '''텍스트 앞뒤의 따옴표를 제거합니다.'''
    if not text:
        return text
    return None.sub('', text).strip()


class EditorService:
    '''Service for managing Pro Editor state'''
    _convert_urls_to_file_paths = (lambda state = None, data_dir = None, flask_port = staticmethod: import copyrender_state = copy.deepcopy(state)tracks = render_state.get('tracks', [])for track in tracks:
clips = track.get('clips', [])for clip in clips:
source_url = clip.get('sourceUrl', '')if source_url.startswith('/data/'):
http_url = f'''http://localhost:{flask_port}{source_url}'''clip['sourceUrl'] = http_urlprint(f'''[Render] Converted: {source_url} -> {http_url}''')if 'text' in clip and clip['text']:
clip['text'] = _clean_text_quotes(clip['text'])render_state)()
    get_state = (lambda project_id = None:
