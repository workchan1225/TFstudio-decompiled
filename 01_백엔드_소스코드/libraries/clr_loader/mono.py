# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mono.pyc (Python 3.11)

import atexit
import re
from pathlib import Path
from typing import Any, Dict, Optional, Sequence
from ffi import ffi, load_mono
from types import Runtime, RuntimeInfo, StrOrPath
from util import optional_path_as_string, path_as_string
__all__ = [
    'Mono']
_MONO: Any = None
_ROOT_DOMAIN: Any = None

class Mono(Runtime):
    
    def __init__(self = None, libmono = None, *, domain, debug, jit_options, config_file, global_config_file, assembly_dir, config_dir, set_signal_chaining, trace_mask, trace_level):
        self._assemblies = { }
        self._version = initialize(config_file = optional_path_as_string(config_file), debug = debug, jit_options = jit_options, global_config_file = optional_path_as_string(global_config_file), libmono = libmono, assembly_dir = assembly_dir, config_dir = config_dir, set_signal_chaining = set_signal_chaining, trace_mask = trace_mask, trace_level = trace_level)
    # WARNING: Decompyle incomplete

    
    def _get_callable(self = None, assembly_path = None, typename = None, function = ('assembly_path', StrOrPath, 'typename', str, 'function', str, 'return', 'MonoMethod')):
        assembly_path = Path(assembly_path)
        assembly = self._assemblies.get(assembly_path)
        if not assembly:
            assembly = _MONO.mono_domain_assembly_open(self._domain, path_as_string(assembly_path).encode('utf8'))
            _check_result(assembly, f'''Unable to load assembly {assembly_path}''')
            self._assemblies[assembly_path] = assembly
        image = _MONO.mono_assembly_get_image(assembly)
        _check_result(image, 'Unable to load image from assembly')
        desc = MethodDesc(typename, function)
        method = desc.search(image)
        _check_result(method, f'''Could not find method {typename}.{function} in assembly''')
        return MonoMethod(method)

    
    def info(self = None):
        return RuntimeInfo(kind = 'Mono', version = self._version, initialized = True, shutdown = _MONO is None, properties = { })

    
    def shutdown(self = None):
        pass



class MethodDesc:
    
    def __init__(self = None, typename = None, function = None):
        self._desc = f'''{typename}:{function}'''
        self._ptr = _MONO.mono_method_desc_new(self._desc.encode('utf8'), 1)

    
    def search(self = None, image = None):
        return _MONO.mono_method_desc_search_in_image(self._ptr, image)

    
    def __del__(self):
        if _MONO:
            _MONO.mono_method_desc_free(self._ptr)
            return None



class MonoMethod:
    
    def __init__(self, ptr):
        self._ptr = ptr

    
    def __call__(self, ptr, size):
        exception = ffi.new('MonoObject**')
        params = ffi.new('void*[2]')
        ptr_ptr = ffi.new('void**', ptr)
        size_ptr = ffi.new('int32_t*', size)
        params[0] = ptr_ptr
        params[1] = size_ptr
        res = _MONO.mono_runtime_invoke(self._ptr, ffi.NULL, params, exception)
        _check_result(res, 'Failed to call method')
        unboxed = ffi.cast('int32_t*', _MONO.mono_object_unbox(res))
        _check_result(unboxed, 'Failed to convert result to int')
        return unboxed[0]



def initialize(libmono, debug, jit_options, config_file, global_config_file, assembly_dir = None, config_dir = None, set_signal_chaining = None, trace_mask = (False, None, None, None, None, None, False, None, None), trace_level = ('libmono', Optional[Path], 'debug', bool, 'jit_options', Optional[Sequence[str]], 'config_file', Optional[str], 'global_config_file', Optional[str], 'assembly_dir', Optional[str], 'config_dir', Optional[str], 'set_signal_chaining', bool, 'trace_mask', Optional[str], 'trace_level', Optional[str], 'return', str)):
    pass
# WARNING: Decompyle incomplete


def _release():
    pass
# WARNING: Decompyle incomplete


def _check_result(res = None, msg = None):
    if not res == ffi.NULL or res:
        raise RuntimeError(msg)
