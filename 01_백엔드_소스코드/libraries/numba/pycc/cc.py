# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cc.pyc (Python 3.11)

from setuptools import distutils as dutils
from setuptools.command import build_ext
from setuptools.extension import Extension
import os
import shutil
import sys
import tempfile
from numba.core import typing, sigutils
from numba.core.compiler_lock import global_compiler_lock
from numba.pycc.compiler import ModuleCompiler, ExportEntry
from numba.pycc.platform import Toolchain
from numba import cext
dir_util = dutils.dir_util
log = dutils.log
extension_libs = cext.get_extension_libs()

class CC(object):
    """
    An ahead-of-time compiler to create extension modules that don't
    depend on Numba.
    """
    _mixin_sources = [
        'modulemixin.c'] + extension_libs
    _extra_cflags = { }
    _extra_ldflags = { }
    
    def __init__(self, extension_name, source_module = (None,)):
        if '.' in extension_name:
            raise ValueError('basename should be a simple module name, not qualified name')
        self._basename = extension_name
        self._init_function = 'pycc_init_' + extension_name
        self._exported_functions = { }
        f = sys._getframe(1)
    # WARNING: Decompyle incomplete

    name = (lambda self: self._basename)()
    output_file = (lambda self: self._output_file)()
    output_file = (lambda self, value: self._output_file = value)()
    output_dir = (lambda self: self._output_dir)()
    output_dir = (lambda self, value: self._output_dir = value)()
    use_nrt = (lambda self: self._use_nrt)()
    use_nrt = (lambda self, value: self._use_nrt = value)()
    target_cpu = (lambda self: self._target_cpu)()
    target_cpu = (lambda self, value: self._target_cpu = value)()
    verbose = (lambda self: self._verbose)()
    verbose = (lambda self, value: self._verbose = value)()
    
    def export(self, exported_name, sig):
        '''
        Mark a function for exporting in the extension module.
        '''
        pass
    # WARNING: Decompyle incomplete

    _export_entries = (lambda self: sorted(self._exported_functions.values(), key = (lambda entry: entry.symbol))
)()
    
    def _get_mixin_sources(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_mixin_defines(self):
        return [
            ('PYCC_MODULE_NAME', self._basename),
            ('PYCC_USE_NRT', int(self._use_nrt))]

    
    def _get_extra_cflags(self):
        extra_cflags = self._extra_cflags.get(sys.platform, [])
        if not extra_cflags:
            extra_cflags = self._extra_cflags.get(os.name, [])
        return extra_cflags

    
    def _get_extra_ldflags(self):
        extra_ldflags = self._extra_ldflags.get(sys.platform, [])
        if not extra_ldflags:
            extra_ldflags = self._extra_ldflags.get(os.name, [])
        if sys.platform.startswith('linux') and '-pthread' not in extra_ldflags:
            extra_ldflags.append('-pthread')
        return extra_ldflags

    
    def _compile_mixins(self, build_dir):
        sources = self._get_mixin_sources()
        macros = self._get_mixin_defines()
        include_dirs = self._toolchain.get_python_include_dirs()
        extra_cflags = self._get_extra_cflags()
        objects = self._toolchain.compile_objects(sources, build_dir, include_dirs = include_dirs, macros = macros, extra_cflags = extra_cflags)
        return objects

    _compile_object_files = (lambda self, build_dir: compiler = ModuleCompiler(self._export_entries, self._basename, self._use_nrt, cpu_name = self._target_cpu)compiler.external_init_function = self._init_functiontemp_obj = os.path.join(build_dir, os.path.splitext(self._output_file)[0] + '.o')log.info("generating LLVM code for '%s' into %s", self._basename, temp_obj)compiler.write_native_object(temp_obj, wrap = True)([
temp_obj], compiler.dll_exports))()
    compile = (lambda self: self._toolchain.verbose = self.verbosebuild_dir = tempfile.mkdtemp(prefix = 'pycc-build-%s-' % self._basename)(objects, dll_exports) = self._compile_object_files(build_dir)objects += self._compile_mixins(build_dir)extra_ldflags = self._get_extra_ldflags()output_dll = os.path.join(self._output_dir, self._output_file)libraries = self._toolchain.get_python_libraries()library_dirs = self._toolchain.get_python_library_dirs()self._toolchain.link_shared(output_dll, objects, libraries, library_dirs, export_symbols = dll_exports, extra_ldflags = extra_ldflags)shutil.rmtree(build_dir))()
    
    def distutils_extension(self, **kwargs):
        '''
        Create a distutils extension object that can be used in your
        setup.py.
        '''
        macros = kwargs.pop('macros', []) + self._get_mixin_defines()
        depends = kwargs.pop('depends', []) + [
            self._source_path]
        extra_compile_args = kwargs.pop('extra_compile_args', []) + self._get_extra_cflags()
        extra_link_args = kwargs.pop('extra_link_args', []) + self._get_extra_ldflags()
        include_dirs = kwargs.pop('include_dirs', []) + self._toolchain.get_python_include_dirs()
        libraries = kwargs.pop('libraries', []) + self._toolchain.get_python_libraries()
        library_dirs = kwargs.pop('library_dirs', []) + self._toolchain.get_python_library_dirs()
        python_package_path = None[self._source_module:self._source_module.rfind('.') + 1]
    # WARNING: Decompyle incomplete



class _CCExtension(Extension):
    '''
    A Numba-specific Extension subclass to LLVM-compile pure Python code
    to an extension module.
    '''
    _cc = None
    _distutils_monkey_patched = False
    
    def _prepare_object_files(self, build_ext):
        cc = self._cc
    # WARNING: Decompyle incomplete

    monkey_patch_distutils = (lambda cls: pass# WARNING: Decompyle incomplete
)()
