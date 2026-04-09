# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exc.pyc (Python 3.11)

'''Exceptions used with SQLAlchemy.

The base exception class is :exc:`.SQLAlchemyError`.  Exceptions which are
raised as a result of DBAPI exceptions are all subclasses of
:exc:`.DBAPIError`.

'''
from __future__ import annotations
import typing
from typing import Any
from typing import List
from typing import Optional
from typing import overload
from typing import Tuple
from typing import Type
from typing import Union
from util import compat
from util import preloaded as _preloaded
if typing.TYPE_CHECKING:
    from engine.interfaces import _AnyExecuteParams
    from engine.interfaces import Dialect
    from sql.compiler import Compiled
    from sql.compiler import TypeCompiler
    from sql.elements import ClauseElement
if typing.TYPE_CHECKING:
    _version_token: 'str'
else:
    _version_token = None

class HasDescriptionCode:
    pass
# WARNING: Decompyle incomplete


class SQLAlchemyError(Exception, HasDescriptionCode):
    '''Generic error class.'''
    
    def _message(self = None):
        if len(self.args) == 1:
            arg_text = self.args[0]
            if isinstance(arg_text, bytes):
                text = compat.decode_backslashreplace(arg_text, 'utf-8')
            else:
                text = str(arg_text)
            return text
        return None(self.args)

    
    def _sql_message(self = None):
        message = self._message()
        if self.code:
            message = f'''{message!s} {self._code_str()!s}'''
        return message

    
    def __str__(self = None):
        return self._sql_message()



class ArgumentError(SQLAlchemyError):
    '''Raised when an invalid or conflicting function argument is supplied.

    This error generally corresponds to construction time state errors.

    '''
    pass


class DuplicateColumnError(ArgumentError):
    '''a Column is being added to a Table that would replace another
    Column, without appropriate parameters to allow this in place.

    .. versionadded:: 2.0.0b4

    '''
    pass


class ObjectNotExecutableError(ArgumentError):
    pass
# WARNING: Decompyle incomplete


class NoSuchModuleError(ArgumentError):
    '''Raised when a dynamically-loaded module (usually a database dialect)
    of a particular name cannot be located.'''
    pass


class NoForeignKeysError(ArgumentError):
    '''Raised when no foreign keys can be located between two selectables
    during a join.'''
    pass


class AmbiguousForeignKeysError(ArgumentError):
    '''Raised when more than one foreign key matching can be located
    between two selectables during a join.'''
    pass


class ConstraintColumnNotFoundError(ArgumentError):
    '''raised when a constraint refers to a string column name that
    is not present in the table being constrained.

    .. versionadded:: 2.0

    '''
    pass


class CircularDependencyError(SQLAlchemyError):
    '''Raised by topological sorts when a circular dependency is detected.

    There are two scenarios where this error occurs:

    * In a Session flush operation, if two objects are mutually dependent
      on each other, they can not be inserted or deleted via INSERT or
      DELETE statements alone; an UPDATE will be needed to post-associate
      or pre-deassociate one of the foreign key constrained values.
      The ``post_update`` flag described at :ref:`post_update` can resolve
      this cycle.
    * In a :attr:`_schema.MetaData.sorted_tables` operation, two
      :class:`_schema.ForeignKey`
      or :class:`_schema.ForeignKeyConstraint` objects mutually refer to each
      other.  Apply the ``use_alter=True`` flag to one or both,
      see :ref:`use_alter`.

    '''
    
    def __init__(self, message = None, cycles = None, edges = None, msg = (None, None), code = ('message', 'str', 'cycles', 'Any', 'edges', 'Any', 'msg', 'Optional[str]', 'code', 'Optional[str]')):
        pass
    # WARNING: Decompyle incomplete

    
    def __reduce__(self = None):
        pass
    # WARNING: Decompyle incomplete



class CompileError(SQLAlchemyError):
    '''Raised when an error occurs during SQL compilation'''
    pass


class UnsupportedCompilationError(CompileError):
    pass
# WARNING: Decompyle incomplete


class IdentifierError(SQLAlchemyError):
    '''Raised when a schema name is beyond the max character limit'''
    pass


class DisconnectionError(SQLAlchemyError):
    '''A disconnect is detected on a raw DB-API connection.

    This error is raised and consumed internally by a connection pool.  It can
    be raised by the :meth:`_events.PoolEvents.checkout`
    event so that the host pool
    forces a retry; the exception will be caught three times in a row before
    the pool gives up and raises :class:`~sqlalchemy.exc.InvalidRequestError`
    regarding the connection attempt.

    '''
    invalidate_pool: 'bool' = False


