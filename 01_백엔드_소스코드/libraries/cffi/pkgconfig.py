# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pkgconfig.pyc (Python 3.11)

import sys
import os
import subprocess
from error import PkgConfigError

def merge_flags(cfg1, cfg2):
    '''Merge values from cffi config flags cfg2 to cf1

    Example:
        merge_flags({"libraries": ["one"]}, {"libraries": ["two"]})
        {"libraries": ["one", "two"]}
    '''
    for key, value in cfg2.items():
        if key not in cfg1:
            cfg1[key] = value
            continue
        if not isinstance(cfg1[key], list):
            raise TypeError(f'''cfg1[{key!r}] should be a list of strings''')
        if not isinstance(value, list):
            raise TypeError(f'''cfg2[{key!r}] should be a list of strings''')
        cfg1[key].extend(value)
        return cfg1


def call(libname, flag, encoding = (sys.getfilesystemencoding(),)):
    '''Calls pkg-config and returns the output if found
    '''
    a = [
        'pkg-config',
        '--print-errors']
    a.append(flag)
    a.append(libname)
    
    try:
        pc = subprocess.Popen(a, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    except EnvironmentError:
        e = None
        raise PkgConfigError(f'''cannot run pkg-config: {str(e).strip()!s}''')
        e = None
        del e

    (bout, berr) = pc.communicate()
    if pc.returncode != 0:
        
        try:
            berr = berr.decode(encoding)
        except Exception:
            pass

        raise PkgConfigError(berr.strip())
    if not sys.version_info >= (3,) and isinstance(bout, str):
        
        try:
            bout = bout.decode(encoding)
        except UnicodeDecodeError:
            raise PkgConfigError(f'''pkg-config {flag!s} {libname!s} returned bytes that cannot be decoded with encoding {encoding!r}:\n{bout!r}''')

        if os.altsep != '\\' and '\\' in bout:
            raise PkgConfigError(f'''pkg-config {flag!s} {libname!s} returned an unsupported backslash-escaped output:\n{bout!r}''')
        return bout


def flags_from_pkgconfig(libs):
    '''Return compiler line flags for FFI.set_source based on pkg-config output

    Usage
        ...
        ffibuilder.set_source("_foo", pkgconfig = ["libfoo", "libbar >= 1.8.3"])

    If pkg-config is installed on build machine, then arguments include_dirs,
    library_dirs, libraries, define_macros, extra_compile_args and
    extra_link_args are extended with an output of pkg-config for libfoo and
    libbar.

    Raises PkgConfigError in case the pkg-config call fails.
    '''
    pass
# WARNING: Decompyle incomplete
