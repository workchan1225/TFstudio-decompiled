# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: printimpl.pyc (Python 3.11)

from functools import singledispatch
from llvmlite import ir
from numba.core import types, cgutils
from numba.core.errors import NumbaWarning
from numba.core.imputils import Registry
from numba.cuda import nvvmutils
from warnings import warn
registry = Registry()
lower = registry.lower
voidptr = ir.PointerType(ir.IntType(8))
print_item = (lambda ty, context, builder, val: raise NotImplementedError(f'''printing unimplemented for values of type {ty!s}'''))()
int_print_impl = (lambda ty, context, builder, val: if ty in types.unsigned_domain:
rawfmt = '%llu'dsttype = types.uint64else:
rawfmt = '%lld'dsttype = types.int64lld = context.cast(builder, val, ty, dsttype)(rawfmt, [
lld]))()()
real_print_impl = (lambda ty, context, builder, val: lld = context.cast(builder, val, ty, types.float64)('%f', [
lld]))()
const_print_impl = (lambda ty, context, builder, sigval: pyval = ty.literal_value# WARNING: Decompyle incomplete
)()
print_varargs = (lambda context, builder, sig, args: vprint = nvvmutils.declare_vprint(builder.module)formats = []values = []for argtype, argval in enumerate(zip(sig.args, args)):
(argfmt, argvals) = print_item(argtype, context, builder, argval)formats.append(argfmt)values.extend(argvals)rawfmt = ' '.join(formats) + '\n'if len(args) > 32:
msg = 'CUDA print() cannot print more than 32 items. The raw format string will be emitted by the kernel instead.'warn(msg, NumbaWarning)rawfmt = rawfmt.replace('%', '%%')fmt = context.insert_string_const_addrspace(builder, rawfmt)array = cgutils.make_anonymous_struct(builder, values)arrayptr = cgutils.alloca_once_value(builder, array)vprint = nvvmutils.declare_vprint(builder.module)builder.call(vprint, (fmt, builder.bitcast(arrayptr, voidptr)))context.get_dummy_value())()
