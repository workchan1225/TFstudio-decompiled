# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parfor.pyc (Python 3.11)

"""
This module transforms data-parallel operations such as Numpy calls into
'Parfor' nodes, which are nested loops that can be parallelized.
It also implements optimizations such as loop fusion, and extends the rest of
compiler analysis and optimizations to support Parfors.
This is similar to ParallelAccelerator package in Julia:
https://github.com/IntelLabs/ParallelAccelerator.jl
'Parallelizing Julia with a Non-invasive DSL', T. Anderson et al., ECOOP'17.
"""
import types as pytypes
import sys
import math
import os
import textwrap
import copy
import inspect
import linecache
from functools import reduce
from collections import defaultdict, OrderedDict, namedtuple
from contextlib import contextmanager
import operator
from dataclasses import make_dataclass
import warnings
from llvmlite import ir as lir
from numba.core.imputils import impl_ret_untracked
import numba.core.ir as numba
from numba.core import types, typing, utils, errors, ir, analysis, postproc, rewrites, typeinfer, config, ir_utils
from numba import prange, pndindex
from numba.np.npdatetime_helpers import datetime_minimum, datetime_maximum
from numba.np.numpy_support import as_dtype, numpy_version
from numba.core.typing.templates import infer_global, AbstractTemplate
from numba.stencils.stencilparfor import StencilPass
from numba.core.extending import register_jitable, lower_builtin
from numba.core.ir_utils import mk_unique_var, next_label, mk_alloc, get_np_ufunc_typ, mk_range_block, mk_loop_header, get_name_var_table, replace_vars, replace_vars_inner, visit_vars, visit_vars_inner, remove_dead, copy_propagate, get_block_copies, apply_copy_propagate, dprint_func_ir, find_topo_order, get_stmt_writes, rename_labels, get_call_table, simplify, simplify_CFG, has_no_side_effect, canonicalize_array_math, add_offset_to_labels, find_callname, find_build_sequence, guard, require, GuardException, compile_to_numba_ir, get_definition, build_definitions, replace_arg_nodes, replace_returns, is_getitem, is_setitem, is_get_setitem, index_var_of_get_setitem, set_index_var_of_get_setitem, find_potential_aliases, replace_var_names, transfer_scope
from numba.core.analysis import compute_use_defs, compute_live_map, compute_dead_maps, compute_cfg_from_blocks
from numba.core.controlflow import CFGraph
from numba.core.typing import npydecl, signature
from numba.core.types.functions import Function
from numba.parfors.array_analysis import random_int_args, random_1arg_size, random_2arg_sizelast, random_3arg_sizelast, random_calls, assert_equiv
from numba.core.extending import overload
import copy
import numpy
import numpy as np
from numba.parfors import array_analysis
import numba.cpython.builtins as numba
from numba.stencils import stencilparfor
_termwidth = 80
_txtwrapper = textwrap.TextWrapper(width = _termwidth, drop_whitespace = False)

def print_wrapped(x):
    for l in x.splitlines():
        _txtwrapper.wrap(l)()
        return None

sequential_parfor_lowering = False

def init_prange():
    pass

init_prange_overload = (lambda : 
def no_op():
passno_op)()

class internal_prange(object):
    
    def __new__(cls, *args):
        pass
    # WARNING: Decompyle incomplete



def min_parallel_impl(return_type, arg):
    if arg.ndim == 0:
        
        def min_1(in_arr):
            return in_arr[()]

    elif arg.ndim == 1:
        if isinstance(arg.dtype, (types.NPDatetime, types.NPTimedelta)):
            
            def min_1(in_arr):
                numba.parfors.parfor.init_prange()
                min_checker(len(in_arr))
                val = numba.cpython.builtins.get_type_max_value(in_arr.dtype)
                for i in numba.parfors.parfor.internal_prange(len(in_arr)):
                    val = datetime_minimum(val, in_arr[i])
                    return val

        else:
            
            def min_1(in_arr):
                numba.parfors.parfor.init_prange()
                min_checker(len(in_arr))
                val = numba.cpython.builtins.get_type_max_value(in_arr.dtype)
                for i in numba.parfors.parfor.internal_prange(len(in_arr)):
                    val = min(val, in_arr[i])
                    return val

    else:
        
        def min_1(in_arr):
            numba.parfors.parfor.init_prange()
            min_checker(len(in_arr))
            val = numba.cpython.builtins.get_type_max_value(in_arr.dtype)
            for i in numba.pndindex(in_arr.shape):
                val = min(val, in_arr[i])
                return val

    return min_1


