# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dist.pyc (Python 3.11)

__all__ = [
    'Distribution']
import io
import sys
import re
import os
import warnings
import numbers
import distutils.log as distutils
import distutils.core as distutils
import distutils.cmd as distutils
import distutils.dist as distutils
import distutils.command as distutils
from distutils.util import strtobool
from distutils.debug import DEBUG
from distutils.fancy_getopt import translate_longopt
from glob import iglob
import itertools
import textwrap
from typing import List, Optional, TYPE_CHECKING
from pathlib import Path
from collections import defaultdict
from email import message_from_file
from distutils.errors import DistutilsOptionError, DistutilsSetupError
from distutils.util import rfc822_escape
from setuptools.extern import packaging
from setuptools.extern import ordered_set
from setuptools.extern.more_itertools import unique_everseen, partition
from _importlib import metadata
from  import SetuptoolsDeprecationWarning
import setuptools
import setuptools.command as setuptools
from setuptools import windows_support
from setuptools.monkey import get_unpatched
from setuptools.config import setupcfg, pyprojecttoml
from setuptools.discovery import ConfigDiscovery
import pkg_resources
from setuptools.extern.packaging import version
from  import _reqs
from  import _entry_points
if TYPE_CHECKING:
    from email.message import Message
__import__('setuptools.extern.packaging.specifiers')
__import__('setuptools.extern.packaging.version')

def _get_unpatched(cls):
    warnings.warn('Do not call this function', DistDeprecationWarning)
    return get_unpatched(cls)


def get_metadata_version(self):
    mv = getattr(self, 'metadata_version', None)
# WARNING: Decompyle incomplete


def rfc822_unescape(content = None):
    '''Reverse RFC-822 escaping by removing leading whitespaces from content.'''
    lines = content.splitlines()
    if len(lines) == 1:
        return lines[0].lstrip()
    return None.join((lines[0].lstrip(), textwrap.dedent('\n'.join(lines[1:]))))


def _read_field_from_msg(msg = None, field = None):
    '''Read Message header field.'''
    value = msg[field]
    if value == 'UNKNOWN':
        return None


def _read_field_unescaped_from_msg(msg = None, field = None):
    '''Read Message header field and apply rfc822_unescape.'''
    value = _read_field_from_msg(msg, field)
# WARNING: Decompyle incomplete


def _read_list_from_msg(msg = None, field = None):
    '''Read Message header field and return all results as list.'''
    values = msg.get_all(field, None)
    if values == []:
        return None


def _read_payload_from_msg(msg = None):
    value = msg.get_payload().strip()
    if not value == 'UNKNOWN' or value:
        return None


def read_pkg_file(self, file):
    '''Reads the metadata values from a file object.'''
    msg = message_from_file(file)
    self.metadata_version = version.Version(msg['metadata-version'])
    self.name = _read_field_from_msg(msg, 'name')
    self.version = _read_field_from_msg(msg, 'version')
    self.description = _read_field_from_msg(msg, 'summary')
    self.author = _read_field_from_msg(msg, 'author')
    self.maintainer = None
    self.author_email = _read_field_from_msg(msg, 'author-email')
    self.maintainer_email = None
    self.url = _read_field_from_msg(msg, 'home-page')
    self.download_url = _read_field_from_msg(msg, 'download-url')
    self.license = _read_field_unescaped_from_msg(msg, 'license')
    self.long_description = _read_field_unescaped_from_msg(msg, 'description')
# WARNING: Decompyle incomplete


def single_line(val):
    '''
    Quick and dirty validation for Summary pypa/setuptools#1390.
    '''
    if '\n' in val:
        warnings.warn('newlines not allowed and will break in the future')
        val = val.strip().split('\n')[0]
    return val


def write_pkg_file(self, file):
    '''Write the PKG-INFO format data to a file object.'''
    pass
# WARNING: Decompyle incomplete

sequence = (tuple, list)

def check_importable(dist, attr, value):
    pass
# WARNING: Decompyle incomplete


def assert_string_list(dist, attr, value):
    '''Verify that value is a string list'''
    pass
# WARNING: Decompyle incomplete


