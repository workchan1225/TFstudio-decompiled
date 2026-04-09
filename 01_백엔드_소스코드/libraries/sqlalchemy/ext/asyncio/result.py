# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: result.pyc (Python 3.11)

from __future__ import annotations
import operator
from typing import Any
from typing import AsyncIterator
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import TYPE_CHECKING
from typing import TypeVar
from  import exc as async_exc
from  import util
from engine import Result
from engine.result import _NO_ROW
from engine.result import _R
from engine.result import _WithKeys
from engine.result import FilterResult
from engine.result import FrozenResult
from engine.result import ResultMetaData
from engine.row import Row
from engine.row import RowMapping
from sql.base import _generative
from util.concurrency import greenlet_spawn
from util.typing import Literal
from util.typing import Self
if TYPE_CHECKING:
    from engine import CursorResult
    from engine.result import _KeyIndexType
    from engine.result import _UniqueFilterType
_T = TypeVar('_T', bound = Any)
_TP = TypeVar('_TP', bound = Tuple[(Any, ...)])

def AsyncCommon():
    '''AsyncCommon'''
    _metadata: 'ResultMetaData' = ()
    
    async def close(self = None):
        '''Close this result.'''
        pass
    # WARNING: Decompyle incomplete

    closed = (lambda self = None: self._real_result.closed)()

AsyncCommon = <NODE:27>(AsyncCommon, 'AsyncCommon', FilterResult[_R])

