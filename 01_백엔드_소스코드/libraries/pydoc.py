# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pydoc.pyc (Python 3.11)

'''Generate Python documentation in HTML or text for interactive use.

At the Python interactive prompt, calling help(thing) on a Python object
documents the object, and calling help() starts up an interactive
help session.

Or, at the shell command line outside of Python:

Run "pydoc <name>" to show documentation on something.  <name> may be
the name of a function, module, package, or a dotted reference to a
class or function within a module or module in a package.  If the
argument contains a path segment delimiter (e.g. slash on Unix,
backslash on Windows) it is treated as the path to a Python source file.

Run "pydoc -k <keyword>" to search for a keyword in the synopsis lines
of all available modules.

Run "pydoc -n <hostname>" to start an HTTP server with the given
hostname (default: localhost) on the local machine.

Run "pydoc -p <port>" to start an HTTP server on the given port on the
local machine.  Port number 0 can be used to get an arbitrary unused port.

Run "pydoc -b" to start an HTTP server on an arbitrary unused port and
open a web browser to interactively browse documentation.  Combine with
the -n and -p options to control the hostname and port used.

Run "pydoc -w <name>" to write out the HTML documentation for a module
to a file named "<name>.html".

Module docs for core modules are assumed to be in

    https://docs.python.org/X.Y/library/

This can be overridden by setting the PYTHONDOCS environment variable
to a different URL or to a local directory containing the Library
Reference Manual pages.
'''
__all__ = [
    'help']
__author__ = 'Ka-Ping Yee <ping@lfw.org>'
__date__ = '26 February 2001'
__credits__ = 'Guido van Rossum, for an excellent programming language.\nTommy Burnette, the original creator of manpy.\nPaul Prescod, for all his work on onlinehelp.\nRichard Chamberlain, for the first implementation of textdoc.\n'
import __future__
import builtins
import importlib._bootstrap as importlib
import importlib._bootstrap_external as importlib
import importlib.machinery as importlib
import importlib.util as importlib
import inspect
import io
import os
import pkgutil
import platform
import re
import sys
import sysconfig
import time
import tokenize
import urllib.parse as urllib
import warnings
from collections import deque
from reprlib import Repr
from traceback import format_exception_only

def pathdirs():
    '''Convert sys.path into a list of absolute, existing, unique paths.'''
    dirs = []
    normdirs = []
    for dir in sys.path:
        if not dir:
            dir = os.path.abspath('.')
            normdir = os.path.normcase(dir)
            if normdir not in normdirs and os.path.isdir(dir):
                dirs.append(dir)
                normdirs.append(normdir)
        return dirs


def _findclass(func):
    cls = sys.modules.get(func.__module__)
# WARNING: Decompyle incomplete


def _finddoc(obj):
    if inspect.ismethod(obj):
        name = obj.__func__.__name__
        self = obj.__self__
        if inspect.isclass(self) and getattr(getattr(self, name, None), '__func__') is obj.__func__:
            cls = self
        else:
            cls = self.__class__
# WARNING: Decompyle incomplete


def _getowndoc(obj):
    '''Get the documentation string for an object if it is not
    inherited from its class.'''
    pass
# WARNING: Decompyle incomplete


def _getdoc(object):
    '''Get the documentation string for an object.

    All tabs are expanded to spaces.  To clean up docstrings that are
    indented to line up with blocks of code, any whitespace than can be
    uniformly removed from the second line onwards is removed.'''
    doc = _getowndoc(object)
# WARNING: Decompyle incomplete


def getdoc(object):
