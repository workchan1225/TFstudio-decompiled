# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: enumerated.pyc (Python 3.11)

from __future__ import annotations
import enum
import re
from typing import Any
from typing import Dict
from typing import Optional
from typing import Set
from typing import Type
from typing import TYPE_CHECKING
from typing import Union
from types import _StringType
from  import exc
from  import sql
from  import util
from sql import sqltypes
from sql import type_api
if TYPE_CHECKING:
    from engine.interfaces import Dialect
    from sql.elements import ColumnElement
    from sql.type_api import _BindProcessorType
    from sql.type_api import _ResultProcessorType
    from sql.type_api import TypeEngine
    from sql.type_api import TypeEngineMixin

class ENUM(_StringType, sqltypes.Enum, type_api.NativeForEmulated):
    pass
# WARNING: Decompyle incomplete


class SET(_StringType):
    pass
# WARNING: Decompyle incomplete
