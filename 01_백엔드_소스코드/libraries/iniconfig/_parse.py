# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _parse.pyc (Python 3.11)

from collections.abc import Mapping
from typing import NamedTuple
from exceptions import ParseError
COMMENTCHARS = '#;'

class ParsedLine(NamedTuple):
    value: str | None = 'ParsedLine'


def parse_ini_data(path = None, data = None, *, strip_inline_comments, strip_section_whitespace):
    '''Parse INI data and return sections and sources mappings.

    Args:
        path: Path for error messages
        data: INI content as string
        strip_inline_comments: Whether to strip inline comments from values
        strip_section_whitespace: Whether to strip whitespace from section and key names
            (default: False). When True, addresses issue #4 by stripping Unicode whitespace.

    Returns:
        Tuple of (sections_data, sources) where:
        - sections_data: mapping of section -> {name -> value}
        - sources: mapping of (section, name) -> line number
    '''
    tokens = parse_lines(path, data.splitlines(True), strip_inline_comments = strip_inline_comments, strip_section_whitespace = strip_section_whitespace)
    sources = { }
    sections_data = { }
# WARNING: Decompyle incomplete


def parse_lines(path = None, line_iter = None, *, strip_inline_comments, strip_section_whitespace):
    result = []
    section = None
# WARNING: Decompyle incomplete


def _parseline(path, line = None, lineno = None, strip_inline_comments = None, strip_section_whitespace = ('path', str, 'line', str, 'lineno', int, 'strip_inline_comments', bool, 'strip_section_whitespace', bool, 'return', tuple[(str | None, str | None)])):
    if iscommentline(line):
        line = ''
    else:
        line = line.rstrip()
    if not line:
        return (None, None)
    if None[0] == '[':
        realline = line
        for c in COMMENTCHARS:
            line = line.split(c)[0].rstrip()
            if line[-1] == ']':
                section_name = line[1:-1]
                if strip_section_whitespace:
                    section_name = section_name.strip()
                return (section_name, None)
            return (None, realline.strip())
    key_name = name.strip()
    value = value.strip()
    if strip_inline_comments:
        for c in COMMENTCHARS:
            value = value.split(c)[0].rstrip()
            return (key_name, value)
            line = line.strip()
            if strip_inline_comments:
                for c in COMMENTCHARS:
                    line = line.split(c)[0].rstrip()
                    return (None, line)


def iscommentline(line = None):
    c = line.lstrip()[:1]
    return c in COMMENTCHARS
