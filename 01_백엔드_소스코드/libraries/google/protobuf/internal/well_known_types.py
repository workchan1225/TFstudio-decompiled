# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: well_known_types.pyc (Python 3.11)

'''Contains well known classes.

This files defines well known classes which need extra maintenance including:
  - Any
  - Duration
  - FieldMask
  - Struct
  - Timestamp
'''
__author__ = 'jieluo@google.com (Jie Luo)'
import calendar
import collections.abc as collections
import datetime
from google.protobuf.internal import field_mask
FieldMask = field_mask.FieldMask
_TIMESTAMPFOMAT = '%Y-%m-%dT%H:%M:%S'
_NANOS_PER_SECOND = 1000000000
_NANOS_PER_MILLISECOND = 1000000
_NANOS_PER_MICROSECOND = 1000
_MILLIS_PER_SECOND = 1000
_MICROS_PER_SECOND = 1000000
_SECONDS_PER_DAY = 86400
_DURATION_SECONDS_MAX = 0x4979CB9E00
_EPOCH_DATETIME_NAIVE = datetime.datetime(1970, 1, 1, tzinfo = None)
_EPOCH_DATETIME_AWARE = _EPOCH_DATETIME_NAIVE.replace(tzinfo = datetime.timezone.utc)

class Any(object):
    '''Class for Any Message type.'''
    __slots__ = ()
    
    def Pack(self, msg, type_url_prefix, deterministic = ('type.googleapis.com/', None)):
        '''Packs the specified message into current Any message.'''
        if len(type_url_prefix) < 1 or type_url_prefix[-1] != '/':
            self.type_url = f'''{type_url_prefix!s}/{msg.DESCRIPTOR.full_name!s}'''
        else:
            self.type_url = f'''{type_url_prefix!s}{msg.DESCRIPTOR.full_name!s}'''
        self.value = msg.SerializeToString(deterministic = deterministic)

    
    def Unpack(self, msg):
        '''Unpacks the current Any message into specified message.'''
        descriptor = msg.DESCRIPTOR
        if not self.Is(descriptor):
            return False
        None.ParseFromString(self.value)
        return True

    
    def TypeName(self):
        '''Returns the protobuf type name of the inner message.'''
        return self.type_url.split('/')[-1]

    
    def Is(self, descriptor):
        '''Checks if this Any represents the given protobuf type.'''
        if '/' in self.type_url:
            pass
        return self.TypeName() == descriptor.full_name



