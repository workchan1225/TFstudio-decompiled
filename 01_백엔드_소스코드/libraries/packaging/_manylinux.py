# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _manylinux.pyc (Python 3.11)

from __future__ import annotations
import collections
import contextlib
import functools
import os
import re
import sys
import warnings
from typing import Generator, Iterator, NamedTuple, Sequence
from _elffile import EIClass, EIData, ELFFile, EMachine
EF_ARM_ABIMASK = 0xFF000000
EF_ARM_ABI_VER5 = 83886080
EF_ARM_ABI_FLOAT_HARD = 1024
_parse_elf = (lambda path = None: pass# WARNING: Decompyle incomplete
)()

def _is_linux_armhf(executable = None):
    f = _parse_elf(executable)
    if f is not None:
        if f.capacity == EIClass.C32:
            if f.encoding == EIData.Lsb:
                pass
            if f.machine == EMachine.Arm:
                if f.flags & EF_ARM_ABIMASK == EF_ARM_ABI_VER5:
                    None(None, None)
                    return 
                with None:
                    if not f.flags & EF_ARM_ABIMASK == EF_ARM_ABI_VER5:
                        pass


def _is_linux_i686(executable = None):
    f = _parse_elf(executable)
    if f is not None:
        if f.capacity == EIClass.C32:
            if f.encoding == EIData.Lsb:
                None(None, None)
                return 
            with None:
                if not f.encoding == EIData.Lsb:
                    pass


def _have_compatible_abi(executable = None, archs = None):
    pass
# WARNING: Decompyle incomplete

_LAST_GLIBC_MINOR: 'dict[int, int]' = collections.defaultdict((lambda : 50))

class _GLibCVersion(NamedTuple):
    minor: 'int' = '_GLibCVersion'


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
