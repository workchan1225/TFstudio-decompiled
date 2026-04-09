# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: path_template.pyc (Python 3.11)

'''Expand and validate URL path templates.

This module provides the :func:`expand` and :func:`validate` functions for
interacting with Google-style URL `path templates`_ which are commonly used
in Google APIs for `resource names`_.

.. _path templates: https://github.com/googleapis/googleapis/blob
    /57e2d376ac7ef48681554204a3ba78a414f2c533/google/api/http.proto#L212
.. _resource names: https://cloud.google.com/apis/design/resource_names
'''
from __future__ import unicode_literals
from collections import deque
import copy
import functools
import re
_VARIABLE_RE = re.compile("\n    (  # Capture the entire variable expression\n        (?P<positional>\\*\\*?)  # Match & capture * and ** positional variables.\n        |\n        # Match & capture named variables {name}\n        {\n            (?P<name>[^/]+?)\n            # Optionally match and capture the named variable's template.\n            (?:=(?P<template>.+?))?\n        }\n    )\n    ", re.VERBOSE)
_SINGLE_SEGMENT_PATTERN = '([^/]+)'
_MULTI_SEGMENT_PATTERN = '(.+)'

def _expand_variable_match(positional_vars, named_vars, match):
    '''Expand a matched variable with its value.

    Args:
        positional_vars (list): A list of positional variables. This list will
            be modified.
        named_vars (dict): A dictionary of named variables.
        match (re.Match): A regular expression match.

    Returns:
        str: The expanded variable to replace the match.

    Raises:
        ValueError: If a positional or named variable is required by the
            template but not specified or if an unexpected template expression
            is encountered.
    '''
    positional = match.group('positional')
    name = match.group('name')
# WARNING: Decompyle incomplete


def expand(tmpl, *args, **kwargs):
    """Expand a path template with the given variables.

    .. code-block:: python

        >>> expand('users/*/messages/*', 'me', '123')
        users/me/messages/123
        >>> expand('/v1/{name=shelves/*/books/*}', name='shelves/1/books/3')
        /v1/shelves/1/books/3

    Args:
        tmpl (str): The path template.
        args: The positional variables for the path.
        kwargs: The named variables for the path.

    Returns:
        str: The expanded path

    Raises:
        ValueError: If a positional or named variable is required by the
            template but not specified or if an unexpected template expression
            is encountered.
    """
    replacer = functools.partial(_expand_variable_match, list(args), kwargs)
    return _VARIABLE_RE.sub(replacer, tmpl)


def _replace_variable_with_pattern(match):
    '''Replace a variable match with a pattern that can be used to validate it.

    Args:
        match (re.Match): A regular expression match

    Returns:
        str: A regular expression pattern that can be used to validate the
            variable in an expanded path.

    Raises:
        ValueError: If an unexpected template expression is encountered.
    '''
    positional = match.group('positional')
    name = match.group('name')
    template = match.group('template')
# WARNING: Decompyle incomplete


def _generate_pattern_for_template(tmpl):
    '''Generate a pattern that can validate a path template.

    Args:
        tmpl (str): The path template

    Returns:
        str: A regular expression pattern that can be used to validate an
            expanded path template.
    '''
    return _VARIABLE_RE.sub(_replace_variable_with_pattern, tmpl)


def get_field(request, field):
    '''Get the value of a field from a given dictionary.

    Args:
        request (dict | Message): A dictionary or a Message object.
        field (str): The key to the request in dot notation.

    Returns:
        The value of the field.
    '''
    parts = field.split('.')
    value = request
    for part in parts:
        if not isinstance(value, dict):
            value = getattr(value, part, None)
            continue
        value = value.get(part)
        if isinstance(value, dict):
            return None
        return None


def delete_field(request, field):
    '''Delete the value of a field from a given dictionary.

    Args:
        request (dict | Message): A dictionary object or a Message.
        field (str): The key to the request in dot notation.
    '''
    parts = deque(field.split('.'))
# WARNING: Decompyle incomplete


def validate(tmpl, path):
    """Validate a path against the path template.

    .. code-block:: python

        >>> validate('users/*/messages/*', 'users/me/messages/123')
        True
        >>> validate('users/*/messages/*', 'users/me/drafts/123')
        False
        >>> validate('/v1/{name=shelves/*/books/*}', /v1/shelves/1/books/3)
        True
        >>> validate('/v1/{name=shelves/*/books/*}', /v1/shelves/1/tapes/3)
        False

    Args:
        tmpl (str): The path template.
        path (str): The expanded path.

    Returns:
        bool: True if the path matches.
    """
    pattern = _generate_pattern_for_template(tmpl) + '$'
# WARNING: Decompyle incomplete


def transcode(http_options, message = (None,), **request_kwargs):
    """Transcodes a grpc request pattern into a proper HTTP request following the rules outlined here,
    https://github.com/googleapis/googleapis/blob/master/google/api/http.proto#L44-L312

     Args:
         http_options (list(dict)): A list of dicts which consist of these keys,
             'method'    (str): The http method
             'uri'       (str): The path template
             'body'      (str): The body field name (optional)
             (This is a simplified representation of the proto option `google.api.http`)

         message (Message) : A request object (optional)
         request_kwargs (dict) : A dict representing the request object

     Returns:
         dict: The transcoded request with these keys,
             'method'        (str)   : The http method
             'uri'           (str)   : The expanded uri
             'body'          (dict | Message)  : A dict or a Message representing the body (optional)
             'query_params'  (dict | Message)  : A dict or Message mapping query parameter variables and values

     Raises:
         ValueError: If the request does not match the given template.
    """
    pass
# WARNING: Decompyle incomplete
