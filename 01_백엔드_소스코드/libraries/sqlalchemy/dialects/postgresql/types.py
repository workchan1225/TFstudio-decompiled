# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from __future__ import annotations
import datetime as dt
from typing import Any
from typing import Optional
from typing import overload
from typing import Type
from typing import TYPE_CHECKING
from uuid import UUID as _python_UUID
from sql import sqltypes
from sql import type_api
from util.typing import Literal
if TYPE_CHECKING:
    from engine.interfaces import Dialect
    from sql.operators import OperatorType
    from sql.type_api import _LiteralProcessorType
    from sql.type_api import TypeEngine
_DECIMAL_TYPES = (1231, 1700)
_FLOAT_TYPES = (700, 701, 1021, 1022)
_INT_TYPES = (20, 21, 23, 26, 1005, 1007, 1016)

def PGUuid():
    '''PGUuid'''
    render_bind_cast = True
    render_literal_cast = True
    if TYPE_CHECKING:
        __init__ = (lambda self = None, as_uuid = None: pass)()
        __init__ = (lambda self = None, as_uuid = None: pass)()
        
        def __init__(self = None, as_uuid = None):
            pass

        return None

PGUuid = <NODE:27>(PGUuid, 'PGUuid', sqltypes.UUID[sqltypes._UUID_RETURN])

class BYTEA(sqltypes.LargeBinary):
    __visit_name__ = 'BYTEA'


class _NetworkAddressTypeMixin:
    
    def coerce_compared_value(self = None, op = None, value = None):
        pass
    # WARNING: Decompyle incomplete



def INET():
    '''INET'''
    __visit_name__ = 'INET'

INET = <NODE:27>(INET, 'INET', _NetworkAddressTypeMixin, sqltypes.TypeEngine[str])
PGInet = INET

def CIDR():
    '''CIDR'''
    __visit_name__ = 'CIDR'

CIDR = <NODE:27>(CIDR, 'CIDR', _NetworkAddressTypeMixin, sqltypes.TypeEngine[str])
PGCidr = CIDR

def MACADDR():
    '''MACADDR'''
    __visit_name__ = 'MACADDR'

MACADDR = <NODE:27>(MACADDR, 'MACADDR', _NetworkAddressTypeMixin, sqltypes.TypeEngine[str])
PGMacAddr = MACADDR

def MACADDR8():
    '''MACADDR8'''
    __visit_name__ = 'MACADDR8'

MACADDR8 = <NODE:27>(MACADDR8, 'MACADDR8', _NetworkAddressTypeMixin, sqltypes.TypeEngine[str])
PGMacAddr8 = MACADDR8

def MONEY():
    '''MONEY'''
    __doc__ = 'Provide the PostgreSQL MONEY type.\n\n    Depending on driver, result rows using this type may return a\n    string value which includes currency symbols.\n\n    For this reason, it may be preferable to provide conversion to a\n    numerically-based currency datatype using :class:`_types.TypeDecorator`::\n\n        import re\n        import decimal\n        from sqlalchemy import Dialect\n        from sqlalchemy import TypeDecorator\n\n\n        class NumericMoney(TypeDecorator):\n            impl = MONEY\n\n            def process_result_value(self, value: Any, dialect: Dialect) -> None:\n                if value is not None:\n                    # adjust this for the currency and numeric\n                    m = re.match(r"\\$([\\d.]+)", value)\n                    if m:\n                        value = decimal.Decimal(m.group(1))\n                return value\n\n    Alternatively, the conversion may be applied as a CAST using\n    the :meth:`_types.TypeDecorator.column_expression` method as follows::\n\n        import decimal\n        from sqlalchemy import cast\n        from sqlalchemy import TypeDecorator\n\n\n        class NumericMoney(TypeDecorator):\n            impl = MONEY\n\n            def column_expression(self, column: Any):\n                return cast(column, Numeric())\n\n    .. versionadded:: 1.2\n\n    '
    __visit_name__ = 'MONEY'

