# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ext.pyc (Python 3.11)

from __future__ import annotations
from typing import Any
from typing import Iterable
from typing import List
from typing import Optional
from typing import overload
from typing import TYPE_CHECKING
from typing import TypeVar
from  import types
from array import ARRAY
from sql import coercions
from sql import elements
from sql import expression
from sql import functions
from sql import roles
from sql import schema
from sql.schema import ColumnCollectionConstraint
from sql.sqltypes import TEXT
from sql.visitors import InternalTraversal
if TYPE_CHECKING:
    from sql._typing import _ColumnExpressionArgument
    from sql.elements import ClauseElement
    from sql.elements import ColumnElement
    from sql.operators import OperatorType
    from sql.selectable import FromClause
    from sql.visitors import _CloneCallableType
    from sql.visitors import _TraverseInternalsType
_T = TypeVar('_T', bound = Any)

def aggregate_order_by():
    '''aggregate_order_by'''
    __doc__ = 'Represent a PostgreSQL aggregate order by expression.\n\n    E.g.::\n\n        from sqlalchemy.dialects.postgresql import aggregate_order_by\n\n        expr = func.array_agg(aggregate_order_by(table.c.a, table.c.b.desc()))\n        stmt = select(expr)\n\n    would represent the expression:\n\n    .. sourcecode:: sql\n\n        SELECT array_agg(a ORDER BY b DESC) FROM table;\n\n    Similarly::\n\n        expr = func.string_agg(\n            table.c.a, aggregate_order_by(literal_column("\',\'"), table.c.a)\n        )\n        stmt = select(expr)\n\n    Would represent:\n\n    .. sourcecode:: sql\n\n        SELECT string_agg(a, \',\' ORDER BY a) FROM table;\n\n    .. versionchanged:: 1.2.13 - the ORDER BY argument may be multiple terms\n\n    .. seealso::\n\n        :class:`_functions.array_agg`\n\n    '
    __visit_name__ = 'aggregate_order_by'
    stringify_dialect = 'postgresql'
    _traverse_internals: '_TraverseInternalsType' = [
        ('target', InternalTraversal.dp_clauseelement),
        ('type', InternalTraversal.dp_type),
        ('order_by', InternalTraversal.dp_clauseelement)]
    __init__ = (lambda self = None, target = None: pass)()
    __init__ = (lambda self = None, target = None: pass)()
    
    def __init__(self = None, target = None, *order_by):
        self.target = coercions.expect(roles.ExpressionElementRole, target)
        self.type = self.target.type
        _lob = len(order_by)
        self
        if _lob == 0:
            raise TypeError('at least one ORDER BY element is required')
        if _lob == 1:
            self.order_by = coercions.expect(roles.ExpressionElementRole, order_by[0])
            return None
    # WARNING: Decompyle incomplete

    
    def self_group(self = None, against = None):
        return self

    
    def get_children(self = None, **kwargs):
        return (self.target, self.order_by)

    
    def _copy_internals(self = None, clone = None, **kw):
        pass
    # WARNING: Decompyle incomplete

    _from_objects = (lambda self = None: self.target._from_objects + self.order_by._from_objects)()

aggregate_order_by = <NODE:27>(aggregate_order_by, 'aggregate_order_by', expression.ColumnElement[_T])

class ExcludeConstraint(ColumnCollectionConstraint):
    pass
# WARNING: Decompyle incomplete


def array_agg(*arg, **kw):
    '''PostgreSQL-specific form of :class:`_functions.array_agg`, ensures
    return type is :class:`_postgresql.ARRAY` and not
    the plain :class:`_types.ARRAY`, unless an explicit ``type_``
    is passed.

    '''
    kw['_default_array_type'] = ARRAY
# WARNING: Decompyle incomplete


def _regconfig_fn():
    '''_regconfig_fn'''
    pass
# WARNING: Decompyle incomplete

_regconfig_fn = <NODE:27>(_regconfig_fn, '_regconfig_fn', functions.GenericFunction[_T])

