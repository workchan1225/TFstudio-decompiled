# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: interpreter.pyc (Python 3.11)

import builtins
import collections
import dis
import operator
import logging
import textwrap
from numba.core import errors, ir, config
from numba.core.errors import NotDefinedError, UnsupportedBytecodeError, error_extras
from numba.core.ir_utils import get_definition, guard
from numba.core.utils import PYVERSION, BINOPS_TO_OPERATORS, INPLACE_BINOPS_TO_OPERATORS, _lazy_pformat
from numba.core.byteflow import Flow, AdaptDFA, AdaptCFA, BlockKind
from numba.core.unsafe import eh
from numba.cpython.unsafe.tuple import unpack_single_tuple
if PYVERSION in ((3, 12), (3, 13), (3, 14)):
    from numba.core.byteflow import CALL_INTRINSIC_1_Operand as ci1op
elif PYVERSION in ((3, 10), (3, 11)):
    pass
else:
    raise NotImplementedError(PYVERSION)

class _UNKNOWN_VALUE(object):
    '''Represents an unknown value, this is for ease of debugging purposes only.
    '''
    
    def __init__(self, varname):
        self._varname = varname

    
    def __repr__(self):
        return '_UNKNOWN_VALUE({})'.format(self._varname)


_logger = logging.getLogger(__name__)

class Assigner(object):
    """
    This object keeps track of potential assignment simplifications
    inside a code block.
    For example `$O.1 = x` followed by `y = $0.1` can be simplified
    into `y = x`, but it's not possible anymore if we have `x = z`
    in-between those two instructions.

    NOTE: this is not only an optimization, but is actually necessary
    due to certain limitations of Numba - such as only accepting the
    returning of an array passed as function argument.
    """
    
    def __init__(self):
        self.dest_to_src = { }
        self.src_invalidate = collections.defaultdict(list)
        self.unused_dests = set()

    
    def assign(self, srcvar, destvar):
        '''
        Assign *srcvar* to *destvar*. Return either *srcvar* or a possible
        simplified assignment source (earlier assigned to *srcvar*).
        '''
        srcname = srcvar.name
        destname = destvar.name
        if destname in self.src_invalidate:
            for d in self.src_invalidate.pop(destname):
                self.dest_to_src.pop(d)
                if srcname in self.dest_to_src:
                    srcvar = self.dest_to_src[srcname]
        if destvar.is_temp:
            self.dest_to_src[destname] = srcvar
            self.src_invalidate[srcname].append(destname)
            self.unused_dests.add(destname)
        return srcvar

    
    def get_assignment_source(self, destname):
        '''
        Get a possible assignment source (a ir.Var instance) to replace
        *destname*, otherwise None.
        '''
        if destname in self.dest_to_src:
            return self.dest_to_src[destname]
        None.unused_dests.discard(destname)



def _remove_assignment_definition(old_body, idx, func_ir, already_deleted_defs):
    '''
    Deletes the definition defined for old_body at index idx
    from func_ir. We assume this stmt will be deleted from
    new_body.

    In some optimizations we may update the same variable multiple times.
    In this situation, we only need to delete a particular definition once,
    this is tracked in already_deleted_def, which is a map from
    assignment name to the set of values that have already been
    deleted.
    '''
    lhs = old_body[idx].target.name
    rhs = old_body[idx].value
    if rhs in func_ir._definitions[lhs]:
        func_ir._definitions[lhs].remove(rhs)
        already_deleted_defs[lhs].add(rhs)
        return None
    if None not in already_deleted_defs[lhs]:
        raise UnsupportedBytecodeError('Inconsistency found in the definitions while executing a peephole optimization. This suggests an internal error or inconsistency elsewhere in the compiler.')


def _call_function_ex_replace_kws_small(old_body, keyword_expr, new_body, buildmap_idx, func_ir, already_deleted_defs):
    '''
    Extracts the kws args passed as varkwarg
    for CALL_FUNCTION_EX. This pass is taken when
    n_kws <= 15 and the bytecode looks like:

        # Start for each argument
        LOAD_FAST  # Load each argument.
        # End for each argument
        ...
        BUILD_CONST_KEY_MAP # Build a map

    In the generated IR, the varkwarg refers
    to a single build_map that contains all of the
    kws. In addition to returning the kws, this
    function updates new_body to remove all usage
    of the map.
    '''
    kws = keyword_expr.items.copy()
    value_indexes = keyword_expr.value_indexes
    for key, index in value_indexes.items():
        kws[index] = (key, kws[index][1])
        new_body[buildmap_idx] = None
        _remove_assignment_definition(old_body, buildmap_idx, func_ir, already_deleted_defs)
        return kws


