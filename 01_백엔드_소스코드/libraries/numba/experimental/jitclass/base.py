# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

import inspect
import operator
import types as pytypes
import typing as pt
from collections import OrderedDict
from collections.abc import Sequence
from llvmlite import ir as llvmir
from numba import njit
from numba.core import cgutils, errors, imputils, types, utils
from numba.core.datamodel import default_manager, models
from numba.core.registry import cpu_target
from numba.core.typing import templates
from numba.core.typing.asnumbatype import as_numba_type
from numba.core.serialize import disable_pickling
from numba.experimental.jitclass import _box

class InstanceModel(models.StructModel):
    pass
# WARNING: Decompyle incomplete


class InstanceDataModel(models.StructModel):
    pass
# WARNING: Decompyle incomplete

default_manager.register(types.ClassInstanceType, InstanceModel)
default_manager.register(types.ClassDataType, InstanceDataModel)
default_manager.register(types.ClassType, models.OpaqueModel)

def _mangle_attr(name):
    """
    Mangle attributes.
    The resulting name does not startswith an underscore '_'.
    """
    return 'm_' + name

_ctor_template = '\ndef ctor({args}):\n    return __numba_cls_({args})\n'

def _getargs(fn_sig):
    '''
    Returns list of positional and keyword argument names in order.
    '''
    params = fn_sig.parameters
    args = []
    for k, v in params.items():
        if v.kind & v.POSITIONAL_OR_KEYWORD == v.POSITIONAL_OR_KEYWORD:
            args.append(k)
            continue
        msg = '%s argument type unsupported in jitclass' % v.kind
        raise errors.UnsupportedError(msg)
        return args

JitClassType = <NODE:12>()

def _validate_spec(spec):
    for k, v in spec.items():
        if not isinstance(k, str):
            raise TypeError(f'''spec keys should be strings, got {k!r}''')
        if not isinstance(v, types.Type):
            raise TypeError(f'''spec values should be Numba type instances, got {v!r}''')
        return None


def _fix_up_private_attr(clsname, spec):
    '''
    Apply the same changes to dunder names as CPython would.
    '''
    out = OrderedDict()
    for k, v in spec.items():
        if not k.startswith('__') and k.endswith('__'):
            k = '_' + clsname + k
        out[k] = v
        return out


def _add_linking_libs(context, call):
    '''
    Add the required libs for the callable to allow inlining.
    '''
    libs = getattr(call, 'libs', ())
    if libs:
        context.add_linking_libs(libs)
        return None


def register_class_type(cls, spec, class_ctor, builder):
    '''
    Internal function to create a jitclass.

    Args
    ----
    cls: the original class object (used as the prototype)
    spec: the structural specification contains the field types.
    class_ctor: the numba type to represent the jitclass
    builder: the internal jitclass builder
    '''
    pass
# WARNING: Decompyle incomplete


class ConstructorTemplate(templates.AbstractTemplate):
    '''
    Base class for jitclass constructor templates.
    '''
    
    def generic(self, args, kws):
        instance_type = self.key.instance_type
        ctor = instance_type.jit_methods['__init__']
        boundargs = (instance_type.get_reference_type(),) + args
        disp_type = types.Dispatcher(ctor)
        sig = disp_type.get_call_type(self.context, boundargs, kws)
        if not isinstance(sig.return_type, types.NoneType):
            raise errors.NumbaTypeError(f'''__init__() should return None, not \'{sig.return_type}\'''')
    # WARNING: Decompyle incomplete



def _drop_ignored_attrs(dct):
    drop = set([
        '__weakref__',
        '__module__',
        '__dict__'])
    if utils.PYVERSION in ((3, 13), (3, 14)):
        drop |= set([
            '__firstlineno__',
            '__static_attributes__'])
# WARNING: Decompyle incomplete


class ClassBuilder(object):
    '''
    A jitclass builder for a mutable jitclass.  This will register
    typing and implementation hooks to the given typing and target contexts.
    '''
    class_impl_registry = imputils.Registry('jitclass builder')
    implemented_methods = set()
    
    def __init__(self, class_type, typingctx, targetctx):
        self.class_type = class_type
        self.typingctx = typingctx
        self.targetctx = targetctx

    
    def register(self):
        '''
        Register to the frontend and backend.
        '''
        self._register_methods(self.class_impl_registry, self.class_type.instance_type)
        self.targetctx.install_registry(self.class_impl_registry)

    
    def _register_methods(self, registry, instance_type):
        '''
        Register method implementations.
        This simply registers that the method names are valid methods.  Inside
        of imp() below we retrieve the actual method to run from the type of
        the receiver argument (i.e. self).
        '''
        to_register = list(instance_type.jit_methods) + list(instance_type.jit_static_methods)
        for meth in to_register:
            if meth not in self.implemented_methods:
                self._implement_method(registry, meth)
                self.implemented_methods.add(meth)
            return None

    
    def _implement_method(self, registry, attr):
        pass
    # WARNING: Decompyle incomplete


ClassAttribute = <NODE:12>()
get_attr_impl = (lambda context, builder, typ, value, attr: if attr in typ.struct:
inst = context.make_helper(builder, typ, value = value)data_pointer = inst.datadata = context.make_data_helper(builder, typ.get_data_type(), ref = data_pointer)imputils.impl_ret_borrowed(context, builder, typ.struct[attr], getattr(data, _mangle_attr(attr)))if None in typ.jit_props:
getter = typ.jit_props[attr]['get']sig = templates.signature(None, typ)dispatcher = types.Dispatcher(getter)sig = dispatcher.get_call_type(context.typing_context, [
typ], { })call = context.get_function(dispatcher, sig)out = call(builder, [
value])_add_linking_libs(context, call)imputils.impl_ret_new_ref(context, builder, sig.return_type, out)raise None('attribute {0!r} not implemented'.format(attr)))()
set_attr_impl = (lambda context, builder, sig, args, attr: (typ, valty) = sig.args(target, val) = argsif attr in typ.struct:
inst = context.make_helper(builder, typ, value = target)data_ptr = inst.datadata = context.make_data_helper(builder, typ.get_data_type(), ref = data_ptr)attr_type = typ.struct[attr]oldvalue = getattr(data, _mangle_attr(attr))setattr(data, _mangle_attr(attr), val)context.nrt.incref(builder, attr_type, val)context.nrt.decref(builder, attr_type, oldvalue)Noneif None in typ.jit_props:
setter = typ.jit_props[attr]['set']disp_type = types.Dispatcher(setter)sig = disp_type.get_call_type(context.typing_context, (typ, valty), { })call = context.get_function(disp_type, sig)call(builder, (target, val))_add_linking_libs(context, call)Noneraise None('attribute {0!r} not implemented'.format(attr)))()

def imp_dtor(context, module, instance_type):
    llvoidptr = context.get_value_type(types.voidptr)
    llsize = context.get_value_type(types.uintp)
    dtor_ftype = llvmir.FunctionType(llvmir.VoidType(), [
        llvoidptr,
        llsize,
        llvoidptr])
    fname = '_Dtor.{0}'.format(instance_type.name)
    dtor_fn = cgutils.get_or_insert_function(module, dtor_ftype, fname)
    if dtor_fn.is_declaration:
        builder = llvmir.IRBuilder(dtor_fn.append_basic_block())
        alloc_fe_type = instance_type.get_data_type()
        alloc_type = context.get_value_type(alloc_fe_type)
        ptr = builder.bitcast(dtor_fn.args[0], alloc_type.as_pointer())
        data = context.make_helper(builder, alloc_fe_type, ref = ptr)
        context.nrt.decref(builder, alloc_fe_type, data._getvalue())
        builder.ret_void()
    return dtor_fn

ctor_impl = (lambda context, builder, sig, args: inst_typ = sig.return_typealloc_type = context.get_data_type(inst_typ.get_data_type())alloc_size = context.get_abi_sizeof(alloc_type)meminfo = context.nrt.meminfo_alloc_dtor(builder, context.get_constant(types.uintp, alloc_size), imp_dtor(context, builder.module, inst_typ))data_pointer = context.nrt.meminfo_data(builder, meminfo)data_pointer = builder.bitcast(data_pointer, alloc_type.as_pointer())builder.store(cgutils.get_null_value(alloc_type), data_pointer)inst_struct = context.make_helper(builder, inst_typ)inst_struct.meminfo = meminfoinst_struct.data = data_pointerinit_sig = (sig.return_type,) + sig.argsinit = inst_typ.jit_methods['__init__']disp_type = types.Dispatcher(init)# WARNING: Decompyle incomplete
)()