def max_parallel_impl(return_type, arg):
    if arg.ndim == 0:
        
        def max_1(in_arr):
            return in_arr[()]

    elif arg.ndim == 1:
        if isinstance(arg.dtype, (types.NPDatetime, types.NPTimedelta)):
            
            def max_1(in_arr):
                numba.parfors.parfor.init_prange()
                max_checker(len(in_arr))
                val = numba.cpython.builtins.get_type_min_value(in_arr.dtype)
                for i in numba.parfors.parfor.internal_prange(len(in_arr)):
                    val = datetime_maximum(val, in_arr[i])
                    return val

        else:
            
            def max_1(in_arr):
                numba.parfors.parfor.init_prange()
                max_checker(len(in_arr))
                val = numba.cpython.builtins.get_type_min_value(in_arr.dtype)
                for i in numba.parfors.parfor.internal_prange(len(in_arr)):
                    val = max(val, in_arr[i])
                    return val

    else:
        
        def max_1(in_arr):
            numba.parfors.parfor.init_prange()
            max_checker(len(in_arr))
            val = numba.cpython.builtins.get_type_min_value(in_arr.dtype)
            for i in numba.pndindex(in_arr.shape):
                val = max(val, in_arr[i])
                return val

    return max_1


def argmin_parallel_impl(in_arr):
    numba.parfors.parfor.init_prange()
    argmin_checker(len(in_arr))
    A = in_arr.ravel()
    init_val = numba.cpython.builtins.get_type_max_value(A.dtype)
    ival = typing.builtins.IndexValue(0, init_val)
    for i in numba.parfors.parfor.internal_prange(len(A)):
        curr_ival = typing.builtins.IndexValue(i, A[i])
        ival = min(ival, curr_ival)
        return ival.index


def argmax_parallel_impl(in_arr):
    numba.parfors.parfor.init_prange()
    argmax_checker(len(in_arr))
    A = in_arr.ravel()
    init_val = numba.cpython.builtins.get_type_min_value(A.dtype)
    ival = typing.builtins.IndexValue(0, init_val)
    for i in numba.parfors.parfor.internal_prange(len(A)):
        curr_ival = typing.builtins.IndexValue(i, A[i])
        ival = max(ival, curr_ival)
        return ival.index


def dotvv_parallel_impl(a, b):
    numba.parfors.parfor.init_prange()
    l = a.shape[0]
    m = b.shape[0]
    s = 0
    for i in numba.parfors.parfor.internal_prange(l):
        s += a[i] * b[i]
        return s


def dotvm_parallel_impl(a, b):
    numba.parfors.parfor.init_prange()
    l = a.shape
    (m, n) = b.shape
    c = np.zeros(n, a.dtype)
    for i in numba.parfors.parfor.internal_prange(m):
        c += a[i] * b[(i, :)]
        return c


def dotmv_parallel_impl(a, b):
    numba.parfors.parfor.init_prange()
    (m, n) = a.shape
    l = b.shape
    c = np.empty(m, a.dtype)
    for i in numba.parfors.parfor.internal_prange(m):
        s = 0
        for j in range(n):
            s += a[(i, j)] * b[j]
            c[i] = s
            return c


def dot_parallel_impl(return_type, atyp, btyp):
    if isinstance(atyp, types.npytypes.Array) or isinstance(btyp, types.npytypes.Array):
        if  == atyp.ndim, btyp.ndim or atyp.ndim, btyp.ndim == 1:
            pass
        
    else:
        return dotvv_parallel_impl
    if None.ndim == 2 or btyp.ndim == 1:
        return dotmv_parallel_impl
    return None
    return None
    return None


