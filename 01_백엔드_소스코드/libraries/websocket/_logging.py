# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _logging.pyc (Python 3.11)

import logging
_logger = logging.getLogger('websocket')

try:
    from logging import NullHandler
except ImportError:
    
    class NullHandler(logging.Handler):
        
        def emit(self = None, record = None):
            pass



_logger.addHandler(NullHandler())
_traceEnabled = False
__all__ = [
    'enableTrace',
    'dump',
    'error',
    'warning',
    'debug',
    'trace',
    'isEnabledForError',
    'isEnabledForDebug',
    'isEnabledForTrace']

def enableTrace(traceable = None, handler = None, level = None):
    '''
    Turn on/off the traceability.

    Parameters
    ----------
    traceable: bool
        If set to True, traceability is enabled.
    '''
    global _traceEnabled
    _traceEnabled = traceable
    if traceable:
        _logger.addHandler(handler)
        _logger.setLevel(getattr(logging, level))
        return None


def dump(title = None, message = None):
    if _traceEnabled:
        _logger.debug(f'''--- {title} ---''')
        _logger.debug(message)
        _logger.debug('-----------------------')
        return None


def error(msg = None):
    _logger.error(msg)


def warning(msg = None):
    _logger.warning(msg)


def debug(msg = None):
    _logger.debug(msg)


def info(msg = None):
    _logger.info(msg)


def trace(msg = None):
    if _traceEnabled:
        _logger.debug(msg)
        return None


def isEnabledForError():
    return _logger.isEnabledFor(logging.ERROR)


def isEnabledForDebug():
    return _logger.isEnabledFor(logging.DEBUG)


def isEnabledForTrace():
    return _traceEnabled
