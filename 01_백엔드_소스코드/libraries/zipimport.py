# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: zipimport.pyc (Python 3.11)

"""zipimport provides support for importing Python modules from Zip archives.

This module exports three objects:
- zipimporter: a class; its constructor takes a path to a Zip archive.
- ZipImportError: exception raised by zipimporter objects. It's a
  subclass of ImportError, so it can be caught as ImportError, too.
- _zip_directory_cache: a dict, mapping archive paths to zip directory
  info dicts, as used in zipimporter._files.

It is usually not needed to use the zipimport module explicitly; it is
used by the builtin import mechanism for sys.path items that are paths
to Zip archives.
"""
import _frozen_importlib_external as _bootstrap_external
from _frozen_importlib_external import _unpack_uint16, _unpack_uint32
import _frozen_importlib as _bootstrap
import _imp
import _io
import marshal
import sys
import time
import _warnings
__all__ = [
    'ZipImportError',
    'zipimporter']
path_sep = _bootstrap_external.path_sep
alt_path_sep = _bootstrap_external.path_separators[1:]

class ZipImportError(ImportError):
    pass

_zip_directory_cache = { }
_module_type = type(sys)
END_CENTRAL_DIR_SIZE = 22
STRING_END_ARCHIVE = b'PK\x05\x06'
MAX_COMMENT_LEN = 65535

class zipimporter(_bootstrap_external._LoaderBasics):
    """zipimporter(archivepath) -> zipimporter object

    Create a new zipimporter instance. 'archivepath' must be a path to
    a zipfile, or to a specific path inside a zipfile. For example, it can be
    '/tmp/myimport.zip', or '/tmp/myimport.zip/mydirectory', if mydirectory is a
    valid directory inside the archive.

    'ZipImportError is raised if 'archivepath' doesn't point to a valid Zip
    archive.

    The 'archive' attribute of zipimporter objects contains the name of the
    zipfile targeted.
    """
    
    def __init__(self, path):
        if not isinstance(path, str):
            raise TypeError(f'''expected str, not {type(path)!r}''')
        if not path:
            raise ZipImportError('archive path is empty', path = path)
        if alt_path_sep:
            path = path.replace(alt_path_sep, path_sep)
        prefix = []
        
        try:
            st = _bootstrap_external._path_stat(path)
            if st.st_mode & 61440 != 32768:
                raise ZipImportError('not a Zip file', path = path)
        except (OSError, ValueError):
            (dirname, basename) = _bootstrap_external._path_split(path)
            if dirname == path:
                raise ZipImportError('not a Zip file', path = path)
            path = dirname
            prefix.append(basename)

        continue
        
        try:
            files = _zip_directory_cache[path]
        except KeyError:
            files = _read_directory(path)
            _zip_directory_cache[path] = files

        self._files = files
        self.archive = path
    # WARNING: Decompyle incomplete

    
    def find_loader(self, fullname, path = (None,)):
        """find_loader(fullname, path=None) -> self, str or None.

        Search for a module specified by 'fullname'. 'fullname' must be the
        fully qualified (dotted) module name. It returns the zipimporter
        instance itself if the module was found, a string containing the
        full path name if it's possibly a portion of a namespace package,
        or None otherwise. The optional 'path' argument is ignored -- it's
        there for compatibility with the importer protocol.

        Deprecated since Python 3.10. Use find_spec() instead.
        """
        _warnings.warn('zipimporter.find_loader() is deprecated and slated for removal in Python 3.12; use find_spec() instead', DeprecationWarning)
        mi = _get_module_info(self, fullname)
    # WARNING: Decompyle incomplete

    
    def find_module(self, fullname, path = (None,)):
        """find_module(fullname, path=None) -> self or None.

        Search for a module specified by 'fullname'. 'fullname' must be the
        fully qualified (dotted) module name. It returns the zipimporter
        instance itself if the module was found, or None if it wasn't.
        The optional 'path' argument is ignored -- it's there for compatibility
        with the importer protocol.

        Deprecated since Python 3.10. Use find_spec() instead.
        """
        _warnings.warn('zipimporter.find_module() is deprecated and slated for removal in Python 3.12; use find_spec() instead', DeprecationWarning)
        return self.find_loader(fullname, path)[0]

    
    def find_spec(self, fullname, target = (None,)):
        '''Create a ModuleSpec for the specified module.

        Returns None if the module cannot be found.
        '''
        module_info = _get_module_info(self, fullname)
    # WARNING: Decompyle incomplete

    
    def get_code(self, fullname):
        """get_code(fullname) -> code object.

        Return the code object for the specified module. Raise ZipImportError
        if the module couldn't be imported.
        """
        (code, ispackage, modpath) = _get_module_code(self, fullname)
        return code

    
    def get_data(self, pathname):
        """get_data(pathname) -> string with file data.

        Return the data associated with 'pathname'. Raise OSError if
        the file wasn't found.
        """
        if alt_path_sep:
            pathname = pathname.replace(alt_path_sep, path_sep)
        key = pathname
        if pathname.startswith(self.archive + path_sep):
            key = pathname[len(self.archive + path_sep):]
        
        try:
            toc_entry = self._files[key]
        except KeyError:
            raise OSError(0, '', key)

        return _get_data(self.archive, toc_entry)

    
    def get_filename(self, fullname):
        """get_filename(fullname) -> filename string.

        Return the filename for the specified module or raise ZipImportError
        if it couldn't be imported.
        """
        (code, ispackage, modpath) = _get_module_code(self, fullname)
        return modpath

    
    def get_source(self, fullname):
        """get_source(fullname) -> source string.

        Return the source code for the specified module. Raise ZipImportError
        if the module couldn't be found, return None if the archive does
        contain the module, but has no source for it.
        """
        mi = _get_module_info(self, fullname)
    # WARNING: Decompyle incomplete

    
    def is_package(self, fullname):
        """is_package(fullname) -> bool.

        Return True if the module specified by fullname is a package.
        Raise ZipImportError if the module couldn't be found.
        """
        mi = _get_module_info(self, fullname)
    # WARNING: Decompyle incomplete

    
    def load_module(self, fullname):
        """load_module(fullname) -> module.

        Load the module specified by 'fullname'. 'fullname' must be the
        fully qualified (dotted) module name. It returns the imported
        module, or raises ZipImportError if it could not be imported.

        Deprecated since Python 3.10. Use exec_module() instead.
        """
        msg = 'zipimport.zipimporter.load_module() is deprecated and slated for removal in Python 3.12; use exec_module() instead'
        _warnings.warn(msg, DeprecationWarning)
        (code, ispackage, modpath) = _get_module_code(self, fullname)
        mod = sys.modules.get(fullname)
    # WARNING: Decompyle incomplete

    
    def get_resource_reader(self, fullname):
        """Return the ResourceReader for a package in a zip file.

        If 'fullname' is a package within the zip file, return the
        'ResourceReader' object for the package.  Otherwise return None.
        """
        
        try:
            if not self.is_package(fullname):
                return None
        except ZipImportError:
            return None
            ZipReader = ZipReader
            import importlib.readers
            return ZipReader(self, fullname)


    
    def invalidate_caches(self):
        '''Reload the file data of the archive path.'''
        
        try:
            self._files = _read_directory(self.archive)
            _zip_directory_cache[self.archive] = self._files
            return None
        except ZipImportError:
            _zip_directory_cache.pop(self.archive, None)
            self._files = { }
            return None


    
    def __repr__(self):
        return f'''<zipimporter object "{self.archive}{path_sep}{self.prefix}">'''


_zip_searchorder = ((path_sep + '__init__.pyc', True, True), (path_sep + '__init__.py', False, True), ('.pyc', True, False), ('.py', False, False))

def _get_module_path(self, fullname):
    return self.prefix + fullname.rpartition('.')[2]


def _is_dir(self, path):
    dirpath = path + path_sep
    return dirpath in self._files


def _get_module_info(self, fullname):
    path = _get_module_path(self, fullname)
    for suffix, isbytecode, ispackage in _zip_searchorder:
        fullpath = path + suffix
        if fullpath in self._files:
            
            return None, ispackage
        return None


def _read_directory(archive):
