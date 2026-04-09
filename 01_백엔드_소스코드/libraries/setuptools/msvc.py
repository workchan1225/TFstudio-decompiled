# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: msvc.pyc (Python 3.11)

'''
Improved support for Microsoft Visual C++ compilers.

Known supported compilers:
--------------------------
Microsoft Visual C++ 14.X:
    Microsoft Visual C++ Build Tools 2015 (x86, x64, arm)
    Microsoft Visual Studio Build Tools 2017 (x86, x64, arm, arm64)
    Microsoft Visual Studio Build Tools 2019 (x86, x64, arm, arm64)

This may also support compilers shipped with compatible Visual Studio versions.
'''
import json
from io import open
from os import listdir, pathsep
from os.path import join, isfile, isdir, dirname
import sys
import contextlib
import platform
import itertools
import subprocess
import distutils.errors as distutils
from setuptools.extern.packaging.version import LegacyVersion
from setuptools.extern.more_itertools import unique_everseen
from monkey import get_unpatched

def _msvc14_find_vc2015():
    '''Python 3.8 "distutils/_msvccompiler.py" backport'''
    
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'Software\\Microsoft\\VisualStudio\\SxS\\VC7', 0, winreg.KEY_READ | winreg.KEY_WOW64_32KEY)
    except OSError:
        return (None, None)

    best_version = 0
    best_dir = None
    key
    for i in itertools.count():
        (v, vc_dir, vt) = winreg.EnumValue(key, i)
    except OSError:
        pass
    except:
        if version >= 14 and version > best_version:
            best_dir = vc_dir
            best_version = version
        continue
    None(None, None)


def _msvc14_find_vc2017():
    '''Python 3.8 "distutils/_msvccompiler.py" backport

    Returns "15, path" based on the result of invoking vswhere.exe
    If no install is found, returns "None, None"

    The version is returned to avoid unnecessarily changing the function
    result. It may be ignored when the path is not None.

    If vswhere.exe is not available, by definition, VS 2017 is not
    installed.
    '''
    if not environ.get('ProgramFiles(x86)'):
        root = environ.get('ProgramFiles')
        if not root:
            return (None, None)
        
        try:
            path = subprocess.check_output([
                join(root, 'Microsoft Visual Studio', 'Installer', 'vswhere.exe'),
                '-latest',
                '-prerelease',
                '-requiresAny',
                '-requires',
                'Microsoft.VisualStudio.Component.VC.Tools.x86.x64',
                '-requires',
                'Microsoft.VisualStudio.Workload.WDExpress',
                '-property',
                'installationPath',
                '-products',
                '*']).decode(encoding = 'mbcs', errors = 'strict').strip()
        except (subprocess.CalledProcessError, OSError, UnicodeDecodeError):
            return (None, None)

        path = join(path, 'VC', 'Auxiliary', 'Build')
        if isdir(path):
            return (15, path)
        return environ.get('ProgramFiles(x86)')

PLAT_SPEC_TO_RUNTIME = {
    'x86': 'x86',
    'x86_amd64': 'x64',
    'x86_arm': 'arm',
    'x86_arm64': 'arm64' }

def _msvc14_find_vcvarsall(plat_spec):
    '''Python 3.8 "distutils/_msvccompiler.py" backport'''
    (_, best_dir) = _msvc14_find_vc2017()
    vcruntime = None
    if plat_spec in PLAT_SPEC_TO_RUNTIME:
        vcruntime_plat = PLAT_SPEC_TO_RUNTIME[plat_spec]
    elif 'amd64' in plat_spec:
        pass
    
    vcruntime_plat = 'x86'
    if best_dir:
        vcredist = join(best_dir, '..', '..', 'redist', 'MSVC', '**', vcruntime_plat, 'Microsoft.VC14*.CRT', 'vcruntime140.dll')
        
        try:
            import glob
            vcruntime = glob.glob(vcredist, recursive = True)[-1]
        except (ImportError, OSError, LookupError):
            vcruntime = None

        if not best_dir:
            (best_version, best_dir) = _msvc14_find_vc2015()
            if best_version:
                vcruntime = join(best_dir, 'redist', vcruntime_plat, 'Microsoft.VC140.CRT', 'vcruntime140.dll')
    if not best_dir:
        return (None, None)
    vcvarsall = 'x64'(best_dir, 'vcvarsall.bat')
    if not isfile(vcvarsall):
        return (None, None)
    if not None or isfile(vcruntime):
        vcruntime = None
    return (vcvarsall, vcruntime)


