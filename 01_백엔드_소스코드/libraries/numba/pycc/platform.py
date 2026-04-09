# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: platform.pyc (Python 3.11)

import setuptools
from setuptools.command.build_ext import build_ext
from setuptools.dist import Distribution
import numpy as np
import functools
import os
import subprocess
import sys
from tempfile import mkdtemp
from contextlib import contextmanager
from pathlib import Path
CCompiler = setuptools.distutils.ccompiler.CCompiler
new_compiler = setuptools.distutils.ccompiler.new_compiler
customize_compiler = setuptools.distutils.sysconfig.customize_compiler
log = setuptools.distutils.log
_configs = {
    'win': ('.dll', '.pyd'),
    'default': ('.so', '.so') }

def get_configs(arg):
    return _configs.get(sys.platform[:3], _configs['default'])[arg]

find_shared_ending = functools.partial(get_configs, 0)
find_pyext_ending = functools.partial(get_configs, 1)
_gentmpfile = (lambda suffix: pass# WARNING: Decompyle incomplete
)()
external_compiler_works = (lambda : compiler = new_compiler()customize_compiler(compiler)for suffix in ('.c', '.cxx'):
ntf = _gentmpfile(suffix)simple_c = 'int main(void) { return 0; }'ntf.write(simple_c)ntf.flush()ntf.close()compiler.compile([
ntf.name], output_dir = Path(ntf.name).anchor)None(None, None)with None:
if not None:
passcontinueexcept Exception:
FalseTrue)()

class _DummyExtension(object):
    libraries = []


class Toolchain(object):
    
    def __init__(self):
        if not external_compiler_works():
            self._raise_external_compiler_error()
        self._verbose = False
        self._compiler = new_compiler()
        customize_compiler(self._compiler)
        self._build_ext = build_ext(Distribution())
        self._build_ext.finalize_options()
        self._py_lib_dirs = self._build_ext.library_dirs
        self._py_include_dirs = self._build_ext.include_dirs
        np_compile_args = {
            'include_dirs': [
                np.get_include()] }
        if sys.platform == 'win32':
            np_compile_args['libraries'] = []
        else:
            np_compile_args['libraries'] = [
                'm']
        self._math_info = np_compile_args

    verbose = (lambda self: self._verbose)()
    verbose = (lambda self, value: self._verbose = valuelog.set_threshold(log.INFO if value else log.WARN))()
    
    def _raise_external_compiler_error(self):
        basemsg = 'Attempted to compile AOT function without the compiler used by `numpy.distutils` present.'
        conda_msg = 'If using conda try:\n\n#> conda install %s'
        plt = sys.platform
        if plt.startswith('linux'):
            if sys.maxsize <= 0x100000000:
                compilers = [
                    'gcc_linux-32',
                    'gxx_linux-32']
            else:
                compilers = [
                    'gcc_linux-64',
                    'gxx_linux-64']
            msg = f'''{basemsg!s} {conda_msg % ' '.join(compilers)!s}'''
        elif plt.startswith('darwin'):
            compilers = [
                'clang_osx-64',
                'clangxx_osx-64']
            msg = f'''{basemsg!s} {conda_msg % ' '.join(compilers)!s}'''
        elif plt.startswith('win32'):
            winmsg = 'Cannot find suitable msvc.'
            msg = f'''{basemsg!s} {winmsg!s}'''
        else:
            msg = 'Unknown platform %s' % plt
        raise RuntimeError(msg)

    
    def compile_objects(self, sources, output_dir, include_dirs, depends, macros, extra_cflags = ((), (), (), None)):
