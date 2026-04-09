# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: minicompat.pyc (Python 3.11)

'''Python version compatibility support for minidom.

This module contains internal implementation details and
should not be imported; use xml.dom.minidom instead.
'''
__all__ = [
    'NodeList',
    'EmptyNodeList',
    'StringTypes',
    'defproperty']
import xml.dom as xml
StringTypes = (str,)

class NodeList(list):
    __slots__ = ()
    
    def item(self, index):
        if  <= 0, index or 0, index < len(self):
            pass
        else:
            return None
        return None[index]

    
    def _get_length(self):
        return len(self)

    
    def _set_length(self, value):
        raise xml.dom.NoModificationAllowedErr("attempt to modify read-only attribute 'length'")

    length = property(_get_length, _set_length, doc = 'The number of nodes in the NodeList.')
    
    def __setstate__(self, state):
        pass
    # WARNING: Decompyle incomplete



class EmptyNodeList(tuple):
    __slots__ = ()
    
    def __add__(self, other):
        NL = NodeList()
        NL.extend(other)
        return NL

    
    def __radd__(self, other):
        NL = NodeList()
        NL.extend(other)
        return NL

    
    def item(self, index):
        pass

    
    def _get_length(self):
        return 0

    
    def _set_length(self, value):
        raise xml.dom.NoModificationAllowedErr("attempt to modify read-only attribute 'length'")

    length = property(_get_length, _set_length, doc = 'The number of nodes in the NodeList.')


def defproperty(klass, name, doc):
    get = getattr(klass, '_get_' + name)
    
    def set(self, value, name = (name,)):
        raise xml.dom.NoModificationAllowedErr('attempt to modify read-only attribute ' + repr(name))

# WARNING: Decompyle incomplete