def sum_parallel_impl(return_type, arg):
    pass
# WARNING: Decompyle incomplete


def prod_parallel_impl(return_type, arg):
    pass
# WARNING: Decompyle incomplete


def mean_parallel_impl(return_type, arg):
    pass
# WARNING: Decompyle incomplete


def var_parallel_impl(return_type, arg):
    if arg.ndim == 0:
        
        def var_1(in_arr):
            return 0

    elif arg.ndim == 1:
        
        def var_1(in_arr):
            m = in_arr.mean()
            numba.parfors.parfor.init_prange()
            ssd = 0
            for i in numba.parfors.parfor.internal_prange(len(in_arr)):
                val = in_arr[i] - m
                ssd += np.real(val * np.conj(val))
                return ssd / len(in_arr)

    else:
        
        def var_1(in_arr):
            m = in_arr.mean()
            numba.parfors.parfor.init_prange()
            ssd = 0
            for i in numba.pndindex(in_arr.shape):
                val = in_arr[i] - m
                ssd += np.real(val * np.conj(val))
                return ssd / in_arr.size

    return var_1


def std_parallel_impl(return_type, arg):
    
    def std_1(in_arr):
        return in_arr.var() ** 0.5

    return std_1


def arange_parallel_impl(return_type = None, *, dtype, *args):
    pass
# WARNING: Decompyle incomplete


def linspace_parallel_impl(return_type, *args):
    pass
# WARNING: Decompyle incomplete

swap_functions_map = {
    ('argmin', 'numpy'): (lambda r, a: argmin_parallel_impl),
    ('argmax', 'numpy'): (lambda r, a: argmax_parallel_impl),
    ('min', 'numpy'): min_parallel_impl,
    ('max', 'numpy'): max_parallel_impl,
    ('amin', 'numpy'): min_parallel_impl,
    ('amax', 'numpy'): max_parallel_impl,
    ('sum', 'numpy'): sum_parallel_impl,
    ('prod', 'numpy'): prod_parallel_impl,
    ('mean', 'numpy'): mean_parallel_impl,
    ('var', 'numpy'): var_parallel_impl,
    ('std', 'numpy'): std_parallel_impl,
    ('dot', 'numpy'): dot_parallel_impl,
    ('arange', 'numpy'): arange_parallel_impl,
    ('linspace', 'numpy'): linspace_parallel_impl }

def fill_parallel_impl(return_type, arr, val):
    '''Parallel implementation of ndarray.fill.  The array on
       which to operate is retrieved from get_call_name and
       is passed along with the value to fill.
    '''
    if arr.ndim == 1:
        
        def fill_1(in_arr, val):
            numba.parfors.parfor.init_prange()
            for i in numba.parfors.parfor.internal_prange(len(in_arr)):
                in_arr[i] = val
                return None

    else:
        
        def fill_1(in_arr, val):
            numba.parfors.parfor.init_prange()
            for i in numba.pndindex(in_arr.shape):
                in_arr[i] = val
                return None

    return fill_1

replace_functions_ndarray = {
    'fill': fill_parallel_impl }
max_checker = (lambda arr_size: if arr_size == 0:
raise ValueError('zero-size array to reduction operation maximum which has no identity'))()
min_checker = (lambda arr_size: if arr_size == 0:
raise ValueError('zero-size array to reduction operation minimum which has no identity'))()
argmin_checker = (lambda arr_size: if arr_size == 0:
raise ValueError('attempt to get argmin of an empty sequence'))()
argmax_checker = (lambda arr_size: if arr_size == 0:
raise ValueError('attempt to get argmax of an empty sequence'))()
checker_impl = namedtuple('checker_impl', [
    'name',
    'func'])
