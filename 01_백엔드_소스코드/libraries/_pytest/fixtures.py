# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fixtures.pyc (Python 3.11)

from __future__ import annotations
import abc
from collections import defaultdict
from collections import deque
from collections import OrderedDict
from collections.abc import Callable
from collections.abc import Generator
from collections.abc import Iterable
from collections.abc import Iterator
from collections.abc import Mapping
from collections.abc import MutableMapping
from collections.abc import Sequence
from collections.abc import Set as AbstractSet
import dataclasses
import functools
import inspect
import os
from pathlib import Path
import sys
import types
from typing import Any
from typing import cast
from typing import Final
from typing import final
from typing import Generic
from typing import NoReturn
from typing import overload
from typing import TYPE_CHECKING
from typing import TypeVar
import warnings
import _pytest
from _pytest import nodes
from _pytest._code import getfslineno
from _pytest._code import Source
from _pytest._code.code import FormattedExcinfo
from _pytest._code.code import TerminalRepr
from _pytest._io import TerminalWriter
from _pytest.compat import assert_never
from _pytest.compat import get_real_func
from _pytest.compat import getfuncargnames
from _pytest.compat import getimfunc
from _pytest.compat import getlocation
from _pytest.compat import NOTSET
from _pytest.compat import NotSetType
from _pytest.compat import safe_getattr
from _pytest.compat import safe_isclass
from _pytest.compat import signature
from _pytest.config import _PluggyPlugin
from _pytest.config import Config
from _pytest.config import ExitCode
from _pytest.config.argparsing import Parser
from _pytest.deprecated import check_ispytest
from _pytest.deprecated import MARKED_FIXTURE
from _pytest.deprecated import YIELD_FIXTURE
from _pytest.main import Session
from _pytest.mark import Mark
from _pytest.mark import ParameterSet
from _pytest.mark.structures import MarkDecorator
from _pytest.outcomes import fail
from _pytest.outcomes import skip
from _pytest.outcomes import TEST_OUTCOME
from _pytest.pathlib import absolutepath
from _pytest.pathlib import bestrelpath
from _pytest.scope import _ScopeName
from _pytest.scope import HIGH_SCOPES
from _pytest.scope import Scope
from _pytest.warning_types import PytestRemovedIn9Warning
from _pytest.warning_types import PytestWarning
if sys.version_info < (3, 11):
    from exceptiongroup import BaseExceptionGroup
if TYPE_CHECKING:
    from _pytest.python import CallSpec2
    from _pytest.python import Function
    from _pytest.python import Metafunc
FixtureValue = TypeVar('FixtureValue', covariant = True)
FixtureFunction = TypeVar('FixtureFunction', bound = Callable[(..., object)])
_FixtureFunc = Callable[(..., FixtureValue)] | Callable[(..., Generator[FixtureValue])]
_FixtureCachedResult = tuple[(FixtureValue, object, None)] | tuple[(None, object, tuple[(BaseException, types.TracebackType | None)])]

def pytest_sessionstart(session = None):
    session._fixturemanager = FixtureManager(session)


def get_scope_package(node = None, fixturedef = None):
    Package = Package
    import _pytest.python
    for parent in node.iter_parents():
        if isinstance(parent, Package) and parent.nodeid == fixturedef.baseid:
            
            return None, parent
        return node.session


def get_scope_node(node = None, scope = None):
    '''Get the closest parent node (including self) which matches the given
    scope.

    If there is no parent node for the scope (e.g. asking for class scope on a
    Module, or on a Function when not defined in a class), returns None.
    '''
    import _pytest.python as _pytest
    if scope is Scope.Function:
        return node.getparent(nodes.Item)
    if None is Scope.Class:
        return node.getparent(_pytest.python.Class)
    if None is Scope.Module:
        return node.getparent(_pytest.python.Module)
    if None is Scope.Package:
        return node.getparent(_pytest.python.Package)
    if None is Scope.Session:
        return node.getparent(_pytest.main.Session)
    None(scope)


def getfixturemarker(obj = None):
    """Return fixturemarker or None if it doesn't exist"""
    if isinstance(obj, FixtureFunctionDefinition):
        return obj._fixture_function_marker

ParamArgKey = <NODE:12>()
_V = TypeVar('_V')
OrderedSet = dict[(_V, None)]

def get_param_argkeys(item = None, scope = None):
    '''Return all ParamArgKeys for item matching the specified high scope.'''
    pass
# WARNING: Decompyle incomplete


def reorder_items(items = None):
    argkeys_by_item = { }
    items_by_argkey = { }
    for scope in HIGH_SCOPES:
        scoped_argkeys_by_item = { }
        argkeys_by_item[scope] = { }
        scoped_items_by_argkey = defaultdict(OrderedDict)
        items_by_argkey[scope] = defaultdict(OrderedDict)
        for item in items:
            argkeys = dict.fromkeys(get_param_argkeys(item, scope))
            if argkeys:
                scoped_argkeys_by_item[item] = argkeys
                for argkey in argkeys:
                    scoped_items_by_argkey[argkey][item] = None
                    items_set = dict.fromkeys(items)
                    return list(reorder_items_atscope(items_set, argkeys_by_item, items_by_argkey, Scope.Session))


def reorder_items_atscope(items = None, argkeys_by_item = None, items_by_argkey = None, scope = ('items', 'OrderedSet[nodes.Item]', 'argkeys_by_item', 'Mapping[Scope, Mapping[nodes.Item, OrderedSet[ParamArgKey]]]', 'items_by_argkey', 'Mapping[Scope, Mapping[ParamArgKey, OrderedDict[nodes.Item, None]]]', 'scope', 'Scope', 'return', 'OrderedSet[nodes.Item]')):
    pass
# WARNING: Decompyle incomplete

FuncFixtureInfo = <NODE:12>()

class FixtureRequest(abc.ABC):
    '''The type of the ``request`` fixture.

    A request object gives access to the requesting test context and has a
    ``param`` attribute in case the fixture is parametrized.
    '''
    
    def __init__(self = None, pyfuncitem = None, fixturename = None, arg2fixturedefs = None, fixture_defs = {
        '_ispytest': False }, *, _ispytest):
        check_ispytest(_ispytest)
        self.fixturename = fixturename
        self._pyfuncitem = pyfuncitem
        self._arg2fixturedefs = arg2fixturedefs
        self._fixture_defs = fixture_defs
        self

    _fixturemanager = (lambda self = None: self._pyfuncitem.session._fixturemanager)()
    _scope = (lambda self = None: raise NotImplementedError())()()
    scope = (lambda self = None: self._scope.value)()
    _check_scope = (lambda self = None, requested_fixturedef = None, requested_scope = abc.abstractmethod: raise NotImplementedError())()
    fixturenames = (lambda self = None: result = list(self._pyfuncitem.fixturenames)result.extend(set(self._fixture_defs).difference(result))result)()
    node = (lambda self: raise NotImplementedError())()()
    config = (lambda self = property: self._pyfuncitem.config)()
    function = (lambda self: if self.scope != 'function':
raise AttributeError(f'''function not available in {self.scope}-scoped context''')self._pyfuncitem.obj)()
    cls = (lambda self: if self.scope not in ('class', 'function'):
raise AttributeError(f'''cls not available in {self.scope}-scoped context''')clscol = self._pyfuncitem.getparent(_pytest.python.Class)if clscol:
clscol.obj)()
    instance = (lambda self: if self.scope != 'function':
NoneNone(self._pyfuncitem, 'instance', None))()
    module = (lambda self: if self.scope not in ('function', 'class', 'module'):
raise AttributeError(f'''module not available in {self.scope}-scoped context''')mod = self._pyfuncitem.getparent(_pytest.python.Module)# WARNING: Decompyle incomplete
)()
    path = (lambda self = property: if self.scope not in ('function', 'class', 'module', 'package'):
raise AttributeError(f'''path not available in {self.scope}-scoped context''')self._pyfuncitem.path)()
    keywords = (lambda self = property: node = self.nodenode.keywords)()
    session = (lambda self = None: self._pyfuncitem.session)()
    addfinalizer = (lambda self = None, finalizer = None: raise NotImplementedError())()
    
    def applymarker(self = None, marker = None):
        """Apply a marker to a single test function invocation.

        This method is useful if you don't want to have a keyword/marker
        on all function invocations.

        :param marker:
            An object created by a call to ``pytest.mark.NAME(...)``.
        """
        self.node.add_marker(marker)

    
    def raiseerror(self = None, msg = None):
        '''Raise a FixtureLookupError exception.

        :param msg:
            An optional custom error message.
        '''
        raise FixtureLookupError(None, self, msg)

    
    def getfixturevalue(self = None, argname = None):
        """Dynamically run a named fixture function.

        Declaring fixtures via function argument is recommended where possible.
        But if you can only decide whether to use another fixture at test
        setup time, you may use this function to retrieve it inside a fixture
        or test function body.

        This method can be used during the test setup phase or the test run
        phase, but during the test teardown phase a fixture's value may not
        be available.

        :param argname:
            The fixture name.
        :raises pytest.FixtureLookupError:
            If the given fixture could not be found.
        """
        fixturedef = self._get_active_fixturedef(argname)
    # WARNING: Decompyle incomplete

    
    def _iter_chain(self = None):
        '''Yield all SubRequests in the chain, from self up.

        Note: does *not* yield the TopRequest.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_active_fixturedef(self = None, argname = None):
        if argname == 'request':
            return RequestFixtureDef(self)
        fixturedef = None._fixture_defs.get(argname)
    # WARNING: Decompyle incomplete

    
    def _check_fixturedef_without_param(self = None, fixturedef = None):
        '''Check that this request is allowed to execute this fixturedef without
        a param.'''
        funcitem = self._pyfuncitem
        has_params = fixturedef.params is not None
        fixtures_not_supported = getattr(funcitem, 'nofuncargs', False)
        if has_params and fixtures_not_supported:
            msg = f'''{funcitem.name} does not support fixtures, maybe unittest.TestCase subclass?\nNode id: {funcitem.nodeid}\nFunction type: {type(funcitem).__name__}'''
            fail(msg, pytrace = False)
        if has_params:
            frame = inspect.stack()[3]
            frameinfo = inspect.getframeinfo(frame[0])
            source_path = absolutepath(frameinfo.filename)
            source_lineno = frameinfo.lineno
            
            try:
                source_path_str = str(source_path.relative_to(funcitem.config.rootpath))
            except ValueError:
                source_path_str = str(source_path)

            location = getlocation(fixturedef.func, funcitem.config.rootpath)
            msg = f'''The requested fixture has no parameter defined for test:\n    {funcitem.nodeid}\n\nRequested fixture \'{fixturedef.argname}\' defined in:\n{location}\n\nRequested here:\n{source_path_str}:{source_lineno}'''
            fail(msg, pytrace = False)
            return None

    
    def _get_fixturestack(self = None):
        values = self._iter_chain()()
        values.reverse()
        return values


