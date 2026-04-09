# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: funcdesc.pyc (Python 3.11)

'''
Function descriptors.
'''
from collections import defaultdict
import importlib
from numba.core import types, itanium_mangler
from numba.core.utils import _dynamic_modname, _dynamic_module

def default_mangler(name = None, argtypes = {
    'abi_tags': (),
    'uid': None }, *, abi_tags, uid):
    return itanium_mangler.mangle(name, argtypes, abi_tags = abi_tags, uid = uid)


def qualifying_prefix(modname, qualname):
    '''
    Returns a new string that is used for the first half of the mangled name.
    '''
    return '{}.{}'.format(modname, qualname) if modname else qualname


class FunctionDescriptor(object):
    '''
    Base class for function descriptors: an object used to carry
    useful metadata about a natively callable function.

    Note that while `FunctionIdentity` denotes a Python function
    which is being concretely compiled by Numba, `FunctionDescriptor`
    may be more "abstract".
    '''
    __slots__ = ('native', 'modname', 'qualname', 'doc', 'typemap', 'calltypes', 'args', 'kws', 'restype', 'argtypes', 'mangled_name', 'unique_name', 'env_name', 'global_dict', 'inline', 'noalias', 'abi_tags', 'uid')
    
    def __init__(self, native, modname, qualname, unique_name, doc, typemap, restype, calltypes, args, kws, mangler, argtypes, inline, noalias, env_name, global_dict, abi_tags, uid = (None, None, False, False, None, None, (), None)):
        pass
    # WARNING: Decompyle incomplete

    
    def lookup_globals(self):
        """
        Return the global dictionary of the function.
        It may not match the Module's globals if the function is created
        dynamically (i.e. exec)
        """
        if not self.global_dict:
            pass
        return self.lookup_module().__dict__

    
    def lookup_module(self):
        """
        Return the module in which this function is supposed to exist.
        This may be a dummy module if the function was dynamically
        generated or the module can't be found.
        """
        if self.modname == _dynamic_modname:
            return _dynamic_module
        
        try:
            return importlib.import_module(self.modname)
        except ImportError:
            return 


    
    def lookup_function(self):
        '''
        Return the original function object described by this object.
        '''
        return getattr(self.lookup_module(), self.qualname)

    llvm_func_name = (lambda self: self.mangled_name)()
    llvm_cpython_wrapper_name = (lambda self: itanium_mangler.prepend_namespace(self.mangled_name, ns = 'cpython'))()
    llvm_cfunc_wrapper_name = (lambda self: 'cfunc.' + self.mangled_name)()
    
    def __repr__(self):
        return '<function descriptor %r>' % self.unique_name

    _get_function_info = (lambda cls, func_ir: func = func_ir.func_id.funcqualname = func_ir.func_id.func_qualnamemodname = func.__module__# WARNING: Decompyle incomplete
)()
    _from_python_function = (lambda cls, func_ir, typemap, restype, calltypes, native, mangler, inline, noalias, abi_tags = (None, False, False, ()): (qualname, unique_name, modname, doc, args, kws, global_dict) = cls._get_function_info(func_ir)self = cls(native, modname, qualname, unique_name, doc, typemap, restype, calltypes, args, kws, mangler = mangler, inline = inline, noalias = noalias, global_dict = global_dict, abi_tags = abi_tags, uid = func_ir.func_id.unique_id)self)()


class PythonFunctionDescriptor(FunctionDescriptor):
    '''
    A FunctionDescriptor subclass for Numba-compiled functions.
    '''
    __slots__ = ()
    from_specialized_function = (lambda cls, func_ir, typemap, restype, calltypes, mangler, inline, noalias, abi_tags: cls._from_python_function(func_ir, typemap, restype, calltypes, native = True, mangler = mangler, inline = inline, noalias = noalias, abi_tags = abi_tags))()
    from_object_mode_function = (lambda cls, func_ir: typemap = defaultdict((lambda : types.pyobject))
        calltypes = typemap.copy()
        restype = types.pyobject
        return cls._from_python_function(func_ir, typemap, restype, calltypes, native = False)
)()


class ExternalFunctionDescriptor(FunctionDescriptor):
    pass
# WARNING: Decompyle incomplete
