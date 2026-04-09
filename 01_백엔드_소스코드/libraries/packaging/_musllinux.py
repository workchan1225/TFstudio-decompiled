# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _musllinux.pyc (Python 3.11)

__doc__ = 'PEP 656 support.\n\nThis module implements logic to detect if the currently running Python is\nlinked against musl, and what musl version is used.\n'
from __future__ import annotations
import functools
import re
import subprocess
import sys
from typing import Iterator, NamedTuple, Sequence
from _elffile import ELFFile

class _MuslVersion(NamedTuple):
    minor: 'int' = '_MuslVersion'


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

_get_musl_version = (lambda executable = None: pass# WARNING: Decompyle incomplete
)()

def platform_tags(archs = None):
    '''Generate musllinux tags compatible to the current platform.

    :param archs: Sequence of compatible architectures.
        The first one shall be the closest to the actual architecture and be the part of
        platform tag after the ``linux_`` prefix, e.g. ``x86_64``.
        The ``linux_`` prefix is assumed as a prerequisite for the current platform to
        be musllinux-compatible.

    :returns: An iterator of compatible musllinux tags.
    '''
    pass
# WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete
