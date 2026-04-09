# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: html.pyc (Python 3.11)

'''
Module for formatting output data in HTML.
'''
from __future__ import annotations
from textwrap import dedent
from typing import TYPE_CHECKING, Any, Final, cast
from pandas._config import get_option
from pandas._libs import lib
from pandas import MultiIndex, option_context
from pandas.io.common import is_url
from pandas.io.formats.format import DataFrameFormatter, get_level_lengths
from pandas.io.formats.printing import pprint_thing
if TYPE_CHECKING:
    from collections.abc import Hashable, Iterable, Mapping

class HTMLFormatter:
    '''
    Internal class for formatting output data in html.
    This class is intended for shared functionality between
    DataFrame.to_html() and DataFrame._repr_html_().
    Any logic in common with other output formatting methods
    should ideally be inherited from classes in format.py
    and this class responsible for only producing html markup.
    '''
    indent_delta: 'Final' = 2
    
    def __init__(self, formatter = None, classes = None, border = None, table_id = (None, None, None, False), render_links = ('formatter', 'DataFrameFormatter', 'classes', 'str | list[str] | tuple[str, ...] | None', 'border', 'int | bool | None', 'table_id', 'str | None', 'render_links', 'bool', 'return', 'None')):
        self.fmt = formatter
        self.classes = classes
        self.frame = self.fmt.frame
        self.columns = self.fmt.tr_frame.columns
        self.elements = []
        self.bold_rows = self.fmt.bold_rows
        self.escape = self.fmt.escape
        self.show_dimensions = self.fmt.show_dimensions
    # WARNING: Decompyle incomplete

    
    def to_string(self = None):
        lines = self.render()
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(lines()):
            lines = lines()
        return '\n'.join(lines)

    
    def render(self = None):
        self._write_table()
        if self.should_show_dimensions:
            by = chr(215)
            self.write(f'''<p>{len(self.frame)} rows {by} {len(self.frame.columns)} columns</p>''')
        return self.elements

    should_show_dimensions = (lambda self = None: self.fmt.should_show_dimensions)()
    show_row_idx_names = (lambda self = None: self.fmt.show_row_idx_names)()
    show_col_idx_names = (lambda self = None: self.fmt.show_col_idx_names)()
    row_levels = (lambda self = None: if self.fmt.index:
self.frame.index.nlevelsif None.show_col_idx_names:
1)()
    
    def _get_columns_formatted_values(self = None):
        return self.columns

    is_truncated = (lambda self = None: self.fmt.is_truncated)()
    ncols = (lambda self = None: len(self.fmt.tr_frame.columns))()
    
    def write(self = None, s = None, indent = None):
        rs = pprint_thing(s)
        self.elements.append(' ' * indent + rs)

    
    def write_th(self = None, s = None, header = None, indent = (False, 0, None), tags = ('s', 'Any', 'header', 'bool', 'indent', 'int', 'tags', 'str | None', 'return', 'None')):
        '''
        Method for writing a formatted <th> cell.

        If col_space is set on the formatter then that is used for
        the value of min-width.

        Parameters
        ----------
        s : object
            The data to be written inside the cell.
        header : bool, default False
            Set to True if the <th> is for use inside <thead>.  This will
            cause min-width to be set if there is one.
        indent : int, default 0
            The indentation level of the cell.
        tags : str, default None
            Tags to include in the cell.

        Returns
        -------
        A written <th> cell.
        '''
        col_space = self.col_space.get(s, None)
    # WARNING: Decompyle incomplete

    
    def write_td(self = None, s = None, indent = None, tags = (0, None)):
        self._write_cell(s, kind = 'td', indent = indent, tags = tags)

    
    def _write_cell(self = None, s = None, kind = None, indent = ('td', 0, None), tags = ('s', 'Any', 'kind', 'str', 'indent', 'int', 'tags', 'str | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def write_tr(self, line, indent, indent_delta = None, header = None, align = None, tags = (0, 0, False, None, None, 0), nindex_levels = ('line', 'Iterable', 'indent', 'int', 'indent_delta', 'int', 'header', 'bool', 'align', 'str | None', 'tags', 'dict[int, str] | None', 'nindex_levels', 'int', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _write_table(self = None, indent = None):
        _classes = [
            'dataframe']
        use_mathjax = get_option('display.html.use_mathjax')
        if not use_mathjax:
            _classes.append('tex2jax_ignore')
            _classes.append('mathjax_ignore')
    # WARNING: Decompyle incomplete

    
    def _write_col_header(self = None, indent = None):
