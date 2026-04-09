# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pg_catalog.pyc (Python 3.11)

from __future__ import annotations
from typing import Any
from typing import Optional
from typing import Sequence
from typing import TYPE_CHECKING
from array import ARRAY
from types import OID
from types import REGCLASS
from  import Column
from  import func
from  import MetaData
from  import Table
from types import BigInteger
from types import Boolean
from types import CHAR
from types import Float
from types import Integer
from types import SmallInteger
from types import String
from types import Text
from types import TypeDecorator
if TYPE_CHECKING:
    from engine.interfaces import Dialect
    from sql.type_api import _ResultProcessorType

def NAME():
    '''NAME'''
    impl = String(64, collation = 'C')
    cache_ok = True

NAME = <NODE:27>(NAME, 'NAME', TypeDecorator[str])

def PG_NODE_TREE():
    '''PG_NODE_TREE'''
    impl = Text(collation = 'C')
    cache_ok = True

PG_NODE_TREE = <NODE:27>(PG_NODE_TREE, 'PG_NODE_TREE', TypeDecorator[str])

def INT2VECTOR():
    '''INT2VECTOR'''
    impl = ARRAY(SmallInteger)
    cache_ok = True

INT2VECTOR = <NODE:27>(INT2VECTOR, 'INT2VECTOR', TypeDecorator[Sequence[int]])

def OIDVECTOR():
    '''OIDVECTOR'''
    impl = ARRAY(OID)
    cache_ok = True

OIDVECTOR = <NODE:27>(OIDVECTOR, 'OIDVECTOR', TypeDecorator[Sequence[int]])

class _SpaceVector:
    
    def result_processor(self = None, dialect = None, coltype = None):
        
        def process(value = None):
            pass
        # WARNING: Decompyle incomplete

        return process


REGPROC = REGCLASS
_pg_cat = func.pg_catalog
quote_ident = _pg_cat.quote_ident
pg_table_is_visible = _pg_cat.pg_table_is_visible
pg_type_is_visible = _pg_cat.pg_type_is_visible
pg_get_viewdef = _pg_cat.pg_get_viewdef
pg_get_serial_sequence = _pg_cat.pg_get_serial_sequence
format_type = _pg_cat.format_type
pg_get_expr = _pg_cat.pg_get_expr
pg_get_constraintdef = _pg_cat.pg_get_constraintdef
pg_get_indexdef = _pg_cat.pg_get_indexdef
RELKINDS_TABLE_NO_FOREIGN = ('r', 'p')
RELKINDS_TABLE = RELKINDS_TABLE_NO_FOREIGN + ('f',)
RELKINDS_VIEW = ('v',)
RELKINDS_MAT_VIEW = ('m',)
RELKINDS_ALL_TABLE_LIKE = RELKINDS_TABLE + RELKINDS_VIEW + RELKINDS_MAT_VIEW
pg_catalog_meta = MetaData(schema = 'pg_catalog')
pg_namespace = Table('pg_namespace', pg_catalog_meta, Column('oid', OID), Column('nspname', NAME), Column('nspowner', OID))
# WARNING: Decompyle incomplete
