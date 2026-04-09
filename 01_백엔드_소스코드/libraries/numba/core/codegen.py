# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: codegen.pyc (Python 3.11)

import warnings
import functools
import locale
import weakref
import ctypes
import html
import textwrap
from llvmlite.binding import binding as ll
from llvmlite.ir import ir as llvmir
from abc import abstractmethod, ABCMeta
from numba.core import utils, config, cgutils
from numba.core.llvm_bindings import create_pass_builder
from numba.core.runtime.nrtopt import remove_redundant_nrt_refct
from numba.core.runtime import rtsys
from numba.core.compiler_lock import require_global_compiler_lock
from numba.core.errors import NumbaInvalidConfigWarning
from numba.misc.inspection import disassemble_elf_to_cfg
from numba.misc.llvm_pass_timings import PassTimingsCollection
_x86arch = frozenset([
    'x86',
    'i386',
    'i486',
    'i586',
    'i686',
    'i786',
    'i886',
    'i986'])

def _is_x86(triple):
    arch = triple.split('-')[0]
    return arch in _x86arch


def _parse_refprune_flags():
    '''Parse refprune flags from the `config`.

    Invalid values are ignored an warn via a `NumbaInvalidConfigWarning`
    category.

    Returns
    -------
    flags : llvmlite.binding.RefPruneSubpasses
    '''
    flags = config.LLVM_REFPRUNE_FLAGS.split(',')
    if not flags:
        return 0
    val = None
    for item in flags:
        item = item.strip()
        val |= getattr(ll.RefPruneSubpasses, item.upper())
        except AttributeError:
            warnings.warn(f'''invalid refprune flags {item!r}''', NumbaInvalidConfigWarning)
            continue
        return val


def dump(header, body, lang):
    pass
# WARNING: Decompyle incomplete


