# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: generator_methods.pyc (Python 3.11)

'''
Implementation of method overloads for Generator objects.
'''
import numpy as np
from numba.core import types
from numba.core.extending import overload_method, register_jitable
from numba.np.numpy_support import as_dtype, from_dtype
from numba.np.random.generator_core import next_float, next_double
from numba.np.numpy_support import is_nonelike
from numba.core.errors import TypingError
from numba.core.types.containers import Tuple, UniTuple
from numba.np.random.distributions import random_standard_exponential_inv_f, random_standard_exponential_inv, random_standard_exponential, random_standard_normal_f, random_standard_gamma, random_standard_normal, random_uniform, random_standard_exponential_f, random_standard_gamma_f, random_normal, random_exponential, random_gamma, random_beta, random_power, random_f, random_chisquare, random_standard_cauchy, random_pareto, random_weibull, random_laplace, random_logistic, random_lognormal, random_rayleigh, random_standard_t, random_wald, random_geometric, random_zipf, random_triangular, random_poisson, random_negative_binomial, random_logseries, random_noncentral_chisquare, random_noncentral_f, random_binomial
from numba.np.random import random_methods

def _get_proper_func(func_32, func_64, dtype, dist_name = ('the given',)):
    '''
        Most of the standard NumPy distributions that accept dtype argument
        only support either np.float32 or np.float64 as dtypes.

        This is a helper function that helps Numba select the proper underlying
        implementation according to provided dtype.
    '''
    if isinstance(dtype, types.Omitted):
        dtype = dtype.value
    np_dt = dtype
    if isinstance(dtype, type):
        nb_dt = from_dtype(np.dtype(dtype))
    elif isinstance(dtype, types.NumberClass):
        nb_dt = dtype
        np_dt = as_dtype(nb_dt)
    if np_dt not in (np.float32, np.float64):
        raise TypingError('Argument dtype is not one of the expected type(s):  np.float32 or np.float64')
    if np_dt == np.float32:
        next_func = func_32
    else:
        next_func = func_64
    return (next_func, nb_dt)


def check_size(size):
    if isinstance(size, UniTuple):
        pass
    if not isinstance(size, Tuple) or any([
        isinstance(size.dtype, types.Integer),
        size.count == 0,
        isinstance(size, types.Integer)]):
        raise TypingError('Argument size is not one of the expected type(s):  an integer, an empty tuple or a tuple of integers')


def check_types(obj, type_list, arg_name):
    '''
    Check if given object is one of the provided types.
    If not raises an TypeError
    '''
    pass
# WARNING: Decompyle incomplete

