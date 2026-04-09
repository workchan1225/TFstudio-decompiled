# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _helpers.pyc (Python 3.11)

'''Helper functions for commonly used utilities.'''
import base64
import calendar
import datetime
from email.message import Message
import hashlib
import json
import logging
import os
import sys
from typing import Any, Dict, Mapping, Optional, Union
import urllib
from google.auth import exceptions
_BASE_LOGGER_NAME = 'google'
_LOGGING_INITIALIZED = False
REFRESH_THRESHOLD = datetime.timedelta(minutes = 3, seconds = 45)
_SENSITIVE_FIELDS = {
    'id_token',
    'client_id',
    'accessToken',
    'access_token',
    'client_secret',
    'refresh_token'}

def copy_docstring(source_class):
    """Decorator that copies a method's docstring from another class.

    Args:
        source_class (type): The class that has the documented method.

    Returns:
        Callable: A decorator that will copy the docstring of the same
            named method in the source class to the decorated method.
    """
    pass
# WARNING: Decompyle incomplete


def parse_content_type(header_value):
    """Parse a 'content-type' header value to get just the plain media-type (without parameters).

    This is done using the class Message from email.message as suggested in PEP 594
        (because the cgi is now deprecated and will be removed in python 3.13,
        see https://peps.python.org/pep-0594/#cgi).

    Args:
        header_value (str): The value of a 'content-type' header as a string.

    Returns:
        str: A string with just the lowercase media-type from the parsed 'content-type' header.
            If the provided content-type is not parsable, returns 'text/plain',
            the default value for textual files.
    """
    m = Message()
    m['content-type'] = header_value
    return m.get_content_type()


def utcnow():
    '''Returns the current UTC datetime.

    Returns:
        datetime: The current time in UTC.
    '''
    now = datetime.datetime.now(datetime.timezone.utc)
    now = now.replace(tzinfo = None)
    return now


def datetime_to_secs(value):
    '''Convert a datetime object to the number of seconds since the UNIX epoch.

    Args:
        value (datetime): The datetime to convert.

    Returns:
        int: The number of seconds since the UNIX epoch.
    '''
    return calendar.timegm(value.utctimetuple())


def to_bytes(value, encoding = ('utf-8',)):
    '''Converts a string value to bytes, if necessary.

    Args:
        value (Union[str, bytes]): The value to be converted.
        encoding (str): The encoding to use to convert unicode to bytes.
            Defaults to "utf-8".

    Returns:
        bytes: The original value converted to bytes (if unicode) or as
            passed in if it started out as bytes.

    Raises:
        google.auth.exceptions.InvalidValue: If the value could not be converted to bytes.
    '''
    result = value.encode(encoding) if isinstance(value, str) else value
    if isinstance(result, bytes):
        return result
    raise None.InvalidValue('{0!r} could not be converted to bytes'.format(value))


def from_bytes(value):
    '''Converts bytes to a string value, if necessary.

    Args:
        value (Union[str, bytes]): The value to be converted.

    Returns:
        str: The original value converted to unicode (if bytes) or as passed in
            if it started out as unicode.

    Raises:
        google.auth.exceptions.InvalidValue: If the value could not be converted to unicode.
    '''
    result = value.decode('utf-8') if isinstance(value, bytes) else value
    if isinstance(result, str):
        return result
    raise None.InvalidValue('{0!r} could not be converted to unicode'.format(value))


def update_query(url, params, remove = (None,)):
    """Updates a URL's query parameters.

    Replaces any current values if they are already present in the URL.

    Args:
        url (str): The URL to update.
        params (Mapping[str, str]): A mapping of query parameter
            keys to values.
        remove (Sequence[str]): Parameters to remove from the query string.

    Returns:
        str: The URL with updated query parameters.

    Examples:

        >>> url = 'http://example.com?a=1'
        >>> update_query(url, {'a': '2'})
        http://example.com?a=2
        >>> update_query(url, {'b': '3'})
        http://example.com?a=1&b=3
        >> update_query(url, {'b': '3'}, remove=['a'])
        http://example.com?b=3

    """
    pass
# WARNING: Decompyle incomplete


def scopes_to_string(scopes):
    '''Converts scope value to a string suitable for sending to OAuth 2.0
    authorization servers.

    Args:
        scopes (Sequence[str]): The sequence of scopes to convert.

    Returns:
        str: The scopes formatted as a single string.
    '''
    return ' '.join(scopes)


def string_to_scopes(scopes):
    '''Converts stringifed scopes value to a list.

    Args:
        scopes (Union[Sequence, str]): The string of space-separated scopes
            to convert.
    Returns:
        Sequence(str): The separated scopes.
    '''
    if not scopes:
        return []
    return None.split(' ')


def padded_urlsafe_b64decode(value):
    '''Decodes base64 strings lacking padding characters.

    Google infrastructure tends to omit the base64 padding characters.

    Args:
        value (Union[str, bytes]): The encoded value.

    Returns:
        bytes: The decoded value
    '''
    b64string = to_bytes(value)
    padded = b64string + b'=' * (-len(b64string) % 4)
    return base64.urlsafe_b64decode(padded)


def unpadded_urlsafe_b64encode(value):
    """Encodes base64 strings removing any padding characters.

    `rfc 7515`_ defines Base64url to NOT include any padding
    characters, but the stdlib doesn't do that by default.

    _rfc7515: https://tools.ietf.org/html/rfc7515#page-6

    Args:
        value (Union[str|bytes]): The bytes-like value to encode

    Returns:
        Union[str|bytes]: The encoded value
    """
    return base64.urlsafe_b64encode(value).rstrip(b'=')


def get_bool_from_env(variable_name, default = (False,)):
    '''Gets a boolean value from an environment variable.

    The environment variable is interpreted as a boolean with the following
    (case-insensitive) rules:
    - "true", "1" are considered true.
    - "false", "0" are considered false.
    Any other values will raise an exception.

    Args:
        variable_name (str): The name of the environment variable.
        default (bool): The default value if the environment variable is not
            set.

    Returns:
        bool: The boolean value of the environment variable.

    Raises:
        google.auth.exceptions.InvalidValue: If the environment variable is
            set to a value that can not be interpreted as a boolean.
    '''
    value = os.environ.get(variable_name)
# WARNING: Decompyle incomplete


def is_python_3():
    '''Check if the Python interpreter is Python 2 or 3.

    Returns:
        bool: True if the Python interpreter is Python 3 and False otherwise.
    '''
    return sys.version_info > (3, 0)


def _hash_sensitive_info(data = None):
    '''
    Hashes sensitive information within a dictionary.

    Args:
        data: The dictionary containing data to be processed.

    Returns:
        A new dictionary with sensitive values replaced by their SHA512 hashes.
        If the input is a list, returns a list with each element recursively processed.
        If the input is neither a dict nor a list, returns the type of the input as a string.

    '''
    if isinstance(data, dict):
        hashed_data = { }
        for key, value in data.items():
            if not key in _SENSITIVE_FIELDS and isinstance(value, (dict, list)):
                hashed_data[key] = _hash_value(value, key)
                continue
            if isinstance(value, (dict, list)):
                hashed_data[key] = _hash_sensitive_info(value)
                continue
            hashed_data[key] = value
            return hashed_data
            if isinstance(data, list):
                hashed_list = []
                for val in data:
                    hashed_list.append(_hash_sensitive_info(val))
                    return hashed_list
                    return str(type(data))


def _hash_value(value = None, field_name = None):
    '''Hashes a value and returns a formatted hash string.'''
    pass
# WARNING: Decompyle incomplete


def _logger_configured(logger = None):
