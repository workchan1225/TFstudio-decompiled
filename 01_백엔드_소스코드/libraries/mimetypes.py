# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mimetypes.pyc (Python 3.11)

'''Guess the MIME type of a file.

This module defines two useful functions:

guess_type(url, strict=True) -- guess the MIME type and encoding of a URL.

guess_extension(type, strict=True) -- guess the extension for a given MIME type.

It also contains the following, for tuning the behavior:

Data:

knownfiles -- list of files to parse
inited -- flag set when init() has been called
suffix_map -- dictionary mapping suffixes to suffixes
encodings_map -- dictionary mapping suffixes to encodings
types_map -- dictionary mapping suffixes to types

Functions:

init([files]) -- parse a list of files, default knownfiles (on Windows, the
  default values are taken from the registry)
read_mime_types(file) -- parse one file, return a dictionary or None
'''
import os
import sys
import posixpath
import urllib.parse as urllib

try:
    from _winapi import _mimetypes_read_windows_registry
except ImportError:
    _mimetypes_read_windows_registry = None


try:
    import winreg as _winreg
except ImportError:
    _winreg = None

__all__ = [
    'knownfiles',
    'inited',
    'MimeTypes',
    'guess_type',
    'guess_all_extensions',
    'guess_extension',
    'add_type',
    'init',
    'read_mime_types',
    'suffix_map',
    'encodings_map',
    'types_map',
    'common_types']
knownfiles = [
    '/etc/mime.types',
    '/etc/httpd/mime.types',
    '/etc/httpd/conf/mime.types',
    '/etc/apache/mime.types',
    '/etc/apache2/mime.types',
    '/usr/local/etc/httpd/conf/mime.types',
    '/usr/local/lib/netscape/mime.types',
    '/usr/local/etc/httpd/conf/mime.types',
    '/usr/local/etc/mime.types']
inited = False
_db = None

class MimeTypes:
    '''MIME-types datastore.

    This datastore can handle information from mime.types-style files
    and supports basic determination of MIME type from a filename or
    URL, and can guess a reasonable extension given a MIME type.
    '''
    
    def __init__(self, filenames, strict = ((), True)):
        if not inited:
            init()
        self.encodings_map = _encodings_map_default.copy()
        self.suffix_map = _suffix_map_default.copy()
        self.types_map = ({ }, { })
        self.types_map_inv = ({ }, { })
        for ext, type in _types_map_default.items():
            self.add_type(type, ext, True)
            for ext, type in _common_types_default.items():
                self.add_type(type, ext, False)
                for name in filenames:
                    self.read(name, strict)
                    return None

    
    def add_type(self, type, ext, strict = (True,)):
        '''Add a mapping between a type and an extension.

        When the extension is already known, the new
        type will replace the old one. When the type
        is already known the extension will be added
        to the list of known extensions.

        If strict is true, information will be added to
        list of standard types, else to the list of non-standard
        types.
        '''
        self.types_map[strict][ext] = type
        exts = self.types_map_inv[strict].setdefault(type, [])
        if ext not in exts:
            exts.append(ext)
            return None

    
    def guess_type(self, url, strict = (True,)):
        """Guess the type of a file which is either a URL or a path-like object.

        Return value is a tuple (type, encoding) where type is None if
        the type can't be guessed (no or unknown suffix) or a string
        of the form type/subtype, usable for a MIME Content-type
        header; and encoding is None for no encoding or the name of
        the program used to encode (e.g. compress or gzip).  The
        mappings are table driven.  Encoding suffixes are case
        sensitive; type suffixes are first tried case sensitive, then
        case insensitive.

        The suffixes .tgz, .taz and .tz (case sensitive!) are all
        mapped to '.tar.gz'.  (This is table-driven too, using the
        dictionary suffix_map.)

        Optional `strict' argument when False adds a bunch of commonly found,
        but non-standard types.
        """
        url = os.fspath(url)
        (scheme, url) = urllib.parse._splittype(url)
        if scheme == 'data':
            comma = url.find(',')
            if comma < 0:
                return (None, None)
            semi = None.find(';', 0, comma)
            if semi >= 0:
                type = url[:semi]
            else:
                type = url[:comma]
            if '=' in type or '/' not in type:
                type = 'text/plain'
            return (type, None)
        (base, ext) = None.splitext(url)
        ext_lower = ext.lower()
    # WARNING: Decompyle incomplete

    
    def guess_all_extensions(self, type, strict = (True,)):
        """Guess the extensions for a file based on its MIME type.

        Return value is a list of strings giving the possible filename
        extensions, including the leading dot ('.').  The extension is not
        guaranteed to have been associated with any particular data stream,
        but would be mapped to the MIME type `type' by guess_type().

        Optional `strict' argument when false adds a bunch of commonly found,
        but non-standard types.
        """
        type = type.lower()
        extensions = list(self.types_map_inv[True].get(type, []))
        if not strict:
            for ext in self.types_map_inv[False].get(type, []):
                if ext not in extensions:
                    extensions.append(ext)
                return extensions

    
    def guess_extension(self, type, strict = (True,)):
        """Guess the extension for a file based on its MIME type.

        Return value is a string giving a filename extension,
        including the leading dot ('.').  The extension is not
        guaranteed to have been associated with any particular data
        stream, but would be mapped to the MIME type `type' by
        guess_type().  If no extension can be guessed for `type', None
        is returned.

        Optional `strict' argument when false adds a bunch of commonly found,
        but non-standard types.
        """
        extensions = self.guess_all_extensions(type, strict)
        if not extensions:
            return None
        return None[0]

    
    def read(self, filename, strict = (True,)):
        '''
        Read a single mime.types-format file, specified by pathname.

        If strict is true, information will be added to
        list of standard types, else to the list of non-standard
        types.
        '''
        fp = open(filename, encoding = 'utf-8')
        self.readfp(fp, strict)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def readfp(self, fp, strict = (True,)):
        '''
        Read a single mime.types-format file.

        If strict is true, information will be added to
        list of standard types, else to the list of non-standard
        types.
        '''
        line = fp.readline()
        if not line:
            return None
        words = None.split()
        for i in range(len(words)):
            if words[i][0] == '#':
                del words[i:]
            
            if not words:
                continue
        suffixes = words[1:]
        type = words[0]
        for suff in suffixes:
            self.add_type(type, '.' + suff, strict)

    
    def read_windows_registry(self, strict = (True,)):
        '''
        Load the MIME types database from Windows registry.

        If strict is true, information will be added to
        list of standard types, else to the list of non-standard
        types.
        '''
        pass
    # WARNING: Decompyle incomplete

    _read_windows_registry = (lambda cls, add_type: 
def enum_types(mimedb):
pass# WARNING: Decompyle incomplete
hkcr = _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, '')for subkeyname in enum_types(hkcr):
subkey = _winreg.OpenKey(hkcr, subkeyname)if not subkeyname.startswith('.'):
None(None, None)continue(mimetype, datatype) = _winreg.QueryValueEx(subkey, 'Content Type')if datatype != _winreg.REG_SZ:
None(None, None)continueadd_type(mimetype, subkeyname)None(None, None)with None:
if not None:
passcontinueexcept OSError:
continueNone(None, None)Nonewith None:
if not None:
pass)()