replace_functions_checkers_map = {
    ('argmin', 'numpy'): checker_impl('argmin_checker', argmin_checker),
    ('argmax', 'numpy'): checker_impl('argmax_checker', argmax_checker),
    ('min', 'numpy'): checker_impl('min_checker', min_checker),
    ('max', 'numpy'): checker_impl('max_checker', max_checker),
    ('amin', 'numpy'): checker_impl('min_checker', min_checker),
    ('amax', 'numpy'): checker_impl('max_checker', max_checker) }

class LoopNest(object):
    '''The LoopNest class holds information of a single loop including
    the index variable (of a non-negative integer value), and the
    range variable, e.g. range(r) is 0 to r-1 with step size 1.
    '''
    
    def __init__(self, index_variable, start, stop, step):
        self.index_variable = index_variable
        self.start = start
        self.stop = stop
        self.step = step

    
    def __repr__(self):
        return 'LoopNest(index_variable = {}, range = ({}, {}, {}))'.format(self.index_variable, self.start, self.stop, self.step)

    
    def list_vars(self):
        all_uses = []
        all_uses.append(self.index_variable)
        if isinstance(self.start, ir.Var):
            all_uses.append(self.start)
        if isinstance(self.stop, ir.Var):
            all_uses.append(self.stop)
        if isinstance(self.step, ir.Var):
            all_uses.append(self.step)
        return all_uses



class Parfor(ir.Stmt, ir.Expr):
    pass
# WARNING: Decompyle incomplete


def _analyze_parfor(parfor, equiv_set, typemap, array_analysis):
    '''Recursive array analysis for parfor nodes.
    '''
    func_ir = array_analysis.func_ir
    parfor_blocks = wrap_parfor_blocks(parfor)
    backup_equivset = array_analysis.equiv_sets.get(0, None)
    array_analysis.run(parfor_blocks, equiv_set)
    unwrap_parfor_blocks(parfor, parfor_blocks)
    parfor.equiv_set = array_analysis.equiv_sets[0]
    if backup_equivset:
        array_analysis.equiv_sets[0] = backup_equivset
    return ([], [])

array_analysis.array_analysis_extensions[Parfor] = _analyze_parfor

