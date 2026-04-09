# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ddl.pyc (Python 3.11)

'''
Provides the hierarchy of DDL-defining schema items as well as routines
to invoke them for a create/drop call.

'''
from __future__ import annotations
import contextlib
import typing
from typing import Any
from typing import Callable
from typing import Generic
from typing import Iterable
from typing import List
from typing import Optional
from typing import Sequence as typing_Sequence
from typing import Tuple
from typing import TypeVar
from typing import Union
from  import roles
from base import _generative
from base import Executable
from base import SchemaVisitor
from elements import ClauseElement
from  import exc
from  import util
from util import topological
from util.typing import Protocol
from util.typing import Self
if typing.TYPE_CHECKING:
    from compiler import Compiled
    from compiler import DDLCompiler
    from elements import BindParameter
    from schema import Column
    from schema import Constraint
    from schema import ForeignKeyConstraint
    from schema import Index
    from schema import SchemaItem
    from schema import Sequence
    from schema import Table
    from selectable import TableClause
    from engine.base import Connection
    from engine.interfaces import CacheStats
    from engine.interfaces import CompiledCacheType
    from engine.interfaces import Dialect
    from engine.interfaces import SchemaTranslateMapType
_SI = TypeVar('_SI', bound = Union[('SchemaItem', str)])

class BaseDDLElement(ClauseElement):
    '''The root of DDL constructs, including those that are sub-elements
    within the "create table" and other processes.

    .. versionadded:: 2.0

    '''
    _hierarchy_supports_caching = False
    
    def _compiler(self, dialect, **kw):
        '''Return a compiler appropriate for this ClauseElement, given a
        Dialect.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _compile_w_cache(self = None, dialect = None, *, compiled_cache, column_keys, for_executemany, schema_translate_map, **kw):
        raise NotImplementedError()



class DDLIfCallable(Protocol):
    
    def __call__(self = None, ddl = None, target = None, bind = None, tables = (None, None), state = {
        'compiler': ... }, *, dialect, compiler, checkfirst):
        pass



class DDLIf(typing.NamedTuple):
    state: 'Optional[Any]' = 'DDLIf'
    
    def _should_execute(self = None, ddl = None, target = None, bind = (None,), compiler = ('ddl', 'BaseDDLElement', 'target', 'Union[SchemaItem, str]', 'bind', 'Optional[Connection]', 'compiler', 'Optional[DDLCompiler]', 'kw', 'Any', 'return', 'bool'), **kw):
        pass
    # WARNING: Decompyle incomplete



class ExecutableDDLElement(BaseDDLElement, Executable, roles.DDLRole):
    '''Base class for standalone executable DDL expression constructs.

    This class is the base for the general purpose :class:`.DDL` class,
    as well as the various create/drop clause constructs such as
    :class:`.CreateTable`, :class:`.DropTable`, :class:`.AddConstraint`,
    etc.

    .. versionchanged:: 2.0  :class:`.ExecutableDDLElement` is renamed from
       :class:`.DDLElement`, which still exists for backwards compatibility.

    :class:`.ExecutableDDLElement` integrates closely with SQLAlchemy events,
    introduced in :ref:`event_toplevel`.  An instance of one is
    itself an event receiving callable::

        event.listen(
            users,
            "after_create",
            AddConstraint(constraint).execute_if(dialect="postgresql"),
        )

    .. seealso::

        :class:`.DDL`

        :class:`.DDLEvents`

        :ref:`event_toplevel`

        :ref:`schema_ddl_sequences`

    '''
    _ddl_if: 'Optional[DDLIf]' = None
    target: 'Union[SchemaItem, str, None]' = None
    
    def _execute_on_connection(self, connection, distilled_params, execution_options):
        return connection._execute_ddl(self, distilled_params, execution_options)

    against = (lambda self = None, target = None: self.target = targetself)()
    execute_if = (lambda self = None, dialect = None, callable_ = _generative, state = (None, None, None): self._ddl_if = DDLIf(dialect, callable_, state)self)()
    
    def _should_execute(self, target, bind, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def _invoke_with(self, bind):
        if self._should_execute(self.target, bind):
            return bind.execute(self)

    
    def __call__(self, target, bind, **kw):
        '''Execute the DDL as a ddl_listener.'''
        self.against(target)._invoke_with(bind)

    
    def _generate(self):
        s = self.__class__.__new__(self.__class__)
        s.__dict__ = self.__dict__.copy()
        return s


DDLElement = ExecutableDDLElement

class DDL(ExecutableDDLElement):
    '''A literal DDL statement.

    Specifies literal SQL DDL to be executed by the database.  DDL objects
    function as DDL event listeners, and can be subscribed to those events
    listed in :class:`.DDLEvents`, using either :class:`_schema.Table` or
    :class:`_schema.MetaData` objects as targets.
    Basic templating support allows
    a single DDL instance to handle repetitive tasks for multiple tables.

    Examples::

      from sqlalchemy import event, DDL

      tbl = Table("users", metadata, Column("uid", Integer))
      event.listen(tbl, "before_create", DDL("DROP TRIGGER users_trigger"))

      spow = DDL("ALTER TABLE %(table)s SET secretpowers TRUE")
      event.listen(tbl, "after_create", spow.execute_if(dialect="somedb"))

      drop_spow = DDL("ALTER TABLE users SET secretpowers FALSE")
      connection.execute(drop_spow)

    When operating on Table events, the following ``statement``
    string substitutions are available:

    .. sourcecode:: text

      %(table)s  - the Table name, with any required quoting applied
      %(schema)s - the schema name, with any required quoting applied
      %(fullname)s - the Table name including schema, quoted if needed

    The DDL\'s "context", if any, will be combined with the standard
    substitutions noted above.  Keys present in the context will override
    the standard substitutions.

    '''
    __visit_name__ = 'ddl'
    
    def __init__(self, statement, context = (None,)):
