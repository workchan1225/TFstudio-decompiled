# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: inspect.pyc (Python 3.11)

"""Get useful information from live Python objects.

This module encapsulates the interface provided by the internal special
attributes (co_*, im_*, tb_*, etc.) in a friendlier fashion.
It also provides some help for examining source code and class layout.

Here are some of the useful functions provided by this module:

    ismodule(), isclass(), ismethod(), isfunction(), isgeneratorfunction(),
        isgenerator(), istraceback(), isframe(), iscode(), isbuiltin(),
        isroutine() - check object types
    getmembers() - get members of an object that satisfy a given condition

    getfile(), getsourcefile(), getsource() - find an object's source code
    getdoc(), getcomments() - get documentation on an object
    getmodule() - determine the module that an object came from
    getclasstree() - arrange classes so as to represent their hierarchy

    getargvalues(), getcallargs() - get info about function arguments
    getfullargspec() - same, with support for Python 3 features
    formatargvalues() - format an argument spec
    getouterframes(), getinnerframes() - get info about frames
    currentframe() - get the current stack frame
    stack(), trace() - get info about frames on the stack or in a traceback

    signature() - get a Signature object for the callable

    get_annotations() - safely compute an object's annotations
"""
__author__ = ('Ka-Ping Yee <ping@lfw.org>', 'Yury Selivanov <yselivanov@sprymix.com>')
__all__ = [
    'ArgInfo',
    'Arguments',
    'Attribute',
    'BlockFinder',
    'BoundArguments',
    'CORO_CLOSED',
    'CORO_CREATED',
    'CORO_RUNNING',
    'CORO_SUSPENDED',
    'CO_ASYNC_GENERATOR',
    'CO_COROUTINE',
    'CO_GENERATOR',
    'CO_ITERABLE_COROUTINE',
    'CO_NESTED',
    'CO_NEWLOCALS',
    'CO_NOFREE',
    'CO_OPTIMIZED',
    'CO_VARARGS',
    'CO_VARKEYWORDS',
    'ClassFoundException',
    'ClosureVars',
    'EndOfBlock',
    'FrameInfo',
    'FullArgSpec',
    'GEN_CLOSED',
    'GEN_CREATED',
    'GEN_RUNNING',
    'GEN_SUSPENDED',
    'Parameter',
    'Signature',
    'TPFLAGS_IS_ABSTRACT',
    'Traceback',
    'classify_class_attrs',
    'cleandoc',
    'currentframe',
    'findsource',
    'formatannotation',
    'formatannotationrelativeto',
    'formatargvalues',
    'get_annotations',
    'getabsfile',
    'getargs',
    'getargvalues',
    'getattr_static',
    'getblock',
    'getcallargs',
    'getclasstree',
    'getclosurevars',
    'getcomments',
    'getcoroutinelocals',
    'getcoroutinestate',
    'getdoc',
    'getfile',
    'getframeinfo',
    'getfullargspec',
    'getgeneratorlocals',
    'getgeneratorstate',
    'getinnerframes',
    'getlineno',
    'getmembers',
    'getmembers_static',
    'getmodule',
    'getmodulename',
    'getmro',
    'getouterframes',
    'getsource',
    'getsourcefile',
    'getsourcelines',
    'indentsize',
    'isabstract',
    'isasyncgen',
    'isasyncgenfunction',
    'isawaitable',
    'isbuiltin',
    'isclass',
    'iscode',
    'iscoroutine',
    'iscoroutinefunction',
    'isdatadescriptor',
    'isframe',
    'isfunction',
    'isgenerator',
    'isgeneratorfunction',
    'isgetsetdescriptor',
    'ismemberdescriptor',
    'ismethod',
    'ismethoddescriptor',
    'ismethodwrapper',
    'ismodule',
    'isroutine',
    'istraceback',
    'signature',
    'stack',
    'trace',
    'unwrap',
    'walktree']
import abc
import ast
import dis
import collections.abc as collections
import enum
import importlib.machinery as importlib
import itertools
import linecache
import os
import re
import sys
import tokenize
import token
import types
import functools
import builtins
from keyword import iskeyword
from operator import attrgetter
from collections import namedtuple, OrderedDict
mod_dict = globals()
for k, v in dis.COMPILER_FLAG_NAMES.items():
    mod_dict['CO_' + v] = k
    del k
    del v
    del mod_dict
    TPFLAGS_IS_ABSTRACT = 1048576
    
    def get_annotations(obj = None, *, globals, locals, eval_str):
        '''Compute the annotations dict for an object.

    obj may be a callable, class, or module.
    Passing in an object of any other type raises TypeError.

    Returns a dict.  get_annotations() returns a new dict every time
    it\'s called; calling it twice on the same object will return two
    different but equivalent dicts.

    This function handles several details for you:

      * If eval_str is true, values of type str will
        be un-stringized using eval().  This is intended
        for use with stringized annotations
        ("from __future__ import annotations").
      * If obj doesn\'t have an annotations dict, returns an
        empty dict.  (Functions and methods always have an
        annotations dict; classes, modules, and other types of
        callables may not.)
      * Ignores inherited annotations on classes.  If a class
        doesn\'t have its own annotations dict, returns an empty dict.
      * All accesses to object members and dict values are done
        using getattr() and dict.get() for safety.
      * Always, always, always returns a freshly-created dict.

    eval_str controls whether or not values of type str are replaced
    with the result of calling eval() on those values:

      * If eval_str is true, eval() is called on values of type str.
      * If eval_str is false (the default), values of type str are unchanged.

    globals and locals are passed in to eval(); see the documentation
    for eval() for more information.  If either globals or locals is
    None, this function may replace that value with a context-specific
    default, contingent on type(obj):

      * If obj is a module, globals defaults to obj.__dict__.
      * If obj is a class, globals defaults to
        sys.modules[obj.__module__].__dict__ and locals
        defaults to the obj class namespace.
      * If obj is a callable, globals defaults to obj.__globals__,
        although if obj is a wrapped function (using
        functools.update_wrapper()) it is first unwrapped.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    def ismodule(object):
        '''Return true if the object is a module.

    Module objects provide these attributes:
        __cached__      pathname to byte compiled file
        __doc__         documentation string
        __file__        filename (missing for built-in modules)'''
        return isinstance(object, types.ModuleType)

    
    def isclass(object):
        '''Return true if the object is a class.

    Class objects provide these attributes:
        __doc__         documentation string
        __module__      name of module in which this class was defined'''
        return isinstance(object, type)

    
    def ismethod(object):
        '''Return true if the object is an instance method.

    Instance method objects provide these attributes:
        __doc__         documentation string
        __name__        name with which this method was defined
        __func__        function object containing implementation of method
        __self__        instance to which this method is bound'''
        return isinstance(object, types.MethodType)

    
    def ismethoddescriptor(object):
