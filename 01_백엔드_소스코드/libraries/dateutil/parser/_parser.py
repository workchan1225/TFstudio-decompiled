# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _parser.pyc (Python 3.11)

'''
This module offers a generic date/time string parser which is able to parse
most known formats to represent a date and/or time.

This module attempts to be forgiving with regards to unlikely input formats,
returning a datetime object even for dates which are ambiguous. If an element
of a date/time stamp is omitted, the following rules are applied:

- If AM or PM is left unspecified, a 24-hour clock is assumed, however, an hour
  on a 12-hour clock (``0 <= hour <= 12``) *must* be specified if AM or PM is
  specified.
- If a time zone is omitted, a timezone-naive datetime is returned.

If any other elements are missing, they are taken from the
:class:`datetime.datetime` object passed to the parameter ``default``. If this
results in a day number exceeding the valid number of days per month, the
value falls back to the end of the month.

Additional resources about date/time string formats can be found below:

- `A summary of the international standard date and time notation
  <https://www.cl.cam.ac.uk/~mgk25/iso-time.html>`_
- `W3C Date and Time Formats <https://www.w3.org/TR/NOTE-datetime>`_
- `Time Formats (Planetary Rings Node) <https://pds-rings.seti.org:443/tools/time_formats.html>`_
- `CPAN ParseDate module
  <https://metacpan.org/pod/release/MUIR/Time-modules-2013.0912/lib/Time/ParseDate.pm>`_
- `Java SimpleDateFormat Class
  <https://docs.oracle.com/javase/6/docs/api/java/text/SimpleDateFormat.html>`_
'''
from __future__ import unicode_literals
import datetime
import re
import string
import time
import warnings
from calendar import monthrange
from io import StringIO
import six
from six import integer_types, text_type
from decimal import Decimal
from warnings import warn
from  import relativedelta
from  import tz
__all__ = [
    'parse',
    'parserinfo',
    'ParserError']

class _timelex(object):
    _split_decimal = re.compile('([.,])')
    
    def __init__(self, instream):
        if isinstance(instream, (bytes, bytearray)):
            instream = instream.decode()
        if isinstance(instream, text_type):
            instream = StringIO(instream)
    # WARNING: Decompyle incomplete

    
    def get_token(self):
        '''
        This function breaks the time string into lexical units (tokens), which
        can be parsed by the parser. Lexical units are demarcated by changes in
        the character set, so any continuous string of letters is considered
        one unit, any continuous string of numbers is considered one unit.

        The main complication arises from the fact that dots (\'.\') can be used
        both as separators (e.g. "Sep.20.2009") or decimal points (e.g.
        "4:30:21.447"). As such, it is necessary to read the full context of
        any dot-separated strings before breaking it into tokens; as such, this
        function maintains a "token stack", for when the ambiguous context
        demands that multiple tokens be parsed at once.
        '''
        if self.tokenstack:
            return self.tokenstack.pop(0)
        seenletters = None
        token = None
        state = None
    # WARNING: Decompyle incomplete

    
    def __iter__(self):
        return self

    
    def __next__(self):
        token = self.get_token()
    # WARNING: Decompyle incomplete

    
    def next(self):
        return self.__next__()

    split = (lambda cls, s: list(cls(s)))()
    isword = (lambda cls, nextchar: nextchar.isalpha())()
    isnum = (lambda cls, nextchar: nextchar.isdigit())()
    isspace = (lambda cls, nextchar: nextchar.isspace())()


class _resultbase(object):
    
    def __init__(self):
        for attr in self.__slots__:
            setattr(self, attr, None)
            return None

    
    def _repr(self, classname):
        l = []
    # WARNING: Decompyle incomplete

    
    def __len__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return self._repr(self.__class__.__name__)