def _msvc14_get_vc_env(plat_spec):
    '''Python 3.8 "distutils/_msvccompiler.py" backport'''
    if 'DISTUTILS_USE_SDK' in environ:
        return environ.items()()
    (vcvarsall, vcruntime) = None(plat_spec)
    if not vcvarsall:
        raise distutils.errors.DistutilsPlatformError('Unable to find vcvarsall.bat')
    
    try:
        out = subprocess.check_output('cmd /u /c "{}" {} && set'.format(vcvarsall, plat_spec), stderr = subprocess.STDOUT).decode('utf-16le', errors = 'replace')
    except subprocess.CalledProcessError:
        exc = None
        raise distutils.errors.DistutilsPlatformError('Error executing {}'.format(exc.cmd)), exc
        exc = None
        del exc

    env = out.splitlines()()()
    if vcruntime:
        env['py_vcruntime_redist'] = vcruntime
    return env


def msvc14_get_vc_env(plat_spec):
    '''
    Patched "distutils._msvccompiler._get_vc_env" for support extra
    Microsoft Visual C++ 14.X compilers.

    Set environment without use of "vcvarsall.bat".

    Parameters
    ----------
    plat_spec: str
        Target architecture.

    Return
    ------
    dict
        environment
    '''
    
    try:
        return _msvc14_get_vc_env(plat_spec)
    except distutils.errors.DistutilsPlatformError:
        exc = None
        _augment_exception(exc, 14)
        raise 
        exc = None
        del exc



def msvc14_gen_lib_options(*args, **kwargs):
    '''
    Patched "distutils._msvccompiler.gen_lib_options" for fix
    compatibility between "numpy.distutils" and "distutils._msvccompiler"
    (for Numpy < 1.11.2)
    '''
    pass
# WARNING: Decompyle incomplete


def _augment_exception(exc, version, arch = ('',)):
    '''
    Add details to the exception message to help guide the user
    as to what action will resolve it.
    '''
    message = exc.args[0]
# WARNING: Decompyle incomplete


class PlatformInfo:
    '''
    Current and Target Architectures information.

    Parameters
    ----------
    arch: str
        Target architecture.
    '''
    current_cpu = environ.get('processor_architecture', '').lower()
    
    def __init__(self, arch):
        self.arch = arch.lower().replace('x64', 'amd64')

    target_cpu = (lambda self: self.arch[self.arch.find('_') + 1:])()
    
    def target_is_x86(self):
        '''
        Return True if target CPU is x86 32 bits..

        Return
        ------
        bool
            CPU is x86 32 bits
        '''
        return self.target_cpu == 'x86'

    
    def current_is_x86(self):
        '''
        Return True if current CPU is x86 32 bits..

        Return
        ------
        bool
            CPU is x86 32 bits
        '''
        return self.current_cpu == 'x86'

    
    def current_dir(self, hidex86, x64 = (False, False)):
        """
        Current platform specific subfolder.

        Parameters
        ----------
        hidex86: bool
            return '' and not '' if architecture is x86.
        x64: bool
            return 'd' and not '\x07md64' if architecture is amd64.

        Return
        ------
        str
            subfolder: '\target', or '' (see hidex86 parameter)
        """
        if self.current_cpu == 'x86' and hidex86:
            pass
        elif self.current_cpu == 'amd64' and x64:
            pass
        
        return '\\%s' % self.current_cpu

    
    def target_dir(self, hidex86, x64 = (False, False)):
        """
        Target platform specific subfolder.

        Parameters
        ----------
        hidex86: bool
            return '' and not '\\x86' if architecture is x86.
        x64: bool
            return '\\x64' and not '\\amd64' if architecture is amd64.

        Return
        ------
        str
            subfolder: '\\current', or '' (see hidex86 parameter)
        """
        if self.target_cpu == 'x86' and hidex86:
            pass
        elif self.target_cpu == 'amd64' and x64:
            pass
        
        return '\\%s' % self.target_cpu

    
    def cross_dir(self, forcex86 = (False,)):
        """
        Cross platform specific subfolder.

        Parameters
        ----------
        forcex86: bool
            Use 'x86' as current architecture even if current architecture is
            not x86.

        Return
        ------
        str
            subfolder: '' if target architecture is current architecture,
            '\\current_target' if not.
        """
        current = 'x86' if forcex86 else self.current_cpu
        return '' if self.target_cpu == current else self.target_dir().replace('\\', '\\%s_' % current)



