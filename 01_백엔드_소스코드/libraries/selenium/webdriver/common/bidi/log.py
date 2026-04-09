# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: log.pyc (Python 3.11)

from __future__ import annotations
from dataclasses import dataclass
from typing import Any

class LogEntryAdded:
    event_class = 'log.entryAdded'
    from_json = (lambda cls = None, json = None: if json['type'] == 'console':
ConsoleLogEntry.from_json(json)if None['type'] == 'javascript':
JavaScriptLogEntry.from_json(json))()

ConsoleLogEntry = <NODE:12>()
JavaScriptLogEntry = <NODE:12>()

class LogLevel:
    '''Represents log level.'''
    DEBUG = 'debug'
    INFO = 'info'
    WARN = 'warn'
    ERROR = 'error'
