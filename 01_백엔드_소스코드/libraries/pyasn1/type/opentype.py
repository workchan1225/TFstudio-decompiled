# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: opentype.pyc (Python 3.11)

__all__ = [
    'OpenType']

class OpenType(object):
    """Create ASN.1 type map indexed by a value

    The *OpenType* object models an untyped field of a constructed ASN.1
    type. In ASN.1 syntax it is usually represented by the
    `ANY DEFINED BY` for scalars or `SET OF ANY DEFINED BY`,
    `SEQUENCE OF ANY DEFINED BY` for container types clauses. Typically
    used together with :class:`~pyasn1.type.univ.Any` object.

    OpenType objects duck-type a read-only Python :class:`dict` objects,
    however the passed `typeMap` is not copied, but stored by reference.
    That means the user can manipulate `typeMap` at run time having this
    reflected on *OpenType* object behavior.

    The |OpenType| class models an untyped field of a constructed ASN.1
    type. In ASN.1 syntax it is usually represented by the
    `ANY DEFINED BY` for scalars or `SET OF ANY DEFINED BY`,
    `SEQUENCE OF ANY DEFINED BY` for container types clauses. Typically
    used with :class:`~pyasn1.type.univ.Any` type.

    Parameters
    ----------
    name: :py:class:`str`
        Field name

    typeMap: :py:class:`dict`
        A map of value->ASN.1 type. It's stored by reference and can be
        mutated later to register new mappings.

    Examples
    --------

    For untyped scalars:

    .. code-block:: python

        openType = OpenType(
            'id', {1: Integer(),
                   2: OctetString()}
        )
        Sequence(
            componentType=NamedTypes(
                NamedType('id', Integer()),
                NamedType('blob', Any(), openType=openType)
            )
        )

    For untyped `SET OF` or `SEQUENCE OF` vectors:

    .. code-block:: python

        openType = OpenType(
            'id', {1: Integer(),
                   2: OctetString()}
        )
        Sequence(
            componentType=NamedTypes(
                NamedType('id', Integer()),
                NamedType('blob', SetOf(componentType=Any()),
                          openType=openType)
            )
        )
    """
    
    def __init__(self, name, typeMap = (None,)):
        self._OpenType__name = name
    # WARNING: Decompyle incomplete

    name = (lambda self: self._OpenType__name)()
    
    def values(self):
        return self._OpenType__typeMap.values()

    
    def keys(self):
        return self._OpenType__typeMap.keys()

    
    def items(self):
        return self._OpenType__typeMap.items()

    
    def __contains__(self, key):
        return key in self._OpenType__typeMap

    
    def __getitem__(self, key):
        return self._OpenType__typeMap[key]

    
    def __iter__(self):
        return iter(self._OpenType__typeMap)
