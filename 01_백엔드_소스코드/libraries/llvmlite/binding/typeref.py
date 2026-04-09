# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typeref.pyc (Python 3.11)

from ctypes import c_int, c_bool, c_void_p, c_uint64, c_uint, POINTER
import enum
from llvmlite import ir
from llvmlite.binding import ffi

class TypeKind(enum.IntEnum):
    void = 0
    half = 1
    float = 2
    double = 3
    x86_fp80 = 4
    fp128 = 5
    ppc_fp128 = 6
    label = 7
    integer = 8
    function = 9
    struct = 10
    array = 11
    pointer = 12
    vector = 13
    metadata = 14
    x86_mmx = 15
    token = 16
    scalable_vector = 17
    bfloat = 18
    x86_amx = 19

_TypeKindToIRType = {
    TypeKind.struct: ir.LiteralStructType,
    TypeKind.vector: ir.VectorType,
    TypeKind.array: ir.ArrayType,
    TypeKind.pointer: ir.PointerType,
    TypeKind.function: ir.FunctionType,
    TypeKind.integer: ir.IntType,
    TypeKind.double: ir.DoubleType,
    TypeKind.float: ir.FloatType,
    TypeKind.half: ir.HalfType,
    TypeKind.void: ir.VoidType }

class TypeRef(ffi.ObjectRef):
    '''A weak reference to a LLVM type
    '''
    name = (lambda self: ffi.ret_string(ffi.lib.LLVMPY_GetTypeName(self)))()
    is_struct = (lambda self: ffi.lib.LLVMPY_TypeIsStruct(self))()
    is_pointer = (lambda self: ffi.lib.LLVMPY_TypeIsPointer(self))()
    is_array = (lambda self: ffi.lib.LLVMPY_TypeIsArray(self))()
    is_vector = (lambda self: ffi.lib.LLVMPY_TypeIsVector(self))()
    is_function = (lambda self: ffi.lib.LLVMPY_TypeIsFunction(self))()
    is_function_vararg = (lambda self: if self.type_kind != TypeKind.function:
raise ValueError('Type {} is not a function'.format(self))ffi.lib.LLVMPY_IsFunctionVararg(self))()
    elements = (lambda self: if self.is_pointer:
raise ValueError("Type {} doesn't contain elements.".format(self))_TypeListIterator(ffi.lib.LLVMPY_ElementIter(self)))()
    element_count = (lambda self: if not self.is_array and self.is_vector:
raise ValueError('Type {} is not an array nor vector'.format(self))ffi.lib.LLVMPY_GetTypeElementCount(self))()
    type_width = (lambda self: ffi.lib.LLVMPY_GetTypeBitWidth(self))()
    type_kind = (lambda self: TypeKind(ffi.lib.LLVMPY_GetTypeKind(self)))()
    is_packed_struct = (lambda self: ffi.lib.LLVMPY_IsPackedStruct(self))()
    is_literal_struct = (lambda self: ffi.lib.LLVMPY_IsLiteralStruct(self))()
    is_opaque_struct = (lambda self: ffi.lib.LLVMPY_IsOpaqueStruct(self))()
    
    def get_function_parameters(self = property):
        nparams = ffi.lib.LLVMPY_CountParamTypes(self)
        if nparams > 0:
            out_buffer = ffi.LLVMTypeRef * nparams(None)
            ffi.lib.LLVMPY_GetParamTypes(self, out_buffer)
            return tuple(map(TypeRef, out_buffer))

    
    def get_function_return(self = property):
        return TypeRef(ffi.lib.LLVMPY_GetReturnType(self))

    
    def as_ir(self = property, ir_ctx = property):
        '''Convert into a ``llvmlite.ir.Type``.
        '''
        
        try:
            cls = _TypeKindToIRType[self.type_kind]
            return cls.from_llvm(self, ir_ctx)
        except KeyError:
            msg = f'''as_ir() unsupported for TypeRef of {self.type_kind}'''
            raise TypeError(msg)


    
    def __str__(self):
        return ffi.ret_string(ffi.lib.LLVMPY_PrintType(self))



class _TypeIterator(ffi.ObjectRef):
    
    def __next__(self):
        vp = self._next()
        if vp:
            return TypeRef(vp)
        raise None

    next = __next__
    
    def __iter__(self):
        return self



class _TypeListIterator(_TypeIterator):
    
    def _dispose(self):
        self._capi.LLVMPY_DisposeElementIter(self)

    
    def _next(self):
        return ffi.lib.LLVMPY_ElementIterNext(self)


ffi.lib.LLVMPY_PrintType.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_PrintType.restype = c_void_p
ffi.lib.LLVMPY_TypeIsPointer.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_TypeIsPointer.restype = c_bool
ffi.lib.LLVMPY_TypeIsArray.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_TypeIsArray.restype = c_bool
ffi.lib.LLVMPY_TypeIsVector.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_TypeIsVector.restype = c_bool
ffi.lib.LLVMPY_TypeIsStruct.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_TypeIsStruct.restype = c_bool
ffi.lib.LLVMPY_TypeIsFunction.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_TypeIsFunction.restype = c_bool
ffi.lib.LLVMPY_IsPackedStruct.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_IsPackedStruct.restype = c_bool
ffi.lib.LLVMPY_IsOpaqueStruct.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_IsOpaqueStruct.restype = c_bool
ffi.lib.LLVMPY_IsLiteralStruct.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_IsLiteralStruct.restype = c_bool
ffi.lib.LLVMPY_GetReturnType.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_GetReturnType.restype = ffi.LLVMTypeRef
ffi.lib.LLVMPY_CountParamTypes.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_CountParamTypes.restype = c_uint
ffi.lib.LLVMPY_GetParamTypes.argtypes = [
    ffi.LLVMTypeRef,
    POINTER(ffi.LLVMTypeRef)]
ffi.lib.LLVMPY_GetParamTypes.restype = None
ffi.lib.LLVMPY_IsFunctionVararg.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_IsFunctionVararg.restype = c_bool
ffi.lib.LLVMPY_GetTypeKind.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_GetTypeKind.restype = c_int
ffi.lib.LLVMPY_GetTypeElementCount.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_GetTypeElementCount.restype = c_int
ffi.lib.LLVMPY_GetTypeBitWidth.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_GetTypeBitWidth.restype = c_uint64
ffi.lib.LLVMPY_ElementIter.argtypes = [
    ffi.LLVMTypeRef]
ffi.lib.LLVMPY_ElementIter.restype = ffi.LLVMElementIterator
ffi.lib.LLVMPY_ElementIterNext.argtypes = [
    ffi.LLVMElementIterator]
ffi.lib.LLVMPY_ElementIterNext.restype = ffi.LLVMTypeRef
ffi.lib.LLVMPY_DisposeElementIter.argtypes = [
    ffi.LLVMElementIterator]
