# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _common.pyc (Python 3.11)

import struct

def load_tzdata(key):
    resources = resources
    import importlib
    components = key.split('/')
    package_name = '.'.join([
        'tzdata.zoneinfo'] + components[:-1])
    resource_name = components[-1]
    
    try:
        return resources.files(package_name).joinpath(resource_name).open('rb')
    except (ImportError, FileNotFoundError, UnicodeEncodeError):
        raise ZoneInfoNotFoundError(f'''No time zone found with key {key}''')



def load_data(fobj):
    pass
# WARNING: Decompyle incomplete


class _TZifHeader:
    __slots__ = [
        'version',
        'isutcnt',
        'isstdcnt',
        'leapcnt',
        'timecnt',
        'typecnt',
        'charcnt']
    
    def __init__(self, *args):
        for attr, val in zip(self.__slots__, args, strict = True):
            setattr(self, attr, val)
            return None

    from_file = (lambda cls, stream: if stream.read(4) != b'TZif':
raise ValueError('Invalid TZif file: magic not found')_version = stream.read(1)if _version == b'\x00':
version = 1else:
version = int(_version)stream.read(15)args = (version,)args = args + struct.unpack('>6l', stream.read(24))# WARNING: Decompyle incomplete
)()


class ZoneInfoNotFoundError(KeyError):
    '''Exception raised when a ZoneInfo key is not found.'''
    pass
