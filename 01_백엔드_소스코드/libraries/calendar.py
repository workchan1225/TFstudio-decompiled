# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: calendar.pyc (Python 3.11)

'''Calendar printing functions

Note when comparing these calendars to the ones printed by cal(1): By
default, these calendars have Monday as the first day of the week, and
Sunday as the last (the European convention). Use setfirstweekday() to
set the first day of the week (0=Monday, 6=Sunday).'''
import sys
import datetime
import locale as _locale
from itertools import repeat
__all__ = [
    'IllegalMonthError',
    'IllegalWeekdayError',
    'setfirstweekday',
    'firstweekday',
    'isleap',
    'leapdays',
    'weekday',
    'monthrange',
    'monthcalendar',
    'prmonth',
    'month',
    'prcal',
    'calendar',
    'timegm',
    'month_name',
    'month_abbr',
    'day_name',
    'day_abbr',
    'Calendar',
    'TextCalendar',
    'HTMLCalendar',
    'LocaleTextCalendar',
    'LocaleHTMLCalendar',
    'weekheader',
    'MONDAY',
    'TUESDAY',
    'WEDNESDAY',
    'THURSDAY',
    'FRIDAY',
    'SATURDAY',
    'SUNDAY']
error = ValueError

class IllegalMonthError(ValueError):
    
    def __init__(self, month):
        self.month = month

    
    def __str__(self):
        return 'bad month number %r; must be 1-12' % self.month



class IllegalWeekdayError(ValueError):
    
    def __init__(self, weekday):
        self.weekday = weekday

    
    def __str__(self):
        return 'bad weekday number %r; must be 0 (Monday) to 6 (Sunday)' % self.weekday


January = 1
February = 2
mdays = [
    0,
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31]

class _localized_month:
    _months = range(12)()
    _months.insert(0, (lambda x: ''))
    
    def __init__(self, format):
        self.format = format

    
    def __getitem__(self, i):
        pass
    # WARNING: Decompyle incomplete

    
    def __len__(self):
        return 13



class _localized_day:
    _days = range(7)()
    
    def __init__(self, format):
        self.format = format

    
    def __getitem__(self, i):
        pass
    # WARNING: Decompyle incomplete

    
    def __len__(self):
        return 7


day_name = _localized_day('%A')
day_abbr = _localized_day('%a')
month_name = _localized_month('%B')
month_abbr = _localized_month('%b')
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)

def isleap(year):