def _call_function_ex_replace_kws_large(old_body, buildmap_name, buildmap_idx, search_end, new_body, func_ir, errmsg, already_deleted_defs):
    '''
    Extracts the kws args passed as varkwarg
    for CALL_FUNCTION_EX. This pass is taken when
    n_kws > 15 and the bytecode looks like:

        BUILD_MAP # Construct the map
        # Start for each argument
        LOAD_CONST # Load a constant for the name of the argument
        LOAD_FAST  # Load each argument.
        MAP_ADD # Append the (key, value) pair to the map
        # End for each argument

    In the IR generated, the initial build map is empty and a series
    of setitems are applied afterwards. THE IR looks like:

        $build_map_var = build_map(items=[])
        $constvar = const(str, ...) # create the const key
        # CREATE THE ARGUMENT, This may take multiple lines.
        $created_arg = ...
        $var = getattr(
            value=$build_map_var,
            attr=__setitem__,
        )
        $unused_var = call $var($constvar, $created_arg)

    We iterate through the IR, deleting all usages of the buildmap
    from the new_body, and adds the kws to a new kws list.
    '''
    new_body[buildmap_idx] = None
    _remove_assignment_definition(old_body, buildmap_idx, func_ir, already_deleted_defs)
    kws = []
    search_start = buildmap_idx + 1
# WARNING: Decompyle incomplete


def _call_function_ex_replace_args_small(old_body, tuple_expr, new_body, buildtuple_idx, func_ir, already_deleted_defs):
    '''
    Extracts the args passed as vararg
    for CALL_FUNCTION_EX. This pass is taken when
    n_args <= 30 and the bytecode looks like:

        # Start for each argument
        LOAD_FAST  # Load each argument.
        # End for each argument
        ...
        BUILD_TUPLE # Create a tuple of the arguments

    In the IR generated, the vararg refer
    to a single build_tuple that contains all of the
    args. In addition to returning the args, this
    function updates new_body to remove all usage
    of the tuple.
    '''
    new_body[buildtuple_idx] = None
    _remove_assignment_definition(old_body, buildtuple_idx, func_ir, already_deleted_defs)
    return tuple_expr.items


def _call_function_ex_replace_args_large(old_body, vararg_stmt, new_body, search_end, func_ir, errmsg, already_deleted_defs):
    '''
    Extracts the args passed as vararg
    for CALL_FUNCTION_EX. This pass is taken when
    n_args > 30 and the bytecode looks like:

        BUILD_TUPLE # Create a list to append to
        # Start for each argument
        LOAD_FAST  # Load each argument.
        LIST_APPEND # Add the argument to the list
        # End for each argument
        ...
        LIST_TO_TUPLE # Convert the args to a tuple.

    In the IR generated, the tuple is created by concatenating
    together several 1 element tuples to an initial empty tuple.
    We traverse backwards in the IR, collecting args, until we
    find the original empty tuple. For example, the IR might
    look like:

        $orig_tuple = build_tuple(items=[])
        $first_var = build_tuple(items=[Var(arg0, test.py:6)])
        $next_tuple = $orig_tuple + $first_var
        ...
        $final_var = build_tuple(items=[Var(argn, test.py:6)])
        $final_tuple = $prev_tuple + $final_var
        $varargs_var = $final_tuple
    '''
    search_start = 0
    total_args = []
    if isinstance(vararg_stmt, ir.Assign) and isinstance(vararg_stmt.value, ir.Var):
        target_name = vararg_stmt.value.name
        new_body[search_end] = None
        _remove_assignment_definition(old_body, search_end, func_ir, already_deleted_defs)
        search_end -= 1
    else:
        raise AssertionError('unreachable')
# WARNING: Decompyle incomplete


