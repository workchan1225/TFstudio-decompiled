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
from distutils.errors import DistutilsExecError, DistutilsPlatformError, CompileError, LibError, LinkError
from distutils.ccompiler import CCompiler, gen_lib_options
from distutils import log
from distutils.util import get_platform
import winreg
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
    '''Helper class to read values from the registry
    '''
    
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
        d = Reg.get_value(base, f'''{p!s}\\{key!s}''')
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
    '''Remove duplicate values of an environment variable.
    '''
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
    '''Launch vcvarsall.bat and read the settings from its environment
    '''
    vcvarsall = find_vcvarsall(version)
    interesting = {
        'lib',
        'path',
        'include',
        'libpath'}
    result = { }
# WARNING: Decompyle incomplete

VERSION = get_build_version()
if VERSION < 8:
    raise DistutilsPlatformError('VC %0.1f is not supported by this module' % VERSION)

class MSVCCompiler(CCompiler):
    '''Concrete class that implements an interface to Microsoft Visual C++,
       as defined by the CCompiler abstract class.'''
    compiler_type = 'msvc'
    executables = { }
    _c_extensions = [
        '.c']
    _cpp_extensions = [
        '.cc',
        '.cpp',
        '.cxx']
    _rc_extensions = [
        '.rc']
    _mc_extensions = [
        '.mc']
    src_extensions = _c_extensions + _cpp_extensions + _rc_extensions + _mc_extensions
    res_extension = '.res'
    obj_extension = '.obj'
    static_lib_extension = '.lib'
    shared_lib_extension = '.dll'
    static_lib_format = '%s%s'
    shared_lib_format = '%s%s'
    exe_extension = '.exe'
    
    def __init__(self, verbose, dry_run, force = (0, 0, 0)):
        CCompiler.__init__(self, verbose, dry_run, force)
        self._MSVCCompiler__version = VERSION
        self._MSVCCompiler__root = 'Software\\Microsoft\\VisualStudio'
        self._MSVCCompiler__paths = []
        self.plat_name = None
        self._MSVCCompiler__arch = None
        self.initialized = False

    
    def initialize(self, plat_name = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def object_filenames(self, source_filenames, strip_dir, output_dir = (0, '')):
        pass
    # WARNING: Decompyle incomplete

    
    def compile(self, sources, output_dir, macros, include_dirs, debug, extra_preargs, extra_postargs, depends = (None, None, None, 0, None, None, None)):
        if not self.initialized:
            self.initialize()
        compile_info = self._setup_compile(output_dir, macros, include_dirs, sources, depends, extra_postargs)
        (macros, objects, extra_postargs, pp_opts, build) = compile_info
        if not extra_preargs:
            compile_opts = []
            compile_opts.append('/c')
            if debug:
                compile_opts.extend(self.compile_options_debug)
            else:
                compile_opts.extend(self.compile_options)
        for obj in objects:
            (src, ext) = build[obj]
        except KeyError:
            continue
        if debug:
            src = os.path.abspath(src)
        if ext in self._c_extensions:
            input_opt = '/Tc' + src
        elif ext in self._cpp_extensions:
            input_opt = '/Tp' + src
        elif ext in self._rc_extensions:
            input_opt = src
            output_opt = '/fo' + obj
            self.spawn([
                self.rc] + pp_opts + [
                output_opt] + [
                input_opt])
        else:
            except DistutilsExecError:
                msg = None
                raise CompileError(msg)
                msg = None
                del msg
        continue
        continue
        raise CompileError(f'''Don\'t know how to compile {src!s} to {obj!s}''')
        output_opt = '/Fo' + obj
        self.spawn([
            self.cc] + compile_opts + pp_opts + [
            input_opt,
            output_opt] + extra_postargs)
        continue
        except DistutilsExecError:
            msg = None
            raise CompileError(msg)
            msg = None
            del msg
        return objects

    
    def create_static_lib(self, objects, output_libname, output_dir, debug, target_lang = (None, 0, None)):
        if not self.initialized:
            self.initialize()
        (objects, output_dir) = self._fix_object_args(objects, output_dir)
        output_filename = self.library_filename(output_libname, output_dir = output_dir)
        if self._need_link(objects, output_filename):
            lib_args = objects + [
                '/OUT:' + output_filename]
            if debug:
                pass
            
            try:
                self.spawn([
                    self.lib] + lib_args)
                return None
            except DistutilsExecError:
                msg = None
                raise LibError(msg)
                msg = None
                del msg
                log.debug('skipping %s (up-to-date)', output_filename)
                return None


    
    def link(self, target_desc, objects, output_filename, output_dir, libraries, library_dirs, runtime_library_dirs, export_symbols, debug, extra_preargs, extra_postargs, build_temp, target_lang = (None, None, None, None, None, 0, None, None, None, None)):
        if not self.initialized:
            self.initialize()
        (objects, output_dir) = self._fix_object_args(objects, output_dir)
        fixed_args = self._fix_lib_args(libraries, library_dirs, runtime_library_dirs)
        (libraries, library_dirs, runtime_library_dirs) = fixed_args
        if runtime_library_dirs:
            self.warn("I don't know what to do with 'runtime_library_dirs': " + str(runtime_library_dirs))
        lib_opts = gen_lib_options(self, library_dirs, runtime_library_dirs, libraries)
    # WARNING: Decompyle incomplete

    
    def manifest_setup_ldargs(self, output_filename, build_temp, ld_args):
        temp_manifest = os.path.join(build_temp, os.path.basename(output_filename) + '.manifest')
        ld_args.append('/MANIFESTFILE:' + temp_manifest)

    
    def manifest_get_embed_info(self, target_desc, ld_args):
        for arg in ld_args:
            if arg.startswith('/MANIFESTFILE:'):
                temp_manifest = arg.split(':', 1)[1]
            
            return None
            if target_desc == CCompiler.EXECUTABLE:
                mfid = 1
            else:
                mfid = 2
                temp_manifest = self._remove_visual_c_ref(temp_manifest)
    # WARNING: Decompyle incomplete

    
    def _remove_visual_c_ref(self, manifest_file):
        pass
    # WARNING: Decompyle incomplete

    
    def library_dir_option(self, dir):
        return '/LIBPATH:' + dir

    
    def runtime_library_dir_option(self, dir):
        raise DistutilsPlatformError("don't know how to set runtime library search path for MSVC++")

    
    def library_option(self, lib):
        return self.library_filename(lib)

    
    def find_library_file(self, dirs, lib, debug = (0,)):
        if debug:
            try_names = [
                lib + '_d',
                lib]
        else:
            try_names = [
                lib]
        for dir in dirs:
            for name in try_names:
                libfile = os.path.join(dir, self.library_filename(name))
                if os.path.exists(libfile):
                    
                    
                    return None, None, libfile
                return None

    
    def find_exe(self, exe):
        """Return path to an MSVC executable program.

        Tries to find the program in several places: first, one of the
        MSVC program search paths from the registry; next, the directories
        in the PATH environment variable.  If any of those work, return an
        absolute path that is known to exist.  If none of them work, just
        return the original program name, 'exe'.
        """
        for p in self._MSVCCompiler__paths:
            fn = os.path.join(os.path.abspath(p), exe)
            if os.path.isfile(fn):
                
                return None, fn
            for os.path.join(os.path.abspath(p), exe) in os.environ['Path'].split(';'):
                if os.path.isfile(fn):
                    
                    return None, fn
                return exe
