# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: unixccompiler.pyc (Python 3.11)

'''distutils.unixccompiler

Contains the UnixCCompiler class, a subclass of CCompiler that handles
the "typical" Unix-style command-line C compiler:
  * macros defined with -Dname[=value]
  * macros undefined with -Uname
  * include search directories specified with -Idir
  * libraries specified with -lllib
  * library search directories specified with -Ldir
  * compile handled by \'cc\' (or similar) executable with -c option:
    compiles .c to .o
  * link static library handled by \'ar\' command (possibly with \'ranlib\')
  * link shared library handled by \'cc -shared\'
'''
import os
import sys
import re
from distutils import sysconfig
from distutils.dep_util import newer
from distutils.ccompiler import CCompiler, gen_preprocess_options, gen_lib_options
from distutils.errors import DistutilsExecError, CompileError, LibError, LinkError
from distutils import log
if sys.platform == 'darwin':
    import _osx_support

class UnixCCompiler(CCompiler):
    compiler_type = 'unix'
    executables = {
        'preprocessor': None,
        'compiler': [
            'cc'],
        'compiler_so': [
            'cc'],
        'compiler_cxx': [
            'cc'],
        'linker_so': [
            'cc',
            '-shared'],
        'linker_exe': [
            'cc'],
        'archiver': [
            'ar',
            '-cr'],
        'ranlib': None }
    if sys.platform[:6] == 'darwin':
        executables['ranlib'] = [
            'ranlib']
    src_extensions = [
        '.c',
        '.C',
        '.cc',
        '.cxx',
        '.cpp',
        '.m']
    obj_extension = '.o'
    static_lib_extension = '.a'
    shared_lib_extension = '.so'
    dylib_lib_extension = '.dylib'
    xcode_stub_lib_extension = '.tbd'
    static_lib_format = 'lib%s%s'
    shared_lib_format = 'lib%s%s'
    dylib_lib_format = 'lib%s%s'
    xcode_stub_lib_format = dylib_lib_format
    if sys.platform == 'cygwin':
        exe_extension = '.exe'
    
    def preprocess(self, source, output_file, macros, include_dirs, extra_preargs, extra_postargs = (None, None, None, None, None)):
        fixed_args = self._fix_compile_args(None, macros, include_dirs)
        (ignore, macros, include_dirs) = fixed_args
        pp_opts = gen_preprocess_options(macros, include_dirs)
        pp_args = self.preprocessor + pp_opts
        if output_file:
            pp_args.extend([
                '-o',
                output_file])
        if extra_preargs:
            pp_args[:0] = extra_preargs
        if extra_postargs:
            pp_args.extend(extra_postargs)
        pp_args.append(source)
    # WARNING: Decompyle incomplete

    
    def _compile(self, obj, src, ext, cc_args, extra_postargs, pp_opts):
        compiler_so = self.compiler_so
        if sys.platform == 'darwin':
            compiler_so = _osx_support.compiler_fixup(compiler_so, cc_args + extra_postargs)
        
        try:
            self.spawn(compiler_so + cc_args + [
                src,
                '-o',
                obj] + extra_postargs)
            return None
        except DistutilsExecError:
            msg = None
            raise CompileError(msg)
            msg = None
            del msg


    
    def create_static_lib(self, objects, output_libname, output_dir, debug, target_lang = (None, 0, None)):
        (objects, output_dir) = self._fix_object_args(objects, output_dir)
        output_filename = self.library_filename(output_libname, output_dir = output_dir)
        if self._need_link(objects, output_filename):
            self.mkpath(os.path.dirname(output_filename))
            self.spawn(self.archiver + [
                output_filename] + objects + self.objects)
            if self.ranlib:
                
                try:
                    self.spawn(self.ranlib + [
                        output_filename])
                    return None
                except DistutilsExecError:
                    msg = None
                    raise LibError(msg)
                    msg = None
                    del msg
                    return None
                    log.debug('skipping %s (up-to-date)', output_filename)
                    return None


    
    def link(self, target_desc, objects, output_filename, output_dir, libraries, library_dirs, runtime_library_dirs, export_symbols, debug, extra_preargs, extra_postargs, build_temp, target_lang = (None, None, None, None, None, 0, None, None, None, None)):
        (objects, output_dir) = self._fix_object_args(objects, output_dir)
        fixed_args = self._fix_lib_args(libraries, library_dirs, runtime_library_dirs)
        (libraries, library_dirs, runtime_library_dirs) = fixed_args
        lib_opts = gen_lib_options(self, library_dirs, runtime_library_dirs, libraries)
        if not isinstance(output_dir, (str, type(None))):
            raise TypeError("'output_dir' must be a string or None")
    # WARNING: Decompyle incomplete

    
    def library_dir_option(self, dir):
        return '-L' + dir

    
    def _is_gcc(self, compiler_name):
        pass
    # WARNING: Decompyle incomplete

    
    def runtime_library_dir_option(self, dir):
        compiler = os.path.basename(sysconfig.get_config_var('CC'))
        if sys.platform[:6] == 'darwin':
            return '-L' + dir
        if None.platform[:7] == 'freebsd':
            return '-Wl,-rpath=' + dir
        if None.platform[:5] == 'hp-ux':
            if self._is_gcc(compiler):
                return [
                    '-Wl,+s',
                    '-L' + dir]
            return [
                None,
                '-L' + dir]
        if None._is_gcc(compiler):
            if sysconfig.get_config_var('GNULD') == 'yes':
                return '-Wl,--enable-new-dtags,-R' + dir
            return None + dir
        return None + dir

    
    def library_option(self, lib):
        return '-l' + lib

    
    def find_library_file(self, dirs, lib, debug = (0,)):
        shared_f = self.library_filename(lib, lib_type = 'shared')
        dylib_f = self.library_filename(lib, lib_type = 'dylib')
        xcode_stub_f = self.library_filename(lib, lib_type = 'xcode_stub')
        static_f = self.library_filename(lib, lib_type = 'static')
    # WARNING: Decompyle incomplete
