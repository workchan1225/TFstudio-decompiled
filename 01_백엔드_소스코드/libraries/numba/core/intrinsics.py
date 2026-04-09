# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: intrinsics.pyc (Python 3.11)

__doc__ = '\nLLVM pass that converts intrinsic into other math calls\n'
from llvmlite import ir

class _DivmodFixer(ir.Visitor):
    
    def visit_Instruction(self, instr):
        pass
    # WARNING: Decompyle incomplete



def fix_divmod(mod):
    '''Replace division and reminder instructions to builtins calls
    '''
    _DivmodFixer().visit(mod)

# WARNING: Decompyle incomplete
