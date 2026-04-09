# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: config.pyc (Python 3.11)

'''distutils.command.config

Implements the Distutils \'config\' command, a (mostly) empty command class
that exists mainly to be sub-classed by specific module distributions and
applications.  The idea is that while every "config" command is different,
at least they\'re all named the same, and users always see "config" in the
list of standard commands.  Also, this is a good place to put common
configure-like tasks: "try to compile this C code", or "figure out where
this header file lives".
'''
import os
import re
from distutils.core import Command
from distutils.errors import DistutilsExecError
from distutils.sysconfig import customize_compiler
from distutils import log
LANG_EXT = {
    'c': '.c',
    'c++': '.cxx' }

class config(Command):
    description = 'prepare to build'
    user_options = [
        ('compiler=', None, 'specify the compiler type'),
        ('cc=', None, 'specify the compiler executable'),
        ('include-dirs=', 'I', 'list of directories to search for header files'),
        ('define=', 'D', 'C preprocessor macros to define'),
        ('undef=', 'U', 'C preprocessor macros to undefine'),
        ('libraries=', 'l', 'external C libraries to link with'),
        ('library-dirs=', 'L', 'directories to search for external C libraries'),
        ('noisy', None, 'show every action (compile, link, run, ...) taken'),
        ('dump-source', None, 'dump generated source files before attempting to compile them')]
    
    def initialize_options(self):
        self.compiler = None
        self.cc = None
        self.include_dirs = None
        self.libraries = None
        self.library_dirs = None
        self.noisy = 1
        self.dump_source = 1
        self.temp_files = []

    
    def finalize_options(self):
        pass
    # WARNING: Decompyle incomplete

    
    def run(self):
        pass

    
    def _check_compiler(self):
        """Check that 'self.compiler' really is a CCompiler object;
        if not, make it one.
        """
        CCompiler = CCompiler
        new_compiler = new_compiler
        import distutils.ccompiler
        if not isinstance(self.compiler, CCompiler):
            self.compiler = new_compiler(compiler = self.compiler, dry_run = self.dry_run, force = 1)
            customize_compiler(self.compiler)
            if self.include_dirs:
                self.compiler.set_include_dirs(self.include_dirs)
            if self.libraries:
                self.compiler.set_libraries(self.libraries)
            if self.library_dirs:
                self.compiler.set_library_dirs(self.library_dirs)
                return None
            return None

    
    def _gen_temp_sourcefile(self, body, headers, lang):
        filename = '_configtest' + LANG_EXT[lang]
        file = open(filename, 'w')
        if headers:
            for header in headers:
                file.write('#include <%s>\n' % header)
                file.write('\n')
                file.write(body)
                if body[-1] != '\n':
                    file.write('\n')
        None(None, None)

    
    def _preprocess(self, body, headers, include_dirs, lang):
        src = self._gen_temp_sourcefile(body, headers, lang)
        out = '_configtest.i'
        self.temp_files.extend([
            src,
            out])
        self.compiler.preprocess(src, out, include_dirs = include_dirs)
        return (src, out)

    
    def _compile(self, body, headers, include_dirs, lang):
        src = self._gen_temp_sourcefile(body, headers, lang)
        if self.dump_source:
            dump_file(src, "compiling '%s':" % src)
        (obj,) = self.compiler.object_filenames([
            src])
        self.temp_files.extend([
            src,
            obj])
        self.compiler.compile([
            src], include_dirs = include_dirs)
        return (src, obj)

    
    def _link(self, body, headers, include_dirs, libraries, library_dirs, lang):
        (src, obj) = self._compile(body, headers, include_dirs, lang)
        prog = os.path.splitext(os.path.basename(src))[0]
        self.compiler.link_executable([
            obj], prog, libraries = libraries, library_dirs = library_dirs, target_lang = lang)
    # WARNING: Decompyle incomplete

    
    def _clean(self, *filenames):
        if not filenames:
            filenames = self.temp_files
            self.temp_files = []
        log.info('removing: %s', ' '.join(filenames))
        for filename in filenames:
            os.remove(filename)
            except OSError:
                continue
            return None

    
    def try_cpp(self, body, headers, include_dirs, lang = (None, None, None, 'c')):
        """Construct a source file from 'body' (a string containing lines
        of C/C++ code) and 'headers' (a list of header files to include)
        and run it through the preprocessor.  Return true if the
        preprocessor succeeded, false if there were any errors.
        ('body' probably isn't of much use, but what the heck.)
        """
        CompileError = CompileError
        import distutils.ccompiler
        self._check_compiler()
        ok = True
        
        try:
            self._preprocess(body, headers, include_dirs, lang)
        except CompileError:
            ok = False

        self._clean()
        return ok

    
    def search_cpp(self, pattern, body, headers, include_dirs, lang = (None, None, None, 'c')):
        """Construct a source file (just like 'try_cpp()'), run it through
        the preprocessor, and return true if any line of the output matches
        'pattern'.  'pattern' should either be a compiled regex object or a
        string containing a regex.  If both 'body' and 'headers' are None,
        preprocesses an empty file -- which can be useful to determine the
        symbols the preprocessor and compiler set by default.
        """
        self._check_compiler()
        (src, out) = self._preprocess(body, headers, include_dirs, lang)
        if isinstance(pattern, str):
            pattern = re.compile(pattern)
        file = open(out)
        match = False
        line = file.readline()
        if line == '':
            pass
        elif pattern.search(line):
            match = True
        
        None(None, None)

    
    def try_compile(self, body, headers, include_dirs, lang = (None, None, 'c')):
