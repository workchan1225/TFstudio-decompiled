# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: datetime_helpers.pyc (Python 3.11)

'''Helpers for :mod:`datetime`.'''
import calendar
import datetime
import re
from google.protobuf import timestamp_pb2
_UTC_EPOCH = datetime.datetime.fromtimestamp(0, datetime.timezone.utc)
_RFC3339_MICROS = '%Y-%m-%dT%H:%M:%S.%fZ'
_RFC3339_NO_FRACTION = '%Y-%m-%dT%H:%M:%S'
_RFC3339_NANOS = re.compile('\n    (?P<no_fraction>\n        \\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}  # YYYY-MM-DDTHH:MM:SS\n    )\n    (                                        # Optional decimal part\n     \\.                                      # decimal point\n     (?P<nanos>\\d{1,9})                      # nanoseconds, maybe truncated\n    )?\n    Z                                        # Zulu\n', re.VERBOSE)

def _from_microseconds(value):
    '''Convert timestamp in microseconds since the unix epoch to datetime.

    Args:
        value (float): The timestamp to convert, in microseconds.

    Returns:
        datetime.datetime: The datetime object equivalent to the timestamp in
            UTC.
    '''
    return _UTC_EPOCH + datetime.timedelta(microseconds = value)


def _to_rfc3339(value, ignore_zone = (True,)):
    '''Convert a datetime to an RFC3339 timestamp string.

    Args:
        value (datetime.datetime):
            The datetime object to be converted to a string.
        ignore_zone (bool): If True, then the timezone (if any) of the
            datetime object is ignored and the datetime is treated as UTC.

    Returns:
        str: The RFC3339 formatted string representing the datetime.
    '''
    pass
# WARNING: Decompyle incomplete


class DatetimeWithNanoseconds(datetime.datetime):
    pass
# WARNING: Decompyle incomplete
