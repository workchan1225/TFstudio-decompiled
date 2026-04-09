# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import re
from typing import FrozenSet, NewType, Tuple, Union, cast
from tags import Tag, parse_tag
from version import InvalidVersion, Version
BuildTag = Union[(Tuple[()], Tuple[(int, str)])]
NormalizedName = NewType('NormalizedName', str)

class InvalidWheelFilename(ValueError):
    '''
    An invalid wheel filename was found, users should refer to PEP 427.
    '''
    pass


class InvalidSdistFilename(ValueError):
    '''
    An invalid sdist filename was found, users should refer to the packaging user guide.
    '''
    pass

_canonicalize_regex = re.compile('[-_.]+')
_build_tag_regex = re.compile('(\\d+)(.*)')

def canonicalize_name(name = None):
    value = _canonicalize_regex.sub('-', name).lower()
    return cast(NormalizedName, value)


def canonicalize_version(version = None):
    '''
    This is very similar to Version.__str__, but has one subtle difference
    with the way it handles the release segment.
    '''
    if isinstance(version, str):
        
        try:
            parsed = Version(version)
        except InvalidVersion:
            return 

        [] = None
        if parsed.epoch != 0:
            parts.append(f'''{parsed.epoch}!''')
    re.sub('(\\.0)+$'('', '.'.join, (lambda .0: pass# WARNING: Decompyle incomplete
)(parsed.release())))
# WARNING: Decompyle incomplete


def parse_wheel_filename(filename = None):
    if not filename.endswith('.whl'):
        raise InvalidWheelFilename(f'''Invalid wheel filename (extension must be \'.whl\'): {filename}''')
    filename = filename[:-4]
    dashes = filename.count('-')
    if dashes not in (4, 5):
        raise InvalidWheelFilename(f'''Invalid wheel filename (wrong number of parts): {filename}''')
    parts = filename.split('-', dashes - 2)
    name_part = parts[0]
# WARNING: Decompyle incomplete


def parse_sdist_filename(filename = None):
    if filename.endswith('.tar.gz'):
        file_stem = filename[:-len('.tar.gz')]
    elif filename.endswith('.zip'):
        file_stem = filename[:-len('.zip')]
    else:
        raise InvalidSdistFilename(f'''Invalid sdist filename (extension must be \'.tar.gz\' or \'.zip\'): {filename}''')
    (name_part, sep, version_part) = file_stem.rpartition('-')
    if not sep:
        raise InvalidSdistFilename(f'''Invalid sdist filename: {filename}''')
    name = canonicalize_name(name_part)
    version = Version(version_part)
    return (name, version)
