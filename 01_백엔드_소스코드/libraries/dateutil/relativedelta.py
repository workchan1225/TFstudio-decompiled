# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: relativedelta.pyc (Python 3.11)

import datetime
import calendar
import operator
from math import copysign
from six import integer_types
from warnings import warn
from _common import weekday
(MO, TU, WE, TH, FR, SA, SU) = (lambda .0: pass# WARNING: Decompyle incomplete
)(range(7)())
weekdays = (lambda .0: pass# WARNING: Decompyle incomplete
)(range(7)())
__all__ = [
    'relativedelta',
    'MO',
    'TU',
    'WE',
    'TH',
    'FR',
    'SA',
    'SU']

class relativedelta(object):
    """
    The relativedelta type is designed to be applied to an existing datetime and
    can replace specific components of that datetime, or represents an interval
    of time.

    It is based on the specification of the excellent work done by M.-A. Lemburg
    in his
    `mx.DateTime <https://www.egenix.com/products/python/mxBase/mxDateTime/>`_ extension.
    However, notice that this type does *NOT* implement the same algorithm as
    his work. Do *NOT* expect it to behave like mx.DateTime's counterpart.

    There are two different ways to build a relativedelta instance. The
    first one is passing it two date/datetime classes::

        relativedelta(datetime1, datetime2)

    The second one is passing it any number of the following keyword arguments::

        relativedelta(arg1=x,arg2=y,arg3=z...)

        year, month, day, hour, minute, second, microsecond:
            Absolute information (argument is singular); adding or subtracting a
            relativedelta with absolute information does not perform an arithmetic
            operation, but rather REPLACES the corresponding value in the
            original datetime with the value(s) in relativedelta.

        years, months, weeks, days, hours, minutes, seconds, microseconds:
            Relative information, may be negative (argument is plural); adding
            or subtracting a relativedelta with relative information performs
            the corresponding arithmetic operation on the original datetime value
            with the information in the relativedelta.

        weekday:
            One of the weekday instances (MO, TU, etc) available in the
            relativedelta module. These instances may receive a parameter N,
            specifying the Nth weekday, which could be positive or negative
            (like MO(+1) or MO(-2)). Not specifying it is the same as specifying
            +1. You can also use an integer, where 0=MO. This argument is always
            relative e.g. if the calculated date is already Monday, using MO(1)
            or MO(-1) won't change the day. To effectively make it absolute, use
            it in combination with the day argument (e.g. day=1, MO(1) for first
            Monday of the month).

        leapdays:
            Will add given days to the date found, if year is a leap
            year, and the date found is post 28 of february.

        yearday, nlyearday:
            Set the yearday or the non-leap year day (jump leap days).
            These are converted to day/month/leapdays information.

    There are relative and absolute forms of the keyword
    arguments. The plural is relative, and the singular is
    absolute. For each argument in the order below, the absolute form
    is applied first (by setting each attribute to that value) and
    then the relative form (by adding the value to the attribute).

    The order of attributes considered when this relativedelta is
    added to a datetime is:

    1. Year
    2. Month
    3. Day
    4. Hours
    5. Minutes
    6. Seconds
    7. Microseconds

    Finally, weekday is applied, using the rule described above.

    For example

    >>> from datetime import datetime
    >>> from dateutil.relativedelta import relativedelta, MO
    >>> dt = datetime(2018, 4, 9, 13, 37, 0)
    >>> delta = relativedelta(hours=25, day=1, weekday=MO(1))
    >>> dt + delta
    datetime.datetime(2018, 4, 2, 14, 37)

    First, the day is set to 1 (the first of the month), then 25 hours
    are added, to get to the 2nd day and 14th hour, finally the
    weekday is applied, but since the 2nd is already a Monday there is
    no effect.

    """
    
    def __init__(self, dt1, dt2, years, months, days, leapdays, weeks, hours, minutes, seconds, microseconds, year, month, day, weekday, yearday, nlyearday, hour, minute, second, microsecond = (None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, None, None, None, None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def _fix(self):
        if abs(self.microseconds) > 999999:
            s = _sign(self.microseconds)
            (div, mod) = divmod(self.microseconds * s, 1000000)
            self.microseconds = mod * s
        if abs(self.seconds) > 59:
            _sign(self.seconds) = self, self.seconds += div * s, .seconds
            (div, mod) = divmod(self.seconds * s, 60)
            self.seconds = mod * s
        if abs(self.minutes) > 59:
            _sign(self.minutes) = self, self.minutes += div * s, .minutes
            (div, mod) = divmod(self.minutes * s, 60)
            self.minutes = mod * s
        if abs(self.hours) > 23:
            _sign(self.hours) = self, self.hours += div * s, .hours
            (div, mod) = divmod(self.hours * s, 24)
            self.hours = mod * s
        if abs(self.months) > 11:
            _sign(self.months) = self, self.days += div * s, .days
            (div, mod) = divmod(self.months * s, 12)
            self.months = mod * s
    # WARNING: Decompyle incomplete

    weeks = (lambda self: int(self.days / 7))()
    weeks = (lambda self, value: self.days = (self.days - self.weeks * 7) + value * 7)()
    
    def _set_months(self, months):
        self.months = months
        if abs(self.months) > 11:
            s = _sign(self.months)
            (div, mod) = divmod(self.months * s, 12)
            self.months = mod * s
            self.years = div * s
            return None
        self.years = None

    
    def normalized(self):
        '''
        Return a version of this object represented entirely using integer
        values for the relative attributes.

        >>> relativedelta(days=1.5, hours=2).normalized()
        relativedelta(days=+1, hours=+14)

        :return:
            Returns a :class:`dateutil.relativedelta.relativedelta` object.
        '''
        days = int(self.days)
        hours_f = round(self.hours + 24 * (self.days - days), 11)
        hours = int(hours_f)
        minutes_f = round(self.minutes + 60 * (hours_f - hours), 10)
        minutes = int(minutes_f)
        seconds_f = round(self.seconds + 60 * (minutes_f - minutes), 8)
        seconds = int(seconds_f)
        microseconds = round(self.microseconds + 1e+06 * (seconds_f - seconds))
        return self.__class__(years = self.years, months = self.months, days = days, hours = hours, minutes = minutes, seconds = seconds, microseconds = microseconds, leapdays = self.leapdays, year = self.year, month = self.month, day = self.day, weekday = self.weekday, hour = self.hour, minute = self.minute, second = self.second, microsecond = self.microsecond)

    
    def __add__(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def __radd__(self, other):
        return self.__add__(other)

    
    def __rsub__(self, other):
        return self.__neg__().__radd__(other)

    
    def __sub__(self, other):
        if not isinstance(other, relativedelta):
            return NotImplemented
    # WARNING: Decompyle incomplete

    
    def __abs__(self):
        return self.__class__(years = abs(self.years), months = abs(self.months), days = abs(self.days), hours = abs(self.hours), minutes = abs(self.minutes), seconds = abs(self.seconds), microseconds = abs(self.microseconds), leapdays = self.leapdays, year = self.year, month = self.month, day = self.day, weekday = self.weekday, hour = self.hour, minute = self.minute, second = self.second, microsecond = self.microsecond)

    
    def __neg__(self):
        return self.__class__(years = -(self.years), months = -(self.months), days = -(self.days), hours = -(self.hours), minutes = -(self.minutes), seconds = -(self.seconds), microseconds = -(self.microseconds), leapdays = self.leapdays, year = self.year, month = self.month, day = self.day, weekday = self.weekday, hour = self.hour, minute = self.minute, second = self.second, microsecond = self.microsecond)

    
    def __bool__(self):
