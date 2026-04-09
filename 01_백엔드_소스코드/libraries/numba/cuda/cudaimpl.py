# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cudaimpl.pyc (Python 3.11)

from functools import reduce
import operator
import math
from llvmlite import ir
from llvmlite.binding import binding as ll
from numba.core.imputils import Registry, lower_cast
from numba.core.typing.npydecl import parse_dtype
from numba.core.datamodel import models
from numba.core import types, cgutils
from numba.np import ufunc_db
from numba.np.npyimpl import register_ufuncs
from cudadrv import nvvm
from numba import cuda
from numba.cuda import nvvmutils, stubs, errors
from numba.cuda.types import dim3, CUDADispatcher
registry = Registry()
lower = registry.lower
lower_attr = registry.lower_getattr
lower_constant = registry.lower_constant

def initialize_dim3(builder, prefix):
    x = nvvmutils.call_sreg(builder, '%s.x' % prefix)
    y = nvvmutils.call_sreg(builder, '%s.y' % prefix)
    z = nvvmutils.call_sreg(builder, '%s.z' % prefix)
    return cgutils.pack_struct(builder, (x, y, z))

cuda_threadIdx = (lambda context, builder, sig, args: initialize_dim3(builder, 'tid'))()
cuda_blockDim = (lambda context, builder, sig, args: initialize_dim3(builder, 'ntid'))()
cuda_blockIdx = (lambda context, builder, sig, args: initialize_dim3(builder, 'ctaid'))()
cuda_gridDim = (lambda context, builder, sig, args: initialize_dim3(builder, 'nctaid'))()
cuda_laneid = (lambda context, builder, sig, args: nvvmutils.call_sreg(builder, 'laneid'))()
dim3_x = (lambda context, builder, sig, args: builder.extract_value(args, 0))()
dim3_y = (lambda context, builder, sig, args: builder.extract_value(args, 1))()
dim3_z = (lambda context, builder, sig, args: builder.extract_value(args, 2))()
cuda_const_array_like = (lambda context, builder, sig, args: args[0])()
_unique_smem_id = 0

def _get_unique_smem_id(name):
    """Due to bug with NVVM invalid internalizing of shared memory in the
    PTX output.  We can't mark shared memory to be internal. We have to
    ensure unique name is generated for shared memory symbol.
    """
    global _unique_smem_id
    _unique_smem_id += 1
    return '{0}_{1}'.format(name, _unique_smem_id)

