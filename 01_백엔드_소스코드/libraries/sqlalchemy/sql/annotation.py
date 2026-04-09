# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: annotation.pyc (Python 3.11)

'''The :class:`.Annotated` class and related routines; creates hash-equivalent
copies of SQL constructs which contain context-specific markers and
associations.

Note that the :class:`.Annotated` concept as implemented in this module is not
related in any way to the pep-593 concept of "Annotated".


'''
from __future__ import annotations
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Dict
from typing import FrozenSet
from typing import Mapping
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from  import operators
from cache_key import HasCacheKey
from visitors import anon_map
from visitors import ExternallyTraversible
from visitors import InternalTraversal
from  import util
from util.typing import Literal
from util.typing import Self
if TYPE_CHECKING:
    from base import _EntityNamespace
    from visitors import _TraverseInternalsType
_AnnotationDict = Mapping[(str, Any)]
EMPTY_ANNOTATIONS: 'util.immutabledict[str, Any]' = util.EMPTY_DICT

class SupportsAnnotations(ExternallyTraversible):
    __slots__ = ()
    _is_immutable: 'bool' = EMPTY_ANNOTATIONS
    
    def _annotate(self = None, values = None):
        raise NotImplementedError()

    _deannotate = (lambda self = None, values = None, clone = overload: pass)()
    _deannotate = (lambda self = None, values = None, clone = overload: pass)()
    
    def _deannotate(self = None, values = None, clone = None):
        raise NotImplementedError()

    _annotations_cache_key = (lambda self = None: anon_map_ = anon_map()self._gen_annotations_cache_key(anon_map_))()
    
    def _gen_annotations_cache_key(self = None, anon_map = None):
        pass
    # WARNING: Decompyle incomplete



class SupportsWrappingAnnotations(SupportsAnnotations):
    _constructor: 'Callable[..., SupportsWrappingAnnotations]' = ()
    if TYPE_CHECKING:
        entity_namespace = (lambda self = None: pass)()
    
    def _annotate(self = None, values = None):
        '''return a copy of this ClauseElement with annotations
        updated by the given dictionary.

        '''
        return Annotated._as_annotated_instance(self, values)

    
    def _with_annotations(self = None, values = None):
        '''return a copy of this ClauseElement with annotations
        replaced by the given dictionary.

        '''
        return Annotated._as_annotated_instance(self, values)

    _deannotate = (lambda self = None, values = None, clone = overload: pass)()
    _deannotate = (lambda self = None, values = None, clone = overload: pass)()
    
    def _deannotate(self = None, values = None, clone = None):
        '''return a copy of this :class:`_expression.ClauseElement`
        with annotations
        removed.

        :param values: optional tuple of individual values
         to remove.

        '''
        if clone:
            s = self._clone()
            return s



class SupportsCloneAnnotations(SupportsWrappingAnnotations):
    if not typing.TYPE_CHECKING:
        __slots__ = ()
    _clone_annotations_traverse_internals: '_TraverseInternalsType' = [
        ('_annotations', InternalTraversal.dp_annotations_key)]
    
    def _annotate(self = None, values = None):
        '''return a copy of this ClauseElement with annotations
        updated by the given dictionary.

        '''
        new = self._clone()
        new._annotations = new._annotations.union(values)
        new.__dict__.pop('_annotations_cache_key', None)
        new.__dict__.pop('_generate_cache_key', None)
        return new

    
    def _with_annotations(self = None, values = None):
        '''return a copy of this ClauseElement with annotations
        replaced by the given dictionary.

        '''
        new = self._clone()
        new._annotations = util.immutabledict(values)
        new.__dict__.pop('_annotations_cache_key', None)
        new.__dict__.pop('_generate_cache_key', None)
        return new

    _deannotate = (lambda self = None, values = None, clone = overload: pass)()
    _deannotate = (lambda self = None, values = None, clone = overload: pass)()
    
    def _deannotate(self = None, values = None, clone = None):
        '''return a copy of this :class:`_expression.ClauseElement`
        with annotations
        removed.

        :param values: optional tuple of individual values
         to remove.

        '''
        if clone or self._annotations:
            new = self._clone()
            new._annotations = util.immutabledict()
            new.__dict__.pop('_annotations_cache_key', None)
            return new



