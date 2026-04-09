# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: value.pyc (Python 3.11)

from ctypes import POINTER, byref, cast, c_char_p, c_double, c_int, c_size_t, c_uint, c_uint64, c_bool, c_void_p
import enum
from llvmlite.binding import ffi
from llvmlite.binding.common import _decode_string, _encode_string
from llvmlite.binding.typeref import TypeRef

class Linkage(enum.IntEnum):
    external = 0
    available_externally = 1
    linkonce_any = 2
    linkonce_odr = 3
    linkonce_odr_autohide = 4
    weak_any = 5
    weak_odr = 6
    appending = 7
    internal = 8
    private = 9
    dllimport = 10
    dllexport = 11
    external_weak = 12
    ghost = 13
    common = 14
    linker_private = 15
    linker_private_weak = 16


class Visibility(enum.IntEnum):
    default = 0
    hidden = 1
    protected = 2


class StorageClass(enum.IntEnum):
    default = 0
    dllimport = 1
    dllexport = 2


class ValueKind(enum.IntEnum):
    argument = 0
    basic_block = 1
    memory_use = 2
    memory_def = 3
    memory_phi = 4
    function = 5
    global_alias = 6
    global_ifunc = 7
    global_variable = 8
    block_address = 9
    constant_expr = 10
    constant_array = 11
    constant_struct = 12
    constant_vector = 13
    undef_value = 14
    constant_aggregate_zero = 15
    constant_data_array = 16
    constant_data_vector = 17
    constant_int = 18
    constant_fp = 19
    constant_pointer_null = 20
    constant_token_none = 21
    metadata_as_value = 22
    inline_asm = 23
    instruction = 24
    poison_value = 25


