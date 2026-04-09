# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from __future__ import annotations
import datetime as dt
from typing import Optional
from typing import Type
from typing import TYPE_CHECKING
from  import exc
from sql import sqltypes
from types import NVARCHAR
from types import VARCHAR
if TYPE_CHECKING:
    from engine.interfaces import Dialect
    from sql.type_api import _LiteralProcessorType

class RAW(sqltypes._Binary):
    __visit_name__ = 'RAW'

OracleRaw = RAW

class NCLOB(sqltypes.Text):
    __visit_name__ = 'NCLOB'


class VARCHAR2(VARCHAR):
    __visit_name__ = 'VARCHAR2'

NVARCHAR2 = NVARCHAR

class NUMBER(sqltypes.Integer, sqltypes.Numeric):
    pass
# WARNING: Decompyle incomplete


class FLOAT(sqltypes.FLOAT):
    pass
# WARNING: Decompyle incomplete


class BINARY_DOUBLE(sqltypes.Double):
    '''Implement the Oracle ``BINARY_DOUBLE`` datatype.

    This datatype differs from the Oracle ``DOUBLE`` datatype in that it
    delivers a true 8-byte FP value.   The datatype may be combined with a
    generic :class:`.Double` datatype using :meth:`.TypeEngine.with_variant`.

    .. seealso::

        :ref:`oracle_float_support`


    '''
    __visit_name__ = 'BINARY_DOUBLE'


class BINARY_FLOAT(sqltypes.Float):
    '''Implement the Oracle ``BINARY_FLOAT`` datatype.

    This datatype differs from the Oracle ``FLOAT`` datatype in that it
    delivers a true 4-byte FP value.   The datatype may be combined with a
    generic :class:`.Float` datatype using :meth:`.TypeEngine.with_variant`.

    .. seealso::

        :ref:`oracle_float_support`


    '''
    __visit_name__ = 'BINARY_FLOAT'


class BFILE(sqltypes.LargeBinary):
    __visit_name__ = 'BFILE'


class LONG(sqltypes.Text):
    __visit_name__ = 'LONG'


class _OracleDateLiteralRender:
    
    def _literal_processor_datetime(self, dialect):
        
        def process(value):
            if getattr(value, 'microsecond', None):
                value = f'''TO_TIMESTAMP(\'{value.isoformat().replace('T', ' ')}\', \'YYYY-MM-DD HH24:MI:SS.FF\')'''
            else:
                value = f'''TO_DATE(\'{value.isoformat().replace('T', ' ')}\', \'YYYY-MM-DD HH24:MI:SS\')'''
            return value

        return process

    
    def _literal_processor_date(self, dialect):
        
        def process(value):
            if getattr(value, 'microsecond', None):
                value = f'''TO_TIMESTAMP(\'{value.isoformat().split('T')[0]}\', \'YYYY-MM-DD\')'''
            else:
                value = f'''TO_DATE(\'{value.isoformat().split('T')[0]}\', \'YYYY-MM-DD\')'''
            return value

        return process



class DATE(sqltypes.DateTime, _OracleDateLiteralRender):
    '''Provide the Oracle Database DATE type.

    This type has no special Python behavior, except that it subclasses
    :class:`_types.DateTime`; this is to suit the fact that the Oracle Database
    ``DATE`` type supports a time value.

    '''
    __visit_name__ = 'DATE'
    
    def literal_processor(self, dialect):
        return self._literal_processor_datetime(dialect)

    
    def _compare_type_affinity(self, other):
        return other._type_affinity in (sqltypes.DateTime, sqltypes.Date)



class _OracleDate(sqltypes.Date, _OracleDateLiteralRender):
    
    def literal_processor(self, dialect):
        return self._literal_processor_date(dialect)



class INTERVAL(sqltypes._AbstractInterval, sqltypes.NativeForEmulated):
    __visit_name__ = 'INTERVAL'
    
    def __init__(self, day_precision, second_precision = (None, None)):
        '''Construct an INTERVAL.

        Note that only DAY TO SECOND intervals are currently supported.
        This is due to a lack of support for YEAR TO MONTH intervals
        within available DBAPIs.

        :param day_precision: the day precision value.  this is the number of
          digits to store for the day field.  Defaults to "2"
        :param second_precision: the second precision value.  this is the
          number of digits to store for the fractional seconds field.
          Defaults to "6".

        '''
        self.day_precision = day_precision
        self.second_precision = second_precision

    _adapt_from_generic_interval = (lambda cls, interval: INTERVAL(day_precision = interval.day_precision, second_precision = interval.second_precision))()
    adapt_emulated_to_native = (lambda cls = None, interval = classmethod: INTERVAL(day_precision = interval.day_precision, second_precision = interval.second_precision))()
    _type_affinity = (lambda self: sqltypes.Interval)()
    
    def as_generic(self, allow_nulltype = (False,)):
        return sqltypes.Interval(native = True, second_precision = self.second_precision, day_precision = self.day_precision)

    python_type = (lambda self = None: dt.timedelta)()
    
    def literal_processor(self = None, dialect = None):
        
        def process(value = None):
            return f'''NUMTODSINTERVAL({value.total_seconds()}, \'SECOND\')'''

        return process



class TIMESTAMP(sqltypes.TIMESTAMP):
    pass
# WARNING: Decompyle incomplete


class ROWID(sqltypes.TypeEngine):
    '''Oracle Database ROWID type.

    When used in a cast() or similar, generates ROWID.

    '''
    __visit_name__ = 'ROWID'


class _OracleBoolean(sqltypes.Boolean):
    
    def get_dbapi_type(self, dbapi):
        return dbapi.NUMBER
