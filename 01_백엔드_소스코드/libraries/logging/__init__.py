# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

"""
Logging package for Python. Based on PEP 282 and comments thereto in
comp.lang.python.

Copyright (C) 2001-2019 Vinay Sajip. All Rights Reserved.

To use, simply 'import logging' and log away!
"""
import sys
import os
import time
import io
import re
import traceback
import warnings
import weakref
import collections.abc as collections
from types import GenericAlias
from string import Template
from string import Formatter as StrFormatter
__all__ = [
    'BASIC_FORMAT',
    'BufferingFormatter',
    'CRITICAL',
    'DEBUG',
    'ERROR',
    'FATAL',
    'FileHandler',
    'Filter',
    'Formatter',
    'Handler',
    'INFO',
    'LogRecord',
    'Logger',
    'LoggerAdapter',
    'NOTSET',
    'NullHandler',
    'StreamHandler',
    'WARN',
    'WARNING',
    'addLevelName',
    'basicConfig',
    'captureWarnings',
    'critical',
    'debug',
    'disable',
    'error',
    'exception',
    'fatal',
    'getLevelName',
    'getLogger',
    'getLoggerClass',
    'info',
    'log',
    'makeLogRecord',
    'setLoggerClass',
    'shutdown',
    'warn',
    'warning',
    'getLogRecordFactory',
    'setLogRecordFactory',
    'lastResort',
    'raiseExceptions',
    'getLevelNamesMapping']
import threading
__author__ = 'Vinay Sajip <vinay_sajip@red-dove.com>'
__status__ = 'production'
__version__ = '0.5.1.2'
__date__ = '07 February 2010'
_startTime = time.time()
raiseExceptions = True
logThreads = True
logMultiprocessing = True
logProcesses = True
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
_levelToName = {
    NOTSET: 'NOTSET',
    DEBUG: 'DEBUG',
    INFO: 'INFO',
    WARNING: 'WARNING',
    ERROR: 'ERROR',
    CRITICAL: 'CRITICAL' }
_nameToLevel = {
    'CRITICAL': CRITICAL,
    'FATAL': FATAL,
    'ERROR': ERROR,
    'WARN': WARNING,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET }

def getLevelNamesMapping():
    return _nameToLevel.copy()


def getLevelName(level):
    """
    Return the textual or numeric representation of logging level 'level'.

    If the level is one of the predefined levels (CRITICAL, ERROR, WARNING,
    INFO, DEBUG) then you get the corresponding string. If you have
    associated levels with names using addLevelName then the name you have
    associated with 'level' is returned.

    If a numeric value corresponding to one of the defined levels is passed
    in, the corresponding string representation is returned.

    If a string representation of the level is passed in, the corresponding
    numeric value is returned.

    If no matching numeric or string value is passed in, the string
    'Level %s' % level is returned.
    """
    result = _levelToName.get(level)
# WARNING: Decompyle incomplete


def addLevelName(level, levelName):
    """
    Associate 'levelName' with 'level'.

    This is used when converting levels to text during message formatting.
    """
    _acquireLock()
    
    try:
        _levelToName[level] = levelName
        _nameToLevel[levelName] = level
        _releaseLock()
        return None
    except:
        _releaseLock()


if hasattr(sys, '_getframe'):
    
    currentframe = lambda : sys._getframe(1)
else:
    
    def currentframe():
        """Return the frame object for the caller's stack frame."""
        
        try:
            raise Exception
        except Exception:
            return 


_srcfile = os.path.normcase(addLevelName.__code__.co_filename)

def _is_internal_frame(frame):