class ValueRef(ffi.ObjectRef):
    '''A weak reference to a LLVM value.
    '''
    
    def __init__(self, ptr, kind, parents):
        self._kind = kind
        self._parents = parents
        ffi.ObjectRef.__init__(self, ptr)

    
    def __str__(self):
        outstr = ffi.OutputString()
        ffi.lib.LLVMPY_PrintValueToString(self, outstr)
        None(None, None)
        return 
        with None:
            if not None, str(outstr):
                pass

    module = (lambda self: self._parents.get('module'))()
    function = (lambda self: self._parents.get('function'))()
    block = (lambda self: self._parents.get('block'))()
    instruction = (lambda self: self._parents.get('instruction'))()
    is_global = (lambda self: self._kind == 'global')()
    is_function = (lambda self: self._kind == 'function')()
    is_block = (lambda self: self._kind == 'block')()
    is_argument = (lambda self: self._kind == 'argument')()
    is_instruction = (lambda self: self._kind == 'instruction')()
    is_operand = (lambda self: self._kind == 'operand')()
    is_constant = (lambda self: bool(ffi.lib.LLVMPY_IsConstant(self)))()
    value_kind = (lambda self: ValueKind(ffi.lib.LLVMPY_GetValueKind(self)))()
    name = (lambda self: _decode_string(ffi.lib.LLVMPY_GetValueName(self)))()
    name = (lambda self, val: ffi.lib.LLVMPY_SetValueName(self, _encode_string(val)))()
    linkage = (lambda self: Linkage(ffi.lib.LLVMPY_GetLinkage(self)))()
    linkage = (lambda self, value: if not isinstance(value, Linkage):
value = Linkage[value]ffi.lib.LLVMPY_SetLinkage(self, value))()
    visibility = (lambda self: Visibility(ffi.lib.LLVMPY_GetVisibility(self)))()
    visibility = (lambda self, value: if not isinstance(value, Visibility):
value = Visibility[value]ffi.lib.LLVMPY_SetVisibility(self, value))()
    storage_class = (lambda self: StorageClass(ffi.lib.LLVMPY_GetDLLStorageClass(self)))()
    storage_class = (lambda self, value: if not isinstance(value, StorageClass):
value = StorageClass[value]ffi.lib.LLVMPY_SetDLLStorageClass(self, value))()
    
    def add_function_attribute(self, attr):
        '''Only works on function value

        Parameters
        -----------
        attr : str
            attribute name
        '''
        if not self.is_function:
            raise ValueError(f'''expected function value, got {self._kind!s}''')
        attrname = str(attr)
        attrval = ffi.lib.LLVMPY_GetEnumAttributeKindForName(_encode_string(attrname), len(attrname))
        if attrval == 0:
            raise ValueError('no such attribute {!r}'.format(attrname))
        ffi.lib.LLVMPY_AddFunctionAttr(self, attrval)

    type = (lambda self: TypeRef(ffi.lib.LLVMPY_TypeOf(self)))()
    global_value_type = (lambda self: pass# WARNING: Decompyle incomplete
)()
    is_declaration = (lambda self: if not self.is_global and self.is_function:
raise ValueError(f'''expected global or function value, got {self._kind!s}''')ffi.lib.LLVMPY_IsDeclaration(self))()
    attributes = (lambda self: itr = iter(())if self.is_function:
it = ffi.lib.LLVMPY_FunctionAttributesIter(self)itr = _AttributeListIterator(it)elif self.is_instruction:
if self.opcode == 'call':
it = ffi.lib.LLVMPY_CallInstAttributesIter(self)itr = _AttributeListIterator(it)elif self.opcode == 'invoke':
it = ffi.lib.LLVMPY_InvokeInstAttributesIter(self)itr = _AttributeListIterator(it)elif self.is_global:
it = ffi.lib.LLVMPY_GlobalAttributesIter(self)itr = _AttributeSetIterator(it)elif self.is_argument:
it = ffi.lib.LLVMPY_ArgumentAttributesIter(self)itr = _AttributeSetIterator(it)itr)()
    blocks = (lambda self: if not self.is_function:
raise ValueError(f'''expected function value, got {self._kind!s}''')it = ffi.lib.LLVMPY_FunctionBlocksIter(self)parents = self._parents.copy()parents.update(function = self)_BlocksIterator(it, parents))()
    arguments = (lambda self: if not self.is_function:
raise ValueError(f'''expected function value, got {self._kind!s}''')it = ffi.lib.LLVMPY_FunctionArgumentsIter(self)parents = self._parents.copy()parents.update(function = self)_ArgumentsIterator(it, parents))()
    instructions = (lambda self: if not self.is_block:
raise ValueError(f'''expected block value, got {self._kind!s}''')it = ffi.lib.LLVMPY_BlockInstructionsIter(self)parents = self._parents.copy()parents.update(block = self)_InstructionsIterator(it, parents))()
    operands = (lambda self: if not self.is_instruction:
raise ValueError(f'''expected instruction value, got {self._kind!s}''')it = ffi.lib.LLVMPY_InstructionOperandsIter(self)parents = self._parents.copy()parents.update(instruction = self)_OperandsIterator(it, parents))()
    opcode = (lambda self: if not self.is_instruction:
raise ValueError(f'''expected instruction value, got {self._kind!s}''')ffi.ret_string(ffi.lib.LLVMPY_GetOpcodeName(self)))()
    incoming_blocks = (lambda self: if self.is_instruction or self.opcode != 'phi':
raise ValueError(f'''expected phi instruction value, got {self._kind!s}''')it = ffi.lib.LLVMPY_PhiIncomingBlocksIter(self)parents = self._parents.copy()parents.update(instruction = self)_IncomingBlocksIterator(it, parents))()
    
    def get_constant_value(self, signed_int, round_fp = (False, False)):
        '''
        Return the constant value, either as a literal (when supported)
        or as a string.

        Parameters
        -----------
        signed_int : bool
            if True and the constant is an integer, returns a signed version
        round_fp : bool
            if True and the constant is a floating point value, rounds the
            result upon accuracy loss (e.g., when querying an fp128 value).
            By default, raises an exception on accuracy loss
        '''
        if not self.is_constant:
            raise ValueError(f'''expected constant value, got {self._kind!s}''')
        if self.value_kind == ValueKind.constant_int:
            little_endian = c_bool(False)
            words = ffi.lib.LLVMPY_GetConstantIntNumWords(self)
            ptr = ffi.lib.LLVMPY_GetConstantIntRawValue(self, byref(little_endian))
            asbytes = bytes(cast(ptr, POINTER(c_uint64 * words)).contents)
            return int.from_bytes(asbytes, 'little' if little_endian.value else 'big', signed = signed_int)
        if None.value_kind == ValueKind.constant_fp:
            accuracy_loss = c_bool(False)
            value = ffi.lib.LLVMPY_GetConstantFPValue(self, byref(accuracy_loss))
            if not accuracy_loss.value and round_fp:
                raise ValueError(f'''Accuracy loss encountered in conversion of constant value {str(self)}''')
            return value
        return None(self)



class _ValueIterator(ffi.ObjectRef):
    kind = None
    
    def __init__(self, ptr, parents):
        ffi.ObjectRef.__init__(self, ptr)
        self._parents = parents
    # WARNING: Decompyle incomplete

    
    def __next__(self):
        vp = self._next()
        if vp:
            return ValueRef(vp, self.kind, self._parents)
        raise None

    next = __next__
    
    def __iter__(self):
        return self



