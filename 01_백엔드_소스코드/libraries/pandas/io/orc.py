# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: orc.pyc (Python 3.11)

'''orc compat'''
from __future__ import annotations
import io
from typing import TYPE_CHECKING, Any, Literal
from pandas._libs import lib
from pandas.compat._optional import import_optional_dependency
from pandas.util._decorators import set_module
from pandas.util._validators import check_dtype_backend
from pandas.core.indexes.api import default_index
from pandas.io._util import arrow_table_to_pandas
from pandas.io.common import get_handle, is_fsspec_url
if TYPE_CHECKING:
    import fsspec
    import pyarrow.fs as pyarrow
    from pandas._typing import DtypeBackend, FilePath, ReadBuffer, WriteBuffer
    from pandas.core.frame import DataFrame
read_orc = (lambda path = None, columns = None, dtype_backend = set_module('pandas'), filesystem = (None, lib.no_default, None): orc = import_optional_dependency('pyarrow.orc')check_dtype_backend(dtype_backend)handles = get_handle(path, 'rb', is_text = False)source = handles.handle# WARNING: Decompyle incomplete
)()

def to_orc(df = None, path = None, *, engine, index, engine_kwargs):
    """
    Write a DataFrame to the ORC format.

    Parameters
    ----------
    df : DataFrame
        The dataframe to be written to ORC. Raises NotImplementedError
        if dtype of one or more columns is category, unsigned integers,
        intervals, periods or sparse.
    path : str, file-like object or None, default None
        If a string, it will be used as Root Directory path
        when writing a partitioned dataset. By file-like object,
        we refer to objects with a write() method, such as a file handle
        (e.g. via builtin open function). If path is None,
        a bytes object is returned.
    engine : str, default 'pyarrow'
        ORC library to use.
    index : bool, optional
        If ``True``, include the dataframe's index(es) in the file output. If
        ``False``, they will not be written to the file.
        If ``None``, similar to ``infer`` the dataframe's index(es)
        will be saved. However, instead of being saved as values,
        the RangeIndex will be stored as a range in the metadata so it
        doesn't require much space and is faster. Other indexes will
        be included as columns in the file output.
    engine_kwargs : dict[str, Any] or None, default None
        Additional keyword arguments passed to :func:`pyarrow.orc.write_table`.

    Returns
    -------
    bytes if no path argument is provided else None

    Raises
    ------
    NotImplementedError
        Dtype of one or more columns is category, unsigned integers, interval,
        period or sparse.
    ValueError
        engine is not pyarrow.

    Notes
    -----
    * Before using this function you should read the
      :ref:`user guide about ORC <io.orc>` and
      :ref:`install optional dependencies <install.warn_orc>`.
    * This function requires `pyarrow <https://arrow.apache.org/docs/python/>`_
      library.
    * For supported dtypes please refer to `supported ORC features in Arrow
      <https://arrow.apache.org/docs/cpp/orc.html#data-types>`__.
    * Currently timezones in datetime columns are not preserved when a
      dataframe is converted into ORC files.
    """
    pass
# WARNING: Decompyle incomplete
