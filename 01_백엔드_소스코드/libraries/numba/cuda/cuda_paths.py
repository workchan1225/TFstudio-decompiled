# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cuda_paths.pyc (Python 3.11)

import sys
import re
import os
from collections import namedtuple
from numba.core.config import IS_WIN32
from numba.misc.findlib import find_lib, find_file
_env_path_tuple = namedtuple('_env_path_tuple', [
    'by',
    'info'])

def _find_valid_path(options):
    """Find valid path from *options*, which is a list of 2-tuple of
    (name, path).  Return first pair where *path* is not None.
    If no valid path is found, return ('<unknown>', None)
    """
    pass
# WARNING: Decompyle incomplete


def _get_libdevice_path_decision():
    options = [
        ('Conda environment', get_conda_ctk()),
        ('Conda environment (NVIDIA package)', get_nvidia_libdevice_ctk()),
        ('CUDA_HOME', get_cuda_home('nvvm', 'libdevice')),
        ('System', get_system_ctk('nvvm', 'libdevice')),
        ('Debian package', get_debian_pkg_libdevice())]
    (by, libdir) = _find_valid_path(options)
    return (by, libdir)


def _nvvm_lib_dir():
    if IS_WIN32:
        return ('nvvm', 'bin')


def _get_nvvm_path_decision():
    pass
# WARNING: Decompyle incomplete


def _get_libdevice_paths():
    (by, libdir) = _get_libdevice_path_decision()
    pat = 'libdevice(\\.\\d+)*\\.bc$'
    candidates = find_file(re.compile(pat), libdir)
    out = max(candidates, default = None)
    return _env_path_tuple(by, out)


def _cudalib_path():
    if IS_WIN32:
        return 'bin'


def _cuda_home_static_cudalib_path():
    if IS_WIN32:
        return ('lib', 'x64')


def _get_cudalib_dir_path_decision():
    options = [
        ('Conda environment', get_conda_ctk()),
        ('Conda environment (NVIDIA package)', get_nvidia_cudalib_ctk()),
        ('CUDA_HOME', get_cuda_home(_cudalib_path())),
        ('System', get_system_ctk(_cudalib_path()))]
    (by, libdir) = _find_valid_path(options)
    return (by, libdir)


def _get_static_cudalib_dir_path_decision():
    pass
# WARNING: Decompyle incomplete


def _get_cudalib_dir():
    (by, libdir) = _get_cudalib_dir_path_decision()
    return _env_path_tuple(by, libdir)


def _get_static_cudalib_dir():
    (by, libdir) = _get_static_cudalib_dir_path_decision()
    return _env_path_tuple(by, libdir)


def get_system_ctk(*subdirs):
    """Return path to system-wide cudatoolkit; or, None if it doesn't exist.
    """
    pass
# WARNING: Decompyle incomplete


def get_conda_ctk():
    '''Return path to directory containing the shared libraries of cudatoolkit.
    '''
    is_conda_env = os.path.exists(os.path.join(sys.prefix, 'conda-meta'))
    if not is_conda_env:
        return None
    paths = None('nvvm')
    if not paths:
        return None
    return None.path.dirname(max(paths))


def get_nvidia_nvvm_ctk():
