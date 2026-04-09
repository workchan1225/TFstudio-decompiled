# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pymssql.pyc (Python 3.11)

"""
.. dialect:: mssql+pymssql
    :name: pymssql
    :dbapi: pymssql
    :connectstring: mssql+pymssql://<username>:<password>@<freetds_name>/?charset=utf8

pymssql is a Python module that provides a Python DBAPI interface around
`FreeTDS <https://www.freetds.org/>`_.

.. versionchanged:: 2.0.5

    pymssql was restored to SQLAlchemy's continuous integration testing


"""
import re
from base import MSDialect
from base import MSIdentifierPreparer
from  import types as sqltypes
from  import util
from engine import processors

class _MSNumeric_pymssql(sqltypes.Numeric):
    
    def result_processor(self, dialect, type_):
        if not self.asdecimal:
            return processors.to_float
        return None.Numeric.result_processor(self, dialect, type_)



class MSIdentifierPreparer_pymssql(MSIdentifierPreparer):
    pass
# WARNING: Decompyle incomplete


class MSDialect_pymssql(MSDialect):
    pass
# WARNING: Decompyle incomplete

dialect = MSDialect_pymssql
