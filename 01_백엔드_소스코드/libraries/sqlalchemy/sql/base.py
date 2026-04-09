# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''Foundational utilities common to many sql modules.'''
from __future__ import annotations
import collections
from enum import Enum
import itertools
from itertools import zip_longest
import operator
import re
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import FrozenSet
from typing import Generator
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import MutableMapping
from typing import NamedTuple
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import roles
from  import visitors
from cache_key import HasCacheKey
from cache_key import MemoizedHasCacheKey
from traversals import HasCopyInternals
from visitors import ClauseVisitor
from visitors import ExtendedInternalTraversal
from visitors import ExternallyTraversible
from visitors import InternalTraversal
from  import event
from  import exc
from  import util
from util import HasMemoized
from util import hybridmethod
from util import typing as compat_typing
from util.typing import Final
from util.typing import Protocol
from util.typing import Self
from util.typing import TypeGuard
if TYPE_CHECKING:
    from  import coercions
    from  import elements
    from  import type_api
    from _orm_types import DMLStrategyArgument
    from _orm_types import SynchronizeSessionArgument
    from _typing import _CLE
    from cache_key import CacheKey
    from compiler import SQLCompiler
    from elements import BindParameter
    from elements import ClauseList
    from elements import ColumnClause
    from elements import ColumnElement
    from elements import NamedColumn
    from elements import SQLCoreOperations
    from elements import TextClause
    from schema import Column
    from schema import DefaultGenerator
    from selectable import _JoinTargetElement
    from selectable import _SelectIterable
    from selectable import FromClause
    from visitors import anon_map
    from engine import Connection
    from engine import CursorResult
    from engine.interfaces import _CoreMultiExecuteParams
    from engine.interfaces import _ExecuteOptions
    from engine.interfaces import _ImmutableExecuteOptions
    from engine.interfaces import CacheStats
    from engine.interfaces import Compiled
    from engine.interfaces import CompiledCacheType
    from engine.interfaces import CoreExecuteOptionsParameter
    from engine.interfaces import Dialect
    from engine.interfaces import IsolationLevel
    from engine.interfaces import SchemaTranslateMapType
    from event import dispatcher
if not TYPE_CHECKING:
    coercions = None
    elements = None
    type_api = None

class _NoArg(Enum):
    NO_ARG = 0
    
    def __repr__(self):
        return f'''_NoArg.{self.name}'''


NO_ARG: 'Final' = _NoArg.NO_ARG

class _NoneName(Enum):
    NONE_NAME = 0

_NONE_NAME: 'Final' = _NoneName.NONE_NAME
_T = TypeVar('_T', bound = Any)
_Fn = TypeVar('_Fn', bound = Callable[(..., Any)])
_AmbiguousTableNameMap = MutableMapping[(str, str)]

class _DefaultDescriptionTuple(NamedTuple):
    is_sentinel: 'Optional[bool]' = '_DefaultDescriptionTuple'
    _from_column_default = (lambda cls = None, default = None: if default:
pass_DefaultDescriptionTuple(default.arg, default.is_scalar, default.is_callable, default.is_sentinel) if (default.has_arg or default.for_update) and default.is_sentinel else _DefaultDescriptionTuple(None, None, None, None))()

_never_select_column: 'operator.attrgetter[Any]' = operator.attrgetter('_omit_from_statements')

class _EntityNamespace(Protocol):
    
    def __getattr__(self = None, key = None):
        pass



class _HasEntityNamespace(Protocol):
    entity_namespace = (lambda self = None: pass)()


def _is_has_entity_namespace(element = None):
    return hasattr(element, 'entity_namespace')

_Self = TypeVar('_Self', bound = Any)

class Immutable:
    '''mark a ClauseElement as \'immutable\' when expressions are cloned.

    "immutable" objects refers to the "mutability" of an object in the
    context of SQL DQL and DML generation.   Such as, in DQL, one can
    compose a SELECT or subquery of varied forms, but one cannot modify
    the structure of a specific table or column within DQL.
    :class:`.Immutable` is mostly intended to follow this concept, and as
    such the primary "immutable" objects are :class:`.ColumnClause`,
    :class:`.Column`, :class:`.TableClause`, :class:`.Table`.

    '''
    __slots__ = ()
    _is_immutable: 'bool' = True
    
    def unique_params(self = None, *optionaldict, **kwargs):
        raise NotImplementedError('Immutable objects do not support copying')

    
    def params(self = None, *optionaldict, **kwargs):
        raise NotImplementedError('Immutable objects do not support copying')

    
    def _clone(self = None, **kw):
        return self

    
    def _copy_internals(self = None, *, omit_attrs, **kw):
        pass



class SingletonConstant(Immutable):
    '''Represent SQL constants like NULL, TRUE, FALSE'''
    _singleton: 'SingletonConstant' = True
    
    def __new__(cls = None, *arg, **kw):
        return cast(_T, cls._singleton)

    proxy_set = (lambda self = None: raise NotImplementedError())()
    _create_singleton = (lambda cls = None: obj = object.__new__(cls)obj.__init__()obj.proxy_set = frozenset([
obj])cls._singleton = obj)()


