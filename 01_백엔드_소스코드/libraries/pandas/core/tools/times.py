# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: times.pyc (Python 3.11)

from __future__ import annotations
from datetime import datetime, time
from typing import TYPE_CHECKING
import numpy as np
from pandas._libs.lib import is_list_like
from pandas.core.dtypes.generic import ABCIndex, ABCSeries
from pandas.core.dtypes.missing import notna
if TYPE_CHECKING:
    from pandas._typing import DateTimeErrorChoices

def to_time(arg = None, format = None, infer_time_format = None, errors = (None, False, 'raise')):
    '''
    Parse time strings to time objects using fixed strptime formats ("%H:%M",
    "%H%M", "%I:%M%p", "%I%M%p", "%H:%M:%S", "%H%M%S", "%I:%M:%S%p",
    "%I%M%S%p")

    Use infer_time_format if all the strings are in the same format to speed
    up conversion.

    Parameters
    ----------
    arg : string in time format, datetime.time, list, tuple, 1-d array,  Series
    format : str, default None
        Format used to convert arg into a time object.  If None, fixed formats
        are used.
    infer_time_format: bool, default False
        Infer the time format based on the first non-NaN element.  If all
        strings are in the same format, this will speed up conversion.
    errors : {\'raise\', \'coerce\'}, default \'raise\'
        - If \'raise\', then invalid parsing will raise an exception
        - If \'coerce\', then invalid parsing will be set as None

    Returns
    -------
    datetime.time
    '''
    pass
# WARNING: Decompyle incomplete

_time_formats = [
    '%H:%M',
    '%H%M',
    '%I:%M%p',
    '%I%M%p',
    '%H:%M:%S',
    '%H%M%S',
    '%I:%M:%S%p',
    '%I%M%S%p']

def _guess_time_format_for_array(arr):
    non_nan_elements = notna(arr).nonzero()[0]
    if len(non_nan_elements):
        element = arr[non_nan_elements[0]]
        for time_format in _time_formats:
            datetime.strptime(element, time_format)
            
            return None, time_format
            except ValueError:
                continue
            return None
