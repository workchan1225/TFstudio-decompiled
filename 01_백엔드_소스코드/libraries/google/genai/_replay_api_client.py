# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _replay_api_client.pyc (Python 3.11)

'''Replay API client.'''
import base64
import copy
import contextlib
import enum
import inspect
import io
import json
import os
import re
from typing import Any, Literal, Optional, Union, Iterator, AsyncIterator
import google.auth as google
from  import errors
from _api_client import BaseApiClient
from _api_client import HttpRequest
from _api_client import HttpResponse
from _common import BaseModel
from types import HttpOptions, HttpOptionsOrDict

def to_snake_case(name = None):
    '''Converts a string from camelCase or PascalCase to snake_case.'''
    if not isinstance(name, str):
        name = str(name)
    s1 = re.sub('(.)([A-Z][a-z]+)', '\\1_\\2', name)
    return re.sub('([a-z0-9])([A-Z])', '\\1_\\2', s1).lower()


def _normalize_json_case(obj = None):
    if isinstance(obj, dict):
        return obj.items()()
    if None(obj, list):
        return obj()
    if None(obj, enum.Enum):
        return obj.value
    if None(obj, str) and 'division by zero' in obj:
        return obj.replace('division by zero', 'integer division or modulo by zero')


def _equals_ignore_key_case(obj1 = None, obj2 = None):
    """Compares two Python objects for equality ignoring key casing.

  Returns:
      bool: True if the two objects are equal regardless of key casing
  (camelCase vs. snake_case). For example, the following are considered equal:

  {'my_key': 'my_value'}
  {'myKey': 'my_value'}

  This also considers enums and strings with the same value as equal.
  For example, the following are considered equal:

  {'type': <Type.STRING: 'STRING'>}}
  {'type': 'STRING'}
  """
    normalized_obj_1 = _normalize_json_case(obj1)
    normalized_obj_2 = _normalize_json_case(obj2)
    if normalized_obj_1 == normalized_obj_2:
        return True


def _redact_version_numbers(version_string = None):
    '''Redacts version numbers in the form x.y.z from a string.'''
    return re.sub('\\d+\\.\\d+\\.\\d+[a-zA-Z0-9]*', '{VERSION_NUMBER}', version_string)


def _redact_language_label(language_label = None):
    '''Removed because replay requests are used for all languages.'''
    return re.sub('gl-python/', '{LANGUAGE_LABEL}/', language_label)


def _redact_request_headers(headers = None):
    '''Redacts headers that should not be recorded.'''
    redacted_headers = { }
    for header_name, header_value in headers.items():
        if header_name.lower() == 'x-goog-api-key':
            redacted_headers[header_name] = '{REDACTED}'
            continue
        if header_name.lower() == 'user-agent':
            redacted_headers[header_name] = _redact_language_label(_redact_version_numbers(header_value))
            continue
        if header_name.lower() == 'x-goog-api-client':
            redacted_headers[header_name] = _redact_language_label(_redact_version_numbers(header_value))
            continue
        if header_name.lower() == 'x-goog-user-project':
            continue
        if header_name.lower() == 'authorization':
            continue
        redacted_headers[header_name] = header_value
        return redacted_headers


def _redact_request_url(url = None):
    result = re.sub('.*/projects/[^/]+/locations/[^/]+/', '{VERTEX_URL_PREFIX}/', url)
    result = re.sub('.*-aiplatform.googleapis.com/[^/]+/', '{VERTEX_URL_PREFIX}/', result)
    result = re.sub('.*aiplatform.googleapis.com/[^/]+/', '{VERTEX_URL_PREFIX}/', result)
    result = re.sub('.*generativelanguage.*.googleapis.com/[^/]+', '{MLDEV_URL_PREFIX}', result)
    return result


def _redact_project_location_path(path = None):
    if 'projects/' in path and 'locations/' in path:
        result = re.sub('projects/[^/]+/locations/[^/]+/', '{PROJECT_AND_LOCATION_PATH}/', path)
        return result


def _redact_request_body(body = None):
    '''Redacts fields in the request body in place.'''
    for key, value in body.items():
        if isinstance(value, str):
            body[key] = _redact_project_location_path(value)
        return None


def redact_http_request(http_request = None):
    http_request.headers = _redact_request_headers(http_request.headers)
    http_request.url = _redact_request_url(http_request.url)
    if not isinstance(http_request.data, bytes):
        _redact_request_body(http_request.data)
        return None


def _current_file_path_and_line():
    '''Prints the current file path and line number.'''
    current_frame = inspect.currentframe()
# WARNING: Decompyle incomplete


def _debug_print(message = None):
    print('DEBUG (test', os.environ.get('PYTEST_CURRENT_TEST'), ')', _current_file_path_and_line(), ':\n    ', message)


def pop_undeterministic_headers(headers = None):
    '''Remove headers that are not deterministic.'''
    headers.pop('Date', None)
    headers.pop('Server-Timing', None)

_record_on_api_error = (lambda client = None, http_request = None: pass# WARNING: Decompyle incomplete
)()
_async_record_on_api_error = (lambda client = None, http_request = None: pass# WARNING: Decompyle incomplete
)()

class ReplayRequest(BaseModel):
    body_segments: list[dict[(str, object)]] = 'Represents a single request in a replay.'


class ReplayResponse(BaseModel):
    '''Represents a single response in a replay.'''
    body_segments: list[dict[(str, object)]] = 200
    sdk_response_segments: list[dict[(str, object)]] = None
    
    def model_post_init(self = None, _ReplayResponse__context = None):
        pop_undeterministic_headers(self.headers)



class ReplayInteraction(BaseModel):
    response: ReplayResponse = 'Represents a single interaction, request and response in a replay.'


class ReplayFile(BaseModel):
    interactions: list[ReplayInteraction] = 'Represents a recorded session.'


class ReplayApiClient(BaseApiClient):
    pass
# WARNING: Decompyle incomplete
