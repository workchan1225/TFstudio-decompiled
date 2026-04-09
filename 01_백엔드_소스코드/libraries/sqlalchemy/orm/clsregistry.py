# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: clsregistry.pyc (Python 3.11)

'''Routines to handle the string class registry used by declarative.

This system allows specification of classes and expressions used in
:func:`_orm.relationship` using strings.

'''
from __future__ import annotations
import re
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import Generator
from typing import Iterable
from typing import List
from typing import Mapping
from typing import MutableMapping
from typing import NoReturn
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
import weakref
from  import attributes
from  import interfaces
from descriptor_props import SynonymProperty
from properties import ColumnProperty
from util import class_mapper
from  import exc
from  import inspection
from  import util
from sql.schema import _get_table_key
from util.typing import CallableReference
if TYPE_CHECKING:
    from relationships import RelationshipProperty
    from sql.schema import MetaData
    from sql.schema import Table
_T = TypeVar('_T', bound = Any)
_ClsRegistryType = MutableMapping[(str, Union[(type, 'ClsRegistryToken')])]
_registries: 'Set[ClsRegistryToken]' = set()

def add_class(classname = None, cls = None, decl_class_registry = None):
    '''Add a class to the _decl_class_registry associated with the
    given declarative class.

    '''
    if classname in decl_class_registry:
        existing = decl_class_registry[classname]
        if not isinstance(existing, _MultipleClassMarker):
            decl_class_registry[classname] = _MultipleClassMarker([
                cls,
                cast('Type[Any]', existing)])
        else:
            decl_class_registry[classname] = cls
    
    try:
        root_module = cast(_ModuleMarker, decl_class_registry['_sa_module_registry'])
    except KeyError:
        decl_class_registry['_sa_module_registry'] = _ModuleMarker('_sa_module_registry', None)
        root_module = _ModuleMarker('_sa_module_registry', None)

    tokens = cls.__module__.split('.')
# WARNING: Decompyle incomplete


def remove_class(classname = None, cls = None, decl_class_registry = None):
    if classname in decl_class_registry:
        existing = decl_class_registry[classname]
        if isinstance(existing, _MultipleClassMarker):
            existing.remove_item(cls)
        else:
            del decl_class_registry[classname]
    
    try:
        root_module = cast(_ModuleMarker, decl_class_registry['_sa_module_registry'])
    except KeyError:
        return None

    tokens = cls.__module__.split('.')
# WARNING: Decompyle incomplete


def _key_is_empty(key = None, decl_class_registry = None, test = None):
    '''test if a key is empty of a certain object.

    used for unit tests against the registry to see if garbage collection
    is working.

    "test" is a callable that will be passed an object should return True
    if the given object is the one we were looking for.

    We can\'t pass the actual object itself b.c. this is for testing garbage
    collection; the caller will have to have removed references to the
    object itself.

    '''
    if key not in decl_class_registry:
        return True
    thing = None[key]
    if isinstance(thing, _MultipleClassMarker):
        for sub_thing in thing.contents:
            if test(sub_thing):
                return False
            raise NotImplementedError('unknown codepath')
            return not test(thing)


class ClsRegistryToken:
    '''an object that can be in the registry._class_registry as a value.'''
    __slots__ = ()


class _MultipleClassMarker(ClsRegistryToken):
    '''refers to multiple classes of the same name
    within _decl_class_registry.

    '''
    on_remove: 'CallableReference[Optional[Callable[[], None]]]' = ('on_remove', 'contents', '__weakref__')
    
    def __init__(self = None, classes = None, on_remove = None):
        pass
    # WARNING: Decompyle incomplete

    
    def remove_item(self = None, cls = None):
        self._remove_item(weakref.ref(cls))

    
    def __iter__(self = None):
        return self.contents()

    
    def attempt_get(self = None, path = None, key = None):
        if len(self.contents) > 1:
            raise exc.InvalidRequestError('Multiple classes found for path "%s" in the registry of this declarative base. Please use a fully module-qualified path.' % '.'.join(path + [
                key]))
        ref = list(self.contents)[0]
        cls = ref()
    # WARNING: Decompyle incomplete

    
    def _remove_item(self = None, ref = None):
        self.contents.discard(ref)
        if not self.contents:
            _registries.discard(self)
            if self.on_remove:
                self.on_remove()
                return None
            return None

    
    def add_item(self = None, item = None):
        modules = list(self.contents)()()
        if item.__module__ in modules:
            util.warn(f'''This declarative base already contains a class with the same class name and module name as {item.__module__!s}.{item.__name__!s}, and will be replaced in the string-lookup table.''')
        self.contents.add(weakref.ref(item, self._remove_item))



