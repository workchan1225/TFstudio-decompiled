# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: visitors.pyc (Python 3.11)

'''Visitor/traversal interface and library functions.'''
from __future__ import annotations
from collections import deque
from enum import Enum
import itertools
import operator
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import ClassVar
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import Optional
from typing import overload
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import exc
from  import util
from util import langhelpers
from util._has_cy import HAS_CYEXTENSION
from util.typing import Literal
from util.typing import Protocol
from util.typing import Self
if TYPE_CHECKING:
    from annotation import _AnnotationDict
    from elements import ColumnElement
if not typing.TYPE_CHECKING or HAS_CYEXTENSION:
    from _py_util import prefix_anon_map
    from _py_util import cache_anon_map as anon_map
else:
    from sqlalchemy.cyextension.util import prefix_anon_map
    from sqlalchemy.cyextension.util import cache_anon_map as anon_map
__all__ = [
    'iterate',
    'traverse_using',
    'traverse',
    'cloned_traverse',
    'replacement_traverse',
    'Visitable',
    'ExternalTraversal',
    'InternalTraversal',
    'anon_map']

class _CompilerDispatchType(Protocol):
    
    def __call__(_self = None, self = None, visitor = None, **kw):
        pass



class Visitable:
    pass
# WARNING: Decompyle incomplete


class InternalTraversal(Enum):
    '''Defines visitor symbols used for internal traversal.

    The :class:`.InternalTraversal` class is used in two ways.  One is that
    it can serve as the superclass for an object that implements the
    various visit methods of the class.   The other is that the symbols
    themselves of :class:`.InternalTraversal` are used within
    the ``_traverse_internals`` collection.   Such as, the :class:`.Case`
    object defines ``_traverse_internals`` as ::

        class Case(ColumnElement[_T]):
            _traverse_internals = [
                ("value", InternalTraversal.dp_clauseelement),
                ("whens", InternalTraversal.dp_clauseelement_tuples),
                ("else_", InternalTraversal.dp_clauseelement),
            ]

    Above, the :class:`.Case` class indicates its internal state as the
    attributes named ``value``, ``whens``, and ``else_``.    They each
    link to an :class:`.InternalTraversal` method which indicates the type
    of datastructure to which each attribute refers.

    Using the ``_traverse_internals`` structure, objects of type
    :class:`.InternalTraversible` will have the following methods automatically
    implemented:

    * :meth:`.HasTraverseInternals.get_children`

    * :meth:`.HasTraverseInternals._copy_internals`

    * :meth:`.HasCacheKey._gen_cache_key`

    Subclasses can also implement these methods directly, particularly for the
    :meth:`.HasTraverseInternals._copy_internals` method, when special steps
    are needed.

    .. versionadded:: 1.4

    '''
    dp_has_cache_key = 'HC'
    dp_has_cache_key_list = 'HL'
    dp_clauseelement = 'CE'
    dp_fromclause_canonical_column_collection = 'FC'
    dp_clauseelement_tuples = 'CTS'
    dp_clauseelement_list = 'CL'
    dp_clauseelement_tuple = 'CT'
    dp_executable_options = 'EO'
    dp_with_context_options = 'WC'
    dp_fromclause_ordered_set = 'CO'
    dp_string = 'S'
    dp_string_list = 'SL'
    dp_anon_name = 'AN'
    dp_boolean = 'B'
    dp_operator = 'O'
    dp_type = 'T'
    dp_plain_dict = 'PD'
    dp_dialect_options = 'DO'
    dp_string_clauseelement_dict = 'CD'
    dp_string_multi_dict = 'MD'
    dp_annotations_key = 'AK'
    dp_plain_obj = 'PO'
    dp_named_ddl_element = 'DD'
    dp_prefix_sequence = 'PS'
    dp_table_hint_list = 'TH'
    dp_setup_join_tuple = 'SJ'
    dp_memoized_select_entities = 'ME'
    dp_statement_hint_list = 'SH'
    dp_unknown_structure = 'UK'
    dp_dml_ordered_values = 'DML_OV'
    dp_dml_values = 'DML_V'
    dp_dml_multi_values = 'DML_MV'
    dp_propagate_attrs = 'PA'
    dp_ignore = 'IG'
    dp_inspectable = 'IS'
    dp_multi = 'M'
    dp_multi_list = 'MT'
    dp_has_cache_key_tuples = 'HT'
    dp_inspectable_list = 'IL'

_TraverseInternalsType = List[Tuple[(str, InternalTraversal)]]

