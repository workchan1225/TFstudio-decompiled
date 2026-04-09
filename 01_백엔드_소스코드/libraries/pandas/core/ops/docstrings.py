# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: docstrings.pyc (Python 3.11)

__doc__ = '\nTemplating for ops docstrings\n'
from __future__ import annotations

def make_flex_doc(op_name = None, typ = None):
    """
    Make the appropriate substitutions for the given operation and class-typ
    into either _flex_doc_SERIES or _flex_doc_FRAME to return the docstring
    to attach to a generated method.

    Parameters
    ----------
    op_name : str {'__add__', '__sub__', ... '__eq__', '__ne__', ...}
    typ : str {series, 'dataframe']}

    Returns
    -------
    doc : str
    """
    op_name = op_name.replace('__', '')
    op_desc = _op_descriptions[op_name]
    op_desc_op = op_desc['op']
# WARNING: Decompyle incomplete

_common_examples_algebra_SERIES = "\nExamples\n--------\n>>> a = pd.Series([1, 1, 1, np.nan], index=['a', 'b', 'c', 'd'])\n>>> a\na    1.0\nb    1.0\nc    1.0\nd    NaN\ndtype: float64\n>>> b = pd.Series([1, np.nan, 1, np.nan], index=['a', 'b', 'd', 'e'])\n>>> b\na    1.0\nb    NaN\nd    1.0\ne    NaN\ndtype: float64"
_common_examples_comparison_SERIES = "\nExamples\n--------\n>>> a = pd.Series([1, 1, 1, np.nan, 1], index=['a', 'b', 'c', 'd', 'e'])\n>>> a\na    1.0\nb    1.0\nc    1.0\nd    NaN\ne    1.0\ndtype: float64\n>>> b = pd.Series([0, 1, 2, np.nan, 1], index=['a', 'b', 'c', 'd', 'f'])\n>>> b\na    0.0\nb    1.0\nc    2.0\nd    NaN\nf    1.0\ndtype: float64"
_add_example_SERIES = _common_examples_algebra_SERIES + '\n>>> a.add(b, fill_value=0)\na    2.0\nb    1.0\nc    1.0\nd    1.0\ne    NaN\ndtype: float64\n'
_sub_example_SERIES = _common_examples_algebra_SERIES + '\n>>> a.subtract(b, fill_value=0)\na    0.0\nb    1.0\nc    1.0\nd   -1.0\ne    NaN\ndtype: float64\n'
_mul_example_SERIES = _common_examples_algebra_SERIES + '\n>>> a.multiply(b, fill_value=0)\na    1.0\nb    0.0\nc    0.0\nd    0.0\ne    NaN\ndtype: float64\n'
_div_example_SERIES = _common_examples_algebra_SERIES + '\n>>> a.divide(b, fill_value=0)\na    1.0\nb    inf\nc    inf\nd    0.0\ne    NaN\ndtype: float64\n'
_floordiv_example_SERIES = _common_examples_algebra_SERIES + '\n>>> a.floordiv(b, fill_value=0)\na    1.0\nb    inf\nc    inf\nd    0.0\ne    NaN\ndtype: float64\n'
_divmod_example_SERIES = _common_examples_algebra_SERIES + '\n>>> a.divmod(b, fill_value=0)\n(a    1.0\n b    inf\n c    inf\n d    0.0\n e    NaN\n dtype: float64,\n a    0.0\n b    NaN\n c    NaN\n d    0.0\n e    NaN\n dtype: float64)\n'
_mod_example_SERIES = _common_examples_algebra_SERIES + '\n>>> a.mod(b, fill_value=0)\na    0.0\nb    NaN\nc    NaN\nd    0.0\ne    NaN\ndtype: float64\n'
_pow_example_SERIES = _common_examples_algebra_SERIES + '\n>>> a.pow(b, fill_value=0)\na    1.0\nb    1.0\nc    1.0\nd    0.0\ne    NaN\ndtype: float64\n'
_ne_example_SERIES = _common_examples_algebra_SERIES + '\n>>> a.ne(b, fill_value=0)\na    False\nb     True\nc     True\nd     True\ne     True\ndtype: bool\n'
_eq_example_SERIES = _common_examples_algebra_SERIES + '\n>>> a.eq(b, fill_value=0)\na     True\nb    False\nc    False\nd    False\ne    False\ndtype: bool\n'
_lt_example_SERIES = _common_examples_comparison_SERIES + '\n>>> a.lt(b, fill_value=0)\na    False\nb    False\nc     True\nd    False\ne    False\nf     True\ndtype: bool\n'
_le_example_SERIES = _common_examples_comparison_SERIES + '\n>>> a.le(b, fill_value=0)\na    False\nb     True\nc     True\nd    False\ne    False\nf     True\ndtype: bool\n'
_gt_example_SERIES = _common_examples_comparison_SERIES + '\n>>> a.gt(b, fill_value=0)\na     True\nb    False\nc    False\nd    False\ne     True\nf    False\ndtype: bool\n'
_ge_example_SERIES = _common_examples_comparison_SERIES + '\n>>> a.ge(b, fill_value=0)\na     True\nb     True\nc    False\nd    False\ne     True\nf    False\ndtype: bool\n'
_returns_series = 'Series\n    The result of the operation.'
_returns_tuple = '2-Tuple of Series\n    The result of the operation.'
_op_descriptions: 'dict[str, dict[str, str | None]]' = {
    'add': {
        'op': '+',
        'desc': 'Addition',
        'reverse': 'radd',
        'series_examples': _add_example_SERIES,
        'series_returns': _returns_series },
    'sub': {
        'op': '-',
        'desc': 'Subtraction',
        'reverse': 'rsub',
        'series_examples': _sub_example_SERIES,
        'series_returns': _returns_series },
    'mul': {
        'op': '*',
        'desc': 'Multiplication',
        'reverse': 'rmul',
        'series_examples': _mul_example_SERIES,
        'series_returns': _returns_series,
        'df_examples': None },
    'mod': {
        'op': '%',
        'desc': 'Modulo',
        'reverse': 'rmod',
        'series_examples': _mod_example_SERIES,
        'series_returns': _returns_series },
    'pow': {
        'op': '**',
        'desc': 'Exponential power',
        'reverse': 'rpow',
        'series_examples': _pow_example_SERIES,
        'series_returns': _returns_series,
        'df_examples': None },
    'truediv': {
        'op': '/',
        'desc': 'Floating division',
        'reverse': 'rtruediv',
        'series_examples': _div_example_SERIES,
        'series_returns': _returns_series,
        'df_examples': None },
    'floordiv': {
        'op': '//',
        'desc': 'Integer division',
        'reverse': 'rfloordiv',
        'series_examples': _floordiv_example_SERIES,
        'series_returns': _returns_series,
        'df_examples': None },
    'divmod': {
        'op': 'divmod',
        'desc': 'Integer division and modulo',
        'reverse': 'rdivmod',
        'series_examples': _divmod_example_SERIES,
        'series_returns': _returns_tuple,
        'df_examples': None },
    'eq': {
        'op': '==',
        'desc': 'Equal to',
        'reverse': None,
        'series_examples': _eq_example_SERIES,
        'series_returns': _returns_series },
    'ne': {
        'op': '!=',
        'desc': 'Not equal to',
        'reverse': 'eq',
        'series_examples': _ne_example_SERIES,
        'series_returns': _returns_series },
    'lt': {
        'op': '<',
        'desc': 'Less than',
        'reverse': None,
        'series_examples': _lt_example_SERIES,
        'series_returns': _returns_series },
    'le': {
        'op': '<=',
        'desc': 'Less than or equal to',
        'reverse': None,
        'series_examples': _le_example_SERIES,
        'series_returns': _returns_series },
    'gt': {
        'op': '>',
        'desc': 'Greater than',
        'reverse': 'lt',
        'series_examples': _gt_example_SERIES,
        'series_returns': _returns_series },
    'ge': {
        'op': '>=',
        'desc': 'Greater than or equal to',
        'reverse': 'le',
        'series_examples': _ge_example_SERIES,
        'series_returns': _returns_series } }
_py_num_ref = 'see\n    `Python documentation\n    <https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types>`_\n    for more details'
_op_names = list(_op_descriptions.keys())
# WARNING: Decompyle incomplete
