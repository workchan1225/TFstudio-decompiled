# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: core_schema.pyc (Python 3.11)

__doc__ = '\nThis module contains definitions to build schemas which `pydantic_core` can\nvalidate and serialize.\n'
from __future__ import annotations as _annotations
import sys
import warnings
from collections.abc import Hashable, Mapping
from datetime import date, datetime, time, timedelta
from decimal import Decimal
from re import Pattern
from typing import TYPE_CHECKING, Any, Callable, Literal, Union
from typing_extensions import TypeVar, deprecated
if sys.version_info < (3, 12):
    from typing_extensions import TypedDict
else:
    from typing import TypedDict
if sys.version_info < (3, 11):
    from typing_extensions import Protocol, Required, TypeAlias
else:
    from typing import Protocol, Required, TypeAlias
if TYPE_CHECKING:
    from pydantic_core import PydanticUndefined
# WARNING: Decompyle incomplete
