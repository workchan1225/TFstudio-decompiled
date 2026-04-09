# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rest_helpers.pyc (Python 3.11)

'''Helpers for rest transports.'''
import functools
import operator

def flatten_query_params(obj, strict = (False,)):
    """Flatten a dict into a list of (name,value) tuples.

    The result is suitable for setting query params on an http request.

    .. code-block:: python

        >>> obj = {'a':
        ...         {'b':
        ...           {'c': ['x', 'y', 'z']} },
        ...      'd': 'uvw',
        ...      'e': True, }
        >>> flatten_query_params(obj, strict=True)
        [('a.b.c', 'x'), ('a.b.c', 'y'), ('a.b.c', 'z'), ('d', 'uvw'), ('e', 'true')]

    Note that, as described in
    https://github.com/googleapis/googleapis/blob/48d9fb8c8e287c472af500221c6450ecd45d7d39/google/api/http.proto#L117,
    repeated fields (i.e. list-valued fields) may only contain primitive types (not lists or dicts).
    This is enforced in this function.

    Args:
      obj: a possibly nested dictionary (from json), or None
      strict: a bool, defaulting to False, to enforce that all values in the
              result tuples be strings and, if boolean, lower-cased.

    Returns: a list of tuples, with each tuple having a (possibly) multi-part name
      and a scalar value.

    Raises:
      TypeError if obj is not a dict or None
      ValueError if obj contains a list of non-primitive values.
    """
    pass
# WARNING: Decompyle incomplete


def _flatten(obj, key_path, strict = (False,)):
    pass
# WARNING: Decompyle incomplete


def _is_primitive_value(obj):
    pass
# WARNING: Decompyle incomplete


def _flatten_value(obj, key_path, strict = (False,)):
    return [
        ('.'.join(key_path), _canonicalize(obj, strict = strict))]


def _flatten_dict(obj, key_path, strict = (False,)):
    pass
# WARNING: Decompyle incomplete


def _flatten_list(elems, key_path, strict = (False,)):
    pass
# WARNING: Decompyle incomplete


def _canonicalize(obj, strict = (False,)):
    if strict:
        value = str(obj)
        if isinstance(obj, bool):
            value = value.lower()
        return value
