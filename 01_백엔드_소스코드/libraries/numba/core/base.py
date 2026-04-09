# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

from collections import defaultdict
import copy
import sys
from itertools import permutations, takewhile
from contextlib import contextmanager
from functools import cached_property
from llvmlite import ir as llvmir
from llvmlite.ir import Constant
from llvmlite.binding import binding as ll
from numba.core import types, utils, datamodel, debuginfo, funcdesc, config, cgutils, imputils
from numba.core import event, errors, targetconfig
from numba import _dynfunc, _helperlib
from numba.core.compiler_lock import global_compiler_lock
from numba.core.pythonapi import PythonAPI
from numba.core.imputils import user_function, user_generator, builtin_registry, impl_ret_borrowed, RegistryLoader
from numba.cpython import builtins
GENERIC_POINTER = llvmir.PointerType(llvmir.IntType(8))
PYOBJECT = GENERIC_POINTER
void_ptr = GENERIC_POINTER

class OverloadSelector(object):
    '''
    An object matching an actual signature against a registry of formal
    signatures and choosing the best candidate, if any.

    In the current implementation:
    - a "signature" is a tuple of type classes or type instances
    - the "best candidate" is the most specific match
    '''
    
    def __init__(self):
        self.versions = []
        self._cache = { }

    
    def find(self, sig):
        out = self._cache.get(sig)
    # WARNING: Decompyle incomplete

    
    def _find(self, sig):
        candidates = self._select_compatible(sig)
        if candidates:
            return candidates[self._best_signature(candidates)]
        raise None.NumbaNotImplementedError(f'''{self}, {sig}''')

    
    def _select_compatible(self, sig):
        '''
        Select all compatible signatures and their implementation.
        '''
        out = { }
        for ver_sig, impl in self.versions:
            if self._match_arglist(ver_sig, sig):
                out[ver_sig] = impl
            return out

    
    def _best_signature(self, candidates):
        '''
        Returns the best signature out of the candidates
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _sort_signatures(self, candidates):
        '''
        Sort signatures in ascending level of genericity.

        Returns a 2-tuple:

            * ordered list of signatures
            * dictionary containing genericity scores
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _match_arglist(self, formal_args, actual_args):
        '''
        Returns True if the signature is "matching".
        A formal signature is "matching" if the actual signature matches exactly
        or if the formal signature is a compatible generic signature.
        '''
        if formal_args and isinstance(formal_args[-1], types.VarArg):
            ndiff = (len(actual_args) - len(formal_args)) + 1
            formal_args = formal_args[:-1] + (formal_args[-1].dtype,) * ndiff
        if len(formal_args) != len(actual_args):
            return False
        for formal, actual in None(formal_args, actual_args):
            if not self._match(formal, actual):
                return False
            return True

    
    def _match(self, formal, actual):
        if formal == actual:
            return True
        if None.Any == formal:
            return True
        if None(formal, type) or issubclass(formal, types.Type):
            if isinstance(actual, type) and issubclass(actual, formal):
                return True
            if None(actual, formal):
                return True
            return None
        return None

    
    def append(self, value, sig):
        '''
        Add a formal signature and its associated value.
        '''
        pass
    # WARNING: Decompyle incomplete


_load_global_helpers = (lambda : ll.add_symbol('_Py_NoneStruct', id(None))for c_helpers in (_helperlib.c_helpers, _dynfunc.c_helpers):
for py_name, c_address in c_helpers.items():
c_name = 'numba_' + py_namell.add_symbol(c_name, c_address)for obj in utils.builtins.__dict__.values():
if isinstance(obj, type) and issubclass(obj, BaseException):
ll.add_symbol('PyExc_%s' % obj.__name__, id(obj))None)()

