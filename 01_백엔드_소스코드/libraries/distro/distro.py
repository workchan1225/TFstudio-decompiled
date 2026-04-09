# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: distro.pyc (Python 3.11)

"""
The ``distro`` package (``distro`` stands for Linux Distribution) provides
information about the Linux distribution it runs on, such as a reliable
machine-readable distro ID, or version information.

It is the recommended replacement for Python's original
:py:func:`platform.linux_distribution` function, but it provides much more
functionality. An alternative implementation became necessary because Python
3.5 deprecated this function, and Python 3.8 removed it altogether. Its
predecessor function :py:func:`platform.dist` was already deprecated since
Python 2.6 and removed in Python 3.8. Still, there are many cases in which
access to OS distribution information is needed. See `Python issue 1322
<https://bugs.python.org/issue1322>`_ for more information.
"""
import argparse
import json
import logging
import os
import re
import shlex
import subprocess
import sys
import warnings
from typing import Any, Callable, Dict, Iterable, Optional, Sequence, TextIO, Tuple, Type

try:
    from typing import TypedDict
except ImportError:
    TypedDict = dict

__version__ = '1.9.0'

class VersionDict(TypedDict):
    build_number: str = 'VersionDict'


class InfoDict(TypedDict):
    codename: str = 'InfoDict'

_UNIXCONFDIR = os.environ.get('UNIXCONFDIR', '/etc')
_UNIXUSRLIBDIR = os.environ.get('UNIXUSRLIBDIR', '/usr/lib')
_OS_RELEASE_BASENAME = 'os-release'
NORMALIZED_OS_ID = {
    'ol': 'oracle',
    'opensuse-leap': 'opensuse' }
NORMALIZED_LSB_ID = {
    'enterpriseenterpriseas': 'oracle',
    'enterpriseenterpriseserver': 'oracle',
    'redhatenterpriseworkstation': 'rhel',
    'redhatenterpriseserver': 'rhel',
    'redhatenterprisecomputenode': 'rhel' }
NORMALIZED_DISTRO_ID = {
    'redhat': 'rhel' }
_DISTRO_RELEASE_CONTENT_REVERSED_PATTERN = re.compile('(?:[^)]*\\)(.*)\\()? *(?:STL )?([\\d.+\\-a-z]*\\d) *(?:esaeler *)?(.+)')
_DISTRO_RELEASE_BASENAME_PATTERN = re.compile('(\\w+)[-_](release|version)$')
_DISTRO_RELEASE_BASENAMES = [
    'SuSE-release',
    'altlinux-release',
    'arch-release',
    'base-release',
    'centos-release',
    'fedora-release',
    'gentoo-release',
    'mageia-release',
    'mandrake-release',
    'mandriva-release',
    'mandrivalinux-release',
    'manjaro-release',
    'oracle-release',
    'redhat-release',
    'rocky-release',
    'sl-release',
    'slackware-version']
_DISTRO_RELEASE_IGNORE_BASENAMES = ('debian_version', 'lsb-release', 'oem-release', _OS_RELEASE_BASENAME, 'system-release', 'plesk-release', 'iredmail-release', 'board-release', 'ec2_version')

def linux_distribution(full_distribution_name = None):
    """
    .. deprecated:: 1.6.0

        :func:`distro.linux_distribution()` is deprecated. It should only be
        used as a compatibility shim with Python's
        :py:func:`platform.linux_distribution()`. Please use :func:`distro.id`,
        :func:`distro.version` and :func:`distro.name` instead.

    Return information about the current OS distribution as a tuple
    ``(id_name, version, codename)`` with items as follows:

    * ``id_name``:  If *full_distribution_name* is false, the result of
      :func:`distro.id`. Otherwise, the result of :func:`distro.name`.

    * ``version``:  The result of :func:`distro.version`.

    * ``codename``:  The extra item (usually in parentheses) after the
      os-release version number, or the result of :func:`distro.codename`.

    The interface of this function is compatible with the original
    :py:func:`platform.linux_distribution` function, supporting a subset of
    its parameters.

    The data it returns may not exactly be the same, because it uses more data
    sources than the original function, and that may lead to different data if
    the OS distribution is not consistent across multiple data sources it
    provides (there are indeed such distributions ...).

    Another reason for differences is the fact that the :func:`distro.id`
    method normalizes the distro ID string to a reliable machine-readable value
    for a number of popular OS distributions.
    """
    warnings.warn("distro.linux_distribution() is deprecated. It should only be used as a compatibility shim with Python's platform.linux_distribution(). Please use distro.id(), distro.version() and distro.name() instead.", DeprecationWarning, stacklevel = 2)
    return _distro.linux_distribution(full_distribution_name)


