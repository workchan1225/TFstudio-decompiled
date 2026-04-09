# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Python.NET runtime loading and configuration'''
import sys
from pathlib import Path
from typing import Dict, Optional, Union, Any
import clr_loader
__all__ = [
    'set_runtime',
    'set_runtime_from_env',
    'load',
    'unload',
    'get_runtime_info']
_RUNTIME: Optional[clr_loader.Runtime] = None
_LOADER_ASSEMBLY: Optional[clr_loader.Assembly] = None
_LOADED: bool = False

def set_runtime(runtime = None, **params):
    '''Set up a clr_loader runtime without loading it

    :param runtime:
        Either an already initialised `clr_loader` runtime, or one of netfx,
        coreclr, mono, or default. If a string parameter is given, the runtime
        will be created.
    '''
    global _RUNTIME
    if _LOADED:
        raise RuntimeError(f'''The runtime {_RUNTIME} has already been loaded''')
    if isinstance(runtime, str):
        runtime = _create_runtime_from_spec(runtime, params)
    _RUNTIME = runtime


def get_runtime_info():
    '''Retrieve information on the configured runtime'''
    pass
# WARNING: Decompyle incomplete


def _get_params_from_env(prefix = None):
    pass
# WARNING: Decompyle incomplete


def _create_runtime_from_spec(spec = None, params = None):
    was_default = False
    if spec == 'default':
        was_default = True
        if sys.platform == 'win32':
            spec = 'netfx'
        else:
            spec = 'mono'
# WARNING: Decompyle incomplete


def set_runtime_from_env():
    '''Set up the runtime using the environment

    This will use the environment variable PYTHONNET_RUNTIME to decide the
    runtime to use, which may be one of netfx, coreclr or mono. The parameters
    of the respective clr_loader.get_<runtime> functions can also be given as
    environment variables, named `PYTHONNET_<RUNTIME>_<PARAM_NAME>`. In
    particular, to use `PYTHONNET_RUNTIME=coreclr`, the variable
    `PYTHONNET_CORECLR_RUNTIME_CONFIG` has to be set to a valid
    `.runtimeconfig.json`.

    If no environment variable is specified, a globally installed Mono is used
    for all environments but Windows, on Windows the legacy .NET Framework is
    used.
    '''
    environ = environ
    import os
    spec = environ.get('PYTHONNET_RUNTIME', 'default')
    runtime = _create_runtime_from_spec(spec)
    set_runtime(runtime)


def load(runtime = None, **params):
    '''Load Python.NET in the specified runtime

    The same parameters as for `set_runtime` can be used. By default,
    `set_default_runtime` is called if no environment has been set yet and no
    parameters are passed.

    After a successful call, further invocations will return immediately.'''
    if _LOADED:
        return None
# WARNING: Decompyle incomplete


def unload():
    '''Explicitly unload a loaded runtime and shut down Python.NET'''
    pass
# WARNING: Decompyle incomplete
