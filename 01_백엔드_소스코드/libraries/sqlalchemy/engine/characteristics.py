# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: characteristics.pyc (Python 3.11)

from __future__ import annotations
import abc
import typing
from typing import Any
from typing import ClassVar
if typing.TYPE_CHECKING:
    from base import Connection
    from interfaces import DBAPIConnection
    from interfaces import Dialect

class ConnectionCharacteristic(abc.ABC):
    '''An abstract base for an object that can set, get and reset a
    per-connection characteristic, typically one that gets reset when the
    connection is returned to the connection pool.

    transaction isolation is the canonical example, and the
    ``IsolationLevelCharacteristic`` implementation provides this for the
    ``DefaultDialect``.

    The ``ConnectionCharacteristic`` class should call upon the ``Dialect`` for
    the implementation of each method.   The object exists strictly to serve as
    a dialect visitor that can be placed into the
    ``DefaultDialect.connection_characteristics`` dictionary where it will take
    effect for calls to :meth:`_engine.Connection.execution_options` and
    related APIs.

    .. versionadded:: 1.4

    '''
    __slots__ = ()
    transactional: 'ClassVar[bool]' = False
    reset_characteristic = (lambda self = None, dialect = None, dbapi_conn = abc.abstractmethod: pass)()
    set_characteristic = (lambda self = None, dialect = None, dbapi_conn = abc.abstractmethod, value = ('dialect', 'Dialect', 'dbapi_conn', 'DBAPIConnection', 'value', 'Any', 'return', 'None'): pass)()
    
    def set_connection_characteristic(self, dialect = None, conn = None, dbapi_conn = None, value = ('dialect', 'Dialect', 'conn', 'Connection', 'dbapi_conn', 'DBAPIConnection', 'value', 'Any', 'return', 'None')):
        '''set characteristic on the :class:`_engine.Connection` to a given
        value.

        .. versionadded:: 2.0.30 - added to support elements that are local
           to the :class:`_engine.Connection` itself.

        '''
        self.set_characteristic(dialect, dbapi_conn, value)

    get_characteristic = (lambda self = None, dialect = None, dbapi_conn = abc.abstractmethod: pass)()
    
    def get_connection_characteristic(self = None, dialect = None, conn = None, dbapi_conn = ('dialect', 'Dialect', 'conn', 'Connection', 'dbapi_conn', 'DBAPIConnection', 'return', 'Any')):
        '''Given a :class:`_engine.Connection`, get the current value of the
        characteristic.

        .. versionadded:: 2.0.30 - added to support elements that are local
           to the :class:`_engine.Connection` itself.

        '''
        return self.get_characteristic(dialect, dbapi_conn)



class IsolationLevelCharacteristic(ConnectionCharacteristic):
    '''Manage the isolation level on a DBAPI connection'''
    transactional: 'ClassVar[bool]' = True
    
    def reset_characteristic(self = None, dialect = None, dbapi_conn = None):
        dialect.reset_isolation_level(dbapi_conn)

    
    def set_characteristic(self = None, dialect = None, dbapi_conn = None, value = ('dialect', 'Dialect', 'dbapi_conn', 'DBAPIConnection', 'value', 'Any', 'return', 'None')):
        dialect._assert_and_set_isolation_level(dbapi_conn, value)

    
    def get_characteristic(self = None, dialect = None, dbapi_conn = None):
        return dialect.get_isolation_level(dbapi_conn)



class LoggingTokenCharacteristic(ConnectionCharacteristic):
    """Manage the 'logging_token' option of a :class:`_engine.Connection`.

    .. versionadded:: 2.0.30

    """
    transactional: 'ClassVar[bool]' = False
    
    def reset_characteristic(self = None, dialect = None, dbapi_conn = None):
        pass

    
    def set_characteristic(self = None, dialect = None, dbapi_conn = None, value = ('dialect', 'Dialect', 'dbapi_conn', 'DBAPIConnection', 'value', 'Any', 'return', 'None')):
        raise NotImplementedError()

    
    def set_connection_characteristic(self, dialect = None, conn = None, dbapi_conn = None, value = ('dialect', 'Dialect', 'conn', 'Connection', 'dbapi_conn', 'DBAPIConnection', 'value', 'Any', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def get_characteristic(self = None, dialect = None, dbapi_conn = None):
        raise NotImplementedError()

    
    def get_connection_characteristic(self = None, dialect = None, conn = None, dbapi_conn = ('dialect', 'Dialect', 'conn', 'Connection', 'dbapi_conn', 'DBAPIConnection', 'return', 'Any')):
        return conn._execution_options.get('logging_token', None)
