# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: removerefctpass.pyc (Python 3.11)

'''
Implement a rewrite pass on a LLVM module to remove unnecessary 
refcount operations.
'''
from llvmlite.ir.transforms import CallVisitor
from numba.core import types

class _MarkNrtCallVisitor(CallVisitor):
    '''
    A pass to mark all NRT_incref and NRT_decref.
    '''
    
    def __init__(self):
        self.marked = set()

    
    def visit_Call(self, instr):
        if getattr(instr.callee, 'name', '') in _accepted_nrtfns:
            self.marked.add(instr)
            return None



def _rewrite_function(function):
    markpass = _MarkNrtCallVisitor()
    markpass.visit_Function(function)
    for bb in function.basic_blocks:
        for inst in list(bb.instructions):
            if inst in markpass.marked:
                bb.instructions.remove(inst)
            return None

_accepted_nrtfns = ('NRT_incref', 'NRT_decref')

def _legalize(module, dmm, fndesc):
    '''
    Legalize the code in the module.
    Returns True if the module is legal for the rewrite pass that removes
    unnecessary refcounts.
    '''
    pass
# WARNING: Decompyle incomplete


def remove_unnecessary_nrt_usage(function, context, fndesc):
    '''
    Remove unnecessary NRT incref/decref in the given LLVM function.
    It uses highlevel type info to determine if the function does not need NRT.
    Such a function does not:

    - return array object(s);
    - take arguments that need refcounting except array;
    - call function(s) that return refcounted object.

    In effect, the function will not capture or create references that extend
    the lifetime of any refcounted objects beyond the lifetime of the function.

    The rewrite is performed in place.
    If rewrite has happened, this function returns True, otherwise, it returns False.
    '''
    dmm = context.data_model_manager
    if _legalize(function.module, dmm, fndesc):
        _rewrite_function(function)
        return True