TopRequest = <NODE:12>()
SubRequest = <NODE:12>()
FixtureLookupError = <NODE:12>()

class FixtureLookupErrorRepr(TerminalRepr):
    
    def __init__(self, filename, firstlineno = None, tblines = None, errorstring = None, argname = ('filename', 'str | os.PathLike[str]', 'firstlineno', 'int', 'tblines', 'Sequence[str]', 'errorstring', 'str', 'argname', 'str | None', 'return', 'None')):
        self.tblines = tblines
        self.errorstring = errorstring
        self.filename = filename
        self.firstlineno = firstlineno
        self.argname = argname

    
    def toterminal(self = None, tw = None):
        for tbline in self.tblines:
            tw.line(tbline.rstrip())
            lines = self.errorstring.split('\n')
            if lines:
                tw.line(f'''{FormattedExcinfo.fail_marker}       {lines[0].strip()}''', red = True)
                for line in lines[1:]:
                    tw.line(f'''{FormattedExcinfo.flow_marker}       {line.strip()}''', red = True)
                    tw.line()
                    tw.line(f'''{os.fspath(self.filename)}:{self.firstlineno + 1}''')
                    return None



def call_fixture_func(fixturefunc = final, request = final, kwargs = None):
    pass
# WARNING: Decompyle incomplete


def _teardown_yield_fixture(fixturefunc = dataclasses.dataclass(frozen = True), it = None):
    '''Execute the teardown of a fixture function by advancing the iterator
    after the yield and ensure the iteration ends (if not it means there is
    more than one yield in the function).'''
    
    try:
        next(it)
        (fs, lineno) = getfslineno(fixturefunc)
        fail(f'''fixture function has more than one \'yield\':\n\n{Source(fixturefunc).indent()}\n{fs}:{lineno + 1}''', pytrace = False)
        return None
    except StopIteration:
        return None



def _eval_scope_callable(scope_callable = None, fixture_name = None, config = None):
    
    try:
        result = scope_callable(fixture_name = fixture_name, config = config)
    except Exception:
        e = None
        raise TypeError(f'''Error evaluating {scope_callable} while defining fixture \'{fixture_name}\'.\nExpected a function with the signature (*, fixture_name, config)'''), e
        e = None
        del e

    if not isinstance(result, str):
        fail(f'''Expected {scope_callable} to return a \'str\' while defining fixture \'{fixture_name}\', but it returned:\n{result!r}''', pytrace = False)
    return result


def FixtureDef():
    '''FixtureDef'''
    __doc__ = 'A container for a fixture definition.\n\n    Note: At this time, only explicitly documented fields and methods are\n    considered public stable API.\n    '
    
    def __init__(self, config = None, baseid = None, argname = None, func = None, scope = (None,), params = {
        '_ispytest': False,
        '_autouse': False }, ids = ('config', 'Config', 'baseid', 'str | None', 'argname', 'str', 'func', '_FixtureFunc[FixtureValue]', 'scope', 'Scope | _ScopeName | Callable[[str, Config], _ScopeName] | None', 'params', 'Sequence[object] | None', 'ids', 'tuple[object | None, ...] | Callable[[Any], object | None] | None', '_ispytest', 'bool', '_autouse', 'bool', 'return', 'None'), *, _ispytest, _autouse):
        check_ispytest(_ispytest)
    # WARNING: Decompyle incomplete

    scope = (lambda self = None: self._scope.value)()
    
    def addfinalizer(self = None, finalizer = None):
        self._finalizers.append(finalizer)

    
    def finish(self = None, request = None):
        exceptions = []
    # WARNING: Decompyle incomplete

    
    def execute(self = None, request = None):
        '''Return the value of this fixture, executing it if not cached.'''
        requested_fixtures_that_should_finalize_us = []
    # WARNING: Decompyle incomplete

    
    def cache_key(self = None, request = None):
        return getattr(request, 'param', None)

    
    def __repr__(self = None):
        return f'''<FixtureDef argname={self.argname!r} scope={self.scope!r} baseid={self.baseid!r}>'''


FixtureDef = <NODE:27>(FixtureDef, 'FixtureDef', Generic[FixtureValue])

def RequestFixtureDef():
    '''RequestFixtureDef'''
    pass
# WARNING: Decompyle incomplete

RequestFixtureDef = <NODE:27>(RequestFixtureDef, 'RequestFixtureDef', FixtureDef[FixtureRequest])

def resolve_fixture_function(fixturedef = None, request = None):
    '''Get the actual callable that can be called to obtain the fixture
    value.'''
    fixturefunc = fixturedef.func
    instance = request.instance
# WARNING: Decompyle incomplete


def pytest_fixture_setup(fixturedef = None, request = None):
    '''Execution of fixture setup.'''
    kwargs = { }
    for argname in fixturedef.argnames:
        kwargs[argname] = request.getfixturevalue(argname)
        fixturefunc = resolve_fixture_function(fixturedef, request)
        my_cache_key = fixturedef.cache_key(request)
        if inspect.isasyncgenfunction(fixturefunc) or inspect.iscoroutinefunction(fixturefunc):
            auto_str = ' with autouse=True' if fixturedef._autouse else ''
            warnings.warn(PytestRemovedIn9Warning(f'''{request.node.name!r} requested an async fixture {request.fixturename!r}{auto_str}, with no plugin or hook that handled it. This is usually an error, as pytest does not natively support it. This will turn into an error in pytest 9.\nSee: https://docs.pytest.org/en/stable/deprecations.html#sync-test-depending-on-async-fixture'''), stacklevel = 1)
    
    try:
        result = call_fixture_func(fixturefunc, request, kwargs)
    except TEST_OUTCOME:
        e = None
        if isinstance(e, skip.Exception):
            e._use_item_location = True
        fixturedef.cached_result = (None, my_cache_key, (e, e.__traceback__))
        raise 
        e = None
        del e

    fixturedef.cached_result = (result, my_cache_key, None)
    return result

