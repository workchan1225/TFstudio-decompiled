# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cache_key.pyc (Python 3.11)

from __future__ import annotations
import enum
from itertools import zip_longest
import typing
from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import MutableMapping
from typing import NamedTuple
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Union
from visitors import anon_map
from visitors import HasTraversalDispatch
from visitors import HasTraverseInternals
from visitors import InternalTraversal
from visitors import prefix_anon_map
from  import util
from inspection import inspect
from util import HasMemoized
from util.typing import Literal
from util.typing import Protocol
if typing.TYPE_CHECKING:
    from elements import BindParameter
    from elements import ClauseElement
    from elements import ColumnElement
    from visitors import _TraverseInternalsType
    from engine.interfaces import _CoreSingleExecuteParams

class _CacheKeyTraversalDispatchType(Protocol):
    
    def __call__(s = None, self = None, visitor = None):
        pass



class CacheConst(enum.Enum):
    NO_CACHE = 0

NO_CACHE = CacheConst.NO_CACHE
_CacheKeyTraversalType = Union[('_TraverseInternalsType', Literal[CacheConst.NO_CACHE], Literal[None])]

class CacheTraverseTarget(enum.Enum):
    CACHE_IN_PLACE = 0
    CALL_GEN_CACHE_KEY = 1
    STATIC_CACHE_KEY = 2
    PROPAGATE_ATTRS = 3
    ANON_NAME = 4

(CACHE_IN_PLACE, CALL_GEN_CACHE_KEY, STATIC_CACHE_KEY, PROPAGATE_ATTRS, ANON_NAME) = tuple(CacheTraverseTarget)
_CacheKeyTraversalDispatchTypeReturn = Sequence[Tuple[(str, Any, Union[(Callable[(..., Tuple[(Any, ...)])], CacheTraverseTarget, InternalTraversal)])]]

class HasCacheKey:
    '''Mixin for objects which can produce a cache key.

    This class is usually in a hierarchy that starts with the
    :class:`.HasTraverseInternals` base, but this is optional.  Currently,
    the class should be able to work on its own without including
    :class:`.HasTraverseInternals`.

    .. seealso::

        :class:`.CacheKey`

        :ref:`sql_caching`

    '''
    __slots__ = ()
    _cache_key_traversal: '_CacheKeyTraversalType' = NO_CACHE
    _is_has_cache_key = True
    _hierarchy_supports_caching = True
    inherit_cache: 'Optional[bool]' = None
    _generated_cache_key_traversal: 'Any' = ()
    _generate_cache_attrs = (lambda cls = None: inherit_cache = cls.__dict__.get('inherit_cache', None)inherit = bool(inherit_cache)# WARNING: Decompyle incomplete
)()
    _gen_cache_key = (lambda self = None, anon_map = None, bindparams = util.preload_module('sqlalchemy.sql.elements'): pass# WARNING: Decompyle incomplete
)()
    
    def _generate_cache_key(self = None):
        '''return a cache key.

        The cache key is a tuple which can contain any series of
        objects that are hashable and also identifies
        this object uniquely within the presence of a larger SQL expression
        or statement, for the purposes of caching the resulting query.

        The cache key should be based on the SQL compiled structure that would
        ultimately be produced.   That is, two structures that are composed in
        exactly the same way should produce the same cache key; any difference
        in the structures that would affect the SQL string or the type handlers
        should result in a different cache key.

        The cache key returned by this method is an instance of
        :class:`.CacheKey`, which consists of a tuple representing the
        cache key, as well as a list of :class:`.BindParameter` objects
        which are extracted from the expression.   While two expressions
        that produce identical cache key tuples will themselves generate
        identical SQL strings, the list of :class:`.BindParameter` objects
        indicates the bound values which may have different values in
        each one; these bound parameters must be consulted in order to
        execute the statement with the correct parameters.

        a :class:`_expression.ClauseElement` structure that does not implement
        a :meth:`._gen_cache_key` method and does not implement a
        :attr:`.traverse_internals` attribute will not be cacheable; when
        such an element is embedded into a larger structure, this method
        will return None, indicating no cache key is available.

        '''
        bindparams = []
        _anon_map = anon_map()
        key = self._gen_cache_key(_anon_map, bindparams)
        if NO_CACHE in _anon_map:
            return None
    # WARNING: Decompyle incomplete

    _generate_cache_key_for_object = (lambda cls = None, obj = None: bindparams = []_anon_map = anon_map()key = obj._gen_cache_key(_anon_map, bindparams)if NO_CACHE in _anon_map:
None# WARNING: Decompyle incomplete
)()


class HasCacheKeyTraverse(HasCacheKey, HasTraverseInternals):
    pass


class MemoizedHasCacheKey(HasMemoized, HasCacheKey):
    __slots__ = ()
    _generate_cache_key = (lambda self = None: HasCacheKey._generate_cache_key(self))()


class SlotsMemoizedHasCacheKey(util.MemoizedSlots, HasCacheKey):
    __slots__ = ()
    
    def _memoized_method__generate_cache_key(self = None):
        return HasCacheKey._generate_cache_key(self)



