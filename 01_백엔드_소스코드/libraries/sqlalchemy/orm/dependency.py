# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dependency.pyc (Python 3.11)

'''Relationship dependencies.'''
from __future__ import annotations
from  import attributes
from  import exc
from  import sync
from  import unitofwork
from  import util as mapperutil
from interfaces import MANYTOMANY
from interfaces import MANYTOONE
from interfaces import ONETOMANY
from  import exc as sa_exc
from  import sql
from  import util

class DependencyProcessor:
    
    def __init__(self, prop):
        self.prop = prop
        self.cascade = prop.cascade
        self.mapper = prop.mapper
        self.parent = prop.parent
        self.secondary = prop.secondary
        self.direction = prop.direction
        self.post_update = prop.post_update
        self.passive_deletes = prop.passive_deletes
        self.passive_updates = prop.passive_updates
        self.enable_typechecks = prop.enable_typechecks
        if self.passive_deletes:
            self._passive_delete_flag = attributes.PASSIVE_NO_INITIALIZE
        else:
            self._passive_delete_flag = attributes.PASSIVE_OFF
        if self.passive_updates:
            self._passive_update_flag = attributes.PASSIVE_NO_INITIALIZE
        else:
            self._passive_update_flag = attributes.PASSIVE_OFF
        self.sort_key = f'''{self.parent._sort_key!s}_{prop.key!s}'''
        self.key = prop.key
        if not self.prop.synchronize_pairs:
            raise sa_exc.ArgumentError("Can't build a DependencyProcessor for relationship %s. No target attributes to populate between parent and child are present" % self.prop)

    from_relationship = (lambda cls, prop: _direction_to_processor[prop.direction](prop))()
    
    def hasparent(self, state):
        '''return True if the given object instance has a parent,
        according to the ``InstrumentedAttribute`` handled by this
        ``DependencyProcessor``.

        '''
        return self.parent.class_manager.get_impl(self.key).hasparent(state)

    
    def per_property_preprocessors(self, uow):
        '''establish actions and dependencies related to a flush.

        These actions will operate on all relevant states in
        the aggregate.

        '''
        uow.register_preprocessor(self, True)

    
    def per_property_flush_actions(self, uow):
        after_save = unitofwork.ProcessAll(uow, self, False, True)
        before_delete = unitofwork.ProcessAll(uow, self, True, True)
        parent_saves = unitofwork.SaveUpdateAll(uow, self.parent.primary_base_mapper)
        child_saves = unitofwork.SaveUpdateAll(uow, self.mapper.primary_base_mapper)
        parent_deletes = unitofwork.DeleteAll(uow, self.parent.primary_base_mapper)
        child_deletes = unitofwork.DeleteAll(uow, self.mapper.primary_base_mapper)
        self.per_property_dependencies(uow, parent_saves, child_saves, parent_deletes, child_deletes, after_save, before_delete)

    
    def per_state_flush_actions(self, uow, states, isdelete):
        """establish actions and dependencies related to a flush.

        These actions will operate on all relevant states
        individually.    This occurs only if there are cycles
        in the 'aggregated' version of events.

        """
        child_base_mapper = self.mapper.primary_base_mapper
        child_saves = unitofwork.SaveUpdateAll(uow, child_base_mapper)
        child_deletes = unitofwork.DeleteAll(uow, child_base_mapper)
        if isdelete:
            before_delete = unitofwork.ProcessAll(uow, self, True, True)
            before_delete.disabled = True
        else:
            after_save = unitofwork.ProcessAll(uow, self, False, True)
            after_save.disabled = True
    # WARNING: Decompyle incomplete

    
    def presort_deletes(self, uowcommit, states):
        return False

    
    def presort_saves(self, uowcommit, states):
        return False

    
    def process_deletes(self, uowcommit, states):
        pass

    
    def process_saves(self, uowcommit, states):
        pass

    
    def prop_has_changes(self, uowcommit, states, isdelete):