def id():
    '''
    Return the distro ID of the current distribution, as a
    machine-readable string.

    For a number of OS distributions, the returned distro ID value is
    *reliable*, in the sense that it is documented and that it does not change
    across releases of the distribution.

    This package maintains the following reliable distro ID values:

    ==============  =========================================
    Distro ID       Distribution
    ==============  =========================================
    "ubuntu"        Ubuntu
    "debian"        Debian
    "rhel"          RedHat Enterprise Linux
    "centos"        CentOS
    "fedora"        Fedora
    "sles"          SUSE Linux Enterprise Server
    "opensuse"      openSUSE
    "amzn"          Amazon Linux
    "arch"          Arch Linux
    "buildroot"     Buildroot
    "cloudlinux"    CloudLinux OS
    "exherbo"       Exherbo Linux
    "gentoo"        GenToo Linux
    "ibm_powerkvm"  IBM PowerKVM
    "kvmibm"        KVM for IBM z Systems
    "linuxmint"     Linux Mint
    "mageia"        Mageia
    "mandriva"      Mandriva Linux
    "parallels"     Parallels
    "pidora"        Pidora
    "raspbian"      Raspbian
    "oracle"        Oracle Linux (and Oracle Enterprise Linux)
    "scientific"    Scientific Linux
    "slackware"     Slackware
    "xenserver"     XenServer
    "openbsd"       OpenBSD
    "netbsd"        NetBSD
    "freebsd"       FreeBSD
    "midnightbsd"   MidnightBSD
    "rocky"         Rocky Linux
    "aix"           AIX
    "guix"          Guix System
    "altlinux"      ALT Linux
    ==============  =========================================

    If you have a need to get distros for reliable IDs added into this set,
    or if you find that the :func:`distro.id` function returns a different
    distro ID for one of the listed distros, please create an issue in the
    `distro issue tracker`_.

    **Lookup hierarchy and transformations:**

    First, the ID is obtained from the following sources, in the specified
    order. The first available and non-empty value is used:

    * the value of the "ID" attribute of the os-release file,

    * the value of the "Distributor ID" attribute returned by the lsb_release
      command,

    * the first part of the file name of the distro release file,

    The so determined ID value then passes the following transformations,
    before it is returned by this method:

    * it is translated to lower case,

    * blanks (which should not be there anyway) are translated to underscores,

    * a normalization of the ID is performed, based upon
      `normalization tables`_. The purpose of this normalization is to ensure
      that the ID is as reliable as possible, even across incompatible changes
      in the OS distributions. A common reason for an incompatible change is
      the addition of an os-release file, or the addition of the lsb_release
      command, with ID values that differ from what was previously determined
      from the distro release file name.
    '''
    return _distro.id()


def name(pretty = None):
    '''
    Return the name of the current OS distribution, as a human-readable
    string.

    If *pretty* is false, the name is returned without version or codename.
    (e.g. "CentOS Linux")

    If *pretty* is true, the version and codename are appended.
    (e.g. "CentOS Linux 7.1.1503 (Core)")

    **Lookup hierarchy:**

    The name is obtained from the following sources, in the specified order.
    The first available and non-empty value is used:

    * If *pretty* is false:

      - the value of the "NAME" attribute of the os-release file,

      - the value of the "Distributor ID" attribute returned by the lsb_release
        command,

      - the value of the "<name>" field of the distro release file.

    * If *pretty* is true:

      - the value of the "PRETTY_NAME" attribute of the os-release file,

      - the value of the "Description" attribute returned by the lsb_release
        command,

      - the value of the "<name>" field of the distro release file, appended
        with the value of the pretty version ("<version_id>" and "<codename>"
        fields) of the distro release file, if available.
    '''
    return _distro.name(pretty)


