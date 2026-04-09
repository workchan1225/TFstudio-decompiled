# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: build_ext.pyc (Python 3.11)

"""distutils.command.build_ext

Implements the Distutils 'build_ext' command, for building extension
modules (currently limited to C extensions, should accommodate C++
extensions ASAP)."""
import contextlib
import os
import re
import sys
from distutils.core import Command
from distutils.errors import *
from distutils.sysconfig import customize_compiler, get_python_version
from distutils.sysconfig import get_config_h_filename
from distutils.dep_util import newer_group
from distutils.extension import Extension
from distutils.util import get_platform
from distutils import log
from site import USER_BASE
extension_name_re = re.compile('^[a-zA-Z_][a-zA-Z_0-9]*(\\.[a-zA-Z_][a-zA-Z_0-9]*)*$')

def show_compilers():
    show_compilers = show_compilers
    import distutils.ccompiler
    show_compilers()


class build_ext(Command):
    description = 'build C/C++ extensions (compile/link to build directory)'
    sep_by = " (separated by '%s')" % os.pathsep
    user_options = [
        ('build-lib=', 'b', 'directory for compiled extension modules'),
        ('build-temp=', 't', 'directory for temporary files (build by-products)'),
        ('plat-name=', 'p', 'platform name to cross-compile for, if supported (default: %s)' % get_platform()),
        ('inplace', 'i', 'ignore build-lib and put compiled extensions into the source directory alongside your pure Python modules'),
        ('include-dirs=', 'I', 'list of directories to search for header files' + sep_by),
        ('define=', 'D', 'C preprocessor macros to define'),
        ('undef=', 'U', 'C preprocessor macros to undefine'),
        ('libraries=', 'l', 'external C libraries to link with'),
        ('library-dirs=', 'L', 'directories to search for external C libraries' + sep_by),
        ('rpath=', 'R', 'directories to search for shared C libraries at runtime'),
        ('link-objects=', 'O', 'extra explicit link objects to include in the link'),
        ('debug', 'g', 'compile/link with debugging information'),
        ('force', 'f', 'forcibly build everything (ignore file timestamps)'),
        ('compiler=', 'c', 'specify the compiler type'),
        ('parallel=', 'j', 'number of parallel build jobs'),
        ('swig-cpp', None, 'make SWIG create C++ files (default is C)'),
        ('swig-opts=', None, 'list of SWIG command line options'),
        ('swig=', None, 'path to the SWIG executable'),
        ('user', None, 'add user include, library and rpath')]
    boolean_options = [
        'inplace',
        'debug',
        'force',
        'swig-cpp',
        'user']
    help_options = [
        ('help-compiler', None, 'list available compilers', show_compilers)]
    
    def initialize_options(self):
        self.extensions = None
        self.build_lib = None
        self.plat_name = None
        self.build_temp = None
        self.inplace = 0
        self.package = None
        self.include_dirs = None
        self.define = None
        self.undef = None
        self.libraries = None
        self.library_dirs = None
        self.rpath = None
        self.link_objects = None
        self.debug = None
        self.force = None
        self.compiler = None
        self.swig = None
        self.swig_cpp = None
        self.swig_opts = None
        self.user = None
        self.parallel = None

    
    def finalize_options(self):
        sysconfig = sysconfig
        import distutils
        self.set_undefined_options('build', ('build_lib', 'build_lib'), ('build_temp', 'build_temp'), ('compiler', 'compiler'), ('debug', 'debug'), ('force', 'force'), ('parallel', 'parallel'), ('plat_name', 'plat_name'))
    # WARNING: Decompyle incomplete

    
    def run(self):
        new_compiler = new_compiler
        import distutils.ccompiler
        if not self.extensions:
            return None
        if None.distribution.has_c_libraries():
            build_clib = self.get_finalized_command('build_clib')
            if not build_clib.get_library_names():
                self.libraries.extend([])
                self.library_dirs.append(build_clib.build_clib)
                self.compiler = new_compiler(compiler = self.compiler, verbose = self.verbose, dry_run = self.dry_run, force = self.force)
                customize_compiler(self.compiler)
                if os.name == 'nt' and self.plat_name != get_platform():
                    self.compiler.initialize(self.plat_name)
    # WARNING: Decompyle incomplete

    
    def check_extensions_list(self, extensions):
        """Ensure that the list of extensions (presumably provided as a
        command option 'extensions') is valid, i.e. it is a list of
        Extension objects.  We also support the old-style list of 2-tuples,
        where the tuples are (ext_name, build_info), which are converted to
        Extension instances here.

        Raise DistutilsSetupError if the structure is invalid anywhere;
        just returns otherwise.
        """
        if not isinstance(extensions, list):
            raise DistutilsSetupError("'ext_modules' option must be a list of Extension instances")
    # WARNING: Decompyle incomplete

    
    def get_source_files(self):
        self.check_extensions_list(self.extensions)
        filenames = []
        for ext in self.extensions:
            filenames.extend(ext.sources)
            return filenames

    
    def get_outputs(self):
        self.check_extensions_list(self.extensions)
        outputs = []
        for ext in self.extensions:
            outputs.append(self.get_ext_fullpath(ext.name))
            return outputs

    
    def build_extensions(self):
        self.check_extensions_list(self.extensions)
        if self.parallel:
            self._build_extensions_parallel()
            return None
        None._build_extensions_serial()

    
    def _build_extensions_parallel(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _build_extensions_serial(self):
        for ext in self.extensions:
            self._filter_build_errors(ext)
            self.build_extension(ext)
            None(None, None)
        with None:
            if not None:
                pass
        continue

    _filter_build_errors = (lambda self, ext: pass# WARNING: Decompyle incomplete
)()
    
    def build_extension(self, ext):
        sources = ext.sources
    # WARNING: Decompyle incomplete

    
    def swig_sources(self, sources, extension):
        """Walk the list of source files in 'sources', looking for SWIG
        interface (.i) files.  Run SWIG on all that are found, and
        return a modified 'sources' list with SWIG source files replaced
        by the generated C (or C++) files.
        """
        new_sources = []
        swig_sources = []
        swig_targets = { }
        if self.swig_cpp:
            log.warn('--swig-cpp is deprecated - use --swig-opts=-c++')
        if self.swig_cpp and '-c++' in self.swig_opts or '-c++' in extension.swig_opts:
            target_ext = '.cpp'
        else:
            target_ext = '.c'
        for source in sources:
            (base, ext) = os.path.splitext(source)
            if ext == '.i':
                new_sources.append(base + '_wrap' + target_ext)
                swig_sources.append(source)
                swig_targets[source] = new_sources[-1]
                continue
            new_sources.append(source)
            if not swig_sources:
                return new_sources
            if not None.swig:
                swig = self.find_swig()
                swig_cmd = [
                    swig,
                    '-python']
                swig_cmd.extend(self.swig_opts)
                if self.swig_cpp:
                    swig_cmd.append('-c++')
        if not self.swig_opts:
            for o in extension.swig_opts:
                swig_cmd.append(o)
                for source in swig_sources:
                    target = swig_targets[source]
                    log.info('swigging %s to %s', source, target)
                    self.spawn(swig_cmd + [
                        '-o',
                        target,
                        source])
                    return new_sources

    
    def find_swig(self):
        '''Return the name of the SWIG executable.  On Unix, this is
        just "swig" -- it should be in the PATH.  Tries a bit harder on
        Windows.
        '''
        if os.name == 'posix':
            return 'swig'
        if None.name == 'nt':
            for vers in ('1.3', '1.2', '1.1'):
                fn = os.path.join('c:\\swig%s' % vers, 'swig.exe')
                if os.path.isfile(fn):
                    
                    return None, fn
                return 'swig.exe'
                raise DistutilsPlatformError("I don't know how to find (much less run) SWIG on platform '%s'" % os.name)

    
    def get_ext_fullpath(self, ext_name):
        '''Returns the path of the filename for a given extension.

        The file is located in `build_lib` or directly in the package
        (inplace option).
        '''
        fullname = self.get_ext_fullname(ext_name)
        modpath = fullname.split('.')
        filename = self.get_ext_filename(modpath[-1])
    # WARNING: Decompyle incomplete

    
    def get_ext_fullname(self, ext_name):
        '''Returns the fullname of a given extension name.

        Adds the `package.` prefix'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_ext_filename(self, ext_name):
        '''Convert the name of an extension (eg. "foo.bar") into the name
        of the file from which it will be loaded (eg. "foo/bar.so", or
        "foo\\bar.pyd").
        '''
        get_config_var = get_config_var
        import distutils.sysconfig
        ext_path = ext_name.split('.')
        ext_suffix = get_config_var('EXT_SUFFIX')
    # WARNING: Decompyle incomplete

    
    def get_export_symbols(self, ext):
        '''Return the list of symbols that a shared extension has to
        export.  This either uses \'ext.export_symbols\' or, if it\'s not
        provided, "PyInit_" + module_name.  Only relevant on Windows, where
        the .pyd file (DLL) must export the module "PyInit_" function.
        '''
        suffix = '_' + ext.name.split('.')[-1]
        
        try:
            suffix.encode('ascii')
        except UnicodeEncodeError:
            suffix = 'U' + suffix.encode('punycode').replace(b'-', b'_').decode('ascii')

        initfunc_name = 'PyInit' + suffix
        if initfunc_name not in ext.export_symbols:
            ext.export_symbols.append(initfunc_name)
        return ext.export_symbols

    
    def get_libraries(self, ext):
        """Return the list of libraries to link against when building a
        shared extension.  On most platforms, this is just 'ext.libraries';
        on Windows, we add the Python library (eg. python20.dll).
        """
        if sys.platform == 'win32':
            MSVCCompiler = MSVCCompiler
            import distutils._msvccompiler
            if not isinstance(self.compiler, MSVCCompiler):
                template = 'python%d%d'
                if self.debug:
                    template = template + '_d'
                pythonlib = template % (sys.hexversion >> 24, sys.hexversion >> 16 & 255)
                return ext.libraries + [
                    pythonlib]
        get_config_var = get_config_var
        import distutils.sysconfig
        link_libpython = False
        if get_config_var('Py_ENABLE_SHARED'):
            if hasattr(sys, 'getandroidapilevel'):
                link_libpython = True
            elif sys.platform == 'cygwin':
                link_libpython = True
            elif '_PYTHON_HOST_PLATFORM' in os.environ:
                if get_config_var('ANDROID_API_LEVEL') != 0:
                    link_libpython = True
                elif get_config_var('MACHDEP') == 'cygwin':
                    link_libpython = True
        if link_libpython:
            ldversion = get_config_var('LDVERSION')
            return ext.libraries + [
                'python' + ldversion]
        return None.libraries