class Timestamp(object):
    '''Class for Timestamp message type.'''
    __slots__ = ()
    
    def ToJsonString(self):
        """Converts Timestamp to RFC 3339 date string format.

    Returns:
      A string converted from timestamp. The string is always Z-normalized
      and uses 3, 6 or 9 fractional digits as required to represent the
      exact time. Example of the return format: '1972-01-01T10:00:20.021Z'
    """
        nanos = self.nanos % _NANOS_PER_SECOND
        total_sec = self.seconds + (self.nanos - nanos) // _NANOS_PER_SECOND
        seconds = total_sec % _SECONDS_PER_DAY
        days = (total_sec - seconds) // _SECONDS_PER_DAY
        dt = datetime.datetime(1970, 1, 1) + datetime.timedelta(days, seconds)
        result = dt.isoformat()
        if nanos % 1e+09 == 0:
            return result + 'Z'
        if None % 1e+06 == 0:
            return result + '.%03dZ' % nanos / 1e+06
        if None % 1000 == 0:
            return result + '.%06dZ' % nanos / 1000
        return None + '.%09dZ' % nanos

    
    def FromJsonString(self, value):
        """Parse a RFC 3339 date string format to Timestamp.

    Args:
      value: A date string. Any fractional digits (or none) and any offset are
          accepted as long as they fit into nano-seconds precision.
          Example of accepted format: '1972-01-01T10:00:20.021-05:00'

    Raises:
      ValueError: On parsing problems.
    """
        if not isinstance(value, str):
            raise ValueError('Timestamp JSON value not a string: {!r}'.format(value))
        timezone_offset = value.find('Z')
        if timezone_offset == -1:
            timezone_offset = value.find('+')
        if timezone_offset == -1:
            timezone_offset = value.rfind('-')
        if timezone_offset == -1:
            raise ValueError('Failed to parse timestamp: missing valid timezone offset.')
        time_value = value[0:timezone_offset]
        point_position = time_value.find('.')
        if point_position == -1:
            second_value = time_value
            nano_value = ''
        else:
            second_value = time_value[:point_position]
            nano_value = time_value[point_position + 1:]
        if 't' in second_value:
            raise ValueError("time data '{0}' does not match format '%Y-%m-%dT%H:%M:%S', lowercase 't' is not accepted".format(second_value))
        date_object = datetime.datetime.strptime(second_value, _TIMESTAMPFOMAT)
        td = date_object - datetime.datetime(1970, 1, 1)
        seconds = td.seconds + td.days * _SECONDS_PER_DAY
        if len(nano_value) > 9:
            raise ValueError('Failed to parse Timestamp: nanos {0} more than 9 fractional digits.'.format(nano_value))
        if nano_value:
            nanos = round(float('0.' + nano_value) * 1e+09)
        else:
            nanos = 0
        if value[timezone_offset] == 'Z':
            if len(value) != timezone_offset + 1:
                raise ValueError('Failed to parse timestamp: invalid trailing data {0}.'.format(value))
        else:
            timezone = value[timezone_offset:]
            pos = timezone.find(':')
            if pos == -1:
                raise ValueError('Invalid timezone offset value: {0}.'.format(timezone))
            if timezone[0] == '+':
                seconds -= (int(timezone[1:pos]) * 60 + int(timezone[pos + 1:])) * 60
            else:
                seconds += (int(timezone[1:pos]) * 60 + int(timezone[pos + 1:])) * 60
        self.seconds = int(seconds)
        self.nanos = int(nanos)

    
    def GetCurrentTime(self):
        '''Get the current UTC into Timestamp.'''
        self.FromDatetime(datetime.datetime.utcnow())

    
    def ToNanoseconds(self):
        '''Converts Timestamp to nanoseconds since epoch.'''
        return self.seconds * _NANOS_PER_SECOND + self.nanos

    
    def ToMicroseconds(self):
        '''Converts Timestamp to microseconds since epoch.'''
        return self.seconds * _MICROS_PER_SECOND + self.nanos // _NANOS_PER_MICROSECOND

    
    def ToMilliseconds(self):
        '''Converts Timestamp to milliseconds since epoch.'''
        return self.seconds * _MILLIS_PER_SECOND + self.nanos // _NANOS_PER_MILLISECOND

    
    def ToSeconds(self):
        '''Converts Timestamp to seconds since epoch.'''
        return self.seconds

    
    def FromNanoseconds(self, nanos):
        '''Converts nanoseconds since epoch to Timestamp.'''
        self.seconds = nanos // _NANOS_PER_SECOND
        self.nanos = nanos % _NANOS_PER_SECOND

    
    def FromMicroseconds(self, micros):
        '''Converts microseconds since epoch to Timestamp.'''
        self.seconds = micros // _MICROS_PER_SECOND
        self.nanos = (micros % _MICROS_PER_SECOND) * _NANOS_PER_MICROSECOND

    
    def FromMilliseconds(self, millis):
        '''Converts milliseconds since epoch to Timestamp.'''
        self.seconds = millis // _MILLIS_PER_SECOND
        self.nanos = (millis % _MILLIS_PER_SECOND) * _NANOS_PER_MILLISECOND

    
    def FromSeconds(self, seconds):
        '''Converts seconds since epoch to Timestamp.'''
        self.seconds = seconds
        self.nanos = 0

    
    def ToDatetime(self, tzinfo = (None,)):
        """Converts Timestamp to a datetime.

    Args:
      tzinfo: A datetime.tzinfo subclass; defaults to None.

    Returns:
      If tzinfo is None, returns a timezone-naive UTC datetime (with no timezone
      information, i.e. not aware that it's UTC).

      Otherwise, returns a timezone-aware datetime in the input timezone.
    """
        delta = datetime.timedelta(seconds = self.seconds, microseconds = _RoundTowardZero(self.nanos, _NANOS_PER_MICROSECOND))
    # WARNING: Decompyle incomplete

    
    def FromDatetime(self, dt):
        """Converts datetime to Timestamp.

    Args:
      dt: A datetime. If it's timezone-naive, it's assumed to be in UTC.
    """
        self.seconds = calendar.timegm(dt.utctimetuple())
        self.nanos = dt.microsecond * _NANOS_PER_MICROSECOND



class Duration(object):
    '''Class for Duration message type.'''
    __slots__ = ()
    
    def ToJsonString(self):
        '''Converts Duration to string format.

    Returns:
      A string converted from self. The string format will contains
      3, 6, or 9 fractional digits depending on the precision required to
      represent the exact Duration value. For example: "1s", "1.010s",
      "1.000000100s", "-3.100s"
    '''
        _CheckDurationValid(self.seconds, self.nanos)
        if self.seconds < 0 or self.nanos < 0:
            result = '-'
            seconds = -(self.seconds) + int((0 - self.nanos) // 1e+09)
            nanos = (0 - self.nanos) % 1e+09
        else:
            result = ''
            seconds = self.seconds + int(self.nanos // 1e+09)
            nanos = self.nanos % 1e+09
        result += '%d' % seconds
        if nanos % 1e+09 == 0:
            return result + 's'
        if None % 1e+06 == 0:
            return result + '.%03ds' % nanos / 1e+06
        if None % 1000 == 0:
            return result + '.%06ds' % nanos / 1000
        return None + '.%09ds' % nanos

    
    def FromJsonString(self, value):
        '''Converts a string to Duration.

    Args:
      value: A string to be converted. The string must end with \'s\'. Any
          fractional digits (or none) are accepted as long as they fit into
          precision. For example: "1s", "1.01s", "1.0000001s", "-3.100s

    Raises:
      ValueError: On parsing problems.
    '''
        if not isinstance(value, str):
            raise ValueError('Duration JSON value not a string: {!r}'.format(value))
        if len(value) < 1 or value[-1] != 's':
            raise ValueError('Duration must end with letter "s": {0}.'.format(value))
        
        try:
            pos = value.find('.')
            if pos == -1:
                seconds = int(value[:-1])
                nanos = 0
            else:
                seconds = int(value[:pos])
                if value[0] == '-':
                    nanos = int(round(float('-0{0}'.format(value[pos:-1])) * 1e+09))
                else:
                    nanos = int(round(float('0{0}'.format(value[pos:-1])) * 1e+09))
            _CheckDurationValid(seconds, nanos)
            self.seconds = seconds
            self.nanos = nanos
            return None
        except ValueError:
            e = None
            raise ValueError("Couldn't parse duration: {0} : {1}.".format(value, e))
            e = None
            del e


    
    def ToNanoseconds(self):
        '''Converts a Duration to nanoseconds.'''
        return self.seconds * _NANOS_PER_SECOND + self.nanos

    
    def ToMicroseconds(self):
        '''Converts a Duration to microseconds.'''
        micros = _RoundTowardZero(self.nanos, _NANOS_PER_MICROSECOND)
        return self.seconds * _MICROS_PER_SECOND + micros

    
    def ToMilliseconds(self):
        '''Converts a Duration to milliseconds.'''
        millis = _RoundTowardZero(self.nanos, _NANOS_PER_MILLISECOND)
        return self.seconds * _MILLIS_PER_SECOND + millis

    
    def ToSeconds(self):
        '''Converts a Duration to seconds.'''
        return self.seconds

    
    def FromNanoseconds(self, nanos):
        '''Converts nanoseconds to Duration.'''
        self._NormalizeDuration(nanos // _NANOS_PER_SECOND, nanos % _NANOS_PER_SECOND)

    
    def FromMicroseconds(self, micros):
        '''Converts microseconds to Duration.'''
        self._NormalizeDuration(micros // _MICROS_PER_SECOND, (micros % _MICROS_PER_SECOND) * _NANOS_PER_MICROSECOND)

    
    def FromMilliseconds(self, millis):
        '''Converts milliseconds to Duration.'''
        self._NormalizeDuration(millis // _MILLIS_PER_SECOND, (millis % _MILLIS_PER_SECOND) * _NANOS_PER_MILLISECOND)

    
    def FromSeconds(self, seconds):
        '''Converts seconds to Duration.'''
        self.seconds = seconds
        self.nanos = 0

    
    def ToTimedelta(self):
        '''Converts Duration to timedelta.'''
        return datetime.timedelta(seconds = self.seconds, microseconds = _RoundTowardZero(self.nanos, _NANOS_PER_MICROSECOND))

    
    def FromTimedelta(self, td):
        '''Converts timedelta to Duration.'''
        self._NormalizeDuration(td.seconds + td.days * _SECONDS_PER_DAY, td.microseconds * _NANOS_PER_MICROSECOND)

    
    def _NormalizeDuration(self, seconds, nanos):
        '''Set Duration by seconds and nanos.'''
        if seconds < 0 and nanos > 0:
            seconds += 1
            nanos -= _NANOS_PER_SECOND
        self.seconds = seconds
        self.nanos = nanos



def _CheckDurationValid(seconds, nanos):
    if seconds < -_DURATION_SECONDS_MAX or seconds > _DURATION_SECONDS_MAX:
        raise ValueError('Duration is not valid: Seconds {0} must be in range [-315576000000, 315576000000].'.format(seconds))
    if nanos <= -_NANOS_PER_SECOND or nanos >= _NANOS_PER_SECOND:
        raise ValueError('Duration is not valid: Nanos {0} must be in range [-999999999, 999999999].'.format(nanos))
    if nanos < 0 or seconds > 0 or nanos > 0 or seconds < 0:
        raise ValueError('Duration is not valid: Sign mismatch.')
    return None


def _RoundTowardZero(value, divider):
    '''Truncates the remainder part after division.'''
    result = value // divider
    remainder = value % divider
    if result < 0 and remainder > 0:
        return result + 1


def _SetStructValue(struct_value, value):
    pass
# WARNING: Decompyle incomplete


def _GetStructValue(struct_value):
    which = struct_value.WhichOneof('kind')
    if which == 'struct_value':
        return struct_value.struct_value
    if None == 'null_value':
        return None
    if None == 'number_value':
        return struct_value.number_value
    if None == 'string_value':
        return struct_value.string_value
    if None == 'bool_value':
        return struct_value.bool_value
    if None == 'list_value':
        return struct_value.list_value
# WARNING: Decompyle incomplete


class Struct(object):
    '''Class for Struct message type.'''
    __slots__ = ()
    
    def __getitem__(self, key):
        return _GetStructValue(self.fields[key])

    
    def __contains__(self, item):
        return item in self.fields

    
    def __setitem__(self, key, value):
        _SetStructValue(self.fields[key], value)

    
    def __delitem__(self, key):
        del self.fields[key]

    
    def __len__(self):
        return len(self.fields)

    
    def __iter__(self):
        return iter(self.fields)

    
    def keys(self):
        return self.fields.keys()

    
    def values(self):
        pass
    # WARNING: Decompyle incomplete

    
    def items(self):
        pass
    # WARNING: Decompyle incomplete

    
    def get_or_create_list(self, key):
        """Returns a list for this key, creating if it didn't exist already."""
        if not self.fields[key].HasField('list_value'):
            self.fields[key].list_value.Clear()
        return self.fields[key].list_value

    
    def get_or_create_struct(self, key):
        """Returns a struct for this key, creating if it didn't exist already."""
        if not self.fields[key].HasField('struct_value'):
            self.fields[key].struct_value.Clear()
        return self.fields[key].struct_value

    
    def update(self, dictionary):
        for key, value in dictionary.items():
            _SetStructValue(self.fields[key], value)
            return None


collections.abc.MutableMapping.register(Struct)

class ListValue(object):
    '''Class for ListValue message type.'''
    __slots__ = ()
    
    def __len__(self):
        return len(self.values)

    
    def append(self, value):
        _SetStructValue(self.values.add(), value)

    
    def extend(self, elem_seq):
        for value in elem_seq:
            self.append(value)
            return None

    
    def __getitem__(self, index):
        '''Retrieves item by the specified index.'''
        return _GetStructValue(self.values.__getitem__(index))

    
    def __setitem__(self, index, value):
        _SetStructValue(self.values.__getitem__(index), value)

    
    def __delitem__(self, key):
        del self.values[key]

    
    def items(self):
        pass
    # WARNING: Decompyle incomplete

    
    def add_struct(self):
        '''Appends and returns a struct value as the next value in the list.'''
        struct_value = self.values.add().struct_value
        struct_value.Clear()
        return struct_value

    
    def add_list(self):
        '''Appends and returns a list value as the next value in the list.'''
        list_value = self.values.add().list_value
        list_value.Clear()
        return list_value


collections.abc.MutableSequence.register(ListValue)
WKTBASES = {
    'google.protobuf.Any': Any,
    'google.protobuf.Duration': Duration,
    'google.protobuf.FieldMask': FieldMask,
    'google.protobuf.ListValue': ListValue,
    'google.protobuf.Struct': Struct,
    'google.protobuf.Timestamp': Timestamp }
