# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import sys
from pathlib import Path
from typing import Optional, Tuple
import cffi
from  import hostfxr, mono, netfx
__all__ = [
    'ffi',
    'load_hostfxr',
    'load_mono',
    'load_netfx']
ffi = cffi.FFI()
for cdef in hostfxr.cdef + mono.cdef + netfx.cdef:
    ffi.cdef(cdef)
    
    def load_hostfxr(dotnet_root = None):
        hostfxr_name = _get_dll_name('hostfxr')
        dotnet_root = dotnet_root.absolute()
        hostfxr_path = dotnet_root / 'host' / 'fxr'
        hostfxr_paths = hostfxr_path.glob(f'''*/{hostfxr_name}''')
        error_report = list()
        for hostfxr_path in reversed(sorted(hostfxr_paths, key = _path_to_version)):
            
            return None, ffi.dlopen(str(hostfxr_path))
            except Exception:
                error_report.append(f'''Path {hostfxr_path} gave the following error:\n{err}''')
                None = None
                del err
                continue
                err = None
                del err
            
            try:
                return ffi.dlopen(str(dotnet_root / hostfxr_name))
            except Exception:
                err = None
                error_report.append(f'''Path {hostfxr_path} gave the following error:\n{err}''')
                err = None
                del err
            except:
                err = None
                del err

            raise RuntimeError(f'''Could not find a suitable hostfxr library in {dotnet_root}. The following paths were scanned:\n\n''' + '\n\n'.join(error_report))

    
    def load_mono(path = None):
        if sys.platform == 'linux':
            ffi.dlopen('stdc++', ffi.RTLD_GLOBAL)
        path_str = str(path) if path else None
        return ffi.dlopen(path_str, ffi.RTLD_GLOBAL)

    
    def load_netfx():
        if sys.platform != 'win32':
            raise RuntimeError('.NET Framework is only supported on Windows')
        dirname = Path(__file__).parent / 'dlls'
        if sys.maxsize > 0x100000000:
            arch = 'amd64'
        else:
            arch = 'x86'
        path = dirname / arch / 'ClrLoader.dll'
        return ffi.dlopen(str(path))

    
    def _path_to_version(path = None):
        name = path.parent.name
        
        try:
            version_part = name.split('-')[0]
            res = list(map(int, version_part.split('.')))
            return tuple(res + [
                0,
                0,
                0])[:3]
        except Exception:
            return (0, 0, 0)


    
    def _get_dll_name(name = None):
        if sys.platform == 'win32':
            return f'''{name}.dll'''
        if None.platform == 'darwin':
            return f'''lib{name}.dylib'''
        return f'''{name}.so'''

    return None