class parserinfo(object):
    '''
    Class which handles what inputs are accepted. Subclass this to customize
    the language and acceptable values for each parameter.

    :param dayfirst:
        Whether to interpret the first value in an ambiguous 3-integer date
        (e.g. 01/05/09) as the day (``True``) or month (``False``). If
        ``yearfirst`` is set to ``True``, this distinguishes between YDM
        and YMD. Default is ``False``.

    :param yearfirst:
        Whether to interpret the first value in an ambiguous 3-integer date
        (e.g. 01/05/09) as the year. If ``True``, the first number is taken
        to be the year, otherwise the last number is taken to be the year.
        Default is ``False``.
    '''
    JUMP = [
        ' ',
        '.',
        ',',
        ';',
        '-',
        '/',
        "'",
        'at',
        'on',
        'and',
        'ad',
        'm',
        't',
        'of',
        'st',
        'nd',
        'rd',
        'th']
    WEEKDAYS = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday')]
    MONTHS = [
        ('Jan', 'January'),
        ('Feb', 'February'),
        ('Mar', 'March'),
        ('Apr', 'April'),
        ('May', 'May'),
        ('Jun', 'June'),
        ('Jul', 'July'),
        ('Aug', 'August'),
        ('Sep', 'Sept', 'September'),
        ('Oct', 'October'),
        ('Nov', 'November'),
        ('Dec', 'December')]
    HMS = [
        ('h', 'hour', 'hours'),
        ('m', 'minute', 'minutes'),
        ('s', 'second', 'seconds')]
    AMPM = [
        ('am', 'a'),
        ('pm', 'p')]
    UTCZONE = [
        'UTC',
        'GMT',
        'Z',
        'z']
    PERTAIN = [
        'of']
    TZOFFSET = { }
    
    def __init__(self, dayfirst, yearfirst = (False, False)):
        self._jump = self._convert(self.JUMP)
        self._weekdays = self._convert(self.WEEKDAYS)
        self._months = self._convert(self.MONTHS)
        self._hms = self._convert(self.HMS)
        self._ampm = self._convert(self.AMPM)
        self._utczone = self._convert(self.UTCZONE)
        self._pertain = self._convert(self.PERTAIN)
        self.dayfirst = dayfirst
        self.yearfirst = yearfirst
        self._year = time.localtime().tm_year
        self._century = (self._year // 100) * 100

    
    def _convert(self, lst):
        dct = { }
        for i, v in enumerate(lst):
            if isinstance(v, tuple):
                for v in v:
                    dct[v.lower()] = i
                    dct[v.lower()] = i
                    return dct

    
    def jump(self, name):
        return name.lower() in self._jump

    
    def weekday(self, name):
        
        try:
            return self._weekdays[name.lower()]
        except KeyError:
            pass


    
    def month(self, name):
        
        try:
            return self._months[name.lower()] + 1
        except KeyError:
            pass


    
    def hms(self, name):
        
        try:
            return self._hms[name.lower()]
        except KeyError:
            return None


    
    def ampm(self, name):
        
        try:
            return self._ampm[name.lower()]
        except KeyError:
            return None


    
    def pertain(self, name):
        return name.lower() in self._pertain

    
    def utczone(self, name):
        return name.lower() in self._utczone

    
    def tzoffset(self, name):
        if name in self._utczone:
            return 0
        return None.TZOFFSET.get(name)

    
    def convertyear(self, year, century_specified = (False,)):
        '''
        Converts two-digit years to year within [-50, 49]
        range of self._year (current local time)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def validate(self, res):
        pass
    # WARNING: Decompyle incomplete



class _ymd(list):
    pass
# WARNING: Decompyle incomplete


class parser(object):
    
    def __init__(self, info = (None,)):
        if not info:
            pass
        self.info = parserinfo()

    
    def parse(self, timestr, default, ignoretz, tzinfos = (None, False, None), **kwargs):
        '''
        Parse the date/time string into a :class:`datetime.datetime` object.

        :param timestr:
            Any date/time string using the supported formats.

        :param default:
            The default datetime object, if this is a datetime object and not
            ``None``, elements specified in ``timestr`` replace elements in the
            default object.

        :param ignoretz:
            If set ``True``, time zones in parsed strings are ignored and a
            naive :class:`datetime.datetime` object is returned.

        :param tzinfos:
            Additional time zone names / aliases which may be present in the
            string. This argument maps time zone names (and optionally offsets
            from those time zones) to time zones. This parameter can be a
            dictionary with timezone aliases mapping time zone names to time
            zones or a function taking two parameters (``tzname`` and
            ``tzoffset``) and returning a time zone.

            The timezones to which the names are mapped can be an integer
            offset from UTC in seconds or a :class:`tzinfo` object.

            .. doctest::
               :options: +NORMALIZE_WHITESPACE

                >>> from dateutil.parser import parse
                >>> from dateutil.tz import gettz
                >>> tzinfos = {"BRST": -7200, "CST": gettz("America/Chicago")}
                >>> parse("2012-01-19 17:21:00 BRST", tzinfos=tzinfos)
                datetime.datetime(2012, 1, 19, 17, 21, tzinfo=tzoffset(u\'BRST\', -7200))
                >>> parse("2012-01-19 17:21:00 CST", tzinfos=tzinfos)
                datetime.datetime(2012, 1, 19, 17, 21,
                                  tzinfo=tzfile(\'/usr/share/zoneinfo/America/Chicago\'))

            This parameter is ignored if ``ignoretz`` is set.

        :param \\*\\*kwargs:
            Keyword arguments as passed to ``_parse()``.

        :return:
            Returns a :class:`datetime.datetime` object or, if the
            ``fuzzy_with_tokens`` option is ``True``, returns a tuple, the
            first element being a :class:`datetime.datetime` object, the second
            a tuple containing the fuzzy tokens.

        :raises ParserError:
            Raised for invalid or unknown string format, if the provided
            :class:`tzinfo` is not in a valid format, or if an invalid date
            would be created.

        :raises TypeError:
            Raised for non-string or character stream input.

        :raises OverflowError:
            Raised if the parsed date exceeds the largest valid C integer on
            your system.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    class _result(_resultbase):
        __slots__ = [
            'year',
            'month',
            'day',
            'weekday',
            'hour',
            'minute',
            'second',
            'microsecond',
            'tzname',
            'tzoffset',
            'ampm',
            'any_unused_tokens']

    
    def _parse(self, timestr, dayfirst, yearfirst, fuzzy, fuzzy_with_tokens = (None, None, False, False)):
        '''
        Private method which performs the heavy lifting of parsing, called from
        ``parse()``, which passes on its ``kwargs`` to this function.

        :param timestr:
            The string to parse.

        :param dayfirst:
            Whether to interpret the first value in an ambiguous 3-integer date
            (e.g. 01/05/09) as the day (``True``) or month (``False``). If
            ``yearfirst`` is set to ``True``, this distinguishes between YDM
            and YMD. If set to ``None``, this value is retrieved from the
            current :class:`parserinfo` object (which itself defaults to
            ``False``).

        :param yearfirst:
            Whether to interpret the first value in an ambiguous 3-integer date
            (e.g. 01/05/09) as the year. If ``True``, the first number is taken
            to be the year, otherwise the last number is taken to be the year.
            If this is set to ``None``, the value is retrieved from the current
            :class:`parserinfo` object (which itself defaults to ``False``).

        :param fuzzy:
            Whether to allow fuzzy parsing, allowing for string like "Today is
            January 1, 2047 at 8:21:00AM".

        :param fuzzy_with_tokens:
            If ``True``, ``fuzzy`` is automatically set to True, and the parser
            will return a tuple where the first element is the parsed
            :class:`datetime.datetime` datetimestamp and the second element is
            a tuple containing the portions of the string which were ignored:

            .. doctest::

                >>> from dateutil.parser import parse
                >>> parse("Today is January 1, 2047 at 8:21:00AM", fuzzy_with_tokens=True)
                (datetime.datetime(2047, 1, 1, 8, 21), (u\'Today is \', u\' \', u\'at \'))

        '''
        if fuzzy_with_tokens:
            fuzzy = True
        info = self.info
    # WARNING: Decompyle incomplete

    
    def _parse_numeric_token(self, tokens, idx, info, ymd, res, fuzzy):
        value_repr = tokens[idx]
        
        try:
            value = self._to_decimal(value_repr)
        except Exception:
            e = None
            six.raise_from(ValueError('Unknown numeric token'), e)
            e = None
            del e
        except:
            e = None
            del e

        len_li = len(value_repr)
        len_l = len(tokens)
    # WARNING: Decompyle incomplete

    
    def _find_hms_idx(self, idx, tokens, info, allow_jump):
        len_l = len(tokens)
    # WARNING: Decompyle incomplete

    
    def _assign_hms(self, res, value_repr, hms):
        value = self._to_decimal(value_repr)
        if hms == 0:
            res.hour = int(value)
            if value % 1:
                res.minute = int(60 * (value % 1))
                return None
            return None
        if None == 1:
            (res.minute, res.second) = self._parse_min_sec(value)
            return None
        if None == 2:
            (res.second, res.microsecond) = self._parsems(value_repr)
            return None

    
    def _could_be_tzname(self, hour, tzname, tzoffset, token):
