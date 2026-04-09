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
import shlex
import itertools
from distutils import sysconfig
from distutils.dep_util import newer
from distutils.ccompiler import CCompiler, gen_preprocess_options, gen_lib_options
from distutils.errors import DistutilsExecError, CompileError, LibError, LinkError
from distutils import log
from _macos_compat import compiler_fixup

def _split_env(cmd):
    """
    For macOS, split command into 'env' portion (if any)
    and the rest of the linker command.

    >>> _split_env(['a', 'b', 'c'])
    ([], ['a', 'b', 'c'])
    >>> _split_env(['/usr/bin/env', 'A=3', 'gcc'])
    (['/usr/bin/env', 'A=3'], ['gcc'])
    """
    pivot = 0
# WARNING: Decompyle incomplete


def _split_aix(cmd):
    """
    AIX platforms prefix the compiler with the ld_so_aix
    script, so split that from the linker command.

    >>> _split_aix(['a', 'b', 'c'])
    ([], ['a', 'b', 'c'])
    >>> _split_aix(['/bin/foo/ld_so_aix', 'gcc'])
    (['/bin/foo/ld_so_aix'], ['gcc'])
    """
    pivot = os.path.basename(cmd[0]) == 'ld_so_aix'
    return (cmd[:pivot], cmd[pivot:])


def _linker_params(linker_cmd, compiler_cmd):
    """
    The linker command usually begins with the compiler
    command (possibly multiple elements), followed by zero or more
    params for shared library building.

    If the LDSHARED env variable overrides the linker command,
    however, the commands may not match.

    Return the best guess of the linker parameters by stripping
    the linker command. If the compiler command does not
    match the linker command, assume the linker command is
    just the first element.

    >>> _linker_params('gcc foo bar'.split(), ['gcc'])
    ['foo', 'bar']
    >>> _linker_params('gcc foo bar'.split(), ['other'])
    ['foo', 'bar']
    >>> _linker_params('ccache gcc foo bar'.split(), 'ccache gcc'.split())
    ['foo', 'bar']
    >>> _linker_params(['gcc'], ['gcc'])
    []
    """
    c_len = len(compiler_cmd)
    pivot = c_len if linker_cmd[:c_len] == compiler_cmd else 1
    return linker_cmd[pivot:]


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
        if not self.force:
            if not output_file is None:
                preprocess = newer(source, output_file)
                if not preprocess:
                    return None
                if None:
                    self.mkpath(os.path.dirname(output_file))
        
        try:
            self.spawn(pp_args)
            return None
        except DistutilsExecError:
            msg = None
            raise CompileError(msg)
            msg = None
            del msg


    
    def _compile(self, obj, src, ext, cc_args, extra_postargs, pp_opts):
        compiler_so = compiler_fixup(self.compiler_so, cc_args + extra_postargs)
        
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

    
    def _is_gcc(self):
