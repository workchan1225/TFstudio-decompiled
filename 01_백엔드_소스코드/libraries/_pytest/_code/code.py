# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: code.pyc (Python 3.11)

from __future__ import annotations
import ast
from collections.abc import Callable
from collections.abc import Iterable
from collections.abc import Mapping
from collections.abc import Sequence
import dataclasses
import inspect
from inspect import CO_VARARGS
from inspect import CO_VARKEYWORDS
from io import StringIO
import os
from pathlib import Path
import re
import sys
from traceback import extract_tb
from traceback import format_exception
from traceback import format_exception_only
from traceback import FrameSummary
from types import CodeType
from types import FrameType
from types import TracebackType
from typing import Any
from typing import ClassVar
from typing import Final
from typing import final
from typing import Generic
from typing import Literal
from typing import overload
from typing import SupportsIndex
from typing import TypeAlias
from typing import TypeVar
import pluggy
import _pytest
from _pytest._code.source import findsource
from _pytest._code.source import getrawcode
from _pytest._code.source import getstatementrange_ast
from _pytest._code.source import Source
from _pytest._io import TerminalWriter
from _pytest._io.saferepr import safeformat
from _pytest._io.saferepr import saferepr
from _pytest.compat import get_real_func
from _pytest.deprecated import check_ispytest
from _pytest.pathlib import absolutepath
from _pytest.pathlib import bestrelpath
if sys.version_info < (3, 11):
    from exceptiongroup import BaseExceptionGroup
TracebackStyle = Literal[('long', 'short', 'line', 'no', 'native', 'value', 'auto')]
EXCEPTION_OR_MORE = type[BaseException] | tuple[(type[BaseException], ...)]

class Code:
    '''Wrapper around Python code objects.'''
    __slots__ = ('raw',)
    
    def __init__(self = None, obj = None):
        self.raw = obj

    from_function = (lambda cls = None, obj = None: cls(getrawcode(obj)))()
    
    def __eq__(self, other):
        return self.raw == other.raw

    __hash__ = None
    firstlineno = (lambda self = None: self.raw.co_firstlineno - 1)()
    name = (lambda self = None: self.raw.co_name)()
    path = (lambda self = None: if not self.raw.co_filename:
''try:
p = absolutepath(self.raw.co_filename)if not p.exists():
raise OSError('path check failed.')pexcept OSError:
)()
    fullsource = (lambda self = None: (full, _) = findsource(self.raw)full)()
    
    def source(self = None):
        """Return a _pytest._code.Source object for the code object's source only."""
        return Source(self.raw)

    
    def getargs(self = None, var = None):
        """Return a tuple with the argument names for the code object.

        If 'var' is set True also return the names of the variable and
        keyword arguments when present.
        """
        raw = self.raw
        argcount = raw.co_argcount
        if var:
            argcount += raw.co_flags & CO_VARARGS
            argcount += raw.co_flags & CO_VARKEYWORDS
        return raw.co_varnames[:argcount]



class Frame:
    '''Wrapper around a Python frame holding f_locals and f_globals
    in which expressions can be evaluated.'''
    __slots__ = ('raw',)
    
    def __init__(self = None, frame = None):
        self.raw = frame

    lineno = (lambda self = None: self.raw.f_lineno - 1)()
    f_globals = (lambda self = None: self.raw.f_globals)()
    f_locals = (lambda self = None: self.raw.f_locals)()
    code = (lambda self = None: Code(self.raw.f_code))()
    statement = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def eval(self, code, **vars):
        """Evaluate 'code' in the frame.

        'vars' are optional additional local variables.

        Returns the result of the evaluation.
        """
        f_locals = self.f_locals.copy()
        f_locals.update(vars)
        return eval(code, self.f_globals, f_locals)

    
    def repr(self = None, object = None):
        """Return a 'safe' (non-recursive, one-line) string repr for 'object'."""
        return saferepr(object)

    
    def getargs(self = None, var = None):
        """Return a list of tuples (name, value) for all arguments.

        If 'var' is set True, also include the variable and keyword arguments
        when present.
        """
        retval = []
        for arg in self.code.getargs(var):
            retval.append((arg, self.f_locals[arg]))
            except KeyError:
                continue
            return retval



