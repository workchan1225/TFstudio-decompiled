# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _musllinux.pyc (Python 3.11)

__doc__ = 'PEP 656 support.\n\nThis module implements logic to detect if the currently running Python is\nlinked against musl, and what musl version is used.\n'
import contextlib
import functools
import operator
import os
import re
import struct
import subprocess
import sys
from typing import IO, Iterator, NamedTuple, Optional, Tuple

def _read_unpacked(f = None, fmt = None):
    return struct.unpack(fmt, f.read(struct.calcsize(fmt)))


def _parse_ld_musl_from_elf(f = None):
    '''Detect musl libc location by parsing the Python executable.

    Based on: https://gist.github.com/lyssdod/f51579ae8d93c8657a5564aefc2ffbca
    ELF header: https://refspecs.linuxfoundation.org/elf/gabi4+/ch4.eheader.html
    '''
    f.seek(0)
    
    try:
        ident = _read_unpacked(f, '16B')
    except struct.error:
        return None

    if ident[:4] != tuple(b'\x7fELF'):
        return None
    None.seek(struct.calcsize('HHI'), 1)
# WARNING: Decompyle incomplete


class _MuslVersion(NamedTuple):
    minor: int = '_MuslVersion'


def _parse_musl_version(output = None):
    lines = output.splitlines()()()
    if len(lines) < 2 or lines[0][:4] != 'musl':
        return None
    m = (lambda .0: pass# WARNING: Decompyle incomplete
).match('Version (\\d+)\\.(\\d+)', lines[1])
    if not m:
        return None
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(major = int(m.group(1)), minor = int(m.group(2)))

_get_musl_version = (lambda executable = None: stack = contextlib.ExitStack()f = stack.enter_context(open(executable, 'rb')))()

def platform_tags(arch = None):
    '''Generate musllinux tags compatible to the current platform.

    :param arch: Should be the part of platform tag after the ``linux_``
        prefix, e.g. ``x86_64``. The ``linux_`` prefix is assumed as a
        prerequisite for the current platform to be musllinux-compatible.

    :returns: An iterator of compatible musllinux tags.
    '''
    pass
# WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete
