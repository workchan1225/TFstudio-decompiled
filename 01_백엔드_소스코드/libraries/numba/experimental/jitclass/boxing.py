# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: boxing.pyc (Python 3.11)

'''
Implement logic relating to wrapping (box) and unwrapping (unbox) instances
of jitclasses for use inside the python interpreter.
'''
from functools import wraps, partial
from llvmlite import ir
from numba.core import types, cgutils
from numba.core.decorators import njit
from numba.core.pythonapi import box, unbox, NativeValue
from numba.core.typing.typeof import typeof_impl
from numba.experimental.jitclass import _box
_getter_code_template = '\ndef accessor(__numba_self_):\n    return __numba_self_.{0}\n'
_setter_code_template = '\ndef mutator(__numba_self_, __numba_val):\n    __numba_self_.{0} = __numba_val\n'
_method_code_template = '\ndef method(__numba_self_, *args):\n    return __numba_self_.{method}(*args)\n'

def _generate_property(field, template, fname):
    '''
    Generate simple function that get/set a field of the instance
    '''
    source = template.format(field)
    glbls = { }
    exec(source, glbls)
    return njit(glbls[fname])

_generate_getter = partial(_generate_property, template = _getter_code_template, fname = 'accessor')
_generate_setter = partial(_generate_property, template = _setter_code_template, fname = 'mutator')

def _generate_method(name, func):
    '''
    Generate a wrapper for calling a method.  Note the wrapper will only
    accept positional arguments.
    '''
    pass
# WARNING: Decompyle incomplete

_cache_specialized_box = { }

def _specialize_box(typ):
    '''
    Create a subclass of Box that is specialized to the jitclass.

    This function caches the result to avoid code bloat.
    '''
    if typ in _cache_specialized_box:
        return _cache_specialized_box[typ]
    dct = {
        '__slots__': None,
        '_numba_type_': typ,
        '__doc__': typ.class_type.class_doc }
# WARNING: Decompyle incomplete

_box_class_instance = (lambda typ, val, c: pass# WARNING: Decompyle incomplete
)()
_unbox_class_instance = (lambda typ, val, c: pass# WARNING: Decompyle incomplete
)()
_typeof_jitclass_box = (lambda val, c: getattr(type(val), '_numba_type_'))()
