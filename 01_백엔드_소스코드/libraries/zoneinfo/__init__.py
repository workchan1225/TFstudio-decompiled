# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

__all__ = [
    'ZoneInfo',
    'reset_tzpath',
    'available_timezones',
    'TZPATH',
    'ZoneInfoNotFoundError',
    'InvalidTZPathWarning']
from  import _tzpath
from _common import ZoneInfoNotFoundError

try:
    from _zoneinfo import ZoneInfo
except ImportError:
    from _zoneinfo import ZoneInfo

reset_tzpath = _tzpath.reset_tzpath
available_timezones = _tzpath.available_timezones
InvalidTZPathWarning = _tzpath.InvalidTZPathWarning

def __getattr__(name):
    if name == 'TZPATH':
        return _tzpath.TZPATH
    raise None(f'''module {__name__!r} has no attribute {name!r}''')


def __dir__():
    return sorted(list(globals()) + [
        'TZPATH'])
