# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: context.pyc (Python 3.11)

from collections import defaultdict
from collections.abc import Sequence
import typing as _tp
import types as pytypes
import weakref
import threading
import contextlib
import operator
from numba.core import types, errors, config
from numba.core.typeconv import Conversion, rules
from numba.core.typing import templates
from numba.core.utils import order_by_target_specificity
from typeof import typeof, Purpose
from numba.core import utils

class Rating(object):
    __slots__ = ('promote', 'safe_convert', 'unsafe_convert')
    
    def __init__(self):
        self.promote = 0
        self.safe_convert = 0
        self.unsafe_convert = 0

    
    def astuple(self):
        '''Returns a tuple suitable for comparing with the worse situation
        start first.
        '''
        return (self.unsafe_convert, self.safe_convert, self.promote)

    
    def __add__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        rsum = None()
        rsum.promote = self.promote + other.promote
        rsum.safe_convert = self.safe_convert + other.safe_convert
        rsum.unsafe_convert = self.unsafe_convert + other.unsafe_convert
        return rsum



class CallStack(Sequence):
    '''
    A compile-time call stack
    '''
    
    def __init__(self):
        self._stack = []
        self._lock = threading.RLock()
        self._fail_cache = { }

    
    def __getitem__(self, index):
        '''
        Returns item in the stack where index=0 is the top and index=1 is
        the second item from the top.
        '''
        return self._stack[len(self) - index - 1]

    
    def __len__(self):
        return len(self._stack)

    register = (lambda self, target, typeinfer, func_id, args: pass# WARNING: Decompyle incomplete
)()
    
    def finditer(self, py_func):
        '''
        Yields frame that matches the function object starting from the top
        of stack.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def findfirst(self, py_func):
        '''
        Returns the first result from `.finditer(py_func)`; or None if no match.
        '''
        
        try:
            return next(self.finditer(py_func))
        except StopIteration:
            return None


    
    def match(self, py_func, args):
        '''
        Returns first function that matches *py_func* and the arguments types in
        *args*; or, None if no match.
        '''
        for frame in self.finditer(py_func):
            if frame.args == args:
                
                return None, frame
            return None

    
    def lookup_resolve_cache(self = None, func = None, args = contextlib.contextmanager, kws = ('return', '_ResolveCache')):
        '''Lookup resolution cache for the given function type and argument
        types.
        '''
        pass
    # WARNING: Decompyle incomplete



class _ResolveCache(object):
    _exc: _tp.Optional[BaseException] = '\n    A cache for function resolution result.\n    Currently only remember failed attempts.\n    '
    
    def __init__(self):
        self._status = 'unmarked'
        self._exc = None

    
    def mark_error(self = None, exc = None):
        '''Mark the function resolution as failed with an exception.'''
        self._status = 'error'
        self._exc = exc

    
    def mark_failed(self = None):
        '''Mark the function resolution as failed.'''
        self._status = 'failed'

    
    def replay_failure(self = None):
        '''Replay the failure if it has been marked as failed or error.'''
        if self._status == 'error':
            raise self._exc
    # WARNING: Decompyle incomplete

    
    def has_failed_previously(self = None):
        '''Return True if the function resolution has failed previously.'''
        return self._status in frozenset({'error', 'failed'})



class CallFrame(object):
    '''
    A compile-time call frame
    '''
    
    def __init__(self, target, typeinfer, func_id, args):
        self.typeinfer = typeinfer
        self.func_id = func_id
        self.args = args
        self.target = target
        self._inferred_retty = set()

    
    def __repr__(self):
        return 'CallFrame({}, {})'.format(self.func_id, self.args)

    
    def add_return_type(self, return_type):
        '''Add *return_type* to the list of inferred return-types.
        If there are too many, raise `TypingError`.
        '''
        RETTY_LIMIT = 16
        self._inferred_retty.add(return_type)
        if len(self._inferred_retty) >= RETTY_LIMIT:
            m = 'Return type of recursive function does not converge'
            raise errors.TypingError(m)



class BaseContext(object):
    '''A typing context for storing function typing constrain template.
    '''
    
    def __init__(self):
        self._registries = { }
        self._functions = defaultdict(list)
        self._attributes = defaultdict(list)
        self._globals = utils.UniqueDict()
        self.tm = rules.default_type_manager
        self.callstack = CallStack()
        self.init()

    
    def init(self):
        '''
        Initialize the typing context.  Can be overridden by subclasses.
        '''
        pass

    
    def refresh(self):
        '''
        Refresh context with new declarations from known registries.
        Useful for third-party extensions.
        '''
        self.load_additional_registries()
        self._load_builtins()

    
    def explain_function_type(self, func):
        '''
        Returns a string description of the type of a function
        '''
        desc = []
        defns = []
        param = False
        if isinstance(func, types.Callable):
            (sigs, param) = func.get_call_signatures()
            defns.extend(sigs)
        elif func in self._functions:
            for tpl in self._functions[func]:
                pass
        if defns:
            desc = [
                'Known signatures:']
            for sig in defns:
                desc.append(' * {0}'.format(sig))
                return '\n'.join(desc)

    
    def resolve_function_type(self, func, args, kws):
        '''
        Resolve function type *func* for argument types *args* and *kws*.
        A signature is returned.
        '''
        cache = self.callstack.lookup_resolve_cache(func, args, kws)
        if cache.has_failed_previously():
            return cache.replay_failure()
        
        try:
            res = self._resolve_user_function_type(func, args, kws)
            last_exception = None
        except errors.TypingError:
            e = None
            last_exception = e
            res = None
            e = None
            del e
        except:
            e = None
            del e

    # WARNING: Decompyle incomplete

    
    def _resolve_builtin_function_type(self, func, args, kws):
        pass
    # WARNING: Decompyle incomplete

    
    def _resolve_user_function_type(self, func, args, kws, literals = (None,)):
        functy = self._lookup_global(func)
    # WARNING: Decompyle incomplete

    
    def _get_attribute_templates(self, typ):
        '''
        Get matching AttributeTemplates for the Numba type.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def resolve_getattr(self, typ, attr):
        """
        Resolve getting the attribute *attr* (a string) on the Numba type.
        The attribute's type is returned, or None if resolution failed.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def find_matching_getattr_template(self, typ, attr):
        templates = list(self._get_attribute_templates(typ))
        get_local_target = get_local_target
        import numba.core.target_extension
        target_hw = get_local_target(self)
        order = order_by_target_specificity(target_hw, templates, fnkey = attr)
    # WARNING: Decompyle incomplete

    
    def resolve_setattr(self, target, attr, value):
        '''
        Resolve setting the attribute *attr* (a string) on the *target* type
        to the given *value* type.
        A function signature is returned, or None if resolution failed.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def resolve_static_getitem(self, value, index):
        pass
    # WARNING: Decompyle incomplete

    
    def resolve_static_setitem(self, target, index, value):
        pass
    # WARNING: Decompyle incomplete

    
    def resolve_setitem(self, target, index, value):
        pass
    # WARNING: Decompyle incomplete

    
    def resolve_delitem(self, target, index):
        args = (target, index)
        kws = { }
        fnty = self.resolve_value_type(operator.delitem)
        sig = fnty.get_call_type(self, args, kws)
        return sig

    
    def resolve_module_constants(self, typ, attr):
        '''
        Resolve module-level global constants.
        Return None or the attribute type
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def resolve_value_type(self, val):
        '''
        Return the numba type of a Python value that is being used
        as a runtime constant.
        ValueError is raised for unsupported types.
        '''
        
        try:
            ty = typeof(val, Purpose.constant)
            return ty
        except ValueError:
            e = None
            typeof_exc = utils.erase_traceback(e)
            e = None
            del e
        except:
            e = None
            del e

        if isinstance(val, types.ExternalFunction):
            return val
        ty = None._get_global_type(val)
    # WARNING: Decompyle incomplete

    
    def resolve_value_type_prefer_literal(self, value):
        '''Resolve value type and prefer Literal types whenever possible.
        '''
        lit = types.maybe_literal(value)
    # WARNING: Decompyle incomplete

    
    def _get_global_type(self, gv):
        ty = self._lookup_global(gv)
    # WARNING: Decompyle incomplete

    
    def _load_builtins(self):
        builtins = builtins
        arraydecl = arraydecl
        npdatetime = npdatetime
        import numba.core.typing
        ctypes_utils = ctypes_utils
        bufproto = bufproto
        import numba.core.typing
        eh = eh
        import numba.core.unsafe
        self.install_registry(templates.builtin_registry)

    
    def load_additional_registries(self):
        '''
        Load target-specific registries.  Can be overridden by subclasses.
        '''
        pass

    
    def install_registry(self, registry):
        '''
        Install a *registry* (a templates.Registry instance) of function,
        attribute and global declarations.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _lookup_global(self, gv):
        '''
        Look up the registered type for global value *gv*.
        '''
        
        try:
            gv = weakref.ref(gv)
        except TypeError:
            pass

        
        try:
            return self._globals.get(gv, None)
        except TypeError:
            return None


    
    def _insert_global(self, gv, gty):
        '''
        Register type *gty* for value *gv*.  Only a weak reference
        to *gv* is kept, if possible.
        '''
        
        def on_disposal(wr, pop = (self._globals.pop,)):
            pop(wr)

        
        try:
            gv = weakref.ref(gv, on_disposal)
        except TypeError:
            pass

        self._globals[gv] = gty

    
    def _remove_global(self, gv):
        '''
        Remove the registered type for global value *gv*.
        '''
        
        try:
            gv = weakref.ref(gv)
        except TypeError:
            pass

        del self._globals[gv]

    
    def insert_global(self, gv, gty):
        self._insert_global(gv, gty)

    
    def insert_attributes(self, at):
        key = at.key
        self._attributes[key].append(at)

    
    def insert_function(self, ft):
        key = ft.key
        self._functions[key].append(ft)

    
    def insert_user_function(self, fn, ft):
        '''Insert a user function.

        Args
        ----
        - fn:
            object used as callee
        - ft:
            function template
        '''
        self._insert_global(fn, types.Function(ft))

    
    def can_convert(self, fromty, toty):
        '''
        Check whether conversion is possible from *fromty* to *toty*.
        If successful, return a numba.typeconv.Conversion instance;
        otherwise None is returned.
        '''
        if fromty == toty:
            return Conversion.exact
        conv = None.tm.check_compatible(fromty, toty)
    # WARNING: Decompyle incomplete

    
    def _rate_arguments(self, actualargs, formalargs, unsafe_casting, exact_match_required = (True, False)):
        '''
        Rate the actual arguments for compatibility against the formal
        arguments.  A Rating instance is returned, or None if incompatible.
        '''
        if len(actualargs) != len(formalargs):
            return None
        rate = None()
    # WARNING: Decompyle incomplete

    
    def install_possible_conversions(self, actualargs, formalargs):
        '''
        Install possible conversions from the actual argument types to
        the formal argument types in the C++ type manager.
        Return True if all arguments can be converted.
        '''
        if len(actualargs) != len(formalargs):
            return False
    # WARNING: Decompyle incomplete

    
    def resolve_overload(self, key, cases, args, kws, allow_ambiguous, unsafe_casting, exact_match_required = (True, True, False)):
        '''
        Given actual *args* and *kws*, find the best matching
        signature in *cases*, or None if none matches.
        *key* is used for error reporting purposes.
        If *allow_ambiguous* is False, a tie in the best matches
        will raise an error.
        If *unsafe_casting* is False, unsafe casting is forbidden.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def unify_types(self, *typelist):
        
        def keyfunc(obj):
            '''Uses bitwidth to order numeric-types.
            Fallback to stable, deterministic sort.
            '''
            return getattr(obj, 'bitwidth', 0)

        typelist = sorted(typelist, key = keyfunc)
        unified = typelist[0]
    # WARNING: Decompyle incomplete

    
    def unify_pairs(self, first, second):
        '''
        Try to unify the two given types.  A third type is returned,
        or None in case of failure.
        '''
        if first == second:
            return first
        if None is types.undefined:
            return second
        if None is types.undefined:
            return first
        unified = None.unify(self, second)
    # WARNING: Decompyle incomplete



class Context(BaseContext):
    
    def load_additional_registries(self):
        cffi_utils = cffi_utils
        cmathdecl = cmathdecl
        enumdecl = enumdecl
        listdecl = listdecl
        mathdecl = mathdecl
        npydecl = npydecl
        setdecl = setdecl
        dictdecl = dictdecl
        import 
        self.install_registry(cffi_utils.registry)
        self.install_registry(cmathdecl.registry)
        self.install_registry(enumdecl.registry)
        self.install_registry(listdecl.registry)
        self.install_registry(mathdecl.registry)
        self.install_registry(npydecl.registry)
        self.install_registry(setdecl.registry)
        self.install_registry(dictdecl.registry)
