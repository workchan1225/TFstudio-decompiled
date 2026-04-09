# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transforms.pyc (Python 3.11)

from llvmlite.ir import CallInstr

class Visitor(object):
    
    def visit(self, module):
        self._module = module
        for func in module.functions:
            self.visit_Function(func)
            return None

    
    def visit_Function(self, func):
        self._function = func
        for bb in func.blocks:
            self.visit_BasicBlock(bb)
            return None

    
    def visit_BasicBlock(self, bb):
        self._basic_block = bb
        for instr in bb.instructions:
            self.visit_Instruction(instr)
            return None

    
    def visit_Instruction(self, instr):
        raise NotImplementedError

    module = (lambda self: self._module)()
    function = (lambda self: self._function)()
    basic_block = (lambda self: self._basic_block)()


class CallVisitor(Visitor):
    
    def visit_Instruction(self, instr):
        if isinstance(instr, CallInstr):
            self.visit_Call(instr)
            return None

    
    def visit_Call(self, instr):
        raise NotImplementedError



class ReplaceCalls(CallVisitor):
    pass
# WARNING: Decompyle incomplete


def replace_all_calls(mod, orig, repl):
    '''Replace all calls to `orig` to `repl` in module `mod`.
    Returns the references to the returned calls
    '''
    rc = ReplaceCalls(orig, repl)
    rc.visit(mod)
    return rc.calls
