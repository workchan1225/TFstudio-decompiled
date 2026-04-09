# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: readers.pyc (Python 3.11)

import collections
import operator
import pathlib
import zipfile
from  import abc
from _itertools import unique_everseen

def remove_duplicates(items):
    return iter(collections.OrderedDict.fromkeys(items))


class FileReader(abc.TraversableResources):
    
    def __init__(self, loader):
        self.path = pathlib.Path(loader.path).parent

    
    def resource_path(self, resource):
        '''
        Return the file system path to prevent
        `resources.path()` from creating a temporary
        copy.
        '''
        return str(self.path.joinpath(resource))

    
    def files(self):
        return self.path



class ZipReader(abc.TraversableResources):
    pass
# WARNING: Decompyle incomplete


class MultiplexedPath(abc.Traversable):
    '''
    Given a series of Traversable objects, implement a merged
    version of the interface across all objects. Useful for
    namespace packages which may be multihomed at a single
    name.
    '''
    
    def __init__(self, *paths):
        self._paths = list(map(pathlib.Path, remove_duplicates(paths)))
        if not self._paths:
            message = 'MultiplexedPath must contain at least one path'
            raise FileNotFoundError(message)
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(self._paths()):
            raise NotADirectoryError('MultiplexedPath only supports directories')

    
    def iterdir(self):
        files = self._paths()
        return unique_everseen(files, key = operator.attrgetter('name'))

    
    def read_bytes(self):
        raise FileNotFoundError(f'''{self} is not a file''')

    
    def read_text(self, *args, **kwargs):
        raise FileNotFoundError(f'''{self} is not a file''')

    
    def is_dir(self):
        return True

    
    def is_file(self):
        return False

    
    def joinpath(self, child):
        for file in self.iterdir():
            if file.name == child:
                
                return None, file
            return self._paths[0] / child

    __truediv__ = joinpath
    
    def open(self, *args, **kwargs):
        raise FileNotFoundError(f'''{self} is not a file''')

    name = (lambda self: self._paths[0].name)()
    
    def __repr__(self):
        paths = (lambda .0: pass# WARNING: Decompyle incomplete
)(self._paths())
        return f'''MultiplexedPath({paths})'''



class NamespaceReader(abc.TraversableResources):
    
    def __init__(self, namespace_path):
        if 'NamespacePath' not in str(namespace_path):
            raise ValueError('Invalid path')
    # WARNING: Decompyle incomplete

    
    def resource_path(self, resource):
        '''
        Return the file system path to prevent
        `resources.path()` from creating a temporary
        copy.
        '''
        return str(self.path.joinpath(resource))

    
    def files(self):
        return self.path
