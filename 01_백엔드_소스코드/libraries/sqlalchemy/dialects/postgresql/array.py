# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: array.pyc (Python 3.11)

from __future__ import annotations
import re
from typing import Any as typing_Any
from typing import Iterable
from typing import Optional
from typing import Sequence
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from operators import CONTAINED_BY
from operators import CONTAINS
from operators import OVERLAP
from  import types as sqltypes
from  import util
from sql import expression
from sql import operators
from sql.visitors import InternalTraversal
if TYPE_CHECKING:
    from engine.interfaces import Dialect
    from sql._typing import _ColumnExpressionArgument
    from sql._typing import _TypeEngineArgument
    from sql.elements import ColumnElement
    from sql.elements import Grouping
    from sql.expression import BindParameter
    from sql.operators import OperatorType
    from sql.selectable import _SelectIterable
    from sql.type_api import _BindProcessorType
    from sql.type_api import _LiteralProcessorType
    from sql.type_api import _ResultProcessorType
    from sql.type_api import TypeEngine
    from sql.visitors import _TraverseInternalsType
    from util.typing import Self
_T = TypeVar('_T', bound = typing_Any)
_CT = TypeVar('_CT', bound = typing_Any)

def Any(other = None, arrexpr = None, operator = None):
    '''A synonym for the ARRAY-level :meth:`.ARRAY.Comparator.any` method.
    See that method for details.

    '''
    return arrexpr.any(other, operator)


def All(other = None, arrexpr = None, operator = None):
    '''A synonym for the ARRAY-level :meth:`.ARRAY.Comparator.all` method.
    See that method for details.

    '''
    return arrexpr.all(other, operator)


def array():
    '''array'''
    pass
# WARNING: Decompyle incomplete

array = <NODE:27>(array, 'array', expression.ExpressionClauseList[_T])

