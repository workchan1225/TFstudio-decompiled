# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: monkeypatch.pyc (Python 3.11)

'''Monkeypatching and mocking functionality.'''
from __future__ import annotations
from collections.abc import Generator
from collections.abc import Mapping
from collections.abc import MutableMapping
from contextlib import contextmanager
import os
from pathlib import Path
import re
import sys
from typing import Any
from typing import final
from typing import overload
from typing import TypeVar
import warnings
from _pytest.deprecated import MONKEYPATCH_LEGACY_NAMESPACE_PACKAGES
from _pytest.fixtures import fixture
from _pytest.warning_types import PytestWarning
RE_IMPORT_ERROR_NAME = re.compile('^No module named (.*)$')
K = TypeVar('K')
V = TypeVar('V')
monkeypatch = (lambda : pass# WARNING: Decompyle incomplete
)()

def resolve(name = None):
    parts = name.split('.')
    used = parts.pop(0)
    found = __import__(used)
    for part in parts:
        used += '.' + part
        found = getattr(found, part)
        except AttributeError:
            pass
        __import__(used)
    except ImportError:
        ex = None
        expected = str(ex).split()[-1]
        if expected == used:
            raise 
        raise ImportError(f'''import error in {used}: {ex}'''), ex
        ex = None
        del ex
    found = annotated_getattr(found, part, used)
    continue
    return found


def annotated_getattr(obj = None, name = None, ann = None):
    
    try:
        obj = getattr(obj, name)
    except AttributeError:
        e = None
        raise AttributeError(f'''{type(obj).__name__!r} object at {ann} has no attribute {name!r}'''), e
        e = None
        del e

    return obj


def derive_importpath(import_path = None, raising = None):
    if isinstance(import_path, str) or '.' not in import_path:
        raise TypeError(f'''must be absolute import path string, not {import_path!r}''')
    (module, attr) = import_path.rsplit('.', 1)
    target = resolve(module)
    if raising:
        annotated_getattr(target, attr, ann = module)
    return (attr, target)


class Notset:
    
    def __repr__(self = None):
        return '<notset>'


notset = Notset()
MonkeyPatch = <NODE:12>()
