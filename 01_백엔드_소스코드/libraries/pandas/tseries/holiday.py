# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: holiday.pyc (Python 3.11)

from __future__ import annotations
from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Literal, overload
import warnings
from dateutil.relativedelta import FR, MO, SA, SU, TH, TU, WE
import numpy as np
from pandas._libs.tslibs.offsets import BaseOffset
from pandas.errors import PerformanceWarning
from pandas import DateOffset, DatetimeIndex, Series, Timestamp, concat, date_range
from pandas.tseries.offsets import Day, Easter
if TYPE_CHECKING:
    from collections.abc import Callable

def next_monday(dt = None):
    '''
    If holiday falls on Saturday, use following Monday instead;
    if holiday falls on Sunday, use Monday instead
    '''
    if dt.weekday() == 5:
        return dt + timedelta(2)
    if None.weekday() == 6:
        return dt + timedelta(1)


def next_monday_or_tuesday(dt = None):
    '''
    For second holiday of two adjacent ones!
    If holiday falls on Saturday, use following Monday instead;
    if holiday falls on Sunday or Monday, use following Tuesday instead
    (because Monday is already taken by adjacent holiday on the day before)
    '''
    dow = dt.weekday()
    if dow in (5, 6):
        return dt + timedelta(2)
    if None == 0:
        return dt + timedelta(1)


def previous_friday(dt = None):
    '''
    If holiday falls on Saturday or Sunday, use previous Friday instead.
    '''
    if dt.weekday() == 5:
        return dt - timedelta(1)
    if None.weekday() == 6:
        return dt - timedelta(2)


def sunday_to_monday(dt = None):
    '''
    If holiday falls on Sunday, use day thereafter (Monday) instead.
    '''
    if dt.weekday() == 6:
        return dt + timedelta(1)


def weekend_to_monday(dt = None):
    '''
    If holiday falls on Sunday or Saturday,
    use day thereafter (Monday) instead.
    Needed for holidays such as Christmas observation in Europe
    '''
    if dt.weekday() == 6:
        return dt + timedelta(1)
    if None.weekday() == 5:
        return dt + timedelta(2)


def nearest_workday(dt = None):
    '''
    If holiday falls on Saturday, use day before (Friday) instead;
    if holiday falls on Sunday, use day thereafter (Monday) instead.
    '''
    if dt.weekday() == 5:
        return dt - timedelta(1)
    if None.weekday() == 6:
        return dt + timedelta(1)


def next_workday(dt = None):
    '''
    returns next workday used for observances
    '''
    dt += timedelta(days = 1)
# WARNING: Decompyle incomplete


def previous_workday(dt = None):
    '''
    returns previous workday used for observances
    '''
    dt -= timedelta(days = 1)
# WARNING: Decompyle incomplete


def before_nearest_workday(dt = None):
    '''
    returns previous workday before nearest workday
    '''
    return previous_workday(nearest_workday(dt))


def after_nearest_workday(dt = None):
    '''
    returns next workday after nearest workday
    needed for Boxing day or multiple holidays in a series
    '''
    return next_workday(nearest_workday(dt))


class Holiday:
    days_of_week: 'tuple[int, ...] | None' = '\n    Class that defines a holiday with start/end dates and rules\n    for observance.\n    '
    
    def __init__(self, name, year, month, day, offset, observance = None, start_date = None, end_date = None, days_of_week = (None, None, None, None, None, None, None, None, None), exclude_dates = ('name', 'str', 'offset', 'BaseOffset | list[BaseOffset] | None', 'observance', 'Callable | None', 'days_of_week', 'tuple | None', 'exclude_dates', 'DatetimeIndex | None', 'return', 'None')):
        '''
        Parameters
        ----------
        name : str
            Name of the holiday , defaults to class name
        year : int, default None
            Year of the holiday
        month : int, default None
            Month of the holiday
        day : int, default None
            Day of the holiday
        offset : list of pandas.tseries.offsets or
                class from pandas.tseries.offsets, default None
            Computes offset from date
        observance : function, default None
            Computes when holiday is given a pandas Timestamp
        start_date : datetime-like, default None
            First date the holiday is observed
        end_date : datetime-like, default None
            Last date the holiday is observed
        days_of_week : tuple of int or dateutil.relativedelta weekday strs, default None
            Provide a tuple of days e.g  (0,1,2,3,) for Monday through Thursday
            Monday=0,..,Sunday=6
            Only instances of the holiday included in days_of_week will be computed
        exclude_dates : DatetimeIndex or default None
            Specific dates to exclude e.g. skipping a specific year\'s holiday

        Examples
        --------
        >>> from dateutil.relativedelta import MO

        >>> USMemorialDay = pd.tseries.holiday.Holiday(
        ...     "Memorial Day", month=5, day=31, offset=pd.DateOffset(weekday=MO(-1))
        ... )
        >>> USMemorialDay
        Holiday: Memorial Day (month=5, day=31, offset=<DateOffset: weekday=MO(-1)>)

        >>> USLaborDay = pd.tseries.holiday.Holiday(
        ...     "Labor Day", month=9, day=1, offset=pd.DateOffset(weekday=MO(1))
        ... )
        >>> USLaborDay
        Holiday: Labor Day (month=9, day=1, offset=<DateOffset: weekday=MO(+1)>)

        >>> July3rd = pd.tseries.holiday.Holiday("July 3rd", month=7, day=3)
        >>> July3rd
        Holiday: July 3rd (month=7, day=3, )

        >>> NewYears = pd.tseries.holiday.Holiday(
        ...     "New Years Day",
        ...     month=1,
        ...     day=1,
        ...     observance=pd.tseries.holiday.nearest_workday,
        ... )
        >>> NewYears  # doctest: +SKIP
        Holiday: New Years Day (
            month=1, day=1, observance=<function nearest_workday at 0x66545e9bc440>
        )

        >>> July3rd = pd.tseries.holiday.Holiday(
        ...     "July 3rd", month=7, day=3, days_of_week=(0, 1, 2, 3)
        ... )
        >>> July3rd
        Holiday: July 3rd (month=7, day=3, )
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        info = ''
    # WARNING: Decompyle incomplete

    dates = (lambda self = None, start_date = None, end_date = overload, return_name = ('return_name', 'Literal[True]', 'return', 'Series'): pass)()
    dates = (lambda self = None, start_date = None, end_date = overload, return_name = ('return_name', 'Literal[False]', 'return', 'DatetimeIndex'): pass)()
    dates = (lambda self = None, start_date = None, end_date = overload: pass)()
    
    def dates(self = None, start_date = None, end_date = None, return_name = (False,)):
        '''
        Calculate holidays observed between start date and end date

        Parameters
        ----------
        start_date : starting date, datetime-like, optional
        end_date : ending date, datetime-like, optional
        return_name : bool, optional, default=False
            If True, return a series that has dates and holiday names.
            False will only return dates.

        Returns
        -------
        Series or DatetimeIndex
            Series if return_name is True
        '''
        start_date = Timestamp(start_date)
        end_date = Timestamp(end_date)
        filter_start_date = start_date
        filter_end_date = end_date
    # WARNING: Decompyle incomplete

    
    def _reference_dates(self = None, start_date = None, end_date = None):
        '''
        Get reference dates for the holiday.

        Return reference dates for the holiday also returning the year
        prior to the start_date and year following the end_date.  This ensures
        that any offsets to be applied will yield the holidays within
        the passed in dates.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _apply_rule(self = None, dates = None):
        '''
        Apply the given offset/observance to a DatetimeIndex of dates.

        Parameters
        ----------
        dates : DatetimeIndex
            Dates to apply the given offset/observance rule

        Returns
        -------
        Dates with rules applied
        '''
        pass
    # WARNING: Decompyle incomplete


holiday_calendars: 'dict[str, type[AbstractHolidayCalendar]]' = { }

def register(cls = None):
    
    try:
        name = cls.name
    except AttributeError:
        name = cls.__name__

    holiday_calendars[name] = cls


def get_calendar(name = None):
    '''
    Return an instance of a calendar based on its name.

    Parameters
    ----------
    name : str
        Calendar name to return an instance of
    '''
    return holiday_calendars[name]()


class HolidayCalendarMetaClass(type):
    pass
# WARNING: Decompyle incomplete


def AbstractHolidayCalendar():
    '''AbstractHolidayCalendar'''
    pass
# WARNING: Decompyle incomplete

AbstractHolidayCalendar = <NODE:27>(AbstractHolidayCalendar, 'AbstractHolidayCalendar', metaclass = HolidayCalendarMetaClass)
USMemorialDay = Holiday('Memorial Day', month = 5, day = 31, offset = DateOffset(weekday = MO(-1)))
USLaborDay = Holiday('Labor Day', month = 9, day = 1, offset = DateOffset(weekday = MO(1)))
USColumbusDay = Holiday('Columbus Day', month = 10, day = 1, offset = DateOffset(weekday = MO(2)))
USThanksgivingDay = Holiday('Thanksgiving Day', month = 11, day = 1, offset = DateOffset(weekday = TH(4)))
USMartinLutherKingJr = Holiday('Birthday of Martin Luther King, Jr.', start_date = datetime(1986, 1, 1), month = 1, day = 1, offset = DateOffset(weekday = MO(3)))
USPresidentsDay = Holiday("Washington's Birthday", month = 2, day = 1, offset = DateOffset(weekday = MO(3)))
GoodFriday = Holiday('Good Friday', month = 1, day = 1, offset = [
    Easter(),
    Day(-2)])
EasterMonday = Holiday('Easter Monday', month = 1, day = 1, offset = [
    Easter(),
    Day(1)])

class USFederalHolidayCalendar(AbstractHolidayCalendar):
    '''
    US Federal Government Holiday Calendar based on rules specified by:
    https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/
    '''
    rules = [
        Holiday("New Year's Day", month = 1, day = 1, observance = nearest_workday),
        USMartinLutherKingJr,
        USPresidentsDay,
        USMemorialDay,
        Holiday('Juneteenth National Independence Day', month = 6, day = 19, start_date = '2021-06-18', observance = nearest_workday),
        Holiday('Independence Day', month = 7, day = 4, observance = nearest_workday),
        USLaborDay,
        USColumbusDay,
        Holiday('Veterans Day', month = 11, day = 11, observance = nearest_workday),
        USThanksgivingDay,
        Holiday('Christmas Day', month = 12, day = 25, observance = nearest_workday)]


def HolidayCalendarFactory(name = None, base = None, other = None, base_class = (AbstractHolidayCalendar,)):
    rules = AbstractHolidayCalendar.merge_class(base, other)
    calendar_class = type(name, (base_class,), {
        'rules': rules,
        'name': name })
    return calendar_class

__all__ = [
    'FR',
    'MO',
    'SA',
    'SU',
    'TH',
    'TU',
    'WE',
    'HolidayCalendarFactory',
    'after_nearest_workday',
    'before_nearest_workday',
    'get_calendar',
    'nearest_workday',
    'next_monday',
    'next_monday_or_tuesday',
    'next_workday',
    'previous_friday',
    'previous_workday',
    'register',
    'sunday_to_monday',
    'weekend_to_monday']
