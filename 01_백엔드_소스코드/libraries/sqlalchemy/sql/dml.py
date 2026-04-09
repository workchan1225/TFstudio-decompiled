# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dml.pyc (Python 3.11)

'''
Provide :class:`_expression.Insert`, :class:`_expression.Update` and
:class:`_expression.Delete`.

'''
from __future__ import annotations
from collections.abc import abc as collections_abc
import operator
from typing import Any
from typing import cast
from typing import Dict
from typing import Iterable
from typing import List
from typing import MutableMapping
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import coercions
from  import roles
from  import util as sql_util
from _typing import _TP
from _typing import _unexpected_kw
from _typing import is_column_element
from _typing import is_named_from_clause
from base import _entity_namespace_key
from base import _exclusive_against
from base import _from_objects
from base import _generative
from base import _select_iterables
from base import ColumnCollection
from base import ColumnSet
from base import CompileState
from base import DialectKWArgs
from base import Executable
from base import Generative
from base import HasCompileState
from elements import BooleanClauseList
from elements import ClauseElement
from elements import ColumnClause
from elements import ColumnElement
from elements import Null
from selectable import Alias
from selectable import ExecutableReturnsRows
from selectable import FromClause
from selectable import HasCTE
from selectable import HasPrefixes
from selectable import Join
from selectable import SelectLabelStyle
from selectable import TableClause
from selectable import TypedReturnsRows
from sqltypes import NullType
from visitors import InternalTraversal
from  import exc
from  import util
from util.typing import Self
from util.typing import TypeGuard
if TYPE_CHECKING:
    from _typing import _ColumnExpressionArgument
    from _typing import _ColumnsClauseArgument
    from _typing import _DMLColumnArgument
    from _typing import _DMLColumnKeyMapping
    from _typing import _DMLTableArgument
    from _typing import _T0
    from _typing import _T1
    from _typing import _T2
    from _typing import _T3
    from _typing import _T4
    from _typing import _T5
    from _typing import _T6
    from _typing import _T7
    from _typing import _TypedColumnClauseArgument as _TCCA
    from base import ReadOnlyColumnCollection
    from compiler import SQLCompiler
    from elements import KeyedColumnElement
    from selectable import _ColumnsClauseElement
    from selectable import _SelectIterable
    from selectable import Select
    from selectable import Selectable
    
    def isupdate(dml = None):
        pass

    
    def isdelete(dml = None):
        pass

    
    def isinsert(dml = None):
        pass

else:
    isupdate = operator.attrgetter('isupdate')
    isdelete = operator.attrgetter('isdelete')
    isinsert = operator.attrgetter('isinsert')
_T = TypeVar('_T', bound = Any)
_DMLColumnElement = Union[(str, ColumnClause[Any])]
_DMLTableElement = Union[(TableClause, Alias, Join)]

