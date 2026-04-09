# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: result.pyc (Python 3.11)

'''Define generic result set constructs.'''
from __future__ import annotations
from enum import Enum
import functools
import itertools
import operator
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from row import Row
from row import RowMapping
from  import exc
from  import util
from sql.base import _generative
from sql.base import HasMemoized
from sql.base import InPlaceGenerative
from util import HasMemoized_ro_memoized_attribute
from util import NONE_SET
from util._has_cy import HAS_CYEXTENSION
from util.typing import Literal
from util.typing import Self
if not typing.TYPE_CHECKING or HAS_CYEXTENSION:
    from _py_row import tuplegetter
else:
    from sqlalchemy.cyextension.resultproxy import tuplegetter
if typing.TYPE_CHECKING:
    from sql.elements import SQLCoreOperations
    from sql.type_api import _ResultProcessorType
_KeyType = Union[(str, 'SQLCoreOperations[Any]')]
_KeyIndexType = Union[(_KeyType, int)]
_KeyMapRecType = Any
_KeyMapType = Mapping[(_KeyType, _KeyMapRecType)]
_RowData = Union[(Row[Any], RowMapping, Any)]
_RawRowType = Tuple[(Any, ...)]
_R = TypeVar('_R', bound = _RowData)
_T = TypeVar('_T', bound = Any)
_TP = TypeVar('_TP', bound = Tuple[(Any, ...)])
_InterimRowType = Union[(_R, _RawRowType)]
_InterimSupportsScalarsRowType = Union[(Row[Any], Any)]
_ProcessorsType = Sequence[Optional['_ResultProcessorType[Any]']]
_TupleGetterType = Callable[([
    Sequence[Any]], Sequence[Any])]
_UniqueFilterType = Callable[([
    Any], Any)]
_UniqueFilterStateType = Tuple[(Set[Any], Optional[_UniqueFilterType])]

