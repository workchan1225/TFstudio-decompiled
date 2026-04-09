# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: npdatetime_helpers.pyc (Python 3.11)

'''
Helper functions for np.timedelta64 and np.datetime64.
For now, multiples-of-units (for example timedeltas expressed in tens
of seconds) are not supported.
'''
import numpy as np
DATETIME_UNITS = {
    'Y': 0,
    'M': 1,
    'W': 2,
    'D': 4,
    'h': 5,
    'm': 6,
    's': 7,
    'ms': 8,
    'us': 9,
    'ns': 10,
    'ps': 11,
    'fs': 12,
    'as': 13,
    '': 14 }
NAT = np.timedelta64('nat').astype(np.int64)

def same_kind(src, dest):
    '''
    Whether the *src* and *dest* units are of the same kind.
    '''
    return DATETIME_UNITS[src] < 5 == DATETIME_UNITS[dest] < 5


def can_cast_timedelta_units(src, dest):
    src = DATETIME_UNITS[src]
    dest = DATETIME_UNITS[dest]
    if src == dest:
        return True
    if None == 14:
        return True
    if None > dest:
        return False
    if None == 14:
        return False
    if None <= 1 and dest > 1:
        return False

_factors = {
    0: (1, 12),
    2: (4, 7),
    4: (5, 24),
    5: (6, 60),
    6: (7, 60),
    7: (8, 1000),
    8: (9, 1000),
    9: (10, 1000),
    10: (11, 1000),
    11: (12, 1000),
    12: (13, 1000) }

def _get_conversion_multiplier(big_unit_code, small_unit_code):
    '''
    Return an integer multiplier allowing to convert from *big_unit_code*
    to *small_unit_code*.
    None is returned if the conversion is not possible through a
    simple integer multiplication.
    '''
    if big_unit_code == 14:
        return 1
    c = None
    factor = 1
# WARNING: Decompyle incomplete


def get_timedelta_conversion_factor(src_unit, dest_unit):
    '''
    Return an integer multiplier allowing to convert from timedeltas
    of *src_unit* to *dest_unit*.
    '''
    return _get_conversion_multiplier(DATETIME_UNITS[src_unit], DATETIME_UNITS[dest_unit])


def get_datetime_timedelta_conversion(datetime_unit, timedelta_unit):
    '''
    Compute a possible conversion for combining *datetime_unit* and
    *timedelta_unit* (presumably for adding or subtracting).
    Return (result unit, integer datetime multiplier, integer timedelta
    multiplier). RuntimeError is raised if the combination is impossible.
    '''
    dt_unit_code = DATETIME_UNITS[datetime_unit]
    td_unit_code = DATETIME_UNITS[timedelta_unit]
    if td_unit_code == 14 or dt_unit_code == 14:
        return (datetime_unit, 1, 1)
    if None < 2 and dt_unit_code >= 2:
        raise RuntimeError(f'''cannot combine datetime64({datetime_unit!r}) and timedelta64({timedelta_unit!r})''')
    (dt_factor, td_factor) = (1, 1)
    if dt_unit_code == 0:
        if td_unit_code >= 4:
            dt_factor = 146097
            td_factor = 400
            dt_unit_code = 4
        elif td_unit_code == 2:
            dt_factor = 146097
            td_factor = 2800
            dt_unit_code = 2
        elif dt_unit_code == 1:
            if td_unit_code >= 4:
                dt_factor = 146097
                td_factor = 4800
                dt_unit_code = 4
            elif td_unit_code == 2:
                dt_factor = 146097
                td_factor = 33600
                dt_unit_code = 2
# WARNING: Decompyle incomplete


def combine_datetime_timedelta_units(datetime_unit, timedelta_unit):
    '''
    Return the unit result of combining *datetime_unit* with *timedelta_unit*
    (e.g. by adding or subtracting).  None is returned if combining
    those units is forbidden.
    '''
    dt_unit_code = DATETIME_UNITS[datetime_unit]
    td_unit_code = DATETIME_UNITS[timedelta_unit]
    if dt_unit_code == 14:
        return timedelta_unit
    if None == 14:
        return datetime_unit
    if None < 2 and dt_unit_code >= 2:
        return None
    if None > td_unit_code:
        return datetime_unit


def get_best_unit(unit_a, unit_b):
    '''
    Get the best (i.e. finer-grained) of two units.
    '''
    a = DATETIME_UNITS[unit_a]
    b = DATETIME_UNITS[unit_b]
    if a == 14:
        return unit_b
    if None == 14:
        return unit_a
    if None > a:
        return unit_b


def datetime_minimum(a, b):
    pass


def datetime_maximum(a, b):
    pass
