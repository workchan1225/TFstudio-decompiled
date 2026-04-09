# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

import sys
from pyasn1 import error
from pyasn1.type import constraint
from pyasn1.type import tag
from pyasn1.type import tagmap
__all__ = [
    'Asn1Item',
    'Asn1Type',
    'SimpleAsn1Type',
    'ConstructedAsn1Type']

class Asn1Item(object):
    getTypeId = (lambda cls, increment = (1,): try:
passexcept AttributeError:
increment = NoneAsn1Item._typeCounter)()


class Asn1Type(Asn1Item):
    '''Base class for all classes representing ASN.1 types.

    In the user code, |ASN.1| class is normally used only for telling
    ASN.1 objects from others.

    Note
    ----
    For as long as ASN.1 is concerned, a way to compare ASN.1 types
    is to use :meth:`isSameTypeWith` and :meth:`isSuperTypeOf` methods.
    '''
    tagSet = tag.TagSet()
    subtypeSpec = constraint.ConstraintsIntersection()
    typeId = None
    
    def __init__(self, **kwargs):
        readOnly = {
            'tagSet': self.tagSet,
            'subtypeSpec': self.subtypeSpec }
        readOnly.update(kwargs)
        self.__dict__.update(readOnly)
        self._readOnly = readOnly

    
    def __setattr__(self, name, value):
        if name[0] != '_' and name in self._readOnly:
            raise error.PyAsn1Error('read-only instance attribute "%s"' % name)
        self.__dict__[name] = value

    
    def __str__(self):
        return self.prettyPrint()

    readOnly = (lambda self: self._readOnly)()
    effectiveTagSet = (lambda self: self.tagSet)()
    tagMap = (lambda self: tagmap.TagMap({
self.tagSet: self }))()
    
    def isSameTypeWith(self, other, matchTags, matchConstraints = (True, True)):
