# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _shimmed_dist_utils.pyc (Python 3.11)

"""
Temporary shim module to indirect the bits of distutils we need from setuptools/distutils while providing useful
error messages beyond `No module named 'distutils' on Python >= 3.12, or when setuptools' vendored distutils is broken.

This is a compromise to avoid a hard-dep on setuptools for Python >= 3.12, since many users don't need runtime compilation support from CFFI.
"""
import sys

try:
    import setuptools
    del setuptools
except Exception:
    ex = None
    if sys.version_info >= (3, 12):
        raise Exception('This CFFI feature requires setuptools on Python >= 3.12. The setuptools module is missing or non-functional.'), ex
    ex = None
    del ex
except:
    ex = None
    del ex


try:
    from distutils import log, sysconfig
    from distutils.ccompiler import CCompiler
    from distutils.command.build_ext import build_ext
    from distutils.core import Distribution, Extension
    from distutils.dir_util import mkpath
    from distutils.errors import DistutilsSetupError, CompileError, LinkError
    from distutils.log import set_threshold, set_verbosity
    if sys.platform == 'win32':
        
        try:
            from distutils.msvc9compiler import MSVCCompiler
            
            try:
                pass
            except ImportError:
                MSVCCompiler = None
                
                try:
                    pass
                try:
                    pass
                except Exception:
                    ex = None
                    if sys.version_info >= (3, 12):
                        raise Exception('This CFFI feature requires setuptools on Python >= 3.12. Please install the setuptools package.'), ex
                    raise Exception('This CFFI feature requires distutils. Please install the distutils or setuptools package.'), ex
                    ex = None
                    del ex

                del sys
                return None
