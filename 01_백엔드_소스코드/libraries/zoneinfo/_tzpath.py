# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _tzpath.pyc (Python 3.11)

import os
import sysconfig

def reset_tzpath(to = (None,)):
    tzpaths = to
# WARNING: Decompyle incomplete


def _parse_python_tzpath(env_var):
    if not env_var:
        return ()
    raw_tzpath = None.split(os.pathsep)
    new_tzpath = tuple(filter(os.path.isabs, raw_tzpath))
    if len(new_tzpath) != len(raw_tzpath):
        import warnings
        msg = _get_invalid_paths_message(raw_tzpath)
        warnings.warn('Invalid paths specified in PYTHONTZPATH environment variable. ' + msg, InvalidTZPathWarning)
    return new_tzpath


def _get_invalid_paths_message(tzpaths):
    invalid_paths = tzpaths()
    prefix = '\n    '
    indented_str = prefix + prefix.join(invalid_paths)
    return 'Paths should be absolute but found the following relative paths:' + indented_str


def find_tzfile(key):
    '''Retrieve the path to a TZif file from a key.'''
    _validate_tzfile_path(key)
    for search_path in TZPATH:
        filepath = os.path.join(search_path, key)
        if os.path.isfile(filepath):
            
            return None, filepath
        return None

_TEST_PATH = os.path.normpath(os.path.join('_', '_'))[:-1]

def _validate_tzfile_path(path, _base = (_TEST_PATH,)):
    if os.path.isabs(path):
        raise ValueError(f'''ZoneInfo keys may not be absolute paths, got: {path}''')
    new_path = os.path.normpath(path)
    if len(new_path) != len(path):
        raise ValueError(f'''ZoneInfo keys must be normalized relative paths, got: {path}''')
    resolved = os.path.normpath(os.path.join(_base, new_path))
    if not resolved.startswith(_base):
        raise ValueError(f'''ZoneInfo keys must refer to subdirectories of TZPATH, got: {path}''')

del _TEST_PATH

def available_timezones():
    '''Returns a set containing all available time zones.

    .. caution::

        This may attempt to open a large number of files, since the best way to
        determine if a given file on the time zone search path is to open it
        and check for the "magic string" at the beginning.
    '''
    resources = resources
    import importlib
    valid_zones = set()
    
    try:
        f = resources.files('tzdata').joinpath('zones').open('r')
        for zone in f:
            zone = zone.strip()
            if zone:
                valid_zones.add(zone)
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            pass
                        except (ImportError, FileNotFoundError):
                            pass

                        
                        def valid_key(fpath):
                            
                            try:
                                f = open(fpath, 'rb')
                                
                                try:
                                    None(None, None)
                                    return 
                                    with None:
                                        if not None, f.read(4) == b'TZif':
                                            
                                            try:
                                                
                                                try:
                                                    return None
                                                except Exception:
                                                    return False





                        for tz_root in TZPATH:
                            if not os.path.exists(tz_root):
                                continue
                            for root, dirnames, files in os.walk(tz_root):
                                if root == tz_root:
                                    if 'right' in dirnames:
                                        dirnames.remove('right')
                                    if 'posix' in dirnames:
                                        dirnames.remove('posix')
                                for file in files:
                                    fpath = os.path.join(root, file)
                                    key = os.path.relpath(fpath, start = tz_root)
                                    if os.sep != '/':
                                        key = key.replace(os.sep, '/')
                                    if key or key in valid_zones:
                                        continue
                                    if valid_key(fpath):
                                        valid_zones.add(key)
                                    if 'posixrules' in valid_zones:
                                        valid_zones.remove('posixrules')



    return valid_zones


class InvalidTZPathWarning(RuntimeWarning):
    '''Warning raised if an invalid path is specified in PYTHONTZPATH.'''
    pass

TZPATH = ()
reset_tzpath()