def AsyncResult():
    '''AsyncResult'''
    __doc__ = 'An asyncio wrapper around a :class:`_result.Result` object.\n\n    The :class:`_asyncio.AsyncResult` only applies to statement executions that\n    use a server-side cursor.  It is returned only from the\n    :meth:`_asyncio.AsyncConnection.stream` and\n    :meth:`_asyncio.AsyncSession.stream` methods.\n\n    .. note:: As is the case with :class:`_engine.Result`, this object is\n       used for ORM results returned by :meth:`_asyncio.AsyncSession.execute`,\n       which can yield instances of ORM mapped objects either individually or\n       within tuple-like rows.  Note that these result objects do not\n       deduplicate instances or rows automatically as is the case with the\n       legacy :class:`_orm.Query` object. For in-Python de-duplication of\n       instances or rows, use the :meth:`_asyncio.AsyncResult.unique` modifier\n       method.\n\n    .. versionadded:: 1.4\n\n    '
    _real_result: 'Result[_TP]' = ()
    
    def __init__(self = None, real_result = None):
        self._real_result = real_result
        self._metadata = real_result._metadata
        self._unique_filter_state = real_result._unique_filter_state
        self._source_supports_scalars = real_result._source_supports_scalars
        self._post_creational_filter = None
        if '_row_getter' in real_result.__dict__:
            self._set_memoized_attribute('_row_getter', real_result.__dict__['_row_getter'])
            return None

    t = (lambda self = None: self)()
    
    def tuples(self = None):
        '''Apply a "typed tuple" typing filter to returned rows.

        This method returns the same :class:`_asyncio.AsyncResult` object
        at runtime,
        however annotates as returning a :class:`_asyncio.AsyncTupleResult`
        object that will indicate to :pep:`484` typing tools that plain typed
        ``Tuple`` instances are returned rather than rows.  This allows
        tuple unpacking and ``__getitem__`` access of :class:`_engine.Row`
        objects to by typed, for those cases where the statement invoked
        itself included typing information.

        .. versionadded:: 2.0

        :return: the :class:`_result.AsyncTupleResult` type at typing time.

        .. seealso::

            :attr:`_asyncio.AsyncResult.t` - shorter synonym

            :attr:`_engine.Row.t` - :class:`_engine.Row` version

        '''
        return self

    unique = (lambda self = None, strategy = None: self._unique_filter_state = (set(), strategy)self)()
    
    def columns(self = None, *col_expressions):
        '''Establish the columns that should be returned in each row.

        Refer to :meth:`_engine.Result.columns` in the synchronous
        SQLAlchemy API for a complete behavioral description.

        '''
        return self._column_slices(col_expressions)

    
    def partitions(self = None, size = None):
        '''Iterate through sub-lists of rows of the size given.

        An async iterator is returned::

            async def scroll_results(connection):
                result = await connection.stream(select(users_table))

                async for partition in result.partitions(100):
                    print("list of rows: %s" % partition)

        Refer to :meth:`_engine.Result.partitions` in the synchronous
        SQLAlchemy API for a complete behavioral description.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def fetchall(self = None):
        '''A synonym for the :meth:`_asyncio.AsyncResult.all` method.

        .. versionadded:: 2.0

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def fetchone(self = None):
        '''Fetch one row.

        When all rows are exhausted, returns None.

        This method is provided for backwards compatibility with
        SQLAlchemy 1.x.x.

        To fetch the first row of a result only, use the
        :meth:`_asyncio.AsyncResult.first` method.  To iterate through all
        rows, iterate the :class:`_asyncio.AsyncResult` object directly.

        :return: a :class:`_engine.Row` object if no filters are applied,
         or ``None`` if no rows remain.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def fetchmany(self = None, size = None):
        '''Fetch many rows.

        When all rows are exhausted, returns an empty list.

        This method is provided for backwards compatibility with
        SQLAlchemy 1.x.x.

        To fetch rows in groups, use the
        :meth:`._asyncio.AsyncResult.partitions` method.

        :return: a list of :class:`_engine.Row` objects.

        .. seealso::

            :meth:`_asyncio.AsyncResult.partitions`

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def all(self = None):
        '''Return all rows in a list.

        Closes the result set after invocation.   Subsequent invocations
        will return an empty list.

        :return: a list of :class:`_engine.Row` objects.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def first(self = None):
        '''Fetch the first row or ``None`` if no row is present.

        Closes the result set and discards remaining rows.

        .. note::  This method returns one **row**, e.g. tuple, by default.
           To return exactly one single scalar value, that is, the first
           column of the first row, use the
           :meth:`_asyncio.AsyncResult.scalar` method,
           or combine :meth:`_asyncio.AsyncResult.scalars` and
           :meth:`_asyncio.AsyncResult.first`.

           Additionally, in contrast to the behavior of the legacy  ORM
           :meth:`_orm.Query.first` method, **no limit is applied** to the
           SQL query which was invoked to produce this
           :class:`_asyncio.AsyncResult`;
           for a DBAPI driver that buffers results in memory before yielding
           rows, all rows will be sent to the Python process and all but
           the first row will be discarded.

           .. seealso::

                :ref:`migration_20_unify_select`

        :return: a :class:`_engine.Row` object, or None
         if no rows remain.

        .. seealso::

            :meth:`_asyncio.AsyncResult.scalar`

            :meth:`_asyncio.AsyncResult.one`

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def one_or_none(self = None):
        '''Return at most one result or raise an exception.

        Returns ``None`` if the result has no rows.
        Raises :class:`.MultipleResultsFound`
        if multiple rows are returned.

        .. versionadded:: 1.4

        :return: The first :class:`_engine.Row` or ``None`` if no row
         is available.

        :raises: :class:`.MultipleResultsFound`

        .. seealso::

            :meth:`_asyncio.AsyncResult.first`

            :meth:`_asyncio.AsyncResult.one`

        '''
        pass
    # WARNING: Decompyle incomplete

    scalar_one = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    scalar_one = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    async def scalar_one(self = None):
        '''Return exactly one scalar result or raise an exception.

        This is equivalent to calling :meth:`_asyncio.AsyncResult.scalars` and
        then :meth:`_asyncio.AsyncScalarResult.one`.

        .. seealso::

            :meth:`_asyncio.AsyncScalarResult.one`

            :meth:`_asyncio.AsyncResult.scalars`

        '''
        pass
    # WARNING: Decompyle incomplete

    scalar_one_or_none = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    scalar_one_or_none = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    async def scalar_one_or_none(self = None):
        '''Return exactly one scalar result or ``None``.

        This is equivalent to calling :meth:`_asyncio.AsyncResult.scalars` and
        then :meth:`_asyncio.AsyncScalarResult.one_or_none`.

        .. seealso::

            :meth:`_asyncio.AsyncScalarResult.one_or_none`

            :meth:`_asyncio.AsyncResult.scalars`

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def one(self = None):
        '''Return exactly one row or raise an exception.

        Raises :class:`.NoResultFound` if the result returns no
        rows, or :class:`.MultipleResultsFound` if multiple rows
        would be returned.

        .. note::  This method returns one **row**, e.g. tuple, by default.
           To return exactly one single scalar value, that is, the first
           column of the first row, use the
           :meth:`_asyncio.AsyncResult.scalar_one` method, or combine
           :meth:`_asyncio.AsyncResult.scalars` and
           :meth:`_asyncio.AsyncResult.one`.

        .. versionadded:: 1.4

        :return: The first :class:`_engine.Row`.

        :raises: :class:`.MultipleResultsFound`, :class:`.NoResultFound`

        .. seealso::

            :meth:`_asyncio.AsyncResult.first`

            :meth:`_asyncio.AsyncResult.one_or_none`

            :meth:`_asyncio.AsyncResult.scalar_one`

        '''
        pass
    # WARNING: Decompyle incomplete

    scalar = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    scalar = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    async def scalar(self = None):
        '''Fetch the first column of the first row, and close the result set.

        Returns ``None`` if there are no rows to fetch.

        No validation is performed to test if additional rows remain.

        After calling this method, the object is fully closed,
        e.g. the :meth:`_engine.CursorResult.close`
        method will have been called.

        :return: a Python scalar value, or ``None`` if no rows remain.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def freeze(self = None):
        '''Return a callable object that will produce copies of this
        :class:`_asyncio.AsyncResult` when invoked.

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
        pass
    # WARNING: Decompyle incomplete

    scalars = (lambda self = None, index = None: pass)()
    scalars = (lambda self = None: pass)()
    scalars = (lambda self = None, index = None: pass)()
    
    def scalars(self = None, index = None):
        '''Return an :class:`_asyncio.AsyncScalarResult` filtering object which
        will return single elements rather than :class:`_row.Row` objects.

        Refer to :meth:`_result.Result.scalars` in the synchronous
        SQLAlchemy API for a complete behavioral description.

        :param index: integer or row key indicating the column to be fetched
         from each row, defaults to ``0`` indicating the first column.

        :return: a new :class:`_asyncio.AsyncScalarResult` filtering object
         referring to this :class:`_asyncio.AsyncResult` object.

        '''
        return AsyncScalarResult(self._real_result, index)

    
    def mappings(self = None):
        '''Apply a mappings filter to returned rows, returning an instance of
        :class:`_asyncio.AsyncMappingResult`.

        When this filter is applied, fetching rows will return
        :class:`_engine.RowMapping` objects instead of :class:`_engine.Row`
        objects.

        :return: a new :class:`_asyncio.AsyncMappingResult` filtering object
         referring to the underlying :class:`_result.Result` object.

        '''
        return AsyncMappingResult(self._real_result)


AsyncResult = <NODE:27>(AsyncResult, 'AsyncResult', _WithKeys, AsyncCommon[Row[_TP]])

def AsyncScalarResult():
    '''AsyncScalarResult'''
    __doc__ = 'A wrapper for a :class:`_asyncio.AsyncResult` that returns scalar values\n    rather than :class:`_row.Row` values.\n\n    The :class:`_asyncio.AsyncScalarResult` object is acquired by calling the\n    :meth:`_asyncio.AsyncResult.scalars` method.\n\n    Refer to the :class:`_result.ScalarResult` object in the synchronous\n    SQLAlchemy API for a complete behavioral description.\n\n    .. versionadded:: 1.4\n\n    '
    __slots__ = ()
    _generate_rows = False
    
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
        :class:`_asyncio.AsyncScalarResult`.

        See :meth:`_asyncio.AsyncResult.unique` for usage details.

        '''
        self._unique_filter_state = (set(), strategy)
        return self

    
    def partitions(self = None, size = None):
        '''Iterate through sub-lists of elements of the size given.

        Equivalent to :meth:`_asyncio.AsyncResult.partitions` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def fetchall(self = None):
        '''A synonym for the :meth:`_asyncio.AsyncScalarResult.all` method.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def fetchmany(self = None, size = None):
        '''Fetch many objects.

        Equivalent to :meth:`_asyncio.AsyncResult.fetchmany` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def all(self = None):
        '''Return all scalar values in a list.

        Equivalent to :meth:`_asyncio.AsyncResult.all` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def first(self = None):
        '''Fetch the first object or ``None`` if no object is present.

        Equivalent to :meth:`_asyncio.AsyncResult.first` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def one_or_none(self = None):
        '''Return at most one object or raise an exception.

        Equivalent to :meth:`_asyncio.AsyncResult.one_or_none` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def one(self = None):
        '''Return exactly one object or raise an exception.

        Equivalent to :meth:`_asyncio.AsyncResult.one` except that
        scalar values, rather than :class:`_engine.Row` objects,
        are returned.

        '''
        pass
    # WARNING: Decompyle incomplete


