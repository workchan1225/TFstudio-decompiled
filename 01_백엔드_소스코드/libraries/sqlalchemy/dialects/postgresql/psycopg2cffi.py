# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: psycopg2cffi.pyc (Python 3.11)

'''
.. dialect:: postgresql+psycopg2cffi
    :name: psycopg2cffi
    :dbapi: psycopg2cffi
    :connectstring: postgresql+psycopg2cffi://user:password@host:port/dbname[?key=value&key=value...]
    :url: https://pypi.org/project/psycopg2cffi/

``psycopg2cffi`` is an adaptation of ``psycopg2``, using CFFI for the C
layer. This makes it suitable for use in e.g. PyPy. Documentation
is as per ``psycopg2``.

.. seealso::

    :mod:`sqlalchemy.dialects.postgresql.psycopg2`

'''
from psycopg2 import PGDialect_psycopg2
from  import util

class PGDialect_psycopg2cffi(PGDialect_psycopg2):
    driver = 'psycopg2cffi'
    supports_unicode_statements = True
    supports_statement_cache = True
    FEATURE_VERSION_MAP = dict(native_json = (2, 4, 4), native_jsonb = (2, 7, 1), sane_multi_rowcount = (2, 4, 4), array_oid = (2, 4, 4), hstore_adapter = (2, 4, 4))
    import_dbapi = (lambda cls: __import__('psycopg2cffi'))()
    _psycopg2_extensions = (lambda cls: root = __import__('psycopg2cffi', fromlist = [
'extensions'])root.extensions)()
    _psycopg2_extras = (lambda cls: root = __import__('psycopg2cffi', fromlist = [
'extras'])root.extras)()

dialect = PGDialect_psycopg2cffi
