# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: datetime_helpers.pyc (Python 3.11)

'''Helpers for :mod:`datetime`.'''
import calendar
import datetime
import re
from google.protobuf import timestamp_pb2
_UTC_EPOCH = datetime.datetime(1970, 1, 1, tzinfo = datetime.timezone.utc)
_RFC3339_MICROS = '%Y-%m-%dT%H:%M:%S.%fZ'
_RFC3339_NO_FRACTION = '%Y-%m-%dT%H:%M:%S'
_RFC3339_NANOS = re.compile('\n    (?P<no_fraction>\n        \\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}  # YYYY-MM-DDTHH:MM:SS\n    )\n    (                                        # Optional decimal part\n     \\.                                      # decimal point\n     (?P<nanos>\\d{1,9})                      # nanoseconds, maybe truncated\n    )?\n    Z                                        # Zulu\n', re.VERBOSE)

def utcnow():
    '''A :meth:`datetime.datetime.utcnow()` alias to allow mocking in tests.'''
    return datetime.datetime.now(tz = datetime.timezone.utc).replace(tzinfo = None)


def to_milliseconds(value):
    '''Convert a zone-aware datetime to milliseconds since the unix epoch.

    Args:
        value (datetime.datetime): The datetime to covert.

    Returns:
        int: Milliseconds since the unix epoch.
    '''
    micros = to_microseconds(value)
    return micros // 1000


def from_microseconds(value):
    '''Convert timestamp in microseconds since the unix epoch to datetime.

    Args:
        value (float): The timestamp to convert, in microseconds.

    Returns:
        datetime.datetime: The datetime object equivalent to the timestamp in
            UTC.
    '''
    return _UTC_EPOCH + datetime.timedelta(microseconds = value)


def to_microseconds(value):
    '''Convert a datetime to microseconds since the unix epoch.

    Args:
        value (datetime.datetime): The datetime to covert.

    Returns:
        int: Microseconds since the unix epoch.
    '''
    if not value.tzinfo:
        value = value.replace(tzinfo = datetime.timezone.utc)
    value = value.astimezone(datetime.timezone.utc)
    return int(calendar.timegm(value.timetuple()) * 1e+06) + value.microsecond


def from_iso8601_date(value):
    '''Convert a ISO8601 date string to a date.

    Args:
        value (str): The ISO8601 date string.

    Returns:
        datetime.date: A date equivalent to the date string.
    '''
    return datetime.datetime.strptime(value, '%Y-%m-%d').date()


def from_iso8601_time(value):
    '''Convert a zoneless ISO8601 time string to a time.

    Args:
        value (str): The ISO8601 time string.

    Returns:
        datetime.time: A time equivalent to the time string.
    '''
    return datetime.datetime.strptime(value, '%H:%M:%S').time()


def from_rfc3339(value):
    '''Convert an RFC3339-format timestamp to a native datetime.

    Supported formats include those without fractional seconds, or with
    any fraction up to nanosecond precision.

    .. note::
        Python datetimes do not support nanosecond precision; this function
        therefore truncates such values to microseconds.

    Args:
        value (str): The RFC3339 string to convert.

    Returns:
        datetime.datetime: The datetime object equivalent to the timestamp
        in UTC.

    Raises:
        ValueError: If the timestamp does not match the RFC3339
            regular expression.
    '''
    with_nanos = _RFC3339_NANOS.match(value)
# WARNING: Decompyle incomplete

from_rfc3339_nanos = from_rfc3339

def to_rfc3339(value, ignore_zone = (True,)):
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
    '''Track nanosecond in addition to normal datetime attrs.

    Nanosecond can be passed only as a keyword argument.
    '''
    __slots__ = ('_nanosecond',)
    
    def __new__(cls, *args, **kw):
        nanos = kw.pop('nanosecond', 0)
        if nanos > 0:
            if 'microsecond' in kw:
                raise TypeError("Specify only one of 'microsecond' or 'nanosecond'")
            kw['microsecond'] = nanos // 1000
    # WARNING: Decompyle incomplete

    nanosecond = (lambda self: self._nanosecond)()
    
    def rfc3339(self):
        '''Return an RFC3339-compliant timestamp.

        Returns:
            (str): Timestamp string according to RFC3339 spec.
        '''
        if self._nanosecond == 0:
            return to_rfc3339(self)
        nanos = None(self._nanosecond).rjust(9, '0').rstrip('0')
        return '{}.{}Z'.format(self.strftime(_RFC3339_NO_FRACTION), nanos)

    from_rfc3339 = (lambda cls, stamp: with_nanos = _RFC3339_NANOS.match(stamp)# WARNING: Decompyle incomplete
)()
    
    def timestamp_pb(self):
        '''Return a timestamp message.

        Returns:
            (:class:`~google.protobuf.timestamp_pb2.Timestamp`): Timestamp message
        '''
        pass
    # WARNING: Decompyle incomplete

    from_timestamp_pb = (lambda cls, stamp: microseconds = int(stamp.seconds * 1e+06)bare = from_microseconds(microseconds)cls(bare.year, bare.month, bare.day, bare.hour, bare.minute, bare.second, nanosecond = stamp.nanos, tzinfo = datetime.timezone.utc))()
