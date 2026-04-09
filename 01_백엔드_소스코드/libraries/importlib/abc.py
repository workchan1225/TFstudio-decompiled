# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: abc.pyc (Python 3.11)

'''Abstract base classes related to import.'''
from  import _bootstrap_external
from  import machinery

try:
    import _frozen_importlib
except ImportError:
    exc = None
    if exc.name != '_frozen_importlib':
        raise 
    _frozen_importlib = None
    exc = None
    del exc
except:
    exc = None
    del exc


try:
    import _frozen_importlib_external
except ImportError:
    _frozen_importlib_external = _bootstrap_external

from _abc import Loader
import abc
import warnings
from resources.abc import ResourceReader, Traversable, TraversableResources
__all__ = [
    'Loader',
    'Finder',
    'MetaPathFinder',
    'PathEntryFinder',
    'ResourceLoader',
    'InspectLoader',
    'ExecutionLoader',
    'FileLoader',
    'SourceLoader',
    'ResourceReader',
    'Traversable',
    'TraversableResources']

def _register(abstract_cls, *classes):
    pass
# WARNING: Decompyle incomplete


def Finder():
    '''Finder'''
    __doc__ = 'Legacy abstract base class for import finders.\n\n    It may be subclassed for compatibility with legacy third party\n    reimplementations of the import system.  Otherwise, finder\n    implementations should derive from the more specific MetaPathFinder\n    or PathEntryFinder ABCs.\n\n    Deprecated since Python 3.3\n    '
    
    def __init__(self):
        warnings.warn('the Finder ABC is deprecated and slated for removal in Python 3.12; use MetaPathFinder or PathEntryFinder instead', DeprecationWarning)

    find_module = (lambda self, fullname, path = (None,): warnings.warn('importlib.abc.Finder along with its find_module() method are deprecated and slated for removal in Python 3.12; use MetaPathFinder.find_spec() or PathEntryFinder.find_spec() instead', DeprecationWarning))()

Finder = <NODE:27>(Finder, 'Finder', metaclass = abc.ABCMeta)

def MetaPathFinder():
    '''MetaPathFinder'''
    __doc__ = 'Abstract base class for import finders on sys.meta_path.'
    
    def find_module(self, fullname, path):
        '''Return a loader for the module.

        If no module is found, return None.  The fullname is a str and
        the path is a list of strings or None.

        This method is deprecated since Python 3.4 in favor of
        finder.find_spec(). If find_spec() exists then backwards-compatible
        functionality is provided for this method.

        '''
        warnings.warn('MetaPathFinder.find_module() is deprecated since Python 3.4 in favor of MetaPathFinder.find_spec() and is slated for removal in Python 3.12', DeprecationWarning, stacklevel = 2)
        if not hasattr(self, 'find_spec'):
            return None
        found = None.find_spec(fullname, path)
    # WARNING: Decompyle incomplete

    
    def invalidate_caches(self):
        """An optional method for clearing the finder's cache, if any.
        This method is used by importlib.invalidate_caches().
        """
        pass


MetaPathFinder = <NODE:27>(MetaPathFinder, 'MetaPathFinder', metaclass = abc.ABCMeta)
_register(MetaPathFinder, machinery.BuiltinImporter, machinery.FrozenImporter, machinery.PathFinder, machinery.WindowsRegistryFinder)

def PathEntryFinder():
    '''PathEntryFinder'''
    __doc__ = 'Abstract base class for path entry finders used by PathFinder.'
    
    def find_loader(self, fullname):
        '''Return (loader, namespace portion) for the path entry.

        The fullname is a str.  The namespace portion is a sequence of
        path entries contributing to part of a namespace package. The
        sequence may be empty.  If loader is not None, the portion will
        be ignored.

        The portion will be discarded if another path entry finder
        locates the module as a normal module or package.

        This method is deprecated since Python 3.4 in favor of
        finder.find_spec(). If find_spec() is provided than backwards-compatible
        functionality is provided.
        '''
        warnings.warn('PathEntryFinder.find_loader() is deprecated since Python 3.4 in favor of PathEntryFinder.find_spec() (available since 3.4)', DeprecationWarning, stacklevel = 2)
        if not hasattr(self, 'find_spec'):
            return (None, [])
        found = None.find_spec(fullname)
    # WARNING: Decompyle incomplete

    find_module = _bootstrap_external._find_module_shim
    
    def invalidate_caches(self):
        """An optional method for clearing the finder's cache, if any.
        This method is used by PathFinder.invalidate_caches().
        """
        pass


