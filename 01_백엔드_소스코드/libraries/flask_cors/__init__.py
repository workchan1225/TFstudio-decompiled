# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
    flask_cors
    ~~~~
    Flask-CORS is a simple extension to Flask allowing you to support cross
    origin resource sharing (CORS) using a simple decorator.

    :copyright: (c) 2016 by Cory Dolphin.
    :license: MIT, see LICENSE for more details.
'''
from decorator import cross_origin
from extension import CORS
from version import __version__
__all__ = [
    'CORS',
    'cross_origin']
import logging
from logging import NullHandler
rootlogger = logging.getLogger(__name__)
rootlogger.addHandler(NullHandler())
if rootlogger.level == logging.NOTSET:
    rootlogger.setLevel(logging.WARN)
    return None
