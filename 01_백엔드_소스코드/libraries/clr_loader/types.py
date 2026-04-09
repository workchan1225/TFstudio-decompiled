# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from os import PathLike
from typing import Any, Callable, Dict, Optional, Union
__all__ = [
    'StrOrPath']

try:
    StrOrPath = Union[(str, PathLike[str])]
except TypeError:
    StrOrPath = Union[(str, PathLike)]

RuntimeInfo = <NODE:12>()

class ClrFunction:
    
    def __init__(self, runtime = None, assembly = None, typename = None, func_name = ('runtime', 'Runtime', 'assembly', StrOrPath, 'typename', str, 'func_name', str)):
        self._assembly = assembly
        self._class = typename
        self._name = func_name
        self._callable = runtime._get_callable(assembly, typename, func_name)

    
    def __call__(self = None, buffer = None):
        ffi = ffi
        import ffi
        buf_arr = ffi.from_buffer('char[]', buffer)
        return self._callable(ffi.cast('void*', buf_arr), len(buf_arr))

    
    def __repr__(self = None):
        return f'''<ClrFunction {self._class}.{self._name} in {self._assembly}>'''



class Assembly:
    
    def __init__(self = None, runtime = None, path = None):
        self._runtime = runtime
        self._path = path

    
    def get_function(self = None, name = None, func = None):
        """Get a wrapped .NET function instance

        The function must be ``static``, and it must have the signature
        ``int Func(IntPtr ptr, int size)``. The returned wrapped instance will
        take a ``binary`` and call the .NET function with a pointer to that
        buffer and the buffer length. The buffer is reflected using CFFI's
        `from_buffer`.

        :param name: If ``func`` is not given, this is the fully qualified name
                     of the function. If ``func`` is given, this is the fully
                     qualified name of the containing class
        :param func: Name of the function
        :return:     A function object that takes a single ``binary`` parameter
                     and returns an ``int``
        """
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return f'''<Assembly {self._path} in {self._runtime}>'''



def Runtime():
    '''Runtime'''
    __doc__ = 'CLR Runtime\n\n    Encapsulates the lifetime of a CLR (.NET) runtime. If the instance is\n    deleted, the runtime will be shut down.\n    '
    info = (lambda self = None: pass)()
    
    def get_assembly(self = None, assembly_path = None):
        '''Get an assembly wrapper

        This function does not guarantee that the respective assembly is or can
        be loaded. Due to the design of the different hosting APIs, loading only
        happens when the first function is referenced, and only then potential
        errors will be raised.'''
        return Assembly(self, assembly_path)

    _get_callable = (lambda self = None, assembly_path = None, typename = abstractmethod, function = ('assembly_path', StrOrPath, 'typename', str, 'function', str, 'return', Callable[([
        Any,
        int], Any)]): pass)()
    shutdown = (lambda self = None: pass)()
    
    def __del__(self = None):
        self.shutdown()


Runtime = <NODE:27>(Runtime, 'Runtime', metaclass = ABCMeta)

def _truncate(string = dataclass, length = None):
    if length <= 1:
        raise TypeError('length must be > 1')
    if len(string) > length - 1:
        return f'''{string[:length - 1]}…'''
