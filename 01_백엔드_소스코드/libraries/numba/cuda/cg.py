# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cg.pyc (Python 3.11)

from numba.core import types
from numba.core.extending import overload, overload_method
from numba.core.typing import signature
from numba.cuda import nvvmutils
from numba.cuda.extending import intrinsic
from numba.cuda.types import grid_group, GridGroup as GridGroupClass

class GridGroup:
    '''A cooperative group representing the entire grid'''
    
    def sync():
        '''Synchronize this grid group'''
        pass



def this_grid():
    '''Get the current grid group.'''
    return GridGroup()

_this_grid = (lambda typingctx: sig = signature(grid_group)
def codegen(context, builder, sig, args):
one = context.get_constant(types.int32, 1)mod = builder.modulebuilder.call(nvvmutils.declare_cudaCGGetIntrinsicHandle(mod), (one,))(sig, codegen))()
_ol_this_grid = (lambda : 
def impl():
_this_grid()impl)()
_grid_group_sync = (lambda typingctx, group: sig = signature(types.int32, group)
def codegen(context, builder, sig, args):
flags = context.get_constant(types.int32, 0)mod = builder.module# WARNING: Decompyle incomplete
(sig, codegen))()
_ol_grid_group_sync = (lambda group: 
def impl(group):
_grid_group_sync(group)impl)()
