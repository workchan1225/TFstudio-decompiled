# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import logging

try:
    from logging import NullHandler
except ImportError:
    
    class NullHandler(logging.Handler):
        
        def emit(self, record):
            pass



logging.getLogger(__name__).addHandler(NullHandler())