NumPyRandomGeneratorType_integers = (lambda inst, low, high, size, dtype, endpoint = (None, np.int64, False): pass# WARNING: Decompyle incomplete
)()
NumPyRandomGeneratorType_shuffle = (lambda inst, x, axis = (0,): check_types(x, [
types.Array], 'x')check_types(axis, [
int,
types.Integer], 'axis')
def impl(inst, x, axis = (0,)):
if axis < 0:
axis = axis + x.ndimif axis > x.ndim - 1 or axis < 0:
raise IndexError('Axis is out of bounds for the given array')z = np.swapaxes(x, 0, axis)buf = np.empty_like(z[(0, ...)])for i in range(len(z) - 1, 0, -1):
j = types.intp(random_methods.random_interval(inst.bit_generator, i))if i == j:
continuebuf[...] = z[(j, ...)]z[(j, ...)] = z[(i, ...)]z[(i, ...)] = bufNoneimpl)()
NumPyRandomGeneratorType_permutation = (lambda inst, x, axis = (0,): pass# WARNING: Decompyle incomplete
)()
NumPyRandomGeneratorType_random = (lambda inst, size, dtype = (None, np.float64): pass# WARNING: Decompyle incomplete
)()
NumPyRandomGeneratorType_standard_exponential = (lambda inst, size, dtype, method = (None, np.float64, 'zig'): pass# WARNING: Decompyle incomplete
)()
NumPyRandomGeneratorType_standard_normal = (lambda inst, size, dtype = (None, np.float64): pass# WARNING: Decompyle incomplete
)()
NumPyRandomGeneratorType_standard_gamma = (lambda inst, shape, size, dtype = (None, np.float64): pass# WARNING: Decompyle incomplete
)()
NumPyRandomGeneratorType_normal = (lambda inst, loc, scale, size = (0, 1, None): check_types(loc, [
types.Float,
types.Integer,
int,
float], 'loc')check_types(scale, [
types.Float,
types.Integer,
int,
float], 'scale')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, loc, scale, size = (0, 1, None)):
random_normal(inst.bit_generator, loc, scale)implNone(size)
def impl(inst, loc, scale, size = (0, 1, None)):
out = np.empty(size, dtype = np.float64)out_f = out.flatfor i in range(out.size):
out_f[i] = random_normal(inst.bit_generator, loc, scale)outimpl)()
NumPyRandomGeneratorType_uniform = (lambda inst, low, high, size = (0, 1, None): check_types(low, [
types.Float,
types.Integer,
int,
float], 'low')check_types(high, [
types.Float,
types.Integer,
int,
float], 'high')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, low, high, size = (0, 1, None)):
random_uniform(inst.bit_generator, low, high - low)implNone(size)
def impl(inst, low, high, size = (0, 1, None)):
out = np.empty(size, dtype = np.float64)out_f = out.flatfor i in range(out.size):
out_f[i] = random_uniform(inst.bit_generator, low, high - low)outimpl)()
NumPyRandomGeneratorType_exponential = (lambda inst, scale, size = (1, None): check_types(scale, [
types.Float,
types.Integer,
int,
float], 'scale')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, scale, size = (1, None)):
random_exponential(inst.bit_generator, scale)implNone(size)
def impl(inst, scale, size = (1, None)):
out = np.empty(size, dtype = np.float64)out_f = out.flatfor i in range(out.size):
out_f[i] = random_exponential(inst.bit_generator, scale)outimpl)()
NumPyRandomGeneratorType_gamma = (lambda inst, shape, scale, size = (1, None): check_types(shape, [
types.Float,
types.Integer,
int,
float], 'shape')check_types(scale, [
types.Float,
types.Integer,
int,
float], 'scale')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, shape, scale, size = (1, None)):
random_gamma(inst.bit_generator, shape, scale)implNone(size)
def impl(inst, shape, scale, size = (1, None)):
out = np.empty(size, dtype = np.float64)out_f = out.flatfor i in range(out.size):
out_f[i] = random_gamma(inst.bit_generator, shape, scale)outimpl)()
NumPyRandomGeneratorType_beta = (lambda inst, a, b, size = (None,): check_types(a, [
types.Float,
types.Integer,
int,
float], 'a')check_types(b, [
types.Float,
types.Integer,
int,
float], 'b')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, a, b, size = (None,)):
random_beta(inst.bit_generator, a, b)implNone(size)
def impl(inst, a, b, size = (None,)):
out = np.empty(size)out_f = out.flatfor i in range(out.size):
out_f[i] = random_beta(inst.bit_generator, a, b)outimpl)()
NumPyRandomGeneratorType_f = (lambda inst, dfnum, dfden, size = (None,): check_types(dfnum, [
types.Float,
types.Integer,
int,
float], 'dfnum')check_types(dfden, [
types.Float,
types.Integer,
int,
float], 'dfden')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, dfnum, dfden, size = (None,)):
random_f(inst.bit_generator, dfnum, dfden)implNone(size)
def impl(inst, dfnum, dfden, size = (None,)):
out = np.empty(size)out_f = out.flatfor i in range(out.size):
out_f[i] = random_f(inst.bit_generator, dfnum, dfden)outimpl)()
NumPyRandomGeneratorType_chisquare = (lambda inst, df, size = (None,): check_types(df, [
types.Float,
types.Integer,
int,
float], 'df')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, df, size = (None,)):
random_chisquare(inst.bit_generator, df)implNone(size)
def impl(inst, df, size = (None,)):
out = np.empty(size)out_f = out.flatfor i in range(out.size):
out_f[i] = random_chisquare(inst.bit_generator, df)outimpl)()
NumPyRandomGeneratorType_standard_cauchy = (lambda inst, size = (None,): if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, size = (None,)):
random_standard_cauchy(inst.bit_generator)implNone(size)
def impl(inst, size = (None,)):
out = np.empty(size)out_f = out.flatfor i in range(out.size):
out_f[i] = random_standard_cauchy(inst.bit_generator)outimpl)()
NumPyRandomGeneratorType_pareto = (lambda inst, a, size = (None,): check_types(a, [
types.Float,
types.Integer,
int,
float], 'a')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, a, size = (None,)):
random_pareto(inst.bit_generator, a)implNone(size)
def impl(inst, a, size = (None,)):
out = np.empty(size)out_f = out.flatfor i in range(out.size):
out_f[i] = random_pareto(inst.bit_generator, a)outimpl)()
NumPyRandomGeneratorType_weibull = (lambda inst, a, size = (None,): check_types(a, [
types.Float,
types.Integer,
int,
float], 'a')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, a, size = (None,)):
random_weibull(inst.bit_generator, a)implNone(size)
def impl(inst, a, size = (None,)):
out = np.empty(size)out_f = out.flatfor i in range(out.size):
out_f[i] = random_weibull(inst.bit_generator, a)outimpl)()
NumPyRandomGeneratorType_power = (lambda inst, a, size = (None,): check_types(a, [
types.Float,
types.Integer,
int,
float], 'a')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, a, size = (None,)):
random_power(inst.bit_generator, a)implNone(size)
def impl(inst, a, size = (None,)):
out = np.empty(size)out_f = out.flatfor i in range(out.size):
out_f[i] = random_power(inst.bit_generator, a)outimpl)()
NumPyRandomGeneratorType_laplace = (lambda inst, loc, scale, size = (0, 1, None): check_types(loc, [
types.Float,
types.Integer,
int,
float], 'loc')check_types(scale, [
types.Float,
types.Integer,
int,
float], 'scale')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, loc, scale, size = (0, 1, None)):
random_laplace(inst.bit_generator, loc, scale)implNone(size)
def impl(inst, loc, scale, size = (0, 1, None)):
out = np.empty(size)out_f = out.flatfor i in range(out.size):
out_f[i] = random_laplace(inst.bit_generator, loc, scale)outimpl)()
NumPyRandomGeneratorType_logistic = (lambda inst, loc, scale, size = (0, 1, None): check_types(loc, [
types.Float,
types.Integer,
int,
float], 'loc')check_types(scale, [
types.Float,
types.Integer,
int,
float], 'scale')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, loc, scale, size = (0, 1, None)):
random_logistic(inst.bit_generator, loc, scale)implNone(size)
def impl(inst, loc, scale, size = (0, 1, None)):
out = np.empty(size)out_f = out.flatfor i in range(out.size):
out_f[i] = random_logistic(inst.bit_generator, loc, scale)outimpl)()
NumPyRandomGeneratorType_lognormal = (lambda inst, mean, sigma, size = (0, 1, None): check_types(mean, [
types.Float,
types.Integer,
int,
float], 'mean')check_types(sigma, [
types.Float,
types.Integer,
int,
float], 'sigma')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, mean, sigma, size = (0, 1, None)):
random_lognormal(inst.bit_generator, mean, sigma)implNone(size)
def impl(inst, mean, sigma, size = (0, 1, None)):
out = np.empty(size)out_f = out.flatfor i in range(out.size):
out_f[i] = random_lognormal(inst.bit_generator, mean, sigma)outimpl)()
NumPyRandomGeneratorType_rayleigh = (lambda inst, scale, size = (1, None): check_types(scale, [
types.Float,
types.Integer,
int,
float], 'scale')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, scale, size = (1, None)):
random_rayleigh(inst.bit_generator, scale)implNone(size)
def impl(inst, scale, size = (1, None)):
out = np.empty(size)out_f = out.flatfor i in range(out.size):
out_f[i] = random_rayleigh(inst.bit_generator, scale)outimpl)()
NumPyRandomGeneratorType_standard_t = (lambda inst, df, size = (None,): check_types(df, [
types.Float,
types.Integer,
int,
float], 'df')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, df, size = (None,)):
random_standard_t(inst.bit_generator, df)implNone(size)
def impl(inst, df, size = (None,)):
out = np.empty(size)out_f = out.flatfor i in range(out.size):
out_f[i] = random_standard_t(inst.bit_generator, df)outimpl)()
NumPyRandomGeneratorType_wald = (lambda inst, mean, scale, size = (None,): check_types(mean, [
types.Float,
types.Integer,
int,
float], 'mean')check_types(scale, [
types.Float,
types.Integer,
int,
float], 'scale')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, mean, scale, size = (None,)):
random_wald(inst.bit_generator, mean, scale)implNone(size)
def impl(inst, mean, scale, size = (None,)):
out = np.empty(size)out_f = out.flatfor i in range(out.size):
out_f[i] = random_wald(inst.bit_generator, mean, scale)outimpl)()
NumPyRandomGeneratorType_geometric = (lambda inst, p, size = (None,): check_types(p, [
types.Float,
types.Integer,
int,
float], 'p')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, p, size = (None,)):
np.int64(random_geometric(inst.bit_generator, p))implNone(size)
def impl(inst, p, size = (None,)):
out = np.empty(size, dtype = np.int64)out_f = out.flatfor i in range(out.size):
out_f[i] = random_geometric(inst.bit_generator, p)outimpl)()
NumPyRandomGeneratorType_zipf = (lambda inst, a, size = (None,): check_types(a, [
types.Float,
types.Integer,
int,
float], 'a')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, a, size = (None,)):
np.int64(random_zipf(inst.bit_generator, a))implNone(size)
def impl(inst, a, size = (None,)):
out = np.empty(size, dtype = np.int64)out_f = out.flatfor i in range(out.size):
out_f[i] = random_zipf(inst.bit_generator, a)outimpl)()
NumPyRandomGeneratorType_triangular = (lambda inst, left, mode, right, size = (None,): check_types(left, [
types.Float,
types.Integer,
int,
float], 'left')check_types(mode, [
types.Float,
types.Integer,
int,
float], 'mode')check_types(right, [
types.Float,
types.Integer,
int,
float], 'right')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, left, mode, right, size = (None,)):
random_triangular(inst.bit_generator, left, mode, right)implNone(size)
def impl(inst, left, mode, right, size = (None,)):
out = np.empty(size)out_f = out.flatfor i in range(out.size):
out_f[i] = random_triangular(inst.bit_generator, left, mode, right)outimpl)()
NumPyRandomGeneratorType_poisson = (lambda inst, lam, size = (None,): check_types(lam, [
types.Float,
types.Integer,
int,
float], 'lam')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, lam, size = (None,)):
np.int64(random_poisson(inst.bit_generator, lam))implNone(size)
def impl(inst, lam, size = (None,)):
out = np.empty(size, dtype = np.int64)out_f = out.flatfor i in range(out.size):
out_f[i] = random_poisson(inst.bit_generator, lam)outimpl)()
NumPyRandomGeneratorType_negative_binomial = (lambda inst, n, p, size = (None,): check_types(n, [
types.Float,
types.Integer,
int,
float], 'n')check_types(p, [
types.Float,
types.Integer,
int,
float], 'p')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, n, p, size = (None,)):
np.int64(random_negative_binomial(inst.bit_generator, n, p))implNone(size)
def impl(inst, n, p, size = (None,)):
out = np.empty(size, dtype = np.int64)out_f = out.flatfor i in range(out.size):
out_f[i] = random_negative_binomial(inst.bit_generator, n, p)outimpl)()
NumPyRandomGeneratorType_noncentral_chisquare = (lambda inst, df, nonc, size = (None,): pass# WARNING: Decompyle incomplete
)()
NumPyRandomGeneratorType_noncentral_f = (lambda inst, dfnum, dfden, nonc, size = (None,): pass# WARNING: Decompyle incomplete
)()
NumPyRandomGeneratorType_logseries = (lambda inst, p, size = (None,): pass# WARNING: Decompyle incomplete
)()
NumPyRandomGeneratorType_binomial = (lambda inst, n, p, size = (None,): check_types(n, [
types.Float,
types.Integer,
int,
float], 'n')check_types(p, [
types.Float,
types.Integer,
int,
float], 'p')if isinstance(size, types.Omitted):
size = size.valueif is_nonelike(size):

def impl(inst, n, p, size = (None,)):
np.int64(random_binomial(inst.bit_generator, n, p))implNone(size)
def impl(inst, n, p, size = (None,)):
out = np.empty(size, dtype = np.int64)for i in np.ndindex(size):
out[i] = random_binomial(inst.bit_generator, n, p)outimpl)()
