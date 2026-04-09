# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _common.pyc (Python 3.11)

import os
import pathlib
import tempfile
import functools
import contextlib
import types
import importlib
from typing import Union, Optional
from abc import ResourceReader, Traversable
from _compat import wrap_spec
Package = Union[(types.ModuleType, str)]

def files(package):
    '''
    Get a Traversable resource from a package
    '''
    return from_package(get_package(package))


def get_resource_reader(package):
    """
    Return the package's loader if it's a ResourceReader.
    """
    spec = package.__spec__
    reader = getattr(spec.loader, 'get_resource_reader', None)
# WARNING: Decompyle incomplete


def resolve(cand):
    return cand if isinstance(cand, types.ModuleType) else importlib.import_module(cand)


def get_package(package):
    '''Take a package name or module object and return the module.

    Raise an exception if the resolved module is not a package.
    '''
    resolved = resolve(package)
# WARNING: Decompyle incomplete


def from_package(package):
    '''
    Return a Traversable object for the given package.

    '''
    spec = wrap_spec(package)
    reader = spec.loader.get_resource_reader(spec.name)
    return reader.files()

_tempfile = (lambda reader, suffix = ('',): pass# WARNING: Decompyle incomplete
)()
as_file = (lambda path: _tempfile(path.read_bytes, suffix = path.name))()
_ = (lambda path: pass# WARNING: Decompyle incomplete
)()()
