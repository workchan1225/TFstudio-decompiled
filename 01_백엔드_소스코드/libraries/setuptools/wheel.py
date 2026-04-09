# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wheel.pyc (Python 3.11)

'''Wheels support.'''
import email
import itertools
import os
import posixpath
import re
import zipfile
import contextlib
from distutils.util import get_platform
import pkg_resources
import setuptools
from pkg_resources import parse_version
from setuptools.extern.packaging.tags import sys_tags
from setuptools.extern.packaging.utils import canonicalize_name
from setuptools.command.egg_info import write_requirements
from setuptools.archive_util import _unpack_zipfile_obj
WHEEL_NAME = re.compile('^(?P<project_name>.+?)-(?P<version>\\d.*?)\n    ((-(?P<build>\\d.*?))?-(?P<py_version>.+?)-(?P<abi>.+?)-(?P<platform>.+?)\n    )\\.whl$', re.VERBOSE).match
NAMESPACE_PACKAGE_INIT = "__import__('pkg_resources').declare_namespace(__name__)\n"

def unpack(src_dir, dst_dir):
    '''Move everything under `src_dir` to `dst_dir`, and delete the former.'''
    pass
# WARNING: Decompyle incomplete

disable_info_traces = (lambda : pass# WARNING: Decompyle incomplete
)()

class Wheel:
    
    def __init__(self, filename):
        match = WHEEL_NAME(os.path.basename(filename))
    # WARNING: Decompyle incomplete

    
    def tags(self):
        '''List tags (py_version, abi, platform) supported by this wheel.'''
        return itertools.product(self.py_version.split('.'), self.abi.split('.'), self.platform.split('.'))

    
    def is_compatible(self):
        '''Is the wheel is compatible with the current platform?'''
        pass
    # WARNING: Decompyle incomplete

    
    def egg_name(self):
        return pkg_resources.Distribution(project_name = self.project_name, version = self.version, platform = None if self.platform == 'any' else get_platform()).egg_name() + '.egg'

    
    def get_dist_info(self, zf):
        for member in zf.namelist():
            dirname = posixpath.dirname(member)
            if dirname.endswith('.dist-info') and canonicalize_name(dirname).startswith(canonicalize_name(self.project_name)):
                
                return None, dirname
            raise ValueError('unsupported wheel format. .dist-info not found')

    
    def install_as_egg(self, destination_eggdir):
        '''Install wheel as an egg directory.'''
        zf = zipfile.ZipFile(self.filename)
        self._install_as_egg(destination_eggdir, zf)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _install_as_egg(self, destination_eggdir, zf):
        dist_basename = f'''{self.project_name!s}-{self.version!s}'''
        dist_info = self.get_dist_info(zf)
        dist_data = '%s.data' % dist_basename
        egg_info = os.path.join(destination_eggdir, 'EGG-INFO')
        self._convert_metadata(zf, destination_eggdir, dist_info, egg_info)
        self._move_data_entries(destination_eggdir, dist_data)
        self._fix_namespace_packages(egg_info, destination_eggdir)

    _convert_metadata = (lambda zf, destination_eggdir, dist_info, egg_info: pass# WARNING: Decompyle incomplete
)()
    _move_data_entries = (lambda destination_eggdir, dist_data: pass# WARNING: Decompyle incomplete
)()
    _fix_namespace_packages = (lambda egg_info, destination_eggdir: namespace_packages = os.path.join(egg_info, 'namespace_packages.txt')if os.path.exists(namespace_packages):
fp = open(namespace_packages)namespace_packages = fp.read().split()None(None, None)else:
with None:
if not None:
pass# WARNING: Decompyle incomplete
)()
