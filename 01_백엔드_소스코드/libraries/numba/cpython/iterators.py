# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: iterators.pyc (Python 3.11)

'''
Implementation of various iterable and iterator types.
'''
from numba.core import types, cgutils
from numba.core.imputils import lower_builtin, iternext_impl, call_iternext, call_getiter, impl_ret_borrowed, impl_ret_new_ref, RefType
iterator_getiter = (lambda context, builder, sig, args: (it,) = argsimpl_ret_borrowed(context, builder, sig.return_type, it))()
make_enumerate_object = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()()
iternext_enumerate = (lambda context, builder, sig, args, result: (enumty,) = sig.args(enum,) = argsenum = context.make_helper(builder, enumty, value = enum)count = builder.load(enum.count)ncount = builder.add(count, context.get_constant(types.intp, 1))builder.store(ncount, enum.count)srcres = call_iternext(context, builder, enumty.source_type, enum.iter)is_valid = srcres.is_valid()result.set_valid(is_valid)builder.if_then(is_valid)srcval = srcres.yielded_value()result.yield_(context.make_tuple(builder, enumty.yield_type, [
count,
srcval]))None(None, None)Nonewith None:
if not None:
pass)()()
make_zip_object = (lambda context, builder, sig, args: zip_type = sig.return_type# WARNING: Decompyle incomplete
)()
iternext_zip = (lambda context, builder, sig, args, result: (zip_type,) = sig.args(zipobj,) = argszipobj = context.make_helper(builder, zip_type, value = zipobj)if len(zipobj) == 0:
result.set_exhausted()Nonep_ret_tup = None.alloca_once(builder, context.get_value_type(zip_type.yield_type))p_is_valid = cgutils.alloca_once_value(builder, value = cgutils.true_bit)for iterobj, srcty in enumerate(zip(zipobj, zip_type.source_types)):
is_valid = builder.load(p_is_valid)builder.if_then(is_valid)srcres = call_iternext(context, builder, srcty, iterobj)is_valid = builder.and_(is_valid, srcres.is_valid())builder.store(is_valid, p_is_valid)val = srcres.yielded_value()ptr = cgutils.gep_inbounds(builder, p_ret_tup, 0, i)builder.store(val, ptr)None(None, None)with None:
if not None:
passcontinueis_valid = builder.load(p_is_valid)result.set_valid(is_valid)builder.if_then(is_valid)result.yield_(builder.load(p_ret_tup))None(None, None)Nonewith None:
if not None:
pass)()()
iternext_zip = (lambda context, builder, sig, args, result:
