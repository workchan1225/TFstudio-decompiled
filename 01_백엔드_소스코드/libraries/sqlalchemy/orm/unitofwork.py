# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: unitofwork.pyc (Python 3.11)

"""The internals for the unit of work system.

The session's flush() process passes objects to a contextual object
here, which assembles flush tasks based on mappers and their properties,
organizes them in order of dependency, and executes.

"""
from __future__ import annotations
from typing import Any
from typing import Dict
from typing import Optional
from typing import Set
from typing import TYPE_CHECKING
from  import attributes
from  import exc as orm_exc
from  import util as orm_util
from  import event
from  import util
from util import topological
if TYPE_CHECKING:
    from dependency import DependencyProcessor
    from interfaces import MapperProperty
    from mapper import Mapper
    from session import Session
    from session import SessionTransaction
    from state import InstanceState

def track_cascade_events(descriptor, prop):
    '''Establish event listeners on object attributes which handle
    cascade-on-set/append.

    '''
    pass
# WARNING: Decompyle incomplete


class UOWTransaction:
    mappers: 'util.defaultdict[Mapper[Any], Set[InstanceState[Any]]]' = 'UOWTransaction'
    
    def __init__(self = None, session = None):
        self.session = session
        self.attributes = { }
        self.deps = util.defaultdict(set)
        self.mappers = util.defaultdict(set)
        self.presort_actions = { }
        self.postsort_actions = { }
        self.dependencies = set()
        self.states = { }
        self.post_update_states = util.defaultdict((lambda : (set(), set())))

    has_work = (lambda self: bool(self.states))()
    
    def was_already_deleted(self, state):
        '''Return ``True`` if the given state is expired and was deleted
        previously.
        '''
        if state.expired:
            
            try:
                state._load_expired(state, attributes.PASSIVE_OFF)
            except orm_exc.ObjectDeletedError:
                self.session._remove_newly_deleted([
                    state])
                return True

            return False

    
    def is_deleted(self, state):
        '''Return ``True`` if the given state is marked as deleted
        within this uowtransaction.'''
        if state in self.states:
            pass
        return self.states[state][0]

    
    def memo(self, key, callable_):
        if key in self.attributes:
            return self.attributes[key]
        self.attributes[key] = callable_()
        ret = callable_()
        return ret

    
    def remove_state_actions(self, state):
        '''Remove pending actions for a state from the uowtransaction.'''
        isdelete = self.states[state][0]
        self.states[state] = (isdelete, True)

    
    def get_attribute_history(self, state, key, passive = (attributes.PASSIVE_NO_INITIALIZE,)):
        '''Facade to attributes.get_state_history(), including
        caching of results.'''
        hashkey = ('history', state, key)
        if hashkey in self.attributes:
            (history, state_history, cached_passive) = self.attributes[hashkey]
            if cached_passive & attributes.SQL_OK and passive & attributes.SQL_OK:
                impl = state.manager[key].impl
                history = impl.get_history(state, state.dict, attributes.PASSIVE_OFF | attributes.LOAD_AGAINST_COMMITTED | attributes.NO_RAISE)
                if history and impl.uses_objects:
                    state_history = history.as_state()
                else:
                    state_history = history
                self.attributes[hashkey] = (history, state_history, passive)
            else:
                impl = state.manager[key].impl
                history = impl.get_history(state, state.dict, passive | attributes.LOAD_AGAINST_COMMITTED | attributes.NO_RAISE)
                if history and impl.uses_objects:
                    state_history = history.as_state()
                else:
                    state_history = history
                self.attributes[hashkey] = (history, state_history, passive)
        return state_history

    
    def has_dep(self, processor):
        return (processor, True) in self.presort_actions

    
    def register_preprocessor(self, processor, fromparent):
        key = (processor, fromparent)
        if key not in self.presort_actions:
            self.presort_actions[key] = Preprocess(processor, fromparent)
            return None

    
    def register_object(self, state, isdelete = None, listonly = None, cancel_delete = property, operation = (False, False, False, None, None), prop = ('state', 'InstanceState[Any]', 'isdelete', 'bool', 'listonly', 'bool', 'cancel_delete', 'bool', 'operation', 'Optional[str]', 'prop', 'Optional[MapperProperty]', 'return', 'bool')):
        pass
    # WARNING: Decompyle incomplete

    
    def register_post_update(self, state, post_update_cols):
        mapper = state.manager.mapper.base_mapper
        (states, cols) = self.post_update_states[mapper]
        states.add(state)
        cols.update(post_update_cols)

    
    def _per_mapper_flush_actions(self, mapper):
        saves = SaveUpdateAll(self, mapper.base_mapper)
        deletes = DeleteAll(self, mapper.base_mapper)
        self.dependencies.add((saves, deletes))
        for dep in mapper._dependency_processors:
            dep.per_property_preprocessors(self)
            for prop in mapper.relationships:
                if prop.viewonly:
                    continue
                dep = prop._dependency_processor
                dep.per_property_preprocessors(self)
                return None

    _mapper_for_dep = (lambda self: util.PopulateDict((lambda tup: tup[0]._props.get(tup[1].key) is tup[1].prop))
)()
    
    def filter_states_for_dep(self, dep, states):
        '''Filter the given list of InstanceStates to those relevant to the
        given DependencyProcessor.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def states_for_mapper_hierarchy(self, mapper, isdelete, listonly):
        pass
    # WARNING: Decompyle incomplete

    
    def _generate_actions(self):
        '''Generate the full, unsorted collection of PostSortRecs as
        well as dependency pairs for this UOWTransaction.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def execute(self = None):
        postsort_actions = self._generate_actions()
        postsort_actions = sorted(postsort_actions, key = (lambda item: item.sort_key))
    # WARNING: Decompyle incomplete

    
    def finalize_flush_changes(self = None):
        '''Mark processed objects as clean / deleted after a successful
        flush().

        This method is called within the flush() method after the
        execute() method has succeeded and the transaction has been committed.

        '''
        if not self.states:
            return None
        states = None(self.states)
        isdel = self.states.items()()
        other = states.difference(isdel)
        if isdel:
            self.session._remove_newly_deleted(isdel)
        if other:
            self.session._register_persistent(other)
            return None
        return (lambda .0: pass# WARNING: Decompyle incomplete
)



class IterateMappersMixin:
    __slots__ = ()
    
    def _mappers(self, uow):
        pass
    # WARNING: Decompyle incomplete



class Preprocess(IterateMappersMixin):
    __slots__ = ('dependency_processor', 'fromparent', 'processed', 'setup_flush_actions')
    
    def __init__(self, dependency_processor, fromparent):
        self.dependency_processor = dependency_processor
        self.fromparent = fromparent
        self.processed = set()
        self.setup_flush_actions = False

    
    def execute(self, uow):
        delete_states = set()
        save_states = set()
        for mapper in self._mappers(uow):
            for state in uow.mappers[mapper].difference(self.processed):
                (isdelete, listonly) = uow.states[state]
                if not listonly:
                    if isdelete:
                        delete_states.add(state)
                        continue
                    save_states.add(state)
                if delete_states:
                    self.dependency_processor.presort_deletes(uow, delete_states)
                    self.processed.update(delete_states)
        if save_states:
            self.dependency_processor.presort_saves(uow, save_states)
            self.processed.update(save_states)
        if delete_states or save_states:
            if not self.setup_flush_actions:
                if self.dependency_processor.prop_has_changes(uow, delete_states, True) or self.dependency_processor.prop_has_changes(uow, save_states, False):
                    self.dependency_processor.per_property_flush_actions(uow)
                    self.setup_flush_actions = True
            return True



class PostSortRec:
    __slots__ = ('disabled',)
    
    def __new__(cls, uow, *args):
        key = (cls,) + args
        if key in uow.postsort_actions:
            return uow.postsort_actions[key]
        uow.postsort_actions[key] = None.__new__(cls)
        ret = None.__new__(cls)
        ret.disabled = False
        return ret

    
    def execute_aggregate(self, uow, recs):
        self.execute(uow)



class ProcessAll(PostSortRec, IterateMappersMixin):
    __slots__ = ('dependency_processor', 'isdelete', 'fromparent', 'sort_key')
    
    def __init__(self, uow, dependency_processor, isdelete, fromparent):
        self.dependency_processor = dependency_processor
        self.sort_key = ('ProcessAll', self.dependency_processor.sort_key, isdelete)
        self.isdelete = isdelete
        self.fromparent = fromparent
        uow.deps[dependency_processor.parent.base_mapper].add(dependency_processor)

    
    def execute(self, uow):
        states = self._elements(uow)
        if self.isdelete:
            self.dependency_processor.process_deletes(uow, states)
            return None
        None.dependency_processor.process_saves(uow, states)

    
    def per_state_flush_actions(self, uow):
        return iter([])

    
    def __repr__(self):
        return f'''{self.__class__.__name__!s}({self.dependency_processor!s}, isdelete={self.isdelete!s})'''

    
    def _elements(self, uow):
        pass
    # WARNING: Decompyle incomplete



class PostUpdateAll(PostSortRec):
    __slots__ = ('mapper', 'isdelete', 'sort_key')
    
    def __init__(self, uow, mapper, isdelete):
        self.mapper = mapper
        self.isdelete = isdelete
        self.sort_key = ('PostUpdateAll', mapper._sort_key, isdelete)

    execute = (lambda self, uow: pass# WARNING: Decompyle incomplete
)()


class SaveUpdateAll(PostSortRec):
    __slots__ = ('mapper', 'sort_key')
    
    def __init__(self, uow, mapper):
        self.mapper = mapper
        self.sort_key = ('SaveUpdateAll', mapper._sort_key)
    # WARNING: Decompyle incomplete

    execute = (lambda self, uow: util.preloaded.orm_persistence.save_obj(self.mapper, uow.states_for_mapper_hierarchy(self.mapper, False, False), uow))()
    
    def per_state_flush_actions(self, uow):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return f'''{self.__class__.__name__!s}({self.mapper!s})'''



class DeleteAll(PostSortRec):
    __slots__ = ('mapper', 'sort_key')
    
    def __init__(self, uow, mapper):
        self.mapper = mapper
        self.sort_key = ('DeleteAll', mapper._sort_key)
    # WARNING: Decompyle incomplete

    execute = (lambda self, uow: util.preloaded.orm_persistence.delete_obj(self.mapper, uow.states_for_mapper_hierarchy(self.mapper, True, False), uow))()
    
    def per_state_flush_actions(self, uow):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return f'''{self.__class__.__name__!s}({self.mapper!s})'''



class ProcessState(PostSortRec):
    __slots__ = ('dependency_processor', 'isdelete', 'state', 'sort_key')
    
    def __init__(self, uow, dependency_processor, isdelete, state):
        self.dependency_processor = dependency_processor
        self.sort_key = ('ProcessState', dependency_processor.sort_key)
        self.isdelete = isdelete
        self.state = state

    
    def execute_aggregate(self, uow, recs):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return f'''{self.__class__.__name__!s}({self.dependency_processor!s}, {orm_util.state_str(self.state)!s}, delete={self.isdelete!s})'''



class SaveUpdateState(PostSortRec):
    __slots__ = ('state', 'mapper', 'sort_key')
    
    def __init__(self, uow, state):
        self.state = state
        self.mapper = state.mapper.base_mapper
        self.sort_key = ('ProcessState', self.mapper._sort_key)

    execute_aggregate = (lambda self, uow, recs: pass# WARNING: Decompyle incomplete
)()
    
    def __repr__(self):
        return f'''{self.__class__.__name__!s}({orm_util.state_str(self.state)!s})'''



class DeleteState(PostSortRec):
    __slots__ = ('state', 'mapper', 'sort_key')
    
    def __init__(self, uow, state):
        self.state = state
        self.mapper = state.mapper.base_mapper
        self.sort_key = ('DeleteState', self.mapper._sort_key)

    execute_aggregate = (lambda self, uow, recs: pass# WARNING: Decompyle incomplete
)()
    
    def __repr__(self):
        return f'''{self.__class__.__name__!s}({orm_util.state_str(self.state)!s})'''
