# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: config.pyc (Python 3.11)

import platform
import sys
import os
import re
import shutil
import warnings
import traceback

try:
    import yaml
    _HAVE_YAML = True
except ImportError:
    _HAVE_YAML = False

from llvmlite.binding import binding as ll
IS_WIN32 = sys.platform.startswith('win32')
IS_OSX = sys.platform.startswith('darwin')
MACHINE_BITS = tuple.__itemsize__ * 8
IS_32BITS = MACHINE_BITS == 32
PYVERSION = sys.version_info[:2]
_config_fname = '.numba_config.yaml'

def _parse_cc(text):
    '''
    Parse CUDA compute capability version string.
    '''
    if not text:
        return None
    m = None.match('(\\d+)\\.(\\d+)', text)
    if not m:
        raise ValueError('Compute capability must be specified as a string of "major.minor" where major and minor are decimals')
    grp = m.groups()
    return (int(grp[0]), int(grp[1]))


def _os_supports_avx():
    '''
    Whether the current OS supports AVX, regardless of the CPU.

    This is necessary because the user may be running a very old Linux
    kernel (e.g. CentOS 5) on a recent CPU.
    '''
    if sys.platform.startswith('linux') or platform.machine() not in ('i386', 'i586', 'i686', 'x86_64'):
        return True
    
    try:
        f = open('/proc/cpuinfo', 'r')
    except OSError:
        return True

    f
    for line in f:
        (head, _, body) = line.partition(':')
        if head.strip() == 'flags' and 'avx' in body.split():
            None(None, None)
            return True
        None(None, None)
        return False
        with None:
            if not None:
                pass


class _OptLevel(int):
    pass
# WARNING: Decompyle incomplete


def _process_opt_level(opt_level):
    if opt_level not in ('0', '1', '2', '3', 'max'):
        msg = f'''Environment variable `NUMBA_OPT` is set to an unsupported value \'{opt_level}\', supported values are 0, 1, 2, 3, and \'max\''''
        raise ValueError(msg)
    return _OptLevel(opt_level)


class _EnvReloader(object):
    
    def __init__(self):
        self.reset()

    
    def reset(self):
        self.old_environ = { }
        self.update(force = True)

    
    def update(self, force = (False,)):
        new_environ = { }
        if os.path.exists(_config_fname) and os.path.isfile(_config_fname):
            if not _HAVE_YAML:
                msg = 'A Numba config file is found but YAML parsing capabilities appear to be missing. To use this feature please install `pyyaml`. e.g. `conda install pyyaml`.'
                warnings.warn(msg)
            else:
                f = open(_config_fname, 'rt')
                y_conf = yaml.safe_load(f)
                None(None, None)
        else:
            with None:
                if not None:
                    pass
    # WARNING: Decompyle incomplete

    
    def validate(self):
        global CUDA_USE_NVIDIA_BINDING
        if CUDA_USE_NVIDIA_BINDING:
            
            try:
                import cuda
            except ImportError:
                ie = None
                msg = f'''CUDA Python bindings requested (the environment variable NUMBA_CUDA_USE_NVIDIA_BINDING is set), but they are not importable: {ie.msg}.'''
                warnings.warn(msg)
                CUDA_USE_NVIDIA_BINDING = False
                ie = None
                del ie
            except:
                ie = None
                del ie

            if CUDA_PER_THREAD_DEFAULT_STREAM:
                warnings.warn('PTDS support is handled by CUDA Python when using the NVIDIA binding. Please set the environment variable CUDA_PYTHON_CUDA_PER_THREAD_DEFAULT_STREAM to 1 instead.')
                return None
            return None
            return None

    
    def process_environ(self, environ):
        pass
    # WARNING: Decompyle incomplete


_env_reloader = _EnvReloader()

def reload_config():
    '''
    Reload the configuration from environment variables, if necessary.
    '''
    _env_reloader.update()