class BaseContext(object):
    '''

    Notes on Structure
    ------------------

    Most objects are lowered as plain-old-data structure in the generated
    llvm.  They are passed around by reference (a pointer to the structure).
    Only POD structure can live across function boundaries by copying the
    data.
    '''
    strict_alignment = False
    implement_powi_as_math_call = False
    implement_pow_as_math_call = False
    enable_debuginfo = False
    DIBuilder = debuginfo.DIBuilder
    enable_boundscheck = (lambda self: pass# WARNING: Decompyle incomplete
)()
    enable_boundscheck = (lambda self, value: self._boundscheck = value)()
    enable_nrt = False
    auto_parallel = False
    aot_mode = False
    error_model = None
    allow_dynamic_globals = False
    fastmath = False
    environment = None
    fndesc = None
    
    def __init__(self, typing_context, target):
        _load_global_helpers()
        self.address_size = utils.MACHINE_BITS
        self.typing_context = typing_context
        target_registry = target_registry
        import numba.core.target_extension
        self.target_name = target
        self.target = target_registry[target]
        self._registries = { }
        self._defns = defaultdict(OverloadSelector)
        self._getattrs = defaultdict(OverloadSelector)
        self._setattrs = defaultdict(OverloadSelector)
        self._casts = OverloadSelector()
        self._get_constants = OverloadSelector()
        self._generators = { }
        self.special_ops = { }
        self.cached_internal_func = { }
        self._pid = None
        self._codelib_stack = []
        self._boundscheck = False
        self.data_model_manager = datamodel.default_manager
        self.init()

    
    def init(self):
        '''
        For subclasses to add initializer
        '''
        pass

    
    def refresh(self):
        '''
        Refresh context with new declarations from known registries.
        Useful for third-party extensions.
        '''
        self.load_additional_registries()
        self.install_registry(builtin_registry)
        self.typing_context.refresh()

    
    def load_additional_registries(self):
        '''
        Load target-specific registries.  Can be overridden by subclasses.
        '''
        pass

    
    def mangler(self, name = enable_boundscheck.setter, types = {
        'abi_tags': (),
        'uid': None }, *, abi_tags, uid):
        '''
        Perform name mangling.
        '''
        return funcdesc.default_mangler(name, types, abi_tags = abi_tags, uid = uid)

    
    def get_env_name(self, fndesc):
        '''Get the environment name given a FunctionDescriptor.

        Use this instead of the ``fndesc.env_name`` so that the target-context
        can provide necessary mangling of the symbol to meet ABI requirements.
        '''
        return fndesc.env_name

    
    def declare_env_global(self, module, envname):
        '''Declare the Environment pointer as a global of the module.

        The pointer is initialized to NULL.  It must be filled by the runtime
        with the actual address of the Env before the associated function
        can be executed.

        Parameters
        ----------
        module :
            The LLVM Module
        envname : str
            The name of the global variable.
        '''
        if envname not in module.globals:
            gv = llvmir.GlobalVariable(module, cgutils.voidptr_t, name = envname)
            gv.linkage = 'common'
            gv.initializer = cgutils.get_null_value(gv.type.pointee)
        return module.globals[envname]

    
    def get_arg_packer(self, fe_args):
        return datamodel.ArgPacker(self.data_model_manager, fe_args)

    
    def get_data_packer(self, fe_types):
        return datamodel.DataPacker(self.data_model_manager, fe_types)

    target_data = (lambda self: raise NotImplementedError)()
    nonconst_module_attrs = (lambda self: tuple())()
    nrt = (lambda self: NRTContext = NRTContextimport numba.core.runtime.contextNRTContext(self, self.enable_nrt))()
    
    def subtarget(self, **kws):
        obj = copy.copy(self)
        for k, v in kws.items():
            if not hasattr(obj, k):
                raise NameError('unknown option {0!r}'.format(k))
            setattr(obj, k, v)
            if obj.codegen() is not self.codegen():
                obj.cached_internal_func = { }
        return obj

    
    def install_registry(self, registry):
        '''
        Install a *registry* (a imputils.Registry instance) of function
        and attribute implementations.
        '''
        
        try:
            loader = self._registries[registry]
        except KeyError:
            loader = RegistryLoader(registry)
            self._registries[registry] = loader

        self.insert_func_defn(loader.new_registrations('functions'))
        self._insert_getattr_defn(loader.new_registrations('getattrs'))
        self._insert_setattr_defn(loader.new_registrations('setattrs'))
        self._insert_cast_defn(loader.new_registrations('casts'))
        self._insert_get_constant_defn(loader.new_registrations('constants'))

    
    def insert_func_defn(self, defns):
        for impl, func, sig in defns:
            self._defns[func].append(impl, sig)
            return None

    
    def _insert_getattr_defn(self, defns):
        for impl, attr, sig in defns:
            self._getattrs[attr].append(impl, sig)
            return None

    
    def _insert_setattr_defn(self, defns):
        for impl, attr, sig in defns:
            self._setattrs[attr].append(impl, sig)
            return None

    
    def _insert_cast_defn(self, defns):
        for impl, sig in defns:
            self._casts.append(impl, sig)
            return None

    
    def _insert_get_constant_defn(self, defns):
        for impl, sig in defns:
            self._get_constants.append(impl, sig)
            return None

    
    def insert_user_function(self, func, fndesc, libs = ((),)):
        impl = user_function(fndesc, libs)
        self._defns[func].append(impl, impl.signature)

    
    def insert_generator(self, genty, gendesc, libs = ((),)):
        pass
    # WARNING: Decompyle incomplete

    
    def remove_user_function(self, func):
        """
        Remove user function *func*.
        KeyError is raised if the function isn't known to us.
        """
        del self._defns[func]

    
    def get_external_function_type(self, fndesc):
        pass
    # WARNING: Decompyle incomplete

    
    def declare_function(self, module, fndesc):
        fnty = self.call_conv.get_function_type(fndesc.restype, fndesc.argtypes)
        fn = cgutils.get_or_insert_function(module, fnty, fndesc.mangled_name)
        self.call_conv.decorate_function(fn, fndesc.args, fndesc.argtypes, noalias = fndesc.noalias)
        if fndesc.inline:
            fn.attributes.add('alwaysinline')
            fn.attributes.discard('noinline')
            fn.attributes.discard('optnone')
        return fn

    
    def declare_external_function(self, module, fndesc):
        fnty = self.get_external_function_type(fndesc)
        fn = cgutils.get_or_insert_function(module, fnty, fndesc.mangled_name)
    # WARNING: Decompyle incomplete

    
    def insert_const_string(self, mod, string):
        '''
        Insert constant *string* (a str object) into module *mod*.
        '''
        stringtype = GENERIC_POINTER
        name = '.const.%s' % string
        text = cgutils.make_bytearray(string.encode('utf-8') + b'\x00')
        gv = self.insert_unique_const(mod, name, text)
        return Constant.bitcast(gv, stringtype)

    
    def insert_const_bytes(self, mod, bytes, name = (None,)):
        '''
        Insert constant *byte* (a `bytes` object) into module *mod*.
        '''
        stringtype = GENERIC_POINTER
        if not name:
            pass
        name = '.bytes.%s' % hash(bytes)
        text = cgutils.make_bytearray(bytes)
        gv = self.insert_unique_const(mod, name, text)
        return Constant.bitcast(gv, stringtype)

    
    def insert_unique_const(self, mod, name, val):
        '''
        Insert a unique internal constant named *name*, with LLVM value
        *val*, into module *mod*.
        '''
        
        try:
            gv = mod.get_global(name)
            return gv
        except KeyError:
            return 


    
    def get_argument_type(self, ty):
        return self.data_model_manager[ty].get_argument_type()

    
    def get_return_type(self, ty):
        return self.data_model_manager[ty].get_return_type()

    
    def get_data_type(self, ty):
        '''
        Get a LLVM data representation of the Numba type *ty* that is safe
        for storage.  Record data are stored as byte array.

        The return value is a llvmlite.ir.Type object, or None if the type
        is an opaque pointer (???).
        '''
        return self.data_model_manager[ty].get_data_type()

    
    def get_value_type(self, ty):
        return self.data_model_manager[ty].get_value_type()

    
    def pack_value(self, builder, ty, value, ptr, align = (None,)):
        '''
        Pack value into the array storage at *ptr*.
        If *align* is given, it is the guaranteed alignment for *ptr*
        (by default, the standard ABI alignment).
        '''
        dataval = self.data_model_manager[ty].as_data(builder, value)
        builder.store(dataval, ptr, align = align)

    
    def unpack_value(self, builder, ty, ptr, align = (None,)):
        '''
        Unpack value from the array storage at *ptr*.
        If *align* is given, it is the guaranteed alignment for *ptr*
        (by default, the standard ABI alignment).
        '''
        dm = self.data_model_manager[ty]
        return dm.load_from_data_pointer(builder, ptr, align)

    
    def get_constant_generic(self, builder, ty, val):
        '''
        Return a LLVM constant representing value *val* of Numba type *ty*.
        '''
        
        try:
            impl = self._get_constants.find((ty,))
            return impl(self, builder, ty, val)
        except NotImplementedError:
            raise NotImplementedError(f'''Cannot lower constant of type \'{ty!s}\'''')


    
    def get_constant(self, ty, val):
        '''
        Same as get_constant_generic(), but without specifying *builder*.
        Works only for simple types.
        '''
        return self.get_constant_generic(None, ty, val)

    
    def get_constant_undef(self, ty):
        lty = self.get_value_type(ty)
        return Constant(lty, llvmir.Undefined)

    
    def get_constant_null(self, ty):
        lty = self.get_value_type(ty)
        return Constant(lty, None)

    
    def get_function(self, fn, sig, _firstcall = (True,)):
        '''
        Return the implementation of function *fn* for signature *sig*.
        The return value is a callable with the signature (builder, args).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_generator_desc(self, genty):
        '''
        '''
        return self._generators[genty][0]

    
    def get_generator_impl(self, genty):
        '''
        '''
        res = self._generators[genty][1]
        self.add_linking_libs(getattr(res, 'libs', ()))
        return res

    
    def get_bound_function(self, builder, obj, ty):
        pass
    # WARNING: Decompyle incomplete

    
    def get_getattr(self, typ, attr):
        '''
        Get the getattr() implementation for the given type and attribute name.
        The return value is a callable with the signature
        (context, builder, typ, val, attr).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_setattr(self, attr, sig):
        '''
        Get the setattr() implementation for the given attribute name
        and signature.
        The return value is a callable with the signature (builder, args).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_argument_value(self, builder, ty, val):
        '''
        Argument representation to local value representation
        '''
        return self.data_model_manager[ty].from_argument(builder, val)

    
    def get_returned_value(self, builder, ty, val):
        '''
        Return value representation to local value representation
        '''
        return self.data_model_manager[ty].from_return(builder, val)

    
    def get_return_value(self, builder, ty, val):
        '''
        Local value representation to return type representation
        '''
        return self.data_model_manager[ty].as_return(builder, val)

    
    def get_value_as_argument(self, builder, ty, val):
        '''Prepare local value representation as argument type representation
        '''
        return self.data_model_manager[ty].as_argument(builder, val)

    
    def get_value_as_data(self, builder, ty, val):
        return self.data_model_manager[ty].as_data(builder, val)

    
    def get_data_as_value(self, builder, ty, val):
        return self.data_model_manager[ty].from_data(builder, val)

    
    def pair_first(self, builder, val, ty):
        '''
        Extract the first element of a heterogeneous pair.
        '''
        pair = self.make_helper(builder, ty, val)
        return pair.first

    
    def pair_second(self, builder, val, ty):
        '''
        Extract the second element of a heterogeneous pair.
        '''
        pair = self.make_helper(builder, ty, val)
        return pair.second

    
    def cast(self, builder, val, fromty, toty):
        '''
        Cast a value of type *fromty* to type *toty*.
        This implements implicit conversions as can happen due to the
        granularity of the Numba type system, or lax Python semantics.
        '''
        if fromty is types._undef_var:
            return self.get_constant_null(toty)
        if None == toty or toty == types.Any:
            return val
        
        try:
            impl = self._casts.find((fromty, toty))
            return impl(self, builder, fromty, toty, val)
        except errors.NumbaNotImplementedError:
            raise errors.NumbaNotImplementedError(f'''Cannot cast {fromty!s} to {toty!s}: {val!s}''')


    
    def generic_compare(self, builder, key, argtypes, args):
        """
        Compare the given LLVM values of the given Numba types using
        the comparison *key* (e.g. '==').  The values are first cast to
        a common safe conversion type.
        """
        (at, bt) = argtypes
        (av, bv) = args
        ty = self.typing_context.unify_types(at, bt)
    # WARNING: Decompyle incomplete

    
    def make_optional_none(self, builder, valtype):
        optval = self.make_helper(builder, types.Optional(valtype))
        optval.valid = cgutils.false_bit
        return optval._getvalue()

    
    def make_optional_value(self, builder, valtype, value):
        optval = self.make_helper(builder, types.Optional(valtype))
        optval.valid = cgutils.true_bit
        optval.data = value
        return optval._getvalue()

    
    def is_true(self, builder, typ, val):
        '''
        Return the truth value of a value of the given Numba type.
        '''
        fnty = self.typing_context.resolve_value_type(bool)
        sig = fnty.get_call_type(self.typing_context, (typ,), { })
        impl = self.get_function(fnty, sig)
        return impl(builder, (val,))

    
    def get_c_value(self, builder, typ, name, dllimport = (False,)):
        '''
        Get a global value through its C-accessible *name*, with the given
        LLVM type.
        If *dllimport* is true, the symbol will be marked as imported
        from a DLL (necessary for AOT compilation under Windows).
        '''
        module = builder.function.module
        
        try:
            gv = module.globals[name]
        except KeyError:
            gv = cgutils.add_global_variable(module, typ, name)
            if dllimport and self.aot_mode and sys.platform == 'win32':
                gv.storage_class = 'dllimport'

        return gv

    
    def call_external_function(self, builder, callee, argtys, args):
        pass
    # WARNING: Decompyle incomplete

    
    def get_function_pointer_type(self, typ):
        return self.data_model_manager[typ].get_data_type()

    
    def call_function_pointer(self, builder, funcptr, args, cconv = (None,)):
        return builder.call(funcptr, args, cconv = cconv)

    
    def print_string(self, builder, text):
        mod = builder.module
        cstring = GENERIC_POINTER
        fnty = llvmir.FunctionType(llvmir.IntType(32), [
            cstring])
        puts = cgutils.get_or_insert_function(mod, fnty, 'puts')
        return builder.call(puts, [
            text])

    
    def debug_print(self, builder, text):
        mod = builder.module
        cstr = self.insert_const_string(mod, str(text))
        self.print_string(builder, cstr)

    
    def printf(self, builder, format_string, *args):
        mod = builder.module
        if isinstance(format_string, str):
            cstr = self.insert_const_string(mod, format_string)
        else:
            cstr = format_string
        fnty = llvmir.FunctionType(llvmir.IntType(32), (GENERIC_POINTER,), var_arg = True)
        fn = cgutils.get_or_insert_function(mod, fnty, 'printf')
        return builder.call(fn, (cstr,) + tuple(args))

    
    def get_struct_type(self, struct):
        '''
        Get the LLVM struct type for the given Structure class *struct*.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_dummy_value(self):
        return Constant(self.get_dummy_type(), None)

    
    def get_dummy_type(self):
        return GENERIC_POINTER

    
    def _compile_subroutine_no_cache(self, builder, impl, sig, locals, flags = (None, None)):
        """
        Invoke the compiler to compile a function to be used inside a
        nopython function, but without generating code to call that
        function.

        Note this context's flags are not inherited.
        """
        compiler = compiler
        import numba.core
    # WARNING: Decompyle incomplete

    
    def compile_subroutine(self, builder, impl, sig, locals, flags, caching = (None, None, True)):
        '''
        Compile the function *impl* for the given *sig* (in nopython mode).
        Return an instance of CompileResult.

        If *caching* evaluates True, the function keeps the compiled function
        for reuse in *.cached_internal_func*.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def compile_internal(self, builder, impl, sig, args, locals = (None,)):
        '''
        Like compile_subroutine(), but also call the function with the given
        *args*.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def call_internal(self, builder, fndesc, sig, args):
        '''
        Given the function descriptor of an internally compiled function,
        emit a call to that function with the given arguments.
        '''
        (status, res) = self.call_internal_no_propagate(builder, fndesc, sig, args)
        cgutils.if_unlikely(builder, status.is_error)
        self.call_conv.return_status_propagate(builder, status)
        None(None, None)

    
    def call_internal_no_propagate(self, builder, fndesc, sig, args):
        '''Similar to `.call_internal()` but does not handle or propagate
        the return status automatically.
        '''
        llvm_mod = builder.module
        fn = self.declare_function(llvm_mod, fndesc)
        (status, res) = self.call_conv.call_function(builder, fn, sig.return_type, sig.args, args)
        return (status, res)

    
    def call_unresolved(self, builder, name, sig, args):
        '''
        Insert a function call to an unresolved symbol with the given *name*.

        Note: this is used for recursive call.

        In the mutual recursion case::

            @njit
            def foo():
                ...  # calls bar()

            @njit
            def bar():
                ... # calls foo()

            foo()

        When foo() is called, the compilation of bar() is fully completed
        (codegen\'ed and loaded) before foo() is. Since MCJIT\'s eager compilation
        doesn\'t allow loading modules with declare-only functions (which is
        needed for foo() in bar()), the call_unresolved injects a global
        variable that the "linker" can update even after the module is loaded by
        MCJIT. The linker would allocate space for the global variable before
        the bar() module is loaded. When later foo() module is defined, it will
        update bar()\'s reference to foo().

        The legacy lazy JIT and the new ORC JIT would allow a declare-only
        function be used in a module as long as it is defined by the time of its
        first use.
        '''
        codegen = self.codegen()
        fnty = self.call_conv.get_function_type(sig.return_type, sig.args)
        fn = codegen.insert_unresolved_ref(builder, fnty, name)
        (status, res) = self.call_conv.call_function(builder, fn, sig.return_type, sig.args, args)
        cgutils.if_unlikely(builder, status.is_error)
        self.call_conv.return_status_propagate(builder, status)
        None(None, None)

    
    def get_executable(self, func, fndesc, env):
        raise NotImplementedError

    
    def get_python_api(self, builder):
        return PythonAPI(self, builder)

    
    def sentry_record_alignment(self, rectyp, attr):
        '''
        Assumes offset starts from a properly aligned location
        '''
        if self.strict_alignment:
            offset = rectyp.offset(attr)
            elemty = rectyp.typeof(attr)
            if isinstance(elemty, types.NestedArray):
                elemty = elemty.dtype
            align = self.get_abi_alignment(self.get_data_type(elemty))
            if offset % align:
                msg = '{rec}.{attr} of type {type} is not aligned'.format(rec = rectyp, attr = attr, type = elemty)
                raise errors.NumbaTypeError(msg)
        return None

    
    def get_helper_class(self, typ, kind = ('value',)):
        '''
        Get a helper class for the given *typ*.
        '''
        return cgutils.create_struct_proxy(typ, kind)

    
    def _make_helper(self, builder, typ, value, ref, kind = (None, None, 'value')):
        cls = self.get_helper_class(typ, kind)
        return cls(self, builder, value = value, ref = ref)

    
    def make_helper(self, builder, typ, value, ref = (None, None)):
        """
        Get a helper object to access the *typ*'s members,
        for the given value or reference.
        """
        return self._make_helper(builder, typ, value, ref, kind = 'value')

    
    def make_data_helper(self, builder, typ, ref = (None,)):
        '''
        As make_helper(), but considers the value as stored in memory,
        rather than a live value.
        '''
        return self._make_helper(builder, typ, ref = ref, kind = 'data')

    
    def make_array(self, typ):
        arrayobj = arrayobj
        import numba.np
        return arrayobj.make_array(typ)

    
    def populate_array(self, arr, **kwargs):
        '''
        Populate array structure.
        '''
        arrayobj = arrayobj
        import numba.np
    # WARNING: Decompyle incomplete

    
    def make_complex(self, builder, typ, value = (None,)):
        """
        Get a helper object to access the given complex numbers' members.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def make_tuple(self, builder, typ, values):
        '''
        Create a tuple of the given *typ* containing the *values*.
        '''
        tup = self.get_constant_undef(typ)
        for i, val in enumerate(values):
            tup = builder.insert_value(tup, val, i)
            return tup

    
    def make_constant_array(self, builder, typ, ary):
        '''
        Create an array structure reifying the given constant array.
        A low-level contiguous array constant is created in the LLVM IR.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def add_dynamic_addr(self, builder, intaddr, info):
        '''
        Returns dynamic address as a void pointer `i8*`.

        Internally, a global variable is added to inform the lowerer about
        the usage of dynamic addresses.  Caching will be disabled.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_abi_sizeof(self, ty):
        '''
        Get the ABI size of LLVM type *ty*.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_abi_alignment(self, ty):
        '''
        Get the ABI alignment of LLVM type *ty*.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_preferred_array_alignment(context, ty):
        '''
        Get preferred array alignment for Numba type *ty*.
        '''
        return 32

    
    def post_lowering(self, mod, library):
        '''Run target specific post-lowering transformation here.
        '''
        pass

    
    def create_module(self, name):
        '''Create a LLVM module

        The default implementation in BaseContext always raises a
        ``NotImplementedError`` exception. Subclasses should implement
        this method.
        '''
        raise NotImplementedError

    active_code_library = (lambda self: self._codelib_stack[-1])()
    push_code_library = (lambda self, lib: pass# WARNING: Decompyle incomplete
)()
    
    def add_linking_libs(self, libs):
        '''Add iterable of linking libraries to the *active_code_library*.
        '''
        colib = self.active_code_library
        for lib in libs:
            colib.add_linking_library(lib)
            return None

    
    def get_ufunc_info(self, ufunc_key):
        '''Get the ufunc implementation for a given ufunc object.

        The default implementation in BaseContext always raises a
        ``NotImplementedError`` exception. Subclasses may raise ``KeyError``
        to signal that the given ``ufunc_key`` is not available.

        Parameters
        ----------
        ufunc_key : NumPy ufunc

        Returns
        -------
        res : dict[str, callable]
            A mapping of a NumPy ufunc type signature to a lower-level
            implementation.
        '''
        raise NotImplementedError(f'''{self} does not support ufunc''')



class _wrap_impl(object):
    '''
    A wrapper object to call an implementation function with some predefined
    (context, signature) arguments.
    The wrapper also forwards attribute queries, which is important.
    '''
    
    def __init__(self, imp, context, sig):
        self._callable = _wrap_missing_loc(imp)
        self._imp = self._callable()
        self._context = context
        self._sig = sig

    
    def __call__(self, builder, args, loc = (None,)):
        res = self._imp(self._context, builder, self._sig, args, loc = loc)
        self._context.add_linking_libs(getattr(self, 'libs', ()))
        return res

    
    def __getattr__(self, item):
        return getattr(self._imp, item)

    
    def __repr__(self):
        return '<wrapped %s>' % repr(self._callable)



def _has_loc(fn):
    '''Does function *fn* take ``loc`` argument?
    '''
    sig = utils.pysignature(fn)
    return 'loc' in sig.parameters


class _wrap_missing_loc(object):
    
    def __init__(self, fn):
        self.func = fn

    
    def __call__(self):
        '''Wrap function for missing ``loc`` keyword argument.
        Otherwise, return the original *fn*.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return '<wrapped %s>' % self.func


_initialize_llvm_lock_event = (lambda : 
def enter_fn():
event.start_event('numba:llvm_lock')
def exit_fn():
event.end_event('numba:llvm_lock')ll.ffi.register_lock_callback(enter_fn, exit_fn))()
_initialize_llvm_lock_event()