def ARRAY():
    '''ARRAY'''
    __doc__ = 'PostgreSQL ARRAY type.\n\n    The :class:`_postgresql.ARRAY` type is constructed in the same way\n    as the core :class:`_types.ARRAY` type; a member type is required, and a\n    number of dimensions is recommended if the type is to be used for more\n    than one dimension::\n\n        from sqlalchemy.dialects import postgresql\n\n        mytable = Table(\n            "mytable",\n            metadata,\n            Column("data", postgresql.ARRAY(Integer, dimensions=2)),\n        )\n\n    The :class:`_postgresql.ARRAY` type provides all operations defined on the\n    core :class:`_types.ARRAY` type, including support for "dimensions",\n    indexed access, and simple matching such as\n    :meth:`.types.ARRAY.Comparator.any` and\n    :meth:`.types.ARRAY.Comparator.all`.  :class:`_postgresql.ARRAY`\n    class also\n    provides PostgreSQL-specific methods for containment operations, including\n    :meth:`.postgresql.ARRAY.Comparator.contains`\n    :meth:`.postgresql.ARRAY.Comparator.contained_by`, and\n    :meth:`.postgresql.ARRAY.Comparator.overlap`, e.g.::\n\n        mytable.c.data.contains([1, 2])\n\n    Indexed access is one-based by default, to match that of PostgreSQL;\n    for zero-based indexed access, set\n    :paramref:`_postgresql.ARRAY.zero_indexes`.\n\n    Additionally, the :class:`_postgresql.ARRAY`\n    type does not work directly in\n    conjunction with the :class:`.ENUM` type.  For a workaround, see the\n    special type at :ref:`postgresql_array_of_enum`.\n\n    .. container:: topic\n\n        **Detecting Changes in ARRAY columns when using the ORM**\n\n        The :class:`_postgresql.ARRAY` type, when used with the SQLAlchemy ORM,\n        does not detect in-place mutations to the array. In order to detect\n        these, the :mod:`sqlalchemy.ext.mutable` extension must be used, using\n        the :class:`.MutableList` class::\n\n            from sqlalchemy.dialects.postgresql import ARRAY\n            from sqlalchemy.ext.mutable import MutableList\n\n\n            class SomeOrmClass(Base):\n                # ...\n\n                data = Column(MutableList.as_mutable(ARRAY(Integer)))\n\n        This extension will allow "in-place" changes such to the array\n        such as ``.append()`` to produce events which will be detected by the\n        unit of work.  Note that changes to elements **inside** the array,\n        including subarrays that are mutated in place, are **not** detected.\n\n        Alternatively, assigning a new array value to an ORM element that\n        replaces the old one will always trigger a change event.\n\n    .. seealso::\n\n        :class:`_types.ARRAY` - base array type\n\n        :class:`_postgresql.array` - produces a literal array value.\n\n    '
    
    def __init__(self = None, item_type = None, as_tuple = None, dimensions = (False, None, False), zero_indexes = ('item_type', '_TypeEngineArgument[_T]', 'as_tuple', 'bool', 'dimensions', 'Optional[int]', 'zero_indexes', 'bool')):
        '''Construct an ARRAY.

        E.g.::

          Column("myarray", ARRAY(Integer))

        Arguments are:

        :param item_type: The data type of items of this array. Note that
          dimensionality is irrelevant here, so multi-dimensional arrays like
          ``INTEGER[][]``, are constructed as ``ARRAY(Integer)``, not as
          ``ARRAY(ARRAY(Integer))`` or such.

        :param as_tuple=False: Specify whether return results
          should be converted to tuples from lists. DBAPIs such
          as psycopg2 return lists by default. When tuples are
          returned, the results are hashable.

        :param dimensions: if non-None, the ARRAY will assume a fixed
         number of dimensions.  This will cause the DDL emitted for this
         ARRAY to include the exact number of bracket clauses ``[]``,
         and will also optimize the performance of the type overall.
         Note that PG arrays are always implicitly "non-dimensioned",
         meaning they can store any number of dimensions no matter how
         they were declared.

        :param zero_indexes=False: when True, index values will be converted
         between Python zero-based and PostgreSQL one-based indexes, e.g.
         a value of one will be added to all index values before passing
         to the database.

        '''
        if isinstance(item_type, ARRAY):
            raise ValueError('Do not nest ARRAY types; ARRAY(basetype) handles multi-dimensional arrays of basetype')
        if isinstance(item_type, type):
            item_type = item_type()
        self.item_type = item_type
        self.as_tuple = as_tuple
        self.dimensions = dimensions
        self.zero_indexes = zero_indexes

    
    def Comparator():
        '''ARRAY.Comparator'''
        __doc__ = 'Define comparison operations for :class:`_types.ARRAY`.\n\n        Note that these operations are in addition to those provided\n        by the base :class:`.types.ARRAY.Comparator` class, including\n        :meth:`.types.ARRAY.Comparator.any` and\n        :meth:`.types.ARRAY.Comparator.all`.\n\n        '
        
        def contains(self = None, other = None, **kwargs):
            '''Boolean expression.  Test if elements are a superset of the
            elements of the argument array expression.

            kwargs may be ignored by this operator but are required for API
            conformance.
            '''
            return self.operate(CONTAINS, other, result_type = sqltypes.Boolean)

        
        def contained_by(self = None, other = None):
            '''Boolean expression.  Test if elements are a proper subset of the
            elements of the argument array expression.
            '''
            return self.operate(CONTAINED_BY, other, result_type = sqltypes.Boolean)

        
        def overlap(self = None, other = None):
            '''Boolean expression.  Test if array has elements in common with
            an argument array expression.
            '''
            return self.operate(OVERLAP, other, result_type = sqltypes.Boolean)


    Comparator = <NODE:27>(Comparator, 'Comparator', sqltypes.ARRAY.Comparator[_CT])
    comparator_factory = Comparator
    _against_native_enum = (lambda self = None:
