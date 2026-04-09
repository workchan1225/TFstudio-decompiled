# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
The sqlite3 extension module provides a DB-API 2.0 (PEP 249) compliant
interface to the SQLite library, and requires SQLite 3.7.15 or newer.

To use the module, start by creating a database Connection object:

    import sqlite3
    cx = sqlite3.connect("test.db")  # test.db will be created or opened

The special path name ":memory:" can be provided to connect to a transient
in-memory database:

    cx = sqlite3.connect(":memory:")  # connect to a database in RAM

Once a connection has been established, create a Cursor object and call
its execute() method to perform SQL queries:

    cu = cx.cursor()

    # create a table
    cu.execute("create table lang(name, first_appeared)")

    # insert values into a table
    cu.execute("insert into lang values (?, ?)", ("C", 1972))

    # execute a query and iterate over the result
    for row in cu.execute("select * from lang"):
        print(row)

    cx.close()

The sqlite3 module is written by Gerhard Häring <gh@ghaering.de>.
'''
from sqlite3.dbapi2 import *

def __getattr__(name):
    if name == 'OptimizedUnicode':
        import warnings
        msg = "\n            OptimizedUnicode is deprecated and will be removed in Python 3.12.\n            Since Python 3.3 it has simply been an alias for 'str'.\n        "
        warnings.warn(msg, DeprecationWarning, stacklevel = 2)
        return str
    raise None(f'''module \'sqlite3\' has no attribute \'{name}\'''')