def _from_objects(*elements):
    return (lambda .0: [ element._from_objects for element in .0 ])(elements())


def _select_iterables(elements = None):
    '''expand tables into individual columns in the
    given list of column expressions.

    '''
    return (lambda .0: [ c._select_iterable for c in .0 ])(elements())

_SelfGenerativeType = TypeVar('_SelfGenerativeType', bound = '_GenerativeType')

class _GenerativeType(compat_typing.Protocol):
    
    def _generate(self = None):
        pass



def _generative(fn = None):
    '''non-caching _generative() decorator.

    This is basically the legacy decorator that copies the object and
    runs a method on the new copy.

    '''
    _generative = (lambda fn = None, self = None: self = self._generate()# WARNING: Decompyle incomplete
)()
    decorated = _generative(fn)
    decorated.non_generative = fn
    return decorated


def _exclusive_against(*names, **kw):
    pass
# WARNING: Decompyle incomplete


def _clone(element, **kw):
    pass
# WARNING: Decompyle incomplete


def _expand_cloned(elements = None):
    """expand the given set of ClauseElements to be the set of all 'cloned'
    predecessors.

    """
    pass
# WARNING: Decompyle incomplete


def _de_clone(elements = None):
    pass
# WARNING: Decompyle incomplete


def _cloned_intersection(a = None, b = None):
    """return the intersection of sets a and b, counting
    any overlap between 'cloned' predecessors.

    The returned set is in terms of the entities present within 'a'.

    """
    pass
# WARNING: Decompyle incomplete


def _cloned_difference(a = None, b = None):
    pass
# WARNING: Decompyle incomplete


def _DialectArgView():
    '''_DialectArgView'''
    __doc__ = 'A dictionary view of dialect-level arguments in the form\n    <dialectname>_<argument_name>.\n\n    '
    __slots__ = ('obj',)
    
    def __init__(self = None, obj = None):
        self.obj = obj

    
    def _key(self = None, key = None):
        
        try:
            (dialect, value_key) = key.split('_', 1)
            return (dialect, value_key)
        except ValueError:
            err = None
            raise KeyError(key), err
            err = None
            del err


    
    def __getitem__(self = None, key = None):
        (dialect, value_key) = self._key(key)
        
        try:
            opt = self.obj.dialect_options[dialect]
            return opt[value_key]
        except exc.NoSuchModuleError:
            err = None
            raise KeyError(key), err
            err = None
            del err


    
    def __setitem__(self = None, key = None, value = None):
        
        try:
            (dialect, value_key) = self._key(key)
            self.obj.dialect_options[dialect][value_key] = value
            return None
        except KeyError:
            err = None
            raise exc.ArgumentError('Keys must be of the form <dialectname>_<argname>'), err
            err = None
            del err


    
    def __delitem__(self = None, key = None):
        (dialect, value_key) = self._key(key)
        del self.obj.dialect_options[dialect][value_key]

    
    def __len__(self = None):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.obj.dialect_options.values()())

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete


_DialectArgView = <NODE:27>(_DialectArgView, '_DialectArgView', MutableMapping[(str, Any)])

def _DialectArgDict():
    '''_DialectArgDict'''
    __doc__ = 'A dictionary view of dialect-level arguments for a specific\n    dialect.\n\n    Maintains a separate collection of user-specified arguments\n    and dialect-specified default arguments.\n\n    '
    
    def __init__(self = None):
        self._non_defaults = { }
        self._defaults = { }

    
    def __len__(self = None):
        return len(set(self._non_defaults).union(self._defaults))

    
    def __iter__(self = None):
        return iter(set(self._non_defaults).union(self._defaults))

    
    def __getitem__(self = None, key = None):
        if key in self._non_defaults:
            return self._non_defaults[key]
        return None._defaults[key]

    
    def __setitem__(self = None, key = None, value = None):
        self._non_defaults[key] = value

    
    def __delitem__(self = None, key = None):
        del self._non_defaults[key]


_DialectArgDict = <NODE:27>(_DialectArgDict, '_DialectArgDict', MutableMapping[(str, Any)])
_kw_reg_for_dialect = (lambda dialect_name = None: dialect_cls = util.preloaded.dialects.registry.load(dialect_name)# WARNING: Decompyle incomplete
)()

