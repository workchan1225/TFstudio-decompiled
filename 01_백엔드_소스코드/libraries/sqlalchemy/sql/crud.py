# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: crud.pyc (Python 3.11)

'''Functions used by compiler.py to determine the parameters rendered
within INSERT and UPDATE statements.

'''
from __future__ import annotations
import functools
import operator
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import Iterable
from typing import List
from typing import MutableMapping
from typing import NamedTuple
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import TYPE_CHECKING
from typing import Union
from  import coercions
from  import dml
from  import elements
from  import roles
from base import _DefaultDescriptionTuple
from dml import isinsert as _compile_state_isinsert
from elements import ColumnClause
from schema import default_is_clause_element
from schema import default_is_sequence
from selectable import Select
from selectable import TableClause
from  import exc
from  import util
from util.typing import Literal
if TYPE_CHECKING:
    from compiler import _BindNameForColProtocol
    from compiler import SQLCompiler
    from dml import _DMLColumnElement
    from dml import DMLState
    from dml import ValuesBase
    from elements import ColumnElement
    from elements import KeyedColumnElement
    from schema import _SQLExprDefault
    from schema import Column
REQUIRED = util.symbol('REQUIRED', '\nPlaceholder for the value within a :class:`.BindParameter`\nwhich is required to be present when the statement is passed\nto :meth:`_engine.Connection.execute`.\n\nThis symbol is typically used when a :func:`_expression.insert`\nor :func:`_expression.update` statement is compiled without parameter\nvalues present.\n\n')

def _as_dml_column(c = None):
    if not isinstance(c, ColumnClause):
        raise exc.CompileError(f'''Can\'t create DML statement against column expression {c!r}''')
    return c

_CrudParamElement = Tuple[('ColumnElement[Any]', str, Optional[Union[(str, '_SQLExprDefault')]], Iterable[str])]
_CrudParamElementStr = Tuple[('KeyedColumnElement[Any]', str, str, Iterable[str])]
_CrudParamElementSQLExpr = Tuple[('ColumnClause[Any]', str, '_SQLExprDefault', Iterable[str])]
_CrudParamSequence = List[_CrudParamElement]

class _CrudParams(NamedTuple):
    all_multi_params: 'List[Sequence[_CrudParamElementStr]]' = '_CrudParams'
    is_default_metavalue_only: 'bool' = False
    use_insertmanyvalues: 'bool' = False
    use_sentinel_columns: 'Optional[Sequence[Column[Any]]]' = None


def _get_crud_params(compiler = None, stmt = None, compile_state = None, toplevel = ('compiler', 'SQLCompiler', 'stmt', 'ValuesBase', 'compile_state', 'DMLState', 'toplevel', 'bool', 'kw', 'Any', 'return', '_CrudParams'), **kw):
    """create a set of tuples representing column/string pairs for use
    in an INSERT or UPDATE statement.

    Also generates the Compiled object's postfetch, prefetch, and
    returning column collections, used for default handling and ultimately
    populating the CursorResult's prefetch_cols() and postfetch_cols()
    collections.

    """
    pass
# WARNING: Decompyle incomplete

_create_bind_param = (lambda compiler, col, value = None, process = None, required = overload, name = (..., False, None, False), force_anonymous = ('compiler', 'SQLCompiler', 'col', 'ColumnElement[Any]', 'value', 'Any', 'process', 'Literal[True]', 'required', 'bool', 'name', 'Optional[str]', 'force_anonymous', 'bool', 'kw', 'Any', 'return', 'str'): pass)()
_create_bind_param = (lambda compiler = None, col = None, value = overload: pass)()

def _create_bind_param(compiler, col, value = None, process = None, required = None, name = (True, False, None, False), force_anonymous = ('compiler', 'SQLCompiler', 'col', 'ColumnElement[Any]', 'value', 'Any', 'process', 'bool', 'required', 'bool', 'name', 'Optional[str]', 'force_anonymous', 'bool', 'kw', 'Any', 'return', 'Union[str, elements.BindParameter[Any]]'), **kw):
    if force_anonymous:
        name = None
# WARNING: Decompyle incomplete


def _handle_values_anonymous_param(compiler, col, value, name, **kw):
    is_cte = 'visiting_cte' in kw
    if is_cte and value.unique and isinstance(value.key, elements._truncated_label):
        compiler.truncated_names[('bindparam', value.key)] = name
    if value.type._isnull:
        value = value._with_binary_element_type(col.type)