PathEntryFinder = <NODE:27>(PathEntryFinder, 'PathEntryFinder', metaclass = abc.ABCMeta)
_register(PathEntryFinder, machinery.FileFinder)

class ResourceLoader(Loader):
    '''Abstract base class for loaders which can return data from their
    back-end storage.

    This ABC represents one of the optional protocols specified by PEP 302.

    '''
    get_data = (lambda self, path: raise OSError)()


class InspectLoader(Loader):
    '''Abstract base class for loaders which support inspection about the
    modules they can load.

    This ABC represents one of the optional protocols specified by PEP 302.

    '''
    
    def is_package(self, fullname):
        '''Optional method which when implemented should return whether the
        module is a package.  The fullname is a str.  Returns a bool.

        Raises ImportError if the module cannot be found.
        '''
        raise ImportError

    
    def get_code(self, fullname):
        '''Method which returns the code object for the module.

        The fullname is a str.  Returns a types.CodeType if possible, else
        returns None if a code object does not make sense
        (e.g. built-in module). Raises ImportError if the module cannot be
        found.
        '''
        source = self.get_source(fullname)
    # WARNING: Decompyle incomplete

    get_source = (lambda self, fullname: raise ImportError)()
    source_to_code = (lambda data, path = ('<string>',): compile(data, path, 'exec', dont_inherit = True))()
    exec_module = _bootstrap_external._LoaderBasics.exec_module
    load_module = _bootstrap_external._LoaderBasics.load_module

_register(InspectLoader, machinery.BuiltinImporter, machinery.FrozenImporter, machinery.NamespaceLoader)

class ExecutionLoader(InspectLoader):
    '''Abstract base class for loaders that wish to support the execution of
    modules as scripts.

    This ABC represents one of the optional protocols specified in PEP 302.

    '''
    get_filename = (lambda self, fullname: raise ImportError)()
    
    def get_code(self, fullname):
        '''Method to return the code object for fullname.

        Should return None if not applicable (e.g. built-in module).
        Raise ImportError if the module cannot be found.
        '''
        source = self.get_source(fullname)
    # WARNING: Decompyle incomplete


_register(ExecutionLoader, machinery.ExtensionFileLoader)

class FileLoader(ExecutionLoader, ResourceLoader, _bootstrap_external.FileLoader):
    '''Abstract base class partially implementing the ResourceLoader and
    ExecutionLoader ABCs.'''
    pass

_register(FileLoader, machinery.SourceFileLoader, machinery.SourcelessFileLoader)

class SourceLoader(ExecutionLoader, ResourceLoader, _bootstrap_external.SourceLoader):
    '''Abstract base class for loading source code (and optionally any
    corresponding bytecode).

    To support loading from source code, the abstractmethods inherited from
    ResourceLoader and ExecutionLoader need to be implemented. To also support
    loading from bytecode, the optional methods specified directly by this ABC
    is required.

    Inherited abstractmethods not implemented in this ABC:

        * ResourceLoader.get_data
        * ExecutionLoader.get_filename

    '''
    
    def path_mtime(self, path):
        '''Return the (int) modification time for the path (str).'''
        if self.path_stats.__func__ is SourceLoader.path_stats:
            raise OSError
        return int(self.path_stats(path)['mtime'])

    
    def path_stats(self, path):
        """Return a metadata dict for the source pointed to by the path (str).
        Possible keys:
        - 'mtime' (mandatory) is the numeric timestamp of last source
          code modification;
        - 'size' (optional) is the size in bytes of the source code.
        """
        if self.path_mtime.__func__ is SourceLoader.path_mtime:
            raise OSError
        return {
            'mtime': self.path_mtime(path) }

    
    def set_data(self, path, data):
        '''Write the bytes to the path (if possible).

        Accepts a str path and data as bytes.

        Any needed intermediary directories are to be created. If for some
        reason the file cannot be written because of permissions, fail
        silently.
        '''
        pass


_register(SourceLoader, machinery.SourceFileLoader)
