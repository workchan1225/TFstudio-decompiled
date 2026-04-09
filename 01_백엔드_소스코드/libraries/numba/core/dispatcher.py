# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dispatcher.pyc (Python 3.11)

import collections
import functools
import sys
import types as pytypes
import uuid
import weakref
from contextlib import ExitStack
from abc import abstractmethod
from numba import _dispatcher
from numba.core import utils, types, errors, typing, serialize, config, compiler, sigutils
from numba.core.compiler_lock import global_compiler_lock
from numba.core.typeconv.rules import default_type_manager
from numba.core.typing.templates import fold_arguments
from numba.core.typing.typeof import Purpose, typeof
from numba.core.bytecode import get_code_object
from numba.core.caching import NullCache, FunctionCache
from numba.core import entrypoints

event
<NODE:12> = None

class _FunctionCompiler(object):
    
    def __init__(self, py_func, targetdescr, targetoptions, locals, pipeline_class):
        self.py_func = py_func
        self.targetdescr = targetdescr
        self.targetoptions = targetoptions
        self.locals = locals
        self.pysig = utils.pysignature(self.py_func)
        self.pipeline_class = pipeline_class
        self._failed_cache = { }

    
    def fold_argument_types(self, args, kws):
        '''
        Given positional and named argument types, fold keyword arguments
        and resolve defaults by inserting types.Omitted() instances.

        A (pysig, argument types) tuple is returned.
        '''
        
        def normal_handler(index, param, value):
            return value

        
        def default_handler(index, param, default):
            return types.Omitted(default)

        
        def stararg_handler(index, param, values):
            return types.StarArgTuple(values)

        args = fold_arguments(self.pysig, args, kws, normal_handler, default_handler, stararg_handler)
        return (self.pysig, args)

    
    def compile(self, args, return_type):
        (status, retval) = self._compile_cached(args, return_type)
        if status:
            return retval
        raise None

    
    def _compile_cached(self, args, return_type):
        key = (tuple(args), return_type)
        
        try:
            return (False, self._failed_cache[key])
        except KeyError:
            pass

        
        try:
            retval = self._compile_core(args, return_type)
            return (True, retval)
        except errors.TypingError:
            e = None
            self._failed_cache[key] = e
            del e
            return None
            None = 
            del e


    
    def _compile_core(self, args, return_type):
        flags = compiler.Flags()
        self.targetdescr.options.parse_as_flags(flags, self.targetoptions)
        flags = self._customize_flags(flags)
        impl = self._get_implementation(args, { })
        cres = compiler.compile_extra(self.targetdescr.typing_context, self.targetdescr.target_context, impl, args = args, return_type = return_type, flags = flags, locals = self.locals, pipeline_class = self.pipeline_class)
    # WARNING: Decompyle incomplete

    
    def get_globals_for_reduction(self):
        return serialize._get_function_globals_for_reduction(self.py_func)

    
    def _get_implementation(self, args, kws):
        return self.py_func

    
    def _customize_flags(self, flags):
        return flags



class _GeneratedFunctionCompiler(_FunctionCompiler):
    pass
# WARNING: Decompyle incomplete

_CompileStats = collections.namedtuple('_CompileStats', ('cache_path', 'cache_hits', 'cache_misses'))

