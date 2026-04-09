# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: traversals.pyc (Python 3.11)

from __future__ import annotations
from collections import deque
from collections.abc import abc as collections_abc
import itertools
from itertools import zip_longest
import operator
import typing
from typing import Any
from typing import Callable
from typing import Deque
from typing import Dict
from typing import Iterable
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type
from  import operators
from cache_key import HasCacheKey
from visitors import _TraverseInternalsType
from visitors import anon_map
from visitors import ExternallyTraversible
from visitors import HasTraversalDispatch
from visitors import HasTraverseInternals
from  import util
from util import langhelpers
from util.typing import Self
SKIP_TRAVERSE = util.symbol('skip_traverse')
COMPARE_FAILED = False
COMPARE_SUCCEEDED = True

def compare(obj1 = None, obj2 = None, **kw):
    if kw.get('use_proxies', False):
        strategy = ColIdentityComparatorStrategy()
    else:
        strategy = TraversalComparatorStrategy()
# WARNING: Decompyle incomplete


def _preconfigure_traversals(target_hierarchy = None):
    for cls in util.walk_subclasses(target_hierarchy):
        if hasattr(cls, '_generate_cache_attrs') and hasattr(cls, '_traverse_internals'):
            cls._generate_cache_attrs()
            _copy_internals.generate_dispatch(cls, cls._traverse_internals, '_generated_copy_internals_traversal')
            _get_children.generate_dispatch(cls, cls._traverse_internals, '_generated_get_children_traversal')
        return None


class HasShallowCopy(HasTraverseInternals):
    """attribute-wide operations that are useful for classes that use
    __slots__ and therefore can't operate on their attributes in a dictionary.


    """
    __slots__ = ()
    if typing.TYPE_CHECKING:
        
        def _generated_shallow_copy_traversal(self = None, other = None):
            pass

        
        def _generated_shallow_from_dict_traversal(self = None, d = None):
            pass

        
        def _generated_shallow_to_dict_traversal(self = None):
            pass

    _generate_shallow_copy = (lambda cls = None, internal_dispatch = None, method_name = classmethod: code = (lambda .0: pass# WARNING: Decompyle incomplete
)(internal_dispatch())
        meth_text = f'''def {method_name}(self, other):\n{code}\n'''
        return langhelpers._exec_code_in_env(meth_text, { }, method_name)
)()
    _generate_shallow_to_dict = (lambda cls = None, internal_dispatch = None, method_name = classmethod: code = (lambda .0: pass# WARNING: Decompyle incomplete
)(internal_dispatch())
        meth_text = f'''def {method_name}(self):\n    return {{{code}}}\n'''
        return langhelpers._exec_code_in_env(meth_text, { }, method_name)
)()
    _generate_shallow_from_dict = (lambda cls = None, internal_dispatch = None, method_name = classmethod: code = (lambda .0: pass# WARNING: Decompyle incomplete
)(internal_dispatch())
        meth_text = f'''def {method_name}(self, d):\n{code}\n'''
        return langhelpers._exec_code_in_env(meth_text, { }, method_name)
)()
    
    def _shallow_from_dict(self = None, d = None):
        cls = self.__class__
        
        try:
            shallow_from_dict = cls.__dict__['_generated_shallow_from_dict_traversal']
        except KeyError:
            shallow_from_dict = self._generate_shallow_from_dict(cls._traverse_internals, '_generated_shallow_from_dict_traversal')
            cls._generated_shallow_from_dict_traversal = shallow_from_dict

        shallow_from_dict(self, d)

    
    def _shallow_to_dict(self = None):
        cls = self.__class__
        
        try:
            shallow_to_dict = cls.__dict__['_generated_shallow_to_dict_traversal']
        except KeyError:
            shallow_to_dict = self._generate_shallow_to_dict(cls._traverse_internals, '_generated_shallow_to_dict_traversal')
            cls._generated_shallow_to_dict_traversal = shallow_to_dict

        return shallow_to_dict(self)

    
    def _shallow_copy_to(self = None, other = None):
        cls = self.__class__
        
        try:
            shallow_copy = cls.__dict__['_generated_shallow_copy_traversal']
        except KeyError:
            shallow_copy = self._generate_shallow_copy(cls._traverse_internals, '_generated_shallow_copy_traversal')
            cls._generated_shallow_copy_traversal = shallow_copy

        shallow_copy(self, other)

    
    def _clone(self = None, **kw):
        '''Create a shallow copy'''
        c = self.__class__.__new__(self.__class__)
        self._shallow_copy_to(c)
        return c



