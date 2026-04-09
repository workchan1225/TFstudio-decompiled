# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parfor_lowering.pyc (Python 3.11)

import copy
import operator
import types as pytypes
import operator
import warnings
from dataclasses import make_dataclass
import llvmlite.ir as llvmlite
import numpy as np
import numba
from numba.parfors import parfor
from numba.core import types, ir, config, compiler, sigutils, cgutils
from numba.core.ir_utils import add_offset_to_labels, replace_var_names, remove_dels, legalize_names, rename_labels, get_name_var_table, visit_vars_inner, get_definition, guard, get_call_table, is_pure, get_np_ufunc_typ, get_unused_var_name, is_const_call, fixup_var_define_in_scope, transfer_scope, find_max_label, get_global_func_typ, find_topo_order
from numba.core.typing import signature
from numba.core import lowering
from numba.parfors.parfor import ensure_parallel_support
from numba.core.errors import NumbaParallelSafetyWarning, NotDefinedError, CompilerError, InternalError
from numba.parfors.parfor_lowering_utils import ParforLoweringBuilder

class ParforLower(lowering.Lower):
    pass
# WARNING: Decompyle incomplete


def _lower_parfor_parallel(lowerer, parfor):
    pass
# WARNING: Decompyle incomplete


def _lower_parfor_parallel_std(lowerer, parfor):
    """Lowerer that handles LLVM code generation for parfor.
    This function lowers a parfor IR node to LLVM.
    The general approach is as follows:
    1) The code from the parfor's init block is lowered normally
       in the context of the current function.
    2) The body of the parfor is transformed into a gufunc function.
    3) Code is inserted into the main function that calls do_scheduling
       to divide the iteration space for each thread, allocates
       reduction arrays, calls the gufunc function, and then invokes
       the reduction function across the reduction arrays to produce
       the final reduction values.
    """
    get_thread_count = get_thread_count
    import numba.np.ufunc.parallel
    ensure_parallel_support()
    typingctx = lowerer.context.typing_context
    targetctx = lowerer.context
    builder = lowerer.builder
    orig_typemap = lowerer.fndesc.typemap
    lowerer.fndesc.typemap = copy.copy(orig_typemap)
    if config.DEBUG_ARRAY_OPT:
        print('lowerer.fndesc', lowerer.fndesc, type(lowerer.fndesc))
    typemap = lowerer.fndesc.typemap
    varmap = lowerer.varmap
    if config.DEBUG_ARRAY_OPT:
        print('_lower_parfor_parallel')
        parfor.dump()
    loc = parfor.init_block.loc
    scope = parfor.init_block.scope
    if config.DEBUG_ARRAY_OPT:
        print('init_block = ', parfor.init_block, ' ', type(parfor.init_block))
    for instr in parfor.init_block.body:
        if config.DEBUG_ARRAY_OPT:
            print('lower init_block instr = ', instr)
        lowerer.lower_inst(instr)
        for racevar in parfor.races:
            if racevar not in varmap:
                rvtyp = typemap[racevar]
                rv = ir.Var(scope, racevar, loc)
                lowerer._alloca_var(rv.name, rvtyp)
            alias_map = { }
            arg_aliases = { }
            numba.parfors.parfor.find_potential_aliases_parfor(parfor, parfor.params, typemap, lowerer.func_ir, alias_map, arg_aliases)
            if config.DEBUG_ARRAY_OPT:
                print('alias_map', alias_map)
                print('arg_aliases', arg_aliases)
# WARNING: Decompyle incomplete

_ReductionInfo = make_dataclass('_ReductionInfo', [
    'redvar_info',
    'redvar_name',
    'redvar_typ',
    'redarr_var',
    'redarr_typ',
    'init_val'], frozen = True)

def _parfor_lowering_finalize_reduction(parfor, redarrs, lowerer, parfor_reddict, thread_count_var):
    '''Emit code to finalize the reduction from the intermediate values of
    each thread.
    '''
    pass
# WARNING: Decompyle incomplete


class ParforsUnexpectedReduceNodeError(InternalError):
    pass
# WARNING: Decompyle incomplete


