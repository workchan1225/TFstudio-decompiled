# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pywintypes.pyc (Python 3.11)

''' A module which supports common Windows types. '''
import contextlib
import collections
import time
from datetime import datetime as _datetime

class error(Exception):
    
    def __init__(self, *args, **kw):
        nargs = len(args)
        if nargs > 0:
            self.winerror = args[0]
        else:
            self.winerror = None
        if nargs > 1:
            self.funcname = args[1]
        else:
            self.funcname = None
        if nargs > 2:
            self.strerror = args[2]
        else:
            self.strerror = None
    # WARNING: Decompyle incomplete


pywin32error = (lambda : pass# WARNING: Decompyle incomplete
)()

class datetime(_datetime):
    
    def Format(self, fmt = ('%c',)):
        return self.strftime(fmt)



def Time(value):
    if isinstance(value, datetime):
        return value
    if None(value, 'timetuple'):
        timetuple = value.timetuple()
        return datetime.fromtimestamp(time.mktime(timetuple))
    if None(value, collections.abc.Sequence):
        time_value = time.mktime(value[:9])
        if len(value) == 10:
            time_value += value[9] / 1000
        return datetime.fromtimestamp(time_value)
    
    try:
        return datetime.fromtimestamp(value)
    except OSError:
        error = None
        if error.errno == 22:
            raise ValueError(error.strerror)
        raise 
        error = None
        del error
