# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pipeline.pyc (Python 3.11)

__doc__ = "Experimental pipeline API functionality. Be careful with this API, it's subject to change."
from __future__ import annotations
import datetime
import operator
import re
import sys
from collections import deque
from collections.abc import Container
from dataclasses import dataclass
from decimal import Decimal
from functools import cached_property, partial
from re import Pattern
from typing import TYPE_CHECKING, Annotated, Any, Callable, Generic, Protocol, TypeVar, Union, overload
import annotated_types
if TYPE_CHECKING:
    from pydantic import GetCoreSchemaHandler
from pydantic_core import PydanticCustomError
from pydantic_core import core_schema as cs
from pydantic import Strict
from pydantic._internal._internal_dataclass import slots_true as _slots_true
if sys.version_info < (3, 10):
    EllipsisType = type(Ellipsis)
else:
    from types import EllipsisType
__all__ = [
    'validate_as',
    'validate_as_deferred',
    'transform']
# WARNING: Decompyle incomplete
