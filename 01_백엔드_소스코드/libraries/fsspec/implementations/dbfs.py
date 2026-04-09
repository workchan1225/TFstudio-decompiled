# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dbfs.pyc (Python 3.11)

from __future__ import annotations
import base64
import urllib
import requests
from requests.adapters import HTTPAdapter, Retry
from typing_extensions import override
from fsspec import AbstractFileSystem
from fsspec.spec import AbstractBufferedFile

class DatabricksException(Exception):
    pass
# WARNING: Decompyle incomplete


class DatabricksFileSystem(AbstractFileSystem):
    pass
# WARNING: Decompyle incomplete


class DatabricksFile(AbstractBufferedFile):
    pass
# WARNING: Decompyle incomplete