FixtureFunctionMarker = <NODE:12>()()

class FixtureFunctionDefinition:
    
    def __init__(self = None, *, function, fixture_function_marker, instance, _ispytest):
        check_ispytest(_ispytest)
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''<pytest_fixture({self._fixture_function})>'''

    
    def __get__(self, instance, owner = (None,)):
        '''Behave like a method if the function it was applied to was a method.'''
        return FixtureFunctionDefinition(function = self._fixture_function, fixture_function_marker = self._fixture_function_marker, instance = instance, _ispytest = True)

    
    def __call__(self = None, *args, **kwds):
        message = f'''Fixture "{self.name}" called directly. Fixtures are not meant to be called directly,\nbut are created automatically when test functions request them as parameters.\nSee https://docs.pytest.org/en/stable/explanation/fixtures.html for more information about fixtures, and\nhttps://docs.pytest.org/en/stable/deprecations.html#calling-fixtures-directly'''
        fail(message, pytrace = False)

    
    def _get_wrapped_function(self = None):
        return self._fixture_function


fixture = (lambda fixture_function = final, *, scope: pass)()
fixture = (lambda fixture_function = None, *, scope: pass)()

def fixture(fixture_function = None, *, scope, params, autouse, ids, name):
    '''Decorator to mark a fixture factory function.

    This decorator can be used, with or without parameters, to define a
    fixture function.

    The name of the fixture function can later be referenced to cause its
    invocation ahead of running tests: test modules or classes can use the
    ``pytest.mark.usefixtures(fixturename)`` marker.

    Test functions can directly use fixture names as input arguments in which
    case the fixture instance returned from the fixture function will be
    injected.

    Fixtures can provide their values to test functions using ``return`` or
    ``yield`` statements. When using ``yield`` the code block after the
    ``yield`` statement is executed as teardown code regardless of the test
    outcome, and must yield exactly once.

    :param scope:
        The scope for which this fixture is shared; one of ``"function"``
        (default), ``"class"``, ``"module"``, ``"package"`` or ``"session"``.

        This parameter may also be a callable which receives ``(fixture_name, config)``
        as parameters, and must return a ``str`` with one of the values mentioned above.

        See :ref:`dynamic scope` in the docs for more information.

    :param params:
        An optional list of parameters which will cause multiple invocations
        of the fixture function and all of the tests using it. The current
        parameter is available in ``request.param``.

    :param autouse:
        If True, the fixture func is activated for all tests that can see it.
        If False (the default), an explicit reference is needed to activate
        the fixture.

    :param ids:
        Sequence of ids each corresponding to the params so that they are
        part of the test id. If no ids are provided they will be generated
        automatically from the params.

    :param name:
        The name of the fixture. This defaults to the name of the decorated
        function. If a fixture is used in the same module in which it is
        defined, the function name of the fixture will be shadowed by the
        function arg that requests the fixture; one way to resolve this is to
        name the decorated function ``fixture_<fixturename>`` and then use
        ``@pytest.fixture(name=\'<fixturename>\')``.
    '''
    pass
# WARNING: Decompyle incomplete


def yield_fixture(fixture_function = None, *, scope, params, autouse, ids, name, *args):
    '''(Return a) decorator to mark a yield-fixture factory function.

    .. deprecated:: 3.0
        Use :py:func:`pytest.fixture` directly instead.
    '''
    warnings.warn(YIELD_FIXTURE, stacklevel = 2)
# WARNING: Decompyle incomplete

pytestconfig = (lambda request = None: request.config)()

def pytest_addoption(parser = None):
    parser.addini('usefixtures', type = 'args', default = [], help = 'List of default fixtures to be used with this project')
    group = parser.getgroup('general')
    group.addoption('--fixtures', '--funcargs', action = 'store_true', dest = 'showfixtures', default = False, help = "Show available fixtures, sorted by plugin appearance (fixtures with leading '_' are only shown with '-v')")
    group.addoption('--fixtures-per-test', action = 'store_true', dest = 'show_fixtures_per_test', default = False, help = 'Show fixtures per test')