class CompilingCounter(object):
    '''
    A simple counter that increment in __enter__ and decrement in __exit__.
    '''
    
    def __init__(self):
        self.counter = 0

    
    def __enter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __exit__(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def __bool__(self):
        return self.counter > 0

    __nonzero__ = __bool__


class _DispatcherBase(_dispatcher.Dispatcher):
    '''
    Common base class for dispatcher Implementations.
    '''
    __numba__ = 'py_func'
    
    def __init__(self, arg_count, py_func, pysig, can_fallback, exact_match_required):
        self._tm = default_type_manager
        self.overloads = collections.OrderedDict()
        self.py_func = py_func
        self.func_code = get_code_object(py_func)
        self.__code__ = self.func_code
        self._types_active_call = set()
        self.__defaults__ = py_func.__defaults__
        argnames = tuple(pysig.parameters)
        if not self.py_func.__defaults__:
            default_values = ()
            defargs = (lambda .0: pass# WARNING: Decompyle incomplete
)(default_values())
            
            try:
                lastarg = list(pysig.parameters.values())[-1]
                has_stararg = lastarg.kind == lastarg.VAR_POSITIONAL
            except IndexError:
                has_stararg = False

            _dispatcher.Dispatcher.__init__(self, self._tm.get_pointer(), arg_count, self._fold_args, argnames, defargs, can_fallback, has_stararg, exact_match_required)
            self.doc = py_func.__doc__
            self._compiling_counter = CompilingCounter()
            self._enable_sysmon = bool(config.ENABLE_SYS_MONITORING)
            weakref.finalize(self, self._make_finalizer())
            return None

    
    def _compilation_chain_init_hook(self):
        '''
        This will be called ahead of any part of compilation taking place (this
        even includes being ahead of working out the types of the arguments).
        This permits activities such as initialising extension entry points so
        that the compiler knows about additional externally defined types etc
        before it does anything.
        '''
        entrypoints.init_all()

    
    def _reset_overloads(self):
        self._clear()
        self.overloads.clear()

    
    def _make_finalizer(self):
        '''
        Return a finalizer function that will release references to
        related compiled functions.
        '''
        pass
    # WARNING: Decompyle incomplete

    signatures = (lambda self: list(self.overloads))()
    nopython_signatures = (lambda self: self.overloads.values()())()
    
    def disable_compile(self, val = (True,)):
        '''Disable the compilation of new signatures at call time.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def add_overload(self, cres):
        args = tuple(cres.signature.args)
        sig = args()
        self._insert(sig, cres.entry_point, cres.objectmode)
        self.overloads[args] = cres

    
    def fold_argument_types(self, args, kws):
        return self._compiler.fold_argument_types(args, kws)

    
    def get_call_template(self, args, kws):
        '''
        Get a typing.ConcreteTemplate for this dispatcher and the given
        *args* and *kws* types.  This allows to resolve the return type.

        A (template, pysig, args, kws) tuple is returned.
        '''
        (pysig, args) = self._compiler.fold_argument_types(args, kws)
        kws = { }
        if self._can_compile:
            self.compile(tuple(args))
        func_name = self.py_func.__name__
        name = 'CallTemplate({0})'.format(func_name)
        call_template = typing.make_concrete_template(name, key = func_name, signatures = self.nopython_signatures)
        return (call_template, pysig, args, kws)

    
    def get_overload(self, sig):
        '''
        Return the compiled function for the given signature.
        '''
        (args, return_type) = sigutils.normalize_signature(sig)
        return self.overloads[tuple(args)].entry_point

    is_compiling = (lambda self: self._compiling_counter)()
    
    def _compile_for_args(self, *args, **kws):
        '''
        For internal use.  Compile a specialized version of the function
        for the given *args* and *kws*, and return the resulting callable.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def inspect_llvm(self, signature = (None,)):
        '''Get the LLVM intermediate representation generated by compilation.

        Parameters
        ----------
        signature : tuple of numba types, optional
            Specify a signature for which to obtain the LLVM IR. If None, the
            IR is returned for all available signatures.

        Returns
        -------
        llvm : dict[signature, str] or str
            Either the LLVM IR string for the specified signature, or, if no
            signature was given, a dictionary mapping signatures to LLVM IR
            strings.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def inspect_asm(self, signature = (None,)):
        '''Get the generated assembly code.

        Parameters
        ----------
        signature : tuple of numba types, optional
            Specify a signature for which to obtain the assembly code. If
            None, the assembly code is returned for all available signatures.

        Returns
        -------
        asm : dict[signature, str] or str
            Either the assembly code for the specified signature, or, if no
            signature was given, a dictionary mapping signatures to assembly
            code.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def inspect_types(self, file, signature, pretty, style = (None, None, False, 'default'), **kwargs):
        '''Print/return Numba intermediate representation (IR)-annotated code.

        Parameters
        ----------
        file : file-like object, optional
            File to which to print. Defaults to sys.stdout if None. Must be
            None if ``pretty=True``.
        signature : tuple of numba types, optional
            Print/return the intermediate representation for only the given
            signature. If None, the IR is printed for all available signatures.
        pretty : bool, optional
            If True, an Annotate object will be returned that can render the
            IR with color highlighting in Jupyter and IPython. ``file`` must
            be None if ``pretty`` is True. Additionally, the ``pygments``
            library must be installed for ``pretty=True``.
        style : str, optional
            Choose a style for rendering. Ignored if ``pretty`` is ``False``.
            This is directly consumed by ``pygments`` formatters. To see a
            list of available styles, import ``pygments`` and run
            ``list(pygments.styles.get_all_styles())``.

        Returns
        -------
        annotated : Annotate object, optional
            Only returned if ``pretty=True``, otherwise this function is only
            used for its printing side effect. If ``pretty=True``, an Annotate
            object is returned that can render itself in Jupyter and IPython.
        '''
        overloads = self.overloads
    # WARNING: Decompyle incomplete

    
    def inspect_cfg(self, signature, show_wrapper = (None, None), **kwargs):
        '''
        For inspecting the CFG of the function.

        By default the CFG of the user function is shown.  The *show_wrapper*
        option can be set to "python" or "cfunc" to show the python wrapper
        function or the *cfunc* wrapper function, respectively.

        Parameters accepted in kwargs
        -----------------------------
        filename : string, optional
            the name of the output file, if given this will write the output to
            filename
        view : bool, optional
            whether to immediately view the optional output file
        highlight : bool, set, dict, optional
            what, if anything, to highlight, options are:
            { incref : bool, # highlight NRT_incref calls
              decref : bool, # highlight NRT_decref calls
              returns : bool, # highlight exits which are normal returns
              raises : bool, # highlight exits which are from raise
              meminfo : bool, # highlight calls to NRT*meminfo
              branches : bool, # highlight true/false branches
             }
            Default is True which sets all of the above to True. Supplying a set
            of strings is also accepted, these are interpreted as key:True with
            respect to the above dictionary. e.g. {\'incref\', \'decref\'} would
            switch on highlighting on increfs and decrefs.
        interleave: bool, set, dict, optional
            what, if anything, to interleave in the LLVM IR, options are:
            { python: bool # interleave python source code with the LLVM IR
              lineinfo: bool # interleave line information markers with the LLVM
                             # IR
            }
            Default is True which sets all of the above to True. Supplying a set
            of strings is also accepted, these are interpreted as key:True with
            respect to the above dictionary. e.g. {\'python\',} would
            switch on interleaving of python source code in the LLVM IR.
        strip_ir : bool, optional
            Default is False. If set to True all LLVM IR that is superfluous to
            that requested in kwarg `highlight` will be removed.
        show_key : bool, optional
            Default is True. Create a "key" for the highlighting in the rendered
            CFG.
        fontsize : int, optional
            Default is 8. Set the fontsize in the output to this value.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def inspect_disasm_cfg(self, signature = (None,)):
        '''
        For inspecting the CFG of the disassembly of the function.

        Requires python package: r2pipe
        Requires radare2 binary on $PATH.
        Notebook rendering requires python package: graphviz

        signature : tuple of Numba types, optional
            Print/return the disassembly CFG for only the given signatures.
            If None, the IR is printed for all available signatures.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_annotation_info(self, signature = (None,)):
        '''
        Gets the annotation information for the function specified by
        signature. If no signature is supplied a dictionary of signature to
        annotation information is returned.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _explain_ambiguous(self, *args, **kws):
        '''
        Callback for the C _Dispatcher object.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _explain_matching_error(self, *args, **kws):
        '''
        Callback for the C _Dispatcher object.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _search_new_conversions(self, *args, **kws):
        '''
        Callback for the C _Dispatcher object.
        Search for approximately matching signatures for the given arguments,
        and ensure the corresponding conversions are registered in the C++
        type manager.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return f'''{type(self).__name__!s}({self.py_func!s})'''

    
    def typeof_pyval(self, val):
        '''
        Resolve the Numba type of Python value *val*.
        This is called from numba._dispatcher as a fallback if the native code
        cannot decide the type.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _callback_add_timer(self, duration, cres, lock_name):
        md = cres.metadata
    # WARNING: Decompyle incomplete

    
    def _callback_add_compiler_timer(self, duration, cres):
        return self._callback_add_timer(duration, cres, lock_name = 'compiler_lock')

    
    def _callback_add_llvm_timer(self, duration, cres):
        return self._callback_add_timer(duration, cres, lock_name = 'llvm_lock')



class _MemoMixin:
    _MemoMixin__uuid = None
    _memo = weakref.WeakValueDictionary()
    _recent = collections.deque(maxlen = config.FUNCTION_CACHE_SIZE)
    _uuid = (lambda self: u = self._MemoMixin__uuid# WARNING: Decompyle incomplete
)()
    
    def _set_uuid(self, u):
        pass
    # WARNING: Decompyle incomplete



class Dispatcher(_DispatcherBase, _MemoMixin, serialize.ReduceMixin):
    '''
    Implementation of user-facing dispatcher objects (i.e. created using
    the @jit decorator).
    This is an abstract base class. Subclasses should define the targetdescr
    class attribute.
    '''
    _fold_args = True
    __numba__ = 'py_func'
    
    def __init__(self, py_func, locals, targetoptions, pipeline_class = (None, None, compiler.Compiler)):
        '''
        Parameters
        ----------
        py_func: function object to be compiled
        locals: dict, optional
            Mapping of local variable names to Numba types.  Used to override
            the types deduced by the type inference engine.
        targetoptions: dict, optional
            Target-specific config options.
        pipeline_class: type numba.compiler.CompilerBase
            The compiler pipeline type.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def dump(self, tab = ('',)):
        print(f'''{tab}DUMP {type(self).__name__}[{self.py_func.__name__}, type code={self._type._code}]''')
        for cres in self.overloads.values():
            cres.dump(tab = tab + '  ')
            print(f'''{tab}END DUMP {type(self).__name__}[{self.py_func.__name__}]''')
            return None

    _numba_type_ = (lambda self: types.Dispatcher(self))()
    
    def enable_caching(self):
        self._cache = FunctionCache(self.py_func)

    
    def __get__(self, obj, objtype = (None,)):
        '''Allow a JIT function to be bound as a method to an object'''
        pass
    # WARNING: Decompyle incomplete

    
    def _reduce_states(self):
        '''
        Reduce the instance for pickling.  This will serialize
        the original function as well the compilation options and
        compiled signatures, but not the compiled code itself.

        NOTE: part of ReduceMixin protocol
        '''
        return dict(uuid = str(self._uuid), py_func = self.py_func, locals = self.locals, targetoptions = self.targetoptions, can_compile = self._can_compile, sigs = sigs)

    _rebuild = (lambda cls, uuid, py_func, locals, targetoptions, can_compile, sigs: try:
cls._memo[uuid]except KeyError:
passself = cls(py_func, locals, targetoptions)self._set_uuid(uuid)for sig in sigs:
self.compile(sig)self._can_compile = can_compileself)()
    
    def compile(self, sig):
        pass
    # WARNING: Decompyle incomplete

    
    def get_compile_result(self, sig):
        '''Compile (if needed) and return the compilation result with the
        given signature.

        Returns ``CompileResult``.
        Raises ``NumbaError`` if the signature is incompatible.
        '''
        atypes = tuple(sig.args)
        if atypes not in self.overloads:
            if self._can_compile:
                self.compile(atypes)
            else:
                msg = f'''{sig} not available and compilation disabled'''
                raise errors.TypingError(msg)
        return self.overloads[atypes]

    
    def recompile(self):
        '''
        Recompile all signatures afresh.
        '''
        sigs = list(self.overloads)
        old_can_compile = self._can_compile
        self._make_finalizer()()
        self._reset_overloads()
        self._cache.flush()
        self._can_compile = True
        
        try:
            for sig in sigs:
                self.compile(sig)
                self._can_compile = old_can_compile
                return None
                self._can_compile = old_can_compile


    stats = (lambda self: _CompileStats(cache_path = self._cache.cache_path, cache_hits = self._cache_hits, cache_misses = self._cache_misses))()
    
    def parallel_diagnostics(self, signature, level = (None, 1)):
        '''
        Print parallel diagnostic information for the given signature. If no
        signature is present it is printed for all known signatures. level is
        used to adjust the verbosity, level=1 (default) is minimal verbosity,
        and 2, 3, and 4 provide increasing levels of verbosity.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_metadata(self, signature = (None,)):
        '''
        Obtain the compilation metadata for a given signature.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_function_type(self):
        '''Return unique function type of dispatcher when possible, otherwise
        return None.

        A Dispatcher instance has unique function type when it
        contains exactly one compilation result and its compilation
        has been disabled (via its disable_compile method).
        '''
        if self._can_compile or len(self.overloads) == 1:
            cres = tuple(self.overloads.values())[0]
            return types.FunctionType(cres.signature)
        return None



class LiftedCode(_DispatcherBase, _MemoMixin, serialize.ReduceMixin):
    '''
    Implementation of the hidden dispatcher objects used for lifted code
    (a lifted loop is really compiled as a separate function).
    '''
    _fold_args = False
    can_cache = False
    
    def __init__(self, func_ir, typingctx, targetctx, flags, locals):
        self.func_ir = func_ir
        self.lifted_from = None
        self.typingctx = typingctx
        self.targetctx = targetctx
        self.flags = flags
        self.locals = locals
        _DispatcherBase.__init__(self, self.func_ir.arg_count, self.func_ir.func_id.func, self.func_ir.func_id.pysig, can_fallback = True, exact_match_required = False)

    
    def _reduce_states(self):
        '''
        Reduce the instance for pickling.  This will serialize
        the original function as well the compilation options and
        compiled signatures, but not the compiled code itself.

        NOTE: part of ReduceMixin protocol
        '''
        return dict(uuid = self._uuid, func_ir = self.func_ir, flags = self.flags, locals = self.locals, extras = self._reduce_extras())

    
    def _reduce_extras(self):
        '''
        NOTE: sub-class can override to add extra states
        '''
        return { }

    _rebuild = (lambda cls, uuid, func_ir, flags, locals, extras: try:
cls._memo[uuid]except KeyError:
passregistry = registryimport numba.coretypingctx = registry.cpu_target.typing_contexttargetctx = registry.cpu_target.target_context# WARNING: Decompyle incomplete
)()
    
    def get_source_location(self):
        '''Return the starting line number of the loop.
        '''
        return self.func_ir.loc.line

    
    def _pre_compile(self, args, return_type, flags):
        '''Pre-compile actions
        '''
        pass

    compile = (lambda self, sig: pass)()
    
    def _get_dispatcher_for_current_target(self):
        return self



class LiftedLoop(LiftedCode):
    
    def _pre_compile(self, args, return_type, flags):
        pass
    # WARNING: Decompyle incomplete

    
    def compile(self, sig):
        pass
    # WARNING: Decompyle incomplete



class LiftedWith(LiftedCode):
    can_cache = True
    
    def _reduce_extras(self):
        return dict(output_types = self.output_types)

    _numba_type_ = (lambda self: types.Dispatcher(self))()
    
    def get_call_template(self, args, kws):
        '''
        Get a typing.ConcreteTemplate for this dispatcher and the given
        *args* and *kws* types.  This enables the resolving of the return type.

        A (template, pysig, args, kws) tuple is returned.
        '''
        if self._can_compile:
            self.compile(tuple(args))
        pysig = None
        func_name = self.py_func.__name__
        name = 'CallTemplate({0})'.format(func_name)
        call_template = typing.make_concrete_template(name, key = func_name, signatures = self.nopython_signatures)
        return (call_template, pysig, args, kws)

    
    def compile(self, sig):
        pass
    # WARNING: Decompyle incomplete



class ObjModeLiftedWith(LiftedWith):
    pass
# WARNING: Decompyle incomplete

if config.USE_LEGACY_TYPE_SYSTEM:
    None(dict, (lambda .0: pass# WARNING: Decompyle incomplete
)(types.number_domain()))
    return None
None(dict, (lambda .0: pass# WARNING: Decompyle incomplete
)(types.np_number_domain()))