cuda_shared_array_integer = (lambda context, builder, sig, args: length = sig.args[0].literal_valuedtype = parse_dtype(sig.args[1])_generic_array(context, builder, shape = (length,), dtype = dtype, symbol_name = _get_unique_smem_id('_cudapy_smem'), addrspace = nvvm.ADDRSPACE_SHARED, can_dynsized = True))()
cuda_shared_array_tuple = (lambda context, builder, sig, args: shape = sig.args[0]()dtype = parse_dtype(sig.args[1])_generic_array(context, builder, shape = shape, dtype = dtype, symbol_name = _get_unique_smem_id('_cudapy_smem'), addrspace = nvvm.ADDRSPACE_SHARED, can_dynsized = True))()()
cuda_local_array_integer = (lambda context, builder, sig, args: length = sig.args[0].literal_valuedtype = parse_dtype(sig.args[1])_generic_array(context, builder, shape = (length,), dtype = dtype, symbol_name = '_cudapy_lmem', addrspace = nvvm.ADDRSPACE_LOCAL, can_dynsized = False))()
ptx_lmem_alloc_array = (lambda context, builder, sig, args: shape = sig.args[0]()dtype = parse_dtype(sig.args[1])_generic_array(context, builder, shape = shape, dtype = dtype, symbol_name = '_cudapy_lmem', addrspace = nvvm.ADDRSPACE_LOCAL, can_dynsized = False))()()
ptx_threadfence_block = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()
ptx_threadfence_system = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()
ptx_threadfence_device = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()
ptx_syncwarp = (lambda context, builder, sig, args: mask = context.get_constant(types.int32, 0xFFFFFFFF)mask_sig = types.none(types.int32)ptx_syncwarp_mask(context, builder, mask_sig, [
mask]))()
ptx_syncwarp_mask = (lambda context, builder, sig, args: fname = 'llvm.nvvm.bar.warp.sync'lmod = builder.modulefnty = ir.FunctionType(ir.VoidType(), (ir.IntType(32),))sync = cgutils.get_or_insert_function(lmod, fnty, fname)builder.call(sync, args)context.get_dummy_value())()
ptx_shfl_sync_i32 = (lambda context, builder, sig, args: (mask, mode, value, index, clamp) = argsvalue_type = sig.args[2]if value_type in types.real_domain:
value = builder.bitcast(value, ir.IntType(value_type.bitwidth))fname = 'llvm.nvvm.shfl.sync.i32'lmod = builder.modulefnty = ir.FunctionType(ir.LiteralStructType((ir.IntType(32), ir.IntType(1))), (ir.IntType(32), ir.IntType(32), ir.IntType(32), ir.IntType(32), ir.IntType(32)))func = cgutils.get_or_insert_function(lmod, fnty, fname)if value_type.bitwidth == 32:
ret = builder.call(func, (mask, mode, value, index, clamp))if value_type == types.float32:
rv = builder.extract_value(ret, 0)pred = builder.extract_value(ret, 1)fv = builder.bitcast(rv, ir.FloatType())ret = cgutils.make_anonymous_struct(builder, (fv, pred))else:
value1 = builder.trunc(value, ir.IntType(32))value_lshr = builder.lshr(value, context.get_constant(types.i8, 32))value2 = builder.trunc(value_lshr, ir.IntType(32))ret1 = builder.call(func, (mask, mode, value1, index, clamp))ret2 = builder.call(func, (mask, mode, value2, index, clamp))rv1 = builder.extract_value(ret1, 0)rv2 = builder.extract_value(ret2, 0)pred = builder.extract_value(ret1, 1)rv1_64 = builder.zext(rv1, ir.IntType(64))rv2_64 = builder.zext(rv2, ir.IntType(64))rv_shl = builder.shl(rv2_64, context.get_constant(types.i8, 32))rv = builder.or_(rv_shl, rv1_64)if value_type == types.float64:
rv = builder.bitcast(rv, ir.DoubleType())ret = cgutils.make_anonymous_struct(builder, (rv, pred))ret)()()()()
ptx_vote_sync = (lambda context, builder, sig, args: fname = 'llvm.nvvm.vote.sync'lmod = builder.modulefnty = ir.FunctionType(ir.LiteralStructType((ir.IntType(32), ir.IntType(1))), (ir.IntType(32), ir.IntType(32), ir.IntType(1)))func = cgutils.get_or_insert_function(lmod, fnty, fname)builder.call(func, args))()
ptx_match_any_sync = (lambda context, builder, sig, args: (mask, value) = argswidth = sig.args[1].bitwidthif sig.args[1] in types.real_domain:
value = builder.bitcast(value, ir.IntType(width))fname = 'llvm.nvvm.match.any.sync.i{}'.format(width)lmod = builder.modulefnty = ir.FunctionType(ir.IntType(32), (ir.IntType(32), ir.IntType(width)))func = cgutils.get_or_insert_function(lmod, fnty, fname)builder.call(func, (mask, value)))()()()()
ptx_match_all_sync = (lambda context, builder, sig, args: (mask, value) = argswidth = sig.args[1].bitwidthif sig.args[1] in types.real_domain:
value = builder.bitcast(value, ir.IntType(width))fname = 'llvm.nvvm.match.all.sync.i{}'.format(width)lmod = builder.modulefnty = ir.FunctionType(ir.LiteralStructType((ir.IntType(32), ir.IntType(1))), (ir.IntType(32), ir.IntType(width)))func = cgutils.get_or_insert_function(lmod, fnty, fname)builder.call(func, (mask, value)))()()()()
ptx_activemask = (lambda context, builder, sig, args: activemask = ir.InlineAsm(ir.FunctionType(ir.IntType(32), []), 'activemask.b32 $0;', '=r', side_effect = True)builder.call(activemask, []))()
ptx_lanemask_lt = (lambda context, builder, sig, args: activemask = ir.InlineAsm(ir.FunctionType(ir.IntType(32), []), 'mov.u32 $0, %lanemask_lt;', '=r', side_effect = True)builder.call(activemask, []))()
ptx_popc = (lambda context, builder, sig, args: builder.ctpop(args[0]))()
ptx_fma = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()

