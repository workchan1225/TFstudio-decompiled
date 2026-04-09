# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: egg_info.pyc (Python 3.11)

"""setuptools.command.egg_info

Create a distribution's .egg-info directory and contents"""
from distutils.filelist import FileList as _FileList
from distutils.errors import DistutilsInternalError
from distutils.util import convert_path
from distutils import log
import distutils.errors as distutils
import distutils.filelist as distutils
import functools
import os
import re
import sys
import io
import warnings
import time
import collections
from _importlib import metadata
from  import _entry_points
from setuptools import Command
from setuptools.command.sdist import sdist
from setuptools.command.sdist import walk_revctrl
from setuptools.command.setopt import edit_config
from setuptools.command import bdist_egg
from pkg_resources import Requirement, safe_name, parse_version, safe_version, to_filename
from setuptools.unicode_utils import unicode_utils
from setuptools.glob import glob
from setuptools.extern import packaging
from setuptools.extern.jaraco.text import yield_lines
from setuptools import SetuptoolsDeprecationWarning

def translate_pattern(glob):
    """
    Translate a file path glob like '*.txt' in to a regular expression.
    This differs from fnmatch.translate which allows wildcards to match
    directory separators. It also knows about '**/' which matches any number of
    directories.
    """
    pat = ''
    chunks = glob.split(os.path.sep)
    sep = re.escape(os.sep)
    valid_char = f'''[^{sep!s}]'''
# WARNING: Decompyle incomplete


class InfoCommon:
    tag_build = None
    tag_date = None
    name = (lambda self: safe_name(self.distribution.get_name()))()
    
    def tagged_version(self):
        return safe_version(self._maybe_tag(self.distribution.get_version()))

    
    def _maybe_tag(self, version):
        '''
        egg_info may be called more than once for a distribution,
        in which case the version string already contains all tags.
        '''
        return version if self.vtags and self._already_tagged(version) else version + self.vtags

    
    def _already_tagged(self = None, version = None):
        if not version.endswith(self.vtags):
            pass
        return version.endswith(self._safe_tags())

    
    def _safe_tags(self = None):
        return safe_version(f'''0{self.vtags}''')[1:]

    
    def tags(self = None):
        version = ''
        if self.tag_build:
            version += self.tag_build
        if self.tag_date:
            version += time.strftime('-%Y%m%d')
        return version

    vtags = property(tags)


class egg_info(Command, InfoCommon):
    description = "create a distribution's .egg-info directory"
    user_options = [
        ('egg-base=', 'e', 'directory containing .egg-info directories (default: top of the source tree)'),
        ('tag-date', 'd', 'Add date stamp (e.g. 20050528) to version number'),
        ('tag-build=', 'b', 'Specify explicit tag to add to version number'),
        ('no-date', 'D', "Don't include date stamp [default]")]
    boolean_options = [
        'tag-date']
    negative_opt = {
        'no-date': 'tag-date' }
    
    def initialize_options(self):
        self.egg_base = None
        self.egg_name = None
        self.egg_info = None
        self.egg_version = None
        self.broken_egg_info = False
        self.ignore_egg_info_in_manifest = False

    tag_svn_revision = (lambda self: pass)()
    tag_svn_revision = (lambda self, value: pass)()
    
    def save_version_info(self, filename):
        '''
        Materialize the value of date into the
        build tag. Install build keys in a deterministic order
        to avoid arbitrary reordering on subsequent builds.
        '''
        egg_info = collections.OrderedDict()
        egg_info['tag_build'] = self.tags()
        egg_info['tag_date'] = 0
        edit_config(filename, dict(egg_info = egg_info))

    
    def finalize_options(self):
        self.egg_name = self.name
        self.egg_version = self.tagged_version()
        parsed_version = parse_version(self.egg_version)
        
        try:
            is_version = isinstance(parsed_version, packaging.version.Version)
            spec = '%s==%s' if is_version else '%s===%s'
            Requirement(spec % (self.egg_name, self.egg_version))
        except ValueError:
            e = None
            raise distutils.errors.DistutilsOptionError(f'''Invalid distribution name or version syntax: {self.egg_name!s}-{self.egg_version!s}'''), e
            e = None
            del e

    # WARNING: Decompyle incomplete

    
    def write_or_delete_file(self, what, filename, data, force = (False,)):
        '''Write `data` to `filename` or delete if empty

        If `data` is non-empty, this routine is the same as ``write_file()``.
        If `data` is empty but not ``None``, this is the same as calling
        ``delete_file(filename)`.  If `data` is ``None``, then this is a no-op
        unless `filename` exists, in which case a warning is issued about the
        orphaned file (if `force` is false), or deleted (if `force` is true).
        '''
        if data:
            self.write_file(what, filename, data)
            return None
    # WARNING: Decompyle incomplete

    
    def write_file(self, what, filename, data):
        '''Write `data` to `filename` (if not a dry run) after announcing it

        `what` is used in a log message to identify what is being written
        to the file.
        '''
        log.info('writing %s to %s', what, filename)
        data = data.encode('utf-8')
        if not self.dry_run:
            f = open(filename, 'wb')
            f.write(data)
            f.close()
            return None

    
    def delete_file(self, filename):
        '''Delete `filename` (if not a dry run) after announcing it'''
        log.info('deleting %s', filename)
        if not self.dry_run:
            os.unlink(filename)
            return None

    
    def run(self):
        self.mkpath(self.egg_info)
        os.utime(self.egg_info, None)
        for ep in metadata.entry_points(group = 'egg_info.writers'):
            writer = ep.load()
            writer(self, ep.name, os.path.join(self.egg_info, ep.name))
            nl = os.path.join(self.egg_info, 'native_libs.txt')
            if os.path.exists(nl):
                self.delete_file(nl)
        self.find_sources()

    
    def find_sources(self):
        '''Generate SOURCES.txt manifest file'''
        manifest_filename = os.path.join(self.egg_info, 'SOURCES.txt')
        mm = manifest_maker(self.distribution)
        mm.ignore_egg_info_dir = self.ignore_egg_info_in_manifest
        mm.manifest = manifest_filename
        mm.run()
        self.filelist = mm.filelist

    
    def check_broken_egg_info(self):
        bei = self.egg_name + '.egg-info'
        if self.egg_base != os.curdir:
            bei = os.path.join(self.egg_base, bei)
        if os.path.exists(bei):
            log.warn('------------------------------------------------------------------------------\nNote: Your current .egg-info directory has a \'-\' in its name;\nthis will not work correctly with "setup.py develop".\n\nPlease rename %s to %s to correct this problem.\n------------------------------------------------------------------------------', bei, self.egg_info)
            self.broken_egg_info = self.egg_info
            self.egg_info = bei
            return None



class FileList(_FileList):
    pass
# WARNING: Decompyle incomplete


class manifest_maker(sdist):
    template = 'MANIFEST.in'
    
    def initialize_options(self):
        self.use_defaults = 1
        self.prune = 1
        self.manifest_only = 1
        self.force_manifest = 1
        self.ignore_egg_info_dir = False

    
    def finalize_options(self):
        pass

    
    def run(self):
        self.filelist = FileList(ignore_egg_info_dir = self.ignore_egg_info_dir)
        if not os.path.exists(self.manifest):
            self.write_manifest()
        self.add_defaults()
        if os.path.exists(self.template):
            self.read_template()
        self.add_license_files()
        self.prune_file_list()
        self.filelist.sort()
        self.filelist.remove_duplicates()
        self.write_manifest()

    
    def _manifest_normalize(self, path):
        path = unicode_utils.filesys_decode(path)
        return path.replace(os.sep, '/')

    
    def write_manifest(self):
        """
        Write the file list in 'self.filelist' to the manifest file
        named by 'self.manifest'.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def warn(self, msg):
        if not self._should_suppress_warning(msg):
            sdist.warn(self, msg)
            return None

    _should_suppress_warning = (lambda msg: re.match('standard file .*not found', msg))()
    
    def add_defaults(self):
        sdist.add_defaults(self)
        self.filelist.append(self.template)
        self.filelist.append(self.manifest)
        rcfiles = list(walk_revctrl())
        if rcfiles:
            self.filelist.extend(rcfiles)
        elif os.path.exists(self.manifest):
            self.read_manifest()
        if os.path.exists('setup.py'):
            self.filelist.append('setup.py')
        ei_cmd = self.get_finalized_command('egg_info')
        self.filelist.graft(ei_cmd.egg_info)

    
    def add_license_files(self):
        if not self.distribution.metadata.license_files:
            license_files = []
            for lf in license_files:
                log.info("adding license file '%s'", lf)
                self.filelist.extend(license_files)
                return None

    
    def prune_file_list(self):
        build = self.get_finalized_command('build')
        base_dir = self.distribution.get_fullname()
        self.filelist.prune(build.build_base)
        self.filelist.prune(base_dir)
        sep = re.escape(os.sep)
        self.filelist.exclude_pattern('(^|' + sep + ')(RCS|CVS|\\.svn)' + sep, is_regex = 1)

    
    def _safe_data_files(self, build_py):
        '''
        The parent class implementation of this method
        (``sdist``) will try to include data files, which
        might cause recursion problems when
        ``include_package_data=True``.

        Therefore, avoid triggering any attempt of
        analyzing/building the manifest again.
        '''
        if hasattr(build_py, 'get_data_files_without_manifest'):
            return build_py.get_data_files_without_manifest()
        None.warn("Custom 'build_py' does not implement 'get_data_files_without_manifest'.\nPlease extend command classes from setuptools instead of distutils.", SetuptoolsDeprecationWarning)
        return build_py.get_data_files()



def write_file(filename, contents):
    """Create a file with the specified name and write 'contents' (a
    sequence of strings without line terminators) to it.
    """
    contents = '\n'.join(contents)
    contents = contents.encode('utf-8')
    f = open(filename, 'wb')
    f.write(contents)
    None(None, None)
    return None
    with None:
        if not None:
            pass


def write_pkg_info(cmd, basename, filename):
    log.info('writing %s', filename)
    if not cmd.dry_run:
        metadata = cmd.distribution.metadata
        metadata.version, oldver = cmd.egg_version, metadata.version
        metadata.name, oldname = cmd.egg_name, metadata.name
        
        try:
            metadata.write_pkg_info(cmd.egg_info)
            metadata.name, metadata.version = oldname, oldver
        except:
            metadata.name, metadata.version = oldname, oldver

        safe = getattr(cmd.distribution, 'zip_safe', None)
        bdist_egg.write_safety_flag(cmd.egg_info, safe)
        return None


def warn_depends_obsolete(cmd, basename, filename):
    if os.path.exists(filename):
        log.warn("WARNING: 'depends.txt' is not used by setuptools 0.6!\nUse the install_requires/extras_require setup() args instead.")
        return None


def _write_requirements(stream, reqs):