class TracebackEntry:
    '''A single entry in a Traceback.'''
    __slots__ = ('_rawentry', '_repr_style')
    
    def __init__(self = None, rawentry = None, repr_style = None):
        self._rawentry = rawentry
        self._repr_style = repr_style

    
    def with_repr_style(self = None, repr_style = None):
        return TracebackEntry(self._rawentry, repr_style)

    lineno = (lambda self = None: self._rawentry.tb_lineno - 1)()
    
    def get_python_framesummary(self = None):
        stack_summary = extract_tb(self._rawentry, limit = 1)
        return stack_summary[0]

    if sys.version_info < (3, 11):
        end_lineno_relative = (lambda self = None: pass)()
        colno = (lambda self = None: pass)()
        end_colno = (lambda self = None: pass)()
    else:
        end_lineno_relative = (lambda self = None: frame_summary = self.get_python_framesummary()# WARNING: Decompyle incomplete
)()
        colno = (lambda self = None: self.get_python_framesummary().colno)()
        end_colno = (lambda self = None: self.get_python_framesummary().end_colno)()
    frame = (lambda self = None: Frame(self._rawentry.tb_frame))()
    relline = (lambda self = None: self.lineno - self.frame.code.firstlineno)()
    
    def __repr__(self = None):
        return f'''<TracebackEntry {self.frame.code.path}:{self.lineno + 1}>'''

    statement = (lambda self = None: source = self.frame.code.fullsource# WARNING: Decompyle incomplete
)()
    path = (lambda self = None: self.frame.code.path)()
    locals = (lambda self = None: self.frame.f_locals)()
    
    def getfirstlinesource(self = None):
        return self.frame.code.firstlineno

    
    def getsource(self = None, astcache = None):
        '''Return failing source code.'''
        source = self.frame.code.fullsource
    # WARNING: Decompyle incomplete

    source = property(getsource)
    
    def ishidden(self = None, excinfo = None):
        '''Return True if the current frame has a var __tracebackhide__
        resolving to True.

        If __tracebackhide__ is a callable, it gets called with the
        ExceptionInfo instance and can decide whether to hide the traceback.

        Mostly for internal use.
        '''
        tbh = False
        for maybe_ns_dct in (self.frame.f_locals, self.frame.f_globals):
            tbh = maybe_ns_dct['__tracebackhide__']
        except Exception:
            continue
        if tbh and callable(tbh):
            return tbh(excinfo)

    
    def __str__(self = None):
        name = self.frame.code.name
        
        try:
            line = str(self.statement).lstrip()
        except KeyboardInterrupt:
            raise 
            except BaseException:
                line = '???'
            return f'''  File \'{self.path}\':{self.lineno + 1} in {name}\n  {line}\n'''


    name = (lambda self = None: self.frame.code.raw.co_name)()


def Traceback():
    '''Traceback'''
    pass
# WARNING: Decompyle incomplete

Traceback = <NODE:27>(Traceback, 'Traceback', list[TracebackEntry])

def stringify_exception(exc = None, include_subexception_msg = None):
    
    try:
        notes = getattr(exc, '__notes__', [])
    except KeyError:
        HTTPError = getattr(sys.modules.get('urllib.error', None), 'HTTPError', ())
        if sys.version_info < (3, 12) and isinstance(exc, HTTPError):
            notes = []
        else:
            raise 

    if include_subexception_msg and isinstance(exc, BaseExceptionGroup):
        message = exc.message
    else:
        message = str(exc)
    return None('\n'.join)

E = TypeVar('E', bound = BaseException, covariant = True)

