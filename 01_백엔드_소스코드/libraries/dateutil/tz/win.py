# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: win.pyc (Python 3.11)

'''
This module provides an interface to the native time zone data on Windows,
including :py:class:`datetime.tzinfo` implementations.

Attempting to import this module on a non-Windows platform will raise an
:py:obj:`ImportError`.
'''
import datetime
import struct
from six.moves import winreg
from six import text_type

try:
    import ctypes
    from ctypes import wintypes
except ValueError:
    raise ImportError('Running tzwin on non-Windows system')

from _common import tzrangebase
__all__ = [
    'tzwin',
    'tzwinlocal',
    'tzres']
ONEWEEK = datetime.timedelta(7)
TZKEYNAMENT = 'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Time Zones'
TZKEYNAME9X = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Time Zones'
TZLOCALKEYNAME = 'SYSTEM\\CurrentControlSet\\Control\\TimeZoneInformation'

def _settzkeyname():
    handle = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    
    try:
        winreg.OpenKey(handle, TZKEYNAMENT).Close()
        TZKEYNAME = TZKEYNAMENT
    except WindowsError:
        TZKEYNAME = TZKEYNAME9X

    handle.Close()
    return TZKEYNAME

TZKEYNAME = _settzkeyname()

class tzres(object):
    '''
    Class for accessing ``tzres.dll``, which contains timezone name related
    resources.

    .. versionadded:: 2.5.0
    '''
    p_wchar = ctypes.POINTER(wintypes.WCHAR)
    
    def __init__(self, tzres_loc = ('tzres.dll',)):
        user32 = ctypes.WinDLL('user32')
        user32.LoadStringW.argtypes = (wintypes.HINSTANCE, wintypes.UINT, wintypes.LPWSTR, ctypes.c_int)
        self.LoadStringW = user32.LoadStringW
        self._tzres = ctypes.WinDLL(tzres_loc)
        self.tzres_loc = tzres_loc

    
    def load_name(self, offset):
        """
        Load a timezone name from a DLL offset (integer).

        >>> from dateutil.tzwin import tzres
        >>> tzr = tzres()
        >>> print(tzr.load_name(112))
        'Eastern Standard Time'

        :param offset:
            A positive integer value referring to a string from the tzres dll.

        .. note::

            Offsets found in the registry are generally of the form
            ``@tzres.dll,-114``. The offset in this case is 114, not -114.

        """
        resource = self.p_wchar()
        lpBuffer = ctypes.cast(ctypes.byref(resource), wintypes.LPWSTR)
        nchar = self.LoadStringW(self._tzres._handle, offset, lpBuffer, 0)
        return resource[:nchar]

    
    def name_from_string(self, tzname_str):
        """
        Parse strings as returned from the Windows registry into the time zone
        name as defined in the registry.

        >>> from dateutil.tzwin import tzres
        >>> tzr = tzres()
        >>> print(tzr.name_from_string('@tzres.dll,-251'))
        'Dateline Daylight Time'
        >>> print(tzr.name_from_string('Eastern Standard Time'))
        'Eastern Standard Time'

        :param tzname_str:
            A timezone name string as returned from a Windows registry key.

        :return:
            Returns the localized timezone string from tzres.dll if the string
            is of the form `@tzres.dll,-offset`, else returns the input string.
        """
        if not tzname_str.startswith('@'):
            return tzname_str
        name_splt = None.split(',-')
        
        try:
            offset = int(name_splt[1])
        except:
            raise ValueError('Malformed timezone string.')

        return self.load_name(offset)



class tzwinbase(tzrangebase):
    """tzinfo class based on win32's timezones available in the registry."""
    
    def __init__(self):
        raise NotImplementedError('tzwinbase is an abstract base class')

    
    def __eq__(self, other):
