# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: msvc9compiler.pyc (Python 3.11)

'''distutils.msvc9compiler

Contains MSVCCompiler, an implementation of the abstract CCompiler class
for the Microsoft Visual Studio 2008.

The module is compatible with VS 2005 and VS 2008. You can find legacy support
for older versions of VS in distutils.msvccompiler.
'''
import os
import subprocess
import sys
import re
import warnings
from distutils.errors import DistutilsExecError, DistutilsPlatformError, CompileError, LibError, LinkError
from distutils.ccompiler import CCompiler, gen_lib_options
from distutils import log
from distutils.util import get_platform
import winreg
warnings.warn('msvc9compiler is deprecated and slated to be removed in the future. Please discontinue use or file an issue with pypa/distutils describing your use case.', DeprecationWarning)
RegOpenKeyEx = winreg.OpenKeyEx
RegEnumKey = winreg.EnumKey
RegEnumValue = winreg.EnumValue
RegError = winreg.error
HKEYS = (winreg.HKEY_USERS, winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CLASSES_ROOT)
if sys.platform == 'win32':
    NATIVE_WIN64 = sys.maxsize > 0x100000000
    if NATIVE_WIN64:
        VS_BASE = 'Software\\Wow6432Node\\Microsoft\\VisualStudio\\%0.1f'
        WINSDK_BASE = 'Software\\Wow6432Node\\Microsoft\\Microsoft SDKs\\Windows'
        NET_BASE = 'Software\\Wow6432Node\\Microsoft\\.NETFramework'
    else:
        VS_BASE = 'Software\\Microsoft\\VisualStudio\\%0.1f'
        WINSDK_BASE = 'Software\\Microsoft\\Microsoft SDKs\\Windows'
        NET_BASE = 'Software\\Microsoft\\.NETFramework'
PLAT_TO_VCVARS = {
    'win32': 'x86',
    'win-amd64': 'amd64' }

class Reg:
    '''Helper class to read values from the registry'''
    
    def get_value(cls, path, key):
        for base in HKEYS:
            d = cls.read_values(base, path)
            if d and key in d:
                
                return None, d[key]
            raise KeyError(key)

    get_value = classmethod(get_value)
    
    def read_keys(cls, base, key):
        '''Return list of registry keys.'''
        
        try:
            handle = RegOpenKeyEx(base, key)
        except RegError:
            return None

        L = []
        i = 0
        
        try:
            k = RegEnumKey(handle, i)
        except RegError:
            pass
        except:
            L.append(k)
            i += 1
            continue

        return L

    read_keys = classmethod(read_keys)
    
    def read_values(cls, base, key):
        '''Return dict of registry keys and values.

        All names are converted to lowercase.
        '''
        
        try:
            handle = RegOpenKeyEx(base, key)
        except RegError:
            return None

        d = { }
        i = 0
        
        try:
            (name, value, type) = RegEnumValue(handle, i)
        except RegError:
            pass
        except:
            name = name.lower()
            d[cls.convert_mbcs(name)] = cls.convert_mbcs(value)
            i += 1
            continue

        return d

    read_values = classmethod(read_values)
    
    def convert_mbcs(s):
        dec = getattr(s, 'decode', None)
    # WARNING: Decompyle incomplete

    convert_mbcs = staticmethod(convert_mbcs)


