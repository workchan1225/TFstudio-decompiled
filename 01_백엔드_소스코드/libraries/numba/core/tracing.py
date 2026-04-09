# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tracing.pyc (Python 3.11)

import inspect
import logging
import sys
import threading
from functools import wraps
from itertools import chain
from numba.core import config

class TLS(threading.local):
    '''Use a subclass to properly initialize the TLS variables in all threads.'''
    
    def __init__(self):
        self.tracing = False
        self.indent = 0


tls = TLS()

def find_function_info(func, spec, args):
    '''Return function meta-data in a tuple.

    (name, type)'''
    module = getattr(func, '__module__', None)
    name = getattr(func, '__name__', None)
    self = getattr(func, '__self__', None)
    cname = None
    if self:
        cname = self.__name__
    elif len(spec.args) and spec.args[0] == 'self':
        cname = args[0].__class__.__name__
    elif len(spec.args) and spec.args[0] == 'cls':
        cname = args[0].__name__
    if name:
        qname = []
        if module and module != '__main__':
            qname.append(module)
            qname.append('.')
        if cname:
            qname.append(cname)
            qname.append('.')
        qname.append(name)
        name = ''.join(qname)
    return (name, None)


def chop(value):
    MAX_SIZE = 320
    s = repr(value)
    if len(s) > MAX_SIZE:
        return s[:MAX_SIZE] + '...' + s[-1]


def create_events(fname, spec, args, kwds):
    pass
# WARNING: Decompyle incomplete


def dotrace(*args, **kwds):
