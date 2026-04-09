# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: logger.pyc (Python 3.11)

import logging
import os
from null_handler import NULLHandler
_default_log_level = os.environ.get('PYREADLINE_LOG', 'DEBUG')
LOGGER = logging.getLogger('PYREADLINE')
LOGGER.setLevel(_default_log_level)
LOGGER.propagate = False
LOGGER.addHandler(NULLHandler())
