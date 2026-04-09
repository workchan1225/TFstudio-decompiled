# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _normalize.pyc (Python 3.11)

from __future__ import annotations
from collections import abc, defaultdict
import copy
from typing import TYPE_CHECKING, Any, DefaultDict, overload
import numpy as np
from pandas._libs.writers import convert_json_to_lines
from pandas.util._decorators import set_module
import pandas as pd
from pandas import DataFrame, Series
if TYPE_CHECKING:
    from collections.abc import Iterable
    from pandas._typing import IgnoreRaise, Scalar

def convert_to_line_delimits(s = None):
    '''
    Helper function that converts JSON lists to line delimited JSON.
    '''
    if s[0] == '[' and s[-1] == ']':
        return s
    s = None[1:-1]
    return convert_json_to_lines(s)

nested_to_record = (lambda ds = None, prefix = None, sep = overload, level = (..., ..., ..., ...), max_level = ('ds', 'dict', 'prefix', 'str', 'sep', 'str', 'level', 'int', 'max_level', 'int | None', 'return', 'dict[str, Any]'): pass)()
nested_to_record = (lambda ds = None, prefix = None, sep = overload, level = (..., ..., ..., ...), max_level = ('ds', 'list[dict]', 'prefix', 'str', 'sep', 'str', 'level', 'int', 'max_level', 'int | None', 'return', 'list[dict[str, Any]]'): pass)()

def nested_to_record(ds = None, prefix = None, sep = None, level = ('', '.', 0, None), max_level = ('ds', 'dict | list[dict]', 'prefix', 'str', 'sep', 'str', 'level', 'int', 'max_level', 'int | None', 'return', 'dict[str, Any] | list[dict[str, Any]]')):
    '''
    A simplified json_normalize

    Converts a nested dict into a flat dict ("record"), unlike json_normalize,
    it does not attempt to extract a subset of the data.

    Parameters
    ----------
    ds : dict or list of dicts
    prefix: the prefix, optional, default: ""
    sep : str, default \'.\'
        Nested records will generate names separated by sep,
        e.g., for sep=\'.\', { \'foo\' : { \'bar\' : 0 } } -> foo.bar
    level: int, optional, default: 0
        The number of levels in the json string.

    max_level: int, optional, default: None
        The max depth to normalize.

    Returns
    -------
    d - dict or list of dicts, matching `ds`

    Examples
    --------
    >>> nested_to_record(
    ...     dict(flat1=1, dict1=dict(c=1, d=2), nested=dict(e=dict(c=1, d=2), d=2))
    ... )
    {\'flat1\': 1, \'dict1.c\': 1, \'dict1.d\': 2, \'nested.e.c\': 1, \'nested.e.d\': 2, \'nested.d\': 2}
    '''
    singleton = False
    if isinstance(ds, dict):
        ds = [
            ds]
        singleton = True
    new_ds = []
# WARNING: Decompyle incomplete


def _normalize_json(data = None, key_string = None, normalized_dict = None, separator = ('data', 'Any', 'key_string', 'str', 'normalized_dict', 'dict[str, Any]', 'separator', 'str', 'return', 'dict[str, Any]')):
    """
    Main recursive function
    Designed for the most basic use case of pd.json_normalize(data)
    intended as a performance improvement, see #15621

    Parameters
    ----------
    data : Any
        Type dependent on types contained within nested Json
    key_string : str
        New key (with separator(s) in) for data
    normalized_dict : dict
        The new normalized/flattened Json dict
    separator : str, default '.'
        Nested records will generate names separated by sep,
        e.g., for sep='.', { 'foo' : { 'bar' : 0 } } -> foo.bar
    """
    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f'''{key_string}{separator}{key}'''
            if not key_string:
                new_key = new_key.removeprefix(separator)
            _normalize_json(data = value, key_string = new_key, normalized_dict = normalized_dict, separator = separator)
    normalized_dict[key_string] = data
    return normalized_dict


def _normalize_json_ordered(data = None, separator = None):
    """
    Order the top level keys and then recursively go to depth

    Parameters
    ----------
    data : dict or list of dicts
    separator : str, default '.'
        Nested records will generate names separated by sep,
        e.g., for sep='.', { 'foo' : { 'bar' : 0 } } -> foo.bar

    Returns
    -------
    dict or list of dicts, matching `normalized_json_object`
    """
    top_dict_ = data.items()()
    nested_dict_ = (lambda .0: pass# WARNING: Decompyle incomplete
)(data = data.items()(), key_string = '', normalized_dict = { }, separator = separator)
# WARNING: Decompyle incomplete


def _simple_json_normalize(ds = None, sep = None):
    '''
    An optimized basic json_normalize

    Converts a nested dict into a flat dict ("record"), unlike
    json_normalize and nested_to_record it doesn\'t do anything clever.
    But for the most basic use cases it enhances performance.
    E.g. pd.json_normalize(data)

    Parameters
    ----------
    ds : dict or list of dicts
    sep : str, default \'.\'
        Nested records will generate names separated by sep,
        e.g., for sep=\'.\', { \'foo\' : { \'bar\' : 0 } } -> foo.bar

    Returns
    -------
    frame : DataFrame
    d - dict or list of dicts, matching `normalized_json_object`

    Examples
    --------
    >>> _simple_json_normalize(
    ...     {
    ...         "flat1": 1,
    ...         "dict1": {"c": 1, "d": 2},
    ...         "nested": {"e": {"c": 1, "d": 2}, "d": 2},
    ...     }
    ... )
    {\'flat1\': 1, \'dict1.c\': 1, \'dict1.d\': 2, \'nested.e.c\': 1, \'nested.e.d\': 2, \'nested.d\': 2}

    '''
    pass
# WARNING: Decompyle incomplete


def _validate_meta(meta = None):
    '''
    Validate that meta parameter contains only strings or lists of strings.
    Parameters
    ----------
    meta : str or list of str or list of list of str or None
        The meta parameter to validate.
    Raises
    ------
    TypeError
        If meta contains elements that are not strings or lists of strings.
    '''
    pass
# WARNING: Decompyle incomplete

json_normalize = (lambda data, record_path, meta, meta_prefix = None, record_prefix = None, errors = set_module('pandas'), sep = (None, None, None, None, 'raise', '.', None), max_level = ('data', 'dict | list[dict] | Series', 'record_path', 'str | list | None', 'meta', 'str | list[str | list[str]] | None', 'meta_prefix', 'str | None', 'record_prefix', 'str | None', 'errors', 'IgnoreRaise', 'sep', 'str', 'max_level', 'int | None', 'return', 'DataFrame'): pass# WARNING: Decompyle incomplete
)()