def peep_hole_call_function_ex_to_call_function_kw(func_ir):
    '''
    This peephole rewrites a bytecode sequence unique to Python 3.10
    where CALL_FUNCTION_EX is used instead of CALL_FUNCTION_KW because of
    stack limitations set by CPython. This limitation is imposed whenever
    a function call has too many arguments or keyword arguments.

    https://github.com/python/cpython/blob/a58ebcc701dd6c43630df941481475ff0f615a81/Python/compile.c#L55
    https://github.com/python/cpython/blob/a58ebcc701dd6c43630df941481475ff0f615a81/Python/compile.c#L4442

    In particular, this change is imposed whenever (n_args / 2) + n_kws > 15.

    Different bytecode is generated for args depending on if n_args > 30
    or n_args <= 30 and similarly if n_kws > 15 or n_kws <= 15.

    This function unwraps the *args and **kwargs in the function call
    and places these values directly into the args and kwargs of the call.
    '''
    errmsg = textwrap.dedent('\n        CALL_FUNCTION_EX with **kwargs not supported.\n        If you are not using **kwargs this may indicate that\n        you have a large number of kwargs and are using inlined control\n        flow. You can resolve this issue by moving the control flow out of\n        the function call. For example, if you have\n\n            f(a=1 if flag else 0, ...)\n\n        Replace that with:\n\n            a_val = 1 if flag else 0\n            f(a=a_val, ...)')
    already_deleted_defs = collections.defaultdict(set)
# WARNING: Decompyle incomplete


def peep_hole_list_to_tuple(func_ir):
    '''
    This peephole rewrites a bytecode sequence new to Python 3.9 that looks
    like e.g.:

    def foo(a):
        return (*a,)

    41          0 BUILD_LIST               0
                2 LOAD_FAST                0 (a)
                4 LIST_EXTEND              1
                6 LIST_TO_TUPLE
                8 RETURN_VAL

    essentially, the unpacking of tuples is written as a list which is appended
    to/extended and then "magicked" into a tuple by the new LIST_TO_TUPLE
    opcode.

    This peephole repeatedly analyses the bytecode in a block looking for a
    window between a `LIST_TO_TUPLE` and `BUILD_LIST` and...

    1. Turns the BUILD_LIST into a BUILD_TUPLE
    2. Sets an accumulator\'s initial value as the target of the BUILD_TUPLE
    3. Searches for \'extend\' on the original list and turns these into binary
       additions on the accumulator.
    4. Searches for \'append\' on the original list and turns these into a
       `BUILD_TUPLE` which is then appended via binary addition to the
       accumulator.
    5. Assigns the accumulator to the variable that exits the peephole and the
       rest of the block/code refers to as the result of the unpack operation.
    6. Patches up
    '''
    pass
# WARNING: Decompyle incomplete


def peep_hole_delete_with_exit(func_ir):
    '''
    This rewrite removes variables used to store the `__exit__` function
    loaded by SETUP_WITH.
    '''
    dead_vars = set()
    for blk in func_ir.blocks.values():
        for stmt in blk.body:
            used = set(stmt.list_vars())
            for v in used:
                if v.name.startswith('$setup_with_exitfn'):
                    dead_vars.add(v)
                if used & dead_vars and isinstance(stmt, ir.Assign):
                    dead_vars.add(stmt.target)
            new_body = []
            for stmt in blk.body:
                if not set(stmt.list_vars()) & dead_vars:
                    new_body.append(stmt)
                blk.body.clear()
                blk.body.extend(new_body)
                return func_ir


