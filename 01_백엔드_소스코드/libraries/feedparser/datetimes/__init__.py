# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from asctime import _parse_date_asctime
from greek import _parse_date_greek
from hungarian import _parse_date_hungarian
from iso8601 import _parse_date_iso8601
from korean import _parse_date_onblog, _parse_date_nate
from perforce import _parse_date_perforce
from rfc822 import _parse_date_rfc822
from w3dtf import _parse_date_w3dtf
_date_handlers = []

def registerDateHandler(func):
    '''Register a date handler function (takes string, returns 9-tuple date in GMT)'''
    _date_handlers.insert(0, func)


def _parse_date(date_string):
    '''Parses a variety of date formats into a 9-tuple in GMT'''
    if not date_string:
        return None
    for handler in None:
        date9tuple = handler(date_string)
    except (KeyError, OverflowError, ValueError, AttributeError):
        continue
    if not date9tuple:
        continue
    if len(date9tuple) != 9:
        continue
    
    return None, date9tuple

registerDateHandler(_parse_date_onblog)
registerDateHandler(_parse_date_nate)
registerDateHandler(_parse_date_greek)
registerDateHandler(_parse_date_hungarian)
registerDateHandler(_parse_date_perforce)
registerDateHandler(_parse_date_asctime)
registerDateHandler(_parse_date_iso8601)
registerDateHandler(_parse_date_rfc822)
registerDateHandler(_parse_date_w3dtf)
