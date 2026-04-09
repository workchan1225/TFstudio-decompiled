# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ranges.pyc (Python 3.11)

from __future__ import annotations
import dataclasses
from datetime import date
from datetime import datetime
from datetime import timedelta
from decimal import Decimal
from typing import Any
from typing import cast
from typing import Generic
from typing import List
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from operators import ADJACENT_TO
from operators import CONTAINED_BY
from operators import CONTAINS
from operators import NOT_EXTEND_LEFT_OF
from operators import NOT_EXTEND_RIGHT_OF
from operators import OVERLAP
from operators import STRICTLY_LEFT_OF
from operators import STRICTLY_RIGHT_OF
from  import types as sqltypes
from sql import operators
from sql.type_api import TypeEngine
from util import py310
from util.typing import Literal
if TYPE_CHECKING:
    from sql.elements import ColumnElement
    from sql.type_api import _TE
    from sql.type_api import TypeEngineMixin
_T = TypeVar('_T', bound = Any)
_BoundsType = Literal[('()', '[)', '(]', '[]')]
if py310:
    dc_slots = {
        'slots': True }
    dc_kwonly = {
        'kw_only': True }
else:
    dc_slots = { }
    dc_kwonly = { }
# WARNING: Decompyle incomplete
