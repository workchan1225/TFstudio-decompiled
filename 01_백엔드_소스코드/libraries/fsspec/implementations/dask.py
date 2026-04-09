# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dask.pyc (Python 3.11)

import dask
from distributed.client import Client, _get_global_client
from distributed.worker import Worker
from fsspec import filesystem
from fsspec.spec import AbstractBufferedFile, AbstractFileSystem
from fsspec.utils import infer_storage_options

def _get_client(client):
    pass
# WARNING: Decompyle incomplete


def _in_worker():
    return bool(Worker._instances)


class DaskWorkerFileSystem(AbstractFileSystem):
    pass
# WARNING: Decompyle incomplete


class DaskFile(AbstractBufferedFile):
    pass
# WARNING: Decompyle incomplete
