# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

"""Extensions to the 'distutils' for large or complex distributions"""
import functools
import os
import re
import warnings
import _distutils_hack.override as _distutils_hack
import distutils.core as distutils
from distutils.errors import DistutilsOptionError
from distutils.util import convert_path as _convert_path
from _deprecation_warning import SetuptoolsDeprecationWarning
import setuptools.version as setuptools
from setuptools.extension import Extension
from setuptools.dist import Distribution
from setuptools.depends import Require
from setuptools.discovery import PackageFinder, PEP420PackageFinder
from  import monkey
from  import logging
__all__ = [
    'setup',
    'Distribution',
    'Command',
    'Extension',
    'Require',
    'SetuptoolsDeprecationWarning',
    'find_packages',
    'find_namespace_packages']
__version__ = setuptools.version.__version__
bootstrap_install_from = None
find_packages = PackageFinder.find
find_namespace_packages = PEP420PackageFinder.find

def _install_setup_requires(attrs):
    
    class MinimalDistribution(distutils.core.Distribution):
        pass
    # WARNING: Decompyle incomplete

    dist = MinimalDistribution(attrs)
    dist.parse_config_files(ignore_option_errors = True)
    if dist.setup_requires:
        dist.fetch_build_eggs(dist.setup_requires)
        return None


def setup(**attrs):
    logging.configure()
    _install_setup_requires(attrs)
# WARNING: Decompyle incomplete

setup.__doc__ = distutils.core.setup.__doc__
_Command = monkey.get_unpatched(distutils.core.Command)

class Command(_Command):
    pass
# WARNING: Decompyle incomplete


def _find_all_simple(path):
    """
    Find all files under 'path'
    """
    results = os.walk(path, followlinks = True)()
    return filter(os.path.isfile, results)


def findall(dir = (os.curdir,)):
    """
    Find all files under 'dir' and return the list of full filenames.
    Unless dir is '.', return full filenames with dir prepended.
    """
    files = _find_all_simple(dir)
    if dir == os.curdir:
        make_rel = functools.partial(os.path.relpath, start = dir)
        files = map(make_rel, files)
    return list(files)

convert_path = (lambda pathname: cleandoc = cleandocimport inspectmsg = '\n    The function `convert_path` is considered internal and not part of the public API.\n    Its direct usage by 3rd-party packages is considered deprecated and the function\n    may be removed in the future.\n    'warnings.warn(cleandoc(msg), SetuptoolsDeprecationWarning)_convert_path(pathname))()

class sic(str):
    '''Treat this string as-is (https://en.wikipedia.org/wiki/Sic)'''
    pass

monkey.patch_all()
