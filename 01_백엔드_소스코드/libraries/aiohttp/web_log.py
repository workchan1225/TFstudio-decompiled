# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_log.pyc (Python 3.11)

import datetime
import functools
import logging
import os
import re
import time as time_mod
from collections import namedtuple
from typing import Any, Callable, Dict, Iterable, List, Tuple
from abc import AbstractAccessLogger
from web_request import BaseRequest
from web_response import StreamResponse
KeyMethod = namedtuple('KeyMethod', 'key method')

class AccessLogger(AbstractAccessLogger):
    pass
# WARNING: Decompyle incomplete
