# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: nrtdynmod.pyc (Python 3.11)

'''
Dynamically generate the NRT module
'''
from numba.core import config
from numba.core import types, cgutils
from llvmlite import ir, binding
_word_type = ir.IntType(config.MACHINE_BITS)
_pointer_type = ir.PointerType(ir.IntType(8))
_meminfo_struct_type = ir.LiteralStructType([
    _word_type,
    _pointer_type,
    _pointer_type,
    _pointer_type,
    _word_type])
incref_decref_ty = ir.FunctionType(ir.VoidType(), [
    _pointer_type])
meminfo_data_ty = ir.FunctionType(_pointer_type, [
    _pointer_type])

def _define_nrt_meminfo_data(module):
    '''
    Implement NRT_MemInfo_data_fast in the module.  This allows LLVM
    to inline lookup of the data pointer.
    '''
    fn = cgutils.get_or_insert_function(module, meminfo_data_ty, 'NRT_MemInfo_data_fast')
    builder = ir.IRBuilder(fn.append_basic_block())
    (ptr,) = fn.args
    struct_ptr = builder.bitcast(ptr, _meminfo_struct_type.as_pointer())
    data_ptr = builder.load(cgutils.gep(builder, struct_ptr, 0, 3))
    builder.ret(data_ptr)


def _define_nrt_incref(module, atomic_incr):
    '''
    Implement NRT_incref in the module
    '''
    fn_incref = cgutils.get_or_insert_function(module, incref_decref_ty, 'NRT_incref')
    fn_incref.attributes.add('noinline')
    builder = ir.IRBuilder(fn_incref.append_basic_block())
    (ptr,) = fn_incref.args
    is_null = builder.icmp_unsigned('==', ptr, cgutils.get_null_value(ptr.type))
    cgutils.if_unlikely(builder, is_null)
    builder.ret_void()
    None(None, None)


def _define_nrt_decref(module, atomic_decr):