class _AttributeIterator(ffi.ObjectRef):
    
    def __next__(self):
        vp = self._next()
        if vp:
            return vp
        raise None

    next = __next__
    
    def __iter__(self):
        return self



class _AttributeListIterator(_AttributeIterator):
    
    def _dispose(self):
        self._capi.LLVMPY_DisposeAttributeListIter(self)

    
    def _next(self):
        return ffi.ret_bytes(ffi.lib.LLVMPY_AttributeListIterNext(self))



class _AttributeSetIterator(_AttributeIterator):
    
    def _dispose(self):
        self._capi.LLVMPY_DisposeAttributeSetIter(self)

    
    def _next(self):
        return ffi.ret_bytes(ffi.lib.LLVMPY_AttributeSetIterNext(self))



class _BlocksIterator(_ValueIterator):
    kind = 'block'
    
    def _dispose(self):
        self._capi.LLVMPY_DisposeBlocksIter(self)

    
    def _next(self):
        return ffi.lib.LLVMPY_BlocksIterNext(self)



class _ArgumentsIterator(_ValueIterator):
    kind = 'argument'
    
    def _dispose(self):
        self._capi.LLVMPY_DisposeArgumentsIter(self)

    
    def _next(self):
        return ffi.lib.LLVMPY_ArgumentsIterNext(self)



class _InstructionsIterator(_ValueIterator):
    kind = 'instruction'
    
    def _dispose(self):
        self._capi.LLVMPY_DisposeInstructionsIter(self)

    
    def _next(self):
        return ffi.lib.LLVMPY_InstructionsIterNext(self)



class _OperandsIterator(_ValueIterator):
    kind = 'operand'
    
    def _dispose(self):
        self._capi.LLVMPY_DisposeOperandsIter(self)

    
    def _next(self):
        return ffi.lib.LLVMPY_OperandsIterNext(self)



class _IncomingBlocksIterator(_ValueIterator):
    kind = 'block'
    
    def _dispose(self):
        self._capi.LLVMPY_DisposeIncomingBlocksIter(self)

    
    def _next(self):
        return ffi.lib.LLVMPY_IncomingBlocksIterNext(self)


ffi.lib.LLVMPY_PrintValueToString.argtypes = [
    ffi.LLVMValueRef,
    POINTER(c_char_p)]
ffi.lib.LLVMPY_GetGlobalParent.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_GetGlobalParent.restype = ffi.LLVMModuleRef
ffi.lib.LLVMPY_GetValueName.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_GetValueName.restype = c_char_p
ffi.lib.LLVMPY_SetValueName.argtypes = [
    ffi.LLVMValueRef,
    c_char_p]
ffi.lib.LLVMPY_TypeOf.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_TypeOf.restype = ffi.LLVMTypeRef
ffi.lib.LLVMPY_GlobalGetValueType.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_GlobalGetValueType.restype = ffi.LLVMTypeRef
ffi.lib.LLVMPY_GetTypeName.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_GetTypeName.restype = c_void_p
ffi.lib.LLVMPY_GetLinkage.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_GetLinkage.restype = c_int
ffi.lib.LLVMPY_SetLinkage.argtypes = [
    ffi.LLVMValueRef,
    c_int]
ffi.lib.LLVMPY_GetVisibility.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_GetVisibility.restype = c_int
ffi.lib.LLVMPY_SetVisibility.argtypes = [
    ffi.LLVMValueRef,
    c_int]
ffi.lib.LLVMPY_GetDLLStorageClass.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_GetDLLStorageClass.restype = c_int
ffi.lib.LLVMPY_SetDLLStorageClass.argtypes = [
    ffi.LLVMValueRef,
    c_int]
ffi.lib.LLVMPY_GetEnumAttributeKindForName.argtypes = [
    c_char_p,
    c_size_t]
ffi.lib.LLVMPY_GetEnumAttributeKindForName.restype = c_uint
ffi.lib.LLVMPY_AddFunctionAttr.argtypes = [
    ffi.LLVMValueRef,
    c_uint]
