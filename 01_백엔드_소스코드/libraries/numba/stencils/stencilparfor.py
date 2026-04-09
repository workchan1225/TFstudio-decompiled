# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stencilparfor.pyc (Python 3.11)

import numbers
import copy
import types as pytypes
from operator import add
import operator
import numpy as np
import numba.parfors.parfor as numba
from numba.core import types, ir, rewrites, config, ir_utils
from numba.core.typing.templates import infer_global, AbstractTemplate
from numba.core.typing import signature
from numba.core import utils, typing
from numba.core.ir_utils import get_call_table, mk_unique_var, compile_to_numba_ir, replace_arg_nodes, guard, find_callname, require, find_const, GuardException
from numba.core.errors import NumbaValueError
from numba.core.utils import OPERATORS_TO_BUILTINS
from numba.np import numpy_support

def _compute_last_ind(dim_size, index_const):
    if index_const > 0:
        return dim_size - index_const


class StencilPass(object):
    
    def __init__(self, func_ir, typemap, calltypes, array_analysis, typingctx, targetctx, flags):
        self.func_ir = func_ir
        self.typemap = typemap
        self.calltypes = calltypes
        self.array_analysis = array_analysis
        self.typingctx = typingctx
        self.targetctx = targetctx
        self.flags = flags

    
    def run(self):
        ''' Finds all calls to StencilFuncs in the IR and converts them to parfor.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def replace_return_with_setitem(self, blocks, exit_value_var, parfor_body_exit_label):
        '''
        Find return statements in the IR and replace them with a SetItem
        call of the value "returned" by the kernel into the result array.
        Returns the block labels that contained return statements.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _mk_stencil_parfor(self, label, in_args, out_arr, stencil_ir, index_offsets, target, return_type, stencil_func, arg_to_arr_dict):
        ''' Converts a set of stencil kernel blocks to a parfor.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_stencil_last_ind(self, dim_size, end_length, gen_nodes, scope, loc):
        last_ind = dim_size
        if end_length != 0:
            index_const = ir.Var(scope, mk_unique_var('stencil_const_var'), loc)
            self.typemap[index_const.name] = types.intp
            if isinstance(end_length, numbers.Number):
                const_assign = ir.Assign(ir.Const(end_length, loc), index_const, loc)
            else:
                const_assign = ir.Assign(end_length, index_const, loc)
            gen_nodes.append(const_assign)
            last_ind = ir.Var(scope, mk_unique_var('last_ind'), loc)
            self.typemap[last_ind.name] = types.intp
            g_var = ir.Var(scope, mk_unique_var('compute_last_ind_var'), loc)
            check_func = numba.njit(_compute_last_ind)
            func_typ = types.functions.Dispatcher(check_func)
            self.typemap[g_var.name] = func_typ
            g_obj = ir.Global('_compute_last_ind', check_func, loc)
            g_assign = ir.Assign(g_obj, g_var, loc)
            gen_nodes.append(g_assign)
            index_call = ir.Expr.call(g_var, [
                dim_size,
                index_const], (), loc)
            self.calltypes[index_call] = func_typ.get_call_type(self.typingctx, [
                types.intp,
                types.intp], { })
            index_assign = ir.Assign(index_call, last_ind, loc)
            gen_nodes.append(index_assign)
        return last_ind

    
    def _get_stencil_start_ind(self, start_length, gen_nodes, scope, loc):
