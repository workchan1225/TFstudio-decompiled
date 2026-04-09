# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polynomial_core.pyc (Python 3.11)

from numba.extending import models, register_model, type_callable, unbox, NativeValue, make_attribute_wrapper, box, lower_builtin
from numba.core import types, cgutils
import warnings
from numba.core.errors import NumbaExperimentalFeatureWarning, NumbaValueError
from numpy.polynomial.polynomial import Polynomial
from contextlib import ExitStack
import numpy as np
from llvmlite import ir
PolynomialModel = <NODE:12>()
type_polynomial = (lambda context: 
def typer(coef, domain, window = (None, None)):
default_domain = types.Array(types.int64, 1, 'C')double_domain = types.Array(types.double, 1, 'C')default_window = types.Array(types.int64, 1, 'C')double_window = types.Array(types.double, 1, 'C')double_coef = types.Array(types.double, 1, 'C')warnings.warn('Polynomial class is experimental', category = NumbaExperimentalFeatureWarning)if isinstance(coef, types.Array) and (lambda .0: [ a is None for a in .0 ])((domain, window)()):
            if coef.ndim == 1:
                return types.PolynomialType(double_coef, default_domain, default_window, 1)
            msg = all
            raise NumbaValueError(msg)
        if (lambda .0: [ isinstance(a, types.Array) for a in .0 ])((coef, domain, window)()):
            if coef.ndim == 1:
                if (lambda .0: [ a.ndim == 1 for a in .0 ])((domain, window)()):
                    return types.PolynomialType(double_coef, double_domain, double_window, 3)
                return all
            msg = all
            raise NumbaValueError(msg)
typer)()
make_attribute_wrapper(types.PolynomialType, 'coef', 'coef')
make_attribute_wrapper(types.PolynomialType, 'domain', 'domain')
make_attribute_wrapper(types.PolynomialType, 'window', 'window')
impl_polynomial1 = (lambda context, builder, sig, args: 
def to_double(arr):
np.asarray(arr, dtype = np.double)
def const_impl():
np.asarray([
-1,
1])typ = sig.return_typepolynomial = cgutils.create_struct_proxy(typ)(context, builder)sig_coef = sig.args[0].copy(dtype = types.double)(sig.args[0])coef_cast = context.compile_internal(builder, to_double, sig_coef, args)sig_domain = sig.args[0].copy(dtype = types.intp)()sig_window = sig.args[0].copy(dtype = types.intp)()domain_cast = context.compile_internal(builder, const_impl, sig_domain, ())window_cast = context.compile_internal(builder, const_impl, sig_window, ())polynomial.coef = coef_castpolynomial.domain = domain_castpolynomial.window = window_castpolynomial._getvalue())()
impl_polynomial3 = (lambda context, builder, sig, args:
