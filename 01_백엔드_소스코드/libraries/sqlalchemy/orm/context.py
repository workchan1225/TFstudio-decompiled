# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: context.pyc (Python 3.11)

from __future__ import annotations
import itertools
from typing import Any
from typing import cast
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from  import attributes
from  import interfaces
from  import loading
from base import _is_aliased_class
from interfaces import ORMColumnDescription
from interfaces import ORMColumnsClauseRole
from path_registry import PathRegistry
from util import _entity_corresponds_to
from util import _ORMJoin
from util import _TraceAdaptRole
from util import AliasedClass
from util import Bundle
from util import ORMAdapter
from util import ORMStatementAdapter
from  import exc as sa_exc
from  import future
from  import inspect
from  import sql
from  import util
from sql import coercions
from sql import expression
from sql import roles
from sql import util as sql_util
from sql import visitors
from sql._typing import _TP
from sql._typing import is_dml
from sql._typing import is_insert_update
from sql._typing import is_select_base
from sql.base import _select_iterables
from sql.base import CacheableOptions
from sql.base import CompileState
from sql.base import Executable
from sql.base import Generative
from sql.base import Options
from sql.dml import UpdateBase
from sql.elements import GroupedElement
from sql.elements import TextClause
from sql.selectable import CompoundSelectState
from sql.selectable import LABEL_STYLE_DISAMBIGUATE_ONLY
from sql.selectable import LABEL_STYLE_NONE
from sql.selectable import LABEL_STYLE_TABLENAME_PLUS_COL
from sql.selectable import Select
from sql.selectable import SelectLabelStyle
from sql.selectable import SelectState
from sql.selectable import TypedReturnsRows
from sql.visitors import InternalTraversal
if TYPE_CHECKING:
    from _typing import _InternalEntityType
    from _typing import OrmExecuteOptionsParameter
    from loading import PostLoad
    from mapper import Mapper
    from query import Query
    from session import _BindArguments
    from session import Session
    from engine import Result
    from engine.interfaces import _CoreSingleExecuteParams
    from sql._typing import _ColumnsClauseArgument
    from sql.compiler import SQLCompiler
    from sql.dml import _DMLTableElement
    from sql.elements import ColumnElement
    from sql.selectable import _JoinTargetElement
    from sql.selectable import _LabelConventionCallable
    from sql.selectable import _SetupJoinsElement
    from sql.selectable import ExecutableReturnsRows
    from sql.selectable import SelectBase
    from sql.type_api import TypeEngine
_T = TypeVar('_T', bound = Any)
_path_registry = PathRegistry.root
_EMPTY_DICT = util.immutabledict()
LABEL_STYLE_LEGACY_ORM = SelectLabelStyle.LABEL_STYLE_LEGACY_ORM

class QueryContext:
    compile_state: 'ORMCompileState' = ('top_level_context', 'compile_state', 'query', 'user_passed_query', 'params', 'load_options', 'bind_arguments', 'execution_options', 'session', 'autoflush', 'populate_existing', 'invoke_all_eagers', 'version_check', 'refresh_state', 'create_eager_joins', 'propagated_loader_options', 'attributes', 'runid', 'partials', 'post_load_paths', 'identity_token', 'yield_per', 'loaders_require_buffering', 'loaders_require_uniquing')
    
    class default_load_options(Options):
        _only_return_tuples = False
        _populate_existing = False
        _version_check = False
        _invoke_all_eagers = True
        _autoflush = True
        _identity_token = None
        _yield_per = None
        _refresh_state = None
        _lazy_loaded_from = None
        _legacy_uniquing = False
        _sa_top_level_orm_context = None
        _is_user_refresh = False

    
    def __init__(self, compile_state, statement, user_passed_query, params = None, session = None, load_options = None, execution_options = (None, None), bind_arguments = ('compile_state', 'CompileState', 'statement', 'Union[Select[Any], FromStatement[Any], UpdateBase]', 'user_passed_query', 'Union[Select[Any], FromStatement[Any], UpdateBase]', 'params', '_CoreSingleExecuteParams', 'session', 'Session', 'load_options', 'Union[Type[QueryContext.default_load_options], QueryContext.default_load_options]', 'execution_options', 'Optional[OrmExecuteOptionsParameter]', 'bind_arguments', 'Optional[_BindArguments]')):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_top_level_context(self = None):