def version(pretty = None, best = None):
    '''
    Return the version of the current OS distribution, as a human-readable
    string.

    If *pretty* is false, the version is returned without codename (e.g.
    "7.0").

    If *pretty* is true, the codename in parenthesis is appended, if the
    codename is non-empty (e.g. "7.0 (Maipo)").

    Some distributions provide version numbers with different precisions in
    the different sources of distribution information. Examining the different
    sources in a fixed priority order does not always yield the most precise
    version (e.g. for Debian 8.2, or CentOS 7.1).

    Some other distributions may not provide this kind of information. In these
    cases, an empty string would be returned. This behavior can be observed
    with rolling releases distributions (e.g. Arch Linux).

    The *best* parameter can be used to control the approach for the returned
    version:

    If *best* is false, the first non-empty version number in priority order of
    the examined sources is returned.

    If *best* is true, the most precise version number out of all examined
    sources is returned.

    **Lookup hierarchy:**

    In all cases, the version number is obtained from the following sources.
    If *best* is false, this order represents the priority order:

    * the value of the "VERSION_ID" attribute of the os-release file,
    * the value of the "Release" attribute returned by the lsb_release
      command,
    * the version number parsed from the "<version_id>" field of the first line
      of the distro release file,
    * the version number parsed from the "PRETTY_NAME" attribute of the
      os-release file, if it follows the format of the distro release files.
    * the version number parsed from the "Description" attribute returned by
      the lsb_release command, if it follows the format of the distro release
      files.
    '''
    return _distro.version(pretty, best)


def version_parts(best = None):
    '''
    Return the version of the current OS distribution as a tuple
    ``(major, minor, build_number)`` with items as follows:

    * ``major``:  The result of :func:`distro.major_version`.

    * ``minor``:  The result of :func:`distro.minor_version`.

    * ``build_number``:  The result of :func:`distro.build_number`.

    For a description of the *best* parameter, see the :func:`distro.version`
    method.
    '''
    return _distro.version_parts(best)


def major_version(best = None):
    '''
    Return the major version of the current OS distribution, as a string,
    if provided.
    Otherwise, the empty string is returned. The major version is the first
    part of the dot-separated version string.

    For a description of the *best* parameter, see the :func:`distro.version`
    method.
    '''
    return _distro.major_version(best)


def minor_version(best = None):
    '''
    Return the minor version of the current OS distribution, as a string,
    if provided.
    Otherwise, the empty string is returned. The minor version is the second
    part of the dot-separated version string.

    For a description of the *best* parameter, see the :func:`distro.version`
    method.
    '''
    return _distro.minor_version(best)


def build_number(best = None):
    '''
    Return the build number of the current OS distribution, as a string,
    if provided.
    Otherwise, the empty string is returned. The build number is the third part
    of the dot-separated version string.

    For a description of the *best* parameter, see the :func:`distro.version`
    method.
    '''
    return _distro.build_number(best)


def like():
    '''
    Return a space-separated list of distro IDs of distributions that are
    closely related to the current OS distribution in regards to packaging
    and programming interfaces, for example distributions the current
    distribution is a derivative from.

    **Lookup hierarchy:**

    This information item is only provided by the os-release file.
    For details, see the description of the "ID_LIKE" attribute in the
    `os-release man page
    <http://www.freedesktop.org/software/systemd/man/os-release.html>`_.
    '''
    return _distro.like()


def codename():
    '''
    Return the codename for the release of the current OS distribution,
    as a string.

    If the distribution does not have a codename, an empty string is returned.

    Note that the returned codename is not always really a codename. For
    example, openSUSE returns "x86_64". This function does not handle such
    cases in any special way and just returns the string it finds, if any.

    **Lookup hierarchy:**

    * the codename within the "VERSION" attribute of the os-release file, if
      provided,

    * the value of the "Codename" attribute returned by the lsb_release
      command,

    * the value of the "<codename>" field of the distro release file.
    '''
    return _distro.codename()


def info(pretty = None, best = None):
    """
    Return certain machine-readable information items about the current OS
    distribution in a dictionary, as shown in the following example:

    .. sourcecode:: python

        {
            'id': 'rhel',
            'version': '7.0',
            'version_parts': {
                'major': '7',
                'minor': '0',
                'build_number': ''
            },
            'like': 'fedora',
            'codename': 'Maipo'
        }

    The dictionary structure and keys are always the same, regardless of which
    information items are available in the underlying data sources. The values
    for the various keys are as follows:

    * ``id``:  The result of :func:`distro.id`.

    * ``version``:  The result of :func:`distro.version`.

    * ``version_parts -> major``:  The result of :func:`distro.major_version`.

    * ``version_parts -> minor``:  The result of :func:`distro.minor_version`.

    * ``version_parts -> build_number``:  The result of
      :func:`distro.build_number`.

    * ``like``:  The result of :func:`distro.like`.

    * ``codename``:  The result of :func:`distro.codename`.

    For a description of the *pretty* and *best* parameters, see the
    :func:`distro.version` method.
    """
    return _distro.info(pretty, best)


