# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pyodbc.pyc (Python 3.11)

from __future__ import annotations
import re
import typing
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union
from urllib.parse import unquote_plus
from  import Connector
from  import ExecutionContext
from  import pool
from  import util
from engine import ConnectArgsType
from engine import Connection
from engine import interfaces
from engine import URL
from sql.type_api import TypeEngine
if typing.TYPE_CHECKING:
    from engine.interfaces import DBAPIModule
    from engine.interfaces import IsolationLevel

class PyODBCConnector(Connector):
    pass
# WARNING: Decompyle incomplete
