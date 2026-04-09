# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

import os
import shutil
import subprocess
import sys
if os.name == 'nt':
    
    def _get_build_version():
        '''Return the version of MSVC that was used to build Python.

        For Python 2.3 and up, the version number is included in
        sys.version.  For earlier versions, assume the compiler is MSVC 6.
        '''
        prefix = 'MSC v.'
        i = sys.version.find(prefix)
        if i == -1:
            return 6
        i = None + len(prefix)
        (s, rest) = sys.version[i:].split(' ', 1)
        majorVersion = int(s[:-2]) - 6
        if majorVersion >= 13:
            majorVersion += 1
        minorVersion = int(s[2:3]) / 10
        if majorVersion == 6:
            minorVersion = 0
        if majorVersion >= 6:
            return majorVersion + minorVersion

    
    def find_msvcrt():
        '''Return the name of the VC runtime dll'''
        version = _get_build_version()
    # WARNING: Decompyle incomplete

    
    def find_library(name):
        if name in ('c', 'm'):
            return find_msvcrt()
        for directory in None.environ['PATH'].split(os.pathsep):
            fname = os.path.join(directory, name)
            if os.path.isfile(fname):
                
                return None, fname
            if None.lower().endswith('.dll'):
                continue
            if os.path.isfile(fname):
                
                return fname + '.dll', fname
            return None

elif os.name == 'posix' and sys.platform == 'darwin':
    from ctypes.macholib.dyld import dyld_find as _dyld_find
    
    def find_library(name):
        possible = [
            'lib%s.dylib' % name,
            '%s.dylib' % name,
            f'''{name!s}.framework/{name!s}''']
        for name in possible:
            
            return None, _dyld_find(name)
            except ValueError:
                continue
            return None

elif sys.platform.startswith('aix'):
    from ctypes._aix import find_library
elif os.name == 'posix':
    import re
    import tempfile
    
    def _is_elf(filename):
        '''Return True if the given file is an ELF file'''
        elf_header = b'\x7fELF'
        
        try:
            thefile = open(filename, 'br')
            
            try:
                None(None, None)
                return 
                with None:
                    if not None, thefile.read(4) == elf_header:
                        
                        try:
                            
                            try:
                                return None
                            except FileNotFoundError:
                                return False





    
    def _findLib_gcc(name):
        expr = os.fsencode('[^\\(\\)\\s]*lib%s\\.[^\\(\\)\\s]*' % re.escape(name))
        c_compiler = shutil.which('gcc')
        if not c_compiler:
            c_compiler = shutil.which('cc')
        if not c_compiler:
            return None
        temp = None.NamedTemporaryFile()
        
        try:
            args = [
                c_compiler,
                '-Wl,-t',
                '-o',
                temp.name,
                '-l' + name]
            env = dict(os.environ)
            env['LC_ALL'] = 'C'
            env['LANG'] = 'C'
            
            try:
                proc = subprocess.Popen(args, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, env = env)
                
                try:
                    pass
                except OSError:
                    
                    try:
                        
                        try:
                            temp.close()
                            return None
                        except FileNotFoundError:
                            return None
                            
                            try:
                                proc
                                trace = proc.stdout.read()
                                
                                try:
                                    None(None, None)
                                with None:
                                    if not None:
                                        
                                        try:
                                            
                                            try:
                                                
                                                try:
                                                    temp.close()
                                                except FileNotFoundError:
                                                    pass

                                                res = re.findall(expr, trace)
                                                if not res:
                                                    return None
                                                for file in None:
                                                    if not _is_elf(file):
                                                        continue
                                                    
                                                    return None, os.fsdecode(file)
                                                    return None










    if sys.platform == 'sunos5':
        
        def _get_soname(f):
