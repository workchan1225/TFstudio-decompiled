# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _table_schema.pyc (Python 3.11)

'''
Table Schema builders

https://specs.frictionlessdata.io/table-schema/
'''
from __future__ import annotations
from typing import TYPE_CHECKING, Any, cast
import warnings
from pandas._config import option_context
from pandas._libs import lib
from pandas._libs.json import ujson_loads
from pandas._libs.tslibs import timezones
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.base import _registry as registry
from pandas.core.dtypes.common import is_bool_dtype, is_integer_dtype, is_numeric_dtype, is_string_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype, DatetimeTZDtype, ExtensionDtype, PeriodDtype
from pandas import DataFrame

common
from pandas.tseries.frequencies import to_offset
import pandas.core.common, core
if TYPE_CHECKING:
    from pandas._typing import DtypeObj, JSONSerializable
    from pandas import Series
    from pandas.core.indexes.multi import MultiIndex
TABLE_SCHEMA_VERSION = '1.4.0'

def as_json_table_type(x = None):
    '''
    Convert a NumPy / pandas type to its corresponding json_table.

    Parameters
    ----------
    x : np.dtype or ExtensionDtype

    Returns
    -------
    str
        the Table Schema data types

    Notes
    -----
    This table shows the relationship between NumPy / pandas dtypes,
    and Table Schema dtypes.

    ==============  =================
    Pandas type     Table Schema type
    ==============  =================
    int64           integer
    float64         number
    bool            boolean
    datetime64[ns]  datetime
    timedelta64[ns] duration
    object          str
    categorical     any
    =============== =================
    '''
    if is_integer_dtype(x):
        return 'integer'
    if None(x):
        return 'boolean'
    if None(x):
        return 'number'
    if None.is_np_dtype(x, 'M') or isinstance(x, (DatetimeTZDtype, PeriodDtype)):
        return 'datetime'
    if None.is_np_dtype(x, 'm'):
        return 'duration'
    if None(x):
        return 'string'


def set_default_names(data):
    """Sets index names to 'index' for regular, or 'level_x' for Multi"""
    pass
# WARNING: Decompyle incomplete


def convert_pandas_type_to_json_field(arr = None):
    dtype = arr.dtype
# WARNING: Decompyle incomplete


def convert_json_field_to_pandas_type(field = None):
    '''
    Converts a JSON field descriptor into its corresponding NumPy / pandas type

    Parameters
    ----------
    field
        A JSON field descriptor

    Returns
    -------
    dtype

    Raises
    ------
    ValueError
        If the type of the provided field is unknown or currently unsupported

    Examples
    --------
    >>> convert_json_field_to_pandas_type({"name": "an_int", "type": "integer"})
    \'int64\'

    >>> convert_json_field_to_pandas_type(
    ...     {
    ...         "name": "a_categorical",
    ...         "type": "any",
    ...         "constraints": {"enum": ["a", "b", "c"]},
    ...         "ordered": True,
    ...     }
    ... )
    CategoricalDtype(categories=[\'a\', \'b\', \'c\'], ordered=True, categories_dtype=str)

    >>> convert_json_field_to_pandas_type({"name": "a_datetime", "type": "datetime"})
    \'datetime64[ns]\'

    >>> convert_json_field_to_pandas_type(
    ...     {"name": "a_datetime_with_tz", "type": "datetime", "tz": "US/Central"}
    ... )
    \'datetime64[ns, US/Central]\'
    '''
    typ = field['type']
    if typ == 'string':
        return field.get('extDtype', None)
    if None == 'integer':
        return field.get('extDtype', 'int64')
    if None == 'number':
        return field.get('extDtype', 'float64')
    if None == 'boolean':
        return field.get('extDtype', 'bool')
    if None == 'duration':
        return 'timedelta64'
    if None == 'datetime':
        if field.get('tz'):
            return f'''datetime64[ns, {field['tz']}]'''
        if None.get('freq'):
            offset = to_offset(field['freq'])
            freq = PeriodDtype(offset)._freqstr
            return f'''period[{freq}]'''
        return None
    if None == 'any':
        if 'constraints' in field and 'ordered' in field:
            return CategoricalDtype(categories = field['constraints']['enum'], ordered = field['ordered'])
        if None in field:
            return registry.find(field['extDtype'])
        return None
    raise None(f'''Unsupported or invalid field type: {typ}''')