def peep_hole_fuse_dict_add_updates(func_ir):
    '''
    This rewrite removes d1._update_from_bytecode(d2)
    calls that are between two dictionaries, d1 and d2,
    in the same basic block. This pattern can appear as a
    result of Python 3.10 bytecode emission changes, which
    prevent large constant literal dictionaries
    (> 15 elements) from being constant. If both dictionaries
    are constant dictionaries defined in the same block and
    neither is used between the update call, then we replace d1
    with a new definition that combines the two dictionaries. At
    the bytecode translation stage we convert DICT_UPDATE into
    _update_from_bytecode, so we know that _update_from_bytecode
    always comes from the bytecode change and not user code.

    Python 3.10 may also rewrite the individual dictionaries
    as an empty build_map + many map_add. Here we again look
    for an _update_from_bytecode, and if so we replace these
    with a single constant dictionary.

    When running this algorithm we can always safely remove d2.

    This is the relevant section of the CPython 3.10 that causes
    this bytecode change:
    https://github.com/python/cpython/blob/3.10/Python/compile.c#L4048
    '''
    errmsg = textwrap.dedent('\n        A DICT_UPDATE op-code was encountered that could not be replaced.\n        If you have created a large constant dictionary, this may\n        be an an indication that you are using inlined control\n        flow. You can resolve this issue by moving the control flow out of\n        the dicitonary constructor. For example, if you have\n\n            d = {a: 1 if flag else 0, ...)\n\n        Replace that with:\n\n            a_val = 1 if flag else 0\n            d = {a: a_val, ...)')
    already_deleted_defs = collections.defaultdict(set)
    for blk in func_ir.blocks.values():
        new_body = []
        lit_map_def_idx = { }
        lit_map_use_idx = collections.defaultdict(list)
        map_updates = { }
        blk_changed = False
        for i, stmt in enumerate(blk.body):
            new_inst = stmt
            stmt_build_map_out = None
            if isinstance(stmt, ir.Assign) and isinstance(stmt.value, ir.Expr):
                if stmt.value.op == 'build_map':
                    stmt_build_map_out = stmt.target.name
                    lit_map_def_idx[stmt.target.name] = i
                    lit_map_use_idx[stmt.target.name].append(i)
                    map_updates[stmt.target.name] = stmt.value.items.copy()
                elif stmt.value.op == 'call' and i > 0:
                    func_name = stmt.value.func.name
                    getattr_stmt = blk.body[i - 1]
                    args = stmt.value.args
                    if isinstance(getattr_stmt, ir.Assign) and getattr_stmt.target.name == func_name and isinstance(getattr_stmt.value, ir.Expr) and getattr_stmt.value.op == 'getattr' and getattr_stmt.value.attr in ('__setitem__', '_update_from_bytecode'):
                        update_map_name = getattr_stmt.value.value.name
                        attr = getattr_stmt.value.attr
                        if attr == '__setitem__' and update_map_name in lit_map_use_idx:
                            map_updates[update_map_name].append(args)
                            lit_map_use_idx[update_map_name].extend([
                                i - 1,
                                i])
                        elif attr == '_update_from_bytecode':
                            d2_map_name = args[0].name
                            if update_map_name in lit_map_use_idx and d2_map_name in lit_map_use_idx:
                                map_updates[update_map_name].extend(map_updates[d2_map_name])
                                lit_map_use_idx[update_map_name].extend(lit_map_use_idx[d2_map_name])
                                lit_map_use_idx[update_map_name].append(i - 1)
                                for linenum in lit_map_use_idx[update_map_name]:
                                    _remove_assignment_definition(blk.body, linenum, func_ir, already_deleted_defs)
                                    new_body[linenum] = None
                                    del lit_map_def_idx[d2_map_name]
                                    del lit_map_use_idx[d2_map_name]
                                    del map_updates[d2_map_name]
                                    _remove_assignment_definition(blk.body, i, func_ir, already_deleted_defs)
                                    new_inst = _build_new_build_map(func_ir, update_map_name, blk.body, lit_map_def_idx[update_map_name], map_updates[update_map_name])
                                    lit_map_use_idx[update_map_name].clear()
                                    lit_map_use_idx[update_map_name].append(i)
                                    blk_changed = True
                            raise UnsupportedBytecodeError(errmsg)
            if not isinstance(stmt, ir.Assign) and isinstance(stmt.value, ir.Expr) and stmt.value.op == 'getattr' and stmt.value.value.name in lit_map_use_idx or stmt.value.attr in ('__setitem__', '_update_from_bytecode'):
                for var in stmt.list_vars():
                    if var.name in lit_map_use_idx and var.name != stmt_build_map_out:
                        del lit_map_def_idx[var.name]
                        del lit_map_use_idx[var.name]
                        del map_updates[var.name]
                    new_body.append(new_inst)
                    if blk_changed:
                        blk.body.clear()
                        (lambda .0: pass# WARNING: Decompyle incomplete
)(new_body())
        return func_ir


def peep_hole_split_at_pop_block(func_ir):
    '''
    Split blocks that contain ir.PopBlock.

    This rewrite restores the IR structure to pre 3.11 so that withlifting
    can work correctly.
    '''
    new_block_map = { }
    sorted_blocks = sorted(func_ir.blocks.items())
    for label, blk in enumerate(sorted_blocks):
        pop_block_locs = []
        for i, inst in enumerate(blk.body):
            if isinstance(inst, ir.PopBlock):
                pop_block_locs.append(i)
            if pop_block_locs:
                new_blocks = []
                for i in pop_block_locs:
                    before_blk = ir.Block(blk.scope, loc = blk.loc)
                    before_blk.body.extend(blk.body[:i])
                    new_blocks.append(before_blk)
                    popblk_blk = ir.Block(blk.scope, loc = blk.loc)
                    popblk_blk.body.append(blk.body[i])
                    new_blocks.append(popblk_blk)
                    prev_label = label
                    for newblk in new_blocks:
                        new_block_map[prev_label] = newblk
                        next_label = prev_label + 1
                        newblk.body.append(ir.Jump(next_label, loc = blk.loc))
                        prev_label = next_label
                        if blk_idx + 1 < len(sorted_blocks) and prev_label >= sorted_blocks[blk_idx + 1][0]:
                            raise errors.InternalError('POP_BLOCK peephole failed')
                        tail_blk = ir.Block(blk.scope, loc = blk.loc)
                        tail_blk.body.extend(blk.body[pop_block_locs[-1] + 1:])
                        new_block_map[prev_label] = tail_blk
                        func_ir.blocks.update(new_block_map)
                        return func_ir


