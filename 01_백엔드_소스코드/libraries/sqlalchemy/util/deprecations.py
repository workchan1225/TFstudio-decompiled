# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: deprecations.pyc (Python 3.11)

'''Helpers related to deprecation of functions, methods, classes, other
functionality.'''
from __future__ import annotations
import re
from typing import Any
from typing import Callable
from typing import Dict
from typing import Match
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union
from  import compat
from langhelpers import _hash_limit_string
from langhelpers import _warnings_warn
from langhelpers import decorator
from langhelpers import inject_docstring_text
from langhelpers import inject_param_text
from  import exc
_T = TypeVar('_T', bound = Any)
_F = TypeVar('_F', bound = 'Callable[..., Any]')

def _warn_with_version(msg = None, version = None, type_ = None, stacklevel = (None,), code = ('msg', 'str', 'version', 'str', 'type_', 'Type[exc.SADeprecationWarning]', 'stacklevel', 'int', 'code', 'Optional[str]', 'return', 'None')):
    warn = type_(msg, code = code)
    warn.deprecated_since = version
    _warnings_warn(warn, stacklevel = stacklevel + 1)


def warn_deprecated(msg = None, version = None, stacklevel = None, code = (3, None)):
    _warn_with_version(msg, version, exc.SADeprecationWarning, stacklevel, code = code)


def warn_deprecated_limited(msg = None, args = None, version = None, stacklevel = (3, None), code = ('msg', 'str', 'args', 'Sequence[Any]', 'version', 'str', 'stacklevel', 'int', 'code', 'Optional[str]', 'return', 'None')):
    '''Issue a deprecation warning with a parameterized string,
    limiting the number of registrations.

    '''
    if args:
        msg = _hash_limit_string(msg, 10, args)
    _warn_with_version(msg, version, exc.SADeprecationWarning, stacklevel, code = code)


def deprecated_cls(version = None, message = None, constructor = None):
    pass
# WARNING: Decompyle incomplete


def deprecated(version = None, message = None, add_deprecation_to_docstring = None, warning = (None, True, None, True), enable_warnings = ('version', 'str', 'message', 'Optional[str]', 'add_deprecation_to_docstring', 'bool', 'warning', 'Optional[Type[exc.SADeprecationWarning]]', 'enable_warnings', 'bool', 'return', 'Callable[[_F], _F]')):
    """Decorates a function and issues a deprecation warning on use.

    :param version:
      Issue version in the warning.

    :param message:
      If provided, issue message in the warning.  A sensible default
      is used if not provided.

    :param add_deprecation_to_docstring:
      Default True.  If False, the wrapped function's __doc__ is left
      as-is.  If True, the 'message' is prepended to the docs if
      provided, or sensible default if message is omitted.

    """
    pass
# WARNING: Decompyle incomplete


def moved_20(message = None, **kw):
    pass
# WARNING: Decompyle incomplete


def became_legacy_20(api_name = None, alternative = None, **kw):
    type_reg = re.match('^:(attr|func|meth):', api_name)
    if type_reg:
        type_ = {
            'attr': 'attribute',
            'func': 'function',
            'meth': 'method' }[type_reg.group(1)]
    else:
        type_ = 'construct'
    message = f'''The {api_name!s} {type_!s} is considered legacy as of the 1.x series of SQLAlchemy and {'becomes a legacy construct'!s} in 2.0.'''
# WARNING: Decompyle incomplete


def deprecated_params(**specs):
    '''Decorates a function to warn on use of certain parameters.

    e.g. ::

        @deprecated_params(
            weak_identity_map=(
                "0.7",
                "the :paramref:`.Session.weak_identity_map parameter "
                "is deprecated.",
            )
        )
        def some_function(**kwargs): ...

    '''
    pass
# WARNING: Decompyle incomplete


def _sanitize_restructured_text(text = None):
    
    def repl(m = None):
        (type_, name) = m.group(1, 2)
        if type_ in ('func', 'meth'):
            name += '()'
        return name

    text = re.sub(':ref:`(.+) <.*>`', (lambda m: '"%s"' % m.group(1)), text)
    return re.sub('\\:(\\w+)\\:`~?(?:_\\w+)?\\.?(.+?)`', repl, text)


def _decorate_cls_with_warning(cls, constructor = None, wtype = None, message = None, version = (None,), docstring_header = ('cls', 'Type[_T]', 'constructor', 'Optional[str]', 'wtype', 'Type[exc.SADeprecationWarning]', 'message', 'str', 'version', 'str', 'docstring_header', 'Optional[str]', 'return', 'Type[_T]')):
    pass
# WARNING: Decompyle incomplete


def _decorate_with_warning(func, wtype = None, message = None, version = None, docstring_header = (None, True), enable_warnings = ('func', '_F', 'wtype', 'Type[exc.SADeprecationWarning]', 'message', 'str', 'version', 'str', 'docstring_header', 'Optional[str]', 'enable_warnings', 'bool', 'return', '_F')):
    '''Wrap a function with a warnings.warn and augmented docstring.'''
    pass
# WARNING: Decompyle incomplete
