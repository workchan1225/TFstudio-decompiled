# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _common.pyc (Python 3.11)

'''Common utilities for the SDK.'''
import base64
import collections.abc as collections
import datetime
import enum
import functools
import logging
import re
import typing
from typing import Any, Callable, FrozenSet, Optional, Union, get_args, get_origin
import uuid
import warnings
import pydantic
from pydantic import alias_generators
from typing_extensions import TypeAlias
logger = logging.getLogger('google_genai._common')
StringDict: TypeAlias = dict[(str, Any)]

class ExperimentalWarning(Warning):
    '''Warning for experimental features.'''
    pass


def set_value_by_path(data = None, keys = None, value = None):
    """Examples:

  set_value_by_path({}, ['a', 'b'], v)
    -> {'a': {'b': v}}
  set_value_by_path({}, ['a', 'b[]', c], [v1, v2])
    -> {'a': {'b': [{'c': v1}, {'c': v2}]}}
  set_value_by_path({'a': {'b': [{'c': v1}, {'c': v2}]}}, ['a', 'b[]', 'd'], v3)
    -> {'a': {'b': [{'c': v1, 'd': v3}, {'c': v2, 'd': v3}]}}
  """
    pass
# WARNING: Decompyle incomplete


def get_value_by_path(data = None, keys = None, *, default_value):
    """Examples:

  get_value_by_path({'a': {'b': v}}, ['a', 'b'])
    -> v
  get_value_by_path({'a': {'b': [{'c': v1}, {'c': v2}]}}, ['a', 'b[]', 'c'])
    -> [v1, v2]
  """
    pass
# WARNING: Decompyle incomplete


def move_value_by_path(data = None, paths = None):
    """Moves values from source paths to destination paths.

  Examples:
    move_value_by_path(
      {'requests': [{'content': v1}, {'content': v2}]},
      {'requests[].*': 'requests[].request.*'}
    )
      -> {'requests': [{'request': {'content': v1}}, {'request': {'content':
      v2}}]}
  """
    for source_path, dest_path in paths.items():
        source_keys = source_path.split('.')
        dest_keys = dest_path.split('.')
        exclude_keys = set()
        wildcard_idx = -1
        for i, key in enumerate(source_keys):
            if key == '*':
                wildcard_idx = i
            
            if wildcard_idx != -1 and len(dest_keys) > wildcard_idx:
                for i in range(wildcard_idx, len(dest_keys)):
                    key = dest_keys[i]
                    if not key != '*' and key.endswith('[]') and key.endswith('[0]'):
                        exclude_keys.add(key)
                    _move_value_recursive(data, source_keys, dest_keys, 0, exclude_keys)
                    return None


def _move_value_recursive(data, source_keys = None, dest_keys = None, key_idx = None, exclude_keys = ('data', Any, 'source_keys', list[str], 'dest_keys', list[str], 'key_idx', int, 'exclude_keys', set[str], 'return', None)):
    '''Recursively moves values from source path to destination path.'''
    pass
# WARNING: Decompyle incomplete


def maybe_snake_to_camel(snake_str = None, convert = None):
    '''Converts a snake_case string to CamelCase, if convert is True.'''
    if not convert:
        return snake_str
    return None.sub('_([a-zA-Z])', (lambda match: match.group(1).upper()), snake_str)


def convert_to_dict(obj = None, convert_keys = None):
    """Recursively converts a given object to a dictionary.

  If the object is a Pydantic model, it uses the model's `model_dump()` method.

  Args:
    obj: The object to convert.
    convert_keys: Whether to convert the keys from snake case to camel case.

  Returns:
    A dictionary representation of the object, a list of objects if a list is
    passed, or the object itself if it is not a dictionary, list, or Pydantic
    model.
  """
    pass
# WARNING: Decompyle incomplete


def _is_struct_type(annotation = None):
