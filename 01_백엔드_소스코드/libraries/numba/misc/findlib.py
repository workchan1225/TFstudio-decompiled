# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: findlib.pyc (Python 3.11)

import sys
import os
import re

def get_lib_dirs():
    '''
    Anaconda specific
    '''
    if sys.platform == 'win32':
        dirnames = [
            'DLLs',
            os.path.join('Library', 'bin')]
    else:
        dirnames = [
            'lib']
    libdirs = dirnames()
    return libdirs

DLLNAMEMAP = {
    'linux': 'lib%(name)s\\.so\\.%(ver)s$',
    'linux2': 'lib%(name)s\\.so\\.%(ver)s$',
    'linux-static': 'lib%(name)s\\.a$',
    'darwin': 'lib%(name)s\\.%(ver)s\\.dylib$',
    'win32': '%(name)s%(ver)s\\.dll$',
    'win32-static': '%(name)s\\.lib$',
    'bsd': 'lib%(name)s\\.so\\.%(ver)s$' }
RE_VER = '[0-9]*([_\\.][0-9]+)*'

def find_lib(libname, libdir, platform, static = (None, None, False)):
    if not platform:
        pass
    platform = sys.platform
    platform = 'bsd' if 'bsd' in platform else platform
    if static:
        platform = f'''{platform}-static'''
    if platform not in DLLNAMEMAP:
        return []
    pat = None[platform] % {
        'name': libname,
        'ver': RE_VER }
    regex = re.compile(pat)
    return find_file(regex, libdir)


def find_file(pat, libdir = (None,)):
    pass
# WARNING: Decompyle incomplete
