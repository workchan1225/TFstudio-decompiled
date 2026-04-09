# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ir_utils.pyc (Python 3.11)

import numpy
import math
import types as pytypes
import collections
import warnings
import numba
from numba.core.extending import _Intrinsic
from numba.core import types, typing, ir, analysis, postproc, rewrites, config
from numba.core.typing.templates import signature
from numba.core.analysis import compute_live_map, compute_use_defs, compute_cfg_from_blocks
from numba.core.errors import TypingError, UnsupportedError, NumbaPendingDeprecationWarning, CompilerError
import copy
_unique_var_count = 0

def mk_unique_var(prefix):
    global _unique_var_count
    var = prefix + '.' + str(_unique_var_count)
    _unique_var_count = _unique_var_count + 1
    return var


class _MaxLabel:
    
    def __init__(self, value = (0,)):
        self._value = value

    
    def next(self):
        return self._value

    
    def update(self, newval):
        self._value = max(newval, self._value)


_the_max_label = _MaxLabel()
del _MaxLabel

def get_unused_var_name(prefix, var_table):
    ''' Get a new var name with a given prefix and
        make sure it is unused in the given variable table.
    '''
    cur = 0
    var = prefix + str(cur)
    if var not in var_table:
        return var
    None += 1
    continue


def next_label():
    return _the_max_label.next()


def mk_alloc(typingctx, typemap, calltypes, lhs, size_var, dtype, scope, loc, lhs_typ):
    '''generate an array allocation with np.empty() and return list of nodes.
    size_var can be an int variable or tuple of int variables.
    lhs_typ is the type of the array being allocated.
    '''
    pass
# WARNING: Decompyle incomplete


def convert_size_to_var(size_var, typemap, scope, loc, nodes):
    if isinstance(size_var, int):
        new_size = ir.Var(scope, mk_unique_var('$alloc_size'), loc)
        if typemap:
            typemap[new_size.name] = types.intp
        size_assign = ir.Assign(ir.Const(size_var, loc), new_size, loc)
        nodes.append(size_assign)
        return new_size
# WARNING: Decompyle incomplete


def get_np_ufunc_typ(func, typingctx):
    '''get type of the incoming function

    Resolve using the context for target-awareness
    '''
    
    try:
        return typingctx.resolve_value_type(func)
    except TypingError:
        raise RuntimeError('type for func ', func, ' not found')



def mk_range_block(typemap, start, stop, step, calltypes, scope, loc):
    '''make a block that initializes loop range and iteration variables.
    target label in jump needs to be set.
    '''
    g_range_var = ir.Var(scope, mk_unique_var('$range_g_var'), loc)
    typemap[g_range_var.name] = get_global_func_typ(range)
    g_range = ir.Global('range', range, loc)
    g_range_assign = ir.Assign(g_range, g_range_var, loc)
    (arg_nodes, args) = _mk_range_args(typemap, start, stop, step, scope, loc)
    range_call = ir.Expr.call(g_range_var, args, (), loc)
    calltypes[range_call] = typemap[g_range_var.name].get_call_type(typing.Context(), [
        types.intp] * len(args), { })
    range_call_var = ir.Var(scope, mk_unique_var('$range_c_var'), loc)
    typemap[range_call_var.name] = types.iterators.RangeType(types.intp)
    range_call_assign = ir.Assign(range_call, range_call_var, loc)
    iter_call = ir.Expr.getiter(range_call_var, loc)
    if config.USE_LEGACY_TYPE_SYSTEM:
        calltype_sig = signature(types.range_iter64_type, types.range_state64_type)
    else:
        calltype_sig = signature(types.range_iter_type, types.range_state_type)
    calltypes[iter_call] = calltype_sig
    iter_var = ir.Var(scope, mk_unique_var('$iter_var'), loc)
    typemap[iter_var.name] = types.iterators.RangeIteratorType(types.intp)
    iter_call_assign = ir.Assign(iter_call, iter_var, loc)
    phi_var = ir.Var(scope, mk_unique_var('$phi'), loc)
    typemap[phi_var.name] = types.iterators.RangeIteratorType(types.intp)
    phi_assign = ir.Assign(iter_var, phi_var, loc)
    jump_header = ir.Jump(-1, loc)
    range_block = ir.Block(scope, loc)
    range_block.body = arg_nodes + [
        g_range_assign,
        range_call_assign,
        iter_call_assign,
        phi_assign,
        jump_header]
    return range_block


