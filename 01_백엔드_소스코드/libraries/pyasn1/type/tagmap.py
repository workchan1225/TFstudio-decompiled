# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tagmap.pyc (Python 3.11)

from pyasn1 import error
__all__ = [
    'TagMap']

class TagMap(object):
    '''Map *TagSet* objects to ASN.1 types

    Create an object mapping *TagSet* object to ASN.1 type.

    *TagMap* objects are immutable and duck-type read-only Python
    :class:`dict` objects holding *TagSet* objects as keys and ASN.1
    type objects as values.

    Parameters
    ----------
    presentTypes: :py:class:`dict`
        Map of :class:`~pyasn1.type.tag.TagSet` to ASN.1 objects considered
        as being unconditionally present in the *TagMap*.

    skipTypes: :py:class:`dict`
        A collection of :class:`~pyasn1.type.tag.TagSet` objects considered
        as absent in the *TagMap* even when *defaultType* is present.

    defaultType: ASN.1 type object
        An ASN.1 type object callee *TagMap* returns for any *TagSet* key not present
        in *presentTypes* (unless given key is present in *skipTypes*).
    '''
    
    def __init__(self, presentTypes, skipTypes, defaultType = (None, None, None)):
