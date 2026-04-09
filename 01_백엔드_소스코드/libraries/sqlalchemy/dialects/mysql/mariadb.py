# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mariadb.pyc (Python 3.11)

from __future__ import annotations
from typing import Any
from typing import Callable
from base import MariaDBIdentifierPreparer
from base import MySQLDialect
from base import MySQLIdentifierPreparer
from base import MySQLTypeCompiler
from sql import sqltypes

def INET4():
    '''INET4'''
    __doc__ = 'INET4 column type for MariaDB\n\n    .. versionadded:: 2.0.37\n    '
    __visit_name__ = 'INET4'

INET4 = <NODE:27>(INET4, 'INET4', sqltypes.TypeEngine[str])

def INET6():
    '''INET6'''
    __doc__ = 'INET6 column type for MariaDB\n\n    .. versionadded:: 2.0.37\n    '
    __visit_name__ = 'INET6'

INET6 = <NODE:27>(INET6, 'INET6', sqltypes.TypeEngine[str])

class MariaDBTypeCompiler(MySQLTypeCompiler):
    
    def visit_INET4(self = None, type_ = None, **kwargs):
        return 'INET4'

    
    def visit_INET6(self = None, type_ = None, **kwargs):
        return 'INET6'



class MariaDBDialect(MySQLDialect):
    is_mariadb = True
    supports_statement_cache = True
    name = 'mariadb'
    preparer: 'type[MySQLIdentifierPreparer]' = MariaDBIdentifierPreparer
    type_compiler_cls = MariaDBTypeCompiler


def loader(driver = None):
    dialect_mod = __import__('sqlalchemy.dialects.mysql.%s' % driver).dialects.mysql
    driver_mod = getattr(dialect_mod, driver)
    if hasattr(driver_mod, 'mariadb_dialect'):
        driver_cls = driver_mod.mariadb_dialect
        return driver_cls
    driver_cls = None.dialect
    return type('MariaDBDialect_%s' % driver, (MariaDBDialect, driver_cls), {
        'supports_statement_cache': True })