class ResultMetaData:
    '''Base for metadata about result rows.'''
    __slots__ = ()
    _tuplefilter: 'Optional[_TupleGetterType]' = None
    _translated_indexes: 'Optional[Sequence[int]]' = None
    _key_to_index: 'Mapping[_KeyType, int]' = None
    keys = (lambda self = None: RMKeyView(self))()
    
    def _has_key(self = None, key = None):
        raise NotImplementedError()

    
    def _for_freeze(self = None):
        raise NotImplementedError()

    _key_fallback = (lambda self = None, key = None, err = overload, raiseerr = (...,): pass)()
    _key_fallback = (lambda self = None, key = None, err = overload, raiseerr = (...,): pass)()
    _key_fallback = (lambda self = None, key = None, err = overload, raiseerr = (...,): pass)()
    
    def _key_fallback(self = None, key = None, err = None, raiseerr = (True,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _raise_for_ambiguous_column_name(self = None, rec = None):
        raise NotImplementedError('ambiguous column name logic is implemented for CursorResultMetaData')

    
    def _index_for_key(self = None, key = None, raiseerr = None):
        raise NotImplementedError()

    
    def _indexes_for_keys(self = None, keys = None):
        raise NotImplementedError()

    
    def _metadata_for_keys(self = None, keys = None):
        raise NotImplementedError()

    
    def _reduce(self = None, keys = None):
        raise NotImplementedError()

    
    def _getter(self = None, key = None, raiseerr = None):
        index = self._index_for_key(key, raiseerr)
    # WARNING: Decompyle incomplete

    
    def _row_as_tuple_getter(self = None, keys = None):
        indexes = self._indexes_for_keys(keys)
    # WARNING: Decompyle incomplete

    
    def _make_key_to_index(self = None, keymap = None, index = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _key_not_found(self = None, key = None, attr_error = None):
        if key in self._keymap:
            self._raise_for_ambiguous_column_name(self._keymap[key])
            return None
        if None:
            
            try:
                self._key_fallback(key, None)
                return None
            except KeyError:
                ke = None
                raise AttributeError(ke.args[0]), ke
                ke = None
                del ke
                self._key_fallback(key, None)
                return None


    _effective_processors = (lambda self = None: if self._processors or NONE_SET.issuperset(self._processors):
NoneNone._processors)()


def RMKeyView():
    '''RMKeyView'''
    _keys: 'Sequence[str]' = ('_parent', '_keys')
    
    def __init__(self = None, parent = None):
        self._parent = parent
        self._keys = parent._keys()

    
    def __len__(self = None):
        return len(self._keys)

    
    def __repr__(self = None):
        return '{0.__class__.__name__}({0._keys!r})'.format(self)

    
    def __iter__(self = None):
        return iter(self._keys)

    
    def __contains__(self = None, item = None):
        if isinstance(item, int):
            return False
        return None._parent._has_key(item)

    
    def __eq__(self = None, other = None):
        return list(other) == list(self)

    
    def __ne__(self = None, other = None):
        return list(other) != list(self)


RMKeyView = <NODE:27>(RMKeyView, 'RMKeyView', typing.KeysView[Any])

class SimpleResultMetaData(ResultMetaData):
    '''result metadata for in-memory collections.'''
    _keys: 'Sequence[str]' = ('_keys', '_keymap', '_processors', '_tuplefilter', '_translated_indexes', '_unique_filters', '_key_to_index')
    
    def __init__(self, keys, extra = None, _processors = None, _tuplefilter = None, _translated_indexes = (None, None, None, None, None), _unique_filters = ('keys', 'Sequence[str]', 'extra', 'Optional[Sequence[Any]]', '_processors', 'Optional[_ProcessorsType]', '_tuplefilter', 'Optional[_TupleGetterType]', '_translated_indexes', 'Optional[Sequence[int]]', '_unique_filters', 'Optional[Sequence[Callable[[Any], Any]]]')):
        self._keys = list(keys)
        self._tuplefilter = _tuplefilter
        self._translated_indexes = _translated_indexes
        self._unique_filters = _unique_filters
        self._keymap = recs_names()
        self._processors = _processors
        self._key_to_index = self._make_key_to_index(self._keymap, 0)

    
    def _has_key(self = None, key = None):
        return key in self._keymap

    
    def _for_freeze(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __getstate__(self = None):
        return {
            '_keys': self._keys,
            '_translated_indexes': self._translated_indexes }

    
    def __setstate__(self = None, state = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _index_for_key(self = None, key = None, raiseerr = None):
        if int in key.__class__.__mro__:
            key = self._keys[key]
        
        try:
            rec = self._keymap[key]
        except KeyError:
            ke = None
            rec = self._key_fallback(key, ke, raiseerr)
            ke = None
            del ke
        except:
            ke = None
            del ke

        return rec[0]

    
    def _indexes_for_keys(self = None, keys = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _metadata_for_keys(self = None, keys = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _reduce(self = None, keys = None):
        pass
    # WARNING: Decompyle incomplete



def result_tuple(fields = None, extra = None):
    parent = SimpleResultMetaData(fields, extra)
    return functools.partial(Row, parent, parent._effective_processors, parent._key_to_index)


class _NoRow(Enum):
    _NO_ROW = 0

_NO_ROW = _NoRow._NO_ROW

def ResultInternal():
    '''ResultInternal'''
    __slots__ = ()
    _real_result: 'Optional[Result[Any]]' = None
    _row_logging_fn: 'Optional[Callable[[Any], Any]]' = True
    _unique_filter_state: 'Optional[_UniqueFilterStateType]' = None
    _post_creational_filter: 'Optional[Callable[[Any], Any]]' = None
    _source_supports_scalars: 'bool' = False
    
    def _fetchiter_impl(self = None):
        raise NotImplementedError()

    
    def _fetchone_impl(self = None, hard_close = None):
        raise NotImplementedError()

    
    def _fetchmany_impl(self = None, size = None):
        raise NotImplementedError()

    
    def _fetchall_impl(self = None):
        raise NotImplementedError()

    
    def _soft_close(self = None, hard = None):
        raise NotImplementedError()

    _row_getter = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    _iterator_getter = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def _raw_all_rows(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _allrows(self = None):
        pass
    # WARNING: Decompyle incomplete

    _onerow_getter = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    _manyrow_getter = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    _only_one_row = (lambda self = None, raise_for_second_row = None, raise_for_none = overload, scalar = ('self', 'ResultInternal[Row[Any]]', 'raise_for_second_row', 'bool', 'raise_for_none', 'bool', 'scalar', 'Literal[True]', 'return', 'Any'): pass)()
    _only_one_row = (lambda self = None, raise_for_second_row = None, raise_for_none = overload, scalar = ('raise_for_second_row', 'bool', 'raise_for_none', 'Literal[True]', 'scalar', 'bool', 'return', '_R'): pass)()
    _only_one_row = (lambda self = None, raise_for_second_row = None, raise_for_none = overload, scalar = ('raise_for_second_row', 'bool', 'raise_for_none', 'bool', 'scalar', 'bool', 'return', 'Optional[_R]'): pass)()
    
    def _only_one_row(self = None, raise_for_second_row = None, raise_for_none = None, scalar = ('raise_for_second_row', 'bool', 'raise_for_none', 'bool', 'scalar', 'bool', 'return', 'Optional[_R]')):
        onerow = self._fetchone_impl
        row = onerow(hard_close = True)
    # WARNING: Decompyle incomplete

    
    def _iter_impl(self = None):
        return self._iterator_getter(self)

    
    def _next_impl(self = None):
        row = self._onerow_getter(self)
        if row is _NO_ROW:
            raise StopIteration()
        return row

    _column_slices = (lambda self = None, indexes = None: real_result = self._real_result if self._real_result else cast('Result[Any]', self)if real_result._source_supports_scalars or len(indexes) != 1:
self._metadata = self._metadata._reduce(indexes)# WARNING: Decompyle incomplete
)()
    _unique_strategy = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

ResultInternal = <NODE:27>(ResultInternal, 'ResultInternal', InPlaceGenerative, Generic[_R])

class _WithKeys:
    _metadata: 'ResultMetaData' = ()
    
    def keys(self = None):
        '''Return an iterable view which yields the string keys that would
        be represented by each :class:`_engine.Row`.

        The keys can represent the labels of the columns returned by a core
        statement or the names of the orm classes returned by an orm
        execution.

        The view also can be tested for key containment using the Python
        ``in`` operator, which will test both for the string keys represented
        in the view, as well as for alternate keys such as column objects.

        .. versionchanged:: 1.4 a key view object is returned rather than a
           plain list.


        '''
        return self._metadata.keys



def Result():
    '''Result'''
    __doc__ = 'Represent a set of database results.\n\n    .. versionadded:: 1.4  The :class:`_engine.Result` object provides a\n       completely updated usage model and calling facade for SQLAlchemy\n       Core and SQLAlchemy ORM.   In Core, it forms the basis of the\n       :class:`_engine.CursorResult` object which replaces the previous\n       :class:`_engine.ResultProxy` interface.   When using the ORM, a\n       higher level object called :class:`_engine.ChunkedIteratorResult`\n       is normally used.\n\n    .. note:: In SQLAlchemy 1.4 and above, this object is\n       used for ORM results returned by :meth:`_orm.Session.execute`, which can\n       yield instances of ORM mapped objects either individually or within\n       tuple-like rows. Note that the :class:`_engine.Result` object does not\n       deduplicate instances or rows automatically as is the case with the\n       legacy :class:`_orm.Query` object. For in-Python de-duplication of\n       instances or rows, use the :meth:`_engine.Result.unique` modifier\n       method.\n\n    .. seealso::\n\n        :ref:`tutorial_fetching_rows` - in the :doc:`/tutorial/index`\n\n    '
    __slots__ = ('_metadata', '__dict__')
    _row_logging_fn: 'Optional[Callable[[Row[Any]], Row[Any]]]' = None
    _source_supports_scalars: 'bool' = False
    _yield_per: 'Optional[int]' = None
    _attributes: 'util.immutabledict[Any, Any]' = util.immutabledict()
    
    def __init__(self = None, cursor_metadata = None):
        self._metadata = cursor_metadata

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, type_ = None, value = None, traceback = ('type_', 'Any', 'value', 'Any', 'traceback', 'Any', 'return', 'None')):
        self.close()

    
    def close(self = None):
        '''close this :class:`_engine.Result`.

        The behavior of this method is implementation specific, and is
        not implemented by default.    The method should generally end
        the resources in use by the result object and also cause any
        subsequent iteration or row fetching to raise
        :class:`.ResourceClosedError`.

        .. versionadded:: 1.4.27 - ``.close()`` was previously not generally
           available for all :class:`_engine.Result` classes, instead only
           being available on the :class:`_engine.CursorResult` returned for
           Core statement executions. As most other result objects, namely the
           ones used by the ORM, are proxying a :class:`_engine.CursorResult`
           in any case, this allows the underlying cursor result to be closed
           from the outside facade for the case when the ORM query is using
           the ``yield_per`` execution option where it does not immediately
           exhaust and autoclose the database cursor.

        '''
        self._soft_close(hard = True)

    _soft_closed = (lambda self = None: raise NotImplementedError())()
    closed = (lambda self = None: raise NotImplementedError())()
    yield_per = (lambda self = None, num = None: self._yield_per = numself)()
    unique = (lambda self = None, strategy = None: self._unique_filter_state = (set(), strategy)self)()
    
    def columns(self = None, *col_expressions):
        '''Establish the columns that should be returned in each row.

        This method may be used to limit the columns returned as well
        as to reorder them.   The given list of expressions are normally
        a series of integers or string key names.   They may also be
        appropriate :class:`.ColumnElement` objects which correspond to
        a given statement construct.

        .. versionchanged:: 2.0  Due to a bug in 1.4, the
           :meth:`_engine.Result.columns` method had an incorrect behavior
           where calling upon the method with just one index would cause the
           :class:`_engine.Result` object to yield scalar values rather than
           :class:`_engine.Row` objects.   In version 2.0, this behavior
           has been corrected such that calling upon
           :meth:`_engine.Result.columns` with a single index will
           produce a :class:`_engine.Result` object that continues
           to yield :class:`_engine.Row` objects, which include
           only a single column.

        E.g.::

            statement = select(table.c.x, table.c.y, table.c.z)
            result = connection.execute(statement)

            for z, y in result.columns("z", "y"):
                ...

        Example of using the column objects from the statement itself::

            for z, y in result.columns(
                statement.selected_columns.c.z, statement.selected_columns.c.y
            ):
                ...

        .. versionadded:: 1.4

        :param \\*col_expressions: indicates columns to be returned.  Elements
         may be integer row indexes, string column names, or appropriate
         :class:`.ColumnElement` objects corresponding to a select construct.

        :return: this :class:`_engine.Result` object with the modifications
         given.

        '''
        return self._column_slices(col_expressions)

    scalars = (lambda self = None: pass)()
    scalars = (lambda self = None, index = None: pass)()
    scalars = (lambda self = None, index = None: pass)()
    
    def scalars(self = None, index = None):
        '''Return a :class:`_engine.ScalarResult` filtering object which
        will return single elements rather than :class:`_row.Row` objects.

        E.g.::

            >>> result = conn.execute(text("select int_id from table"))
            >>> result.scalars().all()
            [1, 2, 3]

        When results are fetched from the :class:`_engine.ScalarResult`
        filtering object, the single column-row that would be returned by the
        :class:`_engine.Result` is instead returned as the column\'s value.

        .. versionadded:: 1.4

        :param index: integer or row key indicating the column to be fetched
         from each row, defaults to ``0`` indicating the first column.

        :return: a new :class:`_engine.ScalarResult` filtering object referring
         to this :class:`_engine.Result` object.

        '''
        return ScalarResult(self, index)

    
    def _getter(self = None, key = None, raiseerr = None):
        '''return a callable that will retrieve the given key from a
        :class:`_engine.Row`.

        '''
        if self._source_supports_scalars:
            raise NotImplementedError("can't use this function in 'only scalars' mode")
        return self._metadata._getter(key, raiseerr)

    
    def _tuple_getter(self = None, keys = None):
        '''return a callable that will retrieve the given keys from a
        :class:`_engine.Row`.

        '''
        if self._source_supports_scalars:
            raise NotImplementedError("can't use this function in 'only scalars' mode")
        return self._metadata._row_as_tuple_getter(keys)

    
    def mappings(self = None):
        '''Apply a mappings filter to returned rows, returning an instance of
        :class:`_engine.MappingResult`.

        When this filter is applied, fetching rows will return
        :class:`_engine.RowMapping` objects instead of :class:`_engine.Row`
        objects.

        .. versionadded:: 1.4

        :return: a new :class:`_engine.MappingResult` filtering object
         referring to this :class:`_engine.Result` object.

        '''
        return MappingResult(self)

    t = (lambda self = None: self)()
    
    def tuples(self = None):
        '''Apply a "typed tuple" typing filter to returned rows.

        This method returns the same :class:`_engine.Result` object
        at runtime,
        however annotates as returning a :class:`_engine.TupleResult` object
        that will indicate to :pep:`484` typing tools that plain typed
        ``Tuple`` instances are returned rather than rows.  This allows
        tuple unpacking and ``__getitem__`` access of :class:`_engine.Row`
        objects to by typed, for those cases where the statement invoked
        itself included typing information.

        .. versionadded:: 2.0

        :return: the :class:`_engine.TupleResult` type at typing time.

        .. seealso::

            :attr:`_engine.Result.t` - shorter synonym

            :attr:`_engine.Row._t` - :class:`_engine.Row` version

        '''
        return self

    
    def _raw_row_iterator(self = None):
        '''Return a safe iterator that yields raw row data.

        This is used by the :meth:`_engine.Result.merge` method
        to merge multiple compatible results together.

        '''
        raise NotImplementedError()

    
    def __iter__(self = None):
        return self._iter_impl()

    
    def __next__(self = None):
        return self._next_impl()

    
    def partitions(self = None, size = None):
        """Iterate through sub-lists of rows of the size given.

        Each list will be of the size given, excluding the last list to
        be yielded, which may have a small number of rows.  No empty
        lists will be yielded.

        The result object is automatically closed when the iterator
        is fully consumed.

        Note that the backend driver will usually buffer the entire result
        ahead of time unless the
        :paramref:`.Connection.execution_options.stream_results` execution
        option is used indicating that the driver should not pre-buffer
        results, if possible.   Not all drivers support this option and
        the option is silently ignored for those who do not.

        When using the ORM, the :meth:`_engine.Result.partitions` method
        is typically more effective from a memory perspective when it is
        combined with use of the
        :ref:`yield_per execution option <orm_queryguide_yield_per>`,
        which instructs both the DBAPI driver to use server side cursors,
        if available, as well as instructs the ORM loading internals to only
        build a certain amount of ORM objects from a result at a time before
        yielding them out.

        .. versionadded:: 1.4

        :param size: indicate the maximum number of rows to be present
         in each list yielded.  If None, makes use of the value set by
         the :meth:`_engine.Result.yield_per`, method, if it were called,
         or the :paramref:`_engine.Connection.execution_options.yield_per`
         execution option, which is equivalent in this regard.  If
         yield_per weren't set, it makes use of the
         :meth:`_engine.Result.fetchmany` default, which may be backend
         specific and not well defined.

        :return: iterator of lists

        .. seealso::

            :ref:`engine_stream_results`

            :ref:`orm_queryguide_yield_per` - in the :ref:`queryguide_toplevel`

        """
        pass
    # WARNING: Decompyle incomplete

    
    def fetchall(self = None):
        '''A synonym for the :meth:`_engine.Result.all` method.'''
        return self._allrows()

    
    def fetchone(self = None):
        '''Fetch one row.

        When all rows are exhausted, returns None.

        This method is provided for backwards compatibility with
        SQLAlchemy 1.x.x.

        To fetch the first row of a result only, use the
        :meth:`_engine.Result.first` method.  To iterate through all
        rows, iterate the :class:`_engine.Result` object directly.

        :return: a :class:`_engine.Row` object if no filters are applied,
         or ``None`` if no rows remain.

        '''
        row = self._onerow_getter(self)
        if row is _NO_ROW:
            return None

    
    def fetchmany(self = None, size = None):
        '''Fetch many rows.

        When all rows are exhausted, returns an empty sequence.

        This method is provided for backwards compatibility with
        SQLAlchemy 1.x.x.

        To fetch rows in groups, use the :meth:`_engine.Result.partitions`
        method.

        :return: a sequence of :class:`_engine.Row` objects.

        .. seealso::

            :meth:`_engine.Result.partitions`

        '''
        return self._manyrow_getter(self, size)

    
    def all(self = None):
        '''Return all rows in a sequence.

        Closes the result set after invocation.   Subsequent invocations
        will return an empty sequence.

        .. versionadded:: 1.4

        :return: a sequence of :class:`_engine.Row` objects.

        .. seealso::

            :ref:`engine_stream_results` - How to stream a large result set
            without loading it completely in python.

        '''
        return self._allrows()

    
    def first(self = None):
        '''Fetch the first row or ``None`` if no row is present.

        Closes the result set and discards remaining rows.

        .. note::  This method returns one **row**, e.g. tuple, by default.
           To return exactly one single scalar value, that is, the first
           column of the first row, use the
           :meth:`_engine.Result.scalar` method,
           or combine :meth:`_engine.Result.scalars` and
           :meth:`_engine.Result.first`.

           Additionally, in contrast to the behavior of the legacy  ORM
           :meth:`_orm.Query.first` method, **no limit is applied** to the
           SQL query which was invoked to produce this
           :class:`_engine.Result`;
           for a DBAPI driver that buffers results in memory before yielding
           rows, all rows will be sent to the Python process and all but
           the first row will be discarded.

           .. seealso::

                :ref:`migration_20_unify_select`

        :return: a :class:`_engine.Row` object, or None
         if no rows remain.

        .. seealso::

            :meth:`_engine.Result.scalar`

            :meth:`_engine.Result.one`

        '''
        return self._only_one_row(raise_for_second_row = False, raise_for_none = False, scalar = False)

    
    def one_or_none(self = None):
        '''Return at most one result or raise an exception.

        Returns ``None`` if the result has no rows.
        Raises :class:`.MultipleResultsFound`
        if multiple rows are returned.

        .. versionadded:: 1.4

        :return: The first :class:`_engine.Row` or ``None`` if no row
         is available.

        :raises: :class:`.MultipleResultsFound`

        .. seealso::

            :meth:`_engine.Result.first`

            :meth:`_engine.Result.one`

        '''
        return self._only_one_row(raise_for_second_row = True, raise_for_none = False, scalar = False)

    scalar_one = (lambda self = None: pass)()
    scalar_one = (lambda self = None: pass)()
    
    def scalar_one(self = None):
        '''Return exactly one scalar result or raise an exception.

        This is equivalent to calling :meth:`_engine.Result.scalars` and
        then :meth:`_engine.ScalarResult.one`.

        .. seealso::

            :meth:`_engine.ScalarResult.one`

            :meth:`_engine.Result.scalars`

        '''
        return self._only_one_row(raise_for_second_row = True, raise_for_none = True, scalar = True)

    scalar_one_or_none = (lambda self = None: pass)()
    scalar_one_or_none = (lambda self = None: pass)()
    
    def scalar_one_or_none(self = None):
        '''Return exactly one scalar result or ``None``.

        This is equivalent to calling :meth:`_engine.Result.scalars` and
        then :meth:`_engine.ScalarResult.one_or_none`.

        .. seealso::

            :meth:`_engine.ScalarResult.one_or_none`

            :meth:`_engine.Result.scalars`

        '''
        return self._only_one_row(raise_for_second_row = True, raise_for_none = False, scalar = True)

    
    def one(self = None):
        '''Return exactly one row or raise an exception.

        Raises :class:`_exc.NoResultFound` if the result returns no
        rows, or :class:`_exc.MultipleResultsFound` if multiple rows
        would be returned.

        .. note::  This method returns one **row**, e.g. tuple, by default.
           To return exactly one single scalar value, that is, the first
           column of the first row, use the
           :meth:`_engine.Result.scalar_one` method, or combine
           :meth:`_engine.Result.scalars` and
           :meth:`_engine.Result.one`.

        .. versionadded:: 1.4

        :return: The first :class:`_engine.Row`.

        :raises: :class:`.MultipleResultsFound`, :class:`.NoResultFound`

        .. seealso::

            :meth:`_engine.Result.first`

            :meth:`_engine.Result.one_or_none`

            :meth:`_engine.Result.scalar_one`

        '''
        return self._only_one_row(raise_for_second_row = True, raise_for_none = True, scalar = False)

    scalar = (lambda self = None: pass)()
    scalar = (lambda self = None: pass)()
    
    def scalar(self = None):
        '''Fetch the first column of the first row, and close the result set.

        Returns ``None`` if there are no rows to fetch.

        No validation is performed to test if additional rows remain.

        After calling this method, the object is fully closed,
        e.g. the :meth:`_engine.CursorResult.close`
        method will have been called.

        :return: a Python scalar value, or ``None`` if no rows remain.

        '''
        return self._only_one_row(raise_for_second_row = False, raise_for_none = False, scalar = True)

    
    def freeze(self = None):
        '''Return a callable object that will produce copies of this
        :class:`_engine.Result` when invoked.

        The callable object returned is an instance of
        :class:`_engine.FrozenResult`.

        This is used for result set caching.  The method must be called
        on the result when it has been unconsumed, and calling the method
        will consume the result fully.   When the :class:`_engine.FrozenResult`
        is retrieved from a cache, it can be called any number of times where
        it will produce a new :class:`_engine.Result` object each time
        against its stored set of rows.

        .. seealso::

            :ref:`do_orm_execute_re_executing` - example usage within the
            ORM to implement a result-set cache.

        '''
        return FrozenResult(self)

    
    def merge(self = None, *others):
        '''Merge this :class:`_engine.Result` with other compatible result
        objects.

        The object returned is an instance of :class:`_engine.MergedResult`,
        which will be composed of iterators from the given result
        objects.

        The new result will use the metadata from this result object.
        The subsequent result objects must be against an identical
        set of result / cursor metadata, otherwise the behavior is
        undefined.

        '''
        return MergedResult(self._metadata, (self,) + others)


Result = <NODE:27>(Result, 'Result', _WithKeys, ResultInternal[Row[_TP]])

def FilterResult():
    '''FilterResult'''
    __doc__ = 'A wrapper for a :class:`_engine.Result` that returns objects other than\n    :class:`_engine.Row` objects, such as dictionaries or scalar objects.\n\n    :class:`_engine.FilterResult` is the common base for additional result\n    APIs including :class:`_engine.MappingResult`,\n    :class:`_engine.ScalarResult` and :class:`_engine.AsyncResult`.\n\n    '
    _real_result: 'Result[Any]' = ('_real_result', '_post_creational_filter', '_metadata', '_unique_filter_state', '__dict__')
    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, type_ = None, value = None, traceback = ('type_', 'Any', 'value', 'Any', 'traceback', 'Any', 'return', 'None')):
        self._real_result.__exit__(type_, value, traceback)

    yield_per = (lambda self = None, num = None: self._real_result = self._real_result.yield_per(num)self)()
    
    def _soft_close(self = None, hard = None):
        self._real_result._soft_close(hard = hard)

    _soft_closed = (lambda self = None: self._real_result._soft_closed)()
    closed = (lambda self = None: self._real_result.closed)()
    
    def close(self = None):
        '''Close this :class:`_engine.FilterResult`.

        .. versionadded:: 1.4.43

        '''
        self._real_result.close()

    _attributes = (lambda self = None: self._real_result._attributes)()
    
    def _fetchiter_impl(self = None):
        return self._real_result._fetchiter_impl()

    
    def _fetchone_impl(self = None, hard_close = None):
        return self._real_result._fetchone_impl(hard_close = hard_close)

    
    def _fetchall_impl(self = None):
        return self._real_result._fetchall_impl()

    
    def _fetchmany_impl(self = None, size = None):
        return self._real_result._fetchmany_impl(size = size)


FilterResult = <NODE:27>(FilterResult, 'FilterResult', ResultInternal[_R])

def ScalarResult():
    '''ScalarResult'''
    __doc__ = 'A wrapper for a :class:`_engine.Result` that returns scalar values\n    rather than :class:`_row.Row` values.\n\n    The :class:`_engine.ScalarResult` object is acquired by calling the\n    :meth:`_engine.Result.scalars` method.\n\n    A special limitation of :class:`_engine.ScalarResult` is that it has\n    no ``fetchone()`` method; since the semantics of ``fetchone()`` are that\n    the ``None`` value indicates no more results, this is not compatible\n    with :class:`_engine.ScalarResult` since there is no way to distinguish\n    between ``None`` as a row value versus ``None`` as an indicator.  Use\n    ``next(result)`` to receive values individually.\n\n    '
    __slots__ = ()
    _post_creational_filter: 'Optional[Callable[[Any], Any]]' = False
    
    def __init__(self = None, real_result = None, index = None):
        self._real_result = real_result
        if real_result._source_supports_scalars:
            self._metadata = real_result._metadata
            self._post_creational_filter = None
        else:
            self._metadata = real_result._metadata._reduce([
                index])
            self._post_creational_filter = operator.itemgetter(0)
        self._unique_filter_state = real_result._unique_filter_state

    
    def unique(self = None, strategy = None):
        '''Apply unique filtering to the objects returned by this
        :class:`_engine.ScalarResult`.

        See :meth:`_engine.Result.unique` for usage details.

        '''
        self._unique_filter_state = (set(), strategy)
        return self

    
    def partitions(self = None, size = None):
        '''Iterate through sub-lists of elements of the size given.

        Equivalent to :meth:`_engine.Result.partitions` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def fetchall(self = None):
        '''A synonym for the :meth:`_engine.ScalarResult.all` method.'''
        return self._allrows()

    
    def fetchmany(self = None, size = None):
        '''Fetch many objects.

        Equivalent to :meth:`_engine.Result.fetchmany` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        '''
        return self._manyrow_getter(self, size)

    
    def all(self = None):
        '''Return all scalar values in a sequence.

        Equivalent to :meth:`_engine.Result.all` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        '''
        return self._allrows()

    
    def __iter__(self = None):
        return self._iter_impl()

    
    def __next__(self = None):
        return self._next_impl()

    
    def first(self = None):
        '''Fetch the first object or ``None`` if no object is present.

        Equivalent to :meth:`_engine.Result.first` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.


        '''
        return self._only_one_row(raise_for_second_row = False, raise_for_none = False, scalar = False)

    
    def one_or_none(self = None):
        '''Return at most one object or raise an exception.

        Equivalent to :meth:`_engine.Result.one_or_none` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        '''
        return self._only_one_row(raise_for_second_row = True, raise_for_none = False, scalar = False)

    
    def one(self = None):
        '''Return exactly one object or raise an exception.

        Equivalent to :meth:`_engine.Result.one` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        '''
        return self._only_one_row(raise_for_second_row = True, raise_for_none = True, scalar = False)


ScalarResult = <NODE:27>(ScalarResult, 'ScalarResult', FilterResult[_R])

def TupleResult():
    '''TupleResult'''
    __doc__ = "A :class:`_engine.Result` that's typed as returning plain\n    Python tuples instead of rows.\n\n    Since :class:`_engine.Row` acts like a tuple in every way already,\n    this class is a typing only class, regular :class:`_engine.Result` is\n    still used at runtime.\n\n    "
    __slots__ = ()
    if TYPE_CHECKING:
        
        def partitions(self = None, size = None):
            '''Iterate through sub-lists of elements of the size given.

            Equivalent to :meth:`_engine.Result.partitions` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            '''
            pass

        
        def fetchone(self = None):
            '''Fetch one tuple.

            Equivalent to :meth:`_engine.Result.fetchone` except that
            tuple values, rather than :class:`_engine.Row`
            objects, are returned.

            '''
            pass

        
        def fetchall(self = None):
            '''A synonym for the :meth:`_engine.ScalarResult.all` method.'''
            pass

        
        def fetchmany(self = None, size = None):
            '''Fetch many objects.

            Equivalent to :meth:`_engine.Result.fetchmany` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            '''
            pass

        
        def all(self = None):
            '''Return all scalar values in a sequence.

            Equivalent to :meth:`_engine.Result.all` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            '''
            pass

        
        def __iter__(self = None):
            pass

        
        def __next__(self = None):
            pass

        
        def first(self = None):
            '''Fetch the first object or ``None`` if no object is present.

            Equivalent to :meth:`_engine.Result.first` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.


            '''
            pass

        
        def one_or_none(self = None):
            '''Return at most one object or raise an exception.

            Equivalent to :meth:`_engine.Result.one_or_none` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            '''
            pass

        
        def one(self = None):
            '''Return exactly one object or raise an exception.

            Equivalent to :meth:`_engine.Result.one` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            '''
            pass

        scalar_one = (lambda self = None: pass)()
        scalar_one = (lambda self = None: pass)()
        
        def scalar_one(self = None):
            '''Return exactly one scalar result or raise an exception.

            This is equivalent to calling :meth:`_engine.Result.scalars`
            and then :meth:`_engine.ScalarResult.one`.

            .. seealso::

                :meth:`_engine.ScalarResult.one`

                :meth:`_engine.Result.scalars`

            '''
            pass

        scalar_one_or_none = (lambda self = None: pass)()
        scalar_one_or_none = (lambda self = None: pass)()
        
        def scalar_one_or_none(self = None):
            '''Return exactly one or no scalar result.

            This is equivalent to calling :meth:`_engine.Result.scalars`
            and then :meth:`_engine.ScalarResult.one_or_none`.

            .. seealso::

                :meth:`_engine.ScalarResult.one_or_none`

                :meth:`_engine.Result.scalars`

            '''
            pass

        scalar = (lambda self = None: pass)()
        scalar = (lambda self = None: pass)()
        
        def scalar(self = None):
            '''Fetch the first column of the first row, and close the result
            set.

            Returns ``None`` if there are no rows to fetch.

            No validation is performed to test if additional rows remain.

            After calling this method, the object is fully closed,
            e.g. the :meth:`_engine.CursorResult.close`
            method will have been called.

            :return: a Python scalar value , or ``None`` if no rows remain.

            '''
            pass

        return None

TupleResult = <NODE:27>(TupleResult, 'TupleResult', FilterResult[_R], util.TypingOnly)

def MappingResult():
    '''MappingResult'''
    __doc__ = 'A wrapper for a :class:`_engine.Result` that returns dictionary values\n    rather than :class:`_engine.Row` values.\n\n    The :class:`_engine.MappingResult` object is acquired by calling the\n    :meth:`_engine.Result.mappings` method.\n\n    '
    __slots__ = ()
    _generate_rows = True
    _post_creational_filter = operator.attrgetter('_mapping')
    
    def __init__(self = None, result = None):
        self._real_result = result
        self._unique_filter_state = result._unique_filter_state
        self._metadata = result._metadata
        if result._source_supports_scalars:
            self._metadata = self._metadata._reduce([
                0])
            return None

    
    def unique(self = None, strategy = None):
        '''Apply unique filtering to the objects returned by this
        :class:`_engine.MappingResult`.

        See :meth:`_engine.Result.unique` for usage details.

        '''
        self._unique_filter_state = (set(), strategy)
        return self

    
    def columns(self = None, *col_expressions):
        '''Establish the columns that should be returned in each row.'''
        return self._column_slices(col_expressions)

    
    def partitions(self = None, size = None):
        '''Iterate through sub-lists of elements of the size given.

        Equivalent to :meth:`_engine.Result.partitions` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def fetchall(self = None):
        '''A synonym for the :meth:`_engine.MappingResult.all` method.'''
        return self._allrows()

    
    def fetchone(self = None):
        '''Fetch one object.

        Equivalent to :meth:`_engine.Result.fetchone` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        '''
        row = self._onerow_getter(self)
        if row is _NO_ROW:
            return None

    
    def fetchmany(self = None, size = None):
        '''Fetch many objects.

        Equivalent to :meth:`_engine.Result.fetchmany` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        '''
        return self._manyrow_getter(self, size)

    
    def all(self = None):
        '''Return all scalar values in a sequence.

        Equivalent to :meth:`_engine.Result.all` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        '''
        return self._allrows()

    
    def __iter__(self = None):
        return self._iter_impl()

    
    def __next__(self = None):
        return self._next_impl()

    
    def first(self = None):
        '''Fetch the first object or ``None`` if no object is present.

        Equivalent to :meth:`_engine.Result.first` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.


        '''
        return self._only_one_row(raise_for_second_row = False, raise_for_none = False, scalar = False)

    
    def one_or_none(self = None):
        '''Return at most one object or raise an exception.

        Equivalent to :meth:`_engine.Result.one_or_none` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        '''
        return self._only_one_row(raise_for_second_row = True, raise_for_none = False, scalar = False)

    
    def one(self = None):
        '''Return exactly one object or raise an exception.

        Equivalent to :meth:`_engine.Result.one` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        '''
        return self._only_one_row(raise_for_second_row = True, raise_for_none = True, scalar = False)


MappingResult = <NODE:27>(MappingResult, 'MappingResult', _WithKeys, FilterResult[RowMapping])

def FrozenResult():
    '''FrozenResult'''
    data: 'Sequence[Any]' = 'Represents a :class:`_engine.Result` object in a "frozen" state suitable\n    for caching.\n\n    The :class:`_engine.FrozenResult` object is returned from the\n    :meth:`_engine.Result.freeze` method of any :class:`_engine.Result`\n    object.\n\n    A new iterable :class:`_engine.Result` object is generated from a fixed\n    set of data each time the :class:`_engine.FrozenResult` is invoked as\n    a callable::\n\n\n        result = connection.execute(query)\n\n        frozen = result.freeze()\n\n        unfrozen_result_one = frozen()\n\n        for row in unfrozen_result_one:\n            print(row)\n\n        unfrozen_result_two = frozen()\n        rows = unfrozen_result_two.all()\n\n        # ... etc\n\n    .. versionadded:: 1.4\n\n    .. seealso::\n\n        :ref:`do_orm_execute_re_executing` - example usage within the\n        ORM to implement a result-set cache.\n\n        :func:`_orm.loading.merge_frozen_result` - ORM function to merge\n        a frozen result back into a :class:`_orm.Session`.\n\n    '
    
    def __init__(self = None, result = None):
        self.metadata = result._metadata._for_freeze()
        self._source_supports_scalars = result._source_supports_scalars
        self._attributes = result._attributes
        if self._source_supports_scalars:
            self.data = list(result._raw_row_iterator())
            return None
        self.data = None.fetchall()

    
    def rewrite_rows(self = None):
