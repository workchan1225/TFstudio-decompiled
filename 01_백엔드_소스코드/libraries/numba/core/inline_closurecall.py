# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: inline_closurecall.pyc (Python 3.11)

import types as pytypes
import copy
import ctypes
import numba.core.analysis as numba
from numba.core import types, typing, errors, ir, rewrites, config, ir_utils, cgutils
from numba.parfors.parfor import internal_prange
from numba.core.ir_utils import next_label, add_offset_to_labels, replace_vars, remove_dels, rename_labels, find_topo_order, merge_adjacent_blocks, GuardException, require, guard, get_definition, find_callname, find_build_sequence, get_np_ufunc_typ, get_ir_of_code, simplify_CFG, canonicalize_array_math, dead_code_elimination
from numba.core.analysis import compute_cfg_from_blocks, compute_use_defs, compute_live_variables
from numba.core.imputils import impl_ret_untracked
from numba.core.extending import intrinsic
from numba.core.typing import signature
from numba.cpython.listobj import ListIterInstance
from numba.cpython.rangeobj import range_impl_map
from numba.np.arrayobj import make_array
from numba.core import postproc
from numba.np.unsafe.ndarray import empty_inferred as unsafe_empty_inferred
import numpy as np
import operator
import numba.misc.special as numba
enable_inline_arraycall = True

def callee_ir_validator(func_ir):
    '''Checks the IR of a callee is supported for inlining
    '''
    for blk in func_ir.blocks.values():
        for stmt in blk.find_insts(ir.Assign):
            if isinstance(stmt.value, ir.Yield):
                msg = 'The use of yield in a closure is unsupported.'
                raise errors.UnsupportedError(msg, loc = stmt.loc)
            return None


def _created_inlined_var_name(function_name, var_name):
    '''Creates a name for an inlined variable based on the function name and the
    variable name. It does this "safely" to avoid the use of characters that are
    illegal in python variable names as there are occasions when function
    generation needs valid python name tokens.'''
    inlined_name = f'''{function_name}.{var_name}'''
    new_name = inlined_name.replace('<', '_').replace('>', '_')
    new_name = new_name.replace('.', '_').replace('$', '_v')
    return new_name


class InlineClosureCallPass(object):
    '''InlineClosureCallPass class looks for direct calls to locally defined
    closures, and inlines the body of the closure function to the call site.
    '''
    
    def __init__(self, func_ir, parallel_options, swapped, typed = (None, False)):
        pass
    # WARNING: Decompyle incomplete

    
    def run(self):
        '''Run inline closure call pass.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _inline_reduction(self, work_list, block, i, expr, call_name):
