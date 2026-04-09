# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bytes.pyc (Python 3.11)

'''
This file provides internal compiler utilities that support certain special
operations with bytes and workarounds for limitations enforced in userland.
'''
from numba.core.extending import intrinsic
from llvmlite import ir
from numba.core import types, cgutils
grab_byte = (lambda typingctx, data, offset: 
def impl(context, builder, signature, args):
(data, idx) = argsptr = builder.bitcast(data, ir.IntType(8).as_pointer())ch = builder.load(builder.gep(ptr, [
idx]))chsig = types.uint8(types.voidptr, types.intp)(sig, impl))()
grab_uint64_t = (lambda typingctx, data, offset: 
def impl(context, builder, signature, args):
(data, idx) = argsptr = builder.bitcast(data, ir.IntType(64).as_pointer())ch = builder.load(builder.gep(ptr, [
idx]))chsig = types.uint64(types.voidptr, types.intp)(sig, impl))()
memcpy_region = (lambda typingctx, dst, dst_offset, src, src_offset, nbytes, align: 
def codegen(context, builder, signature, args):
(dst_val, dst_offset_val, src_val, src_offset_val, nbytes_val, align_val) = argssrc_ptr = builder.gep(src_val, [
src_offset_val])dst_ptr = builder.gep(dst_val, [
dst_offset_val])cgutils.raw_memcpy(builder, dst_ptr, src_ptr, nbytes_val, align_val)context.get_dummy_value()sig = types.void(types.voidptr, types.intp, types.voidptr, types.intp, types.intp, types.intp)(sig, codegen))()
