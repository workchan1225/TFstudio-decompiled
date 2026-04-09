# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _util.pyc (Python 3.11)

from mutagen._util import cdata

def parse_full_atom(data):
    '''Some atoms are versioned. Split them up in (version, flags, payload).
    Can raise ValueError.
    '''
    if len(data) < 4:
        raise ValueError('not enough data')
    version = ord(data[0:1])
    flags = cdata.uint_be(b'\x00' + data[1:4])
    return (version, flags, data[4:])
