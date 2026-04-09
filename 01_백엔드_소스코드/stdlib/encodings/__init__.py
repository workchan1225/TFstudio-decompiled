# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

''' Standard "encodings" Package

    Standard Python encoding modules are stored in this package
    directory.

    Codec modules must have names corresponding to normalized encoding
    names as defined in the normalize_encoding() function below, e.g.
    \'utf-8\' must be implemented by the module \'utf_8.py\'.

    Each codec module must export the following interface:

    * getregentry() -> codecs.CodecInfo object
    The getregentry() API must return a CodecInfo object with encoder, decoder,
    incrementalencoder, incrementaldecoder, streamwriter and streamreader
    attributes which adhere to the Python Codec Interface Standard.

    In addition, a module may optionally also define the following
    APIs which are then used by the package\'s codec search function:

    * getaliases() -> sequence of encoding name strings to use as aliases

    Alias names returned by getaliases() must be normalized encoding
    names as defined by normalize_encoding().

Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

'''
import codecs
import sys
from  import aliases
_cache = { }
_unknown = '--unknown--'
_import_tail = [
    '*']
_aliases = aliases.aliases

class CodecRegistryError(SystemError, LookupError):
    pass


def normalize_encoding(encoding):
    """ Normalize an encoding name.

        Normalization works as follows: all non-alphanumeric
        characters except the dot used for Python package names are
        collapsed and replaced with a single underscore, e.g. '  -;#'
        becomes '_'. Leading and trailing underscores are removed.

        Note that encoding names should be ASCII only.

    """
    if isinstance(encoding, bytes):
        encoding = str(encoding, 'ascii')
    chars = []
    punct = False
    for c in encoding:
        if c.isalnum() or c == '.':
            if punct and chars:
                chars.append('_')
            if c.isascii():
                chars.append(c)
            punct = False
            continue
        punct = True
        return ''.join(chars)


def search_function(encoding):
    entry = _cache.get(encoding, _unknown)
    if entry is not _unknown:
        return entry
    norm_encoding = None(encoding)
# WARNING: Decompyle incomplete

codecs.register(search_function)
if sys.platform == 'win32':
    
    def _alias_mbcs(encoding):
        
        try:
            import _winapi
            ansi_code_page = 'cp%s' % _winapi.GetACP()
            if encoding == ansi_code_page:
                import encodings.mbcs as encodings
                return encodings.mbcs.getregentry()
            return None
        except ImportError:
            return None


    codecs.register(_alias_mbcs)
    return None
