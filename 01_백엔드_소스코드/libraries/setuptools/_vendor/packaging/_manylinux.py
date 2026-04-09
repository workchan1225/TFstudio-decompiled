# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _manylinux.pyc (Python 3.11)

import collections
import functools
import os
import re
import struct
import sys
import warnings
from typing import IO, Dict, Iterator, NamedTuple, Optional, Tuple

class _ELFFileHeader:
    
    class _InvalidELFFileHeader(ValueError):
        '''
        An invalid ELF file header was found.
        '''
        pass

    ELF_MAGIC_NUMBER = 2135247942
    ELFCLASS32 = 1
    ELFCLASS64 = 2
    ELFDATA2LSB = 1
    ELFDATA2MSB = 2
    EM_386 = 3
    EM_S390 = 22
    EM_ARM = 40
    EM_X86_64 = 62
    EF_ARM_ABIMASK = 0xFF000000
    EF_ARM_ABI_VER5 = 83886080
    EF_ARM_ABI_FLOAT_HARD = 1024
    
    def __init__(self = None, file = None):
        pass
    # WARNING: Decompyle incomplete



def _get_elf_header():
    
    try:
        f = open(sys.executable, 'rb')
        elf_header = _ELFFileHeader(f)
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        pass
                    except (OSError, TypeError, _ELFFileHeader._InvalidELFFileHeader):
                        return None

                    return elf_header





def _is_linux_armhf():
    elf_header = _get_elf_header()
# WARNING: Decompyle incomplete


def _is_linux_i686():
    elf_header = _get_elf_header()
# WARNING: Decompyle incomplete


def _have_compatible_abi(arch = None):
    if arch == 'armv7l':
        return _is_linux_armhf()
    if None == 'i686':
        return _is_linux_i686()
    return None in frozenset({'ppc64', 's390x', 'x86_64', 'aarch64', 'ppc64le'})

_LAST_GLIBC_MINOR: Dict[(int, int)] = collections.defaultdict((lambda : 50))

class _GLibCVersion(NamedTuple):
    minor: int = '_GLibCVersion'


def _glibc_version_string_confstr():
    '''
    Primary implementation of glibc_version_string using os.confstr.
    '''
    pass
# WARNING: Decompyle incomplete


def _glibc_version_string_ctypes():
    '''
    Fallback implementation of glibc_version_string using ctypes.
    '''
    
    try:
        import ctypes
    except ImportError:
        return None

    
    try:
        process_namespace = ctypes.CDLL(None)
    except OSError:
        return None

    
    try:
        gnu_get_libc_version = process_namespace.gnu_get_libc_version
    except AttributeError:
        return None

    gnu_get_libc_version.restype = ctypes.c_char_p
    version_str = gnu_get_libc_version()
    if not isinstance(version_str, str):
        version_str = version_str.decode('ascii')
    return version_str


def _glibc_version_string():