class ParforDiagnostics(object):
    '''Holds parfor diagnostic info, this is accumulated throughout the
    PreParforPass and ParforPass, also in the closure inlining!
    '''
    
    def __init__(self):
        self.func = None
        self.replaced_fns = dict()
        self.internal_name = '__numba_parfor_gufunc'
        self.fusion_info = defaultdict(list)
        self.nested_fusion_info = defaultdict(list)
        self.fusion_reports = []
        self.hoist_info = { }
        self.has_setup = False

    
    def setup(self, func_ir, fusion_enabled):
        self.func_ir = func_ir
        self.name = self.func_ir.func_id.func_qualname
        self.line = self.func_ir.loc
        self.fusion_enabled = fusion_enabled
        if self.internal_name in self.name:
            self.purpose = 'Internal parallel function'
        else:
            self.purpose = f'''Function {self.name!s}, {self.line!s}'''
        self.initial_parfors = self.get_parfors()
        self.has_setup = True

    has_setup = (lambda self: self._has_setup)()
    has_setup = (lambda self, state: self._has_setup = state)()
    
    def count_parfors(self, blocks = (None,)):
        return len(self.get_parfors())

    
    def _get_nested_parfors(self, parfor, parfors_list):
        blocks = wrap_parfor_blocks(parfor)
        self._get_parfors(blocks, parfors_list)
        unwrap_parfor_blocks(parfor)

    
    def _get_parfors(self, blocks, parfors_list):
        for label, blk in blocks.items():
            for stmt in blk.body:
                if isinstance(stmt, Parfor):
                    parfors_list.append(stmt)
                    self._get_nested_parfors(stmt, parfors_list)
                return None

    
    def get_parfors(self):
        parfors_list = []
        self._get_parfors(self.func_ir.blocks, parfors_list)
        return parfors_list

    
    def hoisted_allocations(self):
        allocs = []
    # WARNING: Decompyle incomplete

    
    def compute_graph_info(self, _a):
        '''
        compute adjacency list of the fused loops
        and find the roots in of the lists
        '''
        a = copy.deepcopy(_a)
        if a == { }:
            return ([], set())
        vtx = None()
    # WARNING: Decompyle incomplete

    
    def get_stats(self, fadj, nadj, root):
        '''
        Computes the number of fused and serialized loops
        based on a fusion adjacency list `fadj` and a nested
        parfors adjacency list `nadj` for the root, `root`
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def reachable_nodes(self, adj, root):
        '''
        returns a list of nodes reachable in an adjacency list from a
        specified root
        '''
        fusers = []
        fusers.extend(adj[root])
        for k in adj[root]:
            if adj[k] != []:
                fusers.extend(self.reachable_nodes(adj, k))
            return fusers

    
    def sort_pf_by_line(self, pf_id, parfors_simple):
        '''
        pd_id - the parfors id
        parfors_simple - the simple parfors map
        '''
        pf = parfors_simple[pf_id][0]
        pattern = pf.patterns[0]
        line = max(0, pf.loc.line - 1)
        filename = self.func_ir.loc.filename
        (nadj, nroots) = self.compute_graph_info(self.nested_fusion_info)
        (fadj, froots) = self.compute_graph_info(self.fusion_info)
        graphs = [
            nadj,
            fadj]
        if isinstance(pattern, tuple) and pattern[1] == 'internal':
            reported_loc = pattern[2][1]
            if reported_loc.filename == filename:
                return max(0, reported_loc.line - 1)
            tmp = None
            for adj in graphs:
                if adj:
                    for k in adj[pf_id]:
                        tmp.append(self.sort_pf_by_line(k, parfors_simple))
                        if tmp:
                            
                            return None, max(0, min(tmp) - 1)
                        for None in pf.loop_body.values():
                            for None in blk.body:
                                if stmt.loc.filename == filename:
                                    
                                    
                                    return None, None, max(0, stmt.loc.line - 1)
                                for blk.body.index(pf) in self.func_ir.blocks.values():
                                    for i in range(idx - 1, 0, -1):
                                        stmt = blk.body[i]
                                        if not isinstance(stmt, Parfor):
                                            line = max(0, stmt.loc.line - 1)
                                        
                                        except ValueError:
                                            continue
                                        return line

    
    def get_parfors_simple(self, print_loop_search):
        parfors_simple = dict()
    # WARNING: Decompyle incomplete

    
    def get_all_lines(self, parfors_simple):
        (fadj, froots) = self.compute_graph_info(self.fusion_info)
        (nadj, _nroots) = self.compute_graph_info(self.nested_fusion_info)
        if len(fadj) > len(nadj):
            lim = len(fadj)
            tmp = nadj
        else:
            lim = len(nadj)
            tmp = fadj
        for x in range(len(tmp), lim):
            tmp.append([])
            nroots = set()
            if _nroots:
                for r in _nroots:
                    if nadj[r] != []:
                        nroots.add(r)
                    all_roots = froots ^ nroots
                    froots_lines = { }
                    for x in froots:
                        line = self.sort_pf_by_line(x, parfors_simple)
                        froots_lines[line] = ('fuse', x, fadj)
                        nroots_lines = { }
                        for x in nroots:
                            line = self.sort_pf_by_line(x, parfors_simple)
                            nroots_lines[line] = ('nest', x, nadj)
                            all_lines = froots_lines.copy()
                            all_lines.update(nroots_lines)
                            return all_lines

    
    def source_listing(self, parfors_simple, purpose_str):
        filename = self.func_ir.loc.filename
        count = self.count_parfors()
        func_name = self.func_ir.func_id.func
        
        try:
            lines = inspect.getsource(func_name).splitlines()
        except OSError:
            lines = None

    # WARNING: Decompyle incomplete

    
    def print_unoptimised(self, lines):
        pass
    # WARNING: Decompyle incomplete

    
    def print_optimised(self, lines):
        pass
    # WARNING: Decompyle incomplete

    
    def allocation_hoist(self):
        found = False
        print('Allocation hoisting:')
        for pf_id, data in self.hoist_info.items():
            stmt = data.get('hoisted', [])
            for inst in stmt:
                if isinstance(inst.value, ir.Expr):
                    attr = inst.value.attr
                    if attr == 'empty':
                        msg = 'The memory allocation derived from the instruction at %s is hoisted out of the parallel loop labelled #%s (it will be performed before the loop is executed and reused inside the loop):'
                        loc = inst.loc
                        print_wrapped(msg % (loc, pf_id))
                        path = os.path.relpath(loc.filename)
                    else:
                        except ValueError:
                            path = os.path.abspath(loc.filename)
                        lines = linecache.getlines(path)
                        if lines and loc.line:
                            print_wrapped('   Allocation:: ' + lines[0 if loc.line < 2 else loc.line - 1].strip())
                    print_wrapped('    - numpy.empty() is used for the allocation.\n')
                    found = True
                    continue
                    except (KeyError, AttributeError):
                        continue
                if not found:
                    print_wrapped('No allocation hoisting found')
                    return None
                return None

    
    def instruction_hoist(self):
        print('')
        print('Instruction hoisting:')
        hoist_info_printed = False
        if self.hoist_info:
            for pf_id, data in self.hoist_info.items():
                hoisted = data.get('hoisted', None)
                not_hoisted = data.get('not_hoisted', None)
                if not hoisted and not_hoisted:
                    print('loop #%s has nothing to hoist.' % pf_id)
                    continue
                print('loop #%s:' % pf_id)
                if hoisted:
                    print('  Has the following hoisted:')
                    hoisted()
                    hoist_info_printed = True
                if not_hoisted:
                    print('  Failed to hoist the following:')
                    not_hoisted()
                    hoist_info_printed = True
                if not hoist_info_printed:
                    print_wrapped('No instruction hoisting found')
        print_wrapped('--------------------------------------------------------------------------------')

    
    def dump(self, level = (1,)):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        r = 'ParforDiagnostics:\n'
        r += repr(self.replaced_fns)
        return r

    
    def __repr__(self):
        r = 'ParforDiagnostics'
        return r



class PreParforPass(object):
    '''Preprocessing for the Parfor pass. It mostly inlines parallel
    implementations of numpy functions if available.
    '''
    
    def __init__(self, func_ir, typemap, calltypes, typingctx, targetctx, options, swapped, replace_functions_map = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def run(self):
        '''Run pre-parfor processing pass.
        '''
        canonicalize_array_math(self.func_ir, self.typemap, self.calltypes, self.typingctx)
        if self.options.numpy:
            self._replace_parallel_functions(self.func_ir.blocks)
        self.func_ir.blocks = simplify_CFG(self.func_ir.blocks)

    
    def _replace_parallel_functions(self, blocks):
        '''
        Replace functions with their parallel implementation in
        replace_functions_map if available.
        The implementation code is inlined to enable more optimization.
        '''
        pass
    # WARNING: Decompyle incomplete



def find_template(op):
    for ft in numba.core.typing.templates.builtin_registry.functions:
        if ft.key == op:
            
            return None, ft
        return None


class ParforPassStates:
    '''This class encapsulates all internal states of the ParforPass.
    '''
    
    def __init__(self, func_ir, typemap, calltypes, return_type, typingctx, targetctx, options, flags, metadata, diagnostics = (ParforDiagnostics(),)):
        self.func_ir = func_ir
        self.typemap = typemap
        self.calltypes = calltypes
        self.typingctx = typingctx
        self.targetctx = targetctx
        self.return_type = return_type
        self.options = options
        self.diagnostics = diagnostics
        self.swapped_fns = diagnostics.replaced_fns
        self.fusion_info = diagnostics.fusion_info
        self.nested_fusion_info = diagnostics.nested_fusion_info
        self.array_analysis = array_analysis.ArrayAnalysis(self.typingctx, self.func_ir, self.typemap, self.calltypes)
        ir_utils._the_max_label.update(max(func_ir.blocks.keys()))
        self.flags = flags
        self.metadata = metadata
        if 'parfors' not in metadata:
            metadata['parfors'] = { }
            return None



class ConvertInplaceBinop:
    '''Parfor subpass to convert setitem on Arrays
    '''
    
    def __init__(self, pass_states):
        '''
        Parameters
        ----------
        pass_states : ParforPassStates
        '''
        self.pass_states = pass_states
        self.rewritten = []

    
    def run(self, blocks):
        pass_states = self.pass_states
        topo_order = find_topo_order(blocks)
        for label in topo_order:
            block = blocks[label]
            new_body = []
            equiv_set = pass_states.array_analysis.get_equiv_set(label)
            for instr in block.body:
                if isinstance(instr, ir.Assign):
                    lhs = instr.target
                    expr = instr.value
                    if isinstance(expr, ir.Expr) and expr.op == 'inplace_binop':
                        loc = expr.loc
                        target = expr.lhs
                        value = expr.rhs
                        target_typ = pass_states.typemap[target.name]
                        value_typ = pass_states.typemap[value.name]
                        if isinstance(target_typ, types.npytypes.Array) and isinstance(value_typ, types.npytypes.Array):
                            new_instr = self._inplace_binop_to_parfor(equiv_set, loc, expr.immutable_fn, target, value)
                            self.rewritten.append(dict(old = instr, new = new_instr, reason = 'inplace_binop'))
                            instr = [
                                new_instr,
                                ir.Assign(target, lhs, loc)]
                if isinstance(instr, list):
                    new_body.extend(instr)
                    continue
                new_body.append(instr)
                block.body = new_body
                return None

    
    def _inplace_binop_to_parfor(self, equiv_set, loc, op, target, value):
        '''generate parfor from setitem node with a boolean or slice array indices.
        The value can be either a scalar or an array variable, and if a boolean index
        is used for the latter case, the same index must be used for the value too.
        '''
        pass_states = self.pass_states
        scope = target.scope
        arr_typ = pass_states.typemap[target.name]
        el_typ = arr_typ.dtype
        init_block = ir.Block(scope, loc)
        value_typ = pass_states.typemap[value.name]
        size_vars = equiv_set.get_shape(target)
        (index_vars, loopnests) = _mk_parfor_loops(pass_states.typemap, size_vars, scope, loc)
        body_label = next_label()
        body_block = ir.Block(scope, loc)
        (index_var, index_var_typ) = _make_index_var(pass_states.typemap, scope, index_vars, body_block)
        value_var = ir.Var(scope, mk_unique_var('$value_var'), loc)
        pass_states.typemap[value_var.name] = value_typ.dtype
        getitem_call = ir.Expr.getitem(value, index_var, loc)
        pass_states.calltypes[getitem_call] = signature(value_typ.dtype, value_typ, index_var_typ)
        body_block.body.append(ir.Assign(getitem_call, value_var, loc))
        target_var = ir.Var(scope, mk_unique_var('$target_var'), loc)
        pass_states.typemap[target_var.name] = el_typ
        getitem_call = ir.Expr.getitem(target, index_var, loc)
        pass_states.calltypes[getitem_call] = signature(el_typ, arr_typ, index_var_typ)
        body_block.body.append(ir.Assign(getitem_call, target_var, loc))
        expr_out_var = ir.Var(scope, mk_unique_var('$expr_out_var'), loc)
        pass_states.typemap[expr_out_var.name] = el_typ
        binop_expr = ir.Expr.binop(op, target_var, value_var, loc)
        body_block.body.append(ir.Assign(binop_expr, expr_out_var, loc))
        unified_type = self.pass_states.typingctx.unify_pairs(el_typ, value_typ.dtype)
        pass_states.calltypes[binop_expr] = signature(unified_type, unified_type, unified_type)
        setitem_node = ir.SetItem(target, index_var, expr_out_var, loc)
        pass_states.calltypes[setitem_node] = signature(types.none, arr_typ, index_var_typ, el_typ)
        body_block.body.append(setitem_node)
        parfor = Parfor(loopnests, init_block, { }, loc, index_var, equiv_set, ('inplace_binop', ''), pass_states.flags)
        parfor.loop_body = {
            body_label: body_block }
        if config.DEBUG_ARRAY_OPT >= 1:
            print('parfor from inplace_binop')
            parfor.dump()
        return parfor

    
    def _type_getitem(self, args):
        fnty = operator.getitem
        return self.pass_states.typingctx.resolve_function_type(fnty, tuple(args), { })



def get_index_var(x):
    return x.index if isinstance(x, ir.SetItem) else x.index_var


class ConvertSetItemPass:
    '''Parfor subpass to convert setitem on Arrays
    '''
    
    def __init__(self, pass_states):
        '''
        Parameters
        ----------
        pass_states : ParforPassStates
        '''
        self.pass_states = pass_states
        self.rewritten = []

    
    def run(self, blocks):
        pass_states = self.pass_states
        topo_order = find_topo_order(blocks)
    # WARNING: Decompyle incomplete

    
    def _setitem_to_parfor(self, equiv_set, loc, target, index, value, shape = (None,)):
        '''generate parfor from setitem node with a boolean or slice array indices.
        The value can be either a scalar or an array variable, and if a boolean index
        is used for the latter case, the same index must be used for the value too.
        '''
        pass_states = self.pass_states
        scope = target.scope
        arr_typ = pass_states.typemap[target.name]
        el_typ = arr_typ.dtype
        index_typ = pass_states.typemap[index.name]
        init_block = ir.Block(scope, loc)
    # WARNING: Decompyle incomplete

    
    def _type_getitem(self, args):
        fnty = operator.getitem
        return self.pass_states.typingctx.resolve_function_type(fnty, tuple(args), { })



def _make_index_var(typemap, scope, index_vars, body_block, force_tuple = (False,)):
    ''' When generating a SetItem call to an array in a parfor, the general
    strategy is to generate a tuple if the array is more than 1 dimension.
    If it is 1 dimensional then you can use a simple variable.  This routine
    is also used when converting pndindex to parfor but pndindex requires a
    tuple even if the iteration space is 1 dimensional.  The pndindex use of
    this function will use force_tuple to make the output index a tuple even
    if it is one dimensional.
    '''
    ndims = len(index_vars)
    loc = body_block.loc
    if ndims > 1 or force_tuple:
        tuple_var = ir.Var(scope, mk_unique_var('$parfor_index_tuple_var'), loc)
        typemap[tuple_var.name] = types.containers.UniTuple(types.uintp, ndims)
        tuple_call = ir.Expr.build_tuple(list(index_vars), loc)
        tuple_assign = ir.Assign(tuple_call, tuple_var, loc)
        body_block.body.append(tuple_assign)
        return (tuple_var, types.containers.UniTuple(types.uintp, ndims))
    if None == 1:
        return (index_vars[0], types.uintp)
    raise None.UnsupportedRewriteError('Parfor does not handle arrays of dimension 0', loc = loc)


def _mk_parfor_loops(typemap, size_vars, scope, loc):
    '''
    Create loop index variables and build LoopNest objects for a parfor.
    '''
    loopnests = []
    index_vars = []
    for size_var in size_vars:
        index_var = ir.Var(scope, mk_unique_var('parfor_index'), loc)
        index_vars.append(index_var)
        typemap[index_var.name] = types.uintp
        loopnests.append(LoopNest(index_var, 0, size_var, 1))
        return (index_vars, loopnests)


class ConvertNumpyPass:
    '''
    Convert supported Numpy functions, as well as arrayexpr nodes, to
    parfor nodes.
    '''
    
    def __init__(self, pass_states):
        self.pass_states = pass_states
        self.rewritten = []

    
    def run(self, blocks):
        pass_states = self.pass_states
        topo_order = find_topo_order(blocks)
        avail_vars = []
    # WARNING: Decompyle incomplete

    
    def _is_C_order(self, arr_name):