class InvalidatePoolError(DisconnectionError):
    '''Raised when the connection pool should invalidate all stale connections.

    A subclass of :class:`_exc.DisconnectionError` that indicates that the
    disconnect situation encountered on the connection probably means the
    entire pool should be invalidated, as the database has been restarted.

    This exception will be handled otherwise the same way as
    :class:`_exc.DisconnectionError`, allowing three attempts to reconnect
    before giving up.

    .. versionadded:: 1.2

    '''
    invalidate_pool: 'bool' = True


class TimeoutError(SQLAlchemyError):
    '''Raised when a connection pool times out on getting a connection.'''
    pass


class InvalidRequestError(SQLAlchemyError):
    """SQLAlchemy was asked to do something it can't do.

    This error generally corresponds to runtime state errors.

    """
    pass


class IllegalStateChangeError(InvalidRequestError):
    '''An object that tracks state encountered an illegal state change
    of some kind.

    .. versionadded:: 2.0

    '''
    pass


class NoInspectionAvailable(InvalidRequestError):
    '''A subject passed to :func:`sqlalchemy.inspection.inspect` produced
    no context for inspection.'''
    pass


class PendingRollbackError(InvalidRequestError):
    '''A transaction has failed and needs to be rolled back before
    continuing.

    .. versionadded:: 1.4

    '''
    pass


class ResourceClosedError(InvalidRequestError):
    """An operation was requested from a connection, cursor, or other
    object that's in a closed state."""
    pass


class NoSuchColumnError(KeyError, InvalidRequestError):
    '''A nonexistent column is requested from a ``Row``.'''
    pass


class NoResultFound(InvalidRequestError):
    '''A database result was required but none was found.


    .. versionchanged:: 1.4  This exception is now part of the
       ``sqlalchemy.exc`` module in Core, moved from the ORM.  The symbol
       remains importable from ``sqlalchemy.orm.exc``.


    '''
    pass


class MultipleResultsFound(InvalidRequestError):
    '''A single database result was required but more than one were found.

    .. versionchanged:: 1.4  This exception is now part of the
       ``sqlalchemy.exc`` module in Core, moved from the ORM.  The symbol
       remains importable from ``sqlalchemy.orm.exc``.


    '''
    pass


class NoReferenceError(InvalidRequestError):
    table_name: 'str' = 'Raised by ``ForeignKey`` to indicate a reference cannot be resolved.'


class AwaitRequired(InvalidRequestError):
    '''Error raised by the async greenlet spawn if no async operation
    was awaited when it required one.

    '''
    code = 'xd1r'


class MissingGreenlet(InvalidRequestError):
    '''Error raised by the async greenlet await\\_ if called while not inside
    the greenlet spawn context.

    '''
    code = 'xd2s'


class NoReferencedTableError(NoReferenceError):
    '''Raised by ``ForeignKey`` when the referred ``Table`` cannot be
    located.

    '''
    
    def __init__(self = None, message = None, tname = None):
        NoReferenceError.__init__(self, message)
        self.table_name = tname

    
    def __reduce__(self = None):
        return (self.__class__, (self.args[0], self.table_name))



class NoReferencedColumnError(NoReferenceError):
    '''Raised by ``ForeignKey`` when the referred ``Column`` cannot be
    located.

    '''
    
    def __init__(self = None, message = None, tname = None, cname = ('message', 'str', 'tname', 'str', 'cname', 'str')):
        NoReferenceError.__init__(self, message)
        self.table_name = tname
        self.column_name = cname

    
    def __reduce__(self = None):
        return (self.__class__, (self.args[0], self.table_name, self.column_name))



class NoSuchTableError(InvalidRequestError):
    '''Table does not exist or is not visible to a connection.'''
    pass


class UnreflectableTableError(InvalidRequestError):
    """Table exists but can't be reflected for some reason.

    .. versionadded:: 1.2

    """
    pass


class UnboundExecutionError(InvalidRequestError):
    '''SQL was attempted without a database connection to execute it on.'''
    pass


class DontWrapMixin:
    '''A mixin class which, when applied to a user-defined Exception class,
    will not be wrapped inside of :exc:`.StatementError` if the error is
    emitted within the process of executing a statement.

    E.g.::

        from sqlalchemy.exc import DontWrapMixin


        class MyCustomException(Exception, DontWrapMixin):
            pass


        class MySpecialType(TypeDecorator):
            impl = String

            def process_bind_param(self, value, dialect):
                if value == "invalid":
                    raise MyCustomException("invalid!")

    '''
    pass