class HasTraverseInternals:
    '''base for classes that have a "traverse internals" element,
    which defines all kinds of ways of traversing the elements of an object.

    Compared to :class:`.Visitable`, which relies upon an external visitor to
    define how the object is travered (i.e. the :class:`.SQLCompiler`), the
    :class:`.HasTraverseInternals` interface allows classes to define their own
    traversal, that is, what attributes are accessed and in what order.

    '''
    _traverse_internals: '_TraverseInternalsType' = ()
    _is_immutable: 'bool' = False
    get_children = (lambda self = None, *, omit_attrs: pass# WARNING: Decompyle incomplete
)()


class _InternalTraversalDispatchType(Protocol):
    
    def __call__(s = None, self = None, visitor = None):
        pass



class HasTraversalDispatch:
    '''Define infrastructure for classes that perform internal traversals

    .. versionadded:: 2.0

    '''
    __slots__ = ()
    _dispatch_lookup: 'ClassVar[Dict[Union[InternalTraversal, str], str]]' = { }
    
    def dispatch(self = None, visit_symbol = None):
        '''Given a method from :class:`.HasTraversalDispatch`, return the
        corresponding method on a subclass.

        '''
        name = _dispatch_lookup[visit_symbol]
        return getattr(self, name, None)

    
    def run_generated_dispatch(self = None, target = None, internal_dispatch = None, generate_dispatcher_name = ('target', 'object', 'internal_dispatch', '_TraverseInternalsType', 'generate_dispatcher_name', 'str', 'return', 'Any')):
        
        try:
            dispatcher = target.__class__.__dict__[generate_dispatcher_name]
        except KeyError:
            dispatcher = self.generate_dispatch(target.__class__, internal_dispatch, generate_dispatcher_name)

        return dispatcher(target, self)

    
    def generate_dispatch(self = None, target_cls = None, internal_dispatch = None, generate_dispatcher_name = ('target_cls', 'Type[object]', 'internal_dispatch', '_TraverseInternalsType', 'generate_dispatcher_name', 'str', 'return', '_InternalTraversalDispatchType')):
        dispatcher = self._generate_dispatcher(internal_dispatch, generate_dispatcher_name)
        setattr(target_cls, generate_dispatcher_name, dispatcher)
        return dispatcher

    
    def _generate_dispatcher(self = None, internal_dispatch = None, method_name = None):
        names = []
    # WARNING: Decompyle incomplete


ExtendedInternalTraversal = InternalTraversal

def _generate_traversal_dispatch():
    lookup = _dispatch_lookup
# WARNING: Decompyle incomplete

_dispatch_lookup = HasTraversalDispatch._dispatch_lookup
_generate_traversal_dispatch()

class ExternallyTraversible(Visitable, HasTraverseInternals):
    __slots__ = ()
    _annotations: 'Mapping[Any, Any]' = util.EMPTY_DICT
    if typing.TYPE_CHECKING:
        
        def _annotate(self = None, values = None):
            pass

        
        def get_children(self = None, *, omit_attrs, **kw):
            pass

    
    def _clone(self = None, **kw):
        '''clone this element'''
        raise NotImplementedError()

    
    def _copy_internals(self = None, *, omit_attrs, **kw):
        '''Reassign internal elements to be clones of themselves.

        Called during a copy-and-traverse operation on newly
        shallow-copied elements to create a deep copy.

        The given clone function should be used, which may be applying
        additional transformations to the element (i.e. replacement
        traversal, cloned traversal, annotations).

        '''
        raise NotImplementedError()


_ET = TypeVar('_ET', bound = ExternallyTraversible)
_CE = TypeVar('_CE', bound = 'ColumnElement[Any]')
_TraverseCallableType = Callable[([
    _ET], None)]

class _CloneCallableType(Protocol):
    
    def __call__(self = None, element = None, **kw):
        pass



def _TraverseTransformCallableType():
    '''_TraverseTransformCallableType'''
    
    def __call__(self = None, element = None, **kw):
        pass


_TraverseTransformCallableType = <NODE:27>(_TraverseTransformCallableType, '_TraverseTransformCallableType', Protocol[_ET])
_ExtT = TypeVar('_ExtT', bound = 'ExternalTraversal')

