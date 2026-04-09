# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mapped_collection.pyc (Python 3.11)

from __future__ import annotations
import operator
from typing import Any
from typing import Callable
from typing import Dict
from typing import Generic
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import base
from collections import collection
from collections import collection_adapter
from  import exc as sa_exc
from  import util
from sql import coercions
from sql import expression
from sql import roles
from util.langhelpers import Missing
from util.langhelpers import MissingOr
from util.typing import Literal
if TYPE_CHECKING:
    from  import AttributeEventToken
    from  import Mapper
    from collections import CollectionAdapter
    from sql.elements import ColumnElement
_KT = TypeVar('_KT', bound = Any)
_VT = TypeVar('_VT', bound = Any)

def _PlainColumnGetter():
    '''_PlainColumnGetter'''
    __doc__ = 'Plain column getter, stores collection of Column objects\n    directly.\n\n    Serializes to a :class:`._SerializableColumnGetterV2`\n    which has more expensive __call__() performance\n    and some rare caveats.\n\n    '
    __slots__ = ('cols', 'composite')
    
    def __init__(self = None, cols = None):
        self.cols = cols
        self.composite = len(cols) > 1

    
    def __reduce__(self = None):
        return _SerializableColumnGetterV2._reduce_from_cols(self.cols)

    
    def _cols(self = None, mapper = None):
        return self.cols

    
    def __call__(self = None, value = None):
        pass
    # WARNING: Decompyle incomplete


_PlainColumnGetter = <NODE:27>(_PlainColumnGetter, '_PlainColumnGetter', Generic[_KT])

def _SerializableColumnGetterV2():
    '''_SerializableColumnGetterV2'''
    __doc__ = 'Updated serializable getter which deals with\n    multi-table mapped classes.\n\n    Two extremely unusual cases are not supported.\n    Mappings which have tables across multiple metadata\n    objects, or which are mapped to non-Table selectables\n    linked across inheriting mappers may fail to function\n    here.\n\n    '
    __slots__ = ('colkeys',)
    
    def __init__(self = None, colkeys = None):
        self.colkeys = colkeys
        self.composite = len(colkeys) > 1

    
    def __reduce__(self = None):
        return (self.__class__, (self.colkeys,))

    _reduce_from_cols = (lambda cls = None, cols = None: pass# WARNING: Decompyle incomplete
)()
    
    def _cols(self = None, mapper = None):
        cols = []
        metadata = getattr(mapper.local_table, 'metadata', None)
    # WARNING: Decompyle incomplete


_SerializableColumnGetterV2 = <NODE:27>(_SerializableColumnGetterV2, '_SerializableColumnGetterV2', _PlainColumnGetter[_KT])

def column_keyed_dict(mapping_spec = None, *, ignore_unpopulated_attribute):
    '''A dictionary-based collection type with column-based keying.

    .. versionchanged:: 2.0 Renamed :data:`.column_mapped_collection` to
       :class:`.column_keyed_dict`.

    Returns a :class:`.KeyFuncDict` factory which will produce new
    dictionary keys based on the value of a particular :class:`.Column`-mapped
    attribute on ORM mapped instances to be added to the dictionary.

    .. note:: the value of the target attribute must be assigned with its
       value at the time that the object is being added to the
       dictionary collection.   Additionally, changes to the key attribute
       are **not tracked**, which means the key in the dictionary is not
       automatically synchronized with the key value on the target object
       itself.  See :ref:`key_collections_mutations` for further details.

    .. seealso::

        :ref:`orm_dictionary_collection` - background on use

    :param mapping_spec: a :class:`_schema.Column` object that is expected
     to be mapped by the target mapper to a particular attribute on the
     mapped class, the value of which on a particular instance is to be used
     as the key for a new dictionary entry for that instance.
    :param ignore_unpopulated_attribute:  if True, and the mapped attribute
     indicated by the given :class:`_schema.Column` target attribute
     on an object is not populated at all, the operation will be silently
     skipped.  By default, an error is raised.

     .. versionadded:: 2.0 an error is raised by default if the attribute
        being used for the dictionary key is determined that it was never
        populated with any value.  The
        :paramref:`_orm.column_keyed_dict.ignore_unpopulated_attribute`
        parameter may be set which will instead indicate that this condition
        should be ignored, and the append operation silently skipped.
        This is in contrast to the behavior of the 1.x series which would
        erroneously populate the value in the dictionary with an arbitrary key
        value of ``None``.


    '''
    cols = util.to_list(mapping_spec)()
    keyfunc = _PlainColumnGetter(cols)
    return _mapped_collection_cls(keyfunc, ignore_unpopulated_attribute = ignore_unpopulated_attribute)


