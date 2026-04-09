# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cursor.pyc (Python 3.11)

'''Define cursor-specific result set constructs including
:class:`.CursorResult`.'''
from __future__ import annotations
import collections
import functools
import operator
import typing
from typing import Any
from typing import cast
from typing import ClassVar
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import NoReturn
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from result import IteratorResult
from result import MergedResult
from result import Result
from result import ResultMetaData
from result import SimpleResultMetaData
from result import tuplegetter
from row import Row
from  import exc
from  import util
from sql import elements
from sql import sqltypes
from sql import util as sql_util
from sql.base import _generative
from sql.compiler import ResultColumnsEntry
from sql.compiler import RM_NAME
from sql.compiler import RM_OBJECTS
from sql.compiler import RM_RENDERED_NAME
from sql.compiler import RM_TYPE
from sql.type_api import TypeEngine
from util import compat
from util.typing import Literal
from util.typing import Self
if typing.TYPE_CHECKING:
    from base import Connection
    from default import DefaultExecutionContext
    from interfaces import _DBAPICursorDescription
    from interfaces import DBAPICursor
    from interfaces import Dialect
    from interfaces import ExecutionContext
    from result import _KeyIndexType
    from result import _KeyMapRecType
    from result import _KeyMapType
    from result import _KeyType
    from result import _ProcessorsType
    from result import _TupleGetterType
    from sql.type_api import _ResultProcessorType
_T = TypeVar('_T', bound = Any)
MD_INDEX: 'Literal[0]' = 0
MD_RESULT_MAP_INDEX: 'Literal[1]' = 1
MD_OBJECTS: 'Literal[2]' = 2
MD_LOOKUP_KEY: 'Literal[3]' = 3
MD_RENDERED_NAME: 'Literal[4]' = 4
MD_PROCESSOR: 'Literal[5]' = 5
MD_UNTRANSLATED: 'Literal[6]' = 6
_CursorKeyMapRecType = Tuple[(Optional[int], int, List[Any], str, str, Optional['_ResultProcessorType[Any]'], Optional[str])]
_CursorKeyMapType = Mapping[('_KeyType', _CursorKeyMapRecType)]
_NonAmbigCursorKeyMapRecType = Tuple[(int, int, List[Any], str, str, Optional['_ResultProcessorType[Any]'], str)]

