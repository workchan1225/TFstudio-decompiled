# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dml.pyc (Python 3.11)

from __future__ import annotations
from typing import Any
from typing import Dict
from typing import List
from typing import Mapping
from typing import Optional
from typing import Tuple
from typing import Union
from  import exc
from  import util
from sql._typing import _DMLTableArgument
from sql.base import _exclusive_against
from sql.base import _generative
from sql.base import ColumnCollection
from sql.base import ReadOnlyColumnCollection
from sql.dml import Insert as StandardInsert
from sql.elements import ClauseElement
from sql.elements import KeyedColumnElement
from sql.expression import alias
from sql.selectable import NamedFromClause
from util.typing import Self
__all__ = ('Insert', 'insert')

def insert(table = None):
    '''Construct a MySQL/MariaDB-specific variant :class:`_mysql.Insert`
    construct.

    .. container:: inherited_member

        The :func:`sqlalchemy.dialects.mysql.insert` function creates
        a :class:`sqlalchemy.dialects.mysql.Insert`.  This class is based
        on the dialect-agnostic :class:`_sql.Insert` construct which may
        be constructed using the :func:`_sql.insert` function in
        SQLAlchemy Core.

    The :class:`_mysql.Insert` construct includes additional methods
    :meth:`_mysql.Insert.on_duplicate_key_update`.

    '''
    return Insert(table)


class Insert(StandardInsert):
    '''MySQL-specific implementation of INSERT.

    Adds methods for MySQL-specific syntaxes such as ON DUPLICATE KEY UPDATE.

    The :class:`~.mysql.Insert` object is created using the
    :func:`sqlalchemy.dialects.mysql.insert` function.

    .. versionadded:: 1.2

    '''
    stringify_dialect = 'mysql'
    inherit_cache = False
    inserted = (lambda self = None: self.inserted_alias.columns)()
    inserted_alias = (lambda self = None: alias(self.table, name = 'inserted'))()
    on_duplicate_key_update = (lambda self = None: if args and kw:
raise exc.ArgumentError("Can't pass kwargs and positional arguments simultaneously")if args:
if len(args) > 1:
raise exc.ArgumentError('Only a single dictionary or list of tuples is accepted positionally.')values = args[0]else:
values = kwself._post_values_clause = OnDuplicateClause(self.inserted_alias, values)self)()()


class OnDuplicateClause(ClauseElement):
    __visit_name__ = 'on_duplicate_key_update'
    update: 'Dict[str, Any]' = None
    stringify_dialect = 'mysql'
    
    def __init__(self = None, inserted_alias = None, update = None):
        self.inserted_alias = inserted_alias
        if isinstance(update, list) and update and isinstance(update[0], tuple):
            self._parameter_ordering = update()
            update = dict(update)
        if isinstance(update, dict):
            if not update:
                raise ValueError('update parameter dictionary must not be empty')
        elif isinstance(update, ColumnCollection):
            update = dict(update)
        else:
            raise ValueError('update parameter must be a non-empty dictionary or a ColumnCollection such as the `.c.` collection of a Table object')
        self.update = update


_UpdateArg = Union[(Mapping[(Any, Any)], List[Tuple[(str, Any)]], ColumnCollection[(Any, Any)])]