class DialectKWArgs:
    '''Establish the ability for a class to have dialect-specific arguments
    with defaults and constructor validation.

    The :class:`.DialectKWArgs` interacts with the
    :attr:`.DefaultDialect.construct_arguments` present on a dialect.

    .. seealso::

        :attr:`.DefaultDialect.construct_arguments`

    '''
    __slots__ = ()
    _dialect_kwargs_traverse_internals: 'List[Tuple[str, Any]]' = [
        ('dialect_options', InternalTraversal.dp_dialect_options)]
    argument_for = (lambda cls = None, dialect_name = None, argument_name = classmethod, default = ('dialect_name', 'str', 'argument_name', 'str', 'default', 'Any', 'return', 'None'): construct_arg_dictionary = DialectKWArgs._kw_registry[dialect_name]# WARNING: Decompyle incomplete
)()
    dialect_kwargs = (lambda self = None: _DialectArgView(self))()
    kwargs = (lambda self = None: self.dialect_kwargs)()
    _kw_registry: 'util.PopulateDict[str, Optional[Dict[Any, Any]]]' = util.PopulateDict(_kw_reg_for_dialect)
    _kw_reg_for_dialect_cls = (lambda cls = None, dialect_name = None: construct_arg_dictionary = DialectKWArgs._kw_registry[dialect_name]d = _DialectArgDict()# WARNING: Decompyle incomplete
)()
    dialect_options = (lambda self = None: util.PopulateDict(self._kw_reg_for_dialect_cls))()
    
    def _validate_dialect_kwargs(self = None, kwargs = None):
        if not kwargs:
            return None
        for k in None:
            m = re.match('^(.+?)_(.+)$', k)
            if not m:
                raise TypeError("Additional arguments should be named <dialectname>_<argument>, got '%s'" % k)
            (dialect_name, arg_name) = m.group(1, 2)
            construct_arg_dictionary = self.dialect_options[dialect_name]
            if '*' not in construct_arg_dictionary and arg_name not in construct_arg_dictionary:
                raise exc.ArgumentError(f'''Argument {k!r} is not accepted by dialect {dialect_name!r} on behalf of {self.__class__!r}''')
            construct_arg_dictionary[arg_name] = kwargs[k]
            except exc.NoSuchModuleError:
                util.warn(f'''Can\'t validate argument {k!r}; can\'t locate any SQLAlchemy dialect named {dialect_name!r}''')
                self.dialect_options[dialect_name] = _DialectArgDict()
                d = _DialectArgDict()
                d._defaults.update({
                    '*': None })
                d._non_defaults[arg_name] = kwargs[k]
                continue
            return None



class CompileState:
    '''Produces additional object state necessary for a statement to be
    compiled.

    the :class:`.CompileState` class is at the base of classes that assemble
    state for a particular statement object that is then used by the
    compiler.   This process is essentially an extension of the process that
    the SQLCompiler.visit_XYZ() method takes, however there is an emphasis
    on converting raw user intent into more organized structures rather than
    producing string output.   The top-level :class:`.CompileState` for the
    statement being executed is also accessible when the execution context
    works with invoking the statement and collecting results.

    The production of :class:`.CompileState` is specific to the compiler,  such
    as within the :meth:`.SQLCompiler.visit_insert`,
    :meth:`.SQLCompiler.visit_select` etc. methods.  These methods are also
    responsible for associating the :class:`.CompileState` with the
    :class:`.SQLCompiler` itself, if the statement is the "toplevel" statement,
    i.e. the outermost SQL statement that\'s actually being executed.
    There can be other :class:`.CompileState` objects that are not the
    toplevel, such as when a SELECT subquery or CTE-nested
    INSERT/UPDATE/DELETE is generated.

    .. versionadded:: 1.4

    '''
    __slots__ = ('statement', '_ambiguous_table_name_map')
    _ambiguous_table_name_map: 'Optional[_AmbiguousTableNameMap]' = { }
    create_for_statement = (lambda cls = None, statement = None, compiler = classmethod: pass# WARNING: Decompyle incomplete
)()
    
    def __init__(self, statement, compiler, **kw):
        self.statement = statement

    get_plugin_class = (lambda cls = None, statement = None: plugin_name = statement._propagate_attrs.get('compile_state_plugin', None)if plugin_name:
key = (plugin_name, statement._effective_plugin_target)if key in cls.plugins:
cls.plugins[key]try:
cls.plugins[('default', statement._effective_plugin_target)]except KeyError:
None)()
    _get_plugin_class_for_plugin = (lambda cls = None, statement = None, plugin_name = classmethod: try:
cls.plugins[(plugin_name, statement._effective_plugin_target)]except KeyError:
None)()
    plugin_for = (lambda cls = None, plugin_name = None, visit_name = classmethod: pass# WARNING: Decompyle incomplete
)()


class Generative(HasMemoized):
    '''Provide a method-chaining pattern in conjunction with the
    @_generative decorator.'''
    
    def _generate(self = None):
        pass
    # WARNING: Decompyle incomplete



class InPlaceGenerative(HasMemoized):
    '''Provide a method-chaining pattern in conjunction with the
    @_generative decorator that mutates in place.'''
    __slots__ = ()
    
    def _generate(self):
        skip = self._memoized_keys
        for k in skip:
            self.__dict__.pop(k, None)
            return self



class HasCompileState(Generative):
    '''A class that has a :class:`.CompileState` associated with it.'''
    _compile_state_plugin: 'Optional[Type[CompileState]]' = None
    _attributes: 'util.immutabledict[str, Any]' = util.EMPTY_DICT
    _compile_state_factory = CompileState.create_for_statement