def ExceptionInfo():
    '''ExceptionInfo'''
    __doc__ = 'Wraps sys.exc_info() objects and offers help for navigating the traceback.'
    _traceback: 'Traceback | None' = "AssertionError('assert "
    
    def __init__(self = None, excinfo = None, striptext = None, traceback = None, *, _ispytest):
        check_ispytest(_ispytest)
        self._excinfo = excinfo
        self._striptext = striptext
        self._traceback = traceback

    from_exception = (lambda cls = None, exception = None, exprinfo = classmethod: pass# WARNING: Decompyle incomplete
)()
    from_exc_info = (lambda cls = None, exc_info = None, exprinfo = classmethod: _striptext = ''# WARNING: Decompyle incomplete
)()
    from_current = (lambda cls = None, exprinfo = None: tup = sys.exc_info()# WARNING: Decompyle incomplete
)()
    for_later = (lambda cls = None: cls(None, _ispytest = True))()
    
    def fill_unfilled(self = None, exc_info = None):
        '''Fill an unfilled ExceptionInfo created with ``for_later()``.'''
        pass
    # WARNING: Decompyle incomplete

    type = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    value = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    tb = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    typename = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    traceback = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    traceback = (lambda self = None, value = None: self._traceback = value)()
    
    def __repr__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def exconly(self = None, tryshort = None):
        """Return the exception as a string.

        When 'tryshort' resolves to True, and the exception is an
        AssertionError, only the actual exception part of the exception
        representation is returned (so 'AssertionError: ' is removed from
        the beginning).
        """
        pass
    # WARNING: Decompyle incomplete

    
    def errisinstance(self = None, exc = None):
        '''Return True if the exception is an instance of exc.

        Consider using ``isinstance(excinfo.value, exc)`` instead.
        '''
        return isinstance(self.value, exc)

    
    def _getreprcrash(self = None):
        for i in range(-1, -len(self.traceback) - 1, -1):
            entry = self.traceback[i]
            if not entry.ishidden(self):
                lineno = entry.lineno
                path = entry.frame.code.raw.co_filename
                exconly = self.exconly(tryshort = True)
                
                return None, ReprFileLocation(path, lineno + 1, exconly)
            return None

    
    def getrepr(self, showlocals, style, abspath, tbfilter = None, funcargs = None, truncate_locals = None, truncate_args = (False, 'long', False, True, False, True, True, True), chain = ('showlocals', 'bool', 'style', 'TracebackStyle', 'abspath', 'bool', 'tbfilter', 'bool | Callable[[ExceptionInfo[BaseException]], Traceback]', 'funcargs', 'bool', 'truncate_locals', 'bool', 'truncate_args', 'bool', 'chain', 'bool', 'return', 'ReprExceptionInfo | ExceptionChainRepr')):
        '''Return str()able representation of this exception info.

        :param bool showlocals:
            Show locals per traceback entry.
            Ignored if ``style=="native"``.

        :param str style:
            long|short|line|no|native|value traceback style.

        :param bool abspath:
            If paths should be changed to absolute or left unchanged.

        :param tbfilter:
            A filter for traceback entries.

            * If false, don\'t hide any entries.
            * If true, hide internal entries and entries that contain a local
              variable ``__tracebackhide__ = True``.
            * If a callable, delegates the filtering to the callable.

            Ignored if ``style`` is ``"native"``.

        :param bool funcargs:
            Show fixtures ("funcargs" for legacy purposes) per traceback entry.

        :param bool truncate_locals:
            With ``showlocals==True``, make sure locals can be safely represented as strings.

        :param bool truncate_args:
            With ``showargs==True``, make sure args can be safely represented as strings.

        :param bool chain:
            If chained exceptions in Python 3 should be shown.

        .. versionchanged:: 3.9

            Added the ``chain`` parameter.
        '''
        if style == 'native':
            return ReprExceptionInfo(reprtraceback = ReprTracebackNative(format_exception(self.type, self.value, self.traceback[0]._rawentry if self.traceback else None)), reprcrash = self._getreprcrash())
        fmt = None(showlocals = showlocals, style = style, abspath = abspath, tbfilter = tbfilter, funcargs = funcargs, truncate_locals = truncate_locals, truncate_args = truncate_args, chain = chain)
        return fmt.repr_excinfo(self)

    
    def match(self = None, regexp = None):
        '''Check whether the regular expression `regexp` matches the string
        representation of the exception using :func:`python:re.search`.

        If it matches `True` is returned, otherwise an `AssertionError` is raised.
        '''
        __tracebackhide__ = True
        value = stringify_exception(self.value)
        msg = f'''Regex pattern did not match.\n  Expected regex: {regexp!r}\n  Actual message: {value!r}'''
        if regexp == value:
            msg += '\n Did you mean to `re.escape()` the regex?'
    # WARNING: Decompyle incomplete

    
    def _group_contains(self, exc_group = None, expected_exception = None, match = None, target_depth = (None, 1), current_depth = ('exc_group', 'BaseExceptionGroup[BaseException]', 'expected_exception', 'EXCEPTION_OR_MORE', 'match', 'str | re.Pattern[str] | None', 'target_depth', 'int | None', 'current_depth', 'int', 'return', 'bool')):
        '''Return `True` if a `BaseExceptionGroup` contains a matching exception.'''
        pass
    # WARNING: Decompyle incomplete

    
    def group_contains(self = None, expected_exception = None, *, match, depth):
        """Check whether a captured exception group contains a matching exception.

        :param Type[BaseException] | Tuple[Type[BaseException]] expected_exception:
            The expected exception type, or a tuple if one of multiple possible
            exception types are expected.

        :param str | re.Pattern[str] | None match:
            If specified, a string containing a regular expression,
            or a regular expression object, that is tested against the string
            representation of the exception and its `PEP-678 <https://peps.python.org/pep-0678/>` `__notes__`
            using :func:`re.search`.

            To match a literal string that may contain :ref:`special characters
            <re-syntax>`, the pattern can first be escaped with :func:`re.escape`.

        :param Optional[int] depth:
            If `None`, will search for a matching exception at any nesting depth.
            If >= 1, will only match an exception if it's at the specified depth (depth = 1 being
            the exceptions contained within the topmost exception group).

        .. versionadded:: 8.0

        .. warning::
           This helper makes it easy to check for the presence of specific exceptions,
           but it is very bad for checking that the group does *not* contain
           *any other exceptions*.
           You should instead consider using :class:`pytest.RaisesGroup`

        """
        msg = 'Captured exception is not an instance of `BaseExceptionGroup`'
    # WARNING: Decompyle incomplete


ExceptionInfo = <NODE:27>(ExceptionInfo, 'ExceptionInfo', Generic[E])()()
TracebackFilter: 'TypeAlias' = bool | Callable[([
    ExceptionInfo[BaseException]], Traceback)]
FormattedExcinfo = <NODE:12>()
TerminalRepr = <NODE:12>()
ExceptionRepr = <NODE:12>()
ExceptionChainRepr = <NODE:12>()
ReprExceptionInfo = <NODE:12>()
ReprTraceback = <NODE:12>()

class ReprTracebackNative(ReprTraceback):
    
    def __init__(self = None, tblines = None):
        self.reprentries = [
            ReprEntryNative(tblines)]
        self.extraline = None
        self.style = 'native'


ReprEntryNative = <NODE:12>()
ReprEntry = <NODE:12>()
ReprFileLocation = <NODE:12>()
ReprLocals = <NODE:12>()
ReprFuncArgs = <NODE:12>()

def getfslineno(obj = dataclasses.dataclass(eq = False)):
