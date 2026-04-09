# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: perforce.pyc (Python 3.11)

import email._parseaddr as email
import re
import time

def _parse_date_perforce(date_string):
    '''parse a date in yyyy/mm/dd hh:mm:ss TTT format'''
    _my_date_pattern = re.compile('(\\w{,3}), (\\d{,4})/(\\d{,2})/(\\d{2}) (\\d{,2}):(\\d{2}):(\\d{2}) (\\w{,3})')
    m = _my_date_pattern.search(date_string)
# WARNING: Decompyle incomplete
