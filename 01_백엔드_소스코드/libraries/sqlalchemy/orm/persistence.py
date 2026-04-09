# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: persistence.pyc (Python 3.11)

'''private module containing functions used to emit INSERT, UPDATE
and DELETE statements on behalf of a :class:`_orm.Mapper` and its descending
mappers.

The functions here are called only by the unit of work functions
in unitofwork.py.

'''
from __future__ import annotations
from itertools import chain
from itertools import groupby
from itertools import zip_longest
import operator
from  import attributes
from  import exc as orm_exc
from  import loading
from  import sync
from base import state_str
from  import exc as sa_exc
from  import future
from  import sql
from  import util
from engine import cursor as _cursor
from sql import operators
from sql.elements import BooleanClauseList
from sql.selectable import LABEL_STYLE_TABLENAME_PLUS_COL

def save_obj(base_mapper, states, uowtransaction, single = (False,)):
    '''Issue ``INSERT`` and/or ``UPDATE`` statements for a list
    of objects.

    This is called within the context of a UOWTransaction during a
    flush operation, given a list of states to be flushed.  The
    base mapper in an inheritance hierarchy handles the inserts/
    updates for all descendant mappers.

    '''
    if not single and base_mapper.batch:
        for state in _sort_states(base_mapper, states):
            save_obj(base_mapper, [
                state], uowtransaction, single = True)
            return None
            states_to_update = []
            states_to_insert = []
            for state, dict_, mapper, connection, has_identity, row_switch, update_version_id in _organize_states_for_save(base_mapper, states, uowtransaction):
                if has_identity or row_switch:
                    states_to_update.append((state, dict_, mapper, connection, update_version_id))
                    continue
                states_to_insert.append((state, dict_, mapper, connection))
                for table, mapper in base_mapper._sorted_tables.items():
                    if table not in mapper._pks_by_table:
                        continue
                    insert = _collect_insert_commands(table, states_to_insert)
                    update = _collect_update_commands(uowtransaction, table, states_to_update)
                    _emit_update_statements(base_mapper, uowtransaction, mapper, table, update)
                    _emit_insert_statements(base_mapper, uowtransaction, mapper, table, insert)
                    
                    def <genexpr>(.0):
                        pass
                    # WARNING: Decompyle incomplete

                    
                    def <genexpr>(.0):
                        pass
                    # WARNING: Decompyle incomplete

                    None(chain, <genexpr>, states_to_insert()(<genexpr>, states_to_update()))
                    return None


def post_update(base_mapper, states, uowtransaction, post_update_cols):
    '''Issue UPDATE statements on behalf of a relationship() which
    specifies post_update.

    '''
    pass
# WARNING: Decompyle incomplete


def delete_obj(base_mapper, states, uowtransaction):
    '''Issue ``DELETE`` statements for a list of objects.

    This is called within the context of a UOWTransaction during a
    flush operation.

    '''
    states_to_delete = list(_organize_states_for_delete(base_mapper, states, uowtransaction))
    table_to_mapper = base_mapper._sorted_tables
    for table in reversed(list(table_to_mapper.keys())):
        mapper = table_to_mapper[table]
        if table not in mapper._pks_by_table:
            continue
        if mapper.inherits and mapper.passive_deletes:
            continue
        delete = _collect_delete_commands(base_mapper, uowtransaction, table, states_to_delete)
        _emit_delete_statements(base_mapper, uowtransaction, mapper, table, delete)
        for state, state_dict, mapper, connection, update_version_id in states_to_delete:
            mapper.dispatch.after_delete(mapper, connection, state)
            return None


def _organize_states_for_save(base_mapper, states, uowtransaction):
    '''Make an initial pass across a set of states for INSERT or
    UPDATE.

    This includes splitting out into distinct lists for
    each, calling before_insert/before_update, obtaining
    key information for each state including its dictionary,
    mapper, the connection to use for the execution per state,
    and the identity flag.

    '''
    pass
# WARNING: Decompyle incomplete


def _organize_states_for_post_update(base_mapper, states, uowtransaction):
    '''Make an initial pass across a set of states for UPDATE
    corresponding to post_update.

    This includes obtaining key information for each state
    including its dictionary, mapper, the connection to use for
    the execution per state.

    '''
    return _connections_for_states(base_mapper, uowtransaction, states)


def _organize_states_for_delete(base_mapper, states, uowtransaction):
    '''Make an initial pass across a set of states for DELETE.

    This includes calling out before_delete and obtaining
    key information for each state including its dictionary,
    mapper, the connection to use for the execution per state.

    '''
    pass