class DMLState(CompileState):
    _no_parameters = True
    _dict_parameters: 'Optional[MutableMapping[_DMLColumnElement, Any]]' = None
    _multi_parameters: 'Optional[List[MutableMapping[_DMLColumnElement, Any]]]' = None
    _ordered_values: 'Optional[List[Tuple[_DMLColumnElement, Any]]]' = None
    _primary_table: 'FromClause' = None
    _supports_implicit_returning = True
    isupdate = False
    isdelete = False
    statement: 'UpdateBase' = False
    
    def __init__(self = None, statement = None, compiler = None, **kw):
        raise NotImplementedError()

    get_entity_description = (lambda cls = None, statement = None: {
'name': statement.table.name if is_named_from_clause(statement.table) else None,
'table': statement.table })()
    get_returning_column_descriptions = (lambda cls = None, statement = None: statement._all_selected_columns())()
    dml_table = (lambda self = None: self.statement.table)()
    if TYPE_CHECKING:
        get_plugin_class = (lambda cls = None, statement = None: pass)()
    _get_multi_crud_kv_pairs = (lambda cls = None, statement = None, multi_kv_iterator = classmethod: multi_kv_iterator())()
    _get_crud_kv_pairs = (lambda cls = None, statement = None, kv_iterator = classmethod, needs_to_be_cacheable = ('statement', 'UpdateBase', 'kv_iterator', 'Iterable[Tuple[_DMLColumnArgument, Any]]', 'needs_to_be_cacheable', 'bool', 'return', 'List[Tuple[_DMLColumnElement, Any]]'): pass# WARNING: Decompyle incomplete
)()
    
    def _make_extra_froms(self = None, statement = None):
        froms = []
        all_tables = list(sql_util.tables_from_leftmost(statement.table))
        primary_table = all_tables[0]
        seen = {
            primary_table}
        consider = statement._where_criteria
        if self._dict_parameters:
            consider += tuple(self._dict_parameters.values())
        for crit in consider:
            for item in _from_objects(crit):
                if not seen.intersection(item._cloned_set):
                    froms.append(item)
                seen.update(item._cloned_set)
                froms.extend(all_tables[1:])
                return (primary_table, froms)

    
    def _process_values(self = None, statement = None):
        if self._no_parameters:
            self._dict_parameters = statement._values
            self._no_parameters = False
            return None

    
    def _process_select_values(self = None, statement = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _no_multi_values_supported(self = None, statement = None):
        raise exc.InvalidRequestError('%s construct does not support multiple parameter sets.' % statement.__visit_name__.upper())

    
    def _cant_mix_formats_error(self = None):
        raise exc.InvalidRequestError("Can't mix single and multiple VALUES formats in one INSERT statement; one style appends to a list while the other replaces values, so the intent is ambiguous.")


InsertDMLState = <NODE:12>()
UpdateDMLState = <NODE:12>()
DeleteDMLState = <NODE:12>()

class UpdateBase(ClauseElement, ExecutableReturnsRows, Generative, HasPrefixes, DialectKWArgs, HasCompileState, HasCTE, roles.DMLRole):
    '''Form the base for ``INSERT``, ``UPDATE``, and ``DELETE`` statements.'''
    __visit_name__ = 'update_base'
    _hints: 'util.immutabledict[Tuple[_DMLTableElement, str], str]' = util.EMPTY_DICT
    named_with_column = False
    table: '_DMLTableElement' = SelectLabelStyle.LABEL_STYLE_DISAMBIGUATE_ONLY
    _return_defaults = False
    _return_defaults_columns: 'Optional[Tuple[_ColumnsClauseElement, ...]]' = None
    _supplemental_returning: 'Optional[Tuple[_ColumnsClauseElement, ...]]' = None
    _returning: 'Tuple[_ColumnsClauseElement, ...]' = ()
    is_dml = True
    
    def _generate_fromclause_column_proxies(self, fromclause = None, columns = None, primary_key = None, foreign_keys = ('fromclause', 'FromClause', 'columns', 'ColumnCollection[str, KeyedColumnElement[Any]]', 'primary_key', 'ColumnSet', 'foreign_keys', 'Set[KeyedColumnElement[Any]]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def params(self = None, *arg, **kw):
        '''Set the parameters for the statement.

        This method raises ``NotImplementedError`` on the base class,
        and is overridden by :class:`.ValuesBase` to provide the
        SET/VALUES clause of UPDATE and INSERT.

        '''
        raise NotImplementedError('params() is not supported for INSERT/UPDATE/DELETE statements. To set the values for an INSERT or UPDATE statement, use stmt.values(**parameters).')

    with_dialect_options = (lambda self = None: self._validate_dialect_kwargs(opt)self)()
    return_defaults = (lambda self = None, *, supplemental_cols: self._return_defaults = Trueif sort_by_parameter_order:
if not self.is_insert:
raise exc.ArgumentError("The 'sort_by_parameter_order' argument to return_defaults() only applies to INSERT statements")self._sort_by_parameter_order = True# WARNING: Decompyle incomplete
)()
    
    def is_derived_from(self = None, fromclause = None):
        """Return ``True`` if this :class:`.ReturnsRows` is
        'derived' from the given :class:`.FromClause`.

        Since these are DMLs, we dont want such statements ever being adapted
        so we return False for derives.

        """
        return False

    returning = (lambda self = None, *, sort_by_parameter_order: if _UpdateBase__kw:
raise _unexpected_kw('UpdateBase.returning()', _UpdateBase__kw)if self._return_defaults:
raise exc.InvalidRequestError('return_defaults() is already configured on this statement')if sort_by_parameter_order:
if not self.is_insert:
raise exc.ArgumentError("The 'sort_by_parameter_order' argument to returning() only applies to INSERT statements")True = None, tuple += (lambda .0: pass# WARNING: Decompyle incomplete
)(cols()), ._returning
        return self
)()
    
    def corresponding_column(self = None, column = None, require_embedded = None):
        return self.exported_columns.corresponding_column(column, require_embedded = require_embedded)

    _all_selected_columns = (lambda self = None: _select_iterables(self._returning)())()
    exported_columns = (lambda self = None: (lambda .0: pass# WARNING: Decompyle incomplete
)(self._all_selected_columns()).as_readonly()
)()
    with_hint = (lambda self = None, text = None, selectable = _generative, dialect_name = (None, '*'): pass# WARNING: Decompyle incomplete
)()
    entity_description = (lambda self = None: meth = DMLState.get_plugin_class(self).get_entity_descriptionmeth(self))()
    returning_column_descriptions = (lambda self = None: meth = DMLState.get_plugin_class(self).get_returning_column_descriptionsmeth(self))()


class ValuesBase(UpdateBase):
    '''Supplies support for :meth:`.ValuesBase.values` to
    INSERT and UPDATE constructs.'''
    __visit_name__ = 'values_base'
    _supports_multi_parameters = False
    select: 'Optional[Select[Any]]' = None
    _post_values_clause: 'Optional[ClauseElement]' = None
    _values: 'Optional[util.immutabledict[_DMLColumnElement, Any]]' = None
    _multi_values: 'Tuple[Union[Sequence[Dict[_DMLColumnElement, Any]], Sequence[Sequence[Any]]], ...]' = ()
    _ordered_values: 'Optional[List[Tuple[_DMLColumnElement, Any]]]' = None
    _select_names: 'Optional[List[str]]' = None
    _inline: 'bool' = False
    
    def __init__(self = None, table = None):
        self.table = coercions.expect(roles.DMLTableRole, table, apply_propagate_attrs = self)

    values = (lambda self = None: pass# WARNING: Decompyle incomplete
)()()


class Insert(ValuesBase):
    pass
# WARNING: Decompyle incomplete


def ReturningInsert():
    '''ReturningInsert'''
    __doc__ = 'Typing-only class that establishes a generic type form of\n    :class:`.Insert` which tracks returned column types.\n\n    This datatype is delivered when calling the\n    :meth:`.Insert.returning` method.\n\n    .. versionadded:: 2.0\n\n    '

ReturningInsert = <NODE:27>(ReturningInsert, 'ReturningInsert', Insert, TypedReturnsRows[_TP])

class DMLWhereBase:
    table: '_DMLTableElement' = 'DMLWhereBase'
    _where_criteria: 'Tuple[ColumnElement[Any], ...]' = ()
    where = (lambda self = None: for criterion in whereclause:
where_criteria = coercions.expect(roles.WhereHavingRole, criterion, apply_propagate_attrs = self)self)()
    
    def filter(self = None, *criteria):
        '''A synonym for the :meth:`_dml.DMLWhereBase.where` method.

        .. versionadded:: 1.4

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _filter_by_zero(self = None):
        return self.table

    
    def filter_by(self = None, **kwargs):
        '''apply the given filtering criterion as a WHERE clause
        to this select.

        '''
        pass
    # WARNING: Decompyle incomplete

    whereclause = (lambda self = None: BooleanClauseList._construct_for_whereclause(self._where_criteria))()


class Update(ValuesBase, DMLWhereBase):
    pass
# WARNING: Decompyle incomplete


def ReturningUpdate():
    '''ReturningUpdate'''
    __doc__ = 'Typing-only class that establishes a generic type form of\n    :class:`.Update` which tracks returned column types.\n\n    This datatype is delivered when calling the\n    :meth:`.Update.returning` method.\n\n    .. versionadded:: 2.0\n\n    '

ReturningUpdate = <NODE:27>(ReturningUpdate, 'ReturningUpdate', Update, TypedReturnsRows[_TP])

class Delete(UpdateBase, DMLWhereBase):
    '''Represent a DELETE construct.

    The :class:`_expression.Delete` object is created using the
    :func:`_expression.delete()` function.

    '''
    __visit_name__ = 'delete'
    is_delete = True
    _traverse_internals = [
        ('table', InternalTraversal.dp_clauseelement),
        ('_where_criteria', InternalTraversal.dp_clauseelement_tuple),
        ('_returning', InternalTraversal.dp_clauseelement_tuple),
        ('_hints', InternalTraversal.dp_table_hint_list)] + HasPrefixes._has_prefixes_traverse_internals + DialectKWArgs._dialect_kwargs_traverse_internals + Executable._executable_traverse_internals + HasCTE._has_ctes_traverse_internals
    
    def __init__(self = None, table = None):
        self.table = coercions.expect(roles.DMLTableRole, table, apply_propagate_attrs = self)

    if TYPE_CHECKING:
        returning = (lambda self = None, _Delete__ent0 = None: pass)()
        returning = (lambda self = None, _Delete__ent0 = None, _Delete__ent1 = overload: pass)()
        returning = (lambda self = None, _Delete__ent0 = None, _Delete__ent1 = overload, _Delete__ent2 = ('_Delete__ent0', '_TCCA[_T0]', '_Delete__ent1', '_TCCA[_T1]', '_Delete__ent2', '_TCCA[_T2]', 'return', 'ReturningDelete[Tuple[_T0, _T1, _T2]]'): pass)()
        returning = (lambda self, _Delete__ent0 = None, _Delete__ent1 = None, _Delete__ent2 = overload, _Delete__ent3 = ('_Delete__ent0', '_TCCA[_T0]', '_Delete__ent1', '_TCCA[_T1]', '_Delete__ent2', '_TCCA[_T2]', '_Delete__ent3', '_TCCA[_T3]', 'return', 'ReturningDelete[Tuple[_T0, _T1, _T2, _T3]]'): pass)()
        returning = (lambda self, _Delete__ent0, _Delete__ent1 = None, _Delete__ent2 = None, _Delete__ent3 = overload, _Delete__ent4 = ('_Delete__ent0', '_TCCA[_T0]', '_Delete__ent1', '_TCCA[_T1]', '_Delete__ent2', '_TCCA[_T2]', '_Delete__ent3', '_TCCA[_T3]', '_Delete__ent4', '_TCCA[_T4]', 'return', 'ReturningDelete[Tuple[_T0, _T1, _T2, _T3, _T4]]'): pass)()
        returning = (lambda self, _Delete__ent0, _Delete__ent1, _Delete__ent2 = None, _Delete__ent3 = None, _Delete__ent4 = overload, _Delete__ent5 = ('_Delete__ent0', '_TCCA[_T0]', '_Delete__ent1', '_TCCA[_T1]', '_Delete__ent2', '_TCCA[_T2]', '_Delete__ent3', '_TCCA[_T3]', '_Delete__ent4', '_TCCA[_T4]', '_Delete__ent5', '_TCCA[_T5]', 'return', 'ReturningDelete[Tuple[_T0, _T1, _T2, _T3, _T4, _T5]]'): pass)()
        returning = (lambda self, _Delete__ent0, _Delete__ent1, _Delete__ent2, _Delete__ent3 = None, _Delete__ent4 = None, _Delete__ent5 = overload, _Delete__ent6 = ('_Delete__ent0', '_TCCA[_T0]', '_Delete__ent1', '_TCCA[_T1]', '_Delete__ent2', '_TCCA[_T2]', '_Delete__ent3', '_TCCA[_T3]', '_Delete__ent4', '_TCCA[_T4]', '_Delete__ent5', '_TCCA[_T5]', '_Delete__ent6', '_TCCA[_T6]', 'return', 'ReturningDelete[Tuple[_T0, _T1, _T2, _T3, _T4, _T5, _T6]]'): pass)()
        returning = (lambda self, _Delete__ent0, _Delete__ent1, _Delete__ent2, _Delete__ent3, _Delete__ent4 = None, _Delete__ent5 = None, _Delete__ent6 = overload, _Delete__ent7 = ('_Delete__ent0', '_TCCA[_T0]', '_Delete__ent1', '_TCCA[_T1]', '_Delete__ent2', '_TCCA[_T2]', '_Delete__ent3', '_TCCA[_T3]', '_Delete__ent4', '_TCCA[_T4]', '_Delete__ent5', '_TCCA[_T5]', '_Delete__ent6', '_TCCA[_T6]', '_Delete__ent7', '_TCCA[_T7]', 'return', 'ReturningDelete[Tuple[_T0, _T1, _T2, _T3, _T4, _T5, _T6, _T7]]'): pass)()
        returning = (lambda self = None: pass)()
        
        def returning(self = None, *cols, **_Delete__kw):
            pass

        return None


def ReturningDelete():
    '''ReturningDelete'''
    __doc__ = 'Typing-only class that establishes a generic type form of\n    :class:`.Delete` which tracks returned column types.\n\n    This datatype is delivered when calling the\n    :meth:`.Delete.returning` method.\n\n    .. versionadded:: 2.0\n\n    '

ReturningDelete = <NODE:27>(ReturningDelete, 'ReturningDelete', Update, TypedReturnsRows[_TP])
