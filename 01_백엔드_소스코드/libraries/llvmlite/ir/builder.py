# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: builder.pyc (Python 3.11)

import contextlib
import functools
from llvmlite.ir import instructions, types, values
_CMP_MAP = {
    '>': 'gt',
    '<': 'lt',
    '==': 'eq',
    '!=': 'ne',
    '>=': 'ge',
    '<=': 'le' }

def _unop(opname, cls = (instructions.Instruction,)):
    pass
# WARNING: Decompyle incomplete


def _binop(opname, cls = (instructions.Instruction,)):
    pass
# WARNING: Decompyle incomplete


def _binop_with_overflow(opname, cls = (instructions.Instruction,)):
    pass
# WARNING: Decompyle incomplete


def _uniop(opname, cls = (instructions.Instruction,)):
    pass
# WARNING: Decompyle incomplete


def _uniop_intrinsic_int(opname):
    pass
# WARNING: Decompyle incomplete


def _uniop_intrinsic_float(opname):
    pass
# WARNING: Decompyle incomplete


def _uniop_intrinsic_with_flag(opname):
    pass
# WARNING: Decompyle incomplete


def _triop_intrinsic(opname):
    pass
# WARNING: Decompyle incomplete


def _castop(opname, cls = (instructions.CastInstr,)):
    pass
# WARNING: Decompyle incomplete


def _label_suffix(label, suffix):
    """Returns (label + suffix) or a truncated version if it's too long.
    Parameters
    ----------
    label : str
        Label name
    suffix : str
        Label suffix
    """
    if len(label) > 50:
        nhead = 25
        return ''.join([
            label[:nhead],
            '..',
            suffix])
    return None + suffix