class _MetaOptions(type):
    _cache_attrs: 'Tuple[str, ...]' = 'metaclass for the Options class.\n\n    This metaclass is actually necessary despite the availability of the\n    ``__init_subclass__()`` hook as this type also provides custom class-level\n    behavior for the ``__add__()`` method.\n\n    '
    
    def __add__(self, other):
        o1 = self()
        if set(other).difference(self._cache_attrs):
            raise TypeError(f'''dictionary contains attributes not covered by Options class {self!s}: {set(other).difference(self._cache_attrs)!r}''')
        o1.__dict__.update(other)
        return o1

    if TYPE_CHECKING:
        
        def __getattr__(self = None, key = None):
            pass

        
        def __setattr__(self = None, key = None, value = None):
            pass

        
        def __delattr__(self = None, key = None):
            pass

        return None


def Options():
    '''Options'''
    pass
# WARNING: Decompyle incomplete

Options = <NODE:27>(Options, 'Options', metaclass = _MetaOptions)

class CacheableOptions(HasCacheKey, Options):
    __slots__ = ()
    _gen_cache_key_inst = (lambda self = None, anon_map = None, bindparams = hybridmethod: HasCacheKey._gen_cache_key(self, anon_map, bindparams))()
    _gen_cache_key = (lambda cls = None, anon_map = None, bindparams = _gen_cache_key_inst.classlevel: (cls, ()))()
    _generate_cache_key = (lambda self = None: HasCacheKey._generate_cache_key_for_object(self))()


class ExecutableOption(HasCopyInternals):
    __slots__ = ()
    _annotations: '_ImmutableExecuteOptions' = util.EMPTY_DICT
    __visit_name__: 'str' = 'executable_option'
    _is_has_cache_key: 'bool' = False
    _is_core: 'bool' = True
    
    def _clone(self, **kw):
        '''Create a shallow copy of this ExecutableOption.'''
        c = self.__class__.__new__(self.__class__)
        c.__dict__ = dict(self.__dict__)
        return c



class Executable(roles.StatementRole):
    '''Mark a :class:`_expression.ClauseElement` as supporting execution.

    :class:`.Executable` is a superclass for all "statement" types
    of objects, including :func:`select`, :func:`delete`, :func:`update`,
    :func:`insert`, :func:`text`.

    '''
    supports_execution: 'bool' = True
    _execution_options: '_ImmutableExecuteOptions' = util.EMPTY_DICT
    _is_default_generator: 'bool' = False
    _with_options: 'Tuple[ExecutableOption, ...]' = ()
    _compile_options: 'Optional[Union[Type[CacheableOptions], CacheableOptions]]' = ()
    _executable_traverse_internals = [
        ('_with_options', InternalTraversal.dp_executable_options),
        ('_with_context_options', ExtendedInternalTraversal.dp_with_context_options),
        ('_propagate_attrs', ExtendedInternalTraversal.dp_propagate_attrs)]
    is_select: 'bool' = False
    is_from_statement: 'bool' = False
    is_update: 'bool' = False
    is_insert: 'bool' = False
    is_text: 'bool' = False
    is_delete: 'bool' = False
    is_dml: 'bool' = False
    if TYPE_CHECKING:
        __visit_name__: 'str'
        
        def _compile_w_cache(self = None, dialect = None, *, compiled_cache, column_keys, for_executemany, schema_translate_map, **kw):
            pass

        
        def _execute_on_connection(self = None, connection = None, distilled_params = None, execution_options = ('connection', 'Connection', 'distilled_params', '_CoreMultiExecuteParams', 'execution_options', 'CoreExecuteOptionsParameter', 'return', 'CursorResult[Any]')):
            pass

        
        def _execute_on_scalar(self = None, connection = None, distilled_params = None, execution_options = ('connection', 'Connection', 'distilled_params', '_CoreMultiExecuteParams', 'execution_options', 'CoreExecuteOptionsParameter', 'return', 'Any')):
            pass

    _all_selected_columns = (lambda self = None: raise NotImplementedError())()
    _effective_plugin_target = (lambda self = None: self.__visit_name__)()
    options = (lambda self = None: self)()
    _set_compile_options = (lambda self = None, compile_options = None: self._compile_options = compile_optionsself)()
    _update_compile_options = (lambda self = None, options = None: pass# WARNING: Decompyle incomplete
)()
    _add_context_option = (lambda self = None, callable_ = None, cache_args = _generative: self)()
    execution_options = (lambda self = None, *, compiled_cache: pass)()
    execution_options = (lambda self = None: pass)()
    execution_options = (lambda self = None: if 'isolation_level' in kw:
raise exc.ArgumentError("'isolation_level' execution option may only be specified on Connection.execution_options(), or per-engine using the isolation_level argument to create_engine().")if 'compiled_cache' in kw:
raise exc.ArgumentError("'compiled_cache' execution option may only be specified on Connection.execution_options(), not per statement.")self._execution_options = self._execution_options.union(kw)self)()
    
    def get_execution_options(self = None):
        '''Get the non-SQL options which will take effect during execution.

        .. versionadded:: 1.3

        .. seealso::

            :meth:`.Executable.execution_options`
        '''
        return self._execution_options



class SchemaEventTarget(event.EventTarget):
    dispatch: 'dispatcher[SchemaEventTarget]' = 'Base class for elements that are the targets of :class:`.DDLEvents`\n    events.\n\n    This includes :class:`.SchemaItem` as well as :class:`.SchemaType`.\n\n    '
    
    def _set_parent(self = None, parent = None, **kw):
        """Associate with this SchemaEvent's parent object."""
        pass

    
    def _set_parent_with_dispatch(self = None, parent = None, **kw):
        self.dispatch.before_parent_attach(self, parent)
    # WARNING: Decompyle incomplete



