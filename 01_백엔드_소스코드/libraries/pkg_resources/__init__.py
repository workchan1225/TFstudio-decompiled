# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

__doc__ = '\nPackage resource API\n--------------------\n\nA resource is a logical file contained within a package, or a logical\nsubdirectory thereof.  The package resource API expects resource names\nto have their path parts separated with ``/``, *not* whatever the local\npath separator is.  Do not use os.path operations to manipulate resource\nnames being passed into the API.\n\nThe package resource API is designed to work with normal filesystem packages,\n.egg files, and unpacked .egg files.  It can also work in a limited way with\n.zip files and with custom PEP 302 loaders that support the ``get_data()``\nmethod.\n'
import sys
import os
import io
import time
import re
import types
import zipfile
import zipimport
import warnings
import stat
import functools
import pkgutil
import operator
import platform
import collections
import plistlib
import email.parser as email
import errno
import tempfile
import textwrap
import itertools
import inspect
import ntpath
import posixpath
import importlib
from pkgutil import get_importer

try:
    import _imp
except ImportError:
    import imp as _imp


try:
    FileExistsError
except NameError:
    FileExistsError = OSError

from os import utime

try:
    from os import mkdir, rename, unlink
    WRITE_SUPPORT = True
except ImportError:
    WRITE_SUPPORT = False

from os import open as os_open
from os.path import isdir, split

try:
    from importlib.machinery import machinery as importlib_machinery
    importlib_machinery.__name__
except ImportError:
    importlib_machinery = None

from pkg_resources.extern.jaraco.text import yield_lines, drop_comment, join_continuation
from pkg_resources.extern import appdirs
from pkg_resources.extern import packaging
__import__('pkg_resources.extern.packaging.version')
__import__('pkg_resources.extern.packaging.specifiers')
__import__('pkg_resources.extern.packaging.requirements')
__import__('pkg_resources.extern.packaging.markers')
__import__('pkg_resources.extern.packaging.utils')
if sys.version_info < (3, 5):
    raise RuntimeError('Python 3.5 or later is required')
require = None
working_set = None
add_activation_listener = None
resources_stream = None
cleanup_resources = None
resource_dir = None
resource_stream = None
set_extraction_path = None
resource_isdir = None
resource_string = None
iter_entry_points = None
resource_listdir = None
resource_filename = None
resource_exists = None
_distribution_finders = None
_namespace_handlers = None
_namespace_packages = None

class PEP440Warning(RuntimeWarning):
    '''
    Used when there is an issue with a version or specifier not complying with
    PEP 440.
    '''
    pass


def parse_version(v):
    
    try:
        return packaging.version.Version(v)
    except packaging.version.InvalidVersion:
        warnings.warn(f'''{v} is an invalid version and will not be supported in a future release''', PkgResourcesDeprecationWarning)
        return 


_state_vars = { }

def _declare_state(vartype, **kw):
    globals().update(kw)
    _state_vars.update(dict.fromkeys(kw, vartype))


def __getstate__():
    state = { }
    g = globals()
    for k, v in _state_vars.items():
        state[k] = g['_sget_' + v](g[k])
        return state


def __setstate__(state):
    g = globals()
    for k, v in state.items():
        g['_sset_' + _state_vars[k]](k, g[k], v)
        return state


def _sget_dict(val):
    return val.copy()


def _sset_dict(key, ob, state):
    ob.clear()
    ob.update(state)


def _sget_object(val):
    return val.__getstate__()


def _sset_object(key, ob, state):
    ob.__setstate__(state)


_sget_none = lambda *args: pass

_sset_none = lambda *args: pass

def get_supported_platform():
    """Return this platform's maximum compatible version.

    distutils.util.get_platform() normally reports the minimum version
    of macOS that would be required to *use* extensions produced by
    distutils.  But what we want when checking compatibility is to know the
    version of macOS that we are *running*.  To allow usage of packages that
    explicitly require a newer version of macOS, we must also know the
    current version of the OS.

    If this condition occurs for any other platform with a version in its
    platform strings, this function should be extended accordingly.
    """
    plat = get_build_platform()
    m = macosVersionString.match(plat)
# WARNING: Decompyle incomplete

__all__ = [
    'require',
    'run_script',
    'get_provider',
    'get_distribution',
    'load_entry_point',
    'get_entry_map',
    'get_entry_info',
    'iter_entry_points',
    'resource_string',
    'resource_stream',
    'resource_filename',
    'resource_listdir',
    'resource_exists',
    'resource_isdir',
    'declare_namespace',
    'working_set',
    'add_activation_listener',
    'find_distributions',
    'set_extraction_path',
    'cleanup_resources',
    'get_default_cache',
    'Environment',
    'WorkingSet',
    'ResourceManager',
    'Distribution',
    'Requirement',
    'EntryPoint',
    'ResolutionError',
    'VersionConflict',
    'DistributionNotFound',
    'UnknownExtra',
    'ExtractionError',
    'PEP440Warning',
    'parse_requirements',
    'parse_version',
    'safe_name',
    'safe_version',
    'get_platform',
    'compatible_platforms',
    'yield_lines',
    'split_sections',
    'safe_extra',
    'to_filename',
    'invalid_marker',
    'evaluate_marker',
    'ensure_directory',
    'normalize_path',
    'EGG_DIST',
    'BINARY_DIST',
    'SOURCE_DIST',
    'CHECKOUT_DIST',
    'DEVELOP_DIST',
    'IMetadataProvider',
    'IResourceProvider',
    'FileMetadata',
    'PathMetadata',
    'EggMetadata',
    'EmptyProvider',
    'empty_provider',
    'NullProvider',
    'EggProvider',
    'DefaultProvider',
    'ZipProvider',
    'register_finder',
    'register_namespace_handler',
    'register_loader_type',
    'fixup_namespace_packages',
    'get_importer',
    'PkgResourcesDeprecationWarning',
    'run_main',
    'AvailableDistributions']

class ResolutionError(Exception):
    '''Abstract base for dependency resolution errors'''
    
    def __repr__(self):
        return self.__class__.__name__ + repr(self.args)



class VersionConflict(ResolutionError):
    '''
    An already-installed version conflicts with the requested version.

    Should be initialized with the installed Distribution and the requested
    Requirement.
    '''
    _template = '{self.dist} is installed but {self.req} is required'
    dist = (lambda self: self.args[0])()
    req = (lambda self: self.args[1])()
    
    def report(self):
        pass
    # WARNING: Decompyle incomplete

    
    def with_context(self, required_by):
        '''
        If required_by is non-empty, return a version of self that is a
        ContextualVersionConflict.
        '''
        if not required_by:
            return self
        args = None.args + (required_by,)
    # WARNING: Decompyle incomplete



class ContextualVersionConflict(VersionConflict):
    '''
    A VersionConflict that accepts a third parameter, the set of the
    requirements that required the installed Distribution.
    '''
    _template = VersionConflict._template + ' by {self.required_by}'
    required_by = (lambda self: self.args[2])()


class DistributionNotFound(ResolutionError):
    '''A requested distribution was not found'''
    _template = "The '{self.req}' distribution was not found and is required by {self.requirers_str}"
    req = (lambda self: self.args[0])()
    requirers = (lambda self: self.args[1])()
    requirers_str = (lambda self: if not self.requirers:
'the application'None.join(self.requirers))()
    
    def report(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        return self.report()



class UnknownExtra(ResolutionError):
    '''Distribution doesn\'t have an "extra feature" of the given name'''
    pass

_provider_factories = { }
# WARNING: Decompyle incomplete