class CursorResultMetaData(ResultMetaData):
    '''Result metadata for DBAPI cursors.'''
    _translated_indexes: 'Optional[List[int]]' = ('_keymap', '_processors', '_keys', '_keymap_by_result_column_idx', '_tuplefilter', '_translated_indexes', '_safe_for_cache', '_unpickled', '_key_to_index')
    returns_rows: 'ClassVar[bool]' = True
    
    def _has_key(self = None, key = None):
        return key in self._keymap

    
    def _for_freeze(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _make_new_metadata(self = None, *, unpickled, processors, keys, keymap, tuplefilter, translated_indexes, safe_for_cache, keymap_by_result_column_idx):
        new_obj = self.__class__.__new__(self.__class__)
        new_obj._unpickled = unpickled
        new_obj._processors = processors
        new_obj._keys = keys
        new_obj._keymap = keymap
        new_obj._tuplefilter = tuplefilter
        new_obj._translated_indexes = translated_indexes
        new_obj._safe_for_cache = safe_for_cache
        new_obj._keymap_by_result_column_idx = keymap_by_result_column_idx
        new_obj._key_to_index = self._make_key_to_index(keymap, MD_INDEX)
        return new_obj

    
    def _remove_processors(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _splice_horizontally(self = None, other = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _reduce(self = None, keys = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _adapt_to_context(self = None, context = None):
        '''When using a cached Compiled construct that has a _result_map,
        for a new statement that used the cached Compiled, we need to ensure
        the keymap has the Column objects from our new statement as keys.
        So here we rewrite keymap with new entries for the new columns
        as matched to those of the cached statement.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __init__(self = None, parent = None, cursor_description = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _merge_cursor_description(self, context, cursor_description, result_columns, num_ctx_cols, cols_are_ordered, textual_ordered, ad_hoc_textual, loose_column_name_matching):
        """Merge a cursor.description with compiled result column information.

        There are at least four separate strategies used here, selected
        depending on the type of SQL construct used to start with.

        The most common case is that of the compiled SQL expression construct,
        which generated the column names present in the raw SQL string and
        which has the identical number of columns as were reported by
        cursor.description.  In this case, we assume a 1-1 positional mapping
        between the entries in cursor.description and the compiled object.
        This is also the most performant case as we disregard extracting /
        decoding the column names present in cursor.description since we
        already have the desired name we generated in the compiled SQL
        construct.

        The next common case is that of the completely raw string SQL,
        such as passed to connection.execute().  In this case we have no
        compiled construct to work with, so we extract and decode the
        names from cursor.description and index those as the primary
        result row target keys.

        The remaining fairly common case is that of the textual SQL
        that includes at least partial column information; this is when
        we use a :class:`_expression.TextualSelect` construct.
        This construct may have
        unordered or ordered column information.  In the ordered case, we
        merge the cursor.description and the compiled construct's information
        positionally, and warn if there are additional description names
        present, however we still decode the names in cursor.description
        as we don't have a guarantee that the names in the columns match
        on these.   In the unordered case, we match names in cursor.description
        to that of the compiled construct based on name matching.
        In both of these cases, the cursor.description names and the column
        expression objects and names are indexed as result row target keys.

        The final case is much less common, where we have a compiled
        non-textual SQL expression construct, but the number of columns
        in cursor.description doesn't match what's in the compiled
        construct.  We make the guess here that there might be textual
        column expressions in the compiled construct that themselves include
        a comma in them causing them to split.  We do the same name-matching
        as with textual non-ordered columns.

        The name-matched system of merging is the same as that used by
        SQLAlchemy for all cases up through the 0.9 series.   Positional
        matching for compiled SQL expressions was introduced in 1.0 as a
        major performance feature, and positional matching for textual
        :class:`_expression.TextualSelect` objects in 1.1.
        As name matching is no longer
        a common case, it was acceptable to factor it into smaller generator-
        oriented methods that are easier to understand, but incur slightly
        more performance overhead.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def _colnames_from_description(self, context, cursor_description):
        '''Extract column names and data types from a cursor.description.

        Applies unicode decoding, column translation, "normalization",
        and case sensitivity rules to the names based on the dialect.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _merge_textual_cols_by_position(self, context, cursor_description, result_columns):
        pass
    # WARNING: Decompyle incomplete

    
    def _merge_cols_by_name(self, context, cursor_description, result_columns, loose_column_name_matching):
        pass
    # WARNING: Decompyle incomplete

    _create_description_match_map = (lambda cls = None, result_columns = None, loose_column_name_matching = classmethod: d = { }for ridx, elem in enumerate(result_columns):
key = elem[RM_RENDERED_NAME]if key in d:
(e_name, e_obj, e_type, e_ridx) = d[key]d[key] = (e_name, e_obj + elem[RM_OBJECTS], e_type, ridx)else:
d[key] = (elem[RM_NAME], elem[RM_OBJECTS], elem[RM_TYPE], ridx)if loose_column_name_matching:
for r_key in elem[RM_OBJECTS]:
d.setdefault(r_key, (elem[RM_NAME], elem[RM_OBJECTS], elem[RM_TYPE], ridx))d)()
    
    def _merge_cols_by_none(self, context, cursor_description):
        pass
    # WARNING: Decompyle incomplete

    if not TYPE_CHECKING:
        
        def _key_fallback(self = None, key = None, err = None, raiseerr = (True,)):
            if raiseerr:
                if self._unpickled and isinstance(key, elements.ColumnElement):
                    raise exc.NoSuchColumnError('Row was unpickled; lookup by ColumnElement is unsupported'), err
                raise exc.NoSuchColumnError("Could not locate column in row for column '%s'" % util.string_or_unprintable(key)), err

    
    def _raise_for_ambiguous_column_name(self, rec):
        raise exc.InvalidRequestError("Ambiguous column name '%s' in result set column descriptions" % rec[MD_LOOKUP_KEY])

    
    def _index_for_key(self = None, key = None, raiseerr = None):
        if isinstance(key, int):
            key = self._keys[key]
    # WARNING: Decompyle incomplete

    
    def _indexes_for_keys(self, keys):
        pass
    # WARNING: Decompyle incomplete

    
    def _metadata_for_keys(self = None, keys = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __getstate__(self):
        return {
            '_keymap': self._keymap.items()(),
            '_keys': self._keys,
            '_translated_indexes': self._translated_indexes }

    
    def __setstate__(self, state):
        self._processors = range(len(state['_keys']))()
        self._keymap = state['_keymap']
        self._keymap_by_result_column_idx = None
        self._key_to_index = self._make_key_to_index(self._keymap, MD_INDEX)
        self._keys = state['_keys']
        self._unpickled = True
    # WARNING: Decompyle incomplete



class ResultFetchStrategy:
    '''Define a fetching strategy for a result object.


    .. versionadded:: 1.4

    '''
    __slots__ = ()
    alternate_cursor_description: 'Optional[_DBAPICursorDescription]' = None
    
    def soft_close(self = None, result = None, dbapi_cursor = None):
        raise NotImplementedError()

    
    def hard_close(self = None, result = None, dbapi_cursor = None):
        raise NotImplementedError()

    
    def yield_per(self = None, result = None, dbapi_cursor = None, num = ('result', 'CursorResult[Any]', 'dbapi_cursor', 'Optional[DBAPICursor]', 'num', 'int', 'return', 'None')):
        pass

    
    def fetchone(self = None, result = None, dbapi_cursor = None, hard_close = (False,)):
        raise NotImplementedError()

    
    def fetchmany(self = None, result = None, dbapi_cursor = None, size = (None,)):
        raise NotImplementedError()

    
    def fetchall(self = None, result = None, dbapi_cursor = None):
        raise NotImplementedError()

    
    def handle_exception(self = None, result = None, dbapi_cursor = None, err = ('result', 'CursorResult[Any]', 'dbapi_cursor', 'Optional[DBAPICursor]', 'err', 'BaseException', 'return', 'NoReturn')):
        raise err



class NoCursorFetchStrategy(ResultFetchStrategy):
    '''Cursor strategy for a result that has no open cursor.

    There are two varieties of this strategy, one for DQL and one for
    DML (and also DDL), each of which represent a result that had a cursor
    but no longer has one.

    '''
    __slots__ = ()
    
    def soft_close(self, result, dbapi_cursor):
        pass

    
    def hard_close(self, result, dbapi_cursor):
        pass

    
    def fetchone(self, result, dbapi_cursor, hard_close = (False,)):
        return self._non_result(result, None)

    
    def fetchmany(self, result, dbapi_cursor, size = (None,)):
        return self._non_result(result, [])

    
    def fetchall(self, result, dbapi_cursor):
        return self._non_result(result, [])

    
    def _non_result(self, result, default, err = (None,)):
        raise NotImplementedError()



class NoCursorDQLFetchStrategy(NoCursorFetchStrategy):
    '''Cursor strategy for a DQL result that has no open cursor.

    This is a result set that can return rows, i.e. for a SELECT, or for an
    INSERT, UPDATE, DELETE that includes RETURNING. However it is in the state
    where the cursor is closed and no rows remain available.  The owning result
    object may or may not be "hard closed", which determines if the fetch
    methods send empty results or raise for closed result.

    '''
    __slots__ = ()
    
    def _non_result(self, result, default, err = (None,)):
        if result.closed:
            raise exc.ResourceClosedError('This result object is closed.'), err
        return default


_NO_CURSOR_DQL = NoCursorDQLFetchStrategy()

class NoCursorDMLFetchStrategy(NoCursorFetchStrategy):
    '''Cursor strategy for a DML result that has no open cursor.

    This is a result set that does not return rows, i.e. for an INSERT,
    UPDATE, DELETE that does not include RETURNING.

    '''
    __slots__ = ()
    
    def _non_result(self, result, default, err = (None,)):
        pass
    # WARNING: Decompyle incomplete


_NO_CURSOR_DML = NoCursorDMLFetchStrategy()

class CursorFetchStrategy(ResultFetchStrategy):
    '''Call fetch methods from a DBAPI cursor.

    Alternate versions of this class may instead buffer the rows from
    cursors or not use cursors at all.

    '''
    __slots__ = ()
    
    def soft_close(self = None, result = None, dbapi_cursor = None):
        result.cursor_strategy = _NO_CURSOR_DQL

    
    def hard_close(self = None, result = None, dbapi_cursor = None):
        result.cursor_strategy = _NO_CURSOR_DQL

    
    def handle_exception(self = None, result = None, dbapi_cursor = None, err = ('result', 'CursorResult[Any]', 'dbapi_cursor', 'Optional[DBAPICursor]', 'err', 'BaseException', 'return', 'NoReturn')):
        result.connection._handle_dbapi_exception(err, None, None, dbapi_cursor, result.context)

    
    def yield_per(self = None, result = None, dbapi_cursor = None, num = ('result', 'CursorResult[Any]', 'dbapi_cursor', 'Optional[DBAPICursor]', 'num', 'int', 'return', 'None')):
        result.cursor_strategy = BufferedRowCursorFetchStrategy(dbapi_cursor, {
            'max_row_buffer': num }, initial_buffer = collections.deque(), growth_factor = 0)

    
    def fetchone(self = None, result = None, dbapi_cursor = None, hard_close = (False,)):
        pass
    # WARNING: Decompyle incomplete

    
    def fetchmany(self = None, result = None, dbapi_cursor = None, size = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def fetchall(self = None, result = None, dbapi_cursor = None):
        
        try:
            rows = dbapi_cursor.fetchall()
            result._soft_close()
            return rows
        except BaseException:
            e = None
            self.handle_exception(result, dbapi_cursor, e)
            e = None
            del e
            return None
            e = None
            del e



_DEFAULT_FETCH = CursorFetchStrategy()

class BufferedRowCursorFetchStrategy(CursorFetchStrategy):
    pass
# WARNING: Decompyle incomplete


class FullyBufferedCursorFetchStrategy(CursorFetchStrategy):
    pass
# WARNING: Decompyle incomplete


class _NoResultMetaData(ResultMetaData):
    __slots__ = ()
    returns_rows = False
    
    def _we_dont_return_rows(self, err = (None,)):
        raise exc.ResourceClosedError('This result object does not return rows. It has been closed automatically.'), err

    
    def _index_for_key(self, keys, raiseerr):
        self._we_dont_return_rows()

    
    def _metadata_for_keys(self, key):
        self._we_dont_return_rows()

    
    def _reduce(self, keys):
        self._we_dont_return_rows()

    _keymap = (lambda self: self._we_dont_return_rows())()
    _key_to_index = (lambda self: self._we_dont_return_rows())()
    _processors = (lambda self: self._we_dont_return_rows())()
    keys = (lambda self: self._we_dont_return_rows())()

_NO_RESULT_METADATA = _NoResultMetaData()

def null_dml_result():
    it = IteratorResult(_NoResultMetaData(), iter([]))
    it._soft_close()
    return it


def CursorResult():
    '''CursorResult'''
    pass
# WARNING: Decompyle incomplete

CursorResult = <NODE:27>(CursorResult, 'CursorResult', Result[_T])
ResultProxy = CursorResult
