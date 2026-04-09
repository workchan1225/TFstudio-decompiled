# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _py_processors.pyc (Python 3.11)

'''defines generic type conversion functions, as used in bind and result
processors.

They all share one common characteristic: None is passed through unchanged.

'''
from __future__ import annotations
import datetime
from datetime import date as date_cls
from datetime import datetime as datetime_cls
from datetime import time as time_cls
from decimal import Decimal
import typing
from typing import Any
from typing import Callable
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import Union
_DT = TypeVar('_DT', bound = Union[(datetime.datetime, datetime.time, datetime.date)])

def str_to_datetime_processor_factory(regexp = None, type_ = None):
    pass
# WARNING: Decompyle incomplete


def to_decimal_processor_factory(target_class = None, scale = None):
    pass
# WARNING: Decompyle incomplete


def to_float(value = None):
    pass
# WARNING: Decompyle incomplete


def to_str(value = None):
    pass
# WARNING: Decompyle incomplete


def int_to_boolean(value = None):
    pass
# WARNING: Decompyle incomplete


def str_to_datetime(value = None):
    pass
# WARNING: Decompyle incomplete


def str_to_time(value = None):
    pass
# WARNING: Decompyle incomplete


def str_to_date(value = None):
    pass
# WARNING: Decompyle incomplete