def float16_float_ty_constraint(bitwidth):
    typemap = {
        32: ('f32', 'f'),
        64: ('f64', 'd') }
    
    try:
        return typemap[bitwidth]
    except KeyError:
        msg = f'''Conversion between float16 and float{bitwidth} unsupported'''
        raise errors.CudaLoweringError(msg)


float16_to_float_cast = (lambda context, builder, fromty, toty, val: if fromty.bitwidth == toty.bitwidth:
val(ty, constraint) = None(toty.bitwidth)fnty = ir.FunctionType(context.get_value_type(toty), [
ir.IntType(16)])asm = ir.InlineAsm(fnty, f'''cvt.{ty}.f16 $0, $1;''', f'''={constraint},h''')builder.call(asm, [
val]))()
float_to_float16_cast = (lambda context, builder, fromty, toty, val: if fromty.bitwidth == toty.bitwidth:
val(ty, constraint) = None(fromty.bitwidth)fnty = ir.FunctionType(ir.IntType(16), [
context.get_value_type(fromty)])asm = ir.InlineAsm(fnty, f'''cvt.rn.f16.{ty} $0, $1;''', f'''=h,{constraint}''')builder.call(asm, [
val]))()

def float16_int_constraint(bitwidth):
    typemap = {
        8: 'c',
        16: 'h',
        32: 'r',
        64: 'l' }
    
    try:
        return typemap[bitwidth]
    except KeyError:
        msg = f'''Conversion between float16 and int{bitwidth} unsupported'''
        raise errors.CudaLoweringError(msg)


float16_to_integer_cast = (lambda context, builder, fromty, toty, val: bitwidth = toty.bitwidthconstraint = float16_int_constraint(bitwidth)signedness = 's' if toty.signed else 'u'fnty = ir.FunctionType(context.get_value_type(toty), [
ir.IntType(16)])asm = ir.InlineAsm(fnty, f'''cvt.rni.{signedness}{bitwidth}.f16 $0, $1;''', f'''={constraint},h''')builder.call(asm, [
val]))()
integer_to_float16_cast = (lambda context, builder, fromty, toty, val: bitwidth = fromty.bitwidthconstraint = float16_int_constraint(bitwidth)signedness = 's' if fromty.signed else 'u'fnty = ir.FunctionType(ir.IntType(16), [
context.get_value_type(fromty)])asm = ir.InlineAsm(fnty, f'''cvt.rn.f16.{signedness}{bitwidth} $0, $1;''', f'''=h,{constraint}''')builder.call(asm, [
val]))()()

def lower_fp16_binary(fn, op):
    pass
# WARNING: Decompyle incomplete

lower_fp16_binary(stubs.fp16.hadd, 'add')
lower_fp16_binary(operator.add, 'add')
lower_fp16_binary(operator.iadd, 'add')
lower_fp16_binary(stubs.fp16.hsub, 'sub')
lower_fp16_binary(operator.sub, 'sub')
lower_fp16_binary(operator.isub, 'sub')
lower_fp16_binary(stubs.fp16.hmul, 'mul')
lower_fp16_binary(operator.mul, 'mul')
lower_fp16_binary(operator.imul, 'mul')
ptx_fp16_hneg = (lambda context, builder, sig, args: fnty = ir.FunctionType(ir.IntType(16), [
ir.IntType(16)])asm = ir.InlineAsm(fnty, 'neg.f16 $0, $1;', '=h,h')builder.call(asm, args))()
operator_hneg = (lambda context, builder, sig, args: ptx_fp16_hneg(context, builder, sig, args))()
ptx_fp16_habs = (lambda context, builder, sig, args: fnty = ir.FunctionType(ir.IntType(16), [
ir.IntType(16)])asm = ir.InlineAsm(fnty, 'abs.f16 $0, $1;', '=h,h')builder.call(asm, args))()
operator_habs = (lambda context, builder, sig, args: ptx_fp16_habs(context, builder, sig, args))()
ptx_hfma = (lambda context, builder, sig, args: argtys = [
ir.IntType(16),
ir.IntType(16),
ir.IntType(16)]fnty = ir.FunctionType(ir.IntType(16), argtys)asm = ir.InlineAsm(fnty, 'fma.rn.f16 $0,$1,$2,$3;', '=h,h,h,h')builder.call(asm, args))()
fp16_div_impl = (lambda context, builder, sig, args: 
def fp16_div(x, y):
cuda.fp16.hdiv(x, y)context.compile_internal(builder, fp16_div, sig, args))()()
_fp16_cmp = '{{\n          .reg .pred __$$f16_cmp_tmp;\n          setp.{op}.f16 __$$f16_cmp_tmp, $1, $2;\n          selp.u16 $0, 1, 0, __$$f16_cmp_tmp;\n        }}'

def _gen_fp16_cmp(op):
    pass
# WARNING: Decompyle incomplete

lower(stubs.fp16.heq, types.float16, types.float16)(_gen_fp16_cmp('eq'))
lower(operator.eq, types.float16, types.float16)(_gen_fp16_cmp('eq'))
lower(stubs.fp16.hne, types.float16, types.float16)(_gen_fp16_cmp('ne'))
lower(operator.ne, types.float16, types.float16)(_gen_fp16_cmp('ne'))
lower(stubs.fp16.hge, types.float16, types.float16)(_gen_fp16_cmp('ge'))
lower(operator.ge, types.float16, types.float16)(_gen_fp16_cmp('ge'))
lower(stubs.fp16.hgt, types.float16, types.float16)(_gen_fp16_cmp('gt'))
lower(operator.gt, types.float16, types.float16)(_gen_fp16_cmp('gt'))
lower(stubs.fp16.hle, types.float16, types.float16)(_gen_fp16_cmp('le'))
lower(operator.le, types.float16, types.float16)(_gen_fp16_cmp('le'))
lower(stubs.fp16.hlt, types.float16, types.float16)(_gen_fp16_cmp('lt'))
lower(operator.lt, types.float16, types.float16)(_gen_fp16_cmp('lt'))

def lower_fp16_minmax(fn, fname, op):
    pass
# WARNING: Decompyle incomplete

lower_fp16_minmax(stubs.fp16.hmax, 'max', 'gt')
lower_fp16_minmax(stubs.fp16.hmin, 'min', 'lt')
cbrt_funcs = {
    types.float64: '__nv_cbrt',
    types.float32: '__nv_cbrtf' }
ptx_cbrt = (lambda context, builder, sig, args: ty = sig.return_typefname = cbrt_funcs[ty]fty = context.get_value_type(ty)lmod = builder.modulefnty = ir.FunctionType(fty, [
fty])fn = cgutils.get_or_insert_function(lmod, fnty, fname)builder.call(fn, args))()()
ptx_brev_u4 = (lambda context, builder, sig, args: fn = cgutils.get_or_insert_function(builder.module, ir.FunctionType(ir.IntType(32), (ir.IntType(32),)), '__nv_brev')builder.call(fn, args))()
ptx_brev_u8 = (lambda context, builder, sig, args: fn = cgutils.get_or_insert_function(builder.module, ir.FunctionType(ir.IntType(64), (ir.IntType(64),)), '__nv_brevll')builder.call(fn, args))()
ptx_clz = (lambda context, builder, sig, args: builder.ctlz(args[0], context.get_constant(types.boolean, 0)))()
ptx_ffs_32 = (lambda context, builder, sig, args: fn = cgutils.get_or_insert_function(builder.module, ir.FunctionType(ir.IntType(32), (ir.IntType(32),)), '__nv_ffs')builder.call(fn, args))()()
ptx_ffs_64 = (lambda context, builder, sig, args: fn = cgutils.get_or_insert_function(builder.module, ir.FunctionType(ir.IntType(32), (ir.IntType(64),)), '__nv_ffsll')builder.call(fn, args))()()
ptx_selp = (lambda context, builder, sig, args: (test, a, b) = argsbuilder.select(test, a, b))()
ptx_max_f4 = (lambda context, builder, sig, args: fn = cgutils.get_or_insert_function(builder.module, ir.FunctionType(ir.FloatType(), (ir.FloatType(), ir.FloatType())), '__nv_fmaxf')builder.call(fn, args))()
ptx_max_f8 = (lambda context, builder, sig, args: fn = cgutils.get_or_insert_function(builder.module, ir.FunctionType(ir.DoubleType(), (ir.DoubleType(), ir.DoubleType())), '__nv_fmax')builder.call(fn, [
context.cast(builder, args[0], sig.args[0], types.double),
context.cast(builder, args[1], sig.args[1], types.double)]))()()()
ptx_min_f4 = (lambda context, builder, sig, args: fn = cgutils.get_or_insert_function(builder.module, ir.FunctionType(ir.FloatType(), (ir.FloatType(), ir.FloatType())), '__nv_fminf')builder.call(fn, args))()
ptx_min_f8 = (lambda context, builder, sig, args: fn = cgutils.get_or_insert_function(builder.module, ir.FunctionType(ir.DoubleType(), (ir.DoubleType(), ir.DoubleType())), '__nv_fmin')builder.call(fn, [
context.cast(builder, args[0], sig.args[0], types.double),
context.cast(builder, args[1], sig.args[1], types.double)]))()()()
ptx_round = (lambda context, builder, sig, args: fn = cgutils.get_or_insert_function(builder.module, ir.FunctionType(ir.IntType(64), (ir.DoubleType(),)), '__nv_llrint')builder.call(fn, [
context.cast(builder, args[0], sig.args[0], types.double)]))()()
round_to_impl = (lambda context, builder, sig, args: 
def round_ndigits(x, ndigits):
if math.isinf(x) or math.isnan(x):
xif None >= 0:
if ndigits > 22:
pow1 = 10 ** (ndigits - 22)pow2 = 1e+22else:
pow1 = 10 ** ndigitspow2 = 1y = x * pow1 * pow2if math.isinf(y):
xpow1 = 10 ** (-ndigits)y = x / pow1z = round(y)if math.fabs(y - z) == 0.5:
z = 2 * round(y / 2)if ndigits >= 0:
z = z / pow2 / pow1else:
z *= pow1zcontext.compile_internal(builder, round_ndigits, sig, args))()()

def gen_deg_rad(const):
    pass
# WARNING: Decompyle incomplete

_deg2rad = math.pi / 180
_rad2deg = 180 / math.pi
lower(math.radians, types.f4)(gen_deg_rad(_deg2rad))
lower(math.radians, types.f8)(gen_deg_rad(_deg2rad))
lower(math.degrees, types.f4)(gen_deg_rad(_rad2deg))
lower(math.degrees, types.f8)(gen_deg_rad(_rad2deg))

def _normalize_indices(context, builder, indty, inds, aryty, valty):
    '''
    Convert integer indices into tuple of intp
    '''
    pass
# WARNING: Decompyle incomplete


def _atomic_dispatcher(dispatch_fn):
    pass
# WARNING: Decompyle incomplete

ptx_atomic_add_tuple = (lambda context, builder, dtype, ptr, val: if dtype == types.float32:
lmod = builder.modulebuilder.call(nvvmutils.declare_atomic_add_float32(lmod), (ptr, val))if None == types.float64:
lmod = builder.modulebuilder.call(nvvmutils.declare_atomic_add_float64(lmod), (ptr, val))None.atomic_rmw('add', ptr, val, 'monotonic'))()()()()
ptx_atomic_sub = (lambda context, builder, dtype, ptr, val: if dtype == types.float32:
lmod = builder.modulebuilder.call(nvvmutils.declare_atomic_sub_float32(lmod), (ptr, val))if None == types.float64:
lmod = builder.modulebuilder.call(nvvmutils.declare_atomic_sub_float64(lmod), (ptr, val))None.atomic_rmw('sub', ptr, val, 'monotonic'))()()()()
ptx_atomic_inc = (lambda context, builder, dtype, ptr, val: if dtype in cuda.cudadecl.unsigned_int_numba_types:
bw = dtype.bitwidthlmod = builder.modulefn = getattr(nvvmutils, f'''declare_atomic_inc_int{bw}''')builder.call(fn(lmod), (ptr, val))raise None(f'''Unimplemented atomic inc with {dtype} array'''))()()()()
ptx_atomic_dec = (lambda context, builder, dtype, ptr, val: if dtype in cuda.cudadecl.unsigned_int_numba_types:
bw = dtype.bitwidthlmod = builder.modulefn = getattr(nvvmutils, f'''declare_atomic_dec_int{bw}''')builder.call(fn(lmod), (ptr, val))raise None(f'''Unimplemented atomic dec with {dtype} array'''))()()()()

def ptx_atomic_bitwise(stub, op):
    pass
# WARNING: Decompyle incomplete

ptx_atomic_bitwise(stubs.atomic.and_, 'and')
ptx_atomic_bitwise(stubs.atomic.or_, 'or')
ptx_atomic_bitwise(stubs.atomic.xor, 'xor')
ptx_atomic_exch = (lambda context, builder, dtype, ptr, val: if dtype in cuda.cudadecl.integer_numba_types:
builder.atomic_rmw('xchg', ptr, val, 'monotonic')raise None(f'''Unimplemented atomic exch with {dtype} array'''))()()()()
ptx_atomic_max = (lambda context, builder, dtype, ptr, val: lmod = builder.moduleif dtype == types.float64:
builder.call(nvvmutils.declare_atomic_max_float64(lmod), (ptr, val))if None == types.float32:
builder.call(nvvmutils.declare_atomic_max_float32(lmod), (ptr, val))if None in (types.int32, types.int64):
builder.atomic_rmw('max', ptr, val, ordering = 'monotonic')if None in (types.uint32, types.uint64):
builder.atomic_rmw('umax', ptr, val, ordering = 'monotonic')raise None('Unimplemented atomic max with %s array' % dtype))()()()()
ptx_atomic_min = (lambda context, builder, dtype, ptr, val: lmod = builder.moduleif dtype == types.float64:
builder.call(nvvmutils.declare_atomic_min_float64(lmod), (ptr, val))if None == types.float32:
builder.call(nvvmutils.declare_atomic_min_float32(lmod), (ptr, val))if None in (types.int32, types.int64):
builder.atomic_rmw('min', ptr, val, ordering = 'monotonic')if None in (types.uint32, types.uint64):
builder.atomic_rmw('umin', ptr, val, ordering = 'monotonic')raise None('Unimplemented atomic min with %s array' % dtype))()()()()
ptx_atomic_nanmax = (lambda context, builder, dtype, ptr, val: lmod = builder.moduleif dtype == types.float64:
builder.call(nvvmutils.declare_atomic_nanmax_float64(lmod), (ptr, val))if None == types.float32:
builder.call(nvvmutils.declare_atomic_nanmax_float32(lmod), (ptr, val))if None in (types.int32, types.int64):
builder.atomic_rmw('max', ptr, val, ordering = 'monotonic')if None in (types.uint32, types.uint64):
builder.atomic_rmw('umax', ptr, val, ordering = 'monotonic')raise None('Unimplemented atomic max with %s array' % dtype))()()()()
ptx_atomic_nanmin = (lambda context, builder, dtype, ptr, val: lmod = builder.moduleif dtype == types.float64:
builder.call(nvvmutils.declare_atomic_nanmin_float64(lmod), (ptr, val))if None == types.float32:
builder.call(nvvmutils.declare_atomic_nanmin_float32(lmod), (ptr, val))if None in (types.int32, types.int64):
builder.atomic_rmw('min', ptr, val, ordering = 'monotonic')if None in (types.uint32, types.uint64):
builder.atomic_rmw('umin', ptr, val, ordering = 'monotonic')raise None('Unimplemented atomic min with %s array' % dtype))()()()()
ptx_atomic_compare_and_swap = (lambda context, builder, sig, args: sig = sig.return_type(sig.args[0], types.intp, sig.args[1], sig.args[2])args = (args[0], context.get_constant(types.intp, 0), args[1], args[2])ptx_atomic_cas(context, builder, sig, args))()
ptx_atomic_cas = (lambda context, builder, sig, args: (aryty, indty, oldty, valty) = sig.args(ary, inds, old, val) = args(indty, indices) = _normalize_indices(context, builder, indty, inds, aryty, valty)lary = context.make_array(aryty)(context, builder, ary)ptr = cgutils.get_item_pointer(context, builder, aryty, lary, indices, wraparound = True)if aryty.dtype in cuda.cudadecl.integer_numba_types:
lmod = builder.modulebitwidth = aryty.dtype.bitwidthnvvmutils.atomic_cmpxchg(builder, lmod, bitwidth, ptr, old, val)raise None('Unimplemented atomic cas with %s array' % aryty.dtype))()()()
ptx_nanosleep = (lambda context, builder, sig, args: nanosleep = ir.InlineAsm(ir.FunctionType(ir.VoidType(), [
ir.IntType(32)]), 'nanosleep.u32 $0;', 'r', side_effect = True)ns = args[0]builder.call(nanosleep, [
ns]))()

def _generic_array(context, builder, shape, dtype, symbol_name, addrspace, can_dynsized = (False,)):
    pass
# WARNING: Decompyle incomplete

cuda_dispatcher_const = (lambda context, builder, ty, pyval: context.get_dummy_value())()
register_ufuncs(ufunc_db.get_ufuncs(), lower)