class to_tsvector(_regconfig_fn):
    '''The PostgreSQL ``to_tsvector`` SQL function.

    This function applies automatic casting of the REGCONFIG argument
    to use the :class:`_postgresql.REGCONFIG` datatype automatically,
    and applies a return type of :class:`_postgresql.TSVECTOR`.

    Assuming the PostgreSQL dialect has been imported, either by invoking
    ``from sqlalchemy.dialects import postgresql``, or by creating a PostgreSQL
    engine using ``create_engine("postgresql...")``,
    :class:`_postgresql.to_tsvector` will be used automatically when invoking
    ``sqlalchemy.func.to_tsvector()``, ensuring the correct argument and return
    type handlers are used at compile and execution time.

    .. versionadded:: 2.0.0rc1

    '''
    inherit_cache = True
    type = types.TSVECTOR


class to_tsquery(_regconfig_fn):
    '''The PostgreSQL ``to_tsquery`` SQL function.

    This function applies automatic casting of the REGCONFIG argument
    to use the :class:`_postgresql.REGCONFIG` datatype automatically,
    and applies a return type of :class:`_postgresql.TSQUERY`.

    Assuming the PostgreSQL dialect has been imported, either by invoking
    ``from sqlalchemy.dialects import postgresql``, or by creating a PostgreSQL
    engine using ``create_engine("postgresql...")``,
    :class:`_postgresql.to_tsquery` will be used automatically when invoking
    ``sqlalchemy.func.to_tsquery()``, ensuring the correct argument and return
    type handlers are used at compile and execution time.

    .. versionadded:: 2.0.0rc1

    '''
    inherit_cache = True
    type = types.TSQUERY


class plainto_tsquery(_regconfig_fn):
    '''The PostgreSQL ``plainto_tsquery`` SQL function.

    This function applies automatic casting of the REGCONFIG argument
    to use the :class:`_postgresql.REGCONFIG` datatype automatically,
    and applies a return type of :class:`_postgresql.TSQUERY`.

    Assuming the PostgreSQL dialect has been imported, either by invoking
    ``from sqlalchemy.dialects import postgresql``, or by creating a PostgreSQL
    engine using ``create_engine("postgresql...")``,
    :class:`_postgresql.plainto_tsquery` will be used automatically when
    invoking ``sqlalchemy.func.plainto_tsquery()``, ensuring the correct
    argument and return type handlers are used at compile and execution time.

    .. versionadded:: 2.0.0rc1

    '''
    inherit_cache = True
    type = types.TSQUERY


class phraseto_tsquery(_regconfig_fn):
    '''The PostgreSQL ``phraseto_tsquery`` SQL function.

    This function applies automatic casting of the REGCONFIG argument
    to use the :class:`_postgresql.REGCONFIG` datatype automatically,
    and applies a return type of :class:`_postgresql.TSQUERY`.

    Assuming the PostgreSQL dialect has been imported, either by invoking
    ``from sqlalchemy.dialects import postgresql``, or by creating a PostgreSQL
    engine using ``create_engine("postgresql...")``,
    :class:`_postgresql.phraseto_tsquery` will be used automatically when
    invoking ``sqlalchemy.func.phraseto_tsquery()``, ensuring the correct
    argument and return type handlers are used at compile and execution time.

    .. versionadded:: 2.0.0rc1

    '''
    inherit_cache = True
    type = types.TSQUERY


class websearch_to_tsquery(_regconfig_fn):
    '''The PostgreSQL ``websearch_to_tsquery`` SQL function.

    This function applies automatic casting of the REGCONFIG argument
    to use the :class:`_postgresql.REGCONFIG` datatype automatically,
    and applies a return type of :class:`_postgresql.TSQUERY`.

    Assuming the PostgreSQL dialect has been imported, either by invoking
    ``from sqlalchemy.dialects import postgresql``, or by creating a PostgreSQL
    engine using ``create_engine("postgresql...")``,
    :class:`_postgresql.websearch_to_tsquery` will be used automatically when
    invoking ``sqlalchemy.func.websearch_to_tsquery()``, ensuring the correct
    argument and return type handlers are used at compile and execution time.

    .. versionadded:: 2.0.0rc1

    '''
    inherit_cache = True
    type = types.TSQUERY


class ts_headline(_regconfig_fn):
    pass
# WARNING: Decompyle incomplete