class SchemaVisitable(visitors.Visitable, SchemaEventTarget):
    '''Base class for elements that are targets of a :class:`.SchemaVisitor`.

    .. versionadded:: 2.0.41

    '''
    pass


class SchemaVisitor(ClauseVisitor):
    '''Define the visiting for ``SchemaItem`` and more
    generally ``SchemaVisitable`` objects.

    '''
    __traverse_options__: 'Dict[str, Any]' = {
        'schema_visitor': True }


class _SentinelDefaultCharacterization(Enum):
    NONE = 'none'
    UNKNOWN = 'unknown'
    CLIENTSIDE = 'clientside'
    SENTINEL_DEFAULT = 'sentinel_default'
    SERVERSIDE = 'serverside'
    IDENTITY = 'identity'
    SEQUENCE = 'sequence'


class _SentinelColumnCharacterization(NamedTuple):
    columns: 'Optional[Sequence[Column[Any]]]' = None
    is_explicit: 'bool' = False
    is_autoinc: 'bool' = False
    default_characterization: '_SentinelDefaultCharacterization' = _SentinelDefaultCharacterization.NONE

_COLKEY = TypeVar('_COLKEY', Union[(None, str)], str)
_COL_co = TypeVar('_COL_co', bound = 'ColumnElement[Any]', covariant = True)
_COL = TypeVar('_COL', bound = 'ColumnElement[Any]')

def _ColumnMetrics():
    '''_ColumnMetrics'''
    column: '_COL_co' = ('column',)
    
    def __init__(self = None, collection = None, col = None):
        self.column = col
        pi = collection._proxy_index
        if pi:
            for eps_col in col._expanded_proxy_set:
                pi[eps_col].add(self)
                return None
                return None

    
    def get_expanded_proxy_set(self = None):
        return self.column._expanded_proxy_set

    
    def dispose(self = None, collection = None):
        pi = collection._proxy_index
        if not pi:
            return None
    # WARNING: Decompyle incomplete

    
    def embedded(self = None, target_set = None):
        expanded_proxy_set = self.column._expanded_proxy_set
        for t in target_set.difference(expanded_proxy_set):
            if not expanded_proxy_set.intersection(_expand_cloned([
                t])):
                return False
            return True


_ColumnMetrics = <NODE:27>(_ColumnMetrics, '_ColumnMetrics', Generic[_COL_co])

