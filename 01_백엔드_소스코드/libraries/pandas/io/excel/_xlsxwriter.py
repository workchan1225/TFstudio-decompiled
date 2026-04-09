# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _xlsxwriter.pyc (Python 3.11)

from __future__ import annotations
import json
from typing import TYPE_CHECKING, Any
from pandas.io.excel._base import ExcelWriter
from pandas.io.excel._util import combine_kwargs, validate_freeze_panes
if TYPE_CHECKING:
    from pandas._typing import ExcelWriterIfSheetExists, FilePath, StorageOptions, WriteExcelBuffer

class _XlsxStyler:
    STYLE_MAPPING: 'dict[str, list[tuple[tuple[str, ...], str]]]' = {
        'font': [
            (('name',), 'font_name'),
            (('sz',), 'font_size'),
            (('size',), 'font_size'),
            (('color', 'rgb'), 'font_color'),
            (('color',), 'font_color'),
            (('b',), 'bold'),
            (('bold',), 'bold'),
            (('i',), 'italic'),
            (('italic',), 'italic'),
            (('u',), 'underline'),
            (('underline',), 'underline'),
            (('strike',), 'font_strikeout'),
            (('vertAlign',), 'font_script'),
            (('vertalign',), 'font_script')],
        'number_format': [
            (('format_code',), 'num_format'),
            ((), 'num_format')],
        'protection': [
            (('locked',), 'locked'),
            (('hidden',), 'hidden')],
        'alignment': [
            (('horizontal',), 'align'),
            (('vertical',), 'valign'),
            (('text_rotation',), 'rotation'),
            (('wrap_text',), 'text_wrap'),
            (('indent',), 'indent'),
            (('shrink_to_fit',), 'shrink')],
        'fill': [
            (('patternType',), 'pattern'),
            (('patterntype',), 'pattern'),
            (('fill_type',), 'pattern'),
            (('start_color', 'rgb'), 'fg_color'),
            (('fgColor', 'rgb'), 'fg_color'),
            (('fgcolor', 'rgb'), 'fg_color'),
            (('start_color',), 'fg_color'),
            (('fgColor',), 'fg_color'),
            (('fgcolor',), 'fg_color'),
            (('end_color', 'rgb'), 'bg_color'),
            (('bgColor', 'rgb'), 'bg_color'),
            (('bgcolor', 'rgb'), 'bg_color'),
            (('end_color',), 'bg_color'),
            (('bgColor',), 'bg_color'),
            (('bgcolor',), 'bg_color')],
        'border': [
            (('color', 'rgb'), 'border_color'),
            (('color',), 'border_color'),
            (('style',), 'border'),
            (('top', 'color', 'rgb'), 'top_color'),
            (('top', 'color'), 'top_color'),
            (('top', 'style'), 'top'),
            (('top',), 'top'),
            (('right', 'color', 'rgb'), 'right_color'),
            (('right', 'color'), 'right_color'),
            (('right', 'style'), 'right'),
            (('right',), 'right'),
            (('bottom', 'color', 'rgb'), 'bottom_color'),
            (('bottom', 'color'), 'bottom_color'),
            (('bottom', 'style'), 'bottom'),
            (('bottom',), 'bottom'),
            (('left', 'color', 'rgb'), 'left_color'),
            (('left', 'color'), 'left_color'),
            (('left', 'style'), 'left'),
            (('left',), 'left')] }
    convert = (lambda cls = None, style_dict = None, num_format_str = classmethod: props = { }# WARNING: Decompyle incomplete
)()


class XlsxWriter(ExcelWriter):
    pass
# WARNING: Decompyle incomplete