def _mk_range_args(typemap, start, stop, step, scope, loc):
    nodes = []
    if isinstance(stop, ir.Var):
        g_stop_var = stop
# WARNING: Decompyle incomplete


def get_global_func_typ(func):
    '''get type variable for func() from builtin registry'''
    for k, v in typing.templates.builtin_registry.globals:
        if k == func:
            
            return None, v
        raise RuntimeError('func type not found {}'.format(func))


def mk_loop_header(typemap, phi_var, calltypes, scope, loc):
    '''make a block that is a loop header updating iteration variables.
    target labels in branch need to be set.
    '''
    iternext_var = ir.Var(scope, mk_unique_var('$iternext_var'), loc)
    typemap[iternext_var.name] = types.containers.Pair(types.intp, types.boolean)
    iternext_call = ir.Expr.iternext(phi_var, loc)
    if config.USE_LEGACY_TYPE_SYSTEM:
        range_iter_type = types.range_iter64_type
    else:
        range_iter_type = types.range_iter_type
    calltypes[iternext_call] = signature(types.containers.Pair(types.intp, types.boolean), range_iter_type)
    iternext_assign = ir.Assign(iternext_call, iternext_var, loc)
    pair_first_var = ir.Var(scope, mk_unique_var('$pair_first_var'), loc)
    typemap[pair_first_var.name] = types.intp
    pair_first_call = ir.Expr.pair_first(iternext_var, loc)
    pair_first_assign = ir.Assign(pair_first_call, pair_first_var, loc)
    pair_second_var = ir.Var(scope, mk_unique_var('$pair_second_var'), loc)
    typemap[pair_second_var.name] = types.boolean
    pair_second_call = ir.Expr.pair_second(iternext_var, loc)
    pair_second_assign = ir.Assign(pair_second_call, pair_second_var, loc)
    phi_b_var = ir.Var(scope, mk_unique_var('$phi'), loc)
    typemap[phi_b_var.name] = types.intp
    phi_b_assign = ir.Assign(pair_first_var, phi_b_var, loc)
    branch = ir.Branch(pair_second_var, -1, -1, loc)
    header_block = ir.Block(scope, loc)
    header_block.body = [
        iternext_assign,
        pair_first_assign,
        pair_second_assign,
        phi_b_assign,
        branch]
    return header_block


def legalize_names(varnames):
    '''returns a dictionary for conversion of variable names to legal
    parameter names.
    '''
    var_map = { }
# WARNING: Decompyle incomplete


def get_name_var_table(blocks):
    '''create a mapping from variable names to their ir.Var objects'''
    
    def get_name_var_visit(var, namevar):
        namevar[var.name] = var
        return var

    namevar = { }
    visit_vars(blocks, get_name_var_visit, namevar)
    return namevar


def replace_var_names(blocks, namedict):
    '''replace variables (ir.Var to ir.Var) from dictionary (name -> name)'''
    new_namedict = { }
    for l, r in namedict.items():
        if l != r:
            new_namedict[l] = r
        
        def replace_name(var, namedict):
            pass
        # WARNING: Decompyle incomplete

        visit_vars(blocks, replace_name, new_namedict)
        return None


def replace_var_callback(var, vardict):
    pass
# WARNING: Decompyle incomplete


def replace_vars(blocks, vardict):
    '''replace variables (ir.Var to ir.Var) from dictionary (name -> ir.Var)'''
    new_vardict = { }
    for l, r in vardict.items():
        if l != r.name:
            new_vardict[l] = r
        visit_vars(blocks, replace_var_callback, new_vardict)
        return None


