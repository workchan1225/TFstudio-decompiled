# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: style_render.pyc (Python 3.11)

from __future__ import annotations
from collections import defaultdict
from collections.abc import Callable, Sequence
from functools import partial
import pathlib
import re
from typing import TYPE_CHECKING, Any, DefaultDict, TypeAlias, TypedDict
from uuid import uuid4
import numpy as np
from pandas._config import get_option
from pandas._libs import lib
from pandas.compat._optional import import_optional_dependency
from pandas.core.dtypes.common import is_complex, is_float, is_integer
from pandas.core.dtypes.generic import ABCSeries
from pandas import DataFrame, Index, IndexSlice, MultiIndex, Series, isna
from pandas.api.types import is_list_like

common
if TYPE_CHECKING:
    from pandas._typing import Axis, Level
    Level = Level
    import pandas.core.common, core
jinja2 = import_optional_dependency('jinja2', extra = 'DataFrame.style requires jinja2.')
from markupsafe import escape as escape_html
BaseFormatter: 'TypeAlias' = str | Callable
ExtFormatter: 'TypeAlias' = BaseFormatter | dict[(Any, BaseFormatter | None)]
CSSPair: 'TypeAlias' = tuple[(str, str | float)]
CSSList: 'TypeAlias' = list[CSSPair]
CSSProperties: 'TypeAlias' = str | CSSList

class CSSDict(TypedDict):
    props: 'CSSProperties' = 'CSSDict'

CSSStyles: 'TypeAlias' = list[CSSDict]
Subset = slice | Sequence | Index

