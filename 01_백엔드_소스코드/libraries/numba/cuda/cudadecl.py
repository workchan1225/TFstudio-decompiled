# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cudadecl.pyc (Python 3.11)

import operator
from numba.core import types
from numba.core.typing.npydecl import parse_dtype, parse_shape, register_number_classes, register_numpy_ufunc, trigonometric_functions, comparison_functions, math_operations, bit_twiddling_functions
from numba.core.typing.templates import AttributeTemplate, ConcreteTemplate, AbstractTemplate, CallableTemplate, signature, Registry
from numba.cuda.types import dim3
from numba.core.typeconv import Conversion
from numba import cuda
from numba.cuda.compiler import declare_device_function_template
registry = Registry()
register = registry.register
register_attr = registry.register_attr
register_global = registry.register_global
register_number_classes(register_global)

class Cuda_array_decl(CallableTemplate):
    
    def generic(self):
        
        def typer(shape, dtype):
            if isinstance(shape, types.Integer):
                if not isinstance(shape, types.IntegerLiteral):
                    return None
            if isinstance(shape, (types.Tuple, types.UniTuple)):
                if (lambda .0: [ not isinstance(s, types.IntegerLiteral) for s in .0 ])(shape()):
                    return None
            return None
            ndim = parse_shape(shape)
            nb_dtype = parse_dtype(dtype)
        # WARNING: Decompyle incomplete

        return typer


Cuda_shared_array = <NODE:12>()
Cuda_local_array = <NODE:12>()
Cuda_const_array_like = <NODE:12>()
Cuda_threadfence_device = <NODE:12>()
Cuda_threadfence_block = <NODE:12>()
Cuda_threadfence_system = <NODE:12>()
Cuda_syncwarp = <NODE:12>()
Cuda_shfl_sync_intrinsic = <NODE:12>()
Cuda_vote_sync_intrinsic = <NODE:12>()
Cuda_match_any_sync = <NODE:12>()
Cuda_match_all_sync = <NODE:12>()
Cuda_activemask = <NODE:12>()
Cuda_lanemask_lt = <NODE:12>()
Cuda_popc = <NODE:12>()
Cuda_fma = <NODE:12>()
Cuda_hfma = <NODE:12>()
Cuda_cbrt = <NODE:12>()
Cuda_brev = <NODE:12>()
Cuda_clz = <NODE:12>()
Cuda_ffs = <NODE:12>()
Cuda_selp = <NODE:12>()

def _genfp16_unary(l_key):
    pass
# WARNING: Decompyle incomplete


def _genfp16_unary_operator(l_key):
    pass
# WARNING: Decompyle incomplete


def _genfp16_binary(l_key):
    pass
# WARNING: Decompyle incomplete

Float = <NODE:12>()

def _genfp16_binary_comparison(l_key):
    pass
# WARNING: Decompyle incomplete


def _fp16_binary_operator(l_key, retty):
    pass
# WARNING: Decompyle incomplete


def _genfp16_comparison_operator(op):
    return _fp16_binary_operator(op, types.b1)


def _genfp16_binary_operator(op):
    return _fp16_binary_operator(op, types.float16)

Cuda_hadd = _genfp16_binary(cuda.fp16.hadd)
Cuda_add = _genfp16_binary_operator(operator.add)
Cuda_iadd = _genfp16_binary_operator(operator.iadd)
Cuda_hsub = _genfp16_binary(cuda.fp16.hsub)
Cuda_sub = _genfp16_binary_operator(operator.sub)
Cuda_isub = _genfp16_binary_operator(operator.isub)
Cuda_hmul = _genfp16_binary(cuda.fp16.hmul)
Cuda_mul = _genfp16_binary_operator(operator.mul)
Cuda_imul = _genfp16_binary_operator(operator.imul)
Cuda_hmax = _genfp16_binary(cuda.fp16.hmax)
Cuda_hmin = _genfp16_binary(cuda.fp16.hmin)
Cuda_hneg = _genfp16_unary(cuda.fp16.hneg)
Cuda_neg = _genfp16_unary_operator(operator.neg)
Cuda_habs = _genfp16_unary(cuda.fp16.habs)
Cuda_abs = _genfp16_unary_operator(abs)
Cuda_heq = _genfp16_binary_comparison(cuda.fp16.heq)
_genfp16_comparison_operator(operator.eq)
Cuda_hne = _genfp16_binary_comparison(cuda.fp16.hne)
_genfp16_comparison_operator(operator.ne)
Cuda_hge = _genfp16_binary_comparison(cuda.fp16.hge)
_genfp16_comparison_operator(operator.ge)
Cuda_hgt = _genfp16_binary_comparison(cuda.fp16.hgt)
_genfp16_comparison_operator(operator.gt)
Cuda_hle = _genfp16_binary_comparison(cuda.fp16.hle)
_genfp16_comparison_operator(operator.le)
Cuda_hlt = _genfp16_binary_comparison(cuda.fp16.hlt)
_genfp16_comparison_operator(operator.lt)
_genfp16_binary_operator(operator.truediv)
_genfp16_binary_operator(operator.itruediv)

def _resolve_wrapped_unary(fname):
    decl = declare_device_function_template(f'''__numba_wrapper_{fname}''', types.float16, (types.float16,))
    return types.Function(decl)


def _resolve_wrapped_binary(fname):
    decl = declare_device_function_template(f'''__numba_wrapper_{fname}''', types.float16, (types.float16, types.float16))
    return types.Function(decl)

hsin_device = _resolve_wrapped_unary('hsin')
hcos_device = _resolve_wrapped_unary('hcos')
hlog_device = _resolve_wrapped_unary('hlog')
hlog10_device = _resolve_wrapped_unary('hlog10')
hlog2_device = _resolve_wrapped_unary('hlog2')
hexp_device = _resolve_wrapped_unary('hexp')
hexp10_device = _resolve_wrapped_unary('hexp10')
hexp2_device = _resolve_wrapped_unary('hexp2')
hsqrt_device = _resolve_wrapped_unary('hsqrt')
hrsqrt_device = _resolve_wrapped_unary('hrsqrt')
hfloor_device = _resolve_wrapped_unary('hfloor')
hceil_device = _resolve_wrapped_unary('hceil')
hrcp_device = _resolve_wrapped_unary('hrcp')
hrint_device = _resolve_wrapped_unary('hrint')
htrunc_device = _resolve_wrapped_unary('htrunc')
hdiv_device = _resolve_wrapped_binary('hdiv')

def _gen(l_key, supported_types):
    pass
# WARNING: Decompyle incomplete

all_numba_types = (types.float64, types.float32, types.int32, types.uint32, types.int64, types.uint64)
integer_numba_types = (types.int32, types.uint32, types.int64, types.uint64)
unsigned_int_numba_types = (types.uint32, types.uint64)
Cuda_atomic_add = _gen(cuda.atomic.add, all_numba_types)
Cuda_atomic_sub = _gen(cuda.atomic.sub, all_numba_types)
Cuda_atomic_max = _gen(cuda.atomic.max, all_numba_types)
Cuda_atomic_min = _gen(cuda.atomic.min, all_numba_types)
Cuda_atomic_nanmax = _gen(cuda.atomic.nanmax, all_numba_types)
Cuda_atomic_nanmin = _gen(cuda.atomic.nanmin, all_numba_types)
Cuda_atomic_and = _gen(cuda.atomic.and_, integer_numba_types)
Cuda_atomic_or = _gen(cuda.atomic.or_, integer_numba_types)
Cuda_atomic_xor = _gen(cuda.atomic.xor, integer_numba_types)
Cuda_atomic_inc = _gen(cuda.atomic.inc, unsigned_int_numba_types)
Cuda_atomic_dec = _gen(cuda.atomic.dec, unsigned_int_numba_types)
Cuda_atomic_exch = _gen(cuda.atomic.exch, integer_numba_types)
Cuda_atomic_compare_and_swap = <NODE:12>()
Cuda_atomic_cas = <NODE:12>()
Cuda_nanosleep = <NODE:12>()
Dim3_attrs = <NODE:12>()
CudaSharedModuleTemplate = <NODE:12>()
CudaConstModuleTemplate = <NODE:12>()
CudaLocalModuleTemplate = <NODE:12>()
CudaAtomicTemplate = <NODE:12>()
CudaFp16Template = <NODE:12>()
CudaModuleTemplate = <NODE:12>()
register_global(cuda, types.Module(cuda))
for func in trigonometric_functions:
    register_numpy_ufunc(func, register_global)
    for func in comparison_functions:
        register_numpy_ufunc(func, register_global)
        for func in bit_twiddling_functions:
            register_numpy_ufunc(func, register_global)
            for func in math_operations:
                if func in ('log', 'log2', 'log10'):
                    register_numpy_ufunc(func, register_global)
                return None