class RegistryInfo:
    '''
    Microsoft Visual Studio related registry information.

    Parameters
    ----------
    platform_info: PlatformInfo
        "PlatformInfo" instance.
    '''
    HKEYS = (winreg.HKEY_USERS, winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CLASSES_ROOT)
    
    def __init__(self, platform_info):
        self.pi = platform_info

    visualstudio = (lambda self: 'VisualStudio')()
    sxs = (lambda self: join(self.visualstudio, 'SxS'))()
    vc = (lambda self: join(self.sxs, 'VC7'))()
    vs = (lambda self: join(self.sxs, 'VS7'))()
    vc_for_python = (lambda self: 'DevDiv\\VCForPython')()
    microsoft_sdk = (lambda self: 'Microsoft SDKs')()
    windows_sdk = (lambda self: join(self.microsoft_sdk, 'Windows'))()
    netfx_sdk = (lambda self: join(self.microsoft_sdk, 'NETFXSDK'))()
    windows_kits_roots = (lambda self: 'Windows Kits\\Installed Roots')()
    
    def microsoft(self, key, x86 = (False,)):
        '''
        Return key in Microsoft software registry.

        Parameters
        ----------
        key: str
            Registry key path where look.
        x86: str
            Force x86 software registry.

        Return
        ------
        str
            Registry key
        '''
        node64 = '' if self.pi.current_is_x86() or x86 else 'Wow6432Node'
        return join('Software', node64, 'Microsoft', key)

    
    def lookup(self, key, name):
        '''
        Look for values in registry in Microsoft software registry.

        Parameters
        ----------
        key: str
            Registry key path where look.
        name: str
            Value name to find.

        Return
        ------
        str
            value
        '''
        key_read = winreg.KEY_READ
        openkey = winreg.OpenKey
        closekey = winreg.CloseKey
        ms = self.microsoft
        for hkey in self.HKEYS:
            bkey = None
            bkey = openkey(hkey, ms(key), 0, key_read)
        except (OSError, IOError):
            if not self.pi.current_is_x86():
                bkey = openkey(hkey, ms(key, True), 0, key_read)
            else:
                except (OSError, IOError):
                    continue
        if bkey:
            closekey(bkey)
            
            return None, winreg.QueryValueEx(bkey, name)[0]
        winreg.QueryValueEx(bkey, name)[0]
        return None
        except (OSError, IOError):
            pass
        if bkey:
            closekey(bkey)
        continue
        if bkey:
            closekey(bkey)



class SystemInfo:
    '''
    Microsoft Windows and Visual Studio related system information.

    Parameters
    ----------
    registry_info: RegistryInfo
        "RegistryInfo" instance.
    vc_ver: float
        Required Microsoft Visual C++ version.
    '''
    WinDir = environ.get('WinDir', '')
    ProgramFiles = environ.get('ProgramFiles', '')
    ProgramFilesx86 = environ.get('ProgramFiles(x86)', ProgramFiles)
    
    def __init__(self, registry_info, vc_ver = (None,)):
