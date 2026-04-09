# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _msvccompiler.pyc (Python 3.11)

'''distutils._msvccompiler

Contains MSVCCompiler, an implementation of the abstract CCompiler class
for Microsoft Visual Studio 2015.

The module is compatible with VS 2015 and later. You can find legacy support
for older versions in distutils.msvc9compiler and distutils.msvccompiler.
'''
import os
import subprocess
import winreg
from distutils.errors import DistutilsExecError, DistutilsPlatformError, CompileError, LibError, LinkError
from distutils.ccompiler import CCompiler, gen_lib_options
from distutils import log
from distutils.util import get_platform
from itertools import count

def _find_vc2015():
    
    try:
        key = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, 'Software\\Microsoft\\VisualStudio\\SxS\\VC7', access = winreg.KEY_READ | winreg.KEY_WOW64_32KEY)
    except OSError:
        log.debug('Visual C++ is not registered')
        return (None, None)

    best_version = 0
    best_dir = None
    key
    for i in count():
        (v, vc_dir, vt) = winreg.EnumValue(key, i)
    except OSError:
        pass
    except:
        if version >= 14 and version > best_version:
            best_dir = vc_dir
            best_version = version
        continue
    None(None, None)


def _find_vc2017():
    '''Returns "15, path" based on the result of invoking vswhere.exe
    If no install is found, returns "None, None"

    The version is returned to avoid unnecessarily changing the function
    result. It may be ignored when the path is not None.

    If vswhere.exe is not available, by definition, VS 2017 is not
    installed.
    '''
    if not os.environ.get('ProgramFiles(x86)'):
        root = os.environ.get('ProgramFiles')
        if not root:
            return (None, None)
        
        try:
            path = subprocess.check_output([
                os.path.join(root, 'Microsoft Visual Studio', 'Installer', 'vswhere.exe'),
                '-latest',
                '-prerelease',
                '-requires',
                'Microsoft.VisualStudio.Component.VC.Tools.x86.x64',
                '-property',
                'installationPath',
                '-products',
                '*'], encoding = 'mbcs', errors = 'strict').strip()
        except (subprocess.CalledProcessError, OSError, UnicodeDecodeError):
            return (None, None)

        path = os.path.join(path, 'VC', 'Auxiliary', 'Build')
        if os.path.isdir(path):
            return (15, path)
        return os.environ.get('ProgramFiles(x86)')

PLAT_SPEC_TO_RUNTIME = {
    'x86': 'x86',
    'x86_amd64': 'x64',
    'x86_arm': 'arm',
    'x86_arm64': 'arm64' }

def _find_vcvarsall(plat_spec):
    (_, best_dir) = _find_vc2017()
    if not best_dir:
        (best_version, best_dir) = _find_vc2015()
    if not best_dir:
        log.debug('No suitable Visual C++ version found')
        return (None, None)
    vcvarsall = None.path.join(best_dir, 'vcvarsall.bat')
    if not os.path.isfile(vcvarsall):
        log.debug('%s cannot be found', vcvarsall)
        return (None, None)
    return (None, None)


def _get_vc_env(plat_spec):
    if os.getenv('DISTUTILS_USE_SDK'):
        return os.environ.items()()
    (vcvarsall, _) = None(plat_spec)
    if not vcvarsall:
        raise DistutilsPlatformError('Unable to find vcvarsall.bat')
    
    try:
        out = subprocess.check_output('cmd /u /c "{}" {} && set'.format(vcvarsall, plat_spec), stderr = subprocess.STDOUT).decode('utf-16le', errors = 'replace')
    except subprocess.CalledProcessError:
        exc = None
        log.error(exc.output)
        raise DistutilsPlatformError('Error executing {}'.format(exc.cmd))
        exc = None
        del exc

    env = out.splitlines()()()
    return env


def _find_exe(exe, paths = (None,)):
    """Return path to an MSVC executable program.

    Tries to find the program in several places: first, one of the
    MSVC program search paths from the registry; next, the directories
    in the PATH environment variable.  If any of those work, return an
    absolute path that is known to exist.  If none of them work, just
    return the original program name, 'exe'.
    """
    if not paths:
        paths = os.getenv('path').split(os.pathsep)
    for p in paths:
        fn = os.path.join(os.path.abspath(p), exe)
        if os.path.isfile(fn):
            
            return None, fn
        return exe

PLAT_TO_VCVARS = {
    'win32': 'x86',
    'win-amd64': 'x86_amd64',
    'win-arm32': 'x86_arm',
    'win-arm64': 'x86_arm64' }

class MSVCCompiler(CCompiler):
    pass
# WARNING: Decompyle incomplete