def build_table_schema(data = None, index = None, primary_key = None, version = (True, None, True)):
    """
    Create a Table schema from ``data``.

    This method is a utility to generate a JSON-serializable schema
    representation of a pandas Series or DataFrame, compatible with the
    Table Schema specification. It enables structured data to be shared
    and validated in various applications, ensuring consistency and
    interoperability.

    Parameters
    ----------
    data : Series or DataFrame
        The input data for which the table schema is to be created.
    index : bool, default True
        Whether to include ``data.index`` in the schema.
    primary_key : bool or None, default True
        Column names to designate as the primary key.
        The default `None` will set `'primaryKey'` to the index
        level or levels if the index is unique.
    version : bool, default True
        Whether to include a field `pandas_version` with the version
        of pandas that last revised the table schema. This version
        can be different from the installed pandas version.

    Returns
    -------
    dict
        A dictionary representing the Table schema.

    See Also
    --------
    DataFrame.to_json : Convert the object to a JSON string.
    read_json : Convert a JSON string to pandas object.

    Notes
    -----
    See `Table Schema
    <https://pandas.pydata.org/docs/user_guide/io.html#table-schema>`__ for
    conversion types.
    Timedeltas as converted to ISO8601 duration format with
    9 decimal places after the seconds field for nanosecond precision.

    Categoricals are converted to the `any` dtype, and use the `enum` field
    constraint to list the allowed values. The `ordered` attribute is included
    in an `ordered` field.

    Examples
    --------
    >>> from pandas.io.json._table_schema import build_table_schema
    >>> df = pd.DataFrame(
    ...     {'A': [1, 2, 3],
    ...      'B': ['a', 'b', 'c'],
    ...      'C': pd.date_range('2016-01-01', freq='D', periods=3),
    ...      }, index=pd.Index(range(3), name='idx'))
    >>> build_table_schema(df)
    {'fields': [{'name': 'idx', 'type': 'integer'}, {'name': 'A', 'type': 'integer'}, {'name': 'B', 'type': 'string', 'extDtype': 'str'}, {'name': 'C', 'type': 'datetime'}], 'primaryKey': ['idx'], 'pandas_version': '1.4.0'}
    """
    if index is True:
        data = set_default_names(data)
    schema = { }
    fields = []
    if index:
        if data.index.nlevels > 1:
            data.index = cast('MultiIndex', data.index)
            for level, name in zip(data.index.levels, data.index.names, strict = True):
                new_field = convert_pandas_type_to_json_field(level)
                new_field['name'] = name
                fields.append(new_field)
        fields.append(convert_pandas_type_to_json_field(data.index))
    if data.ndim > 1:
        for column, s in data.items():
            fields.append(convert_pandas_type_to_json_field(s))
    fields.append(convert_pandas_type_to_json_field(data))
    schema['fields'] = fields
# WARNING: Decompyle incomplete


def parse_table_schema(json = None, precise_float = None):
    """
    Builds a DataFrame from a given schema

    Parameters
    ----------
    json :
        A JSON table schema
    precise_float : bool
        Flag controlling precision when decoding string to double values, as
        dictated by ``read_json``

    Returns
    -------
    df : DataFrame

    Raises
    ------
    NotImplementedError
        If the JSON table schema contains either timezone or timedelta data

    Notes
    -----
        Because :func:`DataFrame.to_json` uses the string 'index' to denote a
        name-less :class:`Index`, this function sets the name of the returned
        :class:`DataFrame` to ``None`` when said string is encountered with a
        normal :class:`Index`. For a :class:`MultiIndex`, the same limitation
        applies to any strings beginning with 'level_'. Therefore, an
        :class:`Index` name of 'index'  and :class:`MultiIndex` names starting
        with 'level_' are not supported.

    See Also
    --------
    build_table_schema : Inverse function.
    pandas.read_json
    """
    table = ujson_loads(json, precise_float = precise_float)
    col_order = table['schema']['fields']()
    df = DataFrame(table['data'], columns = col_order)[col_order]
    dtypes = table['schema']['fields']()
    if 'timedelta64' in dtypes.values():
        raise NotImplementedError('table="orient" can not yet read ISO-formatted Timedelta data')
    option_context('future.distinguish_nan_and_na', False)
    df = df.astype(dtypes)
    None(None, None)
