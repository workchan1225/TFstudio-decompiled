# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: worker.pyc (Python 3.11)

'''Async gunicorn worker for aiohttp.web'''
import asyncio
import inspect
import os
import re
import signal
import sys
from types import FrameType
from typing import TYPE_CHECKING, Any, Optional
from gunicorn.config import AccessLogFormat as GunicornAccessLogFormat
from gunicorn.workers import base
from aiohttp import web
from helpers import set_result
from web_app import Application
from web_log import AccessLogger
if TYPE_CHECKING:
    import ssl
    SSLContext = ssl.SSLContext
else:
    
    try:
        import ssl
        SSLContext = ssl.SSLContext
    except ImportError:
        ssl = None
        SSLContext = object

    __all__ = ('GunicornWebWorker', 'GunicornUVLoopWebWorker')
    
    class GunicornWebWorker(base.Worker):
        pass
    # WARNING: Decompyle incomplete

    
    class GunicornUVLoopWebWorker(GunicornWebWorker):
        pass
    # WARNING: Decompyle incomplete

    return None
