# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dialogue_line_parser.pyc (Python 3.11)

'''
Shared dialogue line parser for speaker-tagged scripts.

This parser is used by both speaker TTS generation and scene lineIndex mapping,
so line extraction and indexing stay consistent across features.
'''
import re
from typing import Any, Dict, List
from app.utils.script_text_cleaner import remove_parenthetical_directions

class DialogueLineParser:
    '''Parses speaker-tagged chapter content into canonical dialogue lines.'''
    JSON_KEYWORDS = {
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
    CHAPTER_MARKER_PATTERNS = [
        re.compile('^챕터\\s*\\d+$', re.IGNORECASE),
        re.compile('^chapter\\s*\\d+$', re.IGNORECASE),
        re.compile('^\\d+장$', re.IGNORECASE),
        re.compile('^장\\s*\\d+$', re.IGNORECASE),
        re.compile('^part\\s*\\d+$', re.IGNORECASE),
        re.compile('^파트\\s*\\d+$', re.IGNORECASE),
        re.compile('^챕터$', re.IGNORECASE),
        re.compile('^chapter$', re.IGNORECASE),
        re.compile('^파트$', re.IGNORECASE),
        re.compile('^part$', re.IGNORECASE)]
    MALFORMED_SPEAKER_TAG_PATTERN = re.compile('\\[([^\\]\\r\\n:]{1,24})\\s*[:：]\\s*')
    SPEAKER_LINE_PATTERN = re.compile('^(\\[[^\\]]+\\]|\\[[^\\]\\r\\n:]{1,24}|[^:\\[\\]]+)\\s*[:：]\\s*(.*)$')
    QUOTE_PATTERN = re.compile('^["\\\'\\u201c\\u201d\\u2018\\u2019]+|["\\\'\\u201c\\u201d\\u2018\\u2019]+$')
    is_chapter_marker = (lambda speaker = None: pass# WARNING: Decompyle incomplete
)()
    clean_dialogue_text = (lambda text = None: if not text:
''None.QUOTE_PATTERN.sub('', text).strip())()
    _looks_like_recoverable_speaker_label = (lambda label = None:
