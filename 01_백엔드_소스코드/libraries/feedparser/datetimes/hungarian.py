# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hungarian.pyc (Python 3.11)

import re
from w3dtf import _parse_date_w3dtf
_hungarian_months = {
    'január': '01',
    'februári': '02',
    'március': '03',
    'április': '04',
    'máujus': '05',
    'június': '06',
    'július': '07',
    'augusztus': '08',
    'szeptember': '09',
    'október': '10',
    'november': '11',
    'december': '12' }
_hungarian_date_format_re = re.compile('(\\d{4})-([^-]+)-(\\d{,2})T(\\d{,2}):(\\d{2})([+-](\\d{,2}:\\d{2}))')

def _parse_date_hungarian(date_string):
    '''Parse a string according to a Hungarian 8-bit date format.'''
    m = _hungarian_date_format_re.match(date_string)
    if m or m.group(2) not in _hungarian_months:
        return None
    month = None[m.group(2)]
    day = m.group(3)
    if len(day) == 1:
        day = '0' + day
    hour = m.group(4)
    if len(hour) == 1:
        hour = '0' + hour
    w3dtfdate = '%(year)s-%(month)s-%(day)sT%(hour)s:%(minute)s%(zonediff)s' % {
        'year': m.group(1),
        'month': month,
        'day': day,
        'hour': hour,
        'minute': m.group(5),
        'zonediff': m.group(6) }
    return _parse_date_w3dtf(w3dtfdate)
