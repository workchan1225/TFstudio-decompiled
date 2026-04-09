# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: processors.pyc (Python 3.11)

'''defines generic type conversion functions, as used in bind and result
processors.

They all share one common characteristic: None is passed through unchanged.

'''
from __future__ import annotations
import typing
from _py_processors import str_to_datetime_processor_factory
from util._has_cy import HAS_CYEXTENSION
if not typing.TYPE_CHECKING or HAS_CYEXTENSION:
    from _py_processors import int_to_boolean
    from _py_processors import str_to_date
    from _py_processors import str_to_datetime
    from _py_processors import str_to_time
    from _py_processors import to_decimal_processor_factory
    from _py_processors import to_float
    from _py_processors import to_str
    return None
from sqlalchemy.cyextension.processors import DecimalResultProcessor
from sqlalchemy.cyextension.processors import int_to_boolean
from sqlalchemy.cyextension.processors import str_to_date
from sqlalchemy.cyextension.processors import str_to_datetime
from sqlalchemy.cyextension.processors import str_to_time
from sqlalchemy.cyextension.processors import to_float
from sqlalchemy.cyextension.processors import to_str

def to_decimal_processor_factory(target_class, scale):
    return DecimalResultProcessor(target_class, '%%.%df' % scale).process
