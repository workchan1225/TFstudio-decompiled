# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _legacy.pyc (Python 3.11)

import functools
import os
import pathlib
import types
import warnings
from typing import Union, Iterable, ContextManager, BinaryIO, TextIO, Any
from  import _common
Package = Union[(types.ModuleType, str)]
Resource = str

def deprecated(func):
    pass
# WARNING: Decompyle incomplete


def normalize_path(path):
    '''Normalize a path by ensuring it is a string.

    If the resulting string contains path separators, an exception is raised.
    '''
    str_path = str(path)
    (parent, file_name) = os.path.split(str_path)
    if parent:
        raise ValueError(f'''{path!r} must be only a file name''')
    return file_name

open_binary = (lambda package = None, resource = None: (_common.files(package) / normalize_path(resource)).open('rb'))()
read_binary = (lambda package = None, resource = None: (_common.files(package) / normalize_path(resource)).read_bytes())()
open_text = (lambda package = None, resource = None, encoding = deprecated, errors = ('utf-8', 'strict'): (_common.files(package) / normalize_path(resource)).open('r', encoding = encoding, errors = errors))()
read_text = (lambda package = None, resource = None, encoding = deprecated, errors = ('utf-8', 'strict'): fp = open_text(package, resource, encoding, errors)None(None, None)with None:
if not None, fp.read():
pass)()
contents = (lambda package = None: _common.files(package).iterdir()())()
is_resource = (lambda package = None, name = None: pass# WARNING: Decompyle incomplete
)()
path = (lambda package = None, resource = None: _common.as_file(_common.files(package) / normalize_path(resource)))()