def os_release_info():
    '''
    Return a dictionary containing key-value pairs for the information items
    from the os-release file data source of the current OS distribution.

    See `os-release file`_ for details about these information items.
    '''
    return _distro.os_release_info()


def lsb_release_info():
    '''
    Return a dictionary containing key-value pairs for the information items
    from the lsb_release command data source of the current OS distribution.

    See `lsb_release command output`_ for details about these information
    items.
    '''
    return _distro.lsb_release_info()


def distro_release_info():
    '''
    Return a dictionary containing key-value pairs for the information items
    from the distro release file data source of the current OS distribution.

    See `distro release file`_ for details about these information items.
    '''
    return _distro.distro_release_info()


def uname_info():
    '''
    Return a dictionary containing key-value pairs for the information items
    from the distro release file data source of the current OS distribution.
    '''
    return _distro.uname_info()


def os_release_attr(attribute = None):
    '''
    Return a single named information item from the os-release file data source
    of the current OS distribution.

    Parameters:

    * ``attribute`` (string): Key of the information item.

    Returns:

    * (string): Value of the information item, if the item exists.
      The empty string, if the item does not exist.

    See `os-release file`_ for details about these information items.
    '''
    return _distro.os_release_attr(attribute)


def lsb_release_attr(attribute = None):
    '''
    Return a single named information item from the lsb_release command output
    data source of the current OS distribution.

    Parameters:

    * ``attribute`` (string): Key of the information item.

    Returns:

    * (string): Value of the information item, if the item exists.
      The empty string, if the item does not exist.

    See `lsb_release command output`_ for details about these information
    items.
    '''
    return _distro.lsb_release_attr(attribute)


def distro_release_attr(attribute = None):
    '''
    Return a single named information item from the distro release file
    data source of the current OS distribution.

    Parameters:

    * ``attribute`` (string): Key of the information item.

    Returns:

    * (string): Value of the information item, if the item exists.
      The empty string, if the item does not exist.

    See `distro release file`_ for details about these information items.
    '''
    return _distro.distro_release_attr(attribute)


def uname_attr(attribute = None):
    '''
    Return a single named information item from the distro release file
    data source of the current OS distribution.

    Parameters:

    * ``attribute`` (string): Key of the information item.

    Returns:

    * (string): Value of the information item, if the item exists.
                The empty string, if the item does not exist.
    '''
    return _distro.uname_attr(attribute)


try:
    from functools import cached_property
except ImportError:
    
    class cached_property:
        '''A version of @property which caches the value.  On access, it calls the
        underlying function and sets the value in `__dict__` so future accesses
        will not re-call the property.
        '''
        
        def __init__(self = None, f = None):
            self._fname = f.__name__
            self._f = f

        
        def __get__(self = None, obj = None, owner = None):
            pass
        # WARNING: Decompyle incomplete




