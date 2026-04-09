# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dylib.pyc (Python 3.11)

'''
Generic dylib path manipulation
'''
import re
__all__ = [
    'dylib_info']
DYLIB_RE = re.compile('(?x)\n(?P<location>^.*)(?:^|/)\n(?P<name>\n    (?P<shortname>\\w+?)\n    (?:\\.(?P<version>[^._]+))?\n    (?:_(?P<suffix>[^._]+))?\n    \\.dylib$\n)\n')

def dylib_info(filename):
    """
    A dylib name can take one of the following four forms:
        Location/Name.SomeVersion_Suffix.dylib
        Location/Name.SomeVersion.dylib
        Location/Name_Suffix.dylib
        Location/Name.dylib

    returns None if not found or a mapping equivalent to:
        dict(
            location='Location',
            name='Name.SomeVersion_Suffix.dylib',
            shortname='Name',
            version='SomeVersion',
            suffix='Suffix',
        )

    Note that SomeVersion and Suffix are optional and may be None
    if not present.
    """
    is_dylib = DYLIB_RE.match(filename)
    if not is_dylib:
        return None
    return None.groupdict()