def _lower_trivial_inplace_binops(parfor, lowerer, thread_count_var, reduce_info):
    '''Lower trivial inplace-binop reduction.
    '''
    for inst in reduce_info.redvar_info.reduce_nodes:
        if _lower_var_to_var_assign(lowerer, inst):
            pass
        elif _is_right_op_and_rhs_is_init(inst, reduce_info.redvar_name, 'inplace_binop'):
            fn = inst.value.fn
            redvar_result = _emit_binop_reduce_call(fn, lowerer, thread_count_var, reduce_info)
            lowerer.storevar(redvar_result, name = inst.target.name)
        elif _is_right_op_and_rhs_is_init(inst, reduce_info.redvar_name, 'binop'):
            fn = inst.value.fn
            redvar_result = _emit_binop_reduce_call(fn, lowerer, thread_count_var, reduce_info)
            lowerer.storevar(redvar_result, name = inst.target.name)
        else:
            raise ParforsUnexpectedReduceNodeError(inst)
        if _fix_redvar_name_ssa_mismatch(parfor, lowerer, inst, reduce_info.redvar_name):
            pass
        
        if config.DEBUG_ARRAY_OPT_RUNTIME:
            varname = reduce_info.redvar_name
            lowerer.print_variable(f'''{parfor.loc}: parfor {fn.__name__} reduction {varname} =''', varname)
            return None
        return None


def _lower_non_trivial_reduce(parfor, lowerer, thread_count_var, reduce_info):
    '''Lower non-trivial reduction such as call to `functools.reduce()`.
    '''
    pass
# WARNING: Decompyle incomplete


def _lower_var_to_var_assign(lowerer, inst):
    '''Lower Var->Var assignment.

    Returns True if-and-only-if `inst` is a Var->Var assignment.
    '''
    if isinstance(inst, ir.Assign) and isinstance(inst.value, ir.Var):
        loaded = lowerer.loadvar(inst.value.name)
        lowerer.storevar(loaded, name = inst.target.name)
        return True


def _emit_getitem_call(idx, lowerer, reduce_info):
    '''Emit call to ``redarr_var[idx]``
    '''
    
    def reducer_getitem(redarr, index):
        return redarr[index]

    builder = lowerer.builder
    ctx = lowerer.context
    redarr_typ = reduce_info.redarr_typ
    arg_arr = lowerer.loadvar(reduce_info.redarr_var.name)
    args = (arg_arr, idx)
    sig = signature(reduce_info.redvar_typ, redarr_typ, types.intp)
    elem = ctx.compile_internal(builder, reducer_getitem, sig, args)
    return elem


def _emit_binop_reduce_call(binop, lowerer, thread_count_var, reduce_info):
    '''Emit call to the ``binop`` for the reduction variable.
    '''
    
    def reduction_add(thread_count, redarr, init):
        c = init
        for i in range(thread_count):
            c += redarr[i]
            return c

    
    def reduction_mul(thread_count, redarr, init):
        c = init
        for i in range(thread_count):
            c *= redarr[i]
            return c

    kernel = {
        operator.truediv: reduction_mul,
        operator.floordiv: reduction_mul,
        operator.mul: reduction_mul,
        operator.itruediv: reduction_mul,
        operator.ifloordiv: reduction_mul,
        operator.imul: reduction_mul,
        operator.sub: reduction_add,
        operator.add: reduction_add,
        operator.isub: reduction_add,
        operator.iadd: reduction_add }[binop]
    ctx = lowerer.context
    builder = lowerer.builder
    redarr_typ = reduce_info.redarr_typ
    arg_arr = lowerer.loadvar(reduce_info.redarr_var.name)
    if config.DEBUG_ARRAY_OPT_RUNTIME:
        init_var = reduce_info.redarr_var.scope.get(reduce_info.redvar_name)
        res_print = ir.Print(args = [
            reduce_info.redarr_var,
            init_var], vararg = None, loc = lowerer.loc)
        typemap = lowerer.fndesc.typemap
        lowerer.fndesc.calltypes[res_print] = signature(types.none, typemap[reduce_info.redarr_var.name], typemap[init_var.name])
        lowerer.lower_inst(res_print)
    arg_thread_count = lowerer.loadvar(thread_count_var.name)
    args = (arg_thread_count, arg_arr, reduce_info.init_val)
    sig = signature(reduce_info.redvar_typ, types.uintp, redarr_typ, reduce_info.redvar_typ)
    redvar_result = ctx.compile_internal(builder, kernel, sig, args)
    return redvar_result


