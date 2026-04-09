# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: strategies.pyc (Python 3.11)

'''sqlalchemy.orm.interfaces.LoaderStrategy
implementations, and related MapperOptions.'''
from __future__ import annotations
import collections
import itertools
from typing import Any
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import TYPE_CHECKING
from typing import Union
from  import attributes
from  import exc as orm_exc
from  import interfaces
from  import loading
from  import path_registry
from  import properties
from  import query
from  import relationships
from  import unitofwork
from  import util as orm_util
from base import _DEFER_FOR_STATE
from base import _RAISE_FOR_STATE
from base import _SET_DEFERRED_EXPIRED
from base import ATTR_WAS_SET
from base import LoaderCallableStatus
from base import PASSIVE_OFF
from base import PassiveFlag
from context import _column_descriptions
from context import ORMCompileState
from context import ORMSelectCompileState
from context import QueryContext
from interfaces import LoaderStrategy
from interfaces import StrategizedProperty
from session import _state_session
from state import InstanceState
from strategy_options import Load
from util import _none_only_set
from util import AliasedClass
from  import event
from  import exc as sa_exc
from  import inspect
from  import log
from  import sql
from  import util
from sql import util as sql_util
from sql import visitors
from sql.selectable import LABEL_STYLE_TABLENAME_PLUS_COL
from sql.selectable import Select
from util.typing import Literal
if TYPE_CHECKING:
    from mapper import Mapper
    from relationships import RelationshipProperty
    from sql.elements import ColumnElement

def _register_attribute(prop, mapper, useobject, compare_function, typecallable, callable_, proxy_property, active_history, impl_class = (None, None, None, None, False, None), **kw):
    pass
# WARNING: Decompyle incomplete

UninstrumentedColumnLoader = <NODE:12>()
ColumnLoader = <NODE:12>()()
ExpressionColumnLoader = <NODE:12>()()
DeferredColumnLoader = <NODE:12>()()()()

class LoadDeferredColumns:
    '''serializable loader object used by DeferredColumnLoader'''
    
    def __init__(self = None, key = None, raiseload = None):
        self.key = key
        self.raiseload = raiseload

    
    def __call__(self, state, passive = (attributes.PASSIVE_OFF,)):
        key = self.key
        localparent = state.manager.mapper
        prop = localparent._props[key]
        if self.raiseload:
            strategy_key = (('deferred', True), ('instrument', True), ('raiseload', True))
        else:
            strategy_key = (('deferred', True), ('instrument', True))
        strategy = prop._get_strategy(strategy_key)
        return strategy._load_for_state(state, passive)



class AbstractRelationshipLoader(LoaderStrategy):
    pass
# WARNING: Decompyle incomplete

DoNothingLoader = <NODE:12>()()
NoLoader = <NODE:12>()()()
LazyLoader = <NODE:12>()()()()()()

class LoadLazyAttribute:
    """semi-serializable loader object used by LazyLoader

    Historically, this object would be carried along with instances that
    needed to run lazyloaders, so it had to be serializable to support
    cached instances.

    this is no longer a general requirement, and the case where this object
    is used is exactly the case where we can't really serialize easily,
    which is when extra criteria in the loader option is present.

    We can't reliably serialize that as it refers to mapped entities and
    AliasedClass objects that are local to the current process, which would
    need to be matched up on deserialize e.g. the sqlalchemy.ext.serializer
    approach.

    """
    
    def __init__(self, key, initiating_strategy, loadopt, extra_criteria):
        self.key = key
        self.strategy_key = initiating_strategy.strategy_key
        self.loadopt = loadopt
        self.extra_criteria = extra_criteria

    
    def __getstate__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, state, passive = (attributes.PASSIVE_OFF,)):
        key = self.key
        instance_mapper = state.manager.mapper
        prop = instance_mapper._props[key]
        strategy = prop._strategies[self.strategy_key]
        return strategy._load_for_state(state, passive, loadopt = self.loadopt, extra_criteria = self.extra_criteria)



class PostLoader(AbstractRelationshipLoader):
    '''A relationship loader that emits a second SELECT statement.'''
    __slots__ = ()
    
    def _setup_for_recursion(self, context, path, loadopt, join_depth = (None,)):
        if not context.compile_state.current_path:
            pass
        effective_path = orm_util.PathRegistry.root + path
        top_level_context = context._get_top_level_context()
        execution_options = util.immutabledict({
            'sa_top_level_orm_context': top_level_context })
        if loadopt:
            recursion_depth = loadopt.local_opts.get('recursion_depth', None)
            unlimited_recursion = recursion_depth == -1
        else:
            recursion_depth = None
            unlimited_recursion = False
    # WARNING: Decompyle incomplete


ImmediateLoader = <NODE:12>()
SubqueryLoader = <NODE:12>()()
JoinedLoader = <NODE:12>()()()
SelectInLoader = <NODE:12>()()

def single_parent_validator(desc, prop):
    pass
# WARNING: Decompyle incomplete