class _AttrGetter:
    __slots__ = ('attr_name', 'getter')
    
    def __init__(self = None, attr_name = None):
        self.attr_name = attr_name
        self.getter = operator.attrgetter(attr_name)

    
    def __call__(self = None, mapped_object = None):
        obj = self.getter(mapped_object)
    # WARNING: Decompyle incomplete

    
    def __reduce__(self = None):
        return (_AttrGetter, (self.attr_name,))



def attribute_keyed_dict(attr_name = None, *, ignore_unpopulated_attribute):
    '''A dictionary-based collection type with attribute-based keying.

    .. versionchanged:: 2.0 Renamed :data:`.attribute_mapped_collection` to
       :func:`.attribute_keyed_dict`.

    Returns a :class:`.KeyFuncDict` factory which will produce new
    dictionary keys based on the value of a particular named attribute on
    ORM mapped instances to be added to the dictionary.

    .. note:: the value of the target attribute must be assigned with its
       value at the time that the object is being added to the
       dictionary collection.   Additionally, changes to the key attribute
       are **not tracked**, which means the key in the dictionary is not
       automatically synchronized with the key value on the target object
       itself.  See :ref:`key_collections_mutations` for further details.

    .. seealso::

        :ref:`orm_dictionary_collection` - background on use

    :param attr_name: string name of an ORM-mapped attribute
     on the mapped class, the value of which on a particular instance
     is to be used as the key for a new dictionary entry for that instance.
    :param ignore_unpopulated_attribute:  if True, and the target attribute
     on an object is not populated at all, the operation will be silently
     skipped.  By default, an error is raised.

     .. versionadded:: 2.0 an error is raised by default if the attribute
        being used for the dictionary key is determined that it was never
        populated with any value.  The
        :paramref:`_orm.attribute_keyed_dict.ignore_unpopulated_attribute`
        parameter may be set which will instead indicate that this condition
        should be ignored, and the append operation silently skipped.
        This is in contrast to the behavior of the 1.x series which would
        erroneously populate the value in the dictionary with an arbitrary key
        value of ``None``.


    '''
    return _mapped_collection_cls(_AttrGetter(attr_name), ignore_unpopulated_attribute = ignore_unpopulated_attribute)


def keyfunc_mapping(keyfunc = None, *, ignore_unpopulated_attribute):
    '''A dictionary-based collection type with arbitrary keying.

    .. versionchanged:: 2.0 Renamed :data:`.mapped_collection` to
       :func:`.keyfunc_mapping`.

    Returns a :class:`.KeyFuncDict` factory with a keying function
    generated from keyfunc, a callable that takes an entity and returns a
    key value.

    .. note:: the given keyfunc is called only once at the time that the
       target object is being added to the collection.   Changes to the
       effective value returned by the function are not tracked.


    .. seealso::

        :ref:`orm_dictionary_collection` - background on use

    :param keyfunc: a callable that will be passed the ORM-mapped instance
     which should then generate a new key to use in the dictionary.
     If the value returned is :attr:`.LoaderCallableStatus.NO_VALUE`, an error
     is raised.
    :param ignore_unpopulated_attribute:  if True, and the callable returns
     :attr:`.LoaderCallableStatus.NO_VALUE` for a particular instance, the
     operation will be silently skipped.  By default, an error is raised.

     .. versionadded:: 2.0 an error is raised by default if the callable
        being used for the dictionary key returns
        :attr:`.LoaderCallableStatus.NO_VALUE`, which in an ORM attribute
        context indicates an attribute that was never populated with any value.
        The :paramref:`_orm.mapped_collection.ignore_unpopulated_attribute`
        parameter may be set which will instead indicate that this condition
        should be ignored, and the append operation silently skipped. This is
        in contrast to the behavior of the 1.x series which would erroneously
        populate the value in the dictionary with an arbitrary key value of
        ``None``.


    '''
    return _mapped_collection_cls(keyfunc, ignore_unpopulated_attribute = ignore_unpopulated_attribute)


def KeyFuncDict():
    '''KeyFuncDict'''
    pass
# WARNING: Decompyle incomplete

KeyFuncDict = <NODE:27>(KeyFuncDict, 'KeyFuncDict', Dict[(_KT, _VT)])

def _mapped_collection_cls(keyfunc = None, ignore_unpopulated_attribute = None):
    pass
# WARNING: Decompyle incomplete

MappedCollection = KeyFuncDict
mapped_collection = keyfunc_mapping
attribute_mapped_collection = attribute_keyed_dict
column_mapped_collection = column_keyed_dict