AsyncScalarResult = <NODE:27>(AsyncScalarResult, 'AsyncScalarResult', AsyncCommon[_R])

def AsyncMappingResult():
    '''AsyncMappingResult'''
    __doc__ = 'A wrapper for a :class:`_asyncio.AsyncResult` that returns dictionary\n    values rather than :class:`_engine.Row` values.\n\n    The :class:`_asyncio.AsyncMappingResult` object is acquired by calling the\n    :meth:`_asyncio.AsyncResult.mappings` method.\n\n    Refer to the :class:`_result.MappingResult` object in the synchronous\n    SQLAlchemy API for a complete behavioral description.\n\n    .. versionadded:: 1.4\n\n    '
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
        :class:`_asyncio.AsyncMappingResult`.

        See :meth:`_asyncio.AsyncResult.unique` for usage details.

        '''
        self._unique_filter_state = (set(), strategy)
        return self

    
    def columns(self = None, *col_expressions):
        '''Establish the columns that should be returned in each row.'''
        return self._column_slices(col_expressions)

    
    def partitions(self = None, size = None):
        '''Iterate through sub-lists of elements of the size given.

        Equivalent to :meth:`_asyncio.AsyncResult.partitions` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def fetchall(self = None):
        '''A synonym for the :meth:`_asyncio.AsyncMappingResult.all` method.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def fetchone(self = None):
        '''Fetch one object.

        Equivalent to :meth:`_asyncio.AsyncResult.fetchone` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def fetchmany(self = None, size = None):
        '''Fetch many rows.

        Equivalent to :meth:`_asyncio.AsyncResult.fetchmany` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def all(self = None):
        '''Return all rows in a list.

        Equivalent to :meth:`_asyncio.AsyncResult.all` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def first(self = None):
        '''Fetch the first object or ``None`` if no object is present.

        Equivalent to :meth:`_asyncio.AsyncResult.first` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def one_or_none(self = None):
        '''Return at most one object or raise an exception.

        Equivalent to :meth:`_asyncio.AsyncResult.one_or_none` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def one(self = None):
        '''Return exactly one object or raise an exception.

        Equivalent to :meth:`_asyncio.AsyncResult.one` except that
        :class:`_engine.RowMapping` values, rather than :class:`_engine.Row`
        objects, are returned.

        '''
        pass
    # WARNING: Decompyle incomplete