def check_nsp(dist, attr, value):
    '''Verify that namespace packages are valid'''
    ns_packages = value
    assert_string_list(dist, attr, ns_packages)
    for nsp in ns_packages:
        if not dist.has_contents_for(nsp):
            raise DistutilsSetupError('Distribution contains no modules or packages for ' + 'namespace package %r' % nsp)
        (parent, sep, child) = nsp.rpartition('.')
        if parent and parent not in ns_packages:
            distutils.log.warn('WARNING: %r is declared as a package namespace, but %r is not: please correct this in setup.py', nsp, parent)
        msg = 'The namespace_packages parameter is deprecated, consider using implicit namespaces instead (PEP 420).'
        warnings.warn(msg, SetuptoolsDeprecationWarning)
        return None


def check_extras(dist, attr, value):
    '''Verify that extras_require mapping is valid'''
    
    try:
        list(itertools.starmap(_check_extra, value.items()))
        return None
    except (TypeError, ValueError, AttributeError):
        e = None
        raise DistutilsSetupError("'extras_require' must be a dictionary whose values are strings or lists of strings containing valid project/version requirement specifiers."), e
        e = None
        del e



def _check_extra(extra, reqs):
    (name, sep, marker) = extra.partition(':')
    if marker and pkg_resources.invalid_marker(marker):
        raise DistutilsSetupError('Invalid environment marker: ' + marker)
    list(_reqs.parse(reqs))


def assert_bool(dist, attr, value):
    '''Verify that value is True, False, 0, or 1'''
    if bool(value) != value:
        tmpl = '{attr!r} must be a boolean value (got {value!r})'
        raise DistutilsSetupError(tmpl.format(attr = attr, value = value))


def invalid_unless_false(dist, attr, value):
    if not value:
        warnings.warn(f'''{attr} is ignored.''', DistDeprecationWarning)
        return None
    raise None(f'''{attr} is invalid.''')


def check_requirements(dist, attr, value):
    '''Verify that install_requires is a valid requirements list'''
    
    try:
        list(_reqs.parse(value))
        if isinstance(value, (dict, set)):
            raise TypeError('Unordered types are not allowed')
        return None
    except (TypeError, ValueError):
        error = None
        tmpl = '{attr!r} must be a string or list of strings containing valid project/version requirement specifiers; {error}'
        raise DistutilsSetupError(tmpl.format(attr = attr, error = error)), error
        error = None
        del error



def check_specifier(dist, attr, value):
    '''Verify that value is a valid version specifier'''
    
    try:
        packaging.specifiers.SpecifierSet(value)
        return None
    except (packaging.specifiers.InvalidSpecifier, AttributeError):
        error = None
        tmpl = '{attr!r} must be a string containing valid version specifiers; {error}'
        raise DistutilsSetupError(tmpl.format(attr = attr, error = error)), error
        error = None
        del error



def check_entry_points(dist, attr, value):
    '''Verify that entry_points map is parseable'''
    
    try:
        _entry_points.load(value)
        return None
    except Exception:
        e = None
        raise DistutilsSetupError(e), e
        e = None
        del e



def check_test_suite(dist, attr, value):
    if not isinstance(value, str):
        raise DistutilsSetupError('test_suite must be a string')


def check_package_data(dist, attr, value):
    '''Verify that value is a dictionary of package names to glob lists'''
    if not isinstance(value, dict):
        raise DistutilsSetupError('{!r} must be a dictionary mapping package names to lists of string wildcard patterns'.format(attr))
    for k, v in value.items():
        if not isinstance(k, str):
            raise DistutilsSetupError('keys of {!r} dict must be strings (got {!r})'.format(attr, k))
        assert_string_list(dist, 'values of {!r} dict'.format(attr), v)
        return None


def check_packages(dist, attr, value):
    for pkgname in value:
        if not re.match('\\w+(\\.\\w+)*', pkgname):
            distutils.log.warn('WARNING: %r not a valid package name; please use only .-separated package names in setup.py', pkgname)
        return None

_Distribution = get_unpatched(distutils.core.Distribution)

class Distribution(_Distribution):
    pass
# WARNING: Decompyle incomplete


class DistDeprecationWarning(SetuptoolsDeprecationWarning):
    '''Class for warning about deprecations in dist in
    setuptools. Not ignored by default, unlike DeprecationWarning.'''
    pass
