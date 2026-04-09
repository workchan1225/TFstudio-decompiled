# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: simple.pyc (Python 3.11)

'''
Interface adapters for low-level readers.
'''
import abc
import io
import itertools
from typing import BinaryIO, List
from abc import Traversable, TraversableResources

class SimpleReader(abc.ABC):
    '''
    The minimum, low-level interface required from a resource
    provider.
    '''
    package = (lambda self: pass)()
    children = (lambda self: pass)()
    resources = (lambda self: pass)()
    open_binary = (lambda self, resource: pass)()
    name = (lambda self: self.package.split('.')[-1])()


class ResourceHandle(Traversable):
    '''
    Handle to a named resource in a ResourceReader.
    '''
    
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name

    
    def is_file(self):
        return True

    
    def is_dir(self):
        return False

    
    def open(self, mode = ('r',), *args, **kwargs):
        stream = self.parent.reader.open_binary(self.name)
    # WARNING: Decompyle incomplete

    
    def joinpath(self, name):
        raise RuntimeError('Cannot traverse into a resource')



class ResourceContainer(Traversable):
    """
    Traversable container for a package's resources via its reader.
    """
    
    def __init__(self, reader):
        self.reader = reader

    
    def is_dir(self):
        return True

    
    def is_file(self):
        return False

    
    def iterdir(self):
        pass
    # WARNING: Decompyle incomplete

    
    def open(self, *args, **kwargs):
        raise IsADirectoryError()

    
    def joinpath(self, name):
        pass
    # WARNING: Decompyle incomplete



class TraversableReader(SimpleReader, TraversableResources):
    '''
    A TraversableResources based on SimpleReader. Resource providers
    may derive from this class to provide the TraversableResources
    interface by supplying the SimpleReader interface.
    '''
    
    def files(self):
        return ResourceContainer(self)