class Annotated(SupportsAnnotations):
    '''clones a SupportsAnnotations and applies an \'annotations\' dictionary.

    Unlike regular clones, this clone also mimics __hash__() and
    __eq__() of the original element so that it takes its place
    in hashed collections.

    A reference to the original element is maintained, for the important
    reason of keeping its hash value current.  When GC\'ed, the
    hash value may be reused, causing conflicts.

    .. note::  The rationale for Annotated producing a brand new class,
       rather than placing the functionality directly within ClauseElement,
       is **performance**.  The __hash__() method is absent on plain
       ClauseElement which leads to significantly reduced function call
       overhead, as the use of sets and dictionaries against ClauseElement
       objects is prevalent, but most are not "annotated".

    '''
    _is_column_operators = False
    _hash: 'int' = (lambda cls = None, element = None, values = classmethod: try:
cls = annotated_classes[element.__class__]except KeyError:
cls = _new_annotation_type(element.__class__, cls)cls(element, values))()
    
    def __new__(cls = None, *args):
        return object.__new__(cls)

    
    def __init__(self = None, element = None, values = None):
        self.__dict__ = element.__dict__.copy()
        self.__dict__.pop('_annotations_cache_key', None)
        self.__dict__.pop('_generate_cache_key', None)
        self._Annotated__element = element
        self._annotations = util.immutabledict(values)
        self._hash = hash(element)

    
    def _annotate(self = None, values = None):
        _values = self._annotations.union(values)
        new = self._with_annotations(_values)
        return new

    
    def _with_annotations(self = None, values = None):
        clone = self.__class__.__new__(self.__class__)
        clone.__dict__ = self.__dict__.copy()
        clone.__dict__.pop('_annotations_cache_key', None)
        clone.__dict__.pop('_generate_cache_key', None)
        clone._annotations = util.immutabledict(values)
        return clone

    _deannotate = (lambda self = None, values = None, clone = overload: pass)()
    _deannotate = (lambda self = None, values = None, clone = overload: pass)()
    
    def _deannotate(self = None, values = None, clone = None):
        pass
    # WARNING: Decompyle incomplete

    if not typing.TYPE_CHECKING:
        
        def _compiler_dispatch(self = None, visitor = None, **kw):
            pass
        # WARNING: Decompyle incomplete

        _constructor = (lambda self: self._Annotated__element._constructor)()
    
    def _clone(self = None, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def __reduce__(self = None):
        return (self.__class__, (self._Annotated__element, self._annotations))

    
    def __hash__(self = None):
        return self._hash

    
    def __eq__(self = None, other = None):
        if self._is_column_operators:
            return self._Annotated__element.__class__.__eq__(self, other)
        return None(other) == hash(self)

    entity_namespace = (lambda self = None: if 'entity_namespace' in self._annotations:
cast(SupportsWrappingAnnotations, self._annotations['entity_namespace']).entity_namespaceNone._Annotated__element.entity_namespace)()

annotated_classes: 'Dict[Type[SupportsWrappingAnnotations], Type[Annotated]]' = { }
_SA = TypeVar('_SA', bound = 'SupportsAnnotations')

def _safe_annotate(to_annotate = None, annotations = None):
    
    try:
        _annotate = to_annotate._annotate
        return _annotate(annotations)
    except AttributeError:
        return 



def _deep_annotate(element = None, annotations = None, exclude = None, *, detect_subquery_cols, ind_cols_on_fromclause, annotate_callable):
    '''Deep copy the given ClauseElement, annotating each element
    with the given annotations dictionary.

    Elements within the exclude collection will be cloned but not annotated.

    '''
    pass
# WARNING: Decompyle incomplete

_deep_deannotate = (lambda element = None, values = None: pass)()
_deep_deannotate = (lambda element = None, values = None: pass)()

def _deep_deannotate(element = None, values = None):
    '''Deep copy the given element, removing annotations.'''
    pass
# WARNING: Decompyle incomplete


def _shallow_annotate(element = None, annotations = None):
    '''Annotate the given ClauseElement and copy its internals so that
    internal objects refer to the new annotated object.

    Basically used to apply a "don\'t traverse" annotation to a
    selectable, without digging throughout the whole
    structure wasting time.
    '''
    element = element._annotate(annotations)
    element._copy_internals()
    return element


def _new_annotation_type(cls = None, base_cls = None):
    '''Generates a new class that subclasses Annotated and proxies a given
    element type.

    '''
    if issubclass(cls, Annotated):
        return cls
    if None in annotated_classes:
        return annotated_classes[cls]
    for super_ in None.__mro__:
        if super_ in annotated_classes:
            base_cls = annotated_classes[super_]
        
        annotated_classes[cls] = cast(Type[Annotated], type('Annotated%s' % cls.__name__, (base_cls, cls), { }))
        anno_cls = cast(Type[Annotated], type('Annotated%s' % cls.__name__, (base_cls, cls), { }))
        globals()['Annotated%s' % cls.__name__] = anno_cls
        if '_traverse_internals' in cls.__dict__:
            anno_cls._traverse_internals = list(cls._traverse_internals) + [
                ('_annotations', InternalTraversal.dp_annotations_key)]
        elif cls.__dict__.get('inherit_cache', False):
            anno_cls._traverse_internals = list(cls._traverse_internals) + [
                ('_annotations', InternalTraversal.dp_annotations_key)]
    if cls.__dict__.get('inherit_cache', False):
        anno_cls.inherit_cache = True
    elif 'inherit_cache' in cls.__dict__:
        anno_cls.inherit_cache = cls.__dict__['inherit_cache']
    anno_cls._is_column_operators = issubclass(cls, operators.ColumnOperators)
    return anno_cls


def _prepare_annotations(target_hierarchy = None, base_cls = None):
    for cls in util.walk_subclasses(target_hierarchy):
        _new_annotation_type(cls, base_cls)
        return None