# WARNING: Decompyle incomplete


def _key_getters_for_crud_column(compiler = None, stmt = None, compile_state = None):
    pass
# WARNING: Decompyle incomplete


def _scan_insert_from_select_cols(compiler, stmt, compile_state, parameters, _getattr_col_key, _column_as_key, _col_bind_name, check_columns, values, toplevel, kw):
    pass
# WARNING: Decompyle incomplete


def _scan_cols(compiler, stmt, compile_state, parameters, _getattr_col_key, _column_as_key, _col_bind_name, check_columns, values, toplevel, kw):
    pass
# WARNING: Decompyle incomplete


def _setup_delete_return_defaults(compiler, stmt, compile_state, parameters, _getattr_col_key, _column_as_key, _col_bind_name, check_columns, values, toplevel, kw):
    pass
# WARNING: Decompyle incomplete


def _append_param_parameter(compiler, stmt, compile_state, c, col_key, parameters, _col_bind_name, implicit_returning, implicit_return_defaults, postfetch_lastrowid, values, autoincrement_col, insert_null_pk_still_autoincrements, kw):
    value = parameters.pop(col_key)
    has_visiting_cte = kw.get('visiting_cte') is not None
    col_value = compiler.preparer.format_column(c, use_table = compile_state.include_table_with_column_exprs)
    accumulated_bind_names = set()
# WARNING: Decompyle incomplete


def _append_param_insert_pk_returning(compiler, stmt, c, values, kw):
    '''Create a primary key expression in the INSERT statement where
    we want to populate result.inserted_primary_key and RETURNING
    is available.

    '''
    pass
# WARNING: Decompyle incomplete


def _append_param_insert_pk_no_returning(compiler, stmt, c, values, kw):
    '''Create a primary key expression in the INSERT statement where
    we want to populate result.inserted_primary_key and we cannot use
    RETURNING.

    Depending on the kind of default here we may create a bound parameter
    in the INSERT statement and pre-execute a default generation function,
    or we may use cursor.lastrowid if supported by the dialect.


    '''
    pass
# WARNING: Decompyle incomplete


def _append_param_insert_hasdefault(compiler, stmt, c, implicit_return_defaults, values, kw):
    pass
# WARNING: Decompyle incomplete


def _append_param_insert_select_hasdefault(compiler, stmt = None, c = None, values = None, kw = ('compiler', 'SQLCompiler', 'stmt', 'ValuesBase', 'c', 'ColumnClause[Any]', 'values', 'List[_CrudParamElementSQLExpr]', 'kw', 'Dict[str, Any]', 'return', 'None')):
    if default_is_sequence(c.default):
        if compiler.dialect.supports_sequences:
            if not c.default.optional or compiler.dialect.sequences_optional:
                values.append((c, compiler.preparer.format_column(c), c.default.next_value(), ()))
                return None
            return None
        return None
    if None(c.default):
        values.append((c, compiler.preparer.format_column(c), c.default.arg.self_group(), ()))
        return None
# WARNING: Decompyle incomplete


def _append_param_update(compiler, compile_state, stmt, c, implicit_return_defaults, values, kw):
    include_table = compile_state.include_table_with_column_exprs
# WARNING: Decompyle incomplete

_create_insert_prefetch_bind_param = (lambda compiler = None, c = None, process = overload: pass)()
_create_insert_prefetch_bind_param = (lambda compiler = None, c = None, process = overload: pass)()

def _create_insert_prefetch_bind_param(compiler = None, c = None, process = None, name = (True, None), **kw):
    pass
# WARNING: Decompyle incomplete

_create_update_prefetch_bind_param = (lambda compiler = None, c = None, process = overload: pass)()
_create_update_prefetch_bind_param = (lambda compiler = None, c = None, process = overload: pass)()

def _create_update_prefetch_bind_param(compiler = None, c = None, process = None, name = (True, None), **kw):
    pass
# WARNING: Decompyle incomplete


def _multiparam_column():
    '''_multiparam_column'''
    _is_multiparam_column = True
    
    def __init__(self, original, index):
        self.index = index
        self.key = '%s_m%d' % (original.key, index + 1)
        self.original = original
        self.default = original.default
        self.type = original.type

    
    def compare(self, other, **kw):
        raise NotImplementedError()

    
    def _copy_internals(self, **kw):
        raise NotImplementedError()

    
    def __eq__(self, other):
