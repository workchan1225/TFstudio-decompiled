# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from __future__ import annotations
import datetime
import decimal
from typing import Any
from typing import Iterable
from typing import Optional
from typing import TYPE_CHECKING
from typing import Union
from  import exc
from  import util
from sql import sqltypes
if TYPE_CHECKING:
    from base import MySQLDialect
    from engine.interfaces import Dialect
    from sql.type_api import _BindProcessorType
    from sql.type_api import _ResultProcessorType
    from sql.type_api import TypeEngine

class _NumericType:
    pass
# WARNING: Decompyle incomplete


def _FloatType():
    '''_FloatType'''
    pass
# WARNING: Decompyle incomplete

_FloatType = <NODE:27>(_FloatType, '_FloatType', _NumericType, sqltypes.Float[Union[(decimal.Decimal, float)]])

class _IntegerType(sqltypes.Integer, _NumericType):
    pass
# WARNING: Decompyle incomplete


class _StringType(sqltypes.String):
    pass
# WARNING: Decompyle incomplete


def _MatchType():
    '''_MatchType'''
    
    def __init__(self = None, **kw):
        sqltypes.Float.__init__(self)
        sqltypes.MatchType.__init__(self)


_MatchType = <NODE:27>(_MatchType, '_MatchType', sqltypes.Float[Union[(decimal.Decimal, float)]], sqltypes.MatchType)

def NUMERIC():
    '''NUMERIC'''
    pass
# WARNING: Decompyle incomplete

NUMERIC = <NODE:27>(NUMERIC, 'NUMERIC', _NumericType, sqltypes.NUMERIC[Union[(decimal.Decimal, float)]])

def DECIMAL():
    '''DECIMAL'''
    pass
# WARNING: Decompyle incomplete

DECIMAL = <NODE:27>(DECIMAL, 'DECIMAL', _NumericType, sqltypes.DECIMAL[Union[(decimal.Decimal, float)]])

def DOUBLE():
    '''DOUBLE'''
    pass
# WARNING: Decompyle incomplete

DOUBLE = <NODE:27>(DOUBLE, 'DOUBLE', _FloatType, sqltypes.DOUBLE[Union[(decimal.Decimal, float)]])

def REAL():
    '''REAL'''
    pass
# WARNING: Decompyle incomplete

REAL = <NODE:27>(REAL, 'REAL', _FloatType, sqltypes.REAL[Union[(decimal.Decimal, float)]])

def FLOAT():
    '''FLOAT'''
    pass
# WARNING: Decompyle incomplete

FLOAT = <NODE:27>(FLOAT, 'FLOAT', _FloatType, sqltypes.FLOAT[Union[(decimal.Decimal, float)]])

class INTEGER(sqltypes.INTEGER, _IntegerType):
    pass
# WARNING: Decompyle incomplete


class BIGINT(sqltypes.BIGINT, _IntegerType):
    pass
# WARNING: Decompyle incomplete


class MEDIUMINT(_IntegerType):
    pass
# WARNING: Decompyle incomplete


class TINYINT(_IntegerType):
    pass
# WARNING: Decompyle incomplete


class SMALLINT(sqltypes.SMALLINT, _IntegerType):
    pass
# WARNING: Decompyle incomplete


def BIT():
    '''BIT'''
    __doc__ = 'MySQL BIT type.\n\n    This type is for MySQL 5.0.3 or greater for MyISAM, and 5.0.5 or greater\n    for MyISAM, MEMORY, InnoDB and BDB.  For older versions, use a\n    MSTinyInteger() type.\n\n    '
    __visit_name__ = 'BIT'
    
    def __init__(self = None, length = None):
        '''Construct a BIT.

        :param length: Optional, number of bits.

        '''
        self.length = length

    
    def result_processor(self = None, dialect = None, coltype = None):
        """Convert a MySQL's 64 bit, variable length binary string to a
        long."""
        if dialect.supports_native_bit:
            return None
        
        def process(value = None):
            pass
        # WARNING: Decompyle incomplete

        return process


BIT = <NODE:27>(BIT, 'BIT', sqltypes.TypeEngine[Any])

class TIME(sqltypes.TIME):
    pass
# WARNING: Decompyle incomplete


class TIMESTAMP(sqltypes.TIMESTAMP):
    pass
# WARNING: Decompyle incomplete


class DATETIME(sqltypes.DATETIME):
    pass
# WARNING: Decompyle incomplete


def YEAR():
    '''YEAR'''
    __doc__ = 'MySQL YEAR type, for single byte storage of years 1901-2155.'
    __visit_name__ = 'YEAR'
    
    def __init__(self = None, display_width = None):
        self.display_width = display_width


YEAR = <NODE:27>(YEAR, 'YEAR', sqltypes.TypeEngine[Any])

class TEXT(sqltypes.TEXT, _StringType):
    pass
# WARNING: Decompyle incomplete


class TINYTEXT(_StringType):
    pass
# WARNING: Decompyle incomplete


class MEDIUMTEXT(_StringType):
    pass
# WARNING: Decompyle incomplete


class LONGTEXT(_StringType):
    pass
# WARNING: Decompyle incomplete


class VARCHAR(sqltypes.VARCHAR, _StringType):
    pass
# WARNING: Decompyle incomplete


class CHAR(sqltypes.CHAR, _StringType):
    pass
# WARNING: Decompyle incomplete


class NVARCHAR(sqltypes.NVARCHAR, _StringType):
    pass
# WARNING: Decompyle incomplete


class NCHAR(sqltypes.NCHAR, _StringType):
    pass
# WARNING: Decompyle incomplete


class TINYBLOB(sqltypes._Binary):
    '''MySQL TINYBLOB type, for binary data up to 2^8 bytes.'''
    __visit_name__ = 'TINYBLOB'


class MEDIUMBLOB(sqltypes._Binary):
    '''MySQL MEDIUMBLOB type, for binary data up to 2^24 bytes.'''
    __visit_name__ = 'MEDIUMBLOB'


class LONGBLOB(sqltypes._Binary):
    '''MySQL LONGBLOB type, for binary data up to 2^32 bytes.'''
    __visit_name__ = 'LONGBLOB'
