# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bottle.pyc (Python 3.11)

from __future__ import print_function
import sys
__author__ = 'Marcel Hellkamp'
__version__ = '0.13.4'
__license__ = 'MIT'

def _cli_parse(args):
    ArgumentParser = ArgumentParser
    import argparse
    parser = ArgumentParser(prog = args[0], usage = '%(prog)s [options] package.module:app')
    opt = parser.add_argument
    opt('--version', action = 'store_true', help = 'show version number.')
    opt('-b', '--bind', metavar = 'ADDRESS', help = 'bind socket to ADDRESS.')
    opt('-s', '--server', default = 'wsgiref', help = 'use SERVER as backend.')
    opt('-p', '--plugin', action = 'append', help = 'install additional plugin/s.')
    opt('-c', '--conf', action = 'append', metavar = 'FILE', help = 'load config values from FILE.')
    opt('-C', '--param', action = 'append', metavar = 'NAME=VALUE', help = 'override config values.')
    opt('--debug', action = 'store_true', help = 'start server in debug mode.')
    opt('--reload', action = 'store_true', help = 'auto-reload on file changes.')
    opt('app', help = 'WSGI app entry point.', nargs = '?')
    cli_args = parser.parse_args(args[1:])
    return (cli_args, parser)


def _cli_patch(cli_args):
    (parsed_args, _) = _cli_parse(cli_args)
    opts = parsed_args
    if opts.server:
        if opts.server.startswith('gevent'):
            import gevent.monkey as gevent
            gevent.monkey.patch_all()
            return None
        if None.server.startswith('eventlet'):
            import eventlet
            eventlet.monkey_patch()
            return None
        return None

if __name__ == '__main__':
    _cli_patch(sys.argv)
import base64
import calendar
import email.utils as email
import functools
import hmac
import itertools
import mimetypes
import os
import re
import tempfile
import threading
import time
import warnings
import weakref
import hashlib
from types import FunctionType
from datetime import date as datedate, datetime, timedelta
from tempfile import NamedTemporaryFile
from traceback import format_exc, print_exc
from unicodedata import normalize

try:
    from ujson import dumps as json_dumps, loads as json_lds
except ImportError:
    from json import dumps as json_dumps, loads as json_lds

py = sys.version_info
py3k = py.major > 2

def tob(s, enc = ('utf8',)):
    if isinstance(s, unicode):
        return s.encode(enc)
# WARNING: Decompyle incomplete


def touni(s, enc, err = ('utf8', 'strict')):
    if isinstance(s, bytes):
        return s.decode(enc, err)
# WARNING: Decompyle incomplete

tonat = touni if py3k else tob

def _stderr(*args):
    pass
# WARNING: Decompyle incomplete


def update_wrapper(wrapper, wrapped, *a, **ka):
    pass
# WARNING: Decompyle incomplete


def depr(major, minor, cause, fix, stacklevel = (3,)):
    text = 'Warning: Use of deprecated feature or API. (Deprecated in Bottle-%d.%d)\nCause: %s\nFix: %s\n' % (major, minor, cause, fix)
    if DEBUG == 'strict':
        raise DeprecationWarning(text)
    warnings.warn(text, DeprecationWarning, stacklevel = stacklevel)
    return DeprecationWarning(text)


def makelist(data):
    if isinstance(data, (tuple, list, set, dict)):
        return list(data)
    if None:
        return [
            data]


class DictProperty(object):
    ''' Property that maps to a key in a local dict-like attribute. '''
    
    def __init__(self, attr, key, read_only = (None, False)):
        self.attr, self.key, self.read_only = attr, key, read_only

    
    def __call__(self, func):
