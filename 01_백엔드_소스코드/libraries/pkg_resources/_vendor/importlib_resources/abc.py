# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: abc.pyc (Python 3.11)

import abc
from typing import BinaryIO, Iterable, Text
from _compat import runtime_checkable, Protocol

def ResourceReader():
    '''ResourceReader'''
    __doc__ = 'Abstract base class for loaders to provide resource reading support.'
    open_resource = (lambda self = None, resource = None: raise FileNotFoundError)()
    resource_path = (lambda self = None, resource = None: raise FileNotFoundError)()
    is_resource = (lambda self = None, path = None: raise FileNotFoundError)()
    contents = (lambda self = None: raise FileNotFoundError)()

ResourceReader = <NODE:27>(ResourceReader, 'ResourceReader', metaclass = abc.ABCMeta)
Traversable = <NODE:12>()

class TraversableResources(ResourceReader):
    '''
    The required interface for providing traversable
    resources.
    '''
    files = (lambda self: pass)()
    
    def open_resource(self, resource):
        return self.files().joinpath(resource).open('rb')

    
    def resource_path(self, resource):
        raise FileNotFoundError(resource)

    
    def is_resource(self, path):
        return self.files().joinpath(path).is_file()

    
    def contents(self):
        return self.files().iterdir()()