class StylerRenderer:
    '''
    Base class to process rendering a Styler with a specified jinja2 template.
    '''
    this_dir = pathlib.Path(__file__).parent.resolve()
    template_dir = this_dir / 'templates'
    loader = jinja2.FileSystemLoader(template_dir)
    env = jinja2.Environment(loader = loader, trim_blocks = True)
    template_html = env.get_template('html.tpl')
    template_html_table = env.get_template('html_table.tpl')
    template_html_style = env.get_template('html_style.tpl')
    template_latex = env.get_template('latex.tpl')
    template_typst = env.get_template('typst.tpl')
    template_string = env.get_template('string.tpl')
    
    def __init__(self, data, uuid, uuid_len, table_styles = None, table_attributes = None, caption = None, cell_ids = (None, 5, None, None, None, True, None), precision = ('data', 'DataFrame | Series', 'uuid', 'str | None', 'uuid_len', 'int', 'table_styles', 'CSSStyles | None', 'table_attributes', 'str | None', 'caption', 'str | tuple | list | None', 'cell_ids', 'bool', 'precision', 'int | None', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _render(self, sparse_index = None, sparse_columns = None, max_rows = None, max_cols = (None, None, ''), blank = ('sparse_index', 'bool', 'sparse_columns', 'bool', 'max_rows', 'int | None', 'max_cols', 'int | None', 'blank', 'str')):
        '''
        Computes and applies styles and then generates the general render dicts.

        Also extends the `ctx` and `ctx_index` attributes with those of concatenated
        stylers for use within `_translate_latex`
        '''
        self._compute()
        dxs = []
        ctx_len = len(self.index)
    # WARNING: Decompyle incomplete

    
    def _render_html(self = None, sparse_index = None, sparse_columns = None, max_rows = (None, None), max_cols = ('sparse_index', 'bool', 'sparse_columns', 'bool', 'max_rows', 'int | None', 'max_cols', 'int | None', 'return', 'str'), **kwargs):
        '''
        Renders the ``Styler`` including all applied styles to HTML.
        Generates a dict with necessary kwargs passed to jinja2 template.
        '''
        d = self._render(sparse_index, sparse_columns, max_rows, max_cols, '&nbsp;')
        d.update(kwargs)
    # WARNING: Decompyle incomplete

    
    def _render_latex(self = None, sparse_index = None, sparse_columns = None, clines = ('sparse_index', 'bool', 'sparse_columns', 'bool', 'clines', 'str | None', 'return', 'str'), **kwargs):
        '''
        Render a Styler in latex format
        '''
        d = self._render(sparse_index, sparse_columns, None, None)
        self._translate_latex(d, clines = clines)
        self.template_latex.globals['parse_wrap'] = _parse_latex_table_wrapping
        self.template_latex.globals['parse_table'] = _parse_latex_table_styles
        self.template_latex.globals['parse_cell'] = _parse_latex_cell_styles
        self.template_latex.globals['parse_header'] = _parse_latex_header_span
        d.update(kwargs)
    # WARNING: Decompyle incomplete

    
    def _render_typst(self = None, sparse_index = None, sparse_columns = None, max_rows = (None, None), max_cols = ('sparse_index', 'bool', 'sparse_columns', 'bool', 'max_rows', 'int | None', 'max_cols', 'int | None', 'return', 'str'), **kwargs):
        '''
        Render a Styler in typst format
        '''
        d = self._render(sparse_index, sparse_columns, max_rows, max_cols)
        d.update(kwargs)
    # WARNING: Decompyle incomplete

    
    def _render_string(self = None, sparse_index = None, sparse_columns = None, max_rows = (None, None), max_cols = ('sparse_index', 'bool', 'sparse_columns', 'bool', 'max_rows', 'int | None', 'max_cols', 'int | None', 'return', 'str'), **kwargs):
        '''
        Render a Styler in string format
        '''
        d = self._render(sparse_index, sparse_columns, max_rows, max_cols)
        d.update(kwargs)
    # WARNING: Decompyle incomplete

    
    def _compute(self):
        '''
        Execute the style functions built up in `self._todo`.

        Relies on the conventions that all style functions go through
        .apply or .map. The append styles to apply as tuples of

        (application method, *args, **kwargs)
        '''
        self.ctx.clear()
        self.ctx_index.clear()
        self.ctx_columns.clear()
        r = self
    # WARNING: Decompyle incomplete

    
    def _translate(self, sparse_index, sparse_cols = None, max_rows = None, max_cols = None, blank = (None, None, '&nbsp;', None), dxs = ('sparse_index', 'bool', 'sparse_cols', 'bool', 'max_rows', 'int | None', 'max_cols', 'int | None', 'blank', 'str', 'dxs', 'list[dict] | None')):
        '''
        Process Styler data and settings into a dict for template rendering.

        Convert data and settings from ``Styler`` attributes such as ``self.data``,
        ``self.tooltips`` including applying any methods in ``self._todo``.

        Parameters
        ----------
        sparse_index : bool
            Whether to sparsify the index or print all hierarchical index elements.
            Upstream defaults are typically to `pandas.options.styler.sparse.index`.
        sparse_cols : bool
            Whether to sparsify the columns or print all hierarchical column elements.
            Upstream defaults are typically to `pandas.options.styler.sparse.columns`.
        max_rows, max_cols : int, optional
            Specific max rows and cols. max_elements always take precedence in render.
        blank : str
            Entry to top-left blank cells.
        dxs : list[dict]
            The render dicts of the concatenated Stylers.

        Returns
        -------
        d : dict
            The following structure: {uuid, table_styles, caption, head, body,
            cellstyle, table_attributes}
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _translate_header(self = None, sparsify_cols = None, max_cols = None):
        '''
        Build each <tr> within table <head> as a list

        Using the structure:
             +----------------------------+---------------+---------------------------+
             |  index_blanks ...          | column_name_0 |  column_headers (level_0) |
          1) |       ..                   |       ..      |             ..            |
             |  index_blanks ...          | column_name_n |  column_headers (level_n) |
             +----------------------------+---------------+---------------------------+
          2) |  index_names (level_0 to level_n) ...      | column_blanks ...         |
             +----------------------------+---------------+---------------------------+

        Parameters
        ----------
        sparsify_cols : bool
            Whether column_headers section will add colspan attributes (>1) to elements.
        max_cols : int
            Maximum number of columns to render. If exceeded will contain `...` filler.

        Returns
        -------
        head : list
            The associated HTML elements needed for template rendering.
        '''
        col_lengths = _get_level_lengths(self.columns, sparsify_cols, max_cols, self.hidden_columns)
        clabels = self.data.columns.tolist()
        if self.data.columns.nlevels == 1:
            clabels = clabels()
    # WARNING: Decompyle incomplete

    
    def _generate_col_header_row(self = None, iter = None, max_cols = None, col_lengths = ('iter', 'Sequence', 'max_cols', 'int', 'col_lengths', 'dict')):
        '''
        Generate the row containing column headers:

         +----------------------------+---------------+---------------------------+
         |  index_blanks ...          | column_name_i |  column_headers (level_i) |
         +----------------------------+---------------+---------------------------+

        Parameters
        ----------
        iter : tuple
            Looping variables from outer scope
        max_cols : int
            Permissible number of columns
        col_lengths :
            c

        Returns
        -------
        list of elements
        '''
        (r, clabels) = iter
        index_blanks = [
            _element('th', self.css['blank'], self.css['blank_value'], True)] * (self.index.nlevels - sum(self.hide_index_) - 1)
        name = self.data.columns.names[r]
        if name is not None:
            is_display = not (self.hide_column_names)
        value = name if is_display else self.css['blank_value']
        display_value = self._display_funcs_column_names[r](value) if is_display else None
    # WARNING: Decompyle incomplete

    
    def _generate_index_names_row(self = None, iter = None, max_cols = None, col_lengths = ('iter', 'Sequence', 'max_cols', 'int', 'col_lengths', 'dict')):
        '''
        Generate the row containing index names

         +----------------------------+---------------+---------------------------+
         |  index_names (level_0 to level_n) ...      | column_blanks ...         |
         +----------------------------+---------------+---------------------------+

        Parameters
        ----------
        iter : tuple
            Looping variables from outer scope
        max_cols : int
            Permissible number of columns

        Returns
        -------
        list of elements
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _translate_body(self = None, idx_lengths = None, max_rows = None, max_cols = ('idx_lengths', 'dict', 'max_rows', 'int', 'max_cols', 'int')):
        '''
        Build each <tr> within table <body> as a list

        Use the following structure:
          +--------------------------------------------+---------------------------+
          |  index_header_0    ...    index_header_n   |  data_by_column   ...     |
          +--------------------------------------------+---------------------------+

        Also add elements to the cellstyle_map for more efficient grouped elements in
        <style></style> block

        Parameters
        ----------
        sparsify_index : bool
            Whether index_headers section will add rowspan attributes (>1) to elements.

        Returns
        -------
        body : list
            The associated HTML elements needed for template rendering.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _check_trim(self, count, max = None, obj = None, element = None, css = (None, '...'), value = ('count', 'int', 'max', 'int', 'obj', 'list', 'element', 'str', 'css', 'str | None', 'value', 'str', 'return', 'bool')):
        '''
        Indicates whether to break render loops and append a trimming indicator

        Parameters
        ----------
        count : int
            The loop count of previous visible items.
        max : int
            The allowable rendered items in the loop.
        obj : list
            The current render collection of the rendered items.
        element : str
            The type of element to append in the case a trimming indicator is needed.
        css : str, optional
            The css to add to the trimming indicator element.
        value : str, optional
            The value of the elements display if necessary.

        Returns
        -------
        result : bool
            Whether a trimming element was required and appended.
        '''
        if count > max:
            if element == 'row':
                obj.append(self._generate_trimmed_row(max))
            else:
                obj.append(_element(element, css, value, True, attributes = ''))
            return True

    
    def _generate_trimmed_row(self = None, max_cols = None):
        '''
        When a render has too many rows we generate a trimming row containing "..."

        Parameters
        ----------
        max_cols : int
            Number of permissible columns

        Returns
        -------
        list of elements
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _generate_body_row(self = None, iter = None, max_cols = None, idx_lengths = ('iter', 'tuple', 'max_cols', 'int', 'idx_lengths', 'dict')):
        '''
        Generate a regular row for the body section of appropriate format.

          +--------------------------------------------+---------------------------+
          |  index_header_0    ...    index_header_n   |  data_by_column   ...     |
          +--------------------------------------------+---------------------------+

        Parameters
        ----------
        iter : tuple
            Iterable from outer scope: row number, row data tuple, row index labels.
        max_cols : int
            Number of permissible columns.
        idx_lengths : dict
            A map of the sparsification structure of the index

        Returns
        -------
            list of elements
        '''
        (r, row_tup, rlabels) = iter
        index_headers = []
        for c, value in enumerate(rlabels[r]):
            if _is_visible(r, c, idx_lengths):
                header_element_visible = not self.hide_index_[c]
            header_element = _element('th', f'''{self.css['row_heading']} {self.css['level']}{c} {self.css['row']}{r}''', value, header_element_visible, display_value = self._display_funcs_index[(r, c)](value), attributes = f'''rowspan="{idx_lengths.get((c, r), 0)}"''' if idx_lengths.get((c, r), 0) > 1 else '')
            if self.cell_ids:
                header_element['id'] = f'''{self.css['level']}{c}_{self.css['row']}{r}'''
            if header_element_visible and (r, c) in self.ctx_index and self.ctx_index[(r, c)]:
                header_element['id'] = f'''{self.css['level']}{c}_{self.css['row']}{r}'''
                self.cellstyle_map_index[tuple(self.ctx_index[(r, c)])].append(f'''{self.css['level']}{c}_{self.css['row']}{r}''')
            index_headers.append(header_element)
            data = []
            visible_col_count = 0
            for c, value in enumerate(row_tup[1:]):
                if c not in self.hidden_columns:
                    data_element_visible = r not in self.hidden_rows
                    if data_element_visible:
                        visible_col_count += 1
                if self._check_trim(visible_col_count, max_cols, data, 'td', f'''{self.css['data']} {self.css['row']}{r} {self.css['col_trim']}'''):
                    pass
                else:
                    cls = ''
                    if (r, c) in self.cell_context:
                        cls = ' ' + self.cell_context[(r, c)]
                    data_element = _element('td', f'''{self.css['data']} {self.css['row']}{r} {self.css['col']}{c}{cls}''', value, data_element_visible, attributes = '', display_value = self._display_funcs[(r, c)](value))
                    if self.cell_ids:
                        data_element['id'] = f'''{self.css['row']}{r}_{self.css['col']}{c}'''
                    if data_element_visible and (r, c) in self.ctx and self.ctx[(r, c)]:
                        data_element['id'] = f'''{self.css['row']}{r}_{self.css['col']}{c}'''
                        self.cellstyle_map[tuple(self.ctx[(r, c)])].append(f'''{self.css['row']}{r}_{self.css['col']}{c}''')
                    data.append(data_element)
                return index_headers + data

    
    def _translate_latex(self = None, d = None, clines = None):
        '''
        Post-process the default render dict for the LaTeX template format.

        Processing items included are:
          - Remove hidden columns from the non-headers part of the body.
          - Place cellstyles directly in td cells rather than use cellstyle_map.
          - Remove hidden indexes or reinsert missing th elements if part of multiindex
            or multirow sparsification (so that \\multirow and \\multicol work correctly).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def format(self, formatter, subset, na_rep, precision = None, decimal = None, thousands = None, escape = (None, None, None, None, '.', None, None, None), hyperlinks = ('formatter', 'ExtFormatter | None', 'subset', 'Subset | None', 'na_rep', 'str | None', 'precision', 'int | None', 'decimal', 'str', 'thousands', 'str | None', 'escape', 'str | None', 'hyperlinks', 'str | None', 'return', 'StylerRenderer')):
        '''
        Format the text display value of cells.

        Parameters
        ----------
        formatter : str, callable, dict or None
            Object to define how values are displayed. See notes.
        subset : label, array-like, IndexSlice, optional
            A valid 2d input to `DataFrame.loc[<subset>]`, or, in the case of a 1d input
            or single key, to `DataFrame.loc[:, <subset>]` where the columns are
            prioritised, to limit ``data`` to *before* applying the function.
        na_rep : str, optional
            Representation for missing values.
            If ``na_rep`` is None, no special formatting is applied.
        precision : int, optional
            Floating point precision to use for display purposes, if not determined by
            the specified ``formatter``.
        decimal : str, default "."
            Character used as decimal separator for floats, complex and integers.
        thousands : str, optional, default None
            Character used as thousands separator for floats, complex and integers.
        escape : str, optional
            Use \'html\' to replace the characters ``&``, ``<``, ``>``, ``\'``, and ``"``
            in cell display string with HTML-safe sequences.
            Use \'latex\' to replace the characters ``&``, ``%``, ``$``, ``#``, ``_``,
            ``{``, ``}``, ``~``, ``^``, and ``\\`` in the cell display string with
            LaTeX-safe sequences.
            Use \'latex-math\' to replace the characters the same way as in \'latex\' mode,
            except for math substrings, which either are surrounded
            by two characters ``$`` or start with the character ``\\(`` and
            end with ``\\)``. Escaping is done before ``formatter``.
        hyperlinks : {"html", "latex"}, optional
            Convert string patterns containing https://, http://, ftp:// or www. to
            HTML <a> tags as clickable URL hyperlinks if "html", or LaTeX \\href
            commands if "latex".

        Returns
        -------
        Styler
            Returns itself for chaining.

        See Also
        --------
        Styler.format_index: Format the text display value of index labels.

        Notes
        -----
        This method assigns a formatting function, ``formatter``, to each cell in the
        DataFrame. If ``formatter`` is ``None``, then the default formatter is used.
        If a callable then that function should take a data value as input and return
        a displayable representation, such as a string. If ``formatter`` is
        given as a string this is assumed to be a valid Python format specification
        and is wrapped to a callable as ``string.format(x)``. If a ``dict`` is given,
        keys should correspond to column names, and values should be string or
        callable, as above.

        The default formatter currently expresses floats and complex numbers with the
        pandas display precision unless using the ``precision`` argument here. The
        default formatter does not adjust the representation of missing values unless
        the ``na_rep`` argument is used.

        The ``subset`` argument defines which region to apply the formatting function
        to. If the ``formatter`` argument is given in dict form but does not include
        all columns within the subset then these columns will have the default formatter
        applied. Any columns in the formatter dict excluded from the subset will
        be ignored.

        When using a ``formatter`` string the dtypes must be compatible, otherwise a
        `ValueError` will be raised.

        When instantiating a Styler, default formatting can be applied by setting the
        ``pandas.options``:

          - ``styler.format.formatter``: default None.
          - ``styler.format.na_rep``: default None.
          - ``styler.format.precision``: default 6.
          - ``styler.format.decimal``: default ".".
          - ``styler.format.thousands``: default None.
          - ``styler.format.escape``: default None.

        .. warning::
           `Styler.format` is ignored when using the output format `Styler.to_excel`,
           since Excel and Python have inherently different formatting structures.
           However, it is possible to use the `number-format` pseudo CSS attribute
           to force Excel permissible formatting. See examples.

        Examples
        --------
        Using ``na_rep`` and ``precision`` with the default ``formatter``

        >>> df = pd.DataFrame([[np.nan, 1.0, \'A\'], [2.0, np.nan, 3.0]])
        >>> df.style.format(na_rep=\'MISS\', precision=3)  # doctest: +SKIP
                0       1       2
        0    MISS   1.000       A
        1   2.000    MISS   3.000

        Using a ``formatter`` specification on consistent column dtypes

        >>> df.style.format(\'{:.2f}\', na_rep=\'MISS\', subset=[0, 1])  # doctest: +SKIP
                0      1          2
        0    MISS   1.00          A
        1    2.00   MISS   3.000000

        Using the default ``formatter`` for unspecified columns

        >>> df.style.format({0: \'{:.2f}\', 1: \'£ {:.1f}\'},
        ...                 na_rep=\'MISS\', precision=1)  # doctest: +SKIP
                 0      1     2
        0    MISS   £ 1.0     A
        1    2.00    MISS   3.0

        Multiple ``na_rep`` or ``precision`` specifications under the default
        ``formatter``.

        >>> (df.style.format(na_rep=\'MISS\', precision=1, subset=[0]).format(
        ...     na_rep=\'PASS\', precision=2, subset=[1, 2]))  # doctest: +SKIP
                0      1      2
        0    MISS   1.00      A
        1     2.0   PASS   3.00

        Using a callable ``formatter`` function.

        >>> func = lambda s: \'STRING\' if isinstance(s, str) else \'FLOAT\'
        >>> df.style.format({0: \'{:.1f}\', 2: func},
        ...                 precision=4, na_rep=\'MISS\')  # doctest: +SKIP
                0        1        2
        0    MISS   1.0000   STRING
        1     2.0     MISS    FLOAT

        Using a ``formatter`` with HTML ``escape`` and ``na_rep``.

        >>> df = pd.DataFrame([[\'<div></div>\', \'"A&B"\', None]])
        >>> s = df.style.format(
        ...     \'<a href="a.com/{0}">{0}</a>\', escape="html", na_rep="NA")
        >>> s.to_html()  # doctest: +SKIP
        ...
        <td .. ><a href="a.com/&lt;div&gt;&lt;/div&gt;">&lt;div&gt;&lt;/div&gt;</a></td>
        <td .. ><a href="a.com/&#34;A&amp;B&#34;">&#34;A&amp;B&#34;</a></td>
        <td .. >NA</td>
        ...

        Using a ``formatter`` with ``escape`` in \'latex\' mode.

        >>> df = pd.DataFrame([["123"], ["~ ^"], ["$%#"]])
        >>> df.style.format("\\\\textbf{{{}}}",
        ...                 escape="latex").to_latex()  # doctest: +SKIP
        \\begin{tabular}{ll}
         & 0 \\\\
        0 & \\textbf{123} \\\\
        1 & \\textbf{\\textasciitilde \\space \\textasciicircum } \\\\
        2 & \\textbf{\\$\\%\\#} \\\\
        \\end{tabular}

        Applying ``escape`` in \'latex-math\' mode. In the example below
        we enter math mode using the character ``$``.

        >>> df = pd.DataFrame([
        ...     [r"$\\sum_{i=1}^{10} a_i$ a~b $\\alpha = \\frac{\\beta}{\\zeta^2}$"],
        ...     [r"%#^ $ \\$x^2 $"]])
        >>> df.style.format(escape="latex-math").to_latex()  # doctest: +SKIP
        \\begin{tabular}{ll}
         & 0 \\\\
        0 & $\\sum_{i=1}^{10} a_i$ a\\textasciitilde b $\\alpha = \\frac{\\beta}{\\zeta^2}$ \\\\
        1 & \\%\\#\\textasciicircum \\space $ \\$x^2 $ \\\\
        \\end{tabular}

        We can use the character ``\\(`` to enter math mode and the character ``\\)``
        to close math mode.

        >>> df = pd.DataFrame([
        ...     [r"\\(\\sum_{i=1}^{10} a_i\\) a~b \\(\\alpha = \\frac{\\beta}{\\zeta^2}\\)"],
        ...     [r"%#^ \\( \\$x^2 \\)"]])
        >>> df.style.format(escape="latex-math").to_latex()  # doctest: +SKIP
        \\begin{tabular}{ll}
         & 0 \\\\
        0 & \\(\\sum_{i=1}^{10} a_i\\) a\\textasciitilde b \\(\\alpha
        = \\frac{\\beta}{\\zeta^2}\\) \\\\
        1 & \\%\\#\\textasciicircum \\space \\( \\$x^2 \\) \\\\
        \\end{tabular}

        If we have in one DataFrame cell a combination of both shorthands
        for math formulas, the shorthand with the sign ``$`` will be applied.

        >>> df = pd.DataFrame([
        ...     [r"\\( x^2 \\)  $x^2$"],
        ...     [r"$\\frac{\\beta}{\\zeta}$ \\(\\frac{\\beta}{\\zeta}\\)"]])
        >>> df.style.format(escape="latex-math").to_latex()  # doctest: +SKIP
        \\begin{tabular}{ll}
         & 0 \\\\
        0 & \\textbackslash ( x\\textasciicircum 2 \\textbackslash )  $x^2$ \\\\
        1 & $\\frac{\\beta}{\\zeta}$ \\textbackslash (\\textbackslash
        frac\\{\\textbackslash beta\\}\\{\\textbackslash zeta\\}\\textbackslash ) \\\\
        \\end{tabular}

        Pandas defines a `number-format` pseudo CSS attribute instead of the `.format`
        method to create `to_excel` permissible formatting. Note that semi-colons are
        CSS protected characters but used as separators in Excel\'s format string.
        Replace semi-colons with the section separator character (ASCII-245) when
        defining the formatting here.

        >>> df = pd.DataFrame({"A": [1, 0, -1]})
        >>> pseudo_css = "number-format: 0§[Red](0)§-§@;"
        >>> filename = "formatted_file.xlsx"
        >>> df.style.map(lambda v: pseudo_css).to_excel(filename)  # doctest: +SKIP

        .. figure:: ../../_static/style/format_excel_css.png
        '''
        if all((formatter is None, subset is None, precision is None, decimal == '.', thousands is None, na_rep is None, escape is None, hyperlinks is None)):
            self._display_funcs.clear()
            return self
    # WARNING: Decompyle incomplete

    
    def format_index(self, formatter, axis, level, na_rep, precision = None, decimal = None, thousands = None, escape = (None, 0, None, None, None, '.', None, None, None), hyperlinks = ('formatter', 'ExtFormatter | None', 'axis', 'Axis', 'level', 'Level | list[Level] | None', 'na_rep', 'str | None', 'precision', 'int | None', 'decimal', 'str', 'thousands', 'str | None', 'escape', 'str | None', 'hyperlinks', 'str | None', 'return', 'StylerRenderer')):
        '''
        Format the text display value of index labels or column headers.

        Parameters
        ----------
        formatter : str, callable, dict or None
            Object to define how values are displayed. See notes.
        axis : {0, "index", 1, "columns"}
            Whether to apply the formatter to the index or column headers.
        level : int, str, list
            The level(s) over which to apply the generic formatter.
        na_rep : str, optional
            Representation for missing values.
            If ``na_rep`` is None, no special formatting is applied.
        precision : int, optional
            Floating point precision to use for display purposes, if not determined by
            the specified ``formatter``.
        decimal : str, default "."
            Character used as decimal separator for floats, complex and integers.
        thousands : str, optional, default None
            Character used as thousands separator for floats, complex and integers.
        escape : str, optional
            Use \'html\' to replace the characters ``&``, ``<``, ``>``, ``\'``, and ``"``
            in cell display string with HTML-safe sequences.
            Use \'latex\' to replace the characters ``&``, ``%``, ``$``, ``#``, ``_``,
            ``{``, ``}``, ``~``, ``^``, and ``\\`` in the cell display string with
            LaTeX-safe sequences.
            Escaping is done before ``formatter``.
        hyperlinks : {"html", "latex"}, optional
            Convert string patterns containing https://, http://, ftp:// or www. to
            HTML <a> tags as clickable URL hyperlinks if "html", or LaTeX \\href
            commands if "latex".

        Returns
        -------
        Styler
            Returns itself for chaining.

        See Also
        --------
        Styler.format: Format the text display value of data cells.

        Notes
        -----
        This method assigns a formatting function, ``formatter``, to each level label
        in the DataFrame\'s index or column headers. If ``formatter`` is ``None``,
        then the default formatter is used.
        If a callable then that function should take a label value as input and return
        a displayable representation, such as a string. If ``formatter`` is
        given as a string this is assumed to be a valid Python format specification
        and is wrapped to a callable as ``string.format(x)``. If a ``dict`` is given,
        keys should correspond to MultiIndex level numbers or names, and values should
        be string or callable, as above.

        The default formatter currently expresses floats and complex numbers with the
        pandas display precision unless using the ``precision`` argument here. The
        default formatter does not adjust the representation of missing values unless
        the ``na_rep`` argument is used.

        The ``level`` argument defines which levels of a MultiIndex to apply the
        method to. If the ``formatter`` argument is given in dict form but does
        not include all levels within the level argument then these unspecified levels
        will have the default formatter applied. Any levels in the formatter dict
        specifically excluded from the level argument will be ignored.

        When using a ``formatter`` string the dtypes must be compatible, otherwise a
        `ValueError` will be raised.

        .. warning::
           `Styler.format_index` is ignored when using the output format
           `Styler.to_excel`, since Excel and Python have inherently different
           formatting structures.
           However, it is possible to use the `number-format` pseudo CSS attribute
           to force Excel permissible formatting. See documentation for `Styler.format`.

        Examples
        --------
        Using ``na_rep`` and ``precision`` with the default ``formatter``

        >>> df = pd.DataFrame([[1, 2, 3]], columns=[2.0, np.nan, 4.0])
        >>> df.style.format_index(axis=1, na_rep=\'MISS\', precision=3)  # doctest: +SKIP
            2.000    MISS   4.000
        0       1       2       3

        Using a ``formatter`` specification on consistent dtypes in a level

        >>> df.style.format_index(\'{:.2f}\', axis=1, na_rep=\'MISS\')  # doctest: +SKIP
             2.00   MISS    4.00
        0       1      2       3

        Using the default ``formatter`` for unspecified levels

        >>> df = pd.DataFrame([[1, 2, 3]],
        ...                   columns=pd.MultiIndex.from_arrays(
        ...                   [["a", "a", "b"], [2, np.nan, 4]]))
        >>> df.style.format_index({0: lambda v: v.upper()}, axis=1, precision=1)
        ... # doctest: +SKIP
                       A       B
              2.0    nan     4.0
        0       1      2       3

        Using a callable ``formatter`` function.

        >>> func = lambda s: \'STRING\' if isinstance(s, str) else \'FLOAT\'
        >>> df.style.format_index(func, axis=1, na_rep=\'MISS\')
        ... # doctest: +SKIP
                  STRING  STRING
            FLOAT   MISS   FLOAT
        0       1      2       3

        Using a ``formatter`` with HTML ``escape`` and ``na_rep``.

        >>> df = pd.DataFrame([[1, 2, 3]], columns=[\'"A"\', \'A&B\', None])
        >>> s = df.style.format_index(\'$ {0}\', axis=1, escape="html", na_rep="NA")
        ... # doctest: +SKIP
        <th .. >$ &#34;A&#34;</th>
        <th .. >$ A&amp;B</th>
        <th .. >NA</td>
        ...

        Using a ``formatter`` with LaTeX ``escape``.

        >>> df = pd.DataFrame([[1, 2, 3]], columns=["123", "~", "$%#"])
        >>> df.style.format_index("\\\\textbf{{{}}}", escape="latex", axis=1).to_latex()
        ... # doctest: +SKIP
        \\begin{tabular}{lrrr}
        {} & {\\textbf{123}} & {\\textbf{\\textasciitilde }} & {\\textbf{\\$\\%\\#}} \\\\
        0 & 1 & 2 & 3 \\\\
        \\end{tabular}
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def relabel_index(self = None, labels = None, axis = None, level = (0, None)):
        '''
        Relabel the index, or column header, keys to display a set of specified values.

        Parameters
        ----------
        labels : list-like or Index
            New labels to display. Must have same length as the underlying values not
            hidden.
        axis : {"index", 0, "columns", 1}
            Apply to the index or columns.
        level : int, str, list, optional
            The level(s) over which to apply the new labels. If `None` will apply
            to all levels of an Index or MultiIndex which are not hidden.

        Returns
        -------
        Styler
            Returns itself for chaining.

        See Also
        --------
        Styler.format_index: Format the text display value of index or column headers.
        Styler.hide: Hide the index, column headers, or specified data from display.

        Notes
        -----
        As part of Styler, this method allows the display of an index to be
        completely user-specified without affecting the underlying DataFrame data,
        index, or column headers. This means that the flexibility of indexing is
        maintained whilst the final display is customisable.

        Since Styler is designed to be progressively constructed with method chaining,
        this method is adapted to react to the **currently specified hidden elements**.
        This is useful because it means one does not have to specify all the new
        labels if the majority of an index, or column headers, have already been hidden.
        The following produce equivalent display (note the length of ``labels`` in
        each case).

        .. code-block:: python

            # relabel first, then hide
            df = pd.DataFrame({"col": ["a", "b", "c"]})
            df.style.relabel_index(["A", "B", "C"]).hide([0, 1])
            # hide first, then relabel
            df = pd.DataFrame({"col": ["a", "b", "c"]})
            df.style.hide([0, 1]).relabel_index(["C"])

        This method should be used, rather than :meth:`Styler.format_index`, in one of
        the following cases (see examples):

          - A specified set of labels are required which are not a function of the
            underlying index keys.
          - The function of the underlying index keys requires a counter variable,
            such as those available upon enumeration.

        Examples
        --------
        Basic use

        >>> df = pd.DataFrame({"col": ["a", "b", "c"]})
        >>> df.style.relabel_index(["A", "B", "C"])  # doctest: +SKIP
             col
        A      a
        B      b
        C      c

        Chaining with pre-hidden elements

        >>> df.style.hide([0, 1]).relabel_index(["C"])  # doctest: +SKIP
             col
        C      c

        Using a MultiIndex

        >>> midx = pd.MultiIndex.from_product([[0, 1], [0, 1], [0, 1]])
        >>> df = pd.DataFrame({"col": list(range(8))}, index=midx)
        >>> styler = df.style  # doctest: +SKIP
                  col
        0  0  0     0
              1     1
           1  0     2
              1     3
        1  0  0     4
              1     5
           1  0     6
              1     7
        >>> styler.hide(
        ...     (midx.get_level_values(0) == 0) | (midx.get_level_values(1) == 0)
        ... )
        ... # doctest: +SKIP
        >>> styler.hide(level=[0, 1])  # doctest: +SKIP
        >>> styler.relabel_index(["binary6", "binary7"])  # doctest: +SKIP
                  col
        binary6     6
        binary7     7

        We can also achieve the above by indexing first and then re-labeling

        >>> styler = df.loc[[(1, 1, 0), (1, 1, 1)]].style
        >>> styler.hide(level=[0, 1]).relabel_index(["binary6", "binary7"])
        ... # doctest: +SKIP
                  col
        binary6     6
        binary7     7

        Defining a formatting function which uses an enumeration counter. Also note
        that the value of the index key is passed in the case of string labels so it
        can also be inserted into the label, using curly brackets (or double curly
        brackets if the string if pre-formatted),

        >>> df = pd.DataFrame({"samples": np.random.rand(10)})
        >>> styler = df.loc[np.random.randint(0, 10, 3)].style
        >>> styler.relabel_index([f"sample{i + 1} ({{}})" for i in range(3)])
        ... # doctest: +SKIP
                         samples
        sample1 (5)     0.315811
        sample2 (0)     0.495941
        sample3 (2)     0.067946
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def format_index_names(self, formatter, axis, level, na_rep, precision = None, decimal = None, thousands = None, escape = (None, 0, None, None, None, '.', None, None, None), hyperlinks = ('formatter', 'ExtFormatter | None', 'axis', 'Axis', 'level', 'Level | list[Level] | None', 'na_rep', 'str | None', 'precision', 'int | None', 'decimal', 'str', 'thousands', 'str | None', 'escape', 'str | None', 'hyperlinks', 'str | None', 'return', 'StylerRenderer')):
        '''
        Format the text display value of index names or column names.

        .. versionadded:: 3.0

        Parameters
        ----------
        formatter : str, callable, dict or None
            Object to define how values are displayed. See notes.
        axis : {0, "index", 1, "columns"}
            Whether to apply the formatter to the index or column headers.
        level : int, str, list
            The level(s) over which to apply the generic formatter.
        na_rep : str, optional
            Representation for missing values.
            If ``na_rep`` is None, no special formatting is applied.
        precision : int, optional
            Floating point precision to use for display purposes, if not determined by
            the specified ``formatter``.
        decimal : str, default "."
            Character used as decimal separator for floats, complex and integers.
        thousands : str, optional, default None
            Character used as thousands separator for floats, complex and integers.
        escape : str, optional
            Use \'html\' to replace the characters ``&``, ``<``, ``>``, ``\'``, and ``"``
            in cell display string with HTML-safe sequences.
            Use \'latex\' to replace the characters ``&``, ``%``, ``$``, ``#``, ``_``,
            ``{``, ``}``, ``~``, ``^``, and ``\\`` in the cell display string with
            LaTeX-safe sequences.
            Escaping is done before ``formatter``.
        hyperlinks : {"html", "latex"}, optional
            Convert string patterns containing https://, http://, ftp:// or www. to
            HTML <a> tags as clickable URL hyperlinks if "html", or LaTeX \\href
            commands if "latex".

        Returns
        -------
        Styler
            Returns itself for chaining.

        Raises
        ------
        ValueError
            If the `formatter` is a string and the dtypes are incompatible.

        See Also
        --------
        Styler.format_index: Format the text display value of index labels
            or column headers.

        Notes
        -----
        This method has a similar signature to :meth:`Styler.format_index`. Since
        `names` are generally label based, and often not numeric, the typical features
        expected to be more frequently used here are ``escape`` and ``hyperlinks``.

        .. warning::
            `Styler.format_index_names` is ignored when using the output format
            `Styler.to_excel`, since Excel and Python have inherently different
            formatting structures.

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     [[1, 2], [3, 4]],
        ...     index=pd.Index(["a", "b"], name="idx"),
        ... )
        >>> df  # doctest: +SKIP
             0  1
        idx
        a    1  2
        b    3  4
        >>> df.style.format_index_names(lambda x: x.upper(), axis=0)  # doctest: +SKIP
             0  1
        IDX
        a    1  2
        b    3  4
        '''
        pass
    # WARNING: Decompyle incomplete



def _element(html_element = None, html_class = None, value = None, is_visible = ('html_element', 'str', 'html_class', 'str | None', 'value', 'Any', 'is_visible', 'bool', 'return', 'dict'), **kwargs):
    '''
    Template to return container with information for a <td></td> or <th></th> element.
    '''
    pass
# WARNING: Decompyle incomplete


def _get_trimming_maximums(rn, cn = None, max_elements = None, max_rows = None, max_cols = (None, None, 0.8), scaling_factor = ('scaling_factor', 'float', 'return', 'tuple[int, int]')):
    '''
    Recursively reduce the number of rows and columns to satisfy max elements.

    Parameters
    ----------
    rn, cn : int
        The number of input rows / columns
    max_elements : int
        The number of allowable elements
    max_rows, max_cols : int, optional
        Directly specify an initial maximum rows or columns before compression.
    scaling_factor : float
        Factor at which to reduce the number of rows / columns to fit.

    Returns
    -------
    rn, cn : tuple
        New rn and cn values that satisfy the max_elements constraint
    '''
    pass
# WARNING: Decompyle incomplete


def _get_level_lengths(index = None, sparsify = None, max_index = None, hidden_elements = (None,)):
    '''
    Given an index, find the level length for each element.

    Parameters
    ----------
    index : Index
        Index or columns to determine lengths of each element
    sparsify : bool
        Whether to hide or show each distinct element in a MultiIndex
    max_index : int
        The maximum number of elements to analyse along the index due to trimming
    hidden_elements : sequence of int
        Index positions of elements hidden from display in the index affecting
        length

    Returns
    -------
    Dict :
        Result is a dictionary of (level, initial_position): span
    '''
    if isinstance(index, MultiIndex):
        levels = index._format_multi(sparsify = lib.no_default, include_names = False)
    else:
        levels = index._format_flat(include_name = False)
# WARNING: Decompyle incomplete


def _is_visible(idx_row = None, idx_col = None, lengths = None):
    '''
    Index -> {(idx_row, idx_col): bool}).
    '''
    return (idx_col, idx_row) in lengths


def format_table_styles(styles = None):
    """
    looks for multiple CSS selectors and separates them:
    [{'selector': 'td, th', 'props': 'a:v;'}]
        ---> [{'selector': 'td', 'props': 'a:v;'},
              {'selector': 'th', 'props': 'a:v;'}]
    """
    return styles()


def _default_formatter(x = None, precision = None, thousands = None):
    '''
    Format the display of a value

    Parameters
    ----------
    x : Any
        Input variable to be formatted
    precision : Int
        Floating point precision used if ``x`` is float or complex.
    thousands : bool, default False
        Whether to group digits with thousands separated with ",".

    Returns
    -------
    value : Any
        Matches input type, or string if input is float or complex or int with sep.
    '''
    if is_float(x) or is_complex(x):
        return f'''{x:
