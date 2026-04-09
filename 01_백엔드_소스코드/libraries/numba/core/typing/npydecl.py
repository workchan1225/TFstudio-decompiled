# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: npydecl.pyc (Python 3.11)

import warnings
import numpy as np
import operator
from numba.core import types, utils, config
from numba.core.typing.templates import AttributeTemplate, AbstractTemplate, CallableTemplate, Registry, signature
from numba.np.numpy_support import ufunc_find_matching_loop, supported_ufunc_loop, as_dtype, from_dtype, as_dtype, resolve_output_type, carray, farray, _ufunc_loop_sig
from numba.core.errors import TypingError, NumbaPerformanceWarning, NumbaTypeError, NumbaAssertionError
from numba import pndindex
registry = Registry()
infer = registry.register
infer_global = registry.register_global
infer_getattr = registry.register_attr

class Numpy_rules_ufunc(AbstractTemplate):
    _handle_inputs = (lambda cls, ufunc, args, kws: nin = ufunc.ninnout = ufunc.noutnargs = ufunc.nargs# WARNING: Decompyle incomplete
)()
    ufunc = (lambda self: self.key)()
    
    def generic(self, args, kws):
        pass
    # WARNING: Decompyle incomplete



class NumpyRulesArrayOperator(Numpy_rules_ufunc):
    pass
# WARNING: Decompyle incomplete

_binop_map = NumpyRulesArrayOperator._op_map

class NumpyRulesInplaceArrayOperator(NumpyRulesArrayOperator):
    pass
# WARNING: Decompyle incomplete


class NumpyRulesUnaryArrayOperator(NumpyRulesArrayOperator):
    pass
# WARNING: Decompyle incomplete

math_operations = [
    'add',
    'subtract',
    'multiply',
    'logaddexp',
    'logaddexp2',
    'true_divide',
    'floor_divide',
    'negative',
    'positive',
    'power',
    'float_power',
    'remainder',
    'fmod',
    'absolute',
    'rint',
    'sign',
    'conjugate',
    'exp',
    'exp2',
    'log',
    'log2',
    'log10',
    'expm1',
    'log1p',
    'sqrt',
    'square',
    'cbrt',
    'reciprocal',
    'divide',
    'mod',
    'divmod',
    'abs',
    'fabs',
    'gcd',
    'lcm']
trigonometric_functions = [
    'sin',
    'cos',
    'tan',
    'arcsin',
    'arccos',
    'arctan',
    'arctan2',
    'hypot',
    'sinh',
    'cosh',
    'tanh',
    'arcsinh',
    'arccosh',
    'arctanh',
    'deg2rad',
    'rad2deg',
    'degrees',
    'radians']
bit_twiddling_functions = [
    'bitwise_and',
    'bitwise_or',
    'bitwise_xor',
    'invert',
    'left_shift',
    'right_shift',
    'bitwise_not']
comparison_functions = [
    'greater',
    'greater_equal',
    'less',
    'less_equal',
    'not_equal',
    'equal',
    'logical_and',
    'logical_or',
    'logical_xor',
    'logical_not',
    'maximum',
    'minimum',
    'fmax',
    'fmin']
floating_functions = [
    'isfinite',
    'isinf',
    'isnan',
    'signbit',
    'copysign',
    'nextafter',
    'modf',
    'ldexp',
    'frexp',
    'floor',
    'ceil',
    'trunc',
    'spacing']
logic_functions = [
    'isnat']
_unsupported = set([
    'frexp',
    'modf'])

def register_numpy_ufunc(name, register_global = (infer_global,)):
    pass
# WARNING: Decompyle incomplete

all_ufuncs = sum([
    math_operations,
    trigonometric_functions,
    bit_twiddling_functions,
    comparison_functions,
    floating_functions,
    logic_functions], [])
supported_ufuncs = all_ufuncs()
for func in supported_ufuncs:
    register_numpy_ufunc(func)
    all_ufuncs = all_ufuncs()
    supported_ufuncs = supported_ufuncs()
    NumpyRulesUnaryArrayOperator.install_operations()
    NumpyRulesArrayOperator.install_operations()
    NumpyRulesInplaceArrayOperator.install_operations()
    supported_array_operators = set(NumpyRulesUnaryArrayOperator._op_map.keys()).union(NumpyRulesArrayOperator._op_map.keys()).union(NumpyRulesInplaceArrayOperator._op_map.keys())
    del _unsupported
    
    class Numpy_method_redirection(AbstractTemplate):
        '''
    A template redirecting a Numpy global function (e.g. np.sum) to an
    array method of the same name (e.g. ndarray.sum).
    '''
        prefer_literal = True
        
        def generic(self, args, kws):
            pysig = None
        # WARNING: Decompyle incomplete


    
    def _numpy_redirect(fname):
        numpy_function = getattr(np, fname)
        cls = type('Numpy_redirect_{0}'.format(fname), (Numpy_method_redirection,), dict(key = numpy_function, method_name = fname))
        infer_global(numpy_function, types.Function(cls))

    for func in ('sum', 'argsort', 'nonzero', 'ravel'):
        _numpy_redirect(func)
register_number_classes(infer_global)

def parse_shape(shape):
    '''
    Given a shape, return the number of dimensions.
    '''
    pass
# WARNING: Decompyle incomplete


def parse_dtype(dtype):
    '''
    Return the dtype of a type, if it is either a DtypeSpec (used for most
    dtypes) or a TypeRef (used for record types).
    '''
    if isinstance(dtype, types.DTypeSpec):
        return dtype.dtype
    if None(dtype, types.TypeRef):
        return dtype.instance_type
    if None(dtype, types.StringLiteral):
        dtstr = dtype.literal_value
        
        try:
            dt = np.dtype(dtstr)
        except TypeError:
            msg = f'''Invalid NumPy dtype specified: \'{dtstr}\''''
            raise TypingError(msg)

        return from_dtype(dt)


def _parse_nested_sequence(context, typ):
    '''
    Parse a (possibly 0d) nested sequence type.
    A (ndim, dtype) tuple is returned.  Note the sequence may still be
    heterogeneous, as long as it converts to the given dtype.
    '''
    if isinstance(typ, (types.Buffer,)):
        raise TypingError('%s not allowed in a homogeneous sequence' % typ)
    if isinstance(typ, (types.Sequence,)):
        (n, dtype) = _parse_nested_sequence(context, typ.dtype)
        return (n + 1, dtype)
# WARNING: Decompyle incomplete


def _infer_dtype_from_inputs(inputs):
    return dtype


def _homogeneous_dims(context, func_name, arrays):
    ndim = arrays[0].ndim
    for a in arrays:
        if a.ndim != ndim:
            msg = f'''{func_name}(): all the input arrays must have same number of dimensions'''
            raise NumbaTypeError(msg)
        return ndim


def _sequence_of_arrays(context, func_name, arrays, dim_chooser = (_homogeneous_dims,)):
    if not isinstance(arrays, types.BaseTuple) and len(arrays) or (lambda .0: pass# WARNING: Decompyle incomplete
)(arrays()):
        raise TypingError(f'''{func_name!s}(): expecting a non-empty tuple of arrays, got {arrays!s}''')
    ndim = dim_chooser(context, func_name, arrays)
# WARNING: Decompyle incomplete


def _choose_concatenation_layout(arrays):
    return 'F' if (lambda .0: pass# WARNING: Decompyle incomplete
)(arrays()) else 'C'


class MatMulTyperMixin(object):
    
    def matmul_typer(self, a, b, out = (None,)):
        '''
        Typer function for Numpy matrix multiplication.
        '''
        pass
    # WARNING: Decompyle incomplete



def _check_linalg_matrix(a, func_name):
    if not isinstance(a, types.Array):
        return None
    if not None.ndim == 2:
        raise TypingError('np.linalg.%s() only supported on 2-D arrays' % func_name)
    if not isinstance(a.dtype, (types.Float, types.Complex)):
        raise TypingError('np.linalg.%s() only supported on float and complex arrays' % func_name)

NdEnumerate = <NODE:12>()
NdIter = <NODE:12>()
NdIndex = <NODE:12>()()
DtypeEq = <NODE:12>()