def guess_type(url, strict = (True,)):
    '''Guess the type of a file based on its URL.

    Return value is a tuple (type, encoding) where type is None if the
    type can\'t be guessed (no or unknown suffix) or a string of the
    form type/subtype, usable for a MIME Content-type header; and
    encoding is None for no encoding or the name of the program used
    to encode (e.g. compress or gzip).  The mappings are table
    driven.  Encoding suffixes are case sensitive; type suffixes are
    first tried case sensitive, then case insensitive.

    The suffixes .tgz, .taz and .tz (case sensitive!) are all mapped
    to ".tar.gz".  (This is table-driven too, using the dictionary
    suffix_map).

    Optional `strict\' argument when false adds a bunch of commonly found, but
    non-standard types.
    '''
    pass
# WARNING: Decompyle incomplete


def guess_all_extensions(type, strict = (True,)):
    """Guess the extensions for a file based on its MIME type.

    Return value is a list of strings giving the possible filename
    extensions, including the leading dot ('.').  The extension is not
    guaranteed to have been associated with any particular data
    stream, but would be mapped to the MIME type `type' by
    guess_type().  If no extension can be guessed for `type', None
    is returned.

    Optional `strict' argument when false adds a bunch of commonly found,
    but non-standard types.
    """
    pass
# WARNING: Decompyle incomplete


def guess_extension(type, strict = (True,)):
    """Guess the extension for a file based on its MIME type.

    Return value is a string giving a filename extension, including the
    leading dot ('.').  The extension is not guaranteed to have been
    associated with any particular data stream, but would be mapped to the
    MIME type `type' by guess_type().  If no extension can be guessed for
    `type', None is returned.

    Optional `strict' argument when false adds a bunch of commonly found,
    but non-standard types.
    """
    pass
# WARNING: Decompyle incomplete


def add_type(type, ext, strict = (True,)):
    '''Add a mapping between a type and an extension.

    When the extension is already known, the new
    type will replace the old one. When the type
    is already known the extension will be added
    to the list of known extensions.

    If strict is true, information will be added to
    list of standard types, else to the list of non-standard
    types.
    '''
    pass
# WARNING: Decompyle incomplete


def init(files = (None,)):
    global inited
    inited = True
# WARNING: Decompyle incomplete


def read_mime_types(file):
    
    try:
        f = open(file, encoding = 'utf-8')
    except OSError:
        return None

    f
    db = MimeTypes()
    db.readfp(f, True)
    None(None, None)
    return 
    with None:
        if not None, db.types_map[True]:
            pass


def _default_mime_types():
    global suffix_map, _suffix_map_default, encodings_map, _encodings_map_default
    suffix_map = {
        '.svgz': '.svg.gz',
        '.tgz': '.tar.gz',
        '.taz': '.tar.gz',
        '.tz': '.tar.gz',
        '.tbz2': '.tar.bz2',
        '.txz': '.tar.xz' }
    _suffix_map_default = {
        '.svgz': '.svg.gz',
        '.tgz': '.tar.gz',
        '.taz': '.tar.gz',
        '.tz': '.tar.gz',
        '.tbz2': '.tar.bz2',
        '.txz': '.tar.xz' }
    encodings_map = {
        '.gz': 'gzip',
        '.Z': 'compress',
        '.bz2': 'bzip2',
        '.xz': 'xz',
        '.br': 'br' }
    _encodings_map_default = {
        '.gz': 'gzip',
        '.Z': 'compress',
        '.bz2': 'bzip2',
        '.xz': 'xz',
        '.br': 'br' }
# WARNING: Decompyle incomplete

_default_mime_types()

def _main():
    pass
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    _main()
    return None
