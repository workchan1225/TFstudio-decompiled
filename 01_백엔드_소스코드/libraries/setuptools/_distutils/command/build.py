# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: build.pyc (Python 3.11)

"""distutils.command.build

Implements the Distutils 'build' command."""
import sys
import os
from distutils.core import Command
from distutils.errors import DistutilsOptionError
from distutils.util import get_platform

def show_compilers():
    show_compilers = show_compilers
    import distutils.ccompiler
    show_compilers()


class build(Command):
    description = 'build everything needed to install'
    user_options = [
        ('build-base=', 'b', 'base directory for build library'),
        ('build-purelib=', None, 'build directory for platform-neutral distributions'),
        ('build-platlib=', None, 'build directory for platform-specific distributions'),
        ('build-lib=', None, 'build directory for all distribution (defaults to either build-purelib or build-platlib'),
        ('build-scripts=', None, 'build directory for scripts'),
        ('build-temp=', 't', 'temporary build directory'),
        ('plat-name=', 'p', 'platform name to build for, if supported (default: %s)' % get_platform()),
        ('compiler=', 'c', 'specify the compiler type'),
        ('parallel=', 'j', 'number of parallel build jobs'),
        ('debug', 'g', 'compile extensions and libraries with debugging information'),
        ('force', 'f', 'forcibly build everything (ignore file timestamps)'),
        ('executable=', 'e', 'specify final destination interpreter path (build.py)')]
    boolean_options = [
        'debug',
        'force']
    help_options = [
        ('help-compiler', None, 'list available compilers', show_compilers)]
    
    def initialize_options(self):
        self.build_base = 'build'
        self.build_purelib = None
        self.build_platlib = None
        self.build_lib = None
        self.build_temp = None
        self.build_scripts = None
        self.compiler = None
        self.plat_name = None
        self.debug = None
        self.force = 0
        self.executable = None
        self.parallel = None

    
    def finalize_options(self):
        pass
    # WARNING: Decompyle incomplete

    
    def run(self):
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)
            return None

    
    def has_pure_modules(self):
        return self.distribution.has_pure_modules()

    
    def has_c_libraries(self):
        return self.distribution.has_c_libraries()

    
    def has_ext_modules(self):
        return self.distribution.has_ext_modules()

    
    def has_scripts(self):
        return self.distribution.has_scripts()

    sub_commands = [
        ('build_py', has_pure_modules),
        ('build_clib', has_c_libraries),
        ('build_ext', has_ext_modules),
        ('build_scripts', has_scripts)]