def _build_new_build_map(func_ir, name, old_body, old_lineno, new_items):
    '''
    Create a new build_map with a new set of key/value items
    but all the other info the same.
    '''
    old_assign = old_body[old_lineno]
    old_target = old_assign.target
    old_bm = old_assign.value
    literal_keys = []
    values = []
    for pair in new_items:
        (k, v) = pair
        key_def = guard(get_definition, func_ir, k)
        if isinstance(key_def, (ir.Const, ir.Global, ir.FreeVar)):
            literal_keys.append(key_def.value)
        value_def = guard(get_definition, func_ir, v)
        if isinstance(value_def, (ir.Const, ir.Global, ir.FreeVar)):
            values.append(value_def.value)
            continue
        values.append(_UNKNOWN_VALUE(v.name))
        value_indexes = { }
        if len(literal_keys) == len(new_items):
            literal_value = zip(literal_keys, values)()
            for i, k in enumerate(literal_keys):
                value_indexes[k] = i
    literal_value = None
    new_bm = ir.Expr.build_map(items = new_items, size = len(new_items), literal_value = literal_value, value_indexes = value_indexes, loc = old_bm.loc)
    func_ir._definitions[name].append(new_bm)
    return ir.Assign(new_bm, ir.Var(old_target.scope, name, old_target.loc), new_bm.loc)


class Interpreter(object):
    __module__ = __name__
    __qualname__ = 'Interpreter'
    __doc__ = 'A bytecode interpreter that builds up the IR.\n    '
    _DEBUG_PRINT = False
    
    def __init__(self, func_id):
        self.func_id = func_id
        if self._DEBUG_PRINT:
            print(func_id.func)
        self.arg_count = func_id.arg_count
        self.arg_names = func_id.arg_names
        self.loc = ir.Loc.from_function_id(func_id)
        self.first_loc = ir.Loc.from_function_id(func_id)
        self.is_generator = func_id.is_generator
        self.blocks = { }
        self.definitions = collections.defaultdict(list)
        self._exception_vars = set()

    
    def interpret(self, bytecode):
        '''
        Generate IR for this bytecode.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def post_process(self, peepholes, func_ir):
        for peep in peepholes:
            func_ir = peep(func_ir)
            return func_ir

    
    def _end_try_blocks(self):
        """Closes all try blocks by inserting the required marker at the
        exception handler

        This is only needed for py3.11 because of the changes in exception
        handling. This merely maps the new py3.11 semantics back to the old way.

        What the code does:

        - For each block, compute the difference of blockstack to its incoming
          blocks' blockstack.
        - If the incoming blockstack has an extra TRY, the current block must
          be the EXCEPT block and we need to insert a marker.

        See also: _insert_try_block_end
        """
        pass
    # WARNING: Decompyle incomplete

    
    def _legalize_exception_vars(self):
        '''Search for unsupported use of exception variables.
        Note, they cannot be stored into user variable.
        '''
        excvars = self._exception_vars.copy()
        for varname, defnvars in self.definitions.items():
            for v in defnvars:
                if isinstance(v, ir.Var):
                    k = v.name
                    if k in excvars:
                        excvars.add(varname)
                uservar = list(filter((lambda x: not x.startswith('$')), excvars))
                if uservar:
                    first = uservar[0]
                    loc = self.current_scope.get(first).loc
                    msg = 'Exception object cannot be stored into variable ({}).'
                    raise errors.UnsupportedBytecodeError(msg.format(first), loc = loc)
                return None

    
    def init_first_block(self):
        for index, name in enumerate(self.arg_names):
            val = ir.Arg(index = index, name = name, loc = self.loc)
            self.store(val, name)
            return None

    
    def _iter_inst(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _start_new_block(self, offset):
        oldblock = self.current_block
        self.insert_block(offset)
        tryblk = self.dfainfo.active_try_block if self.dfainfo else None
    # WARNING: Decompyle incomplete

    
    def _end_current_block(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _inject_call(self, func, gv_name, res_name = (None,)):
