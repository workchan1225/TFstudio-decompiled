# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: isoparser.pyc (Python 3.11)

'''
This module offers a parser for ISO-8601 strings

It is intended to support all valid date, time and datetime formats per the
ISO-8601 specification.

..versionadded:: 2.7.0
'''
from datetime import datetime, timedelta, time, date
import calendar
from dateutil import tz
from functools import wraps
import re
import six
__all__ = [
    'isoparse',
    'isoparser']

def _takes_ascii(f):
    pass
# WARNING: Decompyle incomplete


class isoparser(object):
    
    def __init__(self, sep = (None,)):
        """
        :param sep:
            A single character that separates date and time portions. If
            ``None``, the parser will accept any single character.
            For strict ISO-8601 adherence, pass ``'T'``.
        """
        pass
    # WARNING: Decompyle incomplete

    isoparse = (lambda self, dt_str: (components, pos) = self._parse_isodate(dt_str)# WARNING: Decompyle incomplete
)()
    parse_isodate = (lambda self, datestr: (components, pos) = self._parse_isodate(datestr)if pos < len(datestr):
raise ValueError('String contains unknown ISO ' + 'components: {!r}'.format(datestr.decode('ascii')))# WARNING: Decompyle incomplete
)()
    parse_isotime = (lambda self, timestr: components = self._parse_isotime(timestr)if components[0] == 24:
components[0] = 0# WARNING: Decompyle incomplete
)()
    parse_tzstr = (lambda self, tzstr, zero_as_utc = (True,): self._parse_tzstr(tzstr, zero_as_utc = zero_as_utc))()
    _DATE_SEP = b'-'
    _TIME_SEP = b':'
    _FRACTION_REGEX = re.compile(b'[\\.,]([0-9]+)')
    
    def _parse_isodate(self, dt_str):
        
        try:
            return self._parse_isodate_common(dt_str)
        except ValueError:
            return 


    
    def _parse_isodate_common(self, dt_str):
        len_str = len(dt_str)
        components = [
            1,
            1,
            1]
        if len_str < 4:
            raise ValueError('ISO string too short')
        components[0] = int(dt_str[0:4])
        pos = 4
        if pos >= len_str:
            return (components, pos)
        has_sep = None[pos:pos + 1] == self._DATE_SEP
        if has_sep:
            pos += 1
        if len_str - pos < 2:
            raise ValueError('Invalid common month')
        components[1] = int(dt_str[pos:pos + 2])
        pos += 2
        if pos >= len_str:
            if has_sep:
                return (components, pos)
            raise None('Invalid ISO format')
        if has_sep:
            if dt_str[pos:pos + 1] != self._DATE_SEP:
                raise ValueError('Invalid separator in ISO string')
            pos += 1
        if len_str - pos < 2:
            raise ValueError('Invalid common day')
        components[2] = int(dt_str[pos:pos + 2])
        return (components, pos + 2)

    
    def _parse_isodate_uncommon(self, dt_str):
        if len(dt_str) < 4:
            raise ValueError('ISO string too short')
        year = int(dt_str[0:4])
        has_sep = dt_str[4:5] == self._DATE_SEP
        pos = 4 + has_sep
        if dt_str[pos:pos + 1] == b'W':
            pos += 1
            weekno = int(dt_str[pos:pos + 2])
            pos += 2
            dayno = 1
            if len(dt_str) > pos:
                if dt_str[pos:pos + 1] == self._DATE_SEP != has_sep:
                    raise ValueError('Inconsistent use of dash separator')
                pos += has_sep
                dayno = int(dt_str[pos:pos + 1])
                pos += 1
            base_date = self._calculate_weekdate(year, weekno, dayno)
        elif len(dt_str) - pos < 3:
            raise ValueError('Invalid ordinal day')
        ordinal_day = int(dt_str[pos:pos + 3])
        pos += 3
        if ordinal_day < 1 or ordinal_day > 365 + calendar.isleap(year):
            raise ValueError('Invalid ordinal day' + ' {} for year {}'.format(ordinal_day, year))
        base_date = date(year, 1, 1) + timedelta(days = ordinal_day - 1)
        components = [
            base_date.year,
            base_date.month,
            base_date.day]
        return (components, pos)

    
    def _calculate_weekdate(self, year, week, day):
        '''
        Calculate the day of corresponding to the ISO year-week-day calendar.

        This function is effectively the inverse of
        :func:`datetime.date.isocalendar`.

        :param year:
            The year in the ISO calendar

        :param week:
            The week in the ISO calendar - range is [1, 53]

        :param day:
            The day in the ISO calendar - range is [1 (MON), 7 (SUN)]

        :return:
            Returns a :class:`datetime.date`
        '''
        if not  < 0, week or 0, week < 54:
            pass
        
        raise ValueError('Invalid week: {}'.format(week))
        if not  < 0, day or 0, day < 8:
            pass
        
        raise ValueError('Invalid weekday: {}'.format(day))
        jan_4 - timedelta(days = jan_4.isocalendar()[2] - 1) = date(year, 1, 4)
        week_offset = (week - 1) * 7 + (day - 1)
        return week_1 + timedelta(days = week_offset)

    
    def _parse_isotime(self, timestr):
        len_str = len(timestr)
        components = [
            0,
            0,
            0,
            0,
            None]
        pos = 0
        comp = -1
        if len_str < 2:
            raise ValueError('ISO time too short')
        has_sep = False
    # WARNING: Decompyle incomplete

    
    def _parse_tzstr(self, tzstr, zero_as_utc = (True,)):
        if tzstr == b'Z' or tzstr == b'z':
            return tz.UTC
        if None(tzstr) not in frozenset({3, 5, 6}):
            raise ValueError('Time zone offset must be 1, 3, 5 or 6 characters')
        if tzstr[0:1] == b'-':
            mult = -1
        elif tzstr[0:1] == b'+':
            mult = 1
        else:
            raise ValueError('Time zone offset requires sign')
        hours = int(tzstr[1:3])
        if len(tzstr) == 3:
            minutes = 0
        elif tzstr[3:4] == self._TIME_SEP:
            pass
        
        minutes = tzstr(4[3:])
        if zero_as_utc and hours == 0 and minutes == 0:
            return tz.UTC
        if int > 59:
            raise ValueError('Invalid minutes in time zone offset')
        if hours > 23:
            raise ValueError('Invalid hours in time zone offset')
        return tz.tzoffset(None, mult * (hours * 60 + minutes) * 60)


DEFAULT_ISOPARSER = isoparser()
isoparse = DEFAULT_ISOPARSER.isoparse