class _ModuleMarker(ClsRegistryToken):
    '''Refers to a module name within
    _decl_class_registry.

    '''
    path: 'List[str]' = ('parent', 'name', 'contents', 'mod_ns', 'path', '__weakref__')
    
    def __init__(self = None, name = None, parent = None):
        self.parent = parent
        self.name = name
        self.contents = { }
        self.mod_ns = _ModNS(self)
        if self.parent:
            self.path = self.parent.path + [
                self.name]
        else:
            self.path = []
        _registries.add(self)

    
    def __contains__(self = None, name = None):
        return name in self.contents

    
    def __getitem__(self = None, name = None):
        return self.contents[name]

    
    def _remove_item(self = None, name = None):
        self.contents.pop(name, None)
    # WARNING: Decompyle incomplete

    
    def resolve_attr(self = None, key = None):
        return self.mod_ns.__getattr__(key)

    
    def get_module(self = None, name = None):
        if name not in self.contents:
            marker = _ModuleMarker(name, self)
            self.contents[name] = marker
        else:
            marker = cast(_ModuleMarker, self.contents[name])
        return marker

    
    def add_class(self = None, name = None, cls = None):
        pass
    # WARNING: Decompyle incomplete

    
    def remove_class(self = None, name = None, cls = None):
        if name in self.contents:
            existing = cast(_MultipleClassMarker, self.contents[name])
            existing.remove_item(cls)
            return None



class _ModNS:
    _ModNS__parent: '_ModuleMarker' = ('__parent',)
    
    def __init__(self = None, parent = None):
        self._ModNS__parent = parent

    
    def __getattr__(self = None, key = None):
        pass
    # WARNING: Decompyle incomplete



class _GetColumns:
    cls: 'Type[Any]' = ('cls',)
    
    def __init__(self = None, cls = None):
        self.cls = cls

    
    def __getattr__(self = None, key = None):
        mp = class_mapper(self.cls, configure = False)
    # WARNING: Decompyle incomplete


inspection._inspects(_GetColumns)((lambda target: inspection.inspect(target.cls)))

class _GetTable:
    metadata: 'MetaData' = ('key', 'metadata')
    
    def __init__(self = None, key = None, metadata = None):
        self.key = key
        self.metadata = metadata

    
    def __getattr__(self = None, key = None):
        return self.metadata.tables[_get_table_key(key, self.key)]



def _determine_container(key = None, value = None):
    if isinstance(value, _MultipleClassMarker):
        value = value.attempt_get([], key)
    return _GetColumns(value)


class _class_resolver:
    _resolvers: 'Tuple[Callable[[str], Any], ...]' = ('cls', 'prop', 'arg', 'fallback', '_dict', '_resolvers', 'favor_tables')
    
    def __init__(self, cls = None, prop = None, fallback = None, arg = (False,), favor_tables = ('cls', 'Type[Any]', 'prop', 'RelationshipProperty[Any]', 'fallback', 'Mapping[str, Any]', 'arg', 'str', 'favor_tables', 'bool')):
        self.cls = cls
        self.prop = prop
        self.arg = arg
        self.fallback = fallback
        self._dict = util.PopulateDict(self._access_cls)
        self._resolvers = ()
        self.favor_tables = favor_tables

    
    def _access_cls(self = None, key = None):
        cls = self.cls
        manager = attributes.manager_of_class(cls)
        decl_base = manager.registry
    # WARNING: Decompyle incomplete

    
    def _raise_for_name(self = None, name = None, err = None):
        generic_match = re.match('(.+)\\[(.+)\\]', name)
        if generic_match:
            clsarg = generic_match.group(2).strip("'")
            raise exc.InvalidRequestError(f'''When initializing mapper {self.prop.parent}, expression "relationship({self.arg!r})" seems to be using a generic class as the argument to relationship(); please state the generic argument using an annotation, e.g. "{self.prop.key}: Mapped[{generic_match.group(1)}[\'{clsarg}\']] = relationship()"'''), err
        raise exc.InvalidRequestError(f'''When initializing mapper {self.prop.parent!s}, expression {self.arg!r} failed to locate a name ({name!r}). If this is a class name, consider adding this relationship() to the {self.cls!r} class after both dependent classes have been defined.'''), err

    
    def _resolve_name(self = None):
        name = self.arg
        d = self._dict
        rval = None
    # WARNING: Decompyle incomplete

    
    def __call__(self = None):
        
        try:
            x = eval(self.arg, globals(), self._dict)
            if isinstance(x, _GetColumns):
                return x.cls
            return None
        except NameError:
            n = None
            self._raise_for_name(n.args[0], n)
            n = None
            del n
            return None
            n = None
            del n



_fallback_dict: 'Mapping[str, Any]' = None

def _resolver(cls = None, prop = None):
    pass
# WARNING: Decompyle incomplete