def replace_vars_stmt(stmt, vardict):
    visit_vars_stmt(stmt, replace_var_callback, vardict)


def replace_vars_inner(node, vardict):
    return visit_vars_inner(node, replace_var_callback, vardict)

visit_vars_extensions = { }

def visit_vars(blocks, callback, cbdata):
    '''go over statements of block bodies and replace variable names with
    dictionary.
    '''
    for block in blocks.values():
        for stmt in block.body:
            visit_vars_stmt(stmt, callback, cbdata)
        return None


def visit_vars_stmt(stmt, callback, cbdata):
    pass
# WARNING: Decompyle incomplete


def visit_vars_inner(node, callback, cbdata):
    pass
# WARNING: Decompyle incomplete

add_offset_to_labels_extensions = { }

def add_offset_to_labels(blocks, offset):
    '''add an offset to all block labels and jump/branch targets
    '''
    new_blocks = { }
    for l, b in blocks.items():
        term = None
        if b.body:
            term = b.body[-1]
            for inst in b.body:
                for T, f in add_offset_to_labels_extensions.items():
                    if isinstance(inst, T):
                        f_max = f(inst, offset)
                    if isinstance(term, ir.Jump):
                        b.body[-1] = ir.Jump(term.target + offset, term.loc)
        if isinstance(term, ir.Branch):
            b.body[-1] = ir.Branch(term.cond, term.truebr + offset, term.falsebr + offset, term.loc)
        new_blocks[l + offset] = b
        return new_blocks

find_max_label_extensions = { }

def find_max_label(blocks):
    max_label = 0
    for l, b in blocks.items():
        term = None
        if b.body:
            term = b.body[-1]
            for inst in b.body:
                for T, f in find_max_label_extensions.items():
                    if isinstance(inst, T):
                        f_max = f(inst)
                        if f_max > max_label:
                            max_label = f_max
                    if l > max_label:
                        max_label = l
        return max_label


def flatten_labels(blocks):
    '''makes the labels in range(0, len(blocks)), useful to compare CFGs
    '''
    blocks = add_offset_to_labels(blocks, find_max_label(blocks) + 1)
    new_blocks = { }
    topo_order = find_topo_order(blocks)
    l_map = dict()
    idx = 0
    for x in topo_order:
        l_map[x] = idx
        idx += 1
        for t_node in topo_order:
            b = blocks[t_node]
            term = None
            if b.body:
                term = b.body[-1]
            if isinstance(term, ir.Jump):
                b.body[-1] = ir.Jump(l_map[term.target], term.loc)
            if isinstance(term, ir.Branch):
                b.body[-1] = ir.Branch(term.cond, l_map[term.truebr], l_map[term.falsebr], term.loc)
            new_blocks[l_map[t_node]] = b
            return new_blocks


def remove_dels(blocks):
    '''remove ir.Del nodes'''
    for block in blocks.values():
        new_body = []
        for stmt in block.body:
            if not isinstance(stmt, ir.Del):
                new_body.append(stmt)
            block.body = new_body
            return None


def remove_args(blocks):
    '''remove ir.Arg nodes'''
    for block in blocks.values():
        new_body = []
        for stmt in block.body:
            if isinstance(stmt, ir.Assign) and isinstance(stmt.value, ir.Arg):
                continue
            new_body.append(stmt)
            block.body = new_body
            return None


def dead_code_elimination(func_ir, typemap, alias_map, arg_aliases = (None, None, None)):
    ''' Performs dead code elimination and leaves the IR in a valid state on
    exit
    '''
    do_post_proc = False
# WARNING: Decompyle incomplete


def remove_dead(blocks, args, func_ir, typemap, alias_map, arg_aliases = (None, None, None)):
    '''dead code elimination using liveness and CFG info.
    Returns True if something has been removed, or False if nothing is removed.
    '''
    cfg = compute_cfg_from_blocks(blocks)
    usedefs = compute_use_defs(blocks)
    live_map = compute_live_map(cfg, blocks, usedefs.usemap, usedefs.defmap)
    (call_table, _) = get_call_table(blocks)
# WARNING: Decompyle incomplete

remove_dead_extensions = { }

def remove_dead_block(block, lives, call_table, arg_aliases, alias_map, alias_set, func_ir, typemap):
    '''remove dead code using liveness info.
    Mutable arguments (e.g. arrays) that are not definitely assigned are live
    after return of function.
    '''
    removed = False
    new_body = [
        block.terminator]
# WARNING: Decompyle incomplete

remove_call_handlers = []

def remove_dead_random_call(rhs, lives, call_list):
    if len(call_list) == 3 and call_list[1:] == [
        'random',
        numpy]:
        return call_list[0] not in frozenset({'seed', 'shuffle'})

remove_call_handlers.append(remove_dead_random_call)

def has_no_side_effect(rhs, lives, call_table):
    ''' Returns True if this expression has no side effects that
        would prevent re-ordering.
    '''
    array_analysis = array_analysis
    parfor = parfor
    import numba.parfors
    prange = prange
    import numba.misc.special
    if isinstance(rhs, ir.Expr) and rhs.op == 'call':
        func_name = rhs.func.name
        if func_name not in call_table or call_table[func_name] == []:
            return False
        call_list = None[func_name]
        if call_list == [
            'empty',
            numpy] and call_list == [
            slice] and call_list == [
            'stencil',
            numba] and call_list == [
            'log',
            numpy] and call_list == [
            'dtype',
            numpy] and call_list == [
            array_analysis.wrap_index] and call_list == [
            prange] and call_list == [
            'prange',
            numba] and call_list == [
            'pndindex',
            numba] and call_list == [
            parfor.internal_prange] and call_list == [
            'ceil',
            math] and call_list == [
            max] or call_list == [
            int]:
            return True
        if None(call_list[0], _Intrinsic):
            if call_list[0]._name == 'empty_inferred' or call_list[0]._name == 'unsafe_empty_inferred':
                return True
            CPUDispatcher = CPUDispatcher
            import numba.core.registry
            dot_3_mv_check_args = dot_3_mv_check_args
            import numba.np.linalg
            if isinstance(call_list[0], CPUDispatcher):
                py_func = call_list[0].py_func
                if py_func == dot_3_mv_check_args:
                    return True
                for f in None:
                    if f(rhs, lives, call_list):
                        return True
                    return False
                    if isinstance(rhs, ir.Expr) and rhs.op == 'inplace_binop':
                        return rhs.lhs.name not in lives
                    if None(rhs, ir.Yield):
                        return False
                    if None(rhs, ir.Expr) and rhs.op == 'pair_first':
                        return False
                    return None

is_pure_extensions = []

def is_pure(rhs, lives, call_table):
    ''' Returns True if every time this expression is evaluated it
        returns the same result.  This is not the case for things
        like calls to numpy.random.
    '''
    if isinstance(rhs, ir.Expr):
        if rhs.op == 'call':
            func_name = rhs.func.name
            if func_name not in call_table or call_table[func_name] == []:
                return False
            call_list = None[func_name]
            if call_list == [
                slice] and call_list == [
                'log',
                numpy] and call_list == [
                'empty',
                numpy] and call_list == [
                'ceil',
                math] and call_list == [
                max] or call_list == [
                int]:
                return True
            for f in None:
                if f(rhs, lives, call_list):
                    return True
                return False
                if rhs.op == 'getiter' or rhs.op == 'iternext':
                    return False
                if None(rhs, ir.Yield):
                    return False
                return None


def is_const_call(module_name, func_name):
    if module_name == 'numpy' and func_name in ('empty',):
        return True

alias_analysis_extensions = { }
alias_func_extensions = { }

def get_canonical_alias(v, alias_map):
    if v not in alias_map:
        return v
    v_aliases = None(list(alias_map[v]))
    return v_aliases[0]


def find_potential_aliases(blocks, args, typemap, func_ir, alias_map, arg_aliases = (None, None)):
    '''find all array aliases and argument aliases to avoid remove as dead'''
    pass
# WARNING: Decompyle incomplete


def _add_alias(lhs, rhs, alias_map, arg_aliases):
    if rhs in arg_aliases:
        arg_aliases.add(lhs)
    elif rhs not in alias_map:
        alias_map[rhs] = set()
    if lhs not in alias_map:
        alias_map[lhs] = set()
    alias_map[rhs].add(lhs)
    alias_map[lhs].add(rhs)


def is_immutable_type(var, typemap):
    pass
# WARNING: Decompyle incomplete


def copy_propagate(blocks, typemap):
    '''compute copy propagation information for each block using fixed-point
     iteration on data flow equations:
     in_b = intersect(predec(B))
     out_b = gen_b | (in_b - kill_b)
    '''
    cfg = compute_cfg_from_blocks(blocks)
    entry = cfg.entry_point()
    c_data = init_copy_propagate_data(blocks, entry, typemap)
    (gen_copies, all_copies, kill_copies, in_copies, out_copies) = c_data
    old_point = None
    new_point = copy.deepcopy(out_copies)
# WARNING: Decompyle incomplete


def init_copy_propagate_data(blocks, entry, typemap):
    '''get initial condition of copy propagation data flow for each block.
    '''
    pass
# WARNING: Decompyle incomplete

copy_propagate_extensions = { }

def get_block_copies(blocks, typemap):
    '''get copies generated and killed by each block
    '''
    block_copies = { }
    extra_kill = { }
    for label, block in blocks.items():
        assign_dict = { }
        extra_kill[label] = set()
        for stmt in block.body:
            for T, f in copy_propagate_extensions.items():
                if isinstance(stmt, T):
                    (gen_set, kill_set) = f(stmt, typemap)
                    for lhs, rhs in gen_set:
                        assign_dict[lhs] = rhs
                        new_assign_dict = { }
                        for l, r in assign_dict.items():
                            if l not in kill_set and r not in kill_set:
                                new_assign_dict[l] = r
                            if r in kill_set:
                                extra_kill[label].add(l)
                            assign_dict = new_assign_dict
                            if isinstance(stmt, ir.Assign):
                                stmt.target.name = None
                                if isinstance(stmt.value, ir.Var):
                                    rhs = stmt.value.name
                                    if typemap[lhs] == typemap[rhs] and lhs != rhs:
                                        assign_dict[lhs] = rhs
                                        continue
                                if isinstance(stmt.value, ir.Expr) and stmt.value.op == 'inplace_binop':
                                    in1_var = stmt.value.lhs.name
                                    in1_typ = typemap[in1_var]
                                    if not isinstance(in1_typ, types.Number) and in1_typ == types.string:
                                        extra_kill[label].add(in1_var)
                                        new_assign_dict = { }
                                        for l, r in assign_dict.items():
                                            if l != in1_var and r != in1_var:
                                                new_assign_dict[l] = r
                                            if r == in1_var:
                                                extra_kill[label].add(l)
                                            assign_dict = new_assign_dict
                                            extra_kill[label].add(lhs)
                                            block_cps = set(assign_dict.items())
                                            block_copies[label] = block_cps
                                            return (block_copies, extra_kill)

apply_copy_propagate_extensions = { }

def apply_copy_propagate(blocks, in_copies, name_var_table, typemap, calltypes, save_copies = (None,)):
    '''apply copy propagation to IR: replace variables when copies available'''
    pass
# WARNING: Decompyle incomplete


def fix_setitem_type(stmt, typemap, calltypes):
    """Copy propagation can replace setitem target variable, which can be array
    with 'A' layout. The replaced variable can be 'C' or 'F', so we update
    setitem call type reflect this (from matrix power test)
    """
    if not isinstance(stmt, (ir.SetItem, ir.StaticSetItem)):
        return None
    t_typ = None[stmt.target.name]
    s_typ = calltypes[stmt].args[0]
    if not isinstance(s_typ, types.npytypes.Array) or isinstance(t_typ, types.npytypes.Array):
        return None
    if None.layout == 'A' and t_typ.layout != 'A':
        new_s_typ = s_typ.copy(layout = t_typ.layout)
        calltypes[stmt].args = (new_s_typ, calltypes[stmt].args[1], calltypes[stmt].args[2])


def dprint_func_ir(func_ir, title, blocks = (None,)):
    """Debug print function IR, with an optional blocks argument
    that may differ from the IR's original blocks.
    """
    if config.DEBUG_ARRAY_OPT >= 1:
        ir_blocks = func_ir.blocks
        func_ir.blocks = ir_blocks if blocks == None else blocks
        name = func_ir.func_id.func_qualname
        print(f'''IR {title!s}: {name!s}'''.center(80, '-'))
        func_ir.dump()
        print('----------------------------------------')
        func_ir.blocks = ir_blocks
        return None


def find_topo_order(blocks, cfg = (None,)):
    '''find topological order of blocks such that true branches are visited
    first (e.g. for_break test in test_dataflow). This is written as an iterative
    implementation of post order traversal to avoid recursion limit issues.
    '''
    pass
# WARNING: Decompyle incomplete

call_table_extensions = { }

def get_call_table(blocks, call_table, reverse_call_table, topological_ordering = (None, None, True)):
    '''returns a dictionary of call variables and their references.
    '''
    pass
# WARNING: Decompyle incomplete

tuple_table_extensions = { }

def get_tuple_table(blocks, tuple_table = (None,)):
    '''returns a dictionary of tuple variables and their values.
    '''
    pass
# WARNING: Decompyle incomplete


def get_stmt_writes(stmt):
    writes = set()
    if isinstance(stmt, (ir.Assign, ir.SetItem, ir.StaticSetItem)):
        writes.add(stmt.target.name)
    return writes


def rename_labels(blocks):
    '''rename labels of function body blocks according to topological sort.
    The set of labels of these blocks will remain unchanged.
    '''
    topo_order = find_topo_order(blocks)
    return_label = -1
    for l, b in blocks.items():
        if isinstance(b.body[-1], ir.Return):
            return_label = l
        if return_label != -1:
            topo_order.remove(return_label)
            topo_order.append(return_label)
    label_map = { }
    all_labels = sorted(topo_order, reverse = True)
    for label in topo_order:
        label_map[label] = all_labels.pop()
        for b in blocks.values():
            term = b.terminator
            if isinstance(term, ir.Jump):
                b.body[-1] = ir.Jump(label_map[term.target], term.loc)
            if isinstance(term, ir.Branch):
                b.body[-1] = ir.Branch(term.cond, label_map[term.truebr], label_map[term.falsebr], term.loc)
            new_blocks = { }
            for k, b in blocks.items():
                new_label = label_map[k]
                new_blocks[new_label] = b
                return new_blocks


def simplify_CFG(blocks):
    '''transform chains of blocks that have no loop into a single block'''
    pass
# WARNING: Decompyle incomplete

arr_math = [
    'min',
    'max',
    'sum',
    'prod',
    'mean',
    'var',
    'std',
    'cumsum',
    'cumprod',
    'argmax',
    'argmin',
    'argsort',
    'nonzero',
    'ravel']

def canonicalize_array_math(func_ir, typemap, calltypes, typingctx):
    pass
# WARNING: Decompyle incomplete

array_accesses_extensions = { }

def get_array_accesses(blocks, accesses = (None,)):
    '''returns a set of arrays accessed and their indices.
    '''
    pass
# WARNING: Decompyle incomplete


def is_slice_index(index):
    '''see if index is a slice index or has slice in it'''
    if isinstance(index, slice):
        return True
    if None(index, tuple):
        for i in index:
            if isinstance(i, slice):
                return True
            return False


