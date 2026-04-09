# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sqlitedb.pyc (Python 3.11)

'''SQLite abstraction for coverage.py'''
from __future__ import annotations
import contextlib
import re
import sqlite3
from collections.abc import Iterable, Iterator
from typing import Any, cast
from coverage.debug import auto_repr, clipped_repr, exc_one_line
from coverage.exceptions import DataError
from coverage.types import TDebugCtl

class SqliteDb:
    '''A simple abstraction over a SQLite database.

    Use as a context manager, then you can use it like a
    :class:`python:sqlite3.Connection` object::

        with SqliteDb(filename, debug_control) as db:
            with db.execute("select a, b from some_table") as cur:
                for a, b in cur:
                    etc(a, b)

    '''
    
    def __init__(self = None, filename = None, debug = None, no_disk = (False,)):
        self.debug = debug
        self.filename = filename
        self.no_disk = no_disk
        self.nest = 0
        self.con = None

    __repr__ = auto_repr
    
    def _connect(self = None):
        '''Connect to the db and do universal initialization.'''
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None, force = None):
        '''If needed, close the connection.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _execute(self = None, sql = None, parameters = None):
        '''Same as :meth:`python:sqlite3.Connection.execute`.'''
        if self.debug.should('sql'):
            tail = f''' with {parameters!r}''' if parameters else ''
            self.debug.write(f'''Executing {sql!r}{tail}''')
    # WARNING: Decompyle incomplete

    execute = (lambda self = None, sql = None, parameters = contextlib.contextmanager: pass# WARNING: Decompyle incomplete
)()
    
    def execute_void(self = None, sql = None, parameters = None, fail_ok = ((), False)):
        """Same as :meth:`python:sqlite3.Connection.execute` when you don't need the cursor.

        If `fail_ok` is True, then SQLite errors are ignored.
        """
        
        try:
            self._execute(sql, parameters).close()
            return None
        except DataError:
            if not fail_ok:
                raise 
            return None


    
    def execute_for_rowid(self = None, sql = None, parameters = None):
        '''Like execute, but returns the lastrowid.'''
        cur = self.execute(sql, parameters)
    # WARNING: Decompyle incomplete

    
    def execute_one(self = None, sql = None, parameters = None):