class GenerativeOnTraversal(HasShallowCopy):
    '''Supplies Generative behavior but making use of traversals to shallow
    copy.

    .. seealso::

        :class:`sqlalchemy.sql.base.Generative`


    '''
    __slots__ = ()
    
    def _generate(self = None):
        cls = self.__class__
        s = cls.__new__(cls)
        self._shallow_copy_to(s)
        return s



def _clone(element, **kw):
    return element._clone()


class HasCopyInternals(HasTraverseInternals):
    __slots__ = ()
    
    def _clone(self, **kw):
        raise NotImplementedError()

    
    def _copy_internals(self = None, *, omit_attrs, **kw):
        '''Reassign internal elements to be clones of themselves.

        Called during a copy-and-traverse operation on newly
        shallow-copied elements to create a deep copy.

        The given clone function should be used, which may be applying
        additional transformations to the element (i.e. replacement
        traversal, cloned traversal, annotations).

        '''
        
        try:
            traverse_internals = self._traverse_internals
        except AttributeError:
            return None

    # WARNING: Decompyle incomplete



class _CopyInternalsTraversal(HasTraversalDispatch):
    '''Generate a _copy_internals internal traversal dispatch for classes
    with a _traverse_internals collection.'''
    
    def visit_clauseelement(self, attrname, parent, element, clone = (_clone,), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_clauseelement_list(self, attrname, parent, element, clone = (_clone,), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_clauseelement_tuple(self, attrname, parent, element, clone = (_clone,), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_executable_options(self, attrname, parent, element, clone = (_clone,), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_clauseelement_unordered_set(self, attrname, parent, element, clone = (_clone,), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_clauseelement_tuples(self, attrname, parent, element, clone = (_clone,), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_string_clauseelement_dict(self, attrname, parent, element, clone = (_clone,), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_setup_join_tuple(self, attrname, parent, element, clone = (_clone,), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_memoized_select_entities(self, attrname, parent, element, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_dml_ordered_values(self, attrname, parent, element, clone = (_clone,), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_dml_values(self, attrname, parent, element, clone = (_clone,), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_dml_multi_values(self, attrname, parent, element, clone = (_clone,), **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_propagate_attrs(self, attrname, parent, element, clone = (_clone,), **kw):
        return element


_copy_internals = _CopyInternalsTraversal()

def _flatten_clauseelement(element):
    pass
# WARNING: Decompyle incomplete


class _GetChildrenTraversal(HasTraversalDispatch):
    '''Generate a _children_traversal internal traversal dispatch for classes
    with a _traverse_internals collection.'''
    
    def visit_has_cache_key(self, element, **kw):
        return ()

    
    def visit_clauseelement(self, element, **kw):
        return (element,)

    
    def visit_clauseelement_list(self, element, **kw):
        return element

    
    def visit_clauseelement_tuple(self, element, **kw):
        return element

    
    def visit_clauseelement_tuples(self, element, **kw):
        return itertools.chain.from_iterable(element)

    
    def visit_fromclause_canonical_column_collection(self, element, **kw):
        return ()

    
    def visit_string_clauseelement_dict(self, element, **kw):
        return element.values()

    
    def visit_fromclause_ordered_set(self, element, **kw):
        return element

    
    def visit_clauseelement_unordered_set(self, element, **kw):
        return element

    
    def visit_setup_join_tuple(self, element, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_memoized_select_entities(self, element, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_dml_ordered_values(self, element, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_dml_values(self, element, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_dml_multi_values(self, element, **kw):
        return ()

    
    def visit_propagate_attrs(self, element, **kw):
        return ()


_get_children = _GetChildrenTraversal()
_resolve_name_for_compare = (lambda element, name, anon_map: if isinstance(name, util.preloaded.sql_elements._anonymous_label):
name = name.apply_map(anon_map)name)()

class TraversalComparatorStrategy(util.MemoizedSlots, HasTraversalDispatch):
    __slots__ = ('stack', 'cache', 'anon_map')
    
    def __init__(self):
        self.stack = deque()
        self.cache = set()

    
    def _memoized_attr_anon_map(self):
        return (anon_map(), anon_map())

    
    def compare(self = None, obj1 = None, obj2 = None, **kw):
        stack = self.stack
        cache = self.cache
        compare_annotations = kw.get('compare_annotations', False)
        stack.append((obj1, obj2))
    # WARNING: Decompyle incomplete

    
    def compare_inner(self, obj1, obj2, **kw):
        comparator = self.__class__()
    # WARNING: Decompyle incomplete

    
    def visit_has_cache_key(self, attrname, left_parent, left, right_parent, right, **kw):
        if left._gen_cache_key(self.anon_map[0], []) != right._gen_cache_key(self.anon_map[1], []):
            return COMPARE_FAILED

    
    def visit_propagate_attrs(self, attrname, left_parent, left, right_parent, right, **kw):
        return self.compare_inner(left.get('plugin_subject', None), right.get('plugin_subject', None))

    
    def visit_has_cache_key_list(self, attrname, left_parent, left, right_parent, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_executable_options(self, attrname, left_parent, left, right_parent, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_clauseelement(self, attrname, left_parent, left, right_parent, right, **kw):
        self.stack.append((left, right))

    
    def visit_fromclause_canonical_column_collection(self, attrname, left_parent, left, right_parent, right, **kw):
        for lcol, rcol in zip_longest(left, right, fillvalue = None):
            self.stack.append((lcol, rcol))
            return None

    
    def visit_fromclause_derived_column_collection(self, attrname, left_parent, left, right_parent, right, **kw):
        pass

    
    def visit_string_clauseelement_dict(self, attrname, left_parent, left, right_parent, right, **kw):
        for lstr, rstr in zip_longest(sorted(left), sorted(right), fillvalue = None):
            if lstr != rstr:
                
                return None, COMPARE_FAILED
            None.stack.append((left[lstr], right[rstr]))
            return None

    
    def visit_clauseelement_tuples(self, attrname, left_parent, left, right_parent, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_clauseelement_list(self, attrname, left_parent, left, right_parent, right, **kw):
        for l, r in zip_longest(left, right, fillvalue = None):
            self.stack.append((l, r))
            return None

    
    def visit_clauseelement_tuple(self, attrname, left_parent, left, right_parent, right, **kw):
        for l, r in zip_longest(left, right, fillvalue = None):
            self.stack.append((l, r))
            return None

    
    def _compare_unordered_sequences(self, seq1, seq2, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_clauseelement_unordered_set(self, attrname, left_parent, left, right_parent, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_fromclause_ordered_set(self, attrname, left_parent, left, right_parent, right, **kw):
        for l, r in zip_longest(left, right, fillvalue = None):
            self.stack.append((l, r))
            return None

    
    def visit_string(self, attrname, left_parent, left, right_parent, right, **kw):
        return left == right

    
    def visit_string_list(self, attrname, left_parent, left, right_parent, right, **kw):
        return left == right

    
    def visit_string_multi_dict(self, attrname, left_parent, left, right_parent, right, **kw):
        for lk, rk in zip_longest(sorted(left.keys()), sorted(right.keys()), fillvalue = (None, None)):
            if lk != rk:
                
                return None, COMPARE_FAILED
            right[rk] = None[lk]
            lhc = isinstance(left, HasCacheKey)
            rhc = isinstance(right, HasCacheKey)
            if lhc and rhc:
                if lv._gen_cache_key(self.anon_map[0], []) != rv._gen_cache_key(self.anon_map[1], []):
                    
                    return None, COMPARE_FAILED
            if lhc != rhc:
                
                return None, COMPARE_FAILED
            if None != rv:
                
                return None, COMPARE_FAILED
            return None

    
    def visit_multi(self, attrname, left_parent, left, right_parent, right, **kw):
        lhc = isinstance(left, HasCacheKey)
        rhc = isinstance(right, HasCacheKey)
        if lhc and rhc:
            if left._gen_cache_key(self.anon_map[0], []) != right._gen_cache_key(self.anon_map[1], []):
                return COMPARE_FAILED
            return None
        if None != rhc:
            return COMPARE_FAILED
        return None == right

    
    def visit_anon_name(self, attrname, left_parent, left, right_parent, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_boolean(self, attrname, left_parent, left, right_parent, right, **kw):
        return left == right

    
    def visit_operator(self, attrname, left_parent, left, right_parent, right, **kw):
        return left == right

    
    def visit_type(self, attrname, left_parent, left, right_parent, right, **kw):
        return left._compare_type_affinity(right)

    
    def visit_plain_dict(self, attrname, left_parent, left, right_parent, right, **kw):
        return left == right

    
    def visit_dialect_options(self, attrname, left_parent, left, right_parent, right, **kw):
        return left == right

    
    def visit_annotations_key(self, attrname, left_parent, left, right_parent, right, **kw):
        if left and right:
            return left_parent._annotations_cache_key == right_parent._annotations_cache_key
        return None == right

    
    def visit_with_context_options(self, attrname, left_parent, left, right_parent, right, **kw):
        return tuple == (lambda .0: pass# WARNING: Decompyle incomplete
)(right())

    
    def visit_plain_obj(self, attrname, left_parent, left, right_parent, right, **kw):
        return left == right

    
    def visit_named_ddl_element(self, attrname, left_parent, left, right_parent, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_prefix_sequence(self, attrname, left_parent, left, right_parent, right, **kw):
        for l_clause, l_str in zip_longest(left, right, fillvalue = (None, None)):
            (r_clause, r_str) = None
            if l_str != r_str:
                
                return None, COMPARE_FAILED
            None.stack.append((l_clause, r_clause))
            return None

    
    def visit_setup_join_tuple(self, attrname, left_parent, left, right_parent, right, **kw):
        for l_target, l_onclause, l_from, l_flags in zip_longest(left, right, fillvalue = (None, None, None, None)):
            (r_target, r_onclause, r_from, r_flags) = None
            if l_flags != r_flags:
                
                return None, COMPARE_FAILED
            None.stack.append((l_target, r_target))
            self.stack.append((l_onclause, r_onclause))
            self.stack.append((l_from, r_from))
            return None

    
    def visit_memoized_select_entities(self, attrname, left_parent, left, right_parent, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_table_hint_list(self, attrname, left_parent, left, right_parent, right, **kw):
        left_keys = sorted(left, key = (lambda elem: (elem[0].fullname, elem[1])))
        right_keys = sorted(right, key = (lambda elem: (elem[0].fullname, elem[1])))
        for ltable, ldialect in zip_longest(left_keys, right_keys, fillvalue = (None, None)):
            (rtable, rdialect) = None
            if ldialect != rdialect:
                
                return None, COMPARE_FAILED
            if None[(ltable, ldialect)] != right[(rtable, rdialect)]:
                
                return None, COMPARE_FAILED
            None.stack.append((ltable, rtable))
            return None

    
    def visit_statement_hint_list(self, attrname, left_parent, left, right_parent, right, **kw):
        return left == right

    
    def visit_unknown_structure(self, attrname, left_parent, left, right_parent, right, **kw):
        raise NotImplementedError()

    
    def visit_dml_ordered_values(self, attrname, left_parent, left, right_parent, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def _compare_dml_values_or_ce(self, lv, rv, **kw):
        lvce = hasattr(lv, '__clause_element__')
        rvce = hasattr(rv, '__clause_element__')
        if lvce != rvce:
            return False
    # WARNING: Decompyle incomplete

    
    def visit_dml_values(self, attrname, left_parent, left, right_parent, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_dml_multi_values(self, attrname, left_parent, left, right_parent, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def compare_expression_clauselist(self, left, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def compare_clauselist(self, left, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def compare_binary(self, left, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def compare_bindparam(self, left, right, **kw):
        compare_keys = kw.pop('compare_keys', True)
        compare_values = kw.pop('compare_values', True)
        if compare_values:
            omit = []
        else:
            omit = [
                'callable',
                'value']
        if not compare_keys:
            omit.append('key')
        return omit



class ColIdentityComparatorStrategy(TraversalComparatorStrategy):
    
    def compare_column_element(self, left, right, use_proxies, equivalents = (True, ()), **kw):
        '''Compare ColumnElements using proxies and equivalent collections.

        This is a comparison strategy specific to the ORM.
        '''
        to_compare = (right,)
        if equivalents and right in equivalents:
            to_compare = equivalents[right].union(to_compare)
        for oth in to_compare:
            if use_proxies and left.shares_lineage(oth):
                
                return None, SKIP_TRAVERSE
            if None(left) == hash(right):
                
                return None, SKIP_TRAVERSE
            return COMPARE_FAILED

    
    def compare_column(self, left, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def compare_label(self, left, right, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def compare_table(self, left, right, **kw):
        return SKIP_TRAVERSE if left is right else COMPARE_FAILED
