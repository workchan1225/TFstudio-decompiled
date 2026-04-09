# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: build_py.pyc (Python 3.11)

"""distutils.command.build_py

Implements the Distutils 'build_py' command."""
import os
import importlib.util as importlib
import sys
import glob
from distutils.core import Command
from distutils.errors import DistutilsOptionError, DistutilsFileError
from distutils.util import convert_path
from distutils import log

class build_py(Command):
    description = '"build" pure Python modules (copy to build directory)'
    user_options = [
        ('build-lib=', 'd', 'directory to "build" (copy) to'),
        ('compile', 'c', 'compile .py to .pyc'),
        ('no-compile', None, "don't compile .py files [default]"),
        ('optimize=', 'O', 'also compile with optimization: -O1 for "python -O", -O2 for "python -OO", and -O0 to disable [default: -O0]'),
        ('force', 'f', 'forcibly build everything (ignore file timestamps)')]
    boolean_options = [
        'compile',
        'force']
    negative_opt = {
        'no-compile': 'compile' }
    
    def initialize_options(self):
        self.build_lib = None
        self.py_modules = None
        self.package = None
        self.package_data = None
        self.package_dir = None
        self.compile = 0
        self.optimize = 0
        self.force = None

    
    def finalize_options(self):
        self.set_undefined_options('build', ('build_lib', 'build_lib'), ('force', 'force'))
        self.packages = self.distribution.packages
        self.py_modules = self.distribution.py_modules
        self.package_data = self.distribution.package_data
        self.package_dir = { }
    # WARNING: Decompyle incomplete

    
    def run(self):
        if self.py_modules:
            self.build_modules()
        if self.packages:
            self.build_packages()
            self.build_package_data()
        self.byte_compile(self.get_outputs(include_bytecode = 0))

    
    def get_data_files(self):
        """Generate list of '(package,src_dir,build_dir,filenames)' tuples"""
        pass
    # WARNING: Decompyle incomplete

    
    def find_data_files(self, package, src_dir):
        """Return filenames for package's data files in 'src_dir'"""
        pass
    # WARNING: Decompyle incomplete

    
    def build_package_data(self):
        '''Copy data files into build directory'''
        for package, src_dir, build_dir, filenames in self.data_files:
            for filename in filenames:
                target = os.path.join(build_dir, filename)
                self.mkpath(os.path.dirname(target))
                self.copy_file(os.path.join(src_dir, filename), target, preserve_mode = False)
                return None

    
    def get_package_dir(self, package):
        """Return the directory, relative to the top of the source
        distribution, where package 'package' should be found
        (at least according to the 'package_dir' option, if any)."""
        path = package.split('.')
    # WARNING: Decompyle incomplete

    
    def check_package(self, package, package_dir):
