# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ffiplatform.pyc (Python 3.11)

import sys
import os
from error import VerificationError
LIST_OF_FILE_NAMES = [
    'sources',
    'include_dirs',
    'library_dirs',
    'extra_objects',
    'depends']

def get_extension(srcfilename, modname, sources = ((),), **kwds):
    Extension = Extension
    import cffi._shimmed_dist_utils
    allsources = [
        srcfilename]
# WARNING: Decompyle incomplete


def compile(tmpdir, ext, compiler_verbose, debug = (0, None)):
    '''Compile a C extension module using distutils.'''
    saved_environ = os.environ.copy()
    
    try:
        outputfilename = _build(tmpdir, ext, compiler_verbose, debug)
        outputfilename = os.path.abspath(outputfilename)
        for key, value in saved_environ.items():
            if os.environ.get(key) != value:
                os.environ[key] = value
    except:
        for key, value in saved_environ.items():
            if os.environ.get(key) != value:
                os.environ[key] = value
            return outputfilename



def _build(tmpdir, ext, compiler_verbose, debug = (0, None)):
    Distribution = Distribution
    CompileError = CompileError
    LinkError = LinkError
    set_threshold = set_threshold
    set_verbosity = set_verbosity
    import cffi._shimmed_dist_utils
    dist = Distribution({
        'ext_modules': [
            ext] })
    dist.parse_config_files()
    options = dist.get_option_dict('build_ext')
# WARNING: Decompyle incomplete


try:
    from os.path import samefile
except ImportError:
    
    def samefile(f1, f2):
        return os.path.abspath(f1) == os.path.abspath(f2)



def maybe_relative_path(path):
    if not os.path.isabs(path):
        return path
    dir = None
    names = []
    prevdir = dir
    (dir, name) = os.path.split(prevdir)
    if not dir == prevdir or dir:
        return path
    None.append(name)
# WARNING: Decompyle incomplete


try:
    int_or_long = (int, long)
    import cStringIO
except NameError:
    int_or_long = int
    import io as cStringIO


def _flatten(x, f):
    if isinstance(x, str):
        f.write('%ds%s' % (len(x), x))
        return None
    if None(x, dict):
        keys = sorted(x.keys())
        f.write('%dd' % len(keys))
        for key in keys:
            _flatten(key, f)
            _flatten(x[key], f)
            return None
            if isinstance(x, (list, tuple)):
                f.write('%dl' % len(x))
                for value in x:
                    _flatten(value, f)
                    return None
                    if isinstance(x, int_or_long):
                        f.write('%di' % (x,))
                        return None
                    raise None(f'''the keywords to verify() contains unsupported object {x!r}''')


def flatten(x):
    f = cStringIO.StringIO()
    _flatten(x, f)
    return f.getvalue()
