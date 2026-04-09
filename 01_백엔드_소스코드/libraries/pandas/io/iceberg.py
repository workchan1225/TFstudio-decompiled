# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: iceberg.pyc (Python 3.11)

from typing import Any
from pandas.compat._optional import import_optional_dependency
from pandas.util._decorators import set_module
from pandas import DataFrame
read_iceberg = (lambda table_identifier = None, catalog_name = None, *, catalog_properties, columns: pyiceberg_catalog = import_optional_dependency('pyiceberg.catalog')pyiceberg_expressions = import_optional_dependency('pyiceberg.expressions')# WARNING: Decompyle incomplete
)()

def to_iceberg(df = None, table_identifier = None, catalog_name = None, *, catalog_properties, location, append, snapshot_properties):
    '''
    Write a DataFrame to an Apache Iceberg table.

    .. versionadded:: 3.0.0

    Parameters
    ----------
    table_identifier : str
        Table identifier.
    catalog_name : str, optional
        The name of the catalog.
    catalog_properties : dict of {str: str}, optional
        The properties that are used next to the catalog configuration.
    location : str, optional
        Location for the table.
    append : bool, default False
        If ``True``, append data to the table, instead of replacing the content.
    snapshot_properties : dict of {str: str}, optional
        Custom properties to be added to the snapshot summary

    See Also
    --------
    read_iceberg : Read an Apache Iceberg table.
    DataFrame.to_parquet : Write a DataFrame in Parquet format.
    '''
    pa = import_optional_dependency('pyarrow')
    pyiceberg_catalog = import_optional_dependency('pyiceberg.catalog')
# WARNING: Decompyle incomplete
