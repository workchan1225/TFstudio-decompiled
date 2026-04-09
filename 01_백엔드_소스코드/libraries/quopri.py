# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: quopri.pyc (Python 3.11)

'''Conversions to/from quoted-printable transport encoding as per RFC 1521.'''
__all__ = [
    'encode',
    'decode',
    'encodestring',
    'decodestring']
ESCAPE = b'='
MAXLINESIZE = 76
HEX = b'0123456789ABCDEF'
EMPTYSTRING = b''

try:
    from binascii import a2b_qp, b2a_qp
except ImportError:
    a2b_qp = None
    b2a_qp = None


def needsquoting(c, quotetabs, header):
    """Decide whether a particular byte ordinal needs to be quoted.

    The 'quotetabs' flag indicates whether embedded tabs and spaces should be
    quoted.  Note that line-ending tabs and spaces are always encoded, as per
    RFC 1521.
    """
    pass
# WARNING: Decompyle incomplete


def quote(c):
    '''Quote a single character.'''
    pass
# WARNING: Decompyle incomplete


def encode(input, output, quotetabs, header = (False,)):
    """Read 'input', apply quoted-printable encoding, and write to 'output'.

    'input' and 'output' are binary file objects. The 'quotetabs' flag
    indicates whether embedded tabs and spaces should be quoted. Note that
    line-ending tabs and spaces are always encoded, as per RFC 1521.
    The 'header' flag indicates whether we are encoding spaces as _ as per RFC
    1522."""
    pass
# WARNING: Decompyle incomplete


def encodestring(s, quotetabs, header = (False, False)):
    pass
# WARNING: Decompyle incomplete


def decode(input, output, header = (False,)):
    """Read 'input', apply quoted-printable decoding, and write to 'output'.
    'input' and 'output' are binary file objects.
    If 'header' is true, decode underscore as space (per RFC 1522)."""
    pass
# WARNING: Decompyle incomplete


def decodestring(s, header = (False,)):
    pass
# WARNING: Decompyle incomplete


def ishex(c):
    """Return true if the byte ordinal 'c' is a hexadecimal digit in ASCII."""
    pass
# WARNING: Decompyle incomplete


def unhex(s):