def _is_right_op_and_rhs_is_init(inst, redvar_name, op):
    '''Is ``inst`` an inplace-binop and the RHS is the reduction init?
    '''
    if not isinstance(inst, ir.Assign):
        return False
    rhs = None.value
    if not isinstance(rhs, ir.Expr):
        return False
    if None.op != op:
        return False
    if None.rhs.name != f'''{redvar_name}#init''':
        return False


def _fix_redvar_name_ssa_mismatch(parfor, lowerer, inst, redvar_name):
    '''Fix reduction variable name mismatch due to SSA.
    '''
    scope = parfor.init_block.scope
    if isinstance(inst, ir.Assign):
        
        try:
            reduction_var = scope.get_exact(redvar_name)
            redvar_unver_name = reduction_var.unversioned_name
            target_unver_name = inst.target.unversioned_name
            is_same_source_var = redvar_unver_name == target_unver_name
        except NotDefinedError:
            is_same_source_var = redvar_name == inst.target.name

        if is_same_source_var and redvar_name != inst.target.name:
            val = lowerer.loadvar(inst.target.name)
            lowerer.storevar(val, name = redvar_name)
            return True
        return None


def _create_shape_signature(get_shape_classes, num_inputs, num_reductions, args, func_sig, races, typemap):
    '''Create shape signature for GUFunc
    '''
    pass
# WARNING: Decompyle incomplete


def _print_block(block):
    for i, inst in enumerate(block.body):
        print('    ', i, ' ', inst)
        return None


def _print_body(body_dict):
    '''Pretty-print a set of IR blocks.
    '''
    topo_order = wrap_find_topo(body_dict)
    for label in topo_order:
        block = body_dict[label]
        print('label: ', label)
        _print_block(block)
        return None


def wrap_loop_body(loop_body):
    blocks = loop_body.copy()
    first_label = min(blocks.keys())
    last_label = max(blocks.keys())
    loc = blocks[last_label].loc
    blocks[last_label].body.append(ir.Jump(first_label, loc))
    return blocks


def unwrap_loop_body(loop_body):
    last_label = max(loop_body.keys())
    loop_body[last_label].body = loop_body[last_label].body[:-1]


def add_to_def_once_sets(a_def, def_once, def_more):
    """If the variable is already defined more than once, do nothing.
       Else if defined exactly once previously then transition this
       variable to the defined more than once set (remove it from
       def_once set and add to def_more set).
       Else this must be the first time we've seen this variable defined
       so add to def_once set.
    """
    if a_def in def_more:
        return None
    if None in def_once:
        def_more.add(a_def)
        def_once.remove(a_def)
        return None
    None.add(a_def)


def compute_def_once_block(block, def_once, def_more, getattr_taken, typemap, module_assigns):
    '''Effect changes to the set of variables defined once or more than once
       for a single block.
       block - the block to process
       def_once - set of variable names known to be defined exactly once
       def_more - set of variable names known to be defined more than once
       getattr_taken - dict mapping variable name to tuple of object and attribute taken
       module_assigns - dict mapping variable name to the Global that they came from
    '''
    assignments = block.find_insts(ir.Assign)
    for one_assign in assignments:
        a_def = one_assign.target.name
        add_to_def_once_sets(a_def, def_once, def_more)
        rhs = one_assign.value
        if isinstance(rhs, ir.Global) and isinstance(rhs.value, pytypes.ModuleType):
            module_assigns[a_def] = rhs.value.__name__
        if isinstance(rhs, ir.Expr) and rhs.op == 'getattr' and rhs.value.name in def_once:
            getattr_taken[a_def] = (rhs.value.name, rhs.attr)
        if isinstance(rhs, ir.Expr) and rhs.op == 'call' and rhs.func.name in getattr_taken:
            (base_obj, base_attr) = getattr_taken[rhs.func.name]
            if base_obj in module_assigns:
                base_mod_name = module_assigns[base_obj]
                if not is_const_call(base_mod_name, base_attr):
                    add_to_def_once_sets(base_obj, def_once, def_more)
                else:
                    add_to_def_once_sets(base_obj, def_once, def_more)
        if isinstance(rhs, ir.Expr) and rhs.op == 'call':
            for argvar in rhs.args:
                if isinstance(argvar, ir.Var):
                    argvar = argvar.name
                avtype = typemap[argvar]
                if getattr(avtype, 'mutable', False):
                    add_to_def_once_sets(argvar, def_once, def_more)
                return None


