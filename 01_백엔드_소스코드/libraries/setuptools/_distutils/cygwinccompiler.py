# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cygwinccompiler.pyc (Python 3.11)

'''distutils.cygwinccompiler

Provides the CygwinCCompiler class, a subclass of UnixCCompiler that
handles the Cygwin port of the GNU C compiler to Windows.  It also contains
the Mingw32CCompiler class which handles the mingw32 port of GCC (same as
cygwin in no-cygwin mode).
'''
import os
import sys
import copy
import shlex
import warnings
from subprocess import check_output
from distutils.unixccompiler import UnixCCompiler
from distutils.file_util import write_file
from distutils.errors import DistutilsExecError, DistutilsPlatformError, CCompilerError, CompileError
from distutils.version import LooseVersion, suppress_known_deprecation

def get_msvcr():
    '''Include the appropriate MSVC runtime library if Python was built
    with MSVC 7.0 or later.
    '''
    msc_pos = sys.version.find('MSC v.')
    if msc_pos != -1:
        msc_ver = sys.version[msc_pos + 6:msc_pos + 10]
        if msc_ver == '1300':
            return [
                'msvcr70']
        if None == '1310':
            return [
                'msvcr71']
        if None == '1400':
            return [
                'msvcr80']
        if None == '1500':
            return [
                'msvcr90']
        if None == '1600':
            return [
                'msvcr100']
        if None == '1700':
            return [
                'msvcr110']
        if None == '1800':
            return [
                'msvcr120']
        if  <= None, int(msc_ver) or None, int(msc_ver) < 2000:
            pass
        
    else:
        return [
            'ucrt',
            'vcruntime140']
    raise None('Unknown MS Compiler version %s ' % msc_ver)

_runtime_library_dirs_msg = 'Unable to set runtime library search path on Windows, usually indicated by `runtime_library_dirs` parameter to Extension'

class CygwinCCompiler(UnixCCompiler):
    pass
# WARNING: Decompyle incomplete


class Mingw32CCompiler(CygwinCCompiler):
    pass
# WARNING: Decompyle incomplete

CONFIG_H_OK = 'ok'
CONFIG_H_NOTOK = 'not ok'
CONFIG_H_UNCERTAIN = 'uncertain'

def check_config_h():
    '''Check if the current Python installation appears amenable to building
    extensions with GCC.

    Returns a tuple (status, details), where \'status\' is one of the following
    constants:

    - CONFIG_H_OK: all is well, go ahead and compile
    - CONFIG_H_NOTOK: doesn\'t look good
    - CONFIG_H_UNCERTAIN: not sure -- unable to read pyconfig.h

    \'details\' is a human-readable string explaining the situation.

    Note there are two ways to conclude "OK": either \'sys.version\' contains
    the string "GCC" (implying that this Python was built with GCC), or the
    installed "pyconfig.h" contains the string "__GNUC__".
    '''
    sysconfig = sysconfig
    import distutils
    if 'GCC' in sys.version:
        return (CONFIG_H_OK, "sys.version mentions 'GCC'")
    if None in sys.version:
        return (CONFIG_H_OK, "sys.version mentions 'Clang'")
    fn = None.get_config_h_filename()
    
    try:
        config_h = open(fn)
        
        try:
            if '__GNUC__' in config_h.read():
                
                try:
                    config_h.close()
                    return (CONFIG_H_OK, "'%s' mentions '__GNUC__'" % fn)
                    
                    try:
                        
                        try:
                            config_h.close()
                            return (CONFIG_H_NOTOK, "'%s' does not mention '__GNUC__'" % fn)
                            config_h.close()
                            
                            try:
                                pass
                            except OSError:
                                exc = None
                                del exc
                                return None
                                None = 
                                del exc








def is_cygwincc(cc):
    '''Try to determine if the compiler that would be used is from cygwin.'''
    out_string = check_output(shlex.split(cc) + [
        '-dumpmachine'])
    return out_string.strip().endswith(b'cygwin')

get_versions = None
