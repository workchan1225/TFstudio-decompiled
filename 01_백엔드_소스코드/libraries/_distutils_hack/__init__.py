# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import sys
import os
is_pypy = '__pypy__' in sys.builtin_module_names

def warn_distutils_present():
    if 'distutils' not in sys.modules:
        return None
    if None and sys.version_info < (3, 7):
        return None
    import warnings
    warnings.warn('Distutils was imported before Setuptools, but importing Setuptools also replaces the `distutils` module in `sys.modules`. This may lead to undesirable behaviors or errors. To avoid these issues, avoid using distutils directly, ensure that setuptools is installed in the traditional way (e.g. not an editable install), and/or make sure that setuptools is always imported before distutils.')


def clear_distutils():
    if 'distutils' not in sys.modules:
        return None
    import warnings
    warnings.warn('Setuptools is replacing distutils.')
    mods = sys.modules()
    for name in mods:
        del sys.modules[name]
        return None


def enabled():
    '''
    Allow selection of distutils by environment variable.
    '''
    which = os.environ.get('SETUPTOOLS_USE_DISTUTILS', 'local')
    return which == 'local'


def ensure_local_distutils():
    import importlib
    clear_distutils()
    shim()
    importlib.import_module('distutils')
    None(None, None)
# WARNING: Decompyle incomplete


def do_override():
    '''
    Ensure that the local copy of distutils is preferred over stdlib.

    See https://github.com/pypa/setuptools/issues/417#issuecomment-392298401
    for more motivation.
    '''
    if enabled():
        warn_distutils_present()
        ensure_local_distutils()
        return None


class _TrivialRe:
    
    def __init__(self, *patterns):
        self._patterns = patterns

    
    def match(self, string):
        pass
    # WARNING: Decompyle incomplete



class DistutilsMetaFinder:
    
    def find_spec(self, fullname, path, target = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def spec_for_distutils(self):
        pass
    # WARNING: Decompyle incomplete

    is_cpython = (lambda : os.path.isfile('pybuilddir.txt'))()
    
    def spec_for_pip(self):
        '''
        Ensure stdlib distutils when running under pip.
        See pypa/pip#8761 for rationale.
        '''
        if self.pip_imported_during_build():
            return None
        None()
        
        self.spec_for_distutils = lambda : pass

    pip_imported_during_build = (lambda cls: pass# WARNING: Decompyle incomplete
)()
    frame_file_is_setup = (lambda frame: frame.f_globals.get('__file__', '').endswith('setup.py'))()
    
    def spec_for_sensitive_tests(self):
        '''
        Ensure stdlib distutils when running select tests under CPython.

        python/cpython#91169
        '''
        clear_distutils()
        
        self.spec_for_distutils = lambda : pass

    sensitive_tests = [
        'test.test_distutils',
        'test.test_peg_generator',
        'test.test_importlib'] if sys.version_info < (3, 10) else [
        'test.test_distutils']

for name in DistutilsMetaFinder.sensitive_tests:
    setattr(DistutilsMetaFinder, f'''spec_for_{name}''', DistutilsMetaFinder.spec_for_sensitive_tests)
    DISTUTILS_FINDER = DistutilsMetaFinder()
    
    def add_shim():
        if not DISTUTILS_FINDER in sys.meta_path:
            insert_shim()
            return None

    
    class shim:
        
        def __enter__(self):
            insert_shim()

        
        def __exit__(self, exc, value, tb):
            remove_shim()


    
    def insert_shim():
        sys.meta_path.insert(0, DISTUTILS_FINDER)

    
    def remove_shim():
        
        try:
            sys.meta_path.remove(DISTUTILS_FINDER)
            return None
        except ValueError:
            return None


    return None
