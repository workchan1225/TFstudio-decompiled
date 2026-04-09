# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from typing import Any
from typing import TYPE_CHECKING
from _typing import ColumnExpressionArgument
from _typing import NotNullable
from _typing import Nullable
from base import Executable
from compiler import COLLECT_CARTESIAN_PRODUCTS
from compiler import FROM_LINTING
from compiler import NO_LINTING
from compiler import WARN_LINTING
from ddl import BaseDDLElement
from ddl import DDL
from ddl import DDLElement
from ddl import ExecutableDDLElement
from expression import Alias
from expression import alias
from expression import all_
from expression import and_
from expression import any_
from expression import asc
from expression import between
from expression import bindparam
from expression import case
from expression import cast
from expression import ClauseElement
from expression import collate
from expression import column
from expression import ColumnCollection
from expression import ColumnElement
from expression import CompoundSelect
from expression import cte
from expression import Delete
from expression import delete
from expression import desc
from expression import distinct
from expression import except_
from expression import except_all
from expression import exists
from expression import extract
from expression import false
from expression import False_
from expression import FromClause
from expression import func
from expression import funcfilter
from expression import Insert
from expression import insert
from expression import intersect
from expression import intersect_all
from expression import Join
from expression import join
from expression import label
from expression import LABEL_STYLE_DEFAULT
from expression import LABEL_STYLE_DISAMBIGUATE_ONLY
from expression import LABEL_STYLE_NONE
from expression import LABEL_STYLE_TABLENAME_PLUS_COL
from expression import lambda_stmt
from expression import LambdaElement
from expression import lateral
from expression import literal
from expression import literal_column
from expression import modifier
from expression import not_
from expression import null
from expression import nulls_first
from expression import nulls_last
from expression import nullsfirst
from expression import nullslast
from expression import or_
from expression import outerjoin
from expression import outparam
from expression import over
from expression import quoted_name
from expression import Select
from expression import select
from expression import Selectable
from expression import SelectLabelStyle
from expression import SQLColumnExpression
from expression import StatementLambdaElement
from expression import Subquery
from expression import table
from expression import TableClause
from expression import TableSample
from expression import tablesample
from expression import text
from expression import true
from expression import True_
from expression import try_cast
from expression import tuple_
from expression import type_coerce
from expression import union
from expression import union_all
from expression import Update
from expression import update
from expression import Values
from expression import values
from expression import within_group
from visitors import ClauseVisitor

def __go(lcls = None):
    _sa_util = util
    import 
    base = base
    import 
    coercions = coercions
    import 
    elements = elements
    import 
    lambdas = lambdas
    import 
    selectable = selectable
    import 
    schema = schema
    import 
    traversals = traversals
    import 
    type_api = type_api
    import 
    if not TYPE_CHECKING:
        base.coercions = coercions
        elements.coercions = coercions
        base.elements = elements
        base.type_api = type_api
        coercions.elements = elements
        coercions.lambdas = lambdas
        coercions.schema = schema
        coercions.selectable = selectable
    _prepare_annotations = _prepare_annotations
    import annotation
    Annotated = Annotated
    import annotation
    AnnotatedColumnElement = AnnotatedColumnElement
    import elements
    ClauseList = ClauseList
    import elements
    AnnotatedFromClause = AnnotatedFromClause
    import selectable
    _prepare_annotations(ColumnElement, AnnotatedColumnElement)
    _prepare_annotations(FromClause, AnnotatedFromClause)
    _prepare_annotations(ClauseList, Annotated)
    _sa_util.preloaded.import_prefix('sqlalchemy.sql')

__go(locals())
