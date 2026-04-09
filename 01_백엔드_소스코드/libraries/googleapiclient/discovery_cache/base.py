# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''An abstract class for caching the discovery document.'''
import abc

class Cache(object):
    '''A base abstract cache class.'''
    __metaclass__ = abc.ABCMeta
    get = (lambda self, url: raise NotImplementedError())()
    set = (lambda self, url, content: raise NotImplementedError())()
