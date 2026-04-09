# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: instructions.pyc (Python 3.11)

'''
Implementation of LLVM IR instructions.
'''
from llvmlite.ir import types
from llvmlite.ir.values import Block, Function, Value, NamedValue, Constant, MetaDataArgument, MetaDataString, AttributeSet, Undefined, ArgumentAttributes
from llvmlite.ir._utils import _HasMetadata

class Instruction(_HasMetadata, NamedValue):
    pass
# WARNING: Decompyle incomplete


class CallInstrAttributes(AttributeSet):
    _known = frozenset([
        'convergent',
        'noreturn',
        'nounwind',
        'readonly',
        'readnone',
        'noinline',
        'alwaysinline'])

TailMarkerOptions = frozenset([
    'tail',
    'musttail',
    'notail'])

class FastMathFlags(AttributeSet):
    _known = frozenset([
        'fast',
        'nnan',
        'ninf',
        'nsz',
        'arcp',
        'contract',
        'afn',
        'reassoc'])


class CallInstr(Instruction):
    pass
# WARNING: Decompyle incomplete


class InvokeInstr(CallInstr):
    pass
# WARNING: Decompyle incomplete


class Terminator(Instruction):
    pass
# WARNING: Decompyle incomplete


class PredictableInstr(Instruction):
    
    def set_weights(self, weights):
        operands = [
            MetaDataString(self.module, 'branch_weights')]
        for w in weights:
            if w < 0:
                raise ValueError('branch weight must be a positive integer')
            operands.append(Constant(types.IntType(32), w))
            md = self.module.add_metadata(operands)
            self.set_metadata('prof', md)
            return None



class Ret(Terminator):
    pass
# WARNING: Decompyle incomplete


class Branch(Terminator):
    pass


class ConditionalBranch(Terminator, PredictableInstr):
    pass


class IndirectBranch(Terminator, PredictableInstr):
    pass
# WARNING: Decompyle incomplete


class SwitchInstr(Terminator, PredictableInstr):
    pass
# WARNING: Decompyle incomplete


class Resume(Terminator):
    pass


class SelectInstr(Instruction):
    pass
# WARNING: Decompyle incomplete


class CompareInstr(Instruction):
    pass
# WARNING: Decompyle incomplete


class ICMPInstr(CompareInstr):
    OPNAME = 'icmp'
    VALID_OP = {
        'eq': 'equal',
        'ne': 'not equal',
        'ugt': 'unsigned greater than',
        'uge': 'unsigned greater or equal',
        'ult': 'unsigned less than',
        'ule': 'unsigned less or equal',
        'sgt': 'signed greater than',
        'sge': 'signed greater or equal',
        'slt': 'signed less than',
        'sle': 'signed less or equal' }
    VALID_FLAG = set()


class FCMPInstr(CompareInstr):
    __module__ = __name__
    __qualname__ = 'FCMPInstr'
    OPNAME = 'fcmp'
# WARNING: Decompyle incomplete


class CastInstr(Instruction):
    pass
# WARNING: Decompyle incomplete


class LoadInstr(Instruction):
    pass
# WARNING: Decompyle incomplete


class StoreInstr(Instruction):
    pass
# WARNING: Decompyle incomplete


class LoadAtomicInstr(Instruction):
    pass
# WARNING: Decompyle incomplete


class StoreAtomicInstr(Instruction):
    pass
# WARNING: Decompyle incomplete


class AllocaInstr(Instruction):
    pass
# WARNING: Decompyle incomplete


class GEPInstr(Instruction):
    pass
# WARNING: Decompyle incomplete


class PhiInstr(Instruction):
    pass
# WARNING: Decompyle incomplete


class ExtractElement(Instruction):
    pass
# WARNING: Decompyle incomplete


class InsertElement(Instruction):
    pass
# WARNING: Decompyle incomplete


class ShuffleVector(Instruction):
    pass
# WARNING: Decompyle incomplete


class ExtractValue(Instruction):
    pass
# WARNING: Decompyle incomplete


class InsertValue(Instruction):
    pass
# WARNING: Decompyle incomplete


class Unreachable(Instruction):
    pass
# WARNING: Decompyle incomplete


class InlineAsm(object):
    
    def __init__(self, ftype, asm, constraint, side_effect = (False,)):
        self.type = ftype.return_type
        self.function_type = ftype
        self.asm = asm
        self.constraint = constraint
        self.side_effect = side_effect

    
    def descr(self, buf):
        sideeffect = 'sideeffect' if self.side_effect else ''
        fmt = 'asm {sideeffect} "{asm}", "{constraint}"'
        buf.append(fmt.format(sideeffect = sideeffect, asm = self.asm, constraint = self.constraint))

    
    def get_reference(self):
        buf = []
        self.descr(buf)
        return ''.join(buf)

    
    def __str__(self):
        return '{0} {1}'.format(self.type, self.get_reference())



class AtomicRMW(Instruction):
    pass
# WARNING: Decompyle incomplete


class CmpXchg(Instruction):
    pass
# WARNING: Decompyle incomplete


class _LandingPadClause(object):
    
    def __init__(self, value):
        self.value = value

    
    def __str__(self):
        return '{kind} {type} {value}'.format(kind = self.kind, type = self.value.type, value = self.value.get_reference())



class CatchClause(_LandingPadClause):
    kind = 'catch'


class FilterClause(_LandingPadClause):
    pass
# WARNING: Decompyle incomplete


class LandingPadInstr(Instruction):
    pass
# WARNING: Decompyle incomplete


class Fence(Instruction):
    pass
# WARNING: Decompyle incomplete


class Comment(Instruction):
    pass
# WARNING: Decompyle incomplete
