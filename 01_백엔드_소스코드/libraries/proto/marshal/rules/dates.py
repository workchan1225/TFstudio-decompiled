# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dates.pyc (Python 3.11)

from datetime import datetime
from datetime import timedelta
from datetime import timezone
from google.protobuf import duration_pb2
from google.protobuf import timestamp_pb2
from proto import datetime_helpers, utils

class TimestampRule:
    '''A marshal between Python datetimes and protobuf timestamps.

    Note: Python datetimes are less precise than protobuf datetimes
    (microsecond vs. nanosecond level precision). If nanosecond-level
    precision matters, it is recommended to interact with the internal
    proto directly.
    '''
    
    def to_python(self = None, value = None, *, absent):
        if isinstance(value, timestamp_pb2.Timestamp):
            if absent:
                return None
            return None.DatetimeWithNanoseconds.from_timestamp_pb(value)

    
    def to_proto(self = None, value = None):
        if isinstance(value, datetime_helpers.DatetimeWithNanoseconds):
            return value.timestamp_pb()
        if None(value, datetime):
            return timestamp_pb2.Timestamp(seconds = int(value.timestamp()), nanos = value.microsecond * 1000)
        if None(value, str):
            timestamp_value = timestamp_pb2.Timestamp()
            timestamp_value.FromJsonString(value = value)
            return timestamp_value



class DurationRule:
    '''A marshal between Python timedeltas and protobuf durations.

    Note: Python timedeltas are less precise than protobuf durations
    (microsecond vs. nanosecond level precision). If nanosecond-level
    precision matters, it is recommended to interact with the internal
    proto directly.
    '''
    
    def to_python(self = None, value = None, *, absent):
        if isinstance(value, duration_pb2.Duration):
            return timedelta(days = value.seconds // 86400, seconds = value.seconds % 86400, microseconds = value.nanos // 1000)

    
    def to_proto(self = None, value = None):
        if isinstance(value, timedelta):
            return duration_pb2.Duration(seconds = value.days * 86400 + value.seconds, nanos = value.microseconds * 1000)
        if None(value, str):
            duration_value = duration_pb2.Duration()
            duration_value.FromJsonString(value = value)
            return duration_value
