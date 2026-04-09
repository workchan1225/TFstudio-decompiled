# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: namedtype.pyc (Python 3.11)

import sys
from pyasn1 import error
from pyasn1.type import tag
from pyasn1.type import tagmap
__all__ = [
    'NamedType',
    'OptionalNamedType',
    'DefaultedNamedType',
    'NamedTypes']

class NamedType(object):
    '''Create named field object for a constructed ASN.1 type.

    The |NamedType| object represents a single name and ASN.1 type of a constructed ASN.1 type.

    |NamedType| objects are immutable and duck-type Python :class:`tuple` objects
    holding *name* and *asn1Object* components.

    Parameters
    ----------
    name: :py:class:`str`
        Field name

    asn1Object:
        ASN.1 type object
    '''
    isOptional = False
    isDefaulted = False
    
    def __init__(self, name, asn1Object, openType = (None,)):
        self._NamedType__name = name
        self._NamedType__type = asn1Object
        self._NamedType__nameAndType = (name, asn1Object)
        self._NamedType__openType = openType

    
    def __repr__(self):
        representation = f'''{self.name!s}={self.asn1Object!r}'''
        if self.openType:
            representation += ', open type %r' % self.openType
        return f'''<{self.__class__.__name__!s} object, type {representation!s}>'''

    
    def __eq__(self, other):
        return self._NamedType__nameAndType == other

    
    def __ne__(self, other):
        return self._NamedType__nameAndType != other

    
    def __lt__(self, other):
        return self._NamedType__nameAndType < other

    
    def __le__(self, other):
        return self._NamedType__nameAndType <= other

    
    def __gt__(self, other):
        return self._NamedType__nameAndType > other

    
    def __ge__(self, other):
        return self._NamedType__nameAndType >= other

    
    def __hash__(self):
        return hash(self._NamedType__nameAndType)

    
    def __getitem__(self, idx):
        return self._NamedType__nameAndType[idx]

    
    def __iter__(self):
        return iter(self._NamedType__nameAndType)

    name = (lambda self: self._NamedType__name)()
    asn1Object = (lambda self: self._NamedType__type)()
    openType = (lambda self: self._NamedType__openType)()
    
    def getName(self):
        return self.name

    
    def getType(self):
        return self.asn1Object



class OptionalNamedType(NamedType):
    __doc__ = NamedType.__doc__
    isOptional = True


class DefaultedNamedType(NamedType):
    __doc__ = NamedType.__doc__
    isDefaulted = True


class NamedTypes(object):
    """Create a collection of named fields for a constructed ASN.1 type.

    The NamedTypes object represents a collection of named fields of a constructed ASN.1 type.

    *NamedTypes* objects are immutable and duck-type Python :class:`dict` objects
    holding *name* as keys and ASN.1 type object as values.

    Parameters
    ----------
    *namedTypes: :class:`~pyasn1.type.namedtype.NamedType`

    Examples
    --------

    .. code-block:: python

        class Description(Sequence):
            '''
            ASN.1 specification:

            Description ::= SEQUENCE {
                surname    IA5String,
                first-name IA5String OPTIONAL,
                age        INTEGER DEFAULT 40
            }
            '''
            componentType = NamedTypes(
                NamedType('surname', IA5String()),
                OptionalNamedType('first-name', IA5String()),
                DefaultedNamedType('age', Integer(40))
            )

        descr = Description()
        descr['surname'] = 'Smith'
        descr['first-name'] = 'John'
    """
    
    def __init__(self, *namedTypes, **kwargs):
