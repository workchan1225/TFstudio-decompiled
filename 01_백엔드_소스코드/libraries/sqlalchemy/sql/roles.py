# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: roles.pyc (Python 3.11)

from __future__ import annotations
from typing import Any
from typing import Generic
from typing import Optional
from typing import TYPE_CHECKING
from typing import TypeVar
from  import util
from util.typing import Literal
if TYPE_CHECKING:
    from _typing import _PropagateAttrsType
    from elements import Label
    from selectable import _SelectIterable
    from selectable import FromClause
    from selectable import Subquery
_T = TypeVar('_T', bound = Any)
_T_co = TypeVar('_T_co', bound = Any, covariant = True)

class SQLRole:
    '''Define a "role" within a SQL statement structure.

    Classes within SQL Core participate within SQLRole hierarchies in order
    to more accurately indicate where they may be used within SQL statements
    of all types.

    .. versionadded:: 1.4

    '''
    __slots__ = ()
    allows_lambda = False
    uses_inspection = False


class UsesInspection:
    __slots__ = ()
    _post_inspect: 'Literal[None]' = None
    uses_inspection = True


class AllowsLambdaRole:
    __slots__ = ()
    allows_lambda = True


class HasCacheKeyRole(SQLRole):
    __slots__ = ()
    _role_name = 'Cacheable Core or ORM object'


class ExecutableOptionRole(SQLRole):
    __slots__ = ()
    _role_name = 'ExecutionOption Core or ORM object'


class LiteralValueRole(SQLRole):
    __slots__ = ()
    _role_name = 'Literal Python value'


class ColumnArgumentRole(SQLRole):
    __slots__ = ()
    _role_name = 'Column expression'


class ColumnArgumentOrKeyRole(ColumnArgumentRole):
    __slots__ = ()
    _role_name = 'Column expression or string key'


class StrAsPlainColumnRole(ColumnArgumentRole):
    __slots__ = ()
    _role_name = 'Column expression or string key'


class ColumnListRole(SQLRole):
    '''Elements suitable for forming comma separated lists of expressions.'''
    __slots__ = ()


class StringRole(SQLRole):
    '''mixin indicating a role that results in strings'''
    __slots__ = ()


class TruncatedLabelRole(SQLRole, StringRole):
    __slots__ = ()
    _role_name = 'String SQL identifier'


class ColumnsClauseRole(ColumnListRole, UsesInspection, AllowsLambdaRole):
    __slots__ = ()
    _role_name = 'Column expression, FROM clause, or other columns clause element'
    _select_iterable = (lambda self = None: raise NotImplementedError())()


def TypedColumnsClauseRole():
    '''TypedColumnsClauseRole'''
    __doc__ = 'element-typed form of ColumnsClauseRole'
    __slots__ = ()

TypedColumnsClauseRole = <NODE:27>(TypedColumnsClauseRole, 'TypedColumnsClauseRole', Generic[_T_co], SQLRole)

class LimitOffsetRole(SQLRole):
    __slots__ = ()
    _role_name = 'LIMIT / OFFSET expression'


class ByOfRole(ColumnListRole):
    __slots__ = ()
    _role_name = 'GROUP BY / OF / etc. expression'


class GroupByRole(ByOfRole, UsesInspection, AllowsLambdaRole):
    __slots__ = ()
    _role_name = 'GROUP BY expression'


class OrderByRole(ByOfRole, AllowsLambdaRole):
    __slots__ = ()
    _role_name = 'ORDER BY expression'


class StructuralRole(SQLRole):
    __slots__ = ()


class StatementOptionRole(StructuralRole):
    __slots__ = ()
    _role_name = 'statement sub-expression element'


class OnClauseRole(StructuralRole, AllowsLambdaRole):
    __slots__ = ()
    _role_name = 'ON clause, typically a SQL expression or ORM relationship attribute'


class WhereHavingRole(OnClauseRole):
    __slots__ = ()
    _role_name = 'SQL expression for WHERE/HAVING role'


def ExpressionElementRole():
    '''ExpressionElementRole'''
    __slots__ = ()
    _role_name = 'SQL expression element'
    
    def label(self = None, name = None):
        raise NotImplementedError()


ExpressionElementRole = <NODE:27>(ExpressionElementRole, 'ExpressionElementRole', TypedColumnsClauseRole[_T_co])

def ConstExprRole():
    '''ConstExprRole'''
    __slots__ = ()
    _role_name = 'Constant True/False/None expression'

ConstExprRole = <NODE:27>(ConstExprRole, 'ConstExprRole', ExpressionElementRole[_T])

def LabeledColumnExprRole():
    '''LabeledColumnExprRole'''
    __slots__ = ()

LabeledColumnExprRole = <NODE:27>(LabeledColumnExprRole, 'LabeledColumnExprRole', ExpressionElementRole[_T])

def BinaryElementRole():
    '''BinaryElementRole'''
    __slots__ = ()
    _role_name = 'SQL expression element or literal value'

BinaryElementRole = <NODE:27>(BinaryElementRole, 'BinaryElementRole', ExpressionElementRole[_T])

class InElementRole(SQLRole):
    __slots__ = ()
    _role_name = 'IN expression list, SELECT construct, or bound parameter object'


class JoinTargetRole(StructuralRole, UsesInspection, AllowsLambdaRole):
    __slots__ = ()
    _role_name = 'Join target, typically a FROM expression, or ORM relationship attribute'


class FromClauseRole(JoinTargetRole, ColumnsClauseRole):
    __slots__ = ()
    _role_name = 'FROM expression, such as a Table or alias() object'
    named_with_column: 'bool' = False


class StrictFromClauseRole(FromClauseRole):
    __slots__ = ()


class AnonymizedFromClauseRole(StrictFromClauseRole):
    __slots__ = ()
    if TYPE_CHECKING:
        
        def _anonymous_fromclause(self = None, *, name, flat):
            pass

        return None


class ReturnsRowsRole(SQLRole):
    __slots__ = ()
    _role_name = 'Row returning expression such as a SELECT, a FROM clause, or an INSERT/UPDATE/DELETE with RETURNING'


class StatementRole(SQLRole):
    __slots__ = ()
    _role_name = 'Executable SQL or text() construct'
    if TYPE_CHECKING:
        _propagate_attrs = (lambda self = None: pass)()
        return None
    _propagate_attrs = None.EMPTY_DICT


class SelectStatementRole(ReturnsRowsRole, StatementRole):
    __slots__ = ()
    _role_name = 'SELECT construct or equivalent text() construct'
    
    def subquery(self = None):
        raise NotImplementedError('All SelectStatementRole objects should implement a .subquery() method.')



class HasCTERole(ReturnsRowsRole):
    __slots__ = ()


class IsCTERole(SQLRole):
    __slots__ = ()
    _role_name = 'CTE object'


class CompoundElementRole(SQLRole, AllowsLambdaRole):
    '''SELECT statements inside a CompoundSelect, e.g. UNION, EXTRACT, etc.'''
    __slots__ = ()
    _role_name = 'SELECT construct for inclusion in a UNION or other set construct'


class DMLRole(StatementRole):
    __slots__ = ()


class DMLTableRole(FromClauseRole):
    __slots__ = ()
    _role_name = 'subject table for an INSERT, UPDATE or DELETE'


class DMLColumnRole(SQLRole):
    __slots__ = ()
    _role_name = 'SET/VALUES column expression or string key'


class DMLSelectRole(SQLRole):
    '''A SELECT statement embedded in DML, typically INSERT from SELECT'''
    __slots__ = ()
    _role_name = 'SELECT statement or equivalent textual object'


class DDLRole(StatementRole):
    __slots__ = ()


class DDLExpressionRole(StructuralRole):
    __slots__ = ()
    _role_name = 'SQL expression element for DDL constraint'


class DDLConstraintColumnRole(SQLRole):
    __slots__ = ()
    _role_name = 'String column name or column expression for DDL constraint'


class DDLReferredColumnRole(DDLConstraintColumnRole):
    __slots__ = ()
    _role_name = 'String column name or Column object for DDL foreign key constraint'