def ColumnCollection():
    '''ColumnCollection'''
    __doc__ = 'Collection of :class:`_expression.ColumnElement` instances,\n    typically for\n    :class:`_sql.FromClause` objects.\n\n    The :class:`_sql.ColumnCollection` object is most commonly available\n    as the :attr:`_schema.Table.c` or :attr:`_schema.Table.columns` collection\n    on the :class:`_schema.Table` object, introduced at\n    :ref:`metadata_tables_and_columns`.\n\n    The :class:`_expression.ColumnCollection` has both mapping- and sequence-\n    like behaviors. A :class:`_expression.ColumnCollection` usually stores\n    :class:`_schema.Column` objects, which are then accessible both via mapping\n    style access as well as attribute access style.\n\n    To access :class:`_schema.Column` objects using ordinary attribute-style\n    access, specify the name like any other object attribute, such as below\n    a column named ``employee_name`` is accessed::\n\n        >>> employee_table.c.employee_name\n\n    To access columns that have names with special characters or spaces,\n    index-style access is used, such as below which illustrates a column named\n    ``employee \' payment`` is accessed::\n\n        >>> employee_table.c["employee \' payment"]\n\n    As the :class:`_sql.ColumnCollection` object provides a Python dictionary\n    interface, common dictionary method names like\n    :meth:`_sql.ColumnCollection.keys`, :meth:`_sql.ColumnCollection.values`,\n    and :meth:`_sql.ColumnCollection.items` are available, which means that\n    database columns that are keyed under these names also need to use indexed\n    access::\n\n        >>> employee_table.c["values"]\n\n\n    The name for which a :class:`_schema.Column` would be present is normally\n    that of the :paramref:`_schema.Column.key` parameter.  In some contexts,\n    such as a :class:`_sql.Select` object that uses a label style set\n    using the :meth:`_sql.Select.set_label_style` method, a column of a certain\n    key may instead be represented under a particular label name such\n    as ``tablename_columnname``::\n\n        >>> from sqlalchemy import select, column, table\n        >>> from sqlalchemy import LABEL_STYLE_TABLENAME_PLUS_COL\n        >>> t = table("t", column("c"))\n        >>> stmt = select(t).set_label_style(LABEL_STYLE_TABLENAME_PLUS_COL)\n        >>> subq = stmt.subquery()\n        >>> subq.c.t_c\n        <sqlalchemy.sql.elements.ColumnClause at 0x7f59dcf04fa0; t_c>\n\n    :class:`.ColumnCollection` also indexes the columns in order and allows\n    them to be accessible by their integer position::\n\n        >>> cc[0]\n        Column(\'x\', Integer(), table=None)\n        >>> cc[1]\n        Column(\'y\', Integer(), table=None)\n\n    .. versionadded:: 1.4 :class:`_expression.ColumnCollection`\n       allows integer-based\n       index access to the collection.\n\n    Iterating the collection yields the column expressions in order::\n\n        >>> list(cc)\n        [Column(\'x\', Integer(), table=None),\n         Column(\'y\', Integer(), table=None)]\n\n    The base :class:`_expression.ColumnCollection` object can store\n    duplicates, which can\n    mean either two columns with the same key, in which case the column\n    returned by key  access is **arbitrary**::\n\n        >>> x1, x2 = Column("x", Integer), Column("x", Integer)\n        >>> cc = ColumnCollection(columns=[(x1.name, x1), (x2.name, x2)])\n        >>> list(cc)\n        [Column(\'x\', Integer(), table=None),\n         Column(\'x\', Integer(), table=None)]\n        >>> cc["x"] is x1\n        False\n        >>> cc["x"] is x2\n        True\n\n    Or it can also mean the same column multiple times.   These cases are\n    supported as :class:`_expression.ColumnCollection`\n    is used to represent the columns in\n    a SELECT statement which may include duplicates.\n\n    A special subclass :class:`.DedupeColumnCollection` exists which instead\n    maintains SQLAlchemy\'s older behavior of not allowing duplicates; this\n    collection is used for schema level objects like :class:`_schema.Table`\n    and\n    :class:`.PrimaryKeyConstraint` where this deduping is helpful.  The\n    :class:`.DedupeColumnCollection` class also has additional mutation methods\n    as the schema constructs have more use cases that require removal and\n    replacement of columns.\n\n    .. versionchanged:: 1.4 :class:`_expression.ColumnCollection`\n       now stores duplicate\n       column keys as well as the same column in multiple positions.  The\n       :class:`.DedupeColumnCollection` class is added to maintain the\n       former behavior in those cases where deduplication as well as\n       additional replace/remove operations are needed.\n\n\n    '
    _colset: 'Set[_COL_co]' = ('_collection', '_index', '_colset', '_proxy_index')
    
    def __init__(self = None, columns = None):
        object.__setattr__(self, '_colset', set())
        object.__setattr__(self, '_index', { })
        object.__setattr__(self, '_proxy_index', collections.defaultdict(util.OrderedSet))
        object.__setattr__(self, '_collection', [])
        if columns:
            self._initial_populate(columns)
            return None

    __clause_element__ = (lambda self = None: elements = util.preloaded.sql_elements# WARNING: Decompyle incomplete
)()
    
    def _initial_populate(self = None, iter_ = None):
        self._populate_separate_keys(iter_)

    _all_columns = (lambda self = None: self._collection())()
    
    def keys(self = None):
        '''Return a sequence of string key names for all columns in this
        collection.'''
        return self._collection()

    
    def values(self = None):
        '''Return a sequence of :class:`_sql.ColumnClause` or
        :class:`_schema.Column` objects for all columns in this
        collection.'''
        return self._collection()

    
    def items(self = None):
        '''Return a sequence of (key, column) tuples for all columns in this
        collection each consisting of a string key name and a
        :class:`_sql.ColumnClause` or
        :class:`_schema.Column` object.
        '''
        return self._collection()

    
    def __bool__(self = None):
        return bool(self._collection)

    
    def __len__(self = None):
        return len(self._collection)

    
    def __iter__(self = None):
        return (lambda .0: [ col for _, col, _ in .0 ])(self._collection())

    __getitem__ = (lambda self = None, key = None: pass)()
    __getitem__ = (lambda self = None, key = None: pass)()
    __getitem__ = (lambda self = None, key = None: pass)()
    
    def __getitem__(self = None, key = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __getattr__(self = None, key = None):
        
        try:
            return self._index[key][1]
        except KeyError:
            err = None
            raise AttributeError(key), err
            err = None
            del err


    
    def __contains__(self = None, key = None):
        if key not in self._index:
            if not isinstance(key, str):
                raise exc.ArgumentError('__contains__ requires a string argument')
            return False

    
    def compare(self = None, other = None):
        '''Compare this :class:`_expression.ColumnCollection` to another
        based on the names of the keys'''
        for l, r in zip_longest(self, other):
            if l is not r:
                return False
            return True

    
    def __eq__(self = None, other = None):
        return self.compare(other)

    get = (lambda self = None, key = None, default = overload: pass)()
    get = (lambda self = None, key = None, default = overload: pass)()
    
    def get(self = None, key = None, default = None):
        '''Get a :class:`_sql.ColumnClause` or :class:`_schema.Column` object
        based on a string key name from this
        :class:`_expression.ColumnCollection`.'''
        if key in self._index:
            return self._index[key][1]

    
    def __str__(self = None):
        return f'''({(lambda .0: pass# WARNING: Decompyle incomplete
)(self())!s})'''

    
    def __setitem__(self = None, key = None, value = None):
        raise NotImplementedError()

    
    def __delitem__(self = None, key = None):
        raise NotImplementedError()

    
    def __setattr__(self = None, key = None, obj = None):
        raise NotImplementedError()

    
    def clear(self = None):
        '''Dictionary clear() is not implemented for
        :class:`_sql.ColumnCollection`.'''
        raise NotImplementedError()

    
    def remove(self = None, column = None):
        raise NotImplementedError()

    
    def update(self = None, iter_ = None):
        '''Dictionary update() is not implemented for
        :class:`_sql.ColumnCollection`.'''
        raise NotImplementedError()

    __hash__: 'Optional[int]' = None
    
    def _populate_separate_keys(self = None, iter_ = None):
        '''populate from an iterator of (key, column)'''
        pass
    # WARNING: Decompyle incomplete

    
    def add(self = None, column = None, key = None):
        '''Add a column to this :class:`_sql.ColumnCollection`.

        .. note::

            This method is **not normally used by user-facing code**, as the
            :class:`_sql.ColumnCollection` is usually part of an existing
            object such as a :class:`_schema.Table`. To add a
            :class:`_schema.Column` to an existing :class:`_schema.Table`
            object, use the :meth:`_schema.Table.append_column` method.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __getstate__(self = None):
        return {
            '_collection': self._collection(),
            '_index': self._index }

    
    def __setstate__(self = None, state = None):
        pass
    # WARNING: Decompyle incomplete

    
    def contains_column(self = None, col = None):
        '''Checks if a column object exists in this collection'''
        if col not in self._colset:
            if isinstance(col, str):
                raise exc.ArgumentError('contains_column cannot be used with string arguments. Use ``col_name in table.c`` instead.')
            return False

    
    def as_readonly(self = None):
        '''Return a "read only" form of this
        :class:`_sql.ColumnCollection`.'''
        return ReadOnlyColumnCollection(self)

    
    def _init_proxy_index(self = None):
        '''populate the "proxy index", if empty.

        proxy index is added in 2.0 to provide more efficient operation
        for the corresponding_column() method.

        For reasons of both time to construct new .c collections as well as
        memory conservation for large numbers of large .c collections, the
        proxy_index is only filled if corresponding_column() is called. once
        filled it stays that way, and new _ColumnMetrics objects created after
        that point will populate it with new data. Note this case would be
        unusual, if not nonexistent, as it means a .c collection is being
        mutated after corresponding_column() were used, however it is tested in
        test/base/test_utils.py.

        '''
        pi = self._proxy_index
        if pi:
            return None
        for _, _, metrics in None._collection:
            eps = metrics.column._expanded_proxy_set
            for eps_col in eps:
                pi[eps_col].add(metrics)
                return None

    
    def corresponding_column(self = None, column = None, require_embedded = None):
        '''Given a :class:`_expression.ColumnElement`, return the exported
        :class:`_expression.ColumnElement` object from this
        :class:`_expression.ColumnCollection`
        which corresponds to that original :class:`_expression.ColumnElement`
        via a common
        ancestor column.

        :param column: the target :class:`_expression.ColumnElement`
                      to be matched.

        :param require_embedded: only return corresponding columns for
         the given :class:`_expression.ColumnElement`, if the given
         :class:`_expression.ColumnElement`
         is actually present within a sub-element
         of this :class:`_expression.Selectable`.
         Normally the column will match if
         it merely shares a common ancestor with one of the exported
         columns of this :class:`_expression.Selectable`.

        .. seealso::

            :meth:`_expression.Selectable.corresponding_column`
            - invokes this method
            against the collection returned by
            :attr:`_expression.Selectable.exported_columns`.

        .. versionchanged:: 1.4 the implementation for ``corresponding_column``
           was moved onto the :class:`_expression.ColumnCollection` itself.

        '''
        pass
    # WARNING: Decompyle incomplete


ColumnCollection = <NODE:27>(ColumnCollection, 'ColumnCollection', Generic[(_COLKEY, _COL_co)])
_NAMEDCOL = TypeVar('_NAMEDCOL', bound = 'NamedColumn[Any]')

def DedupeColumnCollection():
    '''DedupeColumnCollection'''
    __doc__ = 'A :class:`_expression.ColumnCollection`\n    that maintains deduplicating behavior.\n\n    This is useful by schema level objects such as :class:`_schema.Table` and\n    :class:`.PrimaryKeyConstraint`.    The collection includes more\n    sophisticated mutator methods as well to suit schema objects which\n    require mutable column collections.\n\n    .. versionadded:: 1.4\n\n    '
    
    def add(self = None, column = None, key = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _append_new_column(self = None, key = None, named_column = None):
        l = len(self._collection)
        self._collection.append((key, named_column, _ColumnMetrics(self, named_column)))
        self._colset.add(named_column._deannotate())
        self._index[l] = (key, named_column)
        self._index[key] = (key, named_column)

    
    def _populate_separate_keys(self = None, iter_ = None):
        '''populate from an iterator of (key, column)'''
        cols = list(iter_)
        replace_col = []
        for k, col in cols:
            if col.key != k:
                raise exc.ArgumentError('DedupeColumnCollection requires columns be under the same key as their .key')
            if col.name in self._index and col.key != col.name:
                replace_col.append(col)
                continue
            if col.key in self._index:
                replace_col.append(col)
                continue
            self._index[k] = (k, col)
            self._collection.append((k, col, _ColumnMetrics(self, col)))
            (lambda .0: pass# WARNING: Decompyle incomplete
)(self._collection())
            (lambda .0: pass# WARNING: Decompyle incomplete
)(enumerate(self._collection)())
            for col in replace_col:
                self.replace(col)
                return None

    
    def extend(self = None, iter_ = None):
        (lambda .0: pass# WARNING: Decompyle incomplete
)(iter_())

    
    def remove(self = None, column = None):
        pass
    # WARNING: Decompyle incomplete

    
    def replace(self = None, column = None, extra_remove = None):
        '''add the given column to this collection, removing unaliased
        versions of this column  as well as existing columns with the
        same key.

        e.g.::

            t = Table("sometable", metadata, Column("col1", Integer))
            t.columns.replace(Column("col1", Integer, key="columnone"))

        will remove the original \'col1\' from the collection, and add
        the new column under the name \'columnname\'.

        Used by schema.Column to override columns during table reflection.

        '''
        if extra_remove:
            remove_col = set(extra_remove)
        else:
            remove_col = set()
        if column.name in self._index and column.key != column.name:
            other = self._index[column.name][1]
            if other.name == other.key:
                remove_col.add(other)
        if column.key in self._index:
            remove_col.add(self._index[column.key][1])
        if not remove_col:
            self._append_new_column(column.key, column)
            return None
        new_cols = None
        replaced = False
        for k, col, metrics in self._collection:
            if col in remove_col:
                if not replaced:
                    replaced = True
                    new_cols.append((column.key, column, _ColumnMetrics(self, column)))
                continue
            new_cols.append((k, col, metrics))
            if remove_col:
                self._colset.difference_update(remove_col)
                for rc in remove_col:
                    for metrics in self._proxy_index.get(rc, ()):
                        metrics.dispose(self)
                        if not replaced:
                            new_cols.append((column.key, column, _ColumnMetrics(self, column)))
        self._colset.add(column._deannotate())
        self._collection[:] = new_cols
        self._index.clear()
        (lambda .0: pass# WARNING: Decompyle incomplete
)(enumerate(self._collection)())
        (lambda .0: pass# WARNING: Decompyle incomplete
)(self._collection())


DedupeColumnCollection = <NODE:27>(DedupeColumnCollection, 'DedupeColumnCollection', ColumnCollection[(str, _NAMEDCOL)])

def ReadOnlyColumnCollection():
    '''ReadOnlyColumnCollection'''
    __slots__ = ('_parent',)
    
    def __init__(self = None, collection = None):
        object.__setattr__(self, '_parent', collection)
        object.__setattr__(self, '_colset', collection._colset)
        object.__setattr__(self, '_index', collection._index)
        object.__setattr__(self, '_collection', collection._collection)
        object.__setattr__(self, '_proxy_index', collection._proxy_index)

    
    def __getstate__(self = None):
        return {
            '_parent': self._parent }

    
    def __setstate__(self = None, state = None):
        parent = state['_parent']
        self.__init__(parent)

    
    def add(self = None, column = None, key = None):
        self._readonly()

    
    def extend(self = None, elements = None):
        self._readonly()

    
    def remove(self = None, item = None):
        self._readonly()


ReadOnlyColumnCollection = <NODE:27>(ReadOnlyColumnCollection, 'ReadOnlyColumnCollection', util.ReadOnlyContainer, ColumnCollection[(_COLKEY, _COL_co)])

def ColumnSet():
    '''ColumnSet'''
    
    def contains_column(self = None, col = None):
        return col in self

    
    def extend(self = None, cols = None):
        for col in cols:
            self.add(col)
            return None

    
    def __eq__(self, other):
        l = []
    # WARNING: Decompyle incomplete

    
    def __hash__(self = None):
        return tuple((lambda .0: pass# WARNING: Decompyle incomplete
)(self()))


ColumnSet = <NODE:27>(ColumnSet, 'ColumnSet', util.OrderedSet['ColumnClause[Any]'])

def _entity_namespace(entity = None):
    '''Return the nearest .entity_namespace for the given entity.

    If not immediately available, does an iterate to find a sub-element
    that has one, if any.

    '''
    
    try:
        return cast(_HasEntityNamespace, entity).entity_namespace
    except AttributeError:
        for elem in visitors.iterate(cast(ExternallyTraversible, entity)):
            if _is_has_entity_namespace(elem):
                
                return 
            raise 



def _entity_namespace_key(entity = None, key = None, default = None):
    '''Return an entry from an entity_namespace.


    Raises :class:`_exc.InvalidRequestError` rather than attribute error
    on not found.

    '''
    
    try:
        ns = _entity_namespace(entity)
        if default is not NO_ARG:
            return getattr(ns, key, default)
        return None(ns, key)
    except AttributeError:
        err = None
        raise exc.InvalidRequestError(f'''Entity namespace for "{entity!s}" has no property "{key!s}"'''), err
        err = None
        del err
