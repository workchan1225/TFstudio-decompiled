# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _deprecate.pyc (Python 3.11)

from __future__ import annotations
import sys
import warnings
from functools import wraps
from typing import TYPE_CHECKING, ClassVar, TypeVar
import attrs
if TYPE_CHECKING:
    from collections.abc import Callable
    from typing_extensions import ParamSpec
    ArgsT = ParamSpec('ArgsT')
RetT = TypeVar('RetT')

class TrioDeprecationWarning(FutureWarning):
    '''Warning emitted if you use deprecated Trio functionality.

    While a relatively mature project, Trio remains committed to refining its
    design and improving usability. As part of this, we occasionally deprecate
    or remove functionality that proves suboptimal. If you use Trio, we
    recommend `subscribing to issue #1
    <https://github.com/python-trio/trio/issues/1>`__ to get information about
    upcoming deprecations and other backwards compatibility breaking changes.

    Despite the name, this class currently inherits from
    :class:`FutureWarning`, not :class:`DeprecationWarning`, because until a
    1.0 release, we want these warnings to be visible by default. You can hide
    them by installing a filter or with the ``-W`` switch: see the
    :mod:`warnings` documentation for details.
    '''
    pass


def _url_for_issue(issue = None):
    return f'''https://github.com/python-trio/trio/issues/{issue}'''


def _stringify(thing = None):
    if hasattr(thing, '__module__') and hasattr(thing, '__qualname__'):
        return f'''{thing.__module__}.{thing.__qualname__}'''
    return None(thing)


def warn_deprecated(thing = None, version = None, *, issue, instead, stacklevel, use_triodeprecationwarning):
    stacklevel += 1
    msg = f'''{_stringify(thing)} is deprecated since Trio {version}'''
# WARNING: Decompyle incomplete


def deprecated(version = None, *, thing, issue, instead, use_triodeprecationwarning):
    pass
# WARNING: Decompyle incomplete


def deprecated_alias(old_qualname = None, new_fn = None, version = None, *, issue):
    pass
# WARNING: Decompyle incomplete

DeprecatedAttribute = <NODE:12>()

def deprecate_attributes(module_name = None, deprecated_attributes = None):
    pass
# WARNING: Decompyle incomplete
