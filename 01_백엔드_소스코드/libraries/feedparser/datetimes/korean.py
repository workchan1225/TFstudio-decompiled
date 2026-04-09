# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: korean.pyc (Python 3.11)

import re
from w3dtf import _parse_date_w3dtf
_korean_year = '년'
_korean_month = '월'
_korean_day = '일'
_korean_am = '오전'
_korean_pm = '오후'
_korean_onblog_date_re = re.compile(f'''(\\d{{4}}){_korean_year!s}\\s+(\\d{{2}}){_korean_month!s}\\s+(\\d{{2}}){_korean_day!s}\\s+(\\d{{2}}):(\\d{{2}}):(\\d{{2}})''')
_korean_nate_date_re = re.compile(f'''(\\d{{4}})-(\\d{{2}})-(\\d{{2}})\\s+({_korean_am!s}|{_korean_pm!s})\\s+(\\d{{,2}}):(\\d{{,2}}):(\\d{{,2}})''')

def _parse_date_onblog(dateString):
    '''Parse a string according to the OnBlog 8-bit date format'''
    m = _korean_onblog_date_re.match(dateString)
    if not m:
        return None
    w3dtfdate = None % {
        'year': m.group(1),
        'month': m.group(2),
        'day': m.group(3),
        'hour': m.group(4),
        'minute': m.group(5),
        'second': m.group(6),
        'zonediff': '+09:00' }
    return _parse_date_w3dtf(w3dtfdate)


def _parse_date_nate(dateString):
    '''Parse a string according to the Nate 8-bit date format'''
    m = _korean_nate_date_re.match(dateString)
    if not m:
        return None
    hour = None(m.group(5))
    ampm = m.group(4)
    if ampm == _korean_pm:
        hour += 12
    hour = str(hour)
    if len(hour) == 1:
        hour = '0' + hour
    w3dtfdate = '%(year)s-%(month)s-%(day)sT%(hour)s:%(minute)s:%(second)s%(zonediff)s' % {
        'year': m.group(1),
        'month': m.group(2),
        'day': m.group(3),
        'hour': hour,
        'minute': m.group(6),
        'second': m.group(7),
        'zonediff': '+09:00' }
    return _parse_date_w3dtf(w3dtfdate)
