# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: coercions.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as collections_abc
import numbers
import re
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import roles
from  import visitors
from _typing import is_from_clause
from base import ExecutableOption
from base import Options
from cache_key import HasCacheKey
from visitors import Visitable
from  import exc
from  import inspection
from  import util
from util.typing import Literal
if typing.TYPE_CHECKING:
    from  import elements
    from  import lambdas
    from  import schema
    from  import selectable
    from _typing import _ColumnExpressionArgument
    from _typing import _ColumnsClauseArgument
    from _typing import _DDLColumnArgument
    from _typing import _DMLTableArgument
    from _typing import _FromClauseArgument
    from dml import _DMLTableElement
    from elements import BindParameter
    from elements import ClauseElement
    from elements import ColumnClause
    from elements import ColumnElement
    from elements import NamedColumn
    from elements import SQLCoreOperations
    from elements import TextClause
    from schema import Column
    from selectable import _ColumnsClauseElement
    from selectable import _JoinTargetProtocol
    from selectable import FromClause
    from selectable import HasCTE
    from selectable import SelectBase
    from selectable import Subquery
    from visitors import _TraverseCallableType
_SR = TypeVar('_SR', bound = roles.SQLRole)
_F = TypeVar('_F', bound = Callable[(..., Any)])
_StringOnlyR = TypeVar('_StringOnlyR', bound = roles.StringRole)
_T = TypeVar('_T', bound = Any)

def _is_literal(element = None):
