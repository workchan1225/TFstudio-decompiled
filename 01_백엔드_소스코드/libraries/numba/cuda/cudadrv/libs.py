# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: libs.pyc (Python 3.11)

'''CUDA Toolkit libraries lookup utilities.

CUDA Toolkit libraries can be available via either:

- the `cuda-nvcc` and `cuda-nvrtc` conda packages for CUDA 12,
- the `cudatoolkit` conda package for CUDA 11,
- a user supplied location from CUDA_HOME,
- a system wide location,
- package-specific locations (e.g. the Debian NVIDIA packages),
- or can be discovered by the system loader.
'''
import os
import sys
import ctypes
from numba.misc.findlib import find_lib
from numba.cuda.cuda_paths import get_cuda_paths
from numba.cuda.cudadrv.driver import locate_driver_and_loader, load_driver
from numba.cuda.cudadrv.error import CudaSupportError
if sys.platform == 'win32':
    _dllnamepattern = '%s.dll'
    _staticnamepattern = '%s.lib'
elif sys.platform == 'darwin':
    _dllnamepattern = 'lib%s.dylib'
    _staticnamepattern = 'lib%s.a'
else:
    _dllnamepattern = 'lib%s.so'
    _staticnamepattern = 'lib%s.a'

def get_libdevice():
    d = get_cuda_paths()
    paths = d['libdevice'].info
    return paths


def open_libdevice():
    bcfile = open(get_libdevice(), 'rb')
    None(None, None)
    return 
    with None:
        if not None, bcfile.read():
            pass


def get_cudalib(lib, static = (False,)):
    """
    Find the path of a CUDA library based on a search of known locations. If
    the search fails, return a generic filename for the library (e.g.
    'libnvvm.so' for 'nvvm') so that we may attempt to load it using the system
    loader's search mechanism.
    """
    if lib == 'nvvm':
        if not get_cuda_paths()['nvvm'].info:
            return _dllnamepattern % 'nvvm'
    dir_type = 'static_cudalib_dir' if get_cuda_paths()['nvvm'].info else 'cudalib_dir'
    libdir = get_cuda_paths()[dir_type].info
    candidates = find_lib(lib, libdir, static = static)
    namepattern = _staticnamepattern if static else _dllnamepattern
    return max(candidates) if candidates else namepattern % lib


def open_cudalib(lib):
    path = get_cudalib(lib)
    return ctypes.CDLL(path)


def check_static_lib(path):
    if not os.path.isfile(path):
        raise FileNotFoundError(f'''{path} not found''')


def _get_source_variable(lib, static = (False,)):
    if lib == 'nvvm':
        return get_cuda_paths()['nvvm'].by
    if None == 'libdevice':
        return get_cuda_paths()['libdevice'].by
    dir_type = 'static_cudalib_dir' if None else 'cudalib_dir'
    return get_cuda_paths()[dir_type].by


def test():
    '''Test library lookup.  Path info is printed to stdout.
    '''
    failed = False
    
    try:
        (dlloader, candidates) = locate_driver_and_loader()
        print('Finding driver from candidates:')
        for location in candidates:
            print(f'''\t{location}''')
            print(f'''Using loader {dlloader}''')
            print('\tTrying to load driver', end = '...')
            (dll, path) = load_driver(dlloader, candidates)
            print('\tok')
            print(f'''\t\tLoaded from {path}''')
    except CudaSupportError:
        e = None
        print(f'''\tERROR: failed to open driver: {e}''')
        failed = True
        e = None
        del e
    except:
        e = None
        del e

    if not sys.platform == 'linux' and failed:
        pid = os.getpid()
        mapsfile = os.path.join(os.path.sep, 'proc', f'''{pid}''', 'maps')
        
        try:
            f = open(mapsfile)
            maps = f.read()
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            locations = (lambda .0: pass# WARNING: Decompyle incomplete
)(maps.split()())
                            print('\tMapped libcuda.so paths:')
                            for location in locations:
                                print(f'''\t\t{location}''')
                        except OSError:
                            print(f'''\tERROR: Could not open {mapsfile} to determine absolute path to libcuda.so''')

                        libs = 'nvvm nvrtc cudart'.split()
                        for lib in libs:
                            path = get_cudalib(lib)
                            print('Finding {} from {}'.format(lib, _get_source_variable(lib)))
                            print('\tLocated at', path)
                            print('\tTrying to open library', end = '...')
                            open_cudalib(lib)
                            print('\tok')
                            except OSError:
                                e = None
                                print(f'''\tERROR: failed to open {lib!s}:\n{e!s}''')
                                failed = True
                                e = None
                                del e
                                continue
                                e = None
                                del e
                            lib = 'cudadevrt'
                            path = get_cudalib(lib, static = True)
                            print('Finding {} from {}'.format(lib, _get_source_variable(lib, static = True)))
                            print('\tLocated at', path)
                            
                            try:
                                print('\tChecking library', end = '...')
                                check_static_lib(path)
                                print('\tok')
                            except FileNotFoundError:
                                e = None
                                print(f'''\tERROR: failed to find {lib!s}:\n{e!s}''')
                                failed = True
                                e = None
                                del e
                            except:
                                e = None
                                del e

                            where = _get_source_variable('libdevice')
                            print(f'''Finding libdevice from {where}''')
                            path = get_libdevice()
                            print('\tLocated at', path)
                            
                            try:
                                print('\tChecking library', end = '...')
                                check_static_lib(path)
                                print('\tok')
                            except FileNotFoundError:
                                e = None
                                print(f'''\tERROR: failed to find {lib!s}:\n{e!s}''')
                                failed = True
                                e = None
                                del e
                            except:
                                e = None
                                del e

                            return not failed