class _CFG(object):
    '''
    Wraps the CFG graph for different display method.

    Instance of the class can be stringified (``__repr__`` is defined) to get
    the graph in DOT format.  The ``.display()`` method plots the graph in
    PDF.  If in IPython notebook, the returned image can be inlined.
    '''
    
    def __init__(self, cres, name, py_func, **kwargs):
        self.cres = cres
        self.name = name
        self.py_func = py_func
        fn = cres.get_function(name)
        self.dot = ll.get_function_cfg(fn)
        self.kwargs = kwargs

    
    def pretty_printer(self, filename, view, render_format, highlight, interleave, strip_ir, show_key, fontsize = (None, None, None, True, False, False, True, 10)):
        '''
        "Pretty" prints the DOT graph of the CFG.
        For explanation of the parameters see the docstring for
        numba.core.dispatcher::inspect_cfg.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def display(self, filename, format, view = (None, 'pdf', False)):
        """
        Plot the CFG.  In IPython notebook, the return image object can be
        inlined.

        The *filename* option can be set to a specific path for the rendered
        output to write to.  If *view* option is True, the plot is opened by
        the system default application for the image format (PDF). *format* can
        be any valid format string accepted by graphviz, default is 'pdf'.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def _repr_svg_(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return self.dot



def CodeLibrary():
    '''CodeLibrary'''
    __doc__ = '\n    An interface for bundling LLVM code together and compiling it.\n    It is tied to a *codegen* instance (e.g. JITCPUCodegen) that will\n    determine how the LLVM code is transformed and linked together.\n    '
    _finalized = False
    _object_caching_enabled = False
    _disable_inspection = False
    
    def __init__(self = None, codegen = None, name = None):
        self._codegen = codegen
        self._name = name
        ptc_name = f'''{self.__class__.__name__}({self._name!r})'''
        self._recorded_timings = PassTimingsCollection(ptc_name)
        self._dynamic_globals = []
        self._reload_init = set()

    has_dynamic_globals = (lambda self: self._ensure_finalized()len(self._dynamic_globals) > 0)()
    recorded_timings = (lambda self: self._recorded_timings)()
    codegen = (lambda self: self._codegen)()
    name = (lambda self: self._name)()
    
    def __repr__(self):
        return '<Library %r at 0x%x>' % (self.name, id(self))

    
    def _raise_if_finalized(self):
        if self._finalized:
            raise RuntimeError(f'''operation impossible on finalized object {self!r}''')

    
    def _ensure_finalized(self):
        if not self._finalized:
            self.finalize()
            return None

    
    def create_ir_module(self, name):
        '''
        Create an LLVM IR module for use by this library.
        '''
        self._raise_if_finalized()
        ir_module = self._codegen._create_empty_module(name)
        return ir_module

    add_linking_library = (lambda self, library: pass)()
    add_ir_module = (lambda self, ir_module: pass)()
    finalize = (lambda self: pass)()
    get_function = (lambda self, name: pass)()
    get_llvm_str = (lambda self: pass)()
    get_asm_str = (lambda self: pass)()
    
    def enable_object_caching(self):
        self._object_caching_enabled = True
        self._compiled_object = None
        self._compiled = False

    
    def _get_compiled_object(self):
        if not self._object_caching_enabled:
            raise ValueError(f'''object caching not enabled in {self!s}''')
    # WARNING: Decompyle incomplete

    
    def _set_compiled_object(self, value):
        if not self._object_caching_enabled:
            raise ValueError(f'''object caching not enabled in {self!s}''')
        if self._compiled:
            raise ValueError(f'''library already compiled: {self!s}''')
        self._compiled_object = value
        self._disable_inspection = True


CodeLibrary = <NODE:27>(CodeLibrary, 'CodeLibrary', metaclass = ABCMeta)

class CPUCodeLibrary(CodeLibrary):
    pass
# WARNING: Decompyle incomplete


class AOTCodeLibrary(CPUCodeLibrary):
    
    def emit_native_object(self):
        '''
        Return this library as a native object (a bytestring) -- for example
        ELF under Linux.

        This function implicitly calls .finalize().
        '''
        self._ensure_finalized()
        return self._codegen._tm.emit_object(self._final_module)

    
    def emit_bitcode(self):
        '''
        Return this library as LLVM bitcode (a bytestring).

        This function implicitly calls .finalize().
        '''
        self._ensure_finalized()
        return self._final_module.as_bitcode()

    
    def _finalize_specific(self):
        pass



class JITCodeLibrary(CPUCodeLibrary):
    
    def get_pointer_to_function(self, name):
        '''
        Generate native code for function named *name* and return a pointer
        to the start of the function (as an integer).

        This function implicitly calls .finalize().

        Returns
        -------
        pointer : int
            - zero (null) if no symbol of *name* is defined by this code
              library.
            - non-zero if the symbol is defined.
        '''
        self._ensure_finalized()
        ee = self._codegen._engine
        if not ee.is_symbol_defined(name):
            return 0
        return None._codegen._engine.get_function_address(name)

    
    def _finalize_specific(self):
        self._codegen._scan_and_fix_unresolved_refs(self._final_module)
        self._recorded_timings.record_legacy('Finalize object')
        self._codegen._engine.finalize_object()
        None(None, None)
        return None
        with None:
            if not None:
                pass



class RuntimeLinker(object):
    '''
    For tracking unresolved symbols generated at runtime due to recursion.
    '''
    PREFIX = '.numba.unresolved$'
    
    def __init__(self):
        self._unresolved = utils.UniqueDict()
        self._defined = set()
        self._resolved = []

    
    def scan_unresolved_symbols(self, module, engine):
        '''
        Scan and track all unresolved external symbols in the module and
        allocate memory for it.
        '''
        prefix = self.PREFIX
        for gv in module.global_variables:
            if gv.name.startswith(prefix):
                sym = gv.name[len(prefix):]
                if engine.is_symbol_defined(gv.name):
                    continue
                abortfn = rtsys.library.get_pointer_to_function('nrt_unresolved_abort')
                ptr = ctypes.c_void_p(abortfn)
                engine.add_global_mapping(gv, ctypes.addressof(ptr))
                self._unresolved[sym] = ptr
            return None

    
    def scan_defined_symbols(self, module):
        '''
        Scan and track all defined symbols.
        '''
        for fn in module.functions:
            if not fn.is_declaration:
                self._defined.add(fn.name)
            return None

    
    def resolve(self, engine):
        '''
        Fix unresolved symbols if they are defined.
        '''
        pass
    # WARNING: Decompyle incomplete



def _proxy(old):
    pass
# WARNING: Decompyle incomplete


class JitEngine(object):
    """Wraps an ExecutionEngine to provide custom symbol tracking.
    Since the symbol tracking is incomplete  (doesn't consider
    loaded code object), we are not putting it in llvmlite.
    """
    
    def __init__(self, ee):
        self._ee = ee
        self._defined_symbols = set()

    
    def is_symbol_defined(self, name):
        '''Is the symbol defined in this session?
        '''
        return name in self._defined_symbols

    
    def _load_defined_symbols(self, mod):
        '''Extract symbols from the module
        '''
        for gsets in (mod.functions, mod.global_variables):
            return None

    
    def add_module(self, module):
        '''Override ExecutionEngine.add_module
        to keep info about defined symbols.
        '''
        self._load_defined_symbols(module)
        return self._ee.add_module(module)

    
    def add_global_mapping(self, gv, addr):
        '''Override ExecutionEngine.add_global_mapping
        to keep info about defined symbols.
        '''
        self._defined_symbols.add(gv.name)
        return self._ee.add_global_mapping(gv, addr)

    set_object_cache = _proxy(ll.ExecutionEngine.set_object_cache)
    finalize_object = _proxy(ll.ExecutionEngine.finalize_object)
    get_function_address = _proxy(ll.ExecutionEngine.get_function_address)
    get_global_value_address = _proxy(ll.ExecutionEngine.get_global_value_address)


def Codegen():
    '''Codegen'''
    __doc__ = '\n    Base Codegen class. It is expected that subclasses set the class attribute\n    ``_library_class``, indicating the CodeLibrary class for the target.\n\n    Subclasses should also initialize:\n\n    ``self._data_layout``: the data layout for the target.\n    ``self._target_data``: the binding layer ``TargetData`` for the target.\n    '
    _create_empty_module = (lambda self, name: pass)()
    _add_module = (lambda self, module: pass)()
    target_data = (lambda self: self._target_data)()
    
    def create_library(self, name, **kwargs):
        '''
        Create a :class:`CodeLibrary` object for use with this codegen
        instance.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def unserialize_library(self, serialized):
        return self._library_class._unserialize(self, serialized)