class CacheKey(NamedTuple):
    bindparams: 'Sequence[BindParameter[Any]]' = 'The key used to identify a SQL statement construct in the\n    SQL compilation cache.\n\n    .. seealso::\n\n        :ref:`sql_caching`\n\n    '
    
    def __hash__(self = None):
        '''CacheKey itself is not hashable - hash the .key portion'''
        pass

    
    def to_offline_string(self = None, statement_cache = None, statement = None, parameters = ('statement_cache', 'MutableMapping[Any, str]', 'statement', 'ClauseElement', 'parameters', '_CoreSingleExecuteParams', 'return', 'str')):
        '''Generate an "offline string" form of this :class:`.CacheKey`

        The "offline string" is basically the string SQL for the
        statement plus a repr of the bound parameter values in series.
        Whereas the :class:`.CacheKey` object is dependent on in-memory
        identities in order to work as a cache key, the "offline" version
        is suitable for a cache that will work for other processes as well.

        The given ``statement_cache`` is a dictionary-like object where the
        string form of the statement itself will be cached.  This dictionary
        should be in a longer lived scope in order to reduce the time spent
        stringifying statements.


        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __eq__(self = None, other = None):
        return bool(self.key == other.key)

    
    def __ne__(self = None, other = None):
        return not (self.key == other.key)

    _diff_tuples = (lambda cls = None, left = None, right = classmethod: ck1 = CacheKey(left, [])ck2 = CacheKey(right, [])ck1._diff(ck2))()
    
    def _whats_different(self = None, other = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _diff(self = None, other = None):
        return ', '.join(self._whats_different(other))

    
    def __str__(self = None):
        stack = [
            self.key]
        output = []
        sentinel = object()
        indent = -1
    # WARNING: Decompyle incomplete

    
    def _generate_param_dict(self = None):
        '''used for testing'''
        pass
    # WARNING: Decompyle incomplete

    _apply_params_to_element = (lambda self = None, original_cache_key = None, target_element = util.preload_module('sqlalchemy.sql.elements'): if target_element._is_immutable or original_cache_key is self:
target_elementelements = None.preloaded.sql_elementselements._OverrideBinds(target_element, self.bindparams, original_cache_key.bindparams))()


def _ad_hoc_cache_key_from_args(tokens = None, traverse_args = None, args = None):
    '''a quick cache key generator used by reflection.flexi_cache.'''
    bindparams = []
    _anon_map = anon_map()
    tup = tokens
# WARNING: Decompyle incomplete


class _CacheKeyTraversal(HasTraversalDispatch):
    visit_has_cache_key = CALL_GEN_CACHE_KEY
    visit_clauseelement = CALL_GEN_CACHE_KEY
    visit_clauseelement_list = InternalTraversal.dp_clauseelement_list
    visit_annotations_key = InternalTraversal.dp_annotations_key
    visit_clauseelement_tuple = InternalTraversal.dp_clauseelement_tuple
    visit_memoized_select_entities = InternalTraversal.dp_memoized_select_entities
    visit_string = CACHE_IN_PLACE
    visit_boolean = CACHE_IN_PLACE
    visit_operator = CACHE_IN_PLACE
    visit_plain_obj = CACHE_IN_PLACE
    visit_statement_hint_list = CACHE_IN_PLACE
    visit_type = STATIC_CACHE_KEY
    visit_anon_name = ANON_NAME
    visit_propagate_attrs = PROPAGATE_ATTRS
    
    def visit_with_context_options(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(obj())

    
    def visit_inspectable(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        return (attrname, inspect(obj)._gen_cache_key(anon_map, bindparams))

    
    def visit_string_list(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        return tuple(obj)

    
    def visit_multi(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        return (attrname, obj._gen_cache_key(anon_map, bindparams) if isinstance(obj, HasCacheKey) else obj)

    
    def visit_multi_list(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_has_cache_key_tuples(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_has_cache_key_list(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_executable_options(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_inspectable_list(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        
        def <listcomp>(.0):
            return [ inspect(o) for o in .0 ]

        return attrname(<listcomp>, obj(), parent, anon_map, bindparams)

    
    def visit_clauseelement_tuples(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        return self.visit_has_cache_key_tuples(attrname, obj, parent, anon_map, bindparams)

    
    def visit_fromclause_ordered_set(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_clauseelement_unordered_set(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_named_ddl_element(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        return (attrname, obj.name)

    
    def visit_prefix_sequence(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_setup_join_tuple(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_table_hint_list(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_plain_dict(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_dialect_options(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_string_clauseelement_dict(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_string_multi_dict(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_fromclause_canonical_column_collection(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_unknown_structure(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        anon_map[NO_CACHE] = True
        return ()

    
    def visit_dml_ordered_values(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_dml_values(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        pass
    # WARNING: Decompyle incomplete

    
    def visit_dml_multi_values(self, attrname, obj = None, parent = None, anon_map = None, bindparams = ('attrname', 'str', 'obj', 'Any', 'parent', 'Any', 'anon_map', 'anon_map', 'bindparams', 'List[BindParameter[Any]]', 'return', 'Tuple[Any, ...]')):
        anon_map[NO_CACHE] = True
        return ()


_cache_key_traversal_visitor = _CacheKeyTraversal()
