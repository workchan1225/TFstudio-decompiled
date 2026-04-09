# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hostfxr.pyc (Python 3.11)

import sys
from pathlib import Path
from typing import Generator, Tuple, Optional
from ffi import ffi, load_hostfxr
from types import Runtime, RuntimeInfo, StrOrPath
from util import check_result
__all__ = [
    'DotnetCoreRuntime']
_IS_SHUTDOWN = False

class DotnetCoreRuntime(Runtime):
    _version: str = 'DotnetCoreRuntime'
    
    def __init__(self = None, *, dotnet_root, runtime_config, entry_dll, **params):
        self._handle = None
        if _IS_SHUTDOWN:
            raise RuntimeError('Runtime can not be reinitialized')
        self._dotnet_root = Path(dotnet_root)
        self._dll = load_hostfxr(self._dotnet_root)
        self._load_func = None
    # WARNING: Decompyle incomplete

    dotnet_root = (lambda self = None: self._dotnet_root)()
    is_initialized = (lambda self = None: self._load_func is not None)()
    is_shutdown = (lambda self = None: _IS_SHUTDOWN)()
    
    def __getitem__(self = None, key = None):
        if self.is_shutdown:
            raise RuntimeError('Runtime is shut down')
        buf = ffi.new('char_t**')
        res = self._dll.hostfxr_get_runtime_property_value(self._handle, encode(key), buf)
        if res != 0:
            raise KeyError(key)
        return decode(buf[0])

    
    def __setitem__(self = None, key = None, value = None):
        if self.is_initialized:
            raise RuntimeError('Already initialized')
        res = self._dll.hostfxr_set_runtime_property_value(self._handle, encode(key), encode(value))
        check_result(res)

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_load_func(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_callable(self = None, assembly_path = None, typename = None, function = ('assembly_path', StrOrPath, 'typename', str, 'function', str)):
        assembly_path = Path(assembly_path)
        assembly_name = assembly_path.stem
        typename = f'''{typename}, {assembly_name}'''
        delegate_ptr = ffi.new('void**')
        res = self._get_load_func()(encode(str(assembly_path)), encode(typename), encode(function), ffi.NULL, ffi.NULL, delegate_ptr)
        check_result(res)
        return ffi.cast('component_entry_point_fn', delegate_ptr[0])

    
    def shutdown(self = None):
        if self._handle or self._dll:
            self._dll.hostfxr_close(self._handle)
            self._handle = None
            return None
        return None

    
    def info(self):
        return RuntimeInfo(kind = 'CoreCLR', version = self._version, initialized = self._handle is not None, shutdown = self._handle is None, properties = dict(self) if not _IS_SHUTDOWN else { })



def _get_handle_for_runtime_config(dll = None, dotnet_root = None, runtime_config = None):
    params = ffi.new('hostfxr_initialize_parameters*')
    params.size = ffi.sizeof('hostfxr_initialize_parameters')
    params.host_path = ffi.NULL
    dotnet_root_p = ffi.new('char_t[]', encode(str(Path(dotnet_root))))
    params.dotnet_root = dotnet_root_p
    handle_ptr = ffi.new('hostfxr_handle*')
    res = dll.hostfxr_initialize_for_runtime_config(encode(str(Path(runtime_config))), params, handle_ptr)
    check_result(res)
    return handle_ptr[0]


def _get_handle_for_dotnet_command_line(dll = None, dotnet_root = None, entry_dll = None):
    params = ffi.new('hostfxr_initialize_parameters*')
    params.size = ffi.sizeof('hostfxr_initialize_parameters')
    params.host_path = ffi.NULL
    dotnet_root_p = ffi.new('char_t[]', encode(str(Path(dotnet_root))))
    params.dotnet_root = dotnet_root_p
    handle_ptr = ffi.new('hostfxr_handle*')
    args_ptr = ffi.new('char_t*[1]')
    arg_ptr = ffi.new('char_t[]', encode(str(Path(entry_dll))))
    args_ptr[0] = arg_ptr
    res = dll.hostfxr_initialize_for_dotnet_command_line(1, args_ptr, params, handle_ptr)
    check_result(res)
    return handle_ptr[0]


def _get_load_func(dll, handle):
    delegate_ptr = ffi.new('void**')
    res = dll.hostfxr_get_runtime_delegate(handle, dll.hdt_load_assembly_and_get_function_pointer, delegate_ptr)
    check_result(res)
    return ffi.cast('load_assembly_and_get_function_pointer_fn', delegate_ptr[0])

if sys.platform == 'win32':
    
    def encode(string = None):
        return string

    
    def decode(char_ptr = None):
        return ffi.string(char_ptr)

    return None

def encode(string = None):
    return string.encode('utf8')


def decode(char_ptr = None):
    return ffi.string(char_ptr).decode('utf8')