Codegen = <NODE:27>(Codegen, 'Codegen', metaclass = ABCMeta)

class CPUCodegen(Codegen):
    
    def __init__(self, module_name):
        initialize_llvm()
        self._data_layout = None
        self._llvm_module = ll.parse_assembly(str(self._create_empty_module(module_name)))
        self._llvm_module.name = 'global_codegen_module'
        self._rtlinker = RuntimeLinker()
        self._init(self._llvm_module)

    
    def _init(self, llvm_module):
        pass
    # WARNING: Decompyle incomplete

    
    def _create_empty_module(self, name):
        ir_module = llvmir.Module(cgutils.normalize_ir_text(name))
        ir_module.triple = ll.get_process_triple()
        if self._data_layout:
            ir_module.data_layout = self._data_layout
        return ir_module

    
    def _module_pass_manager(self, **kwargs):
        cost = kwargs.pop('cost', None)
    # WARNING: Decompyle incomplete

    
    def _function_pass_manager(self, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _pass_builder(self, **kwargs):
        opt_level = kwargs.pop('opt', config.OPT)
        loop_vectorize = kwargs.pop('loop_vectorize', config.LOOP_VECTORIZE)
        slp_vectorize = kwargs.pop('slp_vectorize', config.SLP_VECTORIZE)
    # WARNING: Decompyle incomplete

    
    def _check_llvm_bugs(self):
        '''
        Guard against some well-known LLVM bug(s).
        '''
        ir = '\n            define double @func()\n            {\n                ret double 1.23e+01\n            }\n            '
        mod = ll.parse_assembly(ir)
        ir_out = str(mod)
        if '12.3' in ir_out or '1.23' in ir_out:
            return None
        if None in ir_out:
            loc = locale.getlocale()
            raise RuntimeError(f'''LLVM will produce incorrect floating-point code in the current locale {loc!s}.\nPlease read https://numba.readthedocs.io/en/stable/user/faq.html#llvm-locale-bug for more information.''')
        raise AssertionError(f'''Unexpected IR:\n{ir_out!s}\n''')

    
    def magic_tuple(self):
        '''
        Return a tuple unambiguously describing the codegen behaviour.
        '''
        return (self._llvm_module.triple, self._get_host_cpu_name(), self._tm_features)

    
    def _scan_and_fix_unresolved_refs(self, module):
        self._rtlinker.scan_unresolved_symbols(module, self._engine)
        self._rtlinker.scan_defined_symbols(module)
        self._rtlinker.resolve(self._engine)

    
    def insert_unresolved_ref(self, builder, fnty, name):
        voidptr = llvmir.IntType(8).as_pointer()
        ptrname = self._rtlinker.PREFIX + name
        llvm_mod = builder.module
        
        try:
            fnptr = llvm_mod.get_global(ptrname)
        except KeyError:
            fnptr = llvmir.GlobalVariable(llvm_mod, voidptr, name = ptrname)
            fnptr.linkage = 'external'

        return builder.bitcast(builder.load(fnptr), fnty.as_pointer())

    
    def _get_host_cpu_name(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_host_cpu_features(self):
        pass
    # WARNING: Decompyle incomplete



class AOTCPUCodegen(CPUCodegen):
    '''
    A codegen implementation suitable for Ahead-Of-Time compilation
    (e.g. generation of object files).
    '''
    _library_class = AOTCodeLibrary
    
    def __init__(self, module_name, cpu_name = (None,)):
