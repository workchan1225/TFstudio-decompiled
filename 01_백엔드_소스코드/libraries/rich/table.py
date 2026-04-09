# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: table.pyc (Python 3.11)

from dataclasses import dataclass, field, replace
from typing import TYPE_CHECKING, Dict, Iterable, List, NamedTuple, Optional, Sequence, Tuple, Union
from  import box, errors
from _loop import loop_first_last, loop_last
from _pick import pick_bool
from _ratio import ratio_distribute, ratio_reduce
from align import VerticalAlignMethod
from jupyter import JupyterMixin
from measure import Measurement
from padding import Padding, PaddingDimensions
from protocol import is_renderable
from segment import Segment
from style import Style, StyleType
from text import Text, TextType
if TYPE_CHECKING:
    from console import Console, ConsoleOptions, JustifyMethod, OverflowMethod, RenderableType, RenderResult
Column = <NODE:12>()
Row = <NODE:12>()

class _Cell(NamedTuple):
    vertical: VerticalAlignMethod = 'A single cell in a table.'


class Table(JupyterMixin):
    rows: List[Row] = 'A console renderable to draw a table.\n\n    Args:\n        *headers (Union[Column, str]): Column headers, either as a string, or :class:`~rich.table.Column` instance.\n        title (Union[str, Text], optional): The title of the table rendered at the top. Defaults to None.\n        caption (Union[str, Text], optional): The table caption rendered below. Defaults to None.\n        width (int, optional): The width in characters of the table, or ``None`` to automatically fit. Defaults to None.\n        min_width (Optional[int], optional): The minimum width of the table, or ``None`` for no minimum. Defaults to None.\n        box (box.Box, optional): One of the constants in box.py used to draw the edges (see :ref:`appendix_box`), or ``None`` for no box lines. Defaults to box.HEAVY_HEAD.\n        safe_box (Optional[bool], optional): Disable box characters that don\'t display on windows legacy terminal with *raster* fonts. Defaults to True.\n        padding (PaddingDimensions, optional): Padding for cells (top, right, bottom, left). Defaults to (0, 1).\n        collapse_padding (bool, optional): Enable collapsing of padding around cells. Defaults to False.\n        pad_edge (bool, optional): Enable padding of edge cells. Defaults to True.\n        expand (bool, optional): Expand the table to fit the available space if ``True``, otherwise the table width will be auto-calculated. Defaults to False.\n        show_header (bool, optional): Show a header row. Defaults to True.\n        show_footer (bool, optional): Show a footer row. Defaults to False.\n        show_edge (bool, optional): Draw a box around the outside of the table. Defaults to True.\n        show_lines (bool, optional): Draw lines between every row. Defaults to False.\n        leading (int, optional): Number of blank lines between rows (precludes ``show_lines``). Defaults to 0.\n        style (Union[str, Style], optional): Default style for the table. Defaults to "none".\n        row_styles (List[Union, str], optional): Optional list of row styles, if more than one style is given then the styles will alternate. Defaults to None.\n        header_style (Union[str, Style], optional): Style of the header. Defaults to "table.header".\n        footer_style (Union[str, Style], optional): Style of the footer. Defaults to "table.footer".\n        border_style (Union[str, Style], optional): Style of the border. Defaults to None.\n        title_style (Union[str, Style], optional): Style of the title. Defaults to None.\n        caption_style (Union[str, Style], optional): Style of the caption. Defaults to None.\n        title_justify (str, optional): Justify method for title. Defaults to "center".\n        caption_justify (str, optional): Justify method for caption. Defaults to "center".\n        highlight (bool, optional): Highlight cell contents (if str). Defaults to False.\n    '
    
    def __init__(self = None, *, title, caption, width, min_width, box, safe_box, padding, collapse_padding, pad_edge, expand, show_header, show_footer, show_edge, show_lines, leading, style, row_styles, header_style, footer_style, border_style, title_style, caption_style, title_justify, caption_justify, highlight, *headers):
        self.columns = []
        self.rows = []
        self.title = title
        self.caption = caption
        self.width = width
        self.min_width = min_width
        self.box = box
        self.safe_box = safe_box
        self._padding = Padding.unpack(padding)
        self.pad_edge = pad_edge
        self._expand = expand
        self.show_header = show_header
        self.show_footer = show_footer
        self.show_edge = show_edge
        self.show_lines = show_lines
        self.leading = leading
        self.collapse_padding = collapse_padding
        self.style = style
        if not header_style:
            self.header_style = ''
            if not footer_style:
                self.footer_style = ''
                self.border_style = border_style
                self.title_style = title_style
                self.caption_style = caption_style
                self.title_justify = title_justify
                self.caption_justify = caption_justify
                self.highlight = highlight
                if not row_styles:
                    self.row_styles = list([])
                    append_column = self.columns.append
                    for header in headers:
                        if isinstance(header, str):
                            self.add_column(header = header)
                            continue
                        header._index = len(self.columns)
                        append_column(header)
                        return None

    grid = (lambda cls = None, *, padding: pass# WARNING: Decompyle incomplete
)()
    expand = (lambda self = None: if not self._expand:
passself.width is not None)()
    expand = (lambda self = None, expand = None: self._expand = expand)()
    _extra_width = (lambda self = None: width = 0if self.box and self.show_edge:
width += 2if self.box:
width += len(self.columns) - 1width)()
    row_count = (lambda self = None: len(self.rows))()
    
    def get_row_style(self = None, console = None, index = None):
        '''Get the current row style.'''
        style = Style.null()
        if self.row_styles:
            style += console.get_style(self.row_styles[index % len(self.row_styles)])
        row_style = self.rows[index].style
    # WARNING: Decompyle incomplete

    
    def __rich_measure__(self = None, console = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    padding = (lambda self = None: self._padding)()
    padding = (lambda self = None, padding = None: self._padding = Padding.unpack(padding)self)()
    
    def add_column(self = None, header = None, footer = None, *, header_style, highlight, footer_style, style, justify, vertical, overflow, width, min_width, max_width, ratio, no_wrap):
        '''Add a column to the table.

        Args:
            header (RenderableType, optional): Text or renderable for the header.
                Defaults to "".
            footer (RenderableType, optional): Text or renderable for the footer.
                Defaults to "".
            header_style (Union[str, Style], optional): Style for the header, or None for default. Defaults to None.
            highlight (bool, optional): Whether to highlight the text. The default of None uses the value of the table (self) object.
            footer_style (Union[str, Style], optional): Style for the footer, or None for default. Defaults to None.
            style (Union[str, Style], optional): Style for the column cells, or None for default. Defaults to None.
            justify (JustifyMethod, optional): Alignment for cells. Defaults to "left".
            vertical (VerticalAlignMethod, optional): Vertical alignment, one of "top", "middle", or "bottom". Defaults to "top".
            overflow (OverflowMethod): Overflow method: "crop", "fold", "ellipsis". Defaults to "ellipsis".
            width (int, optional): Desired width of column in characters, or None to fit to contents. Defaults to None.
            min_width (Optional[int], optional): Minimum width of column, or ``None`` for no minimum. Defaults to None.
            max_width (Optional[int], optional): Maximum width of column, or ``None`` for no maximum. Defaults to None.
            ratio (int, optional): Flexible ratio for the column (requires ``Table.expand`` or ``Table.width``). Defaults to None.
            no_wrap (bool, optional): Set to ``True`` to disable wrapping of this column.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def add_row(self = None, *, style, end_section, *renderables):
