# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: debug.pyc (Python 3.11)

import logging
import sys
from pyasn1 import __version__
from pyasn1 import error
__all__ = [
    'Debug',
    'setLogger',
    'hexdump']
DEBUG_NONE = 0
DEBUG_ENCODER = 1
DEBUG_DECODER = 2
DEBUG_ALL = 65535
FLAG_MAP = {
    'none': DEBUG_NONE,
    'encoder': DEBUG_ENCODER,
    'decoder': DEBUG_DECODER,
    'all': DEBUG_ALL }
LOGGEE_MAP = { }

class Printer(object):
    
    def __init__(self, logger, handler, formatter = (None, None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, msg):
        self._Printer__logger.debug(msg)

    
    def __str__(self):
        return '<python logging>'



class Debug(object):
    defaultPrinter = Printer()
    
    def __init__(self, *flags, **options):
