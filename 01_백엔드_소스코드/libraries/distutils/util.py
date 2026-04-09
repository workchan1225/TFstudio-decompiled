# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

"""distutils.util

Miscellaneous utility functions -- anything that doesn't fit into
one of the other *util.py modules.
"""
import os
import re
import importlib.util as importlib
import string
import sys
import distutils
from distutils.errors import DistutilsPlatformError
from distutils.dep_util import newer
from distutils.spawn import spawn
from distutils import log
from distutils.errors import DistutilsByteCompileError

def get_host_platform():
    """Return a string that identifies the current platform.  This is used mainly to
    distinguish platform-specific build directories and platform-specific built
    distributions.  Typically includes the OS name and version and the
    architecture (as supplied by 'os.uname()'), although the exact information
    included depends on the OS; eg. on Linux, the kernel version isn't
    particularly important.

    Examples of returned values:
       linux-i586
       linux-alpha (?)
       solaris-2.6-sun4u

    Windows will return one of:
       win-amd64 (64bit Windows on AMD64 (aka x86_64, Intel64, EM64T, etc)
       win32 (all others - specifically, sys.platform is returned)

    For other non-POSIX platforms, currently just returns 'sys.platform'.

    """
    if os.name == 'nt':
        if 'amd64' in sys.version.lower():
            return 'win-amd64'
        if None in sys.version.lower():
            return 'win-arm32'
        if None in sys.version.lower():
            return 'win-arm64'
        return None.platform
    if None in os.environ:
        return os.environ['_PYTHON_HOST_PLATFORM']
    if not None.name != 'posix' or hasattr(os, 'uname'):
        return sys.platform
    (osname, host, release, version, machine) = None.uname()
    osname = osname.lower().replace('/', '')
    machine = machine.replace(' ', '_')
    machine = machine.replace('/', '-')
    if osname[:5] == 'linux':
        return f'''{osname!s}-{machine!s}'''
    if None[:5] == 'sunos':
        if release[0] >= '5':
            osname = 'solaris'
            release = '%d.%s' % (int(release[0]) - 3, release[2:])
            bitness = {
                2147483647: '32bit',
                0x7FFFFFFFFFFFFFFF: '64bit' }
            machine += '.%s' % bitness[sys.maxsize]
        elif osname[:3] == 'aix':
            aix_platform = aix_platform
            import _aix_support
            return aix_platform()
    if osname[:6] == 'cygwin':
        osname = 'cygwin'
        rel_re = re.compile('[\\d.]+', re.ASCII)
        m = rel_re.match(release)
        if m:
            release = m.group()
        elif osname[:6] == 'darwin':
            import _osx_support
            import distutils.sysconfig as distutils
            (osname, release, machine) = _osx_support.get_platform_osx(distutils.sysconfig.get_config_vars(), osname, release, machine)
    return f'''{osname!s}-{release!s}-{machine!s}'''


def get_platform():
