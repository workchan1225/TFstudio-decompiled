# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: handlers.pyc (Python 3.11)

'''Base classes for server/gateway implementations'''
from util import FileWrapper, guess_scheme, is_hop_by_hop
from headers import Headers
import sys
import os
import time
__all__ = [
    'BaseHandler',
    'SimpleHandler',
    'BaseCGIHandler',
    'CGIHandler',
    'IISCGIHandler',
    'read_environ']
_weekdayname = [
    'Mon',
    'Tue',
    'Wed',
    'Thu',
    'Fri',
    'Sat',
    'Sun']
_monthname = [
    None,
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec']

def format_date_time(timestamp):
    (year, month, day, hh, mm, ss, wd, y, z) = time.gmtime(timestamp)
    return '%s, %02d %3s %4d %02d:%02d:%02d GMT' % (_weekdayname[wd], day, _monthname[month], year, hh, mm, ss)

_is_request = {
    'HTTPS',
    'AUTH_TYPE',
    'PATH_INFO',
    'REMOTE_USER',
    'SCRIPT_NAME',
    'CONTENT_TYPE',
    'QUERY_STRING',
    'REMOTE_IDENT',
    'CONTENT_LENGTH',
    'REQUEST_METHOD'}.__contains__

def _needs_transcode(k):
