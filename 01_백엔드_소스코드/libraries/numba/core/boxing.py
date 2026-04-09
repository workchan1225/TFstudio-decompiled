# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: boxing.pyc (Python 3.11)

'''
Boxing and unboxing of native Numba values to / from CPython objects.
'''
from llvmlite import ir
from numba.core import types, cgutils
from numba.core.pythonapi import box, unbox, reflect, NativeValue
from numba.core.errors import NumbaNotImplementedError, TypingError
from numba.core.typing.typeof import typeof, Purpose
from numba.cpython import setobj, listobj
from numba.np import numpy_support
from contextlib import contextmanager, ExitStack
box_bool = (lambda typ, val, c: c.pyapi.bool_from_bool(val))()
unbox_boolean = (lambda typ, obj, c: istrue = c.pyapi.object_istrue(obj)zero = ir.Constant(istrue.type, 0)val = c.builder.icmp_signed('!=', istrue, zero)NativeValue(val, is_error = c.pyapi.c_api_error()))()
box_literal_integer = (lambda typ, val, c: val = c.context.cast(c.builder, val, typ, typ.literal_type)c.box(typ.literal_type, val))()()
box_integer = (lambda typ, val, c: if typ.signed:
ival = c.builder.sext(val, c.pyapi.longlong)c.pyapi.long_from_longlong(ival)ullval = None.builder.zext(val, c.pyapi.ulonglong)c.pyapi.long_from_ulonglong(ullval))()
unbox_integer = (lambda typ, obj, c: ll_type = c.context.get_argument_type(typ)val = cgutils.alloca_once(c.builder, ll_type)longobj = c.pyapi.number_long(obj)c.pyapi.if_object_ok(longobj)if typ.signed:
llval = c.pyapi.long_as_longlong(longobj)else:
llval = c.pyapi.long_as_ulonglong(longobj)c.pyapi.decref(longobj)c.builder.store(c.builder.trunc(llval, ll_type), val)None(None, None))()
box_float = (lambda typ, val, c: if typ == types.float32:
dbval = c.builder.fpext(val, c.pyapi.double)# WARNING: Decompyle incomplete
)()
unbox_float = (lambda typ, obj, c: fobj = c.pyapi.number_float(obj)dbval = c.pyapi.float_as_double(fobj)c.pyapi.decref(fobj)if typ == types.float32:
val = c.builder.fptrunc(dbval, c.context.get_argument_type(typ))# WARNING: Decompyle incomplete
)()
box_complex = (lambda typ, val, c: cval = c.context.make_complex(c.builder, typ, value = val)if typ == types.complex64:
freal = c.builder.fpext(cval.real, c.pyapi.double)fimag = c.builder.fpext(cval.imag, c.pyapi.double)# WARNING: Decompyle incomplete
)()
unbox_complex = (lambda typ, obj, c: c128 = c.context.make_complex(c.builder, types.complex128)ok = c.pyapi.complex_adaptor(obj, c128._getpointer())failed = cgutils.is_false(c.builder, ok)cgutils.if_unlikely(c.builder, failed)c.pyapi.err_set_string('PyExc_TypeError', f'''conversion to {typ!s} failed''')None(None, None)# WARNING: Decompyle incomplete
)()
box_none = (lambda typ, val, c: c.pyapi.make_none())()
unbox_none = (lambda typ, val, c: NativeValue(c.context.get_dummy_value()))()()
box_npdatetime = (lambda typ, val, c: c.pyapi.create_np_datetime(val, typ.unit_code))()
unbox_npdatetime = (lambda typ, obj, c: val = c.pyapi.extract_np_datetime(obj)NativeValue(val, is_error = c.pyapi.c_api_error()))()
box_nptimedelta = (lambda typ, val, c: c.pyapi.create_np_timedelta(val, typ.unit_code))()
unbox_nptimedelta = (lambda typ, obj, c: val = c.pyapi.extract_np_timedelta(obj)NativeValue(val, is_error = c.pyapi.c_api_error()))()
box_raw_pointer = (lambda typ, val, c: ll_intp = c.context.get_value_type(types.uintp)addr = c.builder.ptrtoint(val, ll_intp)c.box(types.uintp, addr))()
box_enum = (lambda typ, val, c: valobj = c.box(typ.dtype, val)cls_obj = c.pyapi.unserialize(c.pyapi.serialize_object(typ.instance_class))c.pyapi.call_function_objargs(cls_obj, (valobj,)))()
unbox_enum = (lambda typ, obj, c: valobj = c.pyapi.object_getattr_string(obj, 'value')c.unbox(typ.dtype, valobj))()
box_undefvar = (lambda typ, val, c: msg = 'UndefVar type cannot be boxed, there is no Python equivalent of this type.'raise TypingError(msg))()
box_record = (lambda typ, val, c: size = ir.Constant(ir.IntType(32), val.type.pointee.count)ptr = c.builder.bitcast(val, ir.PointerType(ir.IntType(8)))c.pyapi.recreate_record(ptr, size, typ.dtype, c.env_manager))()
unbox_record = (lambda typ, obj, c: pass# WARNING: Decompyle incomplete
)()
box_unicodecharseq = (lambda typ, val, c:
