# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: linalg.pyc (Python 3.11)

'''
Implementation of linear algebra operations.
'''
import contextlib
import warnings
from llvmlite import ir
import numpy as np
import operator
from numba.core.imputils import lower_builtin, impl_ret_borrowed, impl_ret_new_ref, impl_ret_untracked
from numba.core.typing import signature
from numba.core.extending import intrinsic, overload, register_jitable
from numba.core import types, cgutils, config
from numba.core.errors import TypingError, NumbaTypeError, NumbaPerformanceWarning
from arrayobj import make_array, _empty_nd_impl, array_copy
from numba.np import numpy_support as np_support
ll_char = ir.IntType(8)
ll_char_p = ll_char.as_pointer()
ll_void_p = ll_char_p
ll_intc = ir.IntType(32)
ll_intc_p = ll_intc.as_pointer()
intp_t = cgutils.intp_t
ll_intp_p = intp_t.as_pointer()
F_INT_nptype = np.int32
if config.USE_LEGACY_TYPE_SYSTEM:
    F_INT_nbtype = types.int32
    _blas_kinds = {
        types.complex128: 'z',
        types.complex64: 'c',
        types.float64: 'd',
        types.float32: 's' }
else:
    F_INT_nbtype = types.np_int32
    _blas_kinds = {
        types.np_complex128: 'z',
        types.np_complex64: 'c',
        types.np_float64: 'd',
        types.np_float32: 's' }

def get_blas_kind(dtype, func_name = ('<BLAS function>',)):
    kind = _blas_kinds.get(dtype)
# WARNING: Decompyle incomplete


def ensure_blas():
    
    try:
        import scipy.linalg.cython_blas as scipy
        return None
    except ImportError:
        raise ImportError('scipy 0.16+ is required for linear algebra')



def ensure_lapack():
    
    try:
        import scipy.linalg.cython_lapack as scipy
        return None
    except ImportError:
        raise ImportError('scipy 0.16+ is required for linear algebra')



def make_constant_slot(context, builder, ty, val):
    const = context.get_constant_generic(builder, ty, val)
    return cgutils.alloca_once_value(builder, const)


class _BLAS:
    '''
    Functions to return type signatures for wrapped
    BLAS functions.
    '''
    
    def __init__(self):
        ensure_blas()

    numba_xxnrm2 = (lambda cls, dtype: rtype = getattr(dtype, 'underlying_float', dtype)sig = types.intc(types.char, types.intp, types.CPointer(dtype), types.intp, types.CPointer(rtype))types.ExternalFunction('numba_xxnrm2', sig))()
    numba_xxgemm = (lambda cls, dtype: sig = types.intc(types.char, types.char, types.char, types.intp, types.intp, types.intp, types.CPointer(dtype), types.CPointer(dtype), types.intp, types.CPointer(dtype), types.intp, types.CPointer(dtype), types.CPointer(dtype), types.intp)types.ExternalFunction('numba_xxgemm', sig))()


class _LAPACK:
    '''
    Functions to return type signatures for wrapped
    LAPACK functions.
    '''
    
    def __init__(self):
        ensure_lapack()

    numba_xxgetrf = (lambda cls, dtype: sig = types.intc(types.char, types.intp, types.intp, types.CPointer(dtype), types.intp, types.CPointer(F_INT_nbtype))types.ExternalFunction('numba_xxgetrf', sig))()
    numba_ez_xxgetri = (lambda cls, dtype: sig = types.intc(types.char, types.intp, types.CPointer(dtype), types.intp, types.CPointer(F_INT_nbtype))types.ExternalFunction('numba_ez_xxgetri', sig))()
    numba_ez_rgeev = (lambda cls, dtype: sig = types.intc(types.char, types.char, types.char, types.intp, types.CPointer(dtype), types.intp, types.CPointer(dtype), types.CPointer(dtype), types.CPointer(dtype), types.intp, types.CPointer(dtype), types.intp)types.ExternalFunction('numba_ez_rgeev', sig))()
    numba_ez_cgeev = (lambda cls, dtype: sig = types.intc(types.char, types.char, types.char, types.intp, types.CPointer(dtype), types.intp, types.CPointer(dtype), types.CPointer(dtype), types.intp, types.CPointer(dtype), types.intp)types.ExternalFunction('numba_ez_cgeev', sig))()
    numba_ez_xxxevd = (lambda cls, dtype: wtype = getattr(dtype, 'underlying_float', dtype)sig = types.intc(types.char, types.char, types.char, types.intp, types.CPointer(dtype), types.intp, types.CPointer(wtype))types.ExternalFunction('numba_ez_xxxevd', sig))()
    numba_xxpotrf = (lambda cls, dtype: sig = types.intc(types.char, types.char, types.intp, types.CPointer(dtype), types.intp)types.ExternalFunction('numba_xxpotrf', sig))()
    numba_ez_gesdd = (lambda cls, dtype: stype = getattr(dtype, 'underlying_float', dtype)sig = types.intc(types.char, types.char, types.intp, types.intp, types.CPointer(dtype), types.intp, types.CPointer(stype), types.CPointer(dtype), types.intp, types.CPointer(dtype), types.intp)types.ExternalFunction('numba_ez_gesdd', sig))()
    numba_ez_geqrf = (lambda cls, dtype: sig = types.intc(types.char, types.intp, types.intp, types.CPointer(dtype), types.intp, types.CPointer(dtype))types.ExternalFunction('numba_ez_geqrf', sig))()
    numba_ez_xxgqr = (lambda cls, dtype: sig = types.intc(types.char, types.intp, types.intp, types.intp, types.CPointer(dtype), types.intp, types.CPointer(dtype))types.ExternalFunction('numba_ez_xxgqr', sig))()
    numba_ez_gelsd = (lambda cls, dtype: rtype = getattr(dtype, 'underlying_float', dtype)sig = types.intc(types.char, types.intp, types.intp, types.intp, types.CPointer(dtype), types.intp, types.CPointer(dtype), types.intp, types.CPointer(rtype), types.float64, types.CPointer(types.intc))types.ExternalFunction('numba_ez_gelsd', sig))()
    numba_xgesv = (lambda cls, dtype: sig = types.intc(types.char, types.intp, types.intp, types.CPointer(dtype), types.intp, types.CPointer(F_INT_nbtype), types.CPointer(dtype), types.intp)types.ExternalFunction('numba_xgesv', sig))()

make_contiguous = (lambda context, builder, sig, args: pass# WARNING: Decompyle incomplete
)()

def check_c_int(context, builder, n):
    '''
    Check whether *n* fits in a C `int`.
    '''
    pass
# WARNING: Decompyle incomplete


def check_blas_return(context, builder, res):
    '''
    Check the integer error return from one of the BLAS wrappers in
    _helperlib.c.
    '''
    builder.if_then(cgutils.is_not_null(builder, res), likely = False)
    pyapi = context.get_python_api(builder)
    pyapi.gil_ensure()
    pyapi.fatal_error('BLAS wrapper returned with an error')
    None(None, None)
    return None
    with None:
        if not None:
            pass


def check_lapack_return(context, builder, res):
    '''
    Check the integer error return from one of the LAPACK wrappers in
    _helperlib.c.
    '''
    builder.if_then(cgutils.is_not_null(builder, res), likely = False)
    pyapi = context.get_python_api(builder)
    pyapi.gil_ensure()
    pyapi.fatal_error('LAPACK wrapper returned with an error')
    None(None, None)
    return None
    with None:
        if not None:
            pass


def call_xxdot(context, builder, conjugate, dtype, n, a_data, b_data, out_data):
    '''
    Call the BLAS vector * vector product function for the given arguments.
    '''
    fnty = ir.FunctionType(ir.IntType(32), [
        ll_char,
        ll_char,
        intp_t,
        ll_void_p,
        ll_void_p,
        ll_void_p])
    fn = cgutils.get_or_insert_function(builder.module, fnty, 'numba_xxdot')
    kind = get_blas_kind(dtype)
    kind_val = ir.Constant(ll_char, ord(kind))
    conjugate = ir.Constant(ll_char, int(conjugate))
    res = builder.call(fn, (kind_val, conjugate, n, builder.bitcast(a_data, ll_void_p), builder.bitcast(b_data, ll_void_p), builder.bitcast(out_data, ll_void_p)))
    check_blas_return(context, builder, res)


def call_xxgemv(context, builder, do_trans, m_type, m_shapes, m_data, v_data, out_data):
    '''
    Call the BLAS matrix * vector product function for the given arguments.
    '''
    fnty = ir.FunctionType(ir.IntType(32), [
        ll_char,
        ll_char,
        intp_t,
        intp_t,
        ll_void_p,
        ll_void_p,
        intp_t,
        ll_void_p,
        ll_void_p,
        ll_void_p])
    fn = cgutils.get_or_insert_function(builder.module, fnty, 'numba_xxgemv')
    dtype = m_type.dtype
    alpha = make_constant_slot(context, builder, dtype, 1)
    beta = make_constant_slot(context, builder, dtype, 0)
    if m_type.layout == 'F':
        (m, n) = m_shapes
        lda = m_shapes[0]
    else:
        (n, m) = m_shapes
        lda = m_shapes[1]
    kind = get_blas_kind(dtype)
    kind_val = ir.Constant(ll_char, ord(kind))
    trans = ir.Constant(ll_char, ord('t') if do_trans else ord('n'))
    res = builder.call(fn, (kind_val, trans, m, n, builder.bitcast(alpha, ll_void_p), builder.bitcast(m_data, ll_void_p), lda, builder.bitcast(v_data, ll_void_p), builder.bitcast(beta, ll_void_p), builder.bitcast(out_data, ll_void_p)))
    check_blas_return(context, builder, res)


def call_xxgemm(context, builder, x_type, x_shapes, x_data, y_type, y_shapes, y_data, out_type, out_shapes, out_data):
    '''
    Call the BLAS matrix * matrix product function for the given arguments.
    '''
    pass
# WARNING: Decompyle incomplete


def dot_2_mm(context, builder, sig, args):
    '''
    np.dot(matrix, matrix)
    '''
    
    def dot_impl(a, b):
        (m, k) = a.shape
        (_k, n) = b.shape
        if k == 0:
            return np.zeros((m, n), a.dtype)
        out = None.empty((m, n), a.dtype)
        return np.dot(a, b, out)

    res = context.compile_internal(builder, dot_impl, sig, args)
    return impl_ret_new_ref(context, builder, sig.return_type, res)


def dot_2_vm(context, builder, sig, args):
    '''
    np.dot(vector, matrix)
    '''
    
    def dot_impl(a, b):
        (m,) = a.shape
        (_m, n) = b.shape
        if m == 0:
            return np.zeros((n,), a.dtype)
        out = None.empty((n,), a.dtype)
        return np.dot(a, b, out)

    res = context.compile_internal(builder, dot_impl, sig, args)
    return impl_ret_new_ref(context, builder, sig.return_type, res)


def dot_2_mv(context, builder, sig, args):
    '''
    np.dot(matrix, vector)
    '''
    
    def dot_impl(a, b):
        (m, n) = a.shape
        (_n,) = b.shape
        if n == 0:
            return np.zeros((m,), a.dtype)
        out = None.empty((m,), a.dtype)
        return np.dot(a, b, out)

    res = context.compile_internal(builder, dot_impl, sig, args)
    return impl_ret_new_ref(context, builder, sig.return_type, res)


def dot_2_vv(context, builder, sig, args, conjugate = (False,)):
    '''
    np.dot(vector, vector)
    np.vdot(vector, vector)
    '''
    (aty, bty) = sig.args
    dtype = sig.return_type
    a = make_array(aty)(context, builder, args[0])
    b = make_array(bty)(context, builder, args[1])
    (n,) = cgutils.unpack_tuple(builder, a.shape)
    
    def check_args(a, b):
        (m,) = a.shape
        (n,) = b.shape
        if m != n:
            raise ValueError('incompatible array sizes for np.dot(a, b) (vector * vector)')

# WARNING: Decompyle incomplete

dot_2 = (lambda left, right: dot_2_impl('np.dot()', left, right))()
matmul_2 = (lambda left, right: dot_2_impl("'@'", left, right))()

def dot_2_impl(name, left, right):
    pass
# WARNING: Decompyle incomplete

vdot = (lambda left, right: pass# WARNING: Decompyle incomplete
)()

def dot_3_vm_check_args(a, b, out):
    (m,) = a.shape
    (_m, n) = b.shape
    if m != _m:
        raise ValueError('incompatible array sizes for np.dot(a, b) (vector * matrix)')
    if out.shape != (n,):
        raise ValueError('incompatible output array size for np.dot(a, b, out) (vector * matrix)')


def dot_3_mv_check_args(a, b, out):
    (m, _n) = a.shape
    (n,) = b.shape
    if n != _n:
        raise ValueError('incompatible array sizes for np.dot(a, b) (matrix * vector)')
    if out.shape != (m,):
        raise ValueError('incompatible output array size for np.dot(a, b, out) (matrix * vector)')


def dot_3_vm(context, builder, sig, args):
    '''
    np.dot(vector, matrix, out)
    np.dot(matrix, vector, out)
    '''
    (xty, yty, outty) = sig.args
# WARNING: Decompyle incomplete


def dot_3_mm(context, builder, sig, args):
    '''
    np.dot(matrix, matrix, out)
    '''
    (xty, yty, outty) = sig.args
# WARNING: Decompyle incomplete

dot_3 = (lambda left, right, out: pass# WARNING: Decompyle incomplete
)()
_check_finite_matrix = (lambda a: for v in np.nditer(a):
if not np.isfinite(v.item()):
raise np.linalg.LinAlgError('Array must not contain infs or NaNs.')None)()

def _check_linalg_matrix(a, func_name, la_prefix = (True,)):
    prefix = 'np.linalg' if la_prefix else 'np'
    interp = (prefix, func_name)
    if isinstance(a, types.Optional):
        a = a.type
    if not isinstance(a, types.Array):
        msg = '%s.%s() only supported for array types' % interp
        raise TypingError(msg, highlighting = False)
    if not a.ndim == 2:
        msg = '%s.%s() only supported on 2-D arrays.' % interp
        raise TypingError(msg, highlighting = False)
    if not isinstance(a.dtype, (types.Float, types.Complex)):
        msg = '%s.%s() only supported on float and complex arrays.' % interp
        raise TypingError(msg, highlighting = False)


def _check_homogeneous_types(func_name, *types):
    t0 = types[0].dtype
    for t in types[1:]:
        if t.dtype != t0:
            msg = 'np.linalg.%s() only supports inputs that have homogeneous dtypes.' % func_name
            raise TypingError(msg, highlighting = False)
        return None


def _copy_to_fortran_order():
    pass

ol_copy_to_fortran_order = (lambda a: pass# WARNING: Decompyle incomplete
)()
_inv_err_handler = (lambda r: pass# WARNING: Decompyle incomplete
)()
_dummy_liveness_func = (lambda a: a[0])()
inv_impl = (lambda a: pass# WARNING: Decompyle incomplete
)()
_handle_err_maybe_convergence_problem = (lambda r: pass# WARNING: Decompyle incomplete
)()

def _check_linalg_1_or_2d_matrix(a, func_name, la_prefix = (True,)):
    prefix = 'np.linalg' if la_prefix else 'np'
    interp = (prefix, func_name)
    if not isinstance(a, types.Array):
        raise TypingError('%s.%s() only supported for array types ' % interp)
    if not a.ndim <= 2:
        raise TypingError('%s.%s() only supported on 1 and 2-D arrays ' % interp)
    if not isinstance(a.dtype, (types.Float, types.Complex)):
        raise TypingError('%s.%s() only supported on float and complex arrays.' % interp)

cho_impl = (lambda a: pass# WARNING: Decompyle incomplete
)()
eig_impl = (lambda a: pass# WARNING: Decompyle incomplete
)()
eigvals_impl = (lambda a: pass# WARNING: Decompyle incomplete
)()
eigh_impl = (lambda a: pass# WARNING: Decompyle incomplete
)()
eigvalsh_impl = (lambda a: pass# WARNING: Decompyle incomplete
)()
svd_impl = (lambda a, full_matrices = (1,): pass# WARNING: Decompyle incomplete
)()
qr_impl = (lambda a: pass# WARNING: Decompyle incomplete
)()

def _system_copy_in_b(bcpy, b, nrhs):
    """
    Correctly copy 'b' into the 'bcpy' scratch space.
    """
    raise NotImplementedError

_system_copy_in_b_impl = (lambda bcpy, b, nrhs:
