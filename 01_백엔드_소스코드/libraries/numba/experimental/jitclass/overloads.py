# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: overloads.pyc (Python 3.11)

'''
Overloads for ClassInstanceType for built-in functions that call dunder methods
on an object.
'''
from functools import wraps
import inspect
import operator
from numba.core.extending import overload
from numba.core.types import ClassInstanceType

def _get_args(n_args):
    pass
# WARNING: Decompyle incomplete


def class_instance_overload(target):
    '''
    Decorator to add an overload for target that applies when the first argument
    is a ClassInstanceType.
    '''
    pass
# WARNING: Decompyle incomplete


def extract_template(template, name):
    '''
    Extract a code-generated function from a string template.
    '''
    namespace = { }
    exec(template, namespace)
    return namespace[name]


def register_simple_overload(func = None, *, n_args, *attrs):
    '''
    Register an overload for func that checks for methods __attr__ for each
    attr in attrs.
    '''
    pass
# WARNING: Decompyle incomplete


def try_call_method(cls_type, method, n_args = (1,)):
    '''
    If method is defined for cls_type, return a callable that calls this method.
    If not, return None.
    '''
    if method in cls_type.jit_methods:
        arg_names = _get_args(n_args)
        template = f'''\ndef func({','.join(arg_names)}):\n    return {arg_names[0]}.{method}({','.join(arg_names[1:])})\n'''
        return extract_template(template, 'func')


def try_call_complex_method(cls_type, method):
    ''' __complex__ needs special treatment as the argument names are kwargs
    and therefore specific in name and default value.
    '''
    if method in cls_type.jit_methods:
        template = f'''\ndef func(real=0, imag=0):\n    return real.{method}()\n'''
        return extract_template(template, 'func')


def take_first(*options):
    '''
    Take the first non-None option.
    '''
    pass
# WARNING: Decompyle incomplete

class_bool = (lambda x: using_bool_impl = try_call_method(x, '__bool__')if '__len__' in x.jit_methods:

def using_len_impl(x):
bool(len(x))else:
using_len_impl = None
always_true_impl = lambda x: Truetake_first(using_bool_impl, using_len_impl, always_true_impl))()
class_complex = (lambda real, imag = (0, 0): take_first(try_call_complex_method(real, '__complex__'), (lambda real, imag = (0, 0): complex(float(real))))
)()
class_contains = (lambda x, y: try_call_method(x, '__contains__', 2))()
class_float = (lambda x: options = [
try_call_method(x, '__float__')]if '__index__' in x.jit_methods:
options.append((lambda x: float(x.__index__())))
# WARNING: Decompyle incomplete
)()
class_int = (lambda x: options = [
try_call_method(x, '__int__')]options.append(try_call_method(x, '__index__'))# WARNING: Decompyle incomplete
)()
class_str = (lambda x: take_first(try_call_method(x, '__str__'), (lambda x: repr(x)))
)()
class_ne = (lambda x, y: take_first(try_call_method(x, '__ne__', 2), (lambda x, y: not (x == y)))
)()

def register_reflected_overload(func, meth_forward, meth_reflected):
    pass
# WARNING: Decompyle incomplete

register_simple_overload(abs, 'abs')
register_simple_overload(len, 'len')
register_simple_overload(hash, 'hash')
register_reflected_overload(operator.ge, 'ge', 'le')
register_reflected_overload(operator.gt, 'gt', 'lt')
register_reflected_overload(operator.le, 'le', 'ge')
register_reflected_overload(operator.lt, 'lt', 'gt')
register_reflected_overload(operator.eq, 'eq', 'eq')
register_simple_overload(operator.add, 'add', n_args = 2)
register_simple_overload(operator.floordiv, 'floordiv', n_args = 2)
register_simple_overload(operator.lshift, 'lshift', n_args = 2)
register_simple_overload(operator.mul, 'mul', n_args = 2)
register_simple_overload(operator.mod, 'mod', n_args = 2)
register_simple_overload(operator.neg, 'neg')
register_simple_overload(operator.pos, 'pos')
register_simple_overload(operator.invert, 'invert')
register_simple_overload(operator.pow, 'pow', n_args = 2)
register_simple_overload(operator.rshift, 'rshift', n_args = 2)
register_simple_overload(operator.sub, 'sub', n_args = 2)
register_simple_overload(operator.truediv, 'truediv', n_args = 2)
register_simple_overload(operator.iadd, 'iadd', 'add', n_args = 2)
register_simple_overload(operator.ifloordiv, 'ifloordiv', 'floordiv', n_args = 2)
register_simple_overload(operator.ilshift, 'ilshift', 'lshift', n_args = 2)
register_simple_overload(operator.imul, 'imul', 'mul', n_args = 2)
register_simple_overload(operator.imod, 'imod', 'mod', n_args = 2)
register_simple_overload(operator.ipow, 'ipow', 'pow', n_args = 2)
register_simple_overload(operator.irshift, 'irshift', 'rshift', n_args = 2)
register_simple_overload(operator.isub, 'isub', 'sub', n_args = 2)
register_simple_overload(operator.itruediv, 'itruediv', 'truediv', n_args = 2)
register_simple_overload(operator.and_, 'and', n_args = 2)
register_simple_overload(operator.or_, 'or', n_args = 2)
register_simple_overload(operator.xor, 'xor', n_args = 2)
register_simple_overload(operator.iand, 'iand', 'and', n_args = 2)
register_simple_overload(operator.ior, 'ior', 'or', n_args = 2)
register_simple_overload(operator.ixor, 'ixor', 'xor', n_args = 2)