def merge_adjacent_blocks(blocks):
    cfg = compute_cfg_from_blocks(blocks)
    removed = set()
    for label in list(blocks.keys()):
        if label in removed:
            continue
        block = blocks[label]
        succs = list(cfg.successors(label))
        if len(succs) != 1:
            pass
        else:
            next_label = succs[0][0]
            if next_label in removed:
                pass
            else:
                preds = list(cfg.predecessors(next_label))
                succs = list(cfg.successors(next_label))
                if len(preds) != 1 or preds[0][0] != label:
                    pass
                else:
                    next_block = blocks[next_label]
                    block.body.pop()
                    del blocks[next_label]
                    removed.add(next_label)
                    next_label = block, block.body += next_block.body, .body
        return None


def restore_copy_var_names(blocks, save_copies, typemap):
    '''
    restores variable names of user variables after applying copy propagation
    '''
    if not save_copies:
        return { }
    rename_dict = None
    var_rename_map = { }
    for a, b in save_copies:
        if a.startswith('$') and b.name.startswith('$') and b.name not in rename_dict:
            new_name = mk_unique_var('${}'.format(a))
            rename_dict[b.name] = new_name
            var_rename_map[new_name] = a
            typ = typemap.pop(b.name)
            typemap[new_name] = typ
        replace_var_names(blocks, rename_dict)
        return var_rename_map


def simplify(func_ir, typemap, calltypes, metadata):
    (in_cps, _) = copy_propagate(func_ir.blocks, typemap)
    name_var_table = get_name_var_table(func_ir.blocks)
    save_copies = apply_copy_propagate(func_ir.blocks, in_cps, name_var_table, typemap, calltypes)
    var_rename_map = restore_copy_var_names(func_ir.blocks, save_copies, typemap)
    if 'var_rename_map' not in metadata:
        metadata['var_rename_map'] = { }
    metadata['var_rename_map'].update(var_rename_map)
    if config.DEBUG_ARRAY_OPT >= 1:
        dprint_func_ir(func_ir, 'after copy prop')
    remove_dead(func_ir.blocks, func_ir.arg_names, func_ir, typemap)
    func_ir.blocks = simplify_CFG(func_ir.blocks)
    if config.DEBUG_ARRAY_OPT >= 1:
        dprint_func_ir(func_ir, 'after simplify')
        return None


class GuardException(Exception):
    pass


def require(cond):
    '''
    Raise GuardException if the given condition is False.
    '''
    if not cond:
        raise GuardException


def guard(func, *args, **kwargs):
    '''
    Run a function with given set of arguments, and guard against
    any GuardException raised by the function by returning None,
    or the expected return results if no such exception was raised.
    '''
    pass
# WARNING: Decompyle incomplete


def get_definition(func_ir, name, **kwargs):
    '''
    Same as func_ir.get_definition(name), but raise GuardException if
    exception KeyError is caught.
    '''
    pass
# WARNING: Decompyle incomplete


def build_definitions(blocks, definitions = (None,)):
    '''Build the definitions table of the given blocks by scanning
    through all blocks and instructions, useful when the definitions
    table is out-of-sync.
    Will return a new definition table if one is not passed.
    '''
    pass
# WARNING: Decompyle incomplete

build_defs_extensions = { }

def find_callname(func_ir, expr, typemap, definition_finder = (None, get_definition)):
    """Try to find a call expression's function and module names and return
    them as strings for unbounded calls. If the call is a bounded call, return
    the self object instead of module name. Raise GuardException if failed.

    Providing typemap can make the call matching more accurate in corner cases
    such as bounded call on an object which is inside another object.
    """
    pass
# WARNING: Decompyle incomplete