# WARNING: Decompyle incomplete


def _collect_insert_commands(table = None, states_to_insert = {
    'bulk': False,
    'return_defaults': False,
    'render_nulls': False,
    'include_bulk_keys': () }, *, bulk, return_defaults, render_nulls, include_bulk_keys):
    '''Identify sets of values to use in INSERT statements for a
    list of states.

    '''
    pass
# WARNING: Decompyle incomplete


def _collect_update_commands(uowtransaction, table = None, states_to_update = {
    'bulk': False,
    'use_orm_update_stmt': None,
    'include_bulk_keys': () }, *, bulk, use_orm_update_stmt, include_bulk_keys):
    '''Identify sets of values to use in UPDATE statements for a
    list of states.

    This function works intricately with the history system
    to determine exactly what values should be updated
    as well as how the row should be matched within an UPDATE
    statement.  Includes some tricky scenarios where the primary
    key of an object might have been changed.

    '''
    pass
# WARNING: Decompyle incomplete


def _collect_post_update_commands(base_mapper, uowtransaction, table, states_to_update, post_update_cols):
    '''Identify sets of values to use in UPDATE statements for a
    list of states within a post_update operation.

    '''
    pass
# WARNING: Decompyle incomplete


def _collect_delete_commands(base_mapper, uowtransaction, table, states_to_delete):
    '''Identify values to use in DELETE statements for a list of
    states to be deleted.'''
    pass
# WARNING: Decompyle incomplete


def _emit_update_statements(base_mapper, uowtransaction, mapper, table = None, update = {
    'bookkeeping': True,
    'use_orm_update_stmt': None,
    'enable_check_rowcount': True }, *, bookkeeping, use_orm_update_stmt, enable_check_rowcount):
    '''Emit UPDATE statements corresponding to value lists collected
    by _collect_update_commands().'''
    pass
# WARNING: Decompyle incomplete


def _emit_insert_statements(base_mapper, uowtransaction, mapper, table = None, insert = {
    'bookkeeping': True,
    'use_orm_insert_stmt': None,
    'execution_options': None }, *, bookkeeping, use_orm_insert_stmt, execution_options):
    '''Emit INSERT statements corresponding to value lists collected
    by _collect_insert_commands().'''
    pass
# WARNING: Decompyle incomplete


def _emit_post_update_statements(base_mapper, uowtransaction, mapper, table, update):
    '''Emit UPDATE statements corresponding to value lists collected
    by _collect_post_update_commands().'''
    pass
# WARNING: Decompyle incomplete


def _emit_delete_statements(base_mapper, uowtransaction, mapper, table, delete):
    '''Emit DELETE statements corresponding to value lists collected
    by _collect_delete_commands().'''
    pass
# WARNING: Decompyle incomplete


def _finalize_insert_update_commands(base_mapper, uowtransaction, states):
    '''finalize state on states that have been inserted or updated,
    including calling after_insert/after_update events.

    '''
    pass
# WARNING: Decompyle incomplete


def _postfetch_post_update(mapper, uowtransaction, table, state, dict_, result, params):
    pass
# WARNING: Decompyle incomplete


def _postfetch(mapper, uowtransaction, table, state, dict_, result, params, value_params, isupdate, returned_defaults):
    '''Expire attributes in need of newly persisted database state,
    after an INSERT or UPDATE statement has proceeded for that
    state.'''
    pass
# WARNING: Decompyle incomplete


def _postfetch_bulk_save(mapper, dict_, table):
    for m, equated_pairs in mapper._table_to_equated[table]:
        sync.bulk_populate_inherit_keys(dict_, m, equated_pairs)
        return None


def _connections_for_states(base_mapper, uowtransaction, states):
    '''Return an iterator of (state, state.dict, mapper, connection).

    The states are sorted according to _sort_states, then paired
    with the connection they should be using for the given
    unit of work transaction.

    '''
    pass
# WARNING: Decompyle incomplete


def _sort_states(mapper, states):
    pending = set(states)
    persistent = pending()
    pending.difference_update(persistent)
    
    try:
        persistent_sorted = sorted(persistent, key = mapper._persistent_sortkey_fn)
    except TypeError:
        err = None
        raise sa_exc.InvalidRequestError('Could not sort objects by primary key; primary key values must be sortable in Python (was: %s)' % err), err
        err = None
        del err

    return sorted(pending, key = operator.attrgetter('insert_order')) + persistent_sorted
