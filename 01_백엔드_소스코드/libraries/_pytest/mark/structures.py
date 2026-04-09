# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: structures.pyc (Python 3.11)

from __future__ import annotations
import collections.abc as collections
from collections.abc import Callable
from collections.abc import Collection
from collections.abc import Iterable
from collections.abc import Iterator
from collections.abc import Mapping
from collections.abc import MutableMapping
from collections.abc import Sequence
import dataclasses
import enum
import inspect
from typing import Any
from typing import final
from typing import NamedTuple
from typing import overload
from typing import TYPE_CHECKING
from typing import TypeVar
import warnings
from _code import getfslineno
from compat import NOTSET
from compat import NotSetType
from _pytest.config import Config
from _pytest.deprecated import check_ispytest
from _pytest.deprecated import MARKED_FIXTURE
from _pytest.outcomes import fail
from _pytest.raises import AbstractRaises
from _pytest.scope import _ScopeName
from _pytest.warning_types import PytestUnknownMarkWarning
if TYPE_CHECKING:
    from nodes import Node
EMPTY_PARAMETERSET_OPTION = 'empty_parameter_set_mark'

class _HiddenParam(enum.Enum):
    token = 0

HIDDEN_PARAM = _HiddenParam.token

def istestfunc(func = None):
    if callable(func):
        pass
    return getattr(func, '__name__', '<lambda>') != '<lambda>'


def get_empty_parameterset_mark(config = None, argnames = None, func = None):
    Collector = Collector
    import nodes
    argslisting = ', '.join(argnames)
    (_fs, lineno) = getfslineno(func)
    reason = f'''got empty parameter set for ({argslisting})'''
    requested_mark = config.getini(EMPTY_PARAMETERSET_OPTION)
    if requested_mark in ('', None, 'skip'):
        mark = MARK_GEN.skip(reason = reason)
    elif requested_mark == 'xfail':
        mark = MARK_GEN.xfail(reason = reason, run = False)
    elif requested_mark == 'fail_at_collect':
        raise Collector.CollectError(f'''Empty parameter set in \'{func.__name__}\' at line {lineno + 1}''')
    raise LookupError(requested_mark)
    return mark


class ParameterSet(NamedTuple):
    id: 'str | _HiddenParam | None' = 'A set of values for a set of parameters along with associated marks and\n    an optional ID for the set.\n\n    Examples::\n\n        pytest.param(1, 2, 3)\n        # ParameterSet(values=(1, 2, 3), marks=(), id=None)\n\n        pytest.param("hello", id="greeting")\n        # ParameterSet(values=("hello",), marks=(), id="greeting")\n\n        # Parameter set with marks\n        pytest.param(42, marks=pytest.mark.xfail)\n        # ParameterSet(values=(42,), marks=(MarkDecorator(...),), id=None)\n\n        # From parametrize mark (parameter names + list of parameter sets)\n        pytest.mark.parametrize(\n            ("a", "b", "expected"),\n            [\n                (1, 2, 3),\n                pytest.param(40, 2, 42, id="everything"),\n            ],\n        )\n        # ParameterSet(values=(1, 2, 3), marks=(), id=None)\n        # ParameterSet(values=(40, 2, 42), marks=(), id="everything")\n    '
    param = (lambda cls = None, *, marks: if isinstance(marks, MarkDecorator):
marks = (marks,)# WARNING: Decompyle incomplete
)()
    extract_from = (lambda cls = None, parameterset = None, force_tuple = classmethod: if isinstance(parameterset, cls):
parametersetif None:
cls.param(parameterset)cls(parameterset, marks = [], id = None))()
    _parse_parametrize_args = (lambda argnames = None, argvalues = None: (argnames, force_tuple))()
    _parse_parametrize_parameters = (lambda argvalues = None, force_tuple = None: pass# WARNING: Decompyle incomplete
)()
    _for_parametrize = (lambda cls, argnames, argvalues = None, func = None, config = classmethod, nodeid = ('argnames', 'str | Sequence[str]', 'argvalues', 'Iterable[ParameterSet | Sequence[object] | object]', 'config', 'Config', 'nodeid', 'str', 'return', 'tuple[Sequence[str], list[ParameterSet]]'): (argnames, force_tuple) = cls._parse_parametrize_args(argnames, argvalues)parameters = cls._parse_parametrize_parameters(argvalues, force_tuple)del argvaluesif parameters:
for param in parameters:
if len(param.values) != len(argnames):
msg = '{nodeid}: in "parametrize" the number of names ({names_len}):\n  {names}\nmust be equal to the number of values ({values_len}):\n  {values}'fail(msg.format(nodeid = nodeid, values = param.values, names = argnames, names_len = len(argnames), values_len = len(param.values)), pytrace = False)mark = get_empty_parameterset_mark(config, argnames, func)parameters.append(ParameterSet(values = (NOTSET,) * len(argnames), marks = [
mark], id = 'NOTSET'))(argnames, parameters))()

Mark = <NODE:12>()()
Markable = TypeVar('Markable', bound = Callable[(..., object)] | type)
MarkDecorator = <NODE:12>()

def get_unpacked_marks(obj = None, *, consider_mro):
    '''Obtain the unpacked marks that are stored on an object.

    If obj is a class and consider_mro is true, return marks applied to
    this class and all of its super-classes in MRO order. If consider_mro
    is false, only return marks applied directly to this class.
    '''
    if isinstance(obj, type):
        mark_list = []
        for item in mark_lists:
            if isinstance(item, list):
                mark_list.extend(item)
                continue
            mark_list.append(item)
    mark_attribute = getattr(obj, 'pytestmark', [])
    return list(normalize_mark_list(mark_list))


def normalize_mark_list(mark_list = None):
    '''
    Normalize an iterable of Mark or MarkDecorator objects into a list of marks
    by retrieving the `mark` attribute on MarkDecorator instances.

    :param mark_list: marks to normalize
    :returns: A new list of the extracted Mark objects
    '''
    pass
# WARNING: Decompyle incomplete


def store_mark(obj = None, mark = None, *, stacklevel):
    '''Store a Mark on an object.

    This is used to implement the Mark declarations/decorators correctly.
    '''
    pass
# WARNING: Decompyle incomplete

if TYPE_CHECKING:
    
    class _SkipMarkDecorator(MarkDecorator):
        __call__ = (lambda self = None, arg = None: pass)()
        __call__ = (lambda self = None, reason = None: pass)()

    
    class _SkipifMarkDecorator(MarkDecorator):
        
        def __call__(self = None, condition = None, *, reason, *conditions):
            pass


    
    class _XfailMarkDecorator(MarkDecorator):
        __call__ = (lambda self = None, arg = None: pass)()
        __call__ = (lambda self = None, condition = None, *, reason, run: pass)()

    
    class _ParametrizeMarkDecorator(MarkDecorator):
        
        def __call__(self = None, argnames = None, argvalues = None, *, indirect, ids, scope):
            pass


    
    class _UsefixturesMarkDecorator(MarkDecorator):
        
        def __call__(self = None, *fixtures):
            pass


    
    class _FilterwarningsMarkDecorator(MarkDecorator):
        
        def __call__(self = None, *filters):
            pass


MarkGenerator = <NODE:12>()
MARK_GEN = MarkGenerator(_ispytest = True)

def NodeKeywords():
    '''NodeKeywords'''
    __slots__ = ('_markers', 'node', 'parent')
    
    def __init__(self = None, node = None):
        self.node = node
        self.parent = node.parent
        self._markers = {
            node.name: True }

    
    def __getitem__(self = None, key = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __setitem__(self = None, key = None, value = None):
        self._markers[key] = value

    
    def __contains__(self = None, key = None):
