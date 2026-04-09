# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rrule.pyc (Python 3.11)

'''
The rrule module offers a small, complete, and very fast, implementation of
the recurrence rules documented in the
`iCalendar RFC <https://tools.ietf.org/html/rfc5545>`_,
including support for caching of results.
'''
import calendar
import datetime
import heapq
import itertools
import re
import sys
from functools import wraps
from warnings import warn
from six import advance_iterator, integer_types
from six.moves import _thread, range
from _common import weekday as weekdaybase

try:
    from math import gcd
except ImportError:
    from fractions import gcd

__all__ = [
    'rrule',
    'rruleset',
    'rrulestr',
    'YEARLY',
    'MONTHLY',
    'WEEKLY',
    'DAILY',
    'HOURLY',
    'MINUTELY',
    'SECONDLY',
    'MO',
    'TU',
    'WE',
    'TH',
    'FR',
    'SA',
    'SU']
M366MASK = tuple([
    1] * 31 + [
    2] * 29 + [
    3] * 31 + [
    4] * 30 + [
    5] * 31 + [
    6] * 30 + [
    7] * 31 + [
    8] * 31 + [
    9] * 30 + [
    10] * 31 + [
    11] * 30 + [
    12] * 31 + [
    1] * 7)
M365MASK = list(M366MASK)
M29, M30, M31 = list(range(1, 30)), list(range(1, 31)), list(range(1, 32))
MDAY366MASK = tuple(M31 + M29 + M31 + M30 + M31 + M30 + M31 + M31 + M30 + M31 + M30 + M31 + M31[:7])
MDAY365MASK = list(MDAY366MASK)
M29, M30, M31 = list(range(-29, 0)), list(range(-30, 0)), list(range(-31, 0))
NMDAY366MASK = tuple(M31 + M29 + M31 + M30 + M31 + M30 + M31 + M31 + M30 + M31 + M30 + M31 + M31[:7])
NMDAY365MASK = list(NMDAY366MASK)
M366RANGE = (0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366)
M365RANGE = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365)
WDAYMASK = [
    0,
    1,
    2,
    3,
    4,
    5,
    6] * 55
del M29
del M30
del M31
del M365MASK[59]
del MDAY365MASK[59]
del NMDAY365MASK[31]
MDAY365MASK = tuple(MDAY365MASK)
M365MASK = tuple(M365MASK)
FREQNAMES = [
    'YEARLY',
    'MONTHLY',
    'WEEKLY',
    'DAILY',
    'HOURLY',
    'MINUTELY',
    'SECONDLY']
(YEARLY, MONTHLY, WEEKLY, DAILY, HOURLY, MINUTELY, SECONDLY) = list(range(7))
easter = None
parser = None

class weekday(weekdaybase):
    pass
# WARNING: Decompyle incomplete

(MO, TU, WE, TH, FR, SA, SU) = (lambda .0: pass# WARNING: Decompyle incomplete
)(range(7)())
weekdays = (lambda .0: pass# WARNING: Decompyle incomplete
)(range(7)())

def _invalidates_cache(f):
    '''
    Decorator for rruleset methods which may invalidate the
    cached length.
    '''
    pass
# WARNING: Decompyle incomplete