class StatementError(SQLAlchemyError):
    '''An error occurred during execution of a SQL statement.

    :class:`StatementError` wraps the exception raised
    during execution, and features :attr:`.statement`
    and :attr:`.params` attributes which supply context regarding
    the specifics of the statement which had an issue.

    The wrapped exception object is available in
    the :attr:`.orig` attribute.

    '''
    statement: 'Optional[str]' = None
    params: 'Optional[_AnyExecuteParams]' = None
    orig: 'Optional[BaseException]' = None
    ismulti: 'Optional[bool]' = None
    connection_invalidated: 'bool' = False
    
    def __init__(self, message, statement, params = None, orig = None, hide_parameters = None, code = (False, None, None), ismulti = ('message', 'str', 'statement', 'Optional[str]', 'params', 'Optional[_AnyExecuteParams]', 'orig', 'Optional[BaseException]', 'hide_parameters', 'bool', 'code', 'Optional[str]', 'ismulti', 'Optional[bool]')):
        SQLAlchemyError.__init__(self, message, code = code)
        self.statement = statement
        self.params = params
        self.orig = orig
        self.ismulti = ismulti
        self.hide_parameters = hide_parameters
        self.detail = []

    
    def add_detail(self = None, msg = None):
        self.detail.append(msg)

    
    def __reduce__(self = None):
        return (self.__class__, (self.args[0], self.statement, self.params, self.orig, self.hide_parameters, self.__dict__.get('code'), self.ismulti), {
            'detail': self.detail })

    _sql_message = (lambda self = None: util = _preloaded.sql_utildetails = [
self._message()]if self.statement:
stmt_detail = '[SQL: %s]' % self.statementdetails.append(stmt_detail)if self.params:
if self.hide_parameters:
details.append('[SQL parameters hidden due to hide_parameters=True]')else:
params_repr = util._repr_params(self.params, 10, ismulti = self.ismulti)details.append('[parameters: %r]' % params_repr)code_str = self._code_str()if code_str:
details.append(code_str)(lambda .0: [ '(%s)' % det for det in .0 ])(self.detail() + details)
)()


