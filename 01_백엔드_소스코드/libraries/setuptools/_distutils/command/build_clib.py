# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: build_clib.pyc (Python 3.11)

"""distutils.command.build_clib

Implements the Distutils 'build_clib' command, to build a C/C++ library
that is included in the module distribution and needed by an extension
module."""
import os
from distutils.core import Command
from distutils.errors import DistutilsSetupError
from distutils.sysconfig import customize_compiler
from distutils import log

def show_compilers():
    show_compilers = show_compilers
    import distutils.ccompiler
    show_compilers()


class build_clib(Command):
    description = 'build C/C++ libraries used by Python extensions'
    user_options = [
        ('build-clib=', 'b', 'directory to build C/C++ libraries to'),
        ('build-temp=', 't', 'directory to put temporary build by-products'),
        ('debug', 'g', 'compile with debugging information'),
        ('force', 'f', 'forcibly build everything (ignore file timestamps)'),
        ('compiler=', 'c', 'specify the compiler type')]
    boolean_options = [
        'debug',
        'force']
    help_options = [
        ('help-compiler', None, 'list available compilers', show_compilers)]
    
    def initialize_options(self):
        self.build_clib = None
        self.build_temp = None
        self.libraries = None
        self.include_dirs = None
        self.define = None
        self.undef = None
        self.debug = None
        self.force = 0
        self.compiler = None

    
    def finalize_options(self):
        self.set_undefined_options('build', ('build_temp', 'build_clib'), ('build_temp', 'build_temp'), ('compiler', 'compiler'), ('debug', 'debug'), ('force', 'force'))
        self.libraries = self.distribution.libraries
        if self.libraries:
            self.check_library_list(self.libraries)
    # WARNING: Decompyle incomplete

    
    def run(self):
        if not self.libraries:
            return None
        new_compiler = new_compiler
        import distutils.ccompiler
        self.compiler = new_compiler(compiler = self.compiler, dry_run = self.dry_run, force = self.force)
        customize_compiler(self.compiler)
    # WARNING: Decompyle incomplete

    
    def check_library_list(self, libraries):
        """Ensure that the list of libraries is valid.

        `library` is presumably provided as a command option 'libraries'.
        This method checks that it is a list of 2-tuples, where the tuples
        are (library_name, build_info_dict).

        Raise DistutilsSetupError if the structure is invalid anywhere;
        just returns otherwise.
        """
        if not isinstance(libraries, list):
            raise DistutilsSetupError("'libraries' option must be a list of tuples")
        for lib in libraries:
            if isinstance(lib, tuple) and len(lib) != 2:
                raise DistutilsSetupError("each element of 'libraries' must a 2-tuple")
            (name, build_info) = lib
            if not isinstance(name, str):
                raise DistutilsSetupError("first element of each tuple in 'libraries' must be a string (the library name)")
            if ('/' in name or os.sep != '/') and os.sep in name:
                raise DistutilsSetupError("bad library name '%s': may not contain directory separators" % lib[0])
            if not isinstance(build_info, dict):
                raise DistutilsSetupError("second element of each tuple in 'libraries' must be a dictionary (build info)")
            return None

    
    def get_library_names(self):
        if not self.libraries:
            return None
        lib_names = None
        for lib_name, build_info in self.libraries:
            lib_names.append(lib_name)
            return lib_names

    
    def get_source_files(self):
        self.check_library_list(self.libraries)
        filenames = []
    # WARNING: Decompyle incomplete

    
    def build_libraries(self, libraries):
        pass
    # WARNING: Decompyle incomplete