ffi.lib.LLVMPY_IsDeclaration.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_IsDeclaration.restype = c_int
ffi.lib.LLVMPY_FunctionAttributesIter.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_FunctionAttributesIter.restype = ffi.LLVMAttributeListIterator
ffi.lib.LLVMPY_CallInstAttributesIter.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_CallInstAttributesIter.restype = ffi.LLVMAttributeListIterator
ffi.lib.LLVMPY_InvokeInstAttributesIter.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_InvokeInstAttributesIter.restype = ffi.LLVMAttributeListIterator
ffi.lib.LLVMPY_GlobalAttributesIter.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_GlobalAttributesIter.restype = ffi.LLVMAttributeSetIterator
ffi.lib.LLVMPY_ArgumentAttributesIter.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_ArgumentAttributesIter.restype = ffi.LLVMAttributeSetIterator
ffi.lib.LLVMPY_FunctionBlocksIter.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_FunctionBlocksIter.restype = ffi.LLVMBlocksIterator
ffi.lib.LLVMPY_FunctionArgumentsIter.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_FunctionArgumentsIter.restype = ffi.LLVMArgumentsIterator
ffi.lib.LLVMPY_BlockInstructionsIter.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_BlockInstructionsIter.restype = ffi.LLVMInstructionsIterator
ffi.lib.LLVMPY_InstructionOperandsIter.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_InstructionOperandsIter.restype = ffi.LLVMOperandsIterator
ffi.lib.LLVMPY_PhiIncomingBlocksIter.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_PhiIncomingBlocksIter.restype = ffi.LLVMIncomingBlocksIterator
ffi.lib.LLVMPY_DisposeAttributeListIter.argtypes = [
    ffi.LLVMAttributeListIterator]
ffi.lib.LLVMPY_DisposeAttributeSetIter.argtypes = [
    ffi.LLVMAttributeSetIterator]
ffi.lib.LLVMPY_DisposeBlocksIter.argtypes = [
    ffi.LLVMBlocksIterator]
ffi.lib.LLVMPY_DisposeInstructionsIter.argtypes = [
    ffi.LLVMInstructionsIterator]
ffi.lib.LLVMPY_DisposeOperandsIter.argtypes = [
    ffi.LLVMOperandsIterator]
ffi.lib.LLVMPY_DisposeIncomingBlocksIter.argtypes = [
    ffi.LLVMIncomingBlocksIterator]
ffi.lib.LLVMPY_AttributeListIterNext.argtypes = [
    ffi.LLVMAttributeListIterator]
ffi.lib.LLVMPY_AttributeListIterNext.restype = c_void_p
ffi.lib.LLVMPY_AttributeSetIterNext.argtypes = [
    ffi.LLVMAttributeSetIterator]
ffi.lib.LLVMPY_AttributeSetIterNext.restype = c_void_p
ffi.lib.LLVMPY_BlocksIterNext.argtypes = [
    ffi.LLVMBlocksIterator]
ffi.lib.LLVMPY_BlocksIterNext.restype = ffi.LLVMValueRef
ffi.lib.LLVMPY_ArgumentsIterNext.argtypes = [
    ffi.LLVMArgumentsIterator]
ffi.lib.LLVMPY_ArgumentsIterNext.restype = ffi.LLVMValueRef
ffi.lib.LLVMPY_InstructionsIterNext.argtypes = [
    ffi.LLVMInstructionsIterator]
ffi.lib.LLVMPY_InstructionsIterNext.restype = ffi.LLVMValueRef
ffi.lib.LLVMPY_OperandsIterNext.argtypes = [
    ffi.LLVMOperandsIterator]
ffi.lib.LLVMPY_OperandsIterNext.restype = ffi.LLVMValueRef
ffi.lib.LLVMPY_IncomingBlocksIterNext.argtypes = [
    ffi.LLVMIncomingBlocksIterator]
ffi.lib.LLVMPY_IncomingBlocksIterNext.restype = ffi.LLVMValueRef
ffi.lib.LLVMPY_GetOpcodeName.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_GetOpcodeName.restype = c_void_p
ffi.lib.LLVMPY_IsConstant.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_IsConstant.restype = c_bool
ffi.lib.LLVMPY_GetValueKind.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_GetValueKind.restype = c_int
ffi.lib.LLVMPY_GetConstantIntRawValue.argtypes = [
    ffi.LLVMValueRef,
    POINTER(c_bool)]
ffi.lib.LLVMPY_GetConstantIntRawValue.restype = POINTER(c_uint64)
ffi.lib.LLVMPY_GetConstantIntNumWords.argtypes = [
    ffi.LLVMValueRef]
ffi.lib.LLVMPY_GetConstantIntNumWords.restype = c_uint
ffi.lib.LLVMPY_GetConstantFPValue.argtypes = [
    ffi.LLVMValueRef,
    POINTER(c_bool)]
ffi.lib.LLVMPY_GetConstantFPValue.restype = c_double