def pytest_cmdline_main(config = None):
    if config.option.showfixtures:
        showfixtures(config)
        return 0
    if None.option.show_fixtures_per_test:
        show_fixtures_per_test(config)
        return 0


def _get_direct_parametrize_args(node = None):
    """Return all direct parametrization arguments of a node, so we don't
    mistake them for fixtures.

    Check https://github.com/pytest-dev/pytest/issues/5036.

    These things are done later as well when dealing with parametrization
    so this could be improved.
    """
    parametrize_argnames = set()
# WARNING: Decompyle incomplete


def deduplicate_names(*seqs):
    '''De-duplicate the sequence of names while keeping the original order.'''
    return dict.fromkeys((lambda .0: pass# WARNING: Decompyle incomplete
)(seqs()))


class FixtureManager:
    '''pytest fixture definitions and information is stored and managed
    from this class.

    During collection fm.parsefactories() is called multiple times to parse
    fixture function definitions into FixtureDef objects and internal
    data structures.

    During collection of test functions, metafunc-mechanics instantiate
    a FuncFixtureInfo object which is cached per node/func-name.
    This FuncFixtureInfo object is later retrieved by Function nodes
    which themselves offer a fixturenames attribute.

    The FuncFixtureInfo object holds information about fixtures and FixtureDefs
    relevant for a particular function. An initial list of fixtures is
    assembled like this:

    - config-defined usefixtures
    - autouse-marked fixtures along the collection chain up from the function
    - usefixtures markers at module/class/function level
    - test function funcargs

    Subsequently the funcfixtureinfo.fixturenames attribute is computed
    as the closure of the fixtures needed to setup the initial fixtures,
    i.e. fixtures needed by fixture functions themselves are appended
    to the fixturenames list.

    Upon the test-setup phases all fixturenames are instantiated, retrieved
    by a lookup of their FuncFixtureInfo.
    '''
    
    def __init__(self = None, session = None):
        self.session = session
        self.config = session.config
        self._arg2fixturedefs = { }
        self._holderobjseen = set()
        self._nodeid_autousenames = {
            '': self.config.getini('usefixtures') }
        session.config.pluginmanager.register(self, 'funcmanage')

    
    def getfixtureinfo(self = None, node = None, func = None, cls = ('node', 'nodes.Item', 'func', 'Callable[..., object] | None', 'cls', 'type | None', 'return', 'FuncFixtureInfo')):
        """Calculate the :class:`FuncFixtureInfo` for an item.

        If ``func`` is None, or if the item sets an attribute
        ``nofuncargs = True``, then ``func`` is not examined at all.

        :param node:
            The item requesting the fixtures.
        :param func:
            The item's function.
        :param cls:
            If the function is a method, the method's class.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def pytest_plugin_registered(self = None, plugin = None, plugin_name = None):
        if plugin_name and plugin_name.endswith('conftest.py'):
            conftestpath = absolutepath(plugin_name)
            
            try:
                nodeid = str(conftestpath.parent.relative_to(self.config.rootpath))
            except ValueError:
                nodeid = ''

            if nodeid == '.':
                nodeid = ''
            if os.sep != nodes.SEP:
                nodeid = nodeid.replace(os.sep, nodes.SEP)
            else:
                nodeid = None
        self.parsefactories(plugin, nodeid)

    
    def _getautousenames(self = None, node = None):
        '''Return the names of autouse fixtures applicable to node.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _getusefixturesnames(self = None, node = None):
        '''Return the names of usefixtures fixtures applicable to node.'''
        pass
    # WARNING: Decompyle incomplete

    
    def getfixtureclosure(self = None, parentnode = None, initialnames = None, ignore_args = ('parentnode', 'nodes.Node', 'initialnames', 'tuple[str, ...]', 'ignore_args', 'AbstractSet[str]', 'return', 'tuple[list[str], dict[str, Sequence[FixtureDef[Any]]]]')):
        pass
    # WARNING: Decompyle incomplete

    
    def pytest_generate_tests(self = None, metafunc = None):
        '''Generate new tests based on parametrized fixtures used by the given metafunc'''
        pass
    # WARNING: Decompyle incomplete

    
    def pytest_collection_modifyitems(self = None, items = None):
        items[:] = reorder_items(items)

    
    def _register_fixture(self = None, *, name, func, nodeid, scope, params, ids, autouse):