def wrap_find_topo(loop_body):
    blocks = wrap_loop_body(loop_body)
    topo_order = find_topo_order(blocks)
    unwrap_loop_body(loop_body)
    return topo_order


def compute_def_once_internal(loop_body, def_once, def_more, getattr_taken, typemap, module_assigns):
    '''Compute the set of variables defined exactly once in the given set of blocks
       and use the given sets for storing which variables are defined once, more than
       once and which have had a getattr call on them.
    '''
    topo_order = wrap_find_topo(loop_body)
    for label in topo_order:
        block = loop_body[label]
        compute_def_once_block(block, def_once, def_more, getattr_taken, typemap, module_assigns)
        for inst in block.body:
            if isinstance(inst, parfor.Parfor):
                compute_def_once_block(inst.init_block, def_once, def_more, getattr_taken, typemap, module_assigns)
                compute_def_once_internal(inst.loop_body, def_once, def_more, getattr_taken, typemap, module_assigns)
            return None


def compute_def_once(loop_body, typemap):
    '''Compute the set of variables defined exactly once in the given set of blocks.
    '''
    def_once = set()
    def_more = set()
    getattr_taken = { }
    module_assigns = { }
    compute_def_once_internal(loop_body, def_once, def_more, getattr_taken, typemap, module_assigns)
    return (def_once, def_more)


def find_vars(var, varset):
    pass
# WARNING: Decompyle incomplete


def _hoist_internal(inst, dep_on_param, call_table, hoisted, not_hoisted, typemap, stored_arrays):
    if inst.target.name in stored_arrays:
        not_hoisted.append((inst, 'stored array'))
        if config.DEBUG_ARRAY_OPT >= 1:
            print('Instruction', inst, 'could not be hoisted because the created array is stored.')
        return False
    target_type = None[inst.target.name]
    uses = set()
    visit_vars_inner(inst.value, find_vars, uses)
    unhoistable = not_hoisted()
    use_unhoist = uses & unhoistable
    diff = uses.difference(dep_on_param)
    diff |= use_unhoist
    if config.DEBUG_ARRAY_OPT >= 1:
        print('_hoist_internal:', inst, 'uses:', uses, 'diff:', diff)
    if len(diff) == 0 and is_pure(inst.value, None, call_table):
        if config.DEBUG_ARRAY_OPT >= 1:
            print('Will hoist instruction', inst, target_type)
        hoisted.append(inst)
        if not isinstance(target_type, types.npytypes.Array):
            dep_on_param += [
                inst.target.name]
        return True
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(diff) > 0:
        not_hoisted.append((inst, 'dependency'))
        if config.DEBUG_ARRAY_OPT >= 1:
            print('Instruction', inst, 'could not be hoisted because of a dependency.')
        else:
            not_hoisted.append((inst, 'not pure'))
            if config.DEBUG_ARRAY_OPT >= 1:
                print('Instruction', inst, "could not be hoisted because it isn't pure.")
    return False


def find_setitems_block(setitems, itemsset, block, typemap):
    pass
# WARNING: Decompyle incomplete


def find_setitems_body(setitems, itemsset, loop_body, typemap):
    '''
      Find the arrays that are written into (goes into setitems) and the
      mutable objects (mostly arrays) that are written into other arrays
      (goes into itemsset).
    '''
    for label, block in loop_body.items():
        find_setitems_block(setitems, itemsset, block, typemap)
        return None


def empty_container_allocator_hoist(inst, dep_on_param, call_table, hoisted, not_hoisted, typemap, stored_arrays):
