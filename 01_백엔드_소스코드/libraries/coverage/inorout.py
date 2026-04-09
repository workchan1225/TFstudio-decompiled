# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: inorout.pyc (Python 3.11)

'''Determining whether files are being measured/reported or not.'''
from __future__ import annotations
import importlib.util as importlib
import inspect
import itertools
import os
import os.path as os
import platform
import re
import sys
import sysconfig
import traceback
from collections.abc import Iterable
from types import FrameType, ModuleType
from typing import TYPE_CHECKING, Any, cast
from coverage import env
from coverage.disposition import FileDisposition, disposition_init
from coverage.exceptions import ConfigError, CoverageException, PluginError
from coverage.files import GlobMatcher, ModuleMatcher, TreeMatcher, canonical_filename, find_python_files, prep_patterns
from coverage.misc import isolate_module, sys_modules_saved
from coverage.python import source_for_file, source_for_morf
from coverage.types import TDebugCtl, TFileDisposition, TMorf, TWarnFn
if TYPE_CHECKING:
    from coverage.config import CoverageConfig
    from coverage.plugin_support import Plugins
modules_we_happen_to_have: 'list[ModuleType]' = [
    inspect,
    itertools,
    os,
    platform,
    re,
    sysconfig,
    traceback]
if env.PYPY:
    import _pypy_irc_topic
    import _structseq
    modules_we_happen_to_have.extend([
        _structseq,
        _pypy_irc_topic])
os = isolate_module(os)

def canonical_path(morf = None, directory = None):
    '''Return the canonical path of the module or file `morf`.

    If the module is a package, then return its directory. If it is a
    module, then return its file, unless `directory` is True, in which
    case return its enclosing directory.

    '''
    morf_path = canonical_filename(source_for_morf(morf))
    if morf_path.endswith('__init__.py') or directory:
        morf_path = os.path.split(morf_path)[0]
    return morf_path


def name_for_module(filename = None, frame = None):
    '''Get the name of the module for a filename and frame.

    For configurability\'s sake, we allow __main__ modules to be matched by
    their importable name.

    If loaded via runpy (aka -m), we can usually recover the "original"
    full dotted module name, otherwise, we resort to interpreting the
    file name to get the module\'s name.  In the case that the module name
    can\'t be determined, None is returned.

    '''
    pass
# WARNING: Decompyle incomplete


def module_is_namespace(mod = None):
    '''Is the module object `mod` a PEP420 namespace module?'''
    if hasattr(mod, '__path__'):
        pass
    return getattr(mod, '__file__', None) is None


def module_has_file(mod = None):
    '''Does the module object `mod` have an existing __file__ ?'''
    mod__file__ = getattr(mod, '__file__', None)
# WARNING: Decompyle incomplete


def file_and_path_for_module(modulename = None):
    '''Find the file and search path for `modulename`.

    Returns:
        filename: The filename of the module, or None.
        path: A list (possibly empty) of directories to find submodules in.

    '''
    filename = None
    path = []
# WARNING: Decompyle incomplete


def add_stdlib_paths(paths = None):
    '''Add paths where the stdlib can be found to the set `paths`.'''
    for m in modules_we_happen_to_have:
        if hasattr(m, '__file__'):
            paths.add(canonical_path(m, directory = True))
        return None


def add_third_party_paths(paths = None):
    '''Add locations for third-party packages to the set `paths`.'''
    scheme_names = set(sysconfig.get_scheme_names())
    for scheme in scheme_names:
        better_scheme = 'pypy_posix' if scheme == 'pypy' else scheme
        if os.name in better_scheme.split('_'):
            config_paths = sysconfig.get_paths(scheme)
            for path_name in ('platlib', 'purelib', 'scripts'):
                paths.add(config_paths[path_name])
                return None


def add_coverage_paths(paths = None):
    '''Add paths where coverage.py code can be found to the set `paths`.'''
    cover_path = canonical_path(__file__, directory = True)
    paths.add(cover_path)
    if env.TESTING:
        paths.add(os.path.join(cover_path, 'tests'))
        return None


class InOrOut:
    '''Machinery for determining what files to measure.'''
    
    def __init__(self, config = None, warn = None, debug = None, include_namespace_packages = ('config', 'CoverageConfig', 'warn', 'TWarnFn', 'debug', 'TDebugCtl | None', 'include_namespace_packages', 'bool', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def should_trace(self = None, filename = None, frame = None):
        '''Decide whether to trace execution in `filename`, with a reason.

        This function is called from the trace function.  As each new file name
        is encountered, this function determines whether it is traced or not.

        Returns a FileDisposition object.

        '''
        original_filename = filename
        disp = disposition_init(self.disp_class, filename)
        
        def nope(disp = None, reason = None):
            '''Simple helper to make it easy to return NO.'''
            disp.trace = False
            disp.reason = reason
            return disp

        if original_filename.startswith('<'):
            return nope(disp, 'original file name is not real')
    # WARNING: Decompyle incomplete

    
    def check_include_omit_etc(self = None, filename = None, frame = None):
        """Check a file name against the include, omit, etc, rules.

        Returns a string or None.  String means, don't trace, and is the reason
        why.  None means no reason found to not trace.

        """
        modulename = name_for_module(filename, frame)
        if self.source_match or self.source_pkgs_match:
            extra = ''
            ok = False
            if self.source_pkgs_match:
                if isinstance(modulename, str) and self.source_pkgs_match.match(modulename):
                    ok = True
                    if modulename in self.source_pkgs_unmatched:
                        self.source_pkgs_unmatched.remove(modulename)
                    else:
                        extra = f'''module {modulename!r} '''
            if ok and self.source_match and self.source_match.match(filename):
                ok = True
            if not ok:
                return extra + 'falls outside the --source spec'
            if not None.third_match.match(filename) and self.source_in_third_match.match(filename):
                return 'inside --source, but is third-party'
        if self.include_match:
            if not self.include_match.match(filename):
                return 'falls outside the --include trees'
        if self.cover_match.match(filename):
            return 'is part of coverage.py'
        if None.pylib_match and self.pylib_match.match(filename):
            return 'is in the stdlib'
        if None.third_match.match(filename):
            return 'is a third-party module'
        if None.omit_match and self.omit_match.match(filename):
            return 'is inside an --omit pattern'
        
        try:
            filename.encode('utf-8')
        except UnicodeEncodeError:
            return 'non-encodable filename'


    
    def warn_conflicting_settings(self = None):
        '''Warn if there are settings that conflict.'''
        if self.include:
            if self.source_dirs or self.source_pkgs:
                self.warn('--include is ignored because --source is set', slug = 'include-ignored')
                return None
            return None

    
    def warn_already_imported_files(self = None):
        '''Warn if files have already been imported that we will be measuring.'''
        pass
    # WARNING: Decompyle incomplete

    
    def warn_unimported_source(self = None):
        '''Warn about source packages that were of interest, but never traced.'''
        for pkg in self.source_pkgs_unmatched:
            self._warn_about_unmeasured_code(pkg)
            return None

    
    def _warn_about_unmeasured_code(self = None, pkg = None):
        '''Warn about a package or module that we never traced.

        `pkg` is a string, the name of the package or module.

        '''
        mod = sys.modules.get(pkg)
    # WARNING: Decompyle incomplete

    
    def find_possibly_unexecuted_files(self = None):
        '''Find files in the areas of interest that might be untraced.

        Yields pairs: file path, and responsible plug-in name.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _find_plugin_files(self = None, src_dir = None):
        '''Get executable files from the plugins.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _find_executable_files(self = None, src_dir = None):
        """Find executable files in `src_dir`.

        Search for files in `src_dir` that can be executed because they
        are probably importable. Don't include ones that have been omitted
        by the configuration.

        Yield the file path, and the plugin name that handles the file.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def sys_info(self = None):
        '''Our information for Coverage.sys_info.

        Returns a list of (key, value) pairs.
        '''
        info = [
            ('coverage_paths', self.cover_paths),
            ('stdlib_paths', self.pylib_paths),
            ('third_party_paths', self.third_paths),
            ('source_in_third_party_paths', self.source_in_third_paths)]
        matcher_names = [
            'source_match',
            'source_pkgs_match',
            'include_match',
            'omit_match',
            'cover_match',
            'pylib_match',
            'third_match',
            'source_in_third_match']
        for matcher_name in matcher_names:
            matcher = getattr(self, matcher_name)
            if matcher:
                matcher_info = matcher.info()
            else:
                matcher_info = '-none-'
            info.append((matcher_name, matcher_info))
            return info
