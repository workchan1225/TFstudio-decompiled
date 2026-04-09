# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: imports.pyc (Python 3.11)

from __future__ import annotations
import warnings
from collections.abc import Iterable
from typing import Any
__all__ = [
    'lazy_import']

def import_name(name = None, source = None, namespace = None):
    '''
    Import ``name`` from ``source`` in ``namespace``.

    There are two use cases:

    - ``name`` is an object defined in ``source``;
    - ``name`` is a submodule of ``source``.

    Neither :func:`__import__` nor :func:`~importlib.import_module` does
    exactly this. :func:`__import__` is closer to the intended behavior.

    '''
    level = 0
# WARNING: Decompyle incomplete


def lazy_import(namespace = None, aliases = None, deprecated_aliases = None):
    '''
    Provide lazy, module-level imports.

    Typical use::

        __getattr__, __dir__ = lazy_import(
            globals(),
            aliases={
                "<name>": "<source module>",
                ...
            },
            deprecated_aliases={
                ...,
            }
        )

    This function defines ``__getattr__`` and ``__dir__`` per :pep:`562`.

    '''
    pass
# WARNING: Decompyle incomplete