class DBAPIError(StatementError):
    """Raised when the execution of a database operation fails.

    Wraps exceptions raised by the DB-API underlying the
    database operation.  Driver-specific implementations of the standard
    DB-API exception types are wrapped by matching sub-types of SQLAlchemy's
    :class:`DBAPIError` when possible.  DB-API's ``Error`` type maps to
    :class:`DBAPIError` in SQLAlchemy, otherwise the names are identical.  Note
    that there is no guarantee that different DB-API implementations will
    raise the same exception type for any given error condition.

    :class:`DBAPIError` features :attr:`~.StatementError.statement`
    and :attr:`~.StatementError.params` attributes which supply context
    regarding the specifics of the statement which had an issue, for the
    typical case when the error was raised within the context of
    emitting a SQL statement.

    The wrapped exception object is available in the
    :attr:`~.StatementError.orig` attribute. Its type and properties are
    DB-API implementation specific.

    """
    code = 'dbapi'
    instance = (lambda cls, statement, params, orig, dbapi_base_err = None, hide_parameters = overload, connection_invalidated = classmethod, dialect = (False, False, None, None), ismulti = ('statement', 'Optional[str]', 'params', 'Optional[_AnyExecuteParams]', 'orig', 'Exception', 'dbapi_base_err', 'Type[Exception]', 'hide_parameters', 'bool', 'connection_invalidated', 'bool', 'dialect', 'Optional[Dialect]', 'ismulti', 'Optional[bool]', 'return', 'StatementError'): pass)()()
    instance = (lambda cls, statement, params, orig, dbapi_base_err = None, hide_parameters = overload, connection_invalidated = classmethod, dialect = (False, False, None, None), ismulti = ('statement', 'Optional[str]', 'params', 'Optional[_AnyExecuteParams]', 'orig', 'DontWrapMixin', 'dbapi_base_err', 'Type[Exception]', 'hide_parameters', 'bool', 'connection_invalidated', 'bool', 'dialect', 'Optional[Dialect]', 'ismulti', 'Optional[bool]', 'return', 'DontWrapMixin'): pass)()()
    instance = (lambda cls, statement, params, orig, dbapi_base_err = None, hide_parameters = overload, connection_invalidated = classmethod, dialect = (False, False, None, None), ismulti = ('statement', 'Optional[str]', 'params', 'Optional[_AnyExecuteParams]', 'orig', 'BaseException', 'dbapi_base_err', 'Type[Exception]', 'hide_parameters', 'bool', 'connection_invalidated', 'bool', 'dialect', 'Optional[Dialect]', 'ismulti', 'Optional[bool]', 'return', 'BaseException'): pass)()()
    instance = (lambda cls, statement, params, orig, dbapi_base_err = None, hide_parameters = None, connection_invalidated = classmethod, dialect = (False, False, None, None), ismulti = ('statement', 'Optional[str]', 'params', 'Optional[_AnyExecuteParams]', 'orig', 'Union[BaseException, DontWrapMixin]', 'dbapi_base_err', 'Type[Exception]', 'hide_parameters', 'bool', 'connection_invalidated', 'bool', 'dialect', 'Optional[Dialect]', 'ismulti', 'Optional[bool]', 'return', 'Union[BaseException, DontWrapMixin]'): if isinstance(orig, BaseException) or isinstance(orig, Exception) or isinstance(orig, DontWrapMixin):
orig# WARNING: Decompyle incomplete
)()
    
    def __reduce__(self = None):
        return (self.__class__, (self.statement, self.params, self.orig, self.hide_parameters, self.connection_invalidated, self.__dict__.get('code'), self.ismulti), {
            'detail': self.detail })

    
    def __init__(self, statement, params, orig = None, hide_parameters = None, connection_invalidated = None, code = (False, False, None, None), ismulti = ('statement', 'Optional[str]', 'params', 'Optional[_AnyExecuteParams]', 'orig', 'BaseException', 'hide_parameters', 'bool', 'connection_invalidated', 'bool', 'code', 'Optional[str]', 'ismulti', 'Optional[bool]')):
        
        try:
            text = str(orig)
        except Exception:
            e = None
            text = 'Error in str() of DB-API-generated exception: ' + str(e)
            e = None
            del e
        except:
            e = None
            del e

        StatementError.__init__(self, f'''({orig.__class__.__module__!s}.{orig.__class__.__name__!s}) {text!s}''', statement, params, orig, hide_parameters, code = code, ismulti = ismulti)
        self.connection_invalidated = connection_invalidated



class InterfaceError(DBAPIError):
    '''Wraps a DB-API InterfaceError.'''
    code = 'rvf5'


class DatabaseError(DBAPIError):
    '''Wraps a DB-API DatabaseError.'''
    code = '4xp6'


class DataError(DatabaseError):
    '''Wraps a DB-API DataError.'''
    code = '9h9h'


class OperationalError(DatabaseError):
    '''Wraps a DB-API OperationalError.'''
    code = 'e3q8'


class IntegrityError(DatabaseError):
    '''Wraps a DB-API IntegrityError.'''
    code = 'gkpj'


class InternalError(DatabaseError):
    '''Wraps a DB-API InternalError.'''
    code = '2j85'


class ProgrammingError(DatabaseError):
    '''Wraps a DB-API ProgrammingError.'''
    code = 'f405'


class NotSupportedError(DatabaseError):
    '''Wraps a DB-API NotSupportedError.'''
    code = 'tw8g'


class SATestSuiteWarning(Warning):
    '''warning for a condition detected during tests that is non-fatal

    Currently outside of SAWarning so that we can work around tools like
    Alembic doing the wrong thing with warnings.

    '''
    pass


class SADeprecationWarning(DeprecationWarning, HasDescriptionCode):
    '''Issued for usage of deprecated APIs.'''
    deprecated_since: 'Optional[str]' = None


class Base20DeprecationWarning(SADeprecationWarning):
    pass
# WARNING: Decompyle incomplete


class LegacyAPIWarning(Base20DeprecationWarning):
    """indicates an API that is in 'legacy' status, a long term deprecation."""
    pass


class MovedIn20Warning(Base20DeprecationWarning):
    '''Subtype of RemovedIn20Warning to indicate an API that moved only.'''
    pass


class SAPendingDeprecationWarning(PendingDeprecationWarning):
    '''A similar warning as :class:`_exc.SADeprecationWarning`, this warning
    is not used in modern versions of SQLAlchemy.

    '''
    deprecated_since: 'Optional[str]' = None


class SAWarning(RuntimeWarning, HasDescriptionCode):
    '''Issued at runtime.'''
    _what_are_we = 'warning'
