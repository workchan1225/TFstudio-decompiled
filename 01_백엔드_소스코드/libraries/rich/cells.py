# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cells.pyc (Python 3.11)

from __future__ import annotations
from functools import lru_cache
from operator import itemgetter
from typing import Callable, NamedTuple, Sequence, Tuple
from rich._unicode_data import load as load_cell_table
CellSpan = Tuple[(int, int, int)]
_span_get_cell_len = itemgetter(2)
_SINGLE_CELL_UNICODE_RANGES: 'list[tuple[int, int]]' = [
    (32, 126),
    (160, 172),
    (174, 767),
    (880, 1154),
    (9472, 9724),
    (10240, 10495)]
_SINGLE_CELLS = (lambda .0: [ character for _start, _end in .0 for character in map(chr, range(_start, _end + 1)) ])(_SINGLE_CELL_UNICODE_RANGES())
_is_single_cell_widths: 'Callable[[str], bool]' = _SINGLE_CELLS.issuperset

class CellTable(NamedTuple):
    narrow_to_wide: 'frozenset[str]' = 'Contains unicode data required to measure the cell widths of glyphs.'

get_character_cell_size = (lambda character = frozenset, unicode_version = None: codepoint = ord(character)table = load_cell_table(unicode_version).widthsif codepoint > table[-1][1]:
1lower_bound = Noneupper_bound = len(table) - 1index = (lower_bound + upper_bound) // 2(start, end, width) = table[index]if codepoint < start:
upper_bound = index - 1elif codepoint > end:
lower_bound = index + 1elif width == -1:
passwidthif upper_bound < lower_bound:
passelse:
index = (lower_bound + upper_bound) // 21)()
cached_cell_len = (lambda text = None, unicode_version = None: _cell_len(text, unicode_version))()

def cell_len(text = None, unicode_version = None):
    '''Get the cell length of a string (length as it appears in the terminal).

    Args:
        text: String to measure.
        unicode_version: Unicode version, `"auto"` to auto detect, `"latest"` for the latest unicode version.

    Returns:
        Length of string in terminal cells.
    '''
    if len(text) < 512:
        return cached_cell_len(text, unicode_version)
    return None(text, unicode_version)


def _cell_len(text = None, unicode_version = None):
    '''Get the cell length of a string (length as it appears in the terminal).

    Args:
        text: String to measure.
        unicode_version: Unicode version, `"auto"` to auto detect, `"latest"` for the latest unicode version.

    Returns:
        Length of string in terminal cells.
    '''
    pass
# WARNING: Decompyle incomplete


def split_graphemes(text = None, unicode_version = None):
    '''Divide text into spans that define a single grapheme.

    Args:
        text: String to split.
        unicode_version: Unicode version, `"auto"` to auto detect, `"latest"` for the latest unicode version.

    Returns:
        List of spans.
    '''
    cell_table = load_cell_table(unicode_version)
    codepoint_count = len(text)
    index = 0
    last_measured_character = None
    total_width = 0
    spans = []
    SPECIAL = {
        '‍',
        '️'}
# WARNING: Decompyle incomplete


def _split_text(text = None, cell_position = None, unicode_version = None):
    '''Split text by cell position.

    If the cell position falls within a double width character, it is converted to two spaces.

    Args:
        text: Text to split.
        cell_position Offset in cells.
        unicode_version: Unicode version, `"auto"` to auto detect, `"latest"` for the latest unicode version.

    Returns:
        Tuple to two split strings.
    '''
    if cell_position <= 0:
        return ('', text)
    (spans, cell_length) = None(text, unicode_version)
    offset = int((cell_position / cell_length) * len(spans))
    left_size = sum(map(_span_get_cell_len, spans[:offset]))
    if left_size == cell_position:
        if offset >= len(spans):
            return (text, '')
        split_index = None[offset][0]
        return (text[:split_index], text[split_index:])
    if None < cell_position:
        (start, end, cell_size) = spans[offset]
        if left_size + cell_size > cell_position:
            return (text[:start] + ' ', ' ' + text[end:])
        None += 1
        left_size += cell_size
    else:
        (start, end, cell_size) = spans[offset - 1]
        if left_size - cell_size < cell_position:
            return (text[:start] + ' ', ' ' + text[end:])
        None -= 1
        left_size -= cell_size
    continue


def split_text(text = None, cell_position = None, unicode_version = None):
    '''Split text by cell position.

    If the cell position falls within a double width character, it is converted to two spaces.

    Args:
        text: Text to split.
        cell_position Offset in cells.
        unicode_version: Unicode version, `"auto"` to auto detect, `"latest"` for the latest unicode version.

    Returns:
        Tuple to two split strings.
    '''
    if _is_single_cell_widths(text):
        return (text[:cell_position], text[cell_position:])
    return None(text, cell_position, unicode_version)


def set_cell_size(text = None, total = None, unicode_version = None):
    '''Adjust a string by cropping or padding with spaces such that it fits within the given number of cells.

    Args:
        text: String to adjust.
        total: Desired size in cells.
        unicode_version: Unicode version.

    Returns:
        A string with cell size equal to total.
    '''
    if _is_single_cell_widths(text):
        size = len(text)
        if size < total:
            return text + ' ' * (total - size)
        return None[:total]
    if None <= 0:
        return ''
    cell_size = None(text)
    if cell_size == total:
        return text
    if None < total:
        return text + ' ' * (total - cell_size)
    (text, _) = None(text, total, unicode_version)
    return text


def chop_cells(text = None, width = None, unicode_version = None):
    '''Split text into lines such that each line fits within the available (cell) width.

    Args:
        text: The text to fold such that it fits in the given width.
        width: The width available (number of cells).

    Returns:
        A list of strings such that each string in the list has cell width
        less than or equal to the available width.
    '''
    pass
# WARNING: Decompyle incomplete