class MacroExpander:
    
    def __init__(self, version):
        self.macros = { }
        self.vsbase = VS_BASE % version
        self.load_macros(version)

    
    def set_macro(self, macro, path, key):
        self.macros['$(%s)' % macro] = Reg.get_value(path, key)

    
    def load_macros(self, version):
        self.set_macro('VCInstallDir', self.vsbase + '\\Setup\\VC', 'productdir')
        self.set_macro('VSInstallDir', self.vsbase + '\\Setup\\VS', 'productdir')
        self.set_macro('FrameworkDir', NET_BASE, 'installroot')
        
        try:
            if version >= 8:
                self.set_macro('FrameworkSDKDir', NET_BASE, 'sdkinstallrootv2.0')
            else:
                raise KeyError('sdkinstallrootv2.0')
        except KeyError:
            raise DistutilsPlatformError('Python was built with Visual Studio 2008;\nextensions must be built with a compiler than can generate compatible binaries.\nVisual Studio 2008 was not found on this system. If you have Cygwin installed,\nyou can try compiling with MingW32, by passing "-c mingw32" to setup.py.')

        if version >= 9:
            self.set_macro('FrameworkVersion', self.vsbase, 'clr version')
            self.set_macro('WindowsSdkDir', WINSDK_BASE, 'currentinstallfolder')
            return None
        p = None
        for base in HKEYS:
            h = RegOpenKeyEx(base, p)
        except RegError:
            continue
        key = RegEnumKey(h, 0)
        d = Reg.get_value(base, '{}\\{}'.format(p, key))
        self.macros['$(FrameworkVersion)'] = d['version']
        continue

    
    def sub(self, s):
        for k, v in self.macros.items():
            s = s.replace(k, v)
            return s



def get_build_version():
    '''Return the version of MSVC that was used to build Python.

    For Python 2.3 and up, the version number is included in
    sys.version.  For earlier versions, assume the compiler is MSVC 6.
    '''
    prefix = 'MSC v.'
    i = sys.version.find(prefix)
    if i == -1:
        return 6
    i = None + len(prefix)
    (s, rest) = sys.version[i:].split(' ', 1)
    majorVersion = int(s[:-2]) - 6
    if majorVersion >= 13:
        majorVersion += 1
    minorVersion = int(s[2:3]) / 10
    if majorVersion == 6:
        minorVersion = 0
    if majorVersion >= 6:
        return majorVersion + minorVersion


def normalize_and_reduce_paths(paths):
    '''Return a list of normalized paths with duplicates removed.

    The current order of paths is maintained.
    '''
    reduced_paths = []
    for p in paths:
        np = os.path.normpath(p)
        if np not in reduced_paths:
            reduced_paths.append(np)
        return reduced_paths


def removeDuplicates(variable):
    '''Remove duplicate values of an environment variable.'''
    oldList = variable.split(os.pathsep)
    newList = []
    for i in oldList:
        if i not in newList:
            newList.append(i)
        newVariable = os.pathsep.join(newList)
        return newVariable


def find_vcvarsall(version):
    '''Find the vcvarsall.bat file

    At first it tries to find the productdir of VS 2008 in the registry. If
    that fails it falls back to the VS90COMNTOOLS env var.
    '''
    vsbase = VS_BASE % version
    
    try:
        productdir = Reg.get_value('%s\\Setup\\VC' % vsbase, 'productdir')
    except KeyError:
        log.debug('Unable to find productdir in registry')
        productdir = None

    if not productdir or os.path.isdir(productdir):
        toolskey = 'VS%0.f0COMNTOOLS' % version
        toolsdir = os.environ.get(toolskey, None)
        if toolsdir and os.path.isdir(toolsdir):
            productdir = os.path.join(toolsdir, os.pardir, os.pardir, 'VC')
            productdir = os.path.abspath(productdir)
            if not os.path.isdir(productdir):
                log.debug('%s is not a valid directory' % productdir)
                return None
        log.debug('Env var %s is not set or invalid' % toolskey)
    if not productdir:
        log.debug('No productdir found')
        return None
    vcvarsall = None.path.join(productdir, 'vcvarsall.bat')
    if os.path.isfile(vcvarsall):
        return vcvarsall
    None.debug('Unable to find vcvarsall.bat')


def query_vcvarsall(version, arch = ('x86',)):
    '''Launch vcvarsall.bat and read the settings from its environment'''
    vcvarsall = find_vcvarsall(version)
    interesting = {
        'lib',
        'path',
        'include',
        'libpath'}
    result = { }
# WARNING: Decompyle incomplete

VERSION = get_build_version()

class MSVCCompiler(CCompiler):
    pass
# WARNING: Decompyle incomplete