class ExternalTraversal(util.MemoizedSlots):
    '''Base class for visitor objects which can traverse externally using
    the :func:`.visitors.traverse` function.

    Direct usage of the :func:`.visitors.traverse` function is usually
    preferred.

    '''
    __slots__ = ('_visitor_dict', '_next')
    _next: 'Optional[ExternalTraversal]' = { }
    
    def traverse_single(self = None, obj = None, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def iterate(self = None, obj = None):
        '''Traverse the given expression structure, returning an iterator
        of all elements.

        '''
        return iterate(obj, self.__traverse_options__)

    traverse = (lambda self = None, obj = None: pass)()
    traverse = (lambda self = None, obj = None: pass)()
    
    def traverse(self = None, obj = None):
        '''Traverse and visit the given expression structure.'''
        return traverse(obj, self.__traverse_options__, self._visitor_dict)

    
    def _memoized_attr__visitor_dict(self = None):
        visitors = { }
        for name in dir(self):
            if name.startswith('visit_'):
                visitors[name[6:]] = getattr(self, name)
            return visitors

    visitor_iterator = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def chain(self = None, visitor = None):
        """'Chain' an additional ExternalTraversal onto this ExternalTraversal

        The chained visitor will receive all visit events after this one.

        """
        tail = list(self.visitor_iterator)[-1]
        tail._next = visitor
        return self



class CloningExternalTraversal(ExternalTraversal):
    '''Base class for visitor objects which can traverse using
    the :func:`.visitors.cloned_traverse` function.

    Direct usage of the :func:`.visitors.cloned_traverse` function is usually
    preferred.


    '''
    __slots__ = ()
    
    def copy_and_process(self = None, list_ = None):
        '''Apply cloned traversal to the given list of elements, and return
        the new list.

        '''
        pass
    # WARNING: Decompyle incomplete

    traverse = (lambda self = None, obj = None: pass)()
    traverse = (lambda self = None, obj = None: pass)()
    
    def traverse(self = None, obj = None):
        '''Traverse and visit the given expression structure.'''
        return cloned_traverse(obj, self.__traverse_options__, self._visitor_dict)



class ReplacingExternalTraversal(CloningExternalTraversal):
    '''Base class for visitor objects which can traverse using
    the :func:`.visitors.replacement_traverse` function.

    Direct usage of the :func:`.visitors.replacement_traverse` function is
    usually preferred.

    '''
    __slots__ = ()
    
    def replace(self = None, elem = None):
        '''Receive pre-copied elements during a cloning traversal.

        If the method returns a new element, the element is used
        instead of creating a simple copy of the element.  Traversal
        will halt on the newly returned element if it is re-encountered.
        '''
        pass

    traverse = (lambda self = None, obj = None: pass)()
    traverse = (lambda self = None, obj = None: pass)()
    
    def traverse(self = None, obj = None):
        '''Traverse and visit the given expression structure.'''
        pass
    # WARNING: Decompyle incomplete


Traversible = Visitable
ClauseVisitor = ExternalTraversal
CloningVisitor = CloningExternalTraversal
ReplacingCloningVisitor = ReplacingExternalTraversal

def iterate(obj = None, opts = None):
    '''Traverse the given expression structure, returning an iterator.

    Traversal is configured to be breadth-first.

    The central API feature used by the :func:`.visitors.iterate`
    function is the
    :meth:`_expression.ClauseElement.get_children` method of
    :class:`_expression.ClauseElement` objects.  This method should return all
    the :class:`_expression.ClauseElement` objects which are associated with a
    particular :class:`_expression.ClauseElement` object. For example, a
    :class:`.Case` structure will refer to a series of
    :class:`_expression.ColumnElement` objects within its "whens" and "else\\_"
    member variables.

    :param obj: :class:`_expression.ClauseElement` structure to be traversed

    :param opts: dictionary of iteration options.   This dictionary is usually
     empty in modern usage.

    '''
    pass
# WARNING: Decompyle incomplete

traverse_using = (lambda iterator = None, obj = None, visitors = overload: pass)()
traverse_using = (lambda iterator = None, obj = None, visitors = overload: pass)()

def traverse_using(iterator = None, obj = None, visitors = None):
    '''Visit the given expression structure using the given iterator of
    objects.

    :func:`.visitors.traverse_using` is usually called internally as the result
    of the :func:`.visitors.traverse` function.

    :param iterator: an iterable or sequence which will yield
     :class:`_expression.ClauseElement`
     structures; the iterator is assumed to be the
     product of the :func:`.visitors.iterate` function.

    :param obj: the :class:`_expression.ClauseElement`
     that was used as the target of the
     :func:`.iterate` function.

    :param visitors: dictionary of visit functions.  See :func:`.traverse`
     for details on this dictionary.

    .. seealso::

        :func:`.traverse`


    '''
    for target in iterator:
        meth = visitors.get(target.__visit_name__, None)
        if meth:
            meth(target)
        return obj

traverse = (lambda obj = None, opts = None, visitors = overload: pass)()
traverse = (lambda obj = None, opts = None, visitors = overload: pass)()

def traverse(obj = None, opts = None, visitors = None):
    '''Traverse and visit the given expression structure using the default
    iterator.

     e.g.::

        from sqlalchemy.sql import visitors

        stmt = select(some_table).where(some_table.c.foo == "bar")


        def visit_bindparam(bind_param):
            print("found bound value: %s" % bind_param.value)


        visitors.traverse(stmt, {}, {"bindparam": visit_bindparam})

    The iteration of objects uses the :func:`.visitors.iterate` function,
    which does a breadth-first traversal using a stack.

    :param obj: :class:`_expression.ClauseElement` structure to be traversed

    :param opts: dictionary of iteration options.   This dictionary is usually
     empty in modern usage.

    :param visitors: dictionary of visit functions.   The dictionary should
     have strings as keys, each of which would correspond to the
     ``__visit_name__`` of a particular kind of SQL expression object, and
     callable functions  as values, each of which represents a visitor function
     for that kind of object.

    '''
    return traverse_using(iterate(obj, opts), obj, visitors)

cloned_traverse = (lambda obj = None, opts = None, visitors = overload: pass)()
cloned_traverse = (lambda obj = None, opts = None, visitors = overload: pass)()

def cloned_traverse(obj = None, opts = None, visitors = None):
    '''Clone the given expression structure, allowing modifications by
    visitors for mutable objects.

    Traversal usage is the same as that of :func:`.visitors.traverse`.
    The visitor functions present in the ``visitors`` dictionary may also
    modify the internals of the given structure as the traversal proceeds.

    The :func:`.cloned_traverse` function does **not** provide objects that are
    part of the :class:`.Immutable` interface to the visit methods (this
    primarily includes :class:`.ColumnClause`, :class:`.Column`,
    :class:`.TableClause` and :class:`.Table` objects). As this traversal is
    only intended to allow in-place mutation of objects, :class:`.Immutable`
    objects are skipped. The :meth:`.Immutable._clone` method is still called
    on each object to allow for objects to replace themselves with a different
    object based on a clone of their sub-internals (e.g. a
    :class:`.ColumnClause` that clones its subquery to return a new
    :class:`.ColumnClause`).

    .. versionchanged:: 2.0  The :func:`.cloned_traverse` function omits
       objects that are part of the :class:`.Immutable` interface.

    The central API feature used by the :func:`.visitors.cloned_traverse`
    and :func:`.visitors.replacement_traverse` functions, in addition to the
    :meth:`_expression.ClauseElement.get_children`
    function that is used to achieve
    the iteration, is the :meth:`_expression.ClauseElement._copy_internals`
    method.
    For a :class:`_expression.ClauseElement`
    structure to support cloning and replacement
    traversals correctly, it needs to be able to pass a cloning function into
    its internal members in order to make copies of them.

    .. seealso::

        :func:`.visitors.traverse`

        :func:`.visitors.replacement_traverse`

    '''
    pass
# WARNING: Decompyle incomplete

replacement_traverse = (lambda obj = None, opts = None, replace = overload: pass)()
replacement_traverse = (lambda obj = None, opts = None, replace = overload: pass)()
replacement_traverse = (lambda obj = None, opts = None, replace = overload: pass)()

def replacement_traverse(obj = None, opts = None, replace = None):
    '''Clone the given expression structure, allowing element
    replacement by a given replacement function.

    This function is very similar to the :func:`.visitors.cloned_traverse`
    function, except instead of being passed a dictionary of visitors, all
    elements are unconditionally passed into the given replace function.
    The replace function then has the option to return an entirely new object
    which will replace the one given.  If it returns ``None``, then the object
    is kept in place.

    The difference in usage between :func:`.visitors.cloned_traverse` and
    :func:`.visitors.replacement_traverse` is that in the former case, an
    already-cloned object is passed to the visitor function, and the visitor
    function can then manipulate the internal state of the object.
    In the case of the latter, the visitor function should only return an
    entirely different object, or do nothing.

    The use case for :func:`.visitors.replacement_traverse` is that of
    replacing a FROM clause inside of a SQL structure with a different one,
    as is a common use case within the ORM.

    '''
    pass
# WARNING: Decompyle incomplete