class IRBuilder(object):
    
    def __init__(self, block = (None,)):
        self._block = block
        self._anchor = len(block.instructions) if block else 0
        self.debug_metadata = None

    block = (lambda self: self._block)()
    basic_block = block
    function = (lambda self: self.block.parent)()
    module = (lambda self: self.block.parent.module)()
    
    def position_before(self, instr):
        """
        Position immediately before the given instruction.  The current block
        is also changed to the instruction's basic block.
        """
        self._block = instr.parent
        self._anchor = self._block.instructions.index(instr)

    
    def position_after(self, instr):
        """
        Position immediately after the given instruction.  The current block
        is also changed to the instruction's basic block.
        """
        self._block = instr.parent
        self._anchor = self._block.instructions.index(instr) + 1

    
    def position_at_start(self, block):
        '''
        Position at the start of the basic *block*.
        '''
        self._block = block
        self._anchor = 0

    
    def position_at_end(self, block):
        '''
        Position at the end of the basic *block*.
        '''
        self._block = block
        self._anchor = len(block.instructions)

    
    def append_basic_block(self, name = ('',)):
        '''
        Append a basic block, with the given optional *name*, to the current
        function.  The current block is not changed.  The new block is returned.
        '''
        return self.function.append_basic_block(name)

    
    def remove(self, instr):
        '''Remove the given instruction.'''
        idx = self._block.instructions.index(instr)
        del self._block.instructions[idx]
        if self._block.terminator == instr:
            self._block.terminator = None
        if self._anchor > idx:
            return None

    goto_block = (lambda self, block: pass# WARNING: Decompyle incomplete
)()
    goto_entry_block = (lambda self: pass# WARNING: Decompyle incomplete
)()
    _branch_helper = (lambda self, bbenter, bbexit: pass# WARNING: Decompyle incomplete
)()
    if_then = (lambda self, pred, likely = (None,): pass# WARNING: Decompyle incomplete
)()
    if_else = (lambda self, pred, likely = (None,): pass# WARNING: Decompyle incomplete
)()
    
    def _insert(self, instr):
        pass
    # WARNING: Decompyle incomplete

    
    def _set_terminator(self, term):
        pass
    # WARNING: Decompyle incomplete

    shl = (lambda self, lhs, rhs, name = ('',): pass)()
    lshr = (lambda self, lhs, rhs, name = ('',): pass)()
    ashr = (lambda self, lhs, rhs, name = ('',): pass)()
    add = (lambda self, lhs, rhs, name = ('',): pass)()
    fadd = (lambda self, lhs, rhs, name = ('',): pass)()
    sub = (lambda self, lhs, rhs, name = ('',): pass)()
    fsub = (lambda self, lhs, rhs, name = ('',): pass)()
    mul = (lambda self, lhs, rhs, name = ('',): pass)()
    fmul = (lambda self, lhs, rhs, name = ('',): pass)()
    udiv = (lambda self, lhs, rhs, name = ('',): pass)()
    sdiv = (lambda self, lhs, rhs, name = ('',): pass)()
    fdiv = (lambda self, lhs, rhs, name = ('',): pass)()
    urem = (lambda self, lhs, rhs, name = ('',): pass)()
    srem = (lambda self, lhs, rhs, name = ('',): pass)()
    frem = (lambda self, lhs, rhs, name = ('',): pass)()
    or_ = (lambda self, lhs, rhs, name = ('',): pass)()
    and_ = (lambda self, lhs, rhs, name = ('',): pass)()
    xor = (lambda self, lhs, rhs, name = ('',): pass)()
    sadd_with_overflow = (lambda self, lhs, rhs, name = ('',): pass)()
    smul_with_overflow = (lambda self, lhs, rhs, name = ('',): pass)()
    ssub_with_overflow = (lambda self, lhs, rhs, name = ('',): pass)()
    uadd_with_overflow = (lambda self, lhs, rhs, name = ('',): pass)()
    umul_with_overflow = (lambda self, lhs, rhs, name = ('',): pass)()
    usub_with_overflow = (lambda self, lhs, rhs, name = ('',): pass)()
    
    def not_(self, value, name = ('',)):
        '''
        Bitwise integer complement:
            name = ~value
        '''
        if isinstance(value.type, types.VectorType):
            rhs = values.Constant(value.type, (-1,) * value.type.count)
        else:
            rhs = values.Constant(value.type, -1)
        return self.xor(value, rhs, name = name)

    
    def neg(self, value, name = ('',)):
        '''
        Integer negative:
            name = -value
        '''
        return self.sub(values.Constant(value.type, 0), value, name = name)

    fneg = (lambda self, arg, name, flags = ('', ()): pass)()
    
    def _icmp(self, prefix, cmpop, lhs, rhs, name):
        
        try:
            op = _CMP_MAP[cmpop]
        except KeyError:
            raise ValueError(f'''invalid comparison {cmpop!r} for icmp''')

        if cmpop not in ('==', '!='):
            op = prefix + op
        instr = instructions.ICMPInstr(self.block, op, lhs, rhs, name = name)
        self._insert(instr)
        return instr

    
    def icmp_signed(self, cmpop, lhs, rhs, name = ('',)):
        """
        Signed integer comparison:
            name = lhs <cmpop> rhs

        where cmpop can be '==', '!=', '<', '<=', '>', '>='
        """
        return self._icmp('s', cmpop, lhs, rhs, name)

    
    def icmp_unsigned(self, cmpop, lhs, rhs, name = ('',)):
        """
        Unsigned integer (or pointer) comparison:
            name = lhs <cmpop> rhs

        where cmpop can be '==', '!=', '<', '<=', '>', '>='
        """
        return self._icmp('u', cmpop, lhs, rhs, name)

    
    def fcmp_ordered(self, cmpop, lhs, rhs, name, flags = ('', ())):
        """
        Floating-point ordered comparison:
            name = lhs <cmpop> rhs

        where cmpop can be '==', '!=', '<', '<=', '>', '>=', 'ord', 'uno'
        """
        if cmpop in _CMP_MAP:
            op = 'o' + _CMP_MAP[cmpop]
        else:
            op = cmpop
        instr = instructions.FCMPInstr(self.block, op, lhs, rhs, name = name, flags = flags)
        self._insert(instr)
        return instr

    
    def fcmp_unordered(self, cmpop, lhs, rhs, name, flags = ('', ())):
        """
        Floating-point unordered comparison:
            name = lhs <cmpop> rhs

        where cmpop can be '==', '!=', '<', '<=', '>', '>=', 'ord', 'uno'
        """
        if cmpop in _CMP_MAP:
            op = 'u' + _CMP_MAP[cmpop]
        else:
            op = cmpop
        instr = instructions.FCMPInstr(self.block, op, lhs, rhs, name = name, flags = flags)
        self._insert(instr)
        return instr

    
    def select(self, cond, lhs, rhs, name, flags = ('', ())):
        '''
        Ternary select operator:
            name = cond ? lhs : rhs
        '''
        instr = instructions.SelectInstr(self.block, cond, lhs, rhs, name = name, flags = flags)
        self._insert(instr)
        return instr

    trunc = (lambda self, value, typ, name = ('',): pass)()
    zext = (lambda self, value, typ, name = ('',): pass)()
    sext = (lambda self, value, typ, name = ('',): pass)()
    fptrunc = (lambda self, value, typ, name = ('',): pass)()
    fpext = (lambda self, value, typ, name = ('',): pass)()
    bitcast = (lambda self, value, typ, name = ('',): pass)()
    addrspacecast = (lambda self, value, typ, name = ('',): pass)()
    fptoui = (lambda self, value, typ, name = ('',): pass)()
    uitofp = (lambda self, value, typ, name = ('',): pass)()
    fptosi = (lambda self, value, typ, name = ('',): pass)()
    sitofp = (lambda self, value, typ, name = ('',): pass)()
    ptrtoint = (lambda self, value, typ, name = ('',): pass)()
    inttoptr = (lambda self, value, typ, name = ('',): pass)()
    
    def alloca(self, typ, size, name = (None, '')):
        '''
        Stack-allocate a slot for *size* elements of the given type.
        (default one element)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def load(self, ptr, name, align, typ = ('', None, None)):
        '''
        Load value from pointer, with optional guaranteed alignment:
            name = *ptr
        '''
        if not isinstance(ptr.type, types.PointerType):
            msg = 'cannot load from value of type %s (%r): not a pointer'
            raise TypeError(msg % (ptr.type, str(ptr)))
        ld = instructions.LoadInstr(self.block, ptr, name, typ = typ)
        ld.align = align
        self._insert(ld)
        return ld

    
    def store(self, value, ptr, align = (None,)):
        '''
        Store value to pointer, with optional guaranteed alignment:
            *ptr = name
        '''
        if not isinstance(ptr.type, types.PointerType):
            msg = 'cannot store to value of type %s (%r): not a pointer'
            raise TypeError(msg % (ptr.type, str(ptr)))
        if ptr.type.is_opaque and ptr.type.pointee != value.type:
            raise TypeError(f'''cannot store {value.type!s} to {ptr.type!s}: mismatching types''')
        st = instructions.StoreInstr(self.block, value, ptr)
        st.align = align
        self._insert(st)
        return st

    
    def load_atomic(self, ptr, ordering, align, name, typ = ('', None)):
        '''
        Load value from pointer, with optional guaranteed alignment:
            name = *ptr
        '''
        if not isinstance(ptr.type, types.PointerType):
            msg = 'cannot load from value of type %s (%r): not a pointer'
            raise TypeError(msg % (ptr.type, str(ptr)))
        ld = instructions.LoadAtomicInstr(self.block, ptr, ordering, align, name, typ = typ)
        self._insert(ld)
        return ld

    
    def store_atomic(self, value, ptr, ordering, align):
        '''
        Store value to pointer, with optional guaranteed alignment:
            *ptr = name
        '''
        if not isinstance(ptr.type, types.PointerType):
            msg = 'cannot store to value of type %s (%r): not a pointer'
            raise TypeError(msg % (ptr.type, str(ptr)))
        if ptr.type.pointee != value.type:
            raise TypeError(f'''cannot store {value.type!s} to {ptr.type!s}: mismatching types''')
        st = instructions.StoreAtomicInstr(self.block, value, ptr, ordering, align)
        self._insert(st)
        return st

    
    def switch(self, value, default):
        '''
        Create a switch-case with a single *default* target.
        '''
        swt = instructions.SwitchInstr(self.block, 'switch', value, default)
        self._set_terminator(swt)
        return swt

    
    def branch(self, target):
        '''
        Unconditional branch to *target*.
        '''
        br = instructions.Branch(self.block, 'br', [
            target])
        self._set_terminator(br)
        return br

    
    def cbranch(self, cond, truebr, falsebr):
        '''
        Conditional branch to *truebr* if *cond* is true, else to *falsebr*.
        '''
        br = instructions.ConditionalBranch(self.block, 'br', [
            cond,
            truebr,
            falsebr])
        self._set_terminator(br)
        return br

    
    def branch_indirect(self, addr):
        '''
        Indirect branch to target *addr*.
        '''
        br = instructions.IndirectBranch(self.block, 'indirectbr', addr)
        self._set_terminator(br)
        return br

    
    def ret_void(self):
        '''
        Return from function without a value.
        '''
        return self._set_terminator(instructions.Ret(self.block, 'ret void'))

    
    def ret(self, value):
        '''
        Return from function with the given *value*.
        '''
        return self._set_terminator(instructions.Ret(self.block, 'ret', value))

    
    def resume(self, landingpad):
        '''
        Resume an in-flight exception.
        '''
        br = instructions.Branch(self.block, 'resume', [
            landingpad])
        self._set_terminator(br)
        return br

    
    def call(self, fn, args, name, cconv, tail, fastmath, attrs, arg_attrs = ('', None, False, (), (), None)):
        '''
        Call function *fn* with *args*:
            name = fn(args...)
        '''
        inst = instructions.CallInstr(self.block, fn, args, name = name, cconv = cconv, tail = tail, fastmath = fastmath, attrs = attrs, arg_attrs = arg_attrs)
        self._insert(inst)
        return inst

    
    def asm(self, ftype, asm, constraint, args, side_effect, name = ('',)):
        '''
        Inline assembler.
        '''
        asm = instructions.InlineAsm(ftype, asm, constraint, side_effect)
        return self.call(asm, args, name)

    
    def load_reg(self, reg_type, reg_name, name = ('',)):
        '''
        Load a register value into an LLVM value.
          Example: v = load_reg(IntType(32), "eax")
        '''
        ftype = types.FunctionType(reg_type, [])
        return self.asm(ftype, '', '={%s}' % reg_name, [], False, name)

    
    def store_reg(self, value, reg_type, reg_name, name = ('',)):
        '''
        Store an LLVM value inside a register
        Example:
          store_reg(Constant(IntType(32), 0xAAAAAAAA), IntType(32), "eax")
        '''
        ftype = types.FunctionType(types.VoidType(), [
            reg_type])
        return self.asm(ftype, '', '{%s}' % reg_name, [
            value], True, name)

    
    def invoke(self, fn, args, normal_to, unwind_to, name, cconv, fastmath, attrs, arg_attrs = ('', None, (), (), None)):
        inst = instructions.InvokeInstr(self.block, fn, args, normal_to, unwind_to, name = name, cconv = cconv, fastmath = fastmath, attrs = attrs, arg_attrs = arg_attrs)
        self._set_terminator(inst)
        return inst

    
    def gep(self, ptr, indices, inbounds, name, source_etype = (False, '', None)):
        '''
        Compute effective address (getelementptr):
            name = getelementptr ptr, <indices...>
        '''
        instr = instructions.GEPInstr(self.block, ptr, indices, inbounds = inbounds, name = name, source_etype = source_etype)
        self._insert(instr)
        return instr

    
    def extract_element(self, vector, idx, name = ('',)):
        '''
        Returns the value at position idx.
        '''
        instr = instructions.ExtractElement(self.block, vector, idx, name = name)
        self._insert(instr)
        return instr

    
    def insert_element(self, vector, value, idx, name = ('',)):
        '''
        Returns vector with vector[idx] replaced by value.
        The result is undefined if the idx is larger or equal the vector length.
        '''
        instr = instructions.InsertElement(self.block, vector, value, idx, name = name)
        self._insert(instr)
        return instr

    
    def shuffle_vector(self, vector1, vector2, mask, name = ('',)):
        '''
        Constructs a permutation of elements from *vector1* and *vector2*.
        Returns a new vector in the same length of *mask*.

        * *vector1* and *vector2* must have the same element type.
        * *mask* must be a constant vector of integer types.
        '''
        instr = instructions.ShuffleVector(self.block, vector1, vector2, mask, name = name)
        self._insert(instr)
        return instr

    
    def extract_value(self, agg, idx, name = ('',)):
        '''
        Extract member number *idx* from aggregate.
        '''
        if not isinstance(idx, (tuple, list)):
            idx = [
                idx]
        instr = instructions.ExtractValue(self.block, agg, idx, name = name)
        self._insert(instr)
        return instr

    
    def insert_value(self, agg, value, idx, name = ('',)):
        '''
        Insert *value* into member number *idx* from aggregate.
        '''
        if not isinstance(idx, (tuple, list)):
            idx = [
                idx]
        instr = instructions.InsertValue(self.block, agg, value, idx, name = name)
        self._insert(instr)
        return instr

    
    def phi(self, typ, name, flags = ('', ())):
        inst = instructions.PhiInstr(self.block, typ, name = name, flags = flags)
        self._insert(inst)
        return inst

    
    def unreachable(self):
        inst = instructions.Unreachable(self.block)
        self._set_terminator(inst)
        return inst

    
    def atomic_rmw(self, op, ptr, val, ordering, name = ('',)):
        inst = instructions.AtomicRMW(self.block, op, ptr, val, ordering, name = name)
        self._insert(inst)
        return inst

    
    def cmpxchg(self, ptr, cmp, val, ordering, failordering, name = (None, '')):
        '''
        Atomic compared-and-set:
            atomic {
                old = *ptr
                success = (old == cmp)
                if (success)
                    *ptr = val
                }
            name = { old, success }

        If failordering is `None`, the value of `ordering` is used.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def landingpad(self, typ, name, cleanup = ('', False)):
        inst = instructions.LandingPadInstr(self.block, typ, name, cleanup)
        self._insert(inst)
        return inst

    
    def assume(self, cond):
        '''
        Optimizer hint: assume *cond* is always true.
        '''
        fn = self.module.declare_intrinsic('llvm.assume')
        return self.call(fn, [
            cond])

    
    def fence(self, ordering, targetscope, name = (None, '')):
        '''
        Add a memory barrier, preventing certain reorderings of load and/or
        store accesses with
        respect to other processors and devices.
        '''
        inst = instructions.Fence(self.block, ordering, targetscope, name = name)
        self._insert(inst)
        return inst

    
    def comment(self, text):
        '''
        Puts a single-line comment into the generated IR. This will be ignored
        by LLVM, but can be useful for debugging the output of a compiler. Adds
        a comment to the source file.

        * *text* is a string that does not contain new line characters.
        '''
        inst = instructions.Comment(self.block, text)
        self._insert(inst)
        return inst

    bswap = (lambda self, cond: pass)()
    bitreverse = (lambda self, cond: pass)()
    ctpop = (lambda self, cond: pass)()
    ctlz = (lambda self, cond, flag: pass)()
    cttz = (lambda self, cond, flag: pass)()
    fma = (lambda self, a, b, c: pass)()
    
    def convert_from_fp16(self, a, to, name = (None, '')):
        '''
        Convert from an i16 to the given FP type
        '''
        if not to:
            raise TypeError('expected a float return type')
        if not isinstance(to, (types.FloatType, types.DoubleType)):
            raise TypeError('expected a float type, got %s' % to)
        if not isinstance(a.type, types.IntType) or a.type.width == 16:
            raise TypeError('expected an i16 type, got %s' % a.type)
        opname = 'llvm.convert.from.fp16'
        fn = self.module.declare_intrinsic(opname, [
            to])
        return self.call(fn, [
            a], name)

    convert_to_fp16 = (lambda self, a: pass)()
