# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dml.pyc (Python 3.11)

from __future__ import annotations
from typing import Any
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union
from _typing import _OnConflictIndexElementsT
from _typing import _OnConflictIndexWhereT
from _typing import _OnConflictSetT
from _typing import _OnConflictWhereT
from  import util
from sql import coercions
from sql import roles
from sql import schema
from sql._typing import _DMLTableArgument
from sql.base import _exclusive_against
from sql.base import _generative
from sql.base import ColumnCollection
from sql.base import ReadOnlyColumnCollection
from sql.dml import Insert as StandardInsert
from sql.elements import ClauseElement
from sql.elements import ColumnElement
from sql.elements import KeyedColumnElement
from sql.elements import TextClause
from sql.expression import alias
from util.typing import Self
__all__ = ('Insert', 'insert')

def insert(table = None):
    '''Construct a sqlite-specific variant :class:`_sqlite.Insert`
    construct.

    .. container:: inherited_member

        The :func:`sqlalchemy.dialects.sqlite.insert` function creates
        a :class:`sqlalchemy.dialects.sqlite.Insert`.  This class is based
        on the dialect-agnostic :class:`_sql.Insert` construct which may
        be constructed using the :func:`_sql.insert` function in
        SQLAlchemy Core.

    The :class:`_sqlite.Insert` construct includes additional methods
    :meth:`_sqlite.Insert.on_conflict_do_update`,
    :meth:`_sqlite.Insert.on_conflict_do_nothing`.

    '''
    return Insert(table)


class Insert(StandardInsert):
    '''SQLite-specific implementation of INSERT.

    Adds methods for SQLite-specific syntaxes such as ON CONFLICT.

    The :class:`_sqlite.Insert` object is created using the
    :func:`sqlalchemy.dialects.sqlite.insert` function.

    .. versionadded:: 1.4

    .. seealso::

        :ref:`sqlite_on_conflict_insert`

    '''
    stringify_dialect = 'sqlite'
    inherit_cache = False
    excluded = (lambda self = None: alias(self.table, name = 'excluded').columns)()
    _on_conflict_exclusive = _exclusive_against('_post_values_clause', msgs = {
        '_post_values_clause': 'This Insert construct already has an ON CONFLICT clause established' })
    on_conflict_do_update = (lambda self = None, index_elements = _generative, index_where = _on_conflict_exclusive, set_ = (None, None, None, None), where = ('index_elements', '_OnConflictIndexElementsT', 'index_where', '_OnConflictIndexWhereT', 'set_', '_OnConflictSetT', 'where', '_OnConflictWhereT', 'return', 'Self'): self._post_values_clause = OnConflictDoUpdate(index_elements, index_where, set_, where)self)()()
    on_conflict_do_nothing = (lambda self = None, index_elements = _generative, index_where = _on_conflict_exclusive: self._post_values_clause = OnConflictDoNothing(index_elements, index_where)self)()()


class OnConflictClause(ClauseElement):
    inferred_target_whereclause: 'Optional[Union[ColumnElement[Any], TextClause]]' = 'sqlite'
    
    def __init__(self = None, index_elements = None, index_where = None):
        pass
    # WARNING: Decompyle incomplete



class OnConflictDoNothing(OnConflictClause):
    __visit_name__ = 'on_conflict_do_nothing'


class OnConflictDoUpdate(OnConflictClause):
    pass
# WARNING: Decompyle incomplete