AsyncMappingResult = <NODE:27>(AsyncMappingResult, 'AsyncMappingResult', _WithKeys, AsyncCommon[RowMapping])

def AsyncTupleResult():
    '''AsyncTupleResult'''
    __doc__ = "A :class:`_asyncio.AsyncResult` that's typed as returning plain\n    Python tuples instead of rows.\n\n    Since :class:`_engine.Row` acts like a tuple in every way already,\n    this class is a typing only class, regular :class:`_asyncio.AsyncResult` is\n    still used at runtime.\n\n    "
    __slots__ = ()
    if TYPE_CHECKING:
        
        async def partitions(self = None, size = None):
            '''Iterate through sub-lists of elements of the size given.

            Equivalent to :meth:`_result.Result.partitions` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            '''
            pass
        # WARNING: Decompyle incomplete

        
        async def fetchone(self = None):
            '''Fetch one tuple.

            Equivalent to :meth:`_result.Result.fetchone` except that
            tuple values, rather than :class:`_engine.Row`
            objects, are returned.

            '''
            pass
        # WARNING: Decompyle incomplete

        
        async def fetchall(self = None):
            '''A synonym for the :meth:`_engine.ScalarResult.all` method.'''
            pass
        # WARNING: Decompyle incomplete

        
        async def fetchmany(self = None, size = None):
            '''Fetch many objects.

            Equivalent to :meth:`_result.Result.fetchmany` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            '''
            pass
        # WARNING: Decompyle incomplete

        
        async def all(self = None):
            '''Return all scalar values in a list.

            Equivalent to :meth:`_result.Result.all` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            '''
            pass
        # WARNING: Decompyle incomplete

        
        def __aiter__(self = None):
            pass

        
        async def __anext__(self = None):
            pass
        # WARNING: Decompyle incomplete

        
        async def first(self = None):
            '''Fetch the first object or ``None`` if no object is present.

            Equivalent to :meth:`_result.Result.first` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.


            '''
            pass
        # WARNING: Decompyle incomplete

        
        async def one_or_none(self = None):
            '''Return at most one object or raise an exception.

            Equivalent to :meth:`_result.Result.one_or_none` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            '''
            pass
        # WARNING: Decompyle incomplete

        
        async def one(self = None):
            '''Return exactly one object or raise an exception.

            Equivalent to :meth:`_result.Result.one` except that
            tuple values, rather than :class:`_engine.Row` objects,
            are returned.

            '''
            pass
        # WARNING: Decompyle incomplete

        scalar_one = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
        scalar_one = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
        
        async def scalar_one(self = None):
            '''Return exactly one scalar result or raise an exception.

            This is equivalent to calling :meth:`_engine.Result.scalars`
            and then :meth:`_engine.AsyncScalarResult.one`.

            .. seealso::

                :meth:`_engine.AsyncScalarResult.one`

                :meth:`_engine.Result.scalars`

            '''
            pass
        # WARNING: Decompyle incomplete

        scalar_one_or_none = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
        scalar_one_or_none = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
        
        async def scalar_one_or_none(self = None):
            '''Return exactly one or no scalar result.

            This is equivalent to calling :meth:`_engine.Result.scalars`
            and then :meth:`_engine.AsyncScalarResult.one_or_none`.

            .. seealso::

                :meth:`_engine.AsyncScalarResult.one_or_none`

                :meth:`_engine.Result.scalars`

            '''
            pass
        # WARNING: Decompyle incomplete

        scalar = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
        scalar = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
        
        async def scalar(self = None):
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
        # WARNING: Decompyle incomplete

        return None

AsyncTupleResult = <NODE:27>(AsyncTupleResult, 'AsyncTupleResult', AsyncCommon[_R], util.TypingOnly)
_RT = TypeVar('_RT', bound = 'Result[Any]')

async def _ensure_sync_result(result = None, calling_method = None):
    pass
# WARNING: Decompyle incomplete