class rrulebase(object):
    
    def __init__(self, cache = (False,)):
        if cache:
            self._cache = []
            self._cache_lock = _thread.allocate_lock()
            self._invalidate_cache()
            return None
        self._cache = None
        self._cache_complete = False
        self._len = None

    
    def __iter__(self):
        if self._cache_complete:
            return iter(self._cache)
    # WARNING: Decompyle incomplete

    
    def _invalidate_cache(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _iter_cached(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, item):
        if self._cache_complete:
            return self._cache[item]
        if None(item, slice):
            if item.step and item.step < 0:
                return list(iter(self))[item]
            if not item.start or item.stop:
                if not item.step:
                    return None(itertools.islice(self, 0, sys.maxsize, 1))
                if item.step >= 0:
                    gen = iter(self)
                    
                    try:
                        for i in range(item + 1):
                            res = advance_iterator(gen)
                    except StopIteration:
                        0
                        raise IndexError
                        return res
                        return list(iter(self))[item]


    
    def __contains__(self, item):
        if self._cache_complete:
            return item in self._cache
        for i in None:
            if i == item:
                return True
            if None > item:
                return False
            return False

    
    def count(self):
        """ Returns the number of recurrences in this set. It will have go
            through the whole recurrence, if this hasn't been done before. """
        pass
    # WARNING: Decompyle incomplete

    
    def before(self, dt, inc = (False,)):
        ''' Returns the last recurrence before the given datetime instance. The
            inc keyword defines what happens if dt is an occurrence. With
            inc=True, if dt itself is an occurrence, it will be returned. '''
        if self._cache_complete:
            gen = self._cache
        else:
            gen = self
        last = None
        if inc:
            for i in gen:
                if i > dt:
                    pass
                else:
                    last = i
        for i in gen:
            if i >= dt:
                pass
            else:
                last = i
            return last

    
    def after(self, dt, inc = (False,)):
        ''' Returns the first recurrence after the given datetime instance. The
            inc keyword defines what happens if dt is an occurrence. With
            inc=True, if dt itself is an occurrence, it will be returned.  '''
        if self._cache_complete:
            gen = self._cache
        else:
            gen = self
        if inc:
            for i in gen:
                if i >= dt:
                    
                    return None, i
        for None in gen:
            if i > dt:
                
                return None, i
            return None

    
    def xafter(self, dt, count, inc = (None, False)):
        '''
        Generator which yields up to `count` recurrences after the given
        datetime instance, equivalent to `after`.

        :param dt:
            The datetime at which to start generating recurrences.

        :param count:
            The maximum number of recurrences to generate. If `None` (default),
            dates are generated until the recurrence rule is exhausted.

        :param inc:
            If `dt` is an instance of the rule and `inc` is `True`, it is
            included in the output.

        :yields: Yields a sequence of `datetime` objects.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def between(self, after, before, inc, count = (False, 1)):
        ''' Returns all the occurrences of the rrule between after and before.
        The inc keyword defines what happens if after and/or before are
        themselves occurrences. With inc=True, they will be included in the
        list, if they are found in the recurrence set. '''
        if self._cache_complete:
            gen = self._cache
        else:
            gen = self
        started = False
        l = []
        if inc:
            for i in gen:
                if i > before:
                    pass
                elif not started:
                    if i >= after:
                        started = True
                        l.append(i)
                    continue
                l.append(i)
        for i in gen:
            if i >= before:
                pass
            elif not started:
                if i > after:
                    started = True
                    l.append(i)
                continue
            l.append(i)
            return l



class rrule(rrulebase):
    pass
# WARNING: Decompyle incomplete


class _iterinfo(object):
    __slots__ = [
        'rrule',
        'lastyear',
        'lastmonth',
        'yearlen',
        'nextyearlen',
        'yearordinal',
        'yearweekday',
        'mmask',
        'mrange',
        'mdaymask',
        'nmdaymask',
        'wdaymask',
        'wnomask',
        'nwdaymask',
        'eastermask']
    
    def __init__(self, rrule):
        for attr in self.__slots__:
            setattr(self, attr, None)
            self.rrule = rrule
            return None

    
    def rebuild(self, year, month):
        rr = self.rrule
        if year != self.lastyear:
            self.yearlen = 365 + calendar.isleap(year)
            self.nextyearlen = 365 + calendar.isleap(year + 1)
            firstyday = datetime.date(year, 1, 1)
            self.yearordinal = firstyday.toordinal()
            self.yearweekday = firstyday.weekday()
            wday = datetime.date(year, 1, 1).weekday()
            if self.yearlen == 365:
                self.mmask = M365MASK
                self.mdaymask = MDAY365MASK
                self.nmdaymask = NMDAY365MASK
                self.wdaymask = WDAYMASK[wday:]
                self.mrange = M365RANGE
            else:
                self.mmask = M366MASK
                self.mdaymask = MDAY366MASK
                self.nmdaymask = NMDAY366MASK
                self.wdaymask = WDAYMASK[wday:]
                self.mrange = M366RANGE
            if not rr._byweekno:
                self.wnomask = None
            else:
                self.wnomask = [
                    0] * (self.yearlen + 7)
                no1wkst = ((7 - self.yearweekday) + rr._wkst) % 7
                firstwkst = ((7 - self.yearweekday) + rr._wkst) % 7
                if no1wkst >= 4:
                    no1wkst = 0
                    wyearlen = self.yearlen + (self.yearweekday - rr._wkst) % 7
                else:
                    wyearlen = self.yearlen - no1wkst
                (div, mod) = divmod(wyearlen, 7)
                numweeks = div + mod // 4
                for n in rr._byweekno:
                    if n < 0:
                        n += numweeks + 1
                    if not  < 0, n or 0, n <= numweeks:
                        pass
                    
                    if n > 1:
                        pass
                    for j in range(7):
                        self.wnomask[i] = 1
                        i += 1
                        if self.wdaymask[i] == rr._wkst:
                            None if no1wkst != firstwkst else no1wkst + (n - 1) * 7
                        
                        if 1 in rr._byweekno:
                            i = no1wkst + numweeks * 7
                            if no1wkst != firstwkst:
                                i -= 7 - firstwkst
                            if i < self.yearlen:
                                for j in range(7):
                                    self.wnomask[i] = 1
                                    i += 1
                                    if self.wdaymask[i] == rr._wkst:
                                        None if no1wkst != firstwkst else no1wkst + (n - 1) * 7
                                    
                                    if no1wkst and lnumweeks in rr._byweekno:
                                        for i in range(no1wkst):
                                            self.wnomask[i] = 1
                                            if rr._bynweekday:
                                                if month != self.lastmonth or year != self.lastyear:
                                                    ranges = []
                                                    if rr._freq == YEARLY:
                                                        if rr._bymonth:
                                                            for month in rr._bymonth:
                                                                ranges.append(self.mrange[month - 1:month + 1])
                                                        ranges = [
                                                            (0, self.yearlen)]
                                                    elif rr._freq == MONTHLY:
                                                        ranges = [
                                                            self.mrange[month - 1:month + 1]]
                                                    if ranges:
                                                        self.nwdaymask = [
                                                            0] * self.yearlen
                                                        for first, last in ranges:
                                                            last -= 1
                                                            for wday, n in rr._bynweekday:
                                                                if  <= first, i or first, i <= last:
                                                                    pass
                                                                else:
                                                                    None if n < 0 else None if -1 not in rr._byweekno else None if no1wkst != firstwkst else no1wkst + (n - 1) * 7
                                                                if rr._byeaster:
                                                                    [
                                                                        0] * (self.yearlen + 7) = 1
                                                                    eyday = easter.easter(year).toordinal() - self.yearordinal
                                                                    for offset in rr._byeaster:
                                                                        self.eastermask[eyday + offset] = 1
                                                                        self.lastyear = year
                                                                        self.lastmonth = month
                                                                        return None

    
    def ydayset(self, year, month, day):
        return (list(range(self.yearlen)), 0, self.yearlen)

    
    def mdayset(self, year, month, day):
        dset = [
            None] * self.yearlen
        (start, end) = self.mrange[month - 1:month + 1]
        for i in range(start, end):
            dset[i] = i
            return (dset, start, end)

    
    def wdayset(self, year, month, day):
        dset = [
            None] * (self.yearlen + 7)
        i = datetime.date(year, month, day).toordinal() - self.yearordinal
        start = i
        for j in range(7):
            dset[i] = i
            i += 1
            if self.wdaymask[i] == self.rrule._wkst:
                pass
            
            return (dset, start, i)

    
    def ddayset(self, year, month, day):
        dset = [
            None] * self.yearlen
        i = datetime.date(year, month, day).toordinal() - self.yearordinal
        dset[i] = i
        return (dset, i, i + 1)

    
    def htimeset(self, hour, minute, second):
        tset = []
        rr = self.rrule
        for minute in rr._byminute:
            for second in rr._bysecond:
                tset.append(datetime.time(hour, minute, second, tzinfo = rr._tzinfo))
                tset.sort()
                return tset

    
    def mtimeset(self, hour, minute, second):
        tset = []
        rr = self.rrule
        for second in rr._bysecond:
            tset.append(datetime.time(hour, minute, second, tzinfo = rr._tzinfo))
            tset.sort()
            return tset

    
    def stimeset(self, hour, minute, second):
        return (datetime.time(hour, minute, second, tzinfo = self.rrule._tzinfo),)



class rruleset(rrulebase):
    pass
# WARNING: Decompyle incomplete


class _rrulestr(object):
    ''' Parses a string representation of a recurrence rule or set of
    recurrence rules.

    :param s:
        Required, a string defining one or more recurrence rules.

    :param dtstart:
        If given, used as the default recurrence start if not specified in the
        rule string.

    :param cache:
        If set ``True`` caching of results will be enabled, improving
        performance of multiple queries considerably.

    :param unfold:
        If set ``True`` indicates that a rule string is split over more
        than one line and should be joined before processing.

    :param forceset:
        If set ``True`` forces a :class:`dateutil.rrule.rruleset` to
        be returned.

    :param compatible:
        If set ``True`` forces ``unfold`` and ``forceset`` to be ``True``.

    :param ignoretz:
        If set ``True``, time zones in parsed strings are ignored and a naive
        :class:`datetime.datetime` object is returned.

    :param tzids:
        If given, a callable or mapping used to retrieve a
        :class:`datetime.tzinfo` from a string representation.
        Defaults to :func:`dateutil.tz.gettz`.

    :param tzinfos:
        Additional time zone names / aliases which may be present in a string
        representation.  See :func:`dateutil.parser.parse` for more
        information.

    :return:
        Returns a :class:`dateutil.rrule.rruleset` or
        :class:`dateutil.rrule.rrule`
    '''
    _freq_map = {
        'YEARLY': YEARLY,
        'MONTHLY': MONTHLY,
        'WEEKLY': WEEKLY,
        'DAILY': DAILY,
        'HOURLY': HOURLY,
        'MINUTELY': MINUTELY,
        'SECONDLY': SECONDLY }
    _weekday_map = {
        'MO': 0,
        'TU': 1,
        'WE': 2,
        'TH': 3,
        'FR': 4,
        'SA': 5,
        'SU': 6 }
    
    def _handle_int(self, rrkwargs, name, value, **kwargs):
        rrkwargs[name.lower()] = int(value)

    
    def _handle_int_list(self, rrkwargs, name, value, **kwargs):
        rrkwargs[name.lower()] = value.split(',')()

    _handle_INTERVAL = _handle_int
    _handle_COUNT = _handle_int
    _handle_BYSETPOS = _handle_int_list
    _handle_BYMONTH = _handle_int_list
    _handle_BYMONTHDAY = _handle_int_list
    _handle_BYYEARDAY = _handle_int_list
    _handle_BYEASTER = _handle_int_list
    _handle_BYWEEKNO = _handle_int_list
    _handle_BYHOUR = _handle_int_list
    _handle_BYMINUTE = _handle_int_list
    _handle_BYSECOND = _handle_int_list
    
    def _handle_FREQ(self, rrkwargs, name, value, **kwargs):
        rrkwargs['freq'] = self._freq_map[value]

    
    def _handle_UNTIL(self, rrkwargs, name, value, **kwargs):
        global parser
        if not parser:
            parser = parser
            import dateutil
        
        try:
            rrkwargs['until'] = parser.parse(value, ignoretz = kwargs.get('ignoretz'), tzinfos = kwargs.get('tzinfos'))
            return None
        except ValueError:
            raise ValueError('invalid until date')


    
    def _handle_WKST(self, rrkwargs, name, value, **kwargs):
        rrkwargs['wkst'] = self._weekday_map[value]

    
    def _handle_BYWEEKDAY(self, rrkwargs, name, value, **kwargs):
