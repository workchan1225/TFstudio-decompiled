# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: build_scripts.pyc (Python 3.11)

"""distutils.command.build_scripts

Implements the Distutils 'build_scripts' command."""
import os
import re
from stat import ST_MODE
from distutils import sysconfig
from distutils.core import Command
from distutils.dep_util import newer
from distutils.util import convert_path
from distutils import log
import tokenize
shebang_pattern = re.compile('^#!.*python[0-9.]*([ \t].*)?$')
first_line_re = shebang_pattern

class build_scripts(Command):
    description = '"build" scripts (copy and fixup #! line)'
    user_options = [
        ('build-dir=', 'd', 'directory to "build" (copy) to'),
        ('force', 'f', 'forcibly build everything (ignore file timestamps'),
        ('executable=', 'e', 'specify final destination interpreter path')]
    boolean_options = [
        'force']
    
    def initialize_options(self):
        self.build_dir = None
        self.scripts = None
        self.force = None
        self.executable = None

    
    def finalize_options(self):
        self.set_undefined_options('build', ('build_scripts', 'build_dir'), ('force', 'force'), ('executable', 'executable'))
        self.scripts = self.distribution.scripts

    
    def get_source_files(self):
        return self.scripts

    
    def run(self):
        if not self.scripts:
            return None
        None.copy_scripts()

    
    def copy_scripts(self):
        '''
        Copy each script listed in ``self.scripts``.

        If a script is marked as a Python script (first line matches
        \'shebang_pattern\', i.e. starts with ``#!`` and contains
        "python"), then adjust in the copy the first line to refer to
        the current Python interpreter.
        '''
        self.mkpath(self.build_dir)
        outfiles = []
        updated_files = []
        for script in self.scripts:
            self._copy_script(script, outfiles, updated_files)
            self._change_modes(outfiles)
            return (outfiles, updated_files)

    
    def _copy_script(self, script, outfiles, updated_files):
        shebang_match = None
        script = convert_path(script)
        outfile = os.path.join(self.build_dir, os.path.basename(script))
        outfiles.append(outfile)
        if not self.force and newer(script, outfile):
            log.debug('not copying %s (up-to-date)', script)
            return None
        
        try:
            f = tokenize.open(script)
            first_line = f.readline()
            if not first_line:
                self.warn('%s is an empty file (skipping)' % script)
                return None
            shebang_match = None.match(first_line)
        except OSError:
            if not self.dry_run:
                raise 
            f = None

        updated_files.append(outfile)
        if shebang_match:
            log.info('copying and adjusting %s -> %s', script, self.build_dir)
            if not self.dry_run:
                if not sysconfig.python_build:
                    executable = self.executable
                else:
                    executable = os.path.join(sysconfig.get_config_var('BINDIR'), f'''python{sysconfig.get_config_var('VERSION')!s}{sysconfig.get_config_var('EXE')!s}''')
                if not shebang_match.group(1):
                    post_interp = ''
                    shebang = '#!' + executable + post_interp + '\n'
                    self._validate_shebang(shebang, f.encoding)
                    outf = open(outfile, 'w', encoding = f.encoding)
                    outf.write(shebang)
                    outf.writelines(f.readlines())
                    None(None, None)
                else:
                    with None:
                        if not shebang_match.group(1):
                            pass
            if f:
                f.close()
                return None
            return None
        if f:
            f.close()
        self.copy_file(script, outfile)

    
    def _change_modes(self, outfiles):
        if os.name != 'posix':
            return None
        for file in None:
            self._change_mode(file)
            return None

    
    def _change_mode(self, file):
        if self.dry_run:
            log.info('changing mode of %s', file)
            return None
        oldmode = None.stat(file)[ST_MODE] & 4095
        newmode = (oldmode | 365) & 4095
        if newmode != oldmode:
            log.info('changing mode of %s from %o to %o', file, oldmode, newmode)
            os.chmod(file, newmode)
            return None

    _validate_shebang = (lambda shebang, encoding: try:
shebang.encode('utf-8')except UnicodeEncodeError:
raise ValueError('The shebang ({!r}) is not encodable to utf-8'.format(shebang))try:
shebang.encode(encoding)Noneexcept UnicodeEncodeError:
raise ValueError('The shebang ({!r}) is not encodable to the script encoding ({})'.format(shebang, encoding)))()