class LinuxDistribution:
    '''
    Provides information about a OS distribution.

    This package creates a private module-global instance of this class with
    default initialization arguments, that is used by the
    `consolidated accessor functions`_ and `single source accessor functions`_.
    By using default initialization arguments, that module-global instance
    returns data about the current OS distribution (i.e. the distro this
    package runs on).

    Normally, it is not necessary to create additional instances of this class.
    However, in situations where control is needed over the exact data sources
    that are used, instances of this class can be created with a specific
    distro release file, or a specific os-release file, or without invoking the
    lsb_release command.
    '''
    
    def __init__(self, include_lsb, os_release_file = None, distro_release_file = None, include_uname = None, root_dir = (None, '', '', None, None, None), include_oslevel = ('include_lsb', Optional[bool], 'os_release_file', str, 'distro_release_file', str, 'include_uname', Optional[bool], 'root_dir', Optional[str], 'include_oslevel', Optional[bool], 'return', None)):
        '''
        The initialization method of this class gathers information from the
        available data sources, and stores that in private instance attributes.
        Subsequent access to the information items uses these private instance
        attributes, so that the data sources are read only once.

        Parameters:

        * ``include_lsb`` (bool): Controls whether the
          `lsb_release command output`_ is included as a data source.

          If the lsb_release command is not available in the program execution
          path, the data source for the lsb_release command will be empty.

        * ``os_release_file`` (string): The path name of the
          `os-release file`_ that is to be used as a data source.

          An empty string (the default) will cause the default path name to
          be used (see `os-release file`_ for details).

          If the specified or defaulted os-release file does not exist, the
          data source for the os-release file will be empty.

        * ``distro_release_file`` (string): The path name of the
          `distro release file`_ that is to be used as a data source.

          An empty string (the default) will cause a default search algorithm
          to be used (see `distro release file`_ for details).

          If the specified distro release file does not exist, or if no default
          distro release file can be found, the data source for the distro
          release file will be empty.

        * ``include_uname`` (bool): Controls whether uname command output is
          included as a data source. If the uname command is not available in
          the program execution path the data source for the uname command will
          be empty.

        * ``root_dir`` (string): The absolute path to the root directory to use
          to find distro-related information files. Note that ``include_*``
          parameters must not be enabled in combination with ``root_dir``.

        * ``include_oslevel`` (bool): Controls whether (AIX) oslevel command
          output is included as a data source. If the oslevel command is not
          available in the program execution path the data source will be
          empty.

        Public instance attributes:

        * ``os_release_file`` (string): The path name of the
          `os-release file`_ that is actually used as a data source. The
          empty string if no distro release file is used as a data source.

        * ``distro_release_file`` (string): The path name of the
          `distro release file`_ that is actually used as a data source. The
          empty string if no distro release file is used as a data source.

        * ``include_lsb`` (bool): The result of the ``include_lsb`` parameter.
          This controls whether the lsb information will be loaded.

        * ``include_uname`` (bool): The result of the ``include_uname``
          parameter. This controls whether the uname information will
          be loaded.

        * ``include_oslevel`` (bool): The result of the ``include_oslevel``
          parameter. This controls whether (AIX) oslevel information will be
          loaded.

        * ``root_dir`` (string): The result of the ``root_dir`` parameter.
          The absolute path to the root directory to use to find distro-related
          information files.

        Raises:

        * :py:exc:`ValueError`: Initialization parameters combination is not
           supported.

        * :py:exc:`OSError`: Some I/O issue with an os-release file or distro
          release file.

        * :py:exc:`UnicodeError`: A data source has unexpected characters or
          uses an unexpected encoding.
        '''
        self.root_dir = root_dir
        self.etc_dir = os.path.join(root_dir, 'etc') if root_dir else _UNIXCONFDIR
        self.usr_lib_dir = os.path.join(root_dir, 'usr/lib') if root_dir else _UNIXUSRLIBDIR
        if os_release_file:
            self.os_release_file = os_release_file
        else:
            etc_dir_os_release_file = os.path.join(self.etc_dir, _OS_RELEASE_BASENAME)
            usr_lib_os_release_file = os.path.join(self.usr_lib_dir, _OS_RELEASE_BASENAME)
            if not os.path.isfile(etc_dir_os_release_file) or os.path.isfile(usr_lib_os_release_file):
                self.os_release_file = etc_dir_os_release_file
            else:
                self.os_release_file = usr_lib_os_release_file
        if not distro_release_file:
            self.distro_release_file = ''
            is_root_dir_defined = root_dir is not None
            if is_root_dir_defined:
                if include_lsb and include_uname or include_oslevel:
                    raise ValueError('Including subprocess data sources from specific root_dir is disallowed to prevent false information')
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        '''Return repr of all info'''
        return 'LinuxDistribution(os_release_file={self.os_release_file!r}, distro_release_file={self.distro_release_file!r}, include_lsb={self.include_lsb!r}, include_uname={self.include_uname!r}, include_oslevel={self.include_oslevel!r}, root_dir={self.root_dir!r}, _os_release_info={self._os_release_info!r}, _lsb_release_info={self._lsb_release_info!r}, _distro_release_info={self._distro_release_info!r}, _uname_info={self._uname_info!r}, _oslevel_info={self._oslevel_info!r})'.format(self = self)

    
    def linux_distribution(self = None, full_distribution_name = None):
