# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cloudpickle.pyc (Python 3.11)

'''Pickler class to extend the standard pickle.Pickler functionality

The main objective is to make it natural to perform distributed computing on
clusters (such as PySpark, Dask, Ray...) with interactively defined code
(functions, classes, ...) written in notebooks or console.

In particular this pickler adds the following features:
- serialize interactively-defined or locally-defined functions, classes,
  enums, typevars, lambdas and nested functions to compiled byte code;
- deal with some other non-serializable objects in an ad-hoc manner where
  applicable.

This pickler is therefore meant to be used for the communication between short
lived Python processes running the same version of Python and libraries. In
particular, it is not meant to be used for long term storage of Python objects.

It does not include an unpickler, as standard Python unpickling suffices.

This module was extracted from the `cloud` package, developed by `PiCloud, Inc.
<https://web.archive.org/web/20140626004012/http://www.picloud.com/>`_.

Copyright (c) 2012-now, CloudPickle developers and contributors.
Copyright (c) 2012, Regents of the University of California.
Copyright (c) 2009 `PiCloud, Inc. <https://web.archive.org/web/20140626004012/http://www.picloud.com/>`_.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the University of California, Berkeley nor the
      names of its contributors may be used to endorse or promote
      products derived from this software without specific prior written
      permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
import _collections_abc
from collections import ChainMap, OrderedDict
import abc
import builtins
import copyreg
import dataclasses
import dis
from enum import Enum
import io
import itertools
import logging
import opcode
import pickle
from pickle import _getattribute as _pickle_getattribute
import platform
import struct
import sys
import threading
import types
import typing
import uuid
import warnings
import weakref
from types import CellType
DEFAULT_PROTOCOL = pickle.HIGHEST_PROTOCOL
_PICKLE_BY_VALUE_MODULES = set()
_DYNAMIC_CLASS_TRACKER_BY_CLASS = weakref.WeakKeyDictionary()
_DYNAMIC_CLASS_TRACKER_BY_ID = weakref.WeakValueDictionary()
_DYNAMIC_CLASS_TRACKER_LOCK = threading.Lock()
PYPY = platform.python_implementation() == 'PyPy'
builtin_code_type = None
if PYPY:
    builtin_code_type = type(float.__new__.__code__)
_extract_code_globals_cache = weakref.WeakKeyDictionary()

def _get_or_create_tracker_id(class_def):
    _DYNAMIC_CLASS_TRACKER_LOCK
    class_tracker_id = _DYNAMIC_CLASS_TRACKER_BY_CLASS.get(class_def)
# WARNING: Decompyle incomplete


def _lookup_class_or_track(class_tracker_id, class_def):
    pass
# WARNING: Decompyle incomplete


def register_pickle_by_value(module):
    '''Register a module to make its functions and classes picklable by value.

    By default, functions and classes that are attributes of an importable
    module are to be pickled by reference, that is relying on re-importing
    the attribute from the module at load time.

    If `register_pickle_by_value(module)` is called, all its functions and
    classes are subsequently to be pickled by value, meaning that they can
    be loaded in Python processes where the module is not importable.

    This is especially useful when developing a module in a distributed
    execution environment: restarting the client Python process with the new
    source code is enough: there is no need to re-install the new version
    of the module on all the worker nodes nor to restart the workers.

    Note: this feature is considered experimental. See the cloudpickle
    README.md file for more details and limitations.
    '''
    if not isinstance(module, types.ModuleType):
        raise ValueError(f'''Input should be a module object, got {str(module)} instead''')
    if module.__name__ not in sys.modules:
        raise ValueError(f'''{module} was not imported correctly, have you used an `import` statement to access it?''')
    _PICKLE_BY_VALUE_MODULES.add(module.__name__)


def unregister_pickle_by_value(module):
    '''Unregister that the input module should be pickled by value.'''
    if not isinstance(module, types.ModuleType):
        raise ValueError(f'''Input should be a module object, got {str(module)} instead''')
    if module.__name__ not in _PICKLE_BY_VALUE_MODULES:
        raise ValueError(f'''{module} is not registered for pickle by value''')
    _PICKLE_BY_VALUE_MODULES.remove(module.__name__)


def list_registry_pickle_by_value():
    return _PICKLE_BY_VALUE_MODULES.copy()


def _is_registered_pickle_by_value(module):
    module_name = module.__name__
    if module_name in _PICKLE_BY_VALUE_MODULES:
        return True
    parent_name = module_name.rsplit('.', 1)[0]
    if parent_name == module_name:
        pass
    elif parent_name in _PICKLE_BY_VALUE_MODULES:
        return True
    module_name = parent_name
    continue
    return False

if sys.version_info >= (3, 14):
    
    def _getattribute(obj, name):
        return _pickle_getattribute(obj, name.split('.'))

else:
    
    def _getattribute(obj, name):
        return _pickle_getattribute(obj, name)[0]


def _whichmodule(obj, name):
    """Find the module an object belongs to.

    This function differs from ``pickle.whichmodule`` in two ways:
    - it does not mangle the cases where obj's module is __main__ and obj was
      not found in any module.
    - Errors arising during module introspection are ignored, as those errors
      are considered unwanted side effects.
    """
    module_name = getattr(obj, '__module__', None)
# WARNING: Decompyle incomplete


def _should_pickle_by_reference(obj, name = (None,)):
    '''Test whether an function or a class should be pickled by reference

    Pickling by reference means by that the object (typically a function or a
    class) is an attribute of a module that is assumed to be importable in the
    target Python environment. Loading will therefore rely on importing the
    module and then calling `getattr` on it to access the function or class.

    Pickling by reference is the only option to pickle functions and classes
    in the standard library. In cloudpickle the alternative option is to
    pickle by value (for instance for interactively or locally defined
    functions and classes or for attributes of modules that have been
    explicitly registered to be pickled by value.
    '''
    pass
# WARNING: Decompyle incomplete


def _lookup_module_and_qualname(obj, name = (None,)):
    pass
# WARNING: Decompyle incomplete


def _extract_code_globals(co):
    '''Find all globals names read or written to by codeblock co.'''
    out_names = _extract_code_globals_cache.get(co)
# WARNING: Decompyle incomplete


def _find_imported_submodules(code, top_level_dependencies):
    """Find currently imported submodules used by a function.

    Submodules used by a function need to be detected and referenced for the
    function to work correctly at depickling time. Because submodules can be
    referenced as attribute of their parent package (``package.submodule``), we
    need a special introspection technique that does not rely on GLOBAL-related
    opcodes to find references of them in a code object.

    Example:
    ```
    import concurrent.futures
    import cloudpickle
    def func():
        x = concurrent.futures.ThreadPoolExecutor
    if __name__ == '__main__':
        cloudpickle.dumps(func)
    ```
    The globals extracted by cloudpickle in the function's state include the
    concurrent package, but not its submodule (here, concurrent.futures), which
    is the module used by func. Find_imported_submodules will detect the usage
    of concurrent.futures. Saving this module alongside with func will ensure
    that calling func once depickled does not fail due to concurrent.futures
    not being imported
    """
    subimports = []
# WARNING: Decompyle incomplete

STORE_GLOBAL = opcode.opmap['STORE_GLOBAL']
DELETE_GLOBAL = opcode.opmap['DELETE_GLOBAL']
LOAD_GLOBAL = opcode.opmap['LOAD_GLOBAL']
GLOBAL_OPS = (STORE_GLOBAL, DELETE_GLOBAL, LOAD_GLOBAL)
HAVE_ARGUMENT = dis.HAVE_ARGUMENT
EXTENDED_ARG = dis.EXTENDED_ARG
_BUILTIN_TYPE_NAMES = { }
for k, v in types.__dict__.items():
    if type(v) is type:
        _BUILTIN_TYPE_NAMES[v] = k
    
    def _builtin_type(name):
        if name == 'ClassType':
            return type
        return None(types, name)

    
    def _walk_global_ops(code):
        '''Yield referenced name for global-referencing instructions in code.'''
        pass
    # WARNING: Decompyle incomplete

    
    def _extract_class_dict(cls):
        '''Retrieve a copy of the dict of a class without the inherited method.'''
        pass
    # WARNING: Decompyle incomplete

    
    def is_tornado_coroutine(func):
        '''Return whether `func` is a Tornado coroutine function.

    Running coroutines are not supported.
    '''
        warnings.warn('is_tornado_coroutine is deprecated in cloudpickle 3.0 and will be removed in cloudpickle 4.0. Use tornado.gen.is_coroutine_function directly instead.', category = DeprecationWarning)
        if 'tornado.gen' not in sys.modules:
            return False
        gen = None.modules['tornado.gen']
        if not hasattr(gen, 'is_coroutine_function'):
            return False
        return None.is_coroutine_function(func)

    
    def subimport(name):
        __import__(name)
        return sys.modules[name]

    
    def dynamic_subimport(name, vars):
        mod = types.ModuleType(name)
        mod.__dict__.update(vars)
        mod.__dict__['__builtins__'] = builtins.__dict__
        return mod

    
    def _get_cell_contents(cell):
        
        try:
            return cell.cell_contents
        except ValueError:
            return 


    
    def instance(cls):
        '''Create a new instance of a class.

    Parameters
    ----------
    cls : type
        The class to create an instance of.

    Returns
    -------
    instance : cls
        A new instance of ``cls``.
    '''
        return cls()

    _empty_cell_value = <NODE:12>()
    
    def _make_function(code, globals, name, argdefs, closure):
        globals['__builtins__'] = __builtins__
        return types.FunctionType(code, globals, name, argdefs, closure)

    
    def _make_empty_cell():
        pass
    # WARNING: Decompyle incomplete

    
    def _make_cell(value = (_empty_cell_value,)):
        cell = _make_empty_cell()
        if value is not _empty_cell_value:
            cell.cell_contents = value
        return cell

    
    def _make_skeleton_class(type_constructor, name, bases, type_kwargs, class_tracker_id, extra):
        '''Build dynamic class with an empty __dict__ to be filled once memoized

    If class_tracker_id is not None, try to lookup an existing class definition
    matching that id. If none is found, track a newly reconstructed class
    definition under that id so that other instances stemming from the same
    class id will also reuse this class definition.

    The "extra" variable is meant to be a dict (or None) that can be used for
    forward compatibility shall the need arise.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    def _make_skeleton_enum(bases, name, qualname, members, module, class_tracker_id, extra):
        '''Build dynamic enum with an empty __dict__ to be filled once memoized

    The creation of the enum class is inspired by the code of
    EnumMeta._create_.

    If class_tracker_id is not None, try to lookup an existing enum definition
    matching that id. If none is found, track a newly reconstructed enum
    definition under that id so that other instances stemming from the same
    class id will also reuse this enum definition.

    The "extra" variable is meant to be a dict (or None) that can be used for
    forward compatibility shall the need arise.
    '''
        enum_base = bases[-1]
        metacls = enum_base.__class__
        classdict = metacls.__prepare__(name, bases)
        for member_name, member_value in members.items():
            classdict[member_name] = member_value
            enum_class = metacls.__new__(metacls, name, bases, classdict)
            enum_class.__module__ = module
            enum_class.__qualname__ = qualname
            return _lookup_class_or_track(class_tracker_id, enum_class)

    
    def _make_typevar(name, bound, constraints, covariant, contravariant, class_tracker_id):
        pass
    # WARNING: Decompyle incomplete

    
    def _decompose_typevar(obj):
        return (obj.__name__, obj.__bound__, obj.__constraints__, obj.__covariant__, obj.__contravariant__, _get_or_create_tracker_id(obj))

    
    def _typevar_reduce(obj):
        module_and_name = _lookup_module_and_qualname(obj, name = obj.__name__)
    # WARNING: Decompyle incomplete

    
    def _get_bases(typ):
        if '__orig_bases__' in getattr(typ, '__dict__', { }):
            bases_attr = '__orig_bases__'
        else:
            bases_attr = '__bases__'
        return getattr(typ, bases_attr)

    
    def _make_dict_keys(obj, is_ordered = (False,)):
        if is_ordered:
            return OrderedDict.fromkeys(obj).keys()
        return None.fromkeys(obj).keys()

    
    def _make_dict_values(obj, is_ordered = (False,)):
