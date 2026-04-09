# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

from __future__ import annotations
import importlib.util as importlib
import os
import sys
import typing as t
from datetime import datetime
from functools import lru_cache
from functools import update_wrapper
import werkzeug.utils as werkzeug
from werkzeug.exceptions import abort as _wz_abort
from werkzeug.utils import redirect as _wz_redirect
from globals import _cv_request
from globals import current_app
from globals import request
from globals import request_ctx
from globals import session
from signals import message_flashed
if t.TYPE_CHECKING:
    from werkzeug.wrappers import Response as BaseResponse
    from wrappers import Response

def get_debug_flag():
