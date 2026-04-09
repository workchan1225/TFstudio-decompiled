# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bulk_persistence.pyc (Python 3.11)

'''additional ORM persistence classes related to "bulk" operations,
specifically outside of the flush() process.

'''
from __future__ import annotations
from typing import Any
from typing import cast
from typing import Dict
from typing import Iterable
from typing import Optional
from typing import overload
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import attributes
from  import context
from  import evaluator
from  import exc as orm_exc
from  import loading
from  import persistence
from base import NO_VALUE
from context import AbstractORMCompileState
from context import FromStatement
from context import ORMFromStatementCompileState
from context import QueryContext
from  import exc as sa_exc
from  import util
from engine import Dialect
from engine import result as _result
from sql import coercions
from sql import dml
from sql import expression
from sql import roles
from sql import select
from sql import sqltypes
from sql.base import _entity_namespace_key
from sql.base import CompileState
from sql.base import Options
from sql.dml import DeleteDMLState
from sql.dml import InsertDMLState
from sql.dml import UpdateDMLState
from util import EMPTY_DICT
from util.typing import Literal
if TYPE_CHECKING:
    from _typing import DMLStrategyArgument
    from _typing import OrmExecuteOptionsParameter
    from _typing import SynchronizeSessionArgument
    from mapper import Mapper
    from session import _BindArguments
    from session import ORMExecuteState
    from session import Session
    from session import SessionTransaction
    from state import InstanceState
    from engine import Connection
    from engine import cursor
    from engine.interfaces import _CoreAnyExecuteParams
_O = TypeVar('_O', bound = object)
_bulk_insert = (lambda mapper = None, mappings = None, session_transaction = None, *, isstates, return_defaults, render_nulls: pass)()
_bulk_insert = (lambda mapper = None, mappings = None, session_transaction = None, *, isstates, return_defaults, render_nulls: pass)()

def _bulk_insert(mapper = None, mappings = None, session_transaction = None, *, isstates, return_defaults, render_nulls, use_orm_insert_stmt, execution_options):
    pass
# WARNING: Decompyle incomplete

_bulk_update = (lambda mapper = None, mappings = None, session_transaction = None, *, isstates, update_changed_only, use_orm_update_stmt: pass)()
_bulk_update = (lambda mapper = None, mappings = None, session_transaction = None, *, isstates, update_changed_only, use_orm_update_stmt: pass)()

def _bulk_update(mapper = None, mappings = None, session_transaction = None, *, isstates, update_changed_only, use_orm_update_stmt, enable_check_rowcount):
    pass
# WARNING: Decompyle incomplete


def _expand_composites(mapper, mappings):
    pass
# WARNING: Decompyle incomplete


class ORMDMLState(AbstractORMCompileState):
    is_dml_returning = True
    from_statement_ctx: 'Optional[ORMFromStatementCompileState]' = None
    _get_orm_crud_kv_pairs = (lambda cls, mapper, statement, kv_iterator, needs_to_be_cacheable: pass# WARNING: Decompyle incomplete
)()
    _get_dml_plugin_subject = (lambda cls, statement: plugin_subject = statement.table._propagate_attrs.get('plugin_subject')if plugin_subject and plugin_subject.mapper or plugin_subject is not statement._propagate_attrs['plugin_subject']:
None)()
    _get_multi_crud_kv_pairs = (lambda cls, statement, kv_iterator: pass# WARNING: Decompyle incomplete
)()
    _get_crud_kv_pairs = (lambda cls, statement, kv_iterator, needs_to_be_cacheable: pass# WARNING: Decompyle incomplete
)()
    get_entity_description = (lambda cls, statement: ext_info = statement.table._annotations['parententity']mapper = ext_info.mapperif ext_info.is_aliased_class:
_label_name = ext_info.nameelse:
_label_name = mapper.class_.__name__{
'name': _label_name,
'type': mapper.class_,
'expr': ext_info.entity,
'entity': ext_info.entity,
'table': mapper.local_table })()
    get_returning_column_descriptions = (lambda cls, statement: pass# WARNING: Decompyle incomplete
)()
    
    def _setup_orm_returning(self, compiler, orm_level_statement, dml_level_statement = classmethod, dml_mapper = {
        'use_supplemental_cols': True }, *, use_supplemental_cols):
        '''establish ORM column handlers for an INSERT, UPDATE, or DELETE
        which uses explicit returning().

        called within compilation level create_for_statement.

        The _return_orm_returning() method then receives the Result
        after the statement was executed, and applies ORM loading to the
        state that we first established here.

        '''
        pass
    # WARNING: Decompyle incomplete

    _return_orm_returning = (lambda cls, session, statement, params, execution_options, bind_arguments, result: execution_context = result.contextcompile_state = execution_context.compiled.compile_stateif not compile_state.from_statement_ctx and compile_state.from_statement_ctx.compile_options._is_star:
load_options = execution_options.get('_sa_orm_load_options', QueryContext.default_load_options)querycontext = QueryContext(compile_state.from_statement_ctx, compile_state.select_statement, statement, params, session, load_options, execution_options, bind_arguments)loading.instances(result, querycontext))()