MONEY = <NODE:27>(MONEY, 'MONEY', sqltypes.TypeEngine[str])

def OID():
    '''OID'''
    __doc__ = 'Provide the PostgreSQL OID type.'
    __visit_name__ = 'OID'

OID = <NODE:27>(OID, 'OID', sqltypes.TypeEngine[int])

def REGCONFIG():
    '''REGCONFIG'''
    __doc__ = 'Provide the PostgreSQL REGCONFIG type.\n\n    .. versionadded:: 2.0.0rc1\n\n    '
    __visit_name__ = 'REGCONFIG'

REGCONFIG = <NODE:27>(REGCONFIG, 'REGCONFIG', sqltypes.TypeEngine[str])

def TSQUERY():
    '''TSQUERY'''
    __doc__ = 'Provide the PostgreSQL TSQUERY type.\n\n    .. versionadded:: 2.0.0rc1\n\n    '
    __visit_name__ = 'TSQUERY'

TSQUERY = <NODE:27>(TSQUERY, 'TSQUERY', sqltypes.TypeEngine[str])

def REGCLASS():
    '''REGCLASS'''
    __doc__ = 'Provide the PostgreSQL REGCLASS type.\n\n    .. versionadded:: 1.2.7\n\n    '
    __visit_name__ = 'REGCLASS'

REGCLASS = <NODE:27>(REGCLASS, 'REGCLASS', sqltypes.TypeEngine[str])

class TIMESTAMP(sqltypes.TIMESTAMP):
    pass
# WARNING: Decompyle incomplete


class TIME(sqltypes.TIME):
    pass
# WARNING: Decompyle incomplete


class INTERVAL(sqltypes._AbstractInterval, type_api.NativeForEmulated):
    '''PostgreSQL INTERVAL type.'''
    __visit_name__ = 'INTERVAL'
    native = True
    
    def __init__(self = None, precision = None, fields = None):
        '''Construct an INTERVAL.

        :param precision: optional integer precision value
        :param fields: string fields specifier.  allows storage of fields
         to be limited, such as ``"YEAR"``, ``"MONTH"``, ``"DAY TO HOUR"``,
         etc.

         .. versionadded:: 1.2

        '''
        self.precision = precision
        self.fields = fields

    adapt_emulated_to_native = (lambda cls = None, interval = None: INTERVAL(precision = interval.second_precision))()
    _type_affinity = (lambda self = None: sqltypes.Interval)()
    
    def as_generic(self = None, allow_nulltype = None):
        return sqltypes.Interval(native = True, second_precision = self.precision)

    python_type = (lambda self = None: dt.timedelta)()
    
    def literal_processor(self = None, dialect = None):
        
        def process(value = None):
            return f'''make_interval(secs=>{value.total_seconds()})'''

        return process


PGInterval = INTERVAL

def BIT():
    '''BIT'''
    __visit_name__ = 'BIT'
    
    def __init__(self = None, length = None, varying = None):
        if varying:
            self.length = length
        elif not length:
            self.length = 1
            self.varying = varying
            return None


BIT = <NODE:27>(BIT, 'BIT', sqltypes.TypeEngine[int])
PGBit = BIT

def TSVECTOR():
    '''TSVECTOR'''
    __doc__ = 'The :class:`_postgresql.TSVECTOR` type implements the PostgreSQL\n    text search type TSVECTOR.\n\n    It can be used to do full text queries on natural language\n    documents.\n\n    .. seealso::\n\n        :ref:`postgresql_match`\n\n    '
    __visit_name__ = 'TSVECTOR'

TSVECTOR = <NODE:27>(TSVECTOR, 'TSVECTOR', sqltypes.TypeEngine[str])

class CITEXT(sqltypes.TEXT):
    '''Provide the PostgreSQL CITEXT type.

    .. versionadded:: 2.0.7

    '''
    __visit_name__ = 'CITEXT'
    
    def coerce_compared_value(self = None, op = None, value = None):
        return self