def find_build_sequence(func_ir, var):
    '''Check if a variable is constructed via build_tuple or
    build_list or build_set, and return the sequence and the
    operator, or raise GuardException otherwise.
    Note: only build_tuple is immutable, so use with care.
    '''
    require(isinstance(var, ir.Var))
    var_def = get_definition(func_ir, var)
    require(isinstance(var_def, ir.Expr))
    build_ops = [
        'build_tuple',
        'build_list',
        'build_set']
    require(var_def.op in build_ops)
    return (var_def.items, var_def.op)


def find_const(func_ir, var):
    '''Check if a variable is defined as constant, and return
    the constant value, or raise GuardException otherwise.
    '''
    require(isinstance(var, ir.Var))
    var_def = get_definition(func_ir, var)
    require(isinstance(var_def, (ir.Const, ir.Global, ir.FreeVar)))
    return var_def.value


def compile_to_numba_ir(mk_func, glbls, typingctx, targetctx, arg_typs, typemap, calltypes = (None, None, None, None, None)):
    '''
    Compile a function or a make_function node to Numba IR.

    Rename variables and
    labels to avoid conflict if inlined somewhere else. Perform type inference
    if typingctx and other typing inputs are available and update typemap and
    calltypes.
    '''
    typed_passes = typed_passes
    import numba.core
    if hasattr(mk_func, 'code'):
        code = mk_func.code
    elif hasattr(mk_func, '__code__'):
        code = mk_func.__code__
    else:
        raise NotImplementedError('function type not recognized {}'.format(mk_func))
    f_ir = get_ir_of_code(glbls, code)
    remove_dels(f_ir.blocks)
    f_ir.blocks = add_offset_to_labels(f_ir.blocks, _the_max_label.next())
    max_label = max(f_ir.blocks.keys())
    _the_max_label.update(max_label)
    var_table = get_name_var_table(f_ir.blocks)
    new_var_dict = { }
    for name, var in var_table.items():
        new_var_dict[name] = mk_unique_var(name)
        replace_var_names(f_ir.blocks, new_var_dict)
        if typingctx:
            (f_typemap, f_return_type, f_calltypes, _) = typed_passes.type_inference_stage(typingctx, targetctx, f_ir, arg_typs, None)
            arg_names = f_typemap()
            for a in arg_names:
                f_typemap.pop(a)
                typemap.update(f_typemap)
                calltypes.update(f_calltypes)
                return f_ir


def _create_function_from_code_obj(fcode, func_env, func_arg, func_clo, glbls):
    '''
    Creates a function from a code object. Args:
    * fcode - the code object
    * func_env - string for the freevar placeholders
    * func_arg - string for the function args (e.g. "a, b, c, d=None")
    * func_clo - string for the closure args
    * glbls - the function globals
    '''
    sanitized_co_name = fcode.co_name.replace('<', '_').replace('>', '_')
    func_text = f'''def closure():\n{func_env}\n\tdef {sanitized_co_name}({func_arg}):\n\t\treturn ({func_clo})\n\treturn {sanitized_co_name}'''
    loc = { }
    exec(func_text, glbls, loc)
    f = loc['closure']()
    f.__code__ = fcode
    f.__name__ = fcode.co_name
    return f


def get_ir_of_code(glbls, fcode):
    '''
    Compile a code object to get its IR, ir.Del nodes are emitted
    '''
    pass
# WARNING: Decompyle incomplete


def replace_arg_nodes(block, args):
    '''
    Replace ir.Arg(...) with variables
    '''
    pass
# WARNING: Decompyle incomplete


def replace_returns(blocks, target, return_label):
    '''
    Return return statement by assigning directly to target, and a jump.
    '''
    pass
# WARNING: Decompyle incomplete


def gen_np_call(func_as_str, func, lhs, args, typingctx, typemap, calltypes):
    pass
# WARNING: Decompyle incomplete


def dump_block(label, block):
    print(label, ':')
    for stmt in block.body:
        print('    ', stmt)
        return None


def dump_blocks(blocks):
    for label, block in blocks.items():
        dump_block(label, block)
        return None


def is_operator_or_getitem(expr):