class BulkUDCompileState(ORMDMLState):
    
    class default_update_options(Options):
        _dml_strategy: 'DMLStrategyArgument' = 'auto'
        _synchronize_session: 'SynchronizeSessionArgument' = 'auto'
        _can_use_returning: 'bool' = False
        _is_delete_using: 'bool' = False
        _is_update_from: 'bool' = False
        _autoflush: 'bool' = True
        _subject_mapper: 'Optional[Mapper[Any]]' = None
        _resolved_values = EMPTY_DICT
        _eval_condition = None
        _matched_rows = None
        _identity_token = None
        _populate_existing: 'bool' = False

    can_use_returning = (lambda cls = None, dialect = None, mapper = None, *, is_multitable, is_update_from, is_delete_using: raise NotImplementedError())()
    orm_pre_session_exec = (lambda cls, session, statement, params, execution_options, bind_arguments, is_pre_event: (update_options, execution_options) = BulkUDCompileState.default_update_options.from_execution_options('_sa_orm_update_options', {
'autoflush',
'dml_strategy',
'identity_token',
'is_update_from',
'is_delete_using',
'populate_existing',
'synchronize_session'}, execution_options, statement._execution_options)bind_arguments['clause'] = statement# WARNING: Decompyle incomplete
)()
    orm_setup_cursor_result = (lambda cls, session, statement, params, execution_options, bind_arguments, result: update_options = execution_options['_sa_orm_update_options']if update_options._dml_strategy == 'orm':
if update_options._synchronize_session == 'evaluate':
cls._do_post_synchronize_evaluate(session, statement, result, update_options)elif update_options._synchronize_session == 'fetch':
cls._do_post_synchronize_fetch(session, statement, result, update_options)elif update_options._dml_strategy == 'bulk':
if update_options._synchronize_session == 'evaluate':
cls._do_post_synchronize_bulk_evaluate(session, params, result, update_options)resultcls._return_orm_returning(session, statement, params, execution_options, bind_arguments, result))()
    _adjust_for_extra_criteria = (lambda cls, global_attributes, ext_info: pass# WARNING: Decompyle incomplete
)()
    _interpret_returning_rows = (lambda cls, result, mapper, rows: pass# WARNING: Decompyle incomplete
)()
    _get_matched_objects_on_criteria = (lambda cls, update_options, states: pass# WARNING: Decompyle incomplete
)()
    _eval_condition_from_statement = (lambda cls, update_options, statement: mapper = update_options._subject_mappertarget_cls = mapper.class_evaluator_compiler = evaluator._EvaluatorCompiler(target_cls)crit = ()if statement._where_criteria:
crit += statement._where_criteriaglobal_attributes = { }for opt in statement._with_options:
if opt._is_criteria_option:
opt.get_global_criteria(global_attributes)if global_attributes:
crit += cls._adjust_for_extra_criteria(global_attributes, mapper)# WARNING: Decompyle incomplete
)()
    _do_pre_synchronize_auto = (lambda cls, session, statement, params, execution_options, bind_arguments, update_options: try:
eval_condition = cls._eval_condition_from_statement(update_options, statement)update_options + {
'_eval_condition': eval_condition,
'_synchronize_session': 'evaluate' }except evaluator.UnevaluatableError:
passupdate_options += {
'_synchronize_session': 'fetch' }cls._do_pre_synchronize_fetch(session, statement, params, execution_options, bind_arguments, update_options))()
    _do_pre_synchronize_evaluate = (lambda cls, session, statement, params, execution_options, bind_arguments, update_options: try:
eval_condition = cls._eval_condition_from_statement(update_options, statement)except evaluator.UnevaluatableError:
err = Noneraise sa_exc.InvalidRequestError('Could not evaluate current criteria in Python: "%s". Specify \'fetch\' or False for the synchronize_session execution option.' % err), errerr = Nonedel errupdate_options + {
'_eval_condition': eval_condition })()
    _get_resolved_values = (lambda cls, mapper, statement: if statement._multi_values:
[]if None._ordered_values:
list(statement._ordered_values)if None._values:
list(statement._values.items()))()
    _resolved_keys_as_propnames = (lambda cls, mapper, resolved_values: values = []for k, v in resolved_values:
if mapper and isinstance(k, expression.ColumnElement):
attr = mapper._columntoproperty[k]values.append((attr.key, v))continueexcept orm_exc.UnmappedColumnError:
continueraise sa_exc.InvalidRequestError("Attribute name not found, can't be synchronized back to objects: %r" % k)values)()
    _do_pre_synchronize_fetch = (lambda cls, session, statement, params, execution_options, bind_arguments, update_options: pass# WARNING: Decompyle incomplete
)()

BulkORMInsert = <NODE:12>()
BulkORMUpdate = <NODE:12>()
BulkORMDelete = <NODE:12>()
