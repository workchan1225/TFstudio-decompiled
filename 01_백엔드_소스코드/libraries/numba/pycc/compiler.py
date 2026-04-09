# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compiler.pyc (Python 3.11)

import logging
import os
import sys
from llvmlite import ir
from llvmlite.binding import Linkage
from numba.pycc import llvm_types as lt
from numba.core.cgutils import create_constant_array
from numba.core.compiler import compile_extra, Flags
from numba.core.compiler_lock import global_compiler_lock
from numba.core.registry import cpu_target
from numba.core.runtime import nrtdynmod
from numba.core import cgutils
from numba.core.environment import lookup_environment
logger = logging.getLogger(__name__)
__all__ = [
    'Compiler']
NULL = ir.Constant(lt._void_star, None)
ZERO = ir.Constant(lt._int32, 0)
ONE = ir.Constant(lt._int32, 1)
METH_VARARGS_AND_KEYWORDS = ir.Constant(lt._int32, 3)

def get_header():
    import numpy
    import textwrap
    return textwrap.dedent('    #include <stdint.h>\n\n    #ifndef HAVE_LONGDOUBLE\n        #define HAVE_LONGDOUBLE %d\n    #endif\n\n    typedef struct {\n        float real;\n        float imag;\n    } complex64;\n\n    typedef struct {\n        double real;\n        double imag;\n    } complex128;\n\n    #if HAVE_LONGDOUBLE\n    typedef struct {\n        long double real;\n        long double imag;\n    } complex256;\n    #endif\n\n    typedef float float32;\n    typedef double float64;\n    #if HAVE_LONGDOUBLE\n    typedef long double float128;\n    #endif\n    ' % hasattr(numpy, 'complex256'))


class ExportEntry(object):
    '''
    A simple record for exporting symbols.
    '''
    
    def __init__(self, symbol, signature, function):
        self.symbol = symbol
        self.signature = signature
        self.function = function

    
    def __repr__(self):
        return f'''ExportEntry({self.symbol!r}, {self.signature!r})'''



class _ModuleCompiler(object):
    '''A base class to compile Python modules to a single shared library or
    extension module.

    :param export_entries: a list of ExportEntry instances.
    :param module_name: the name of the exported module.
    '''
    method_def_ty = ir.LiteralStructType((lt._int8_star, lt._void_star, lt._int32, lt._int8_star))
    method_def_ptr = ir.PointerType(method_def_ty)
    env_def_ty = ir.LiteralStructType((lt._void_star, lt._int32, lt._void_star, lt._void_star, lt._int32))
    env_def_ptr = ir.PointerType(env_def_ty)
    
    def __init__(self, export_entries, module_name, use_nrt = (False,), **aot_options):
        self.module_name = module_name
        self.export_python_wrap = False
        self.dll_exports = []
        self.export_entries = export_entries
        self.external_init_function = None
        self.use_nrt = use_nrt
        self.typing_context = cpu_target.typing_context
    # WARNING: Decompyle incomplete

    
    def _mangle_method_symbol(self, func_name):
        return f'''._pycc_method_{func_name!s}'''

    
    def _emit_python_wrapper(self, llvm_module):
        '''Emit generated Python wrapper and extension module code.
        '''
        raise NotImplementedError

    _cull_exports = (lambda self: self.exported_function_types = { }self.function_environments = { }self.environment_gvs = { }self.extra_environments = { }codegen = self.context.codegen()library = codegen.create_library(self.module_name)flags = Flags()flags.no_compile = Trueif not self.export_python_wrap:
flags.no_cpython_wrapper = Trueflags.no_cfunc_wrapper = Trueif self.use_nrt:
flags.nrt = True(nrt_module, _) = nrtdynmod.create_nrt_module(self.context)library.add_ir_module(nrt_module)# WARNING: Decompyle incomplete
)()
    
    def write_llvm_bitcode(self, output, wrap = (False,), **kws):
        self.export_python_wrap = wrap
        library = self._cull_exports()
        fout = open(output, 'wb')
        fout.write(library.emit_bitcode())
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def write_native_object(self, output, wrap = (False,), **kws):
        self.export_python_wrap = wrap
        library = self._cull_exports()
        fout = open(output, 'wb')
        fout.write(library.emit_native_object())
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def emit_type(self, tyobj):
        ret_val = str(tyobj)
        if 'int' in ret_val and ret_val.endswith(('8', '16', '32', '64')):
            ret_val += '_t'
        return ret_val

    
    def emit_header(self, output):
        pass
    # WARNING: Decompyle incomplete

    
    def _emit_method_array(self, llvm_module):
        '''
        Collect exported methods and emit a PyMethodDef array.

        :returns: a pointer to the PyMethodDef array.
        '''
        method_defs = []
        for entry in self.export_entries:
            name = entry.symbol
            llvm_func_name = self._mangle_method_symbol(name)
            fnty = self.exported_function_types[entry]
            lfunc = ir.Function(llvm_module, fnty, llvm_func_name)
            method_name = self.context.insert_const_string(llvm_module, name)
            method_def_const = ir.Constant.literal_struct((method_name, ir.Constant.bitcast(lfunc, lt._void_star), METH_VARARGS_AND_KEYWORDS, NULL))
            method_defs.append(method_def_const)
            sentinel = ir.Constant.literal_struct([
                NULL,
                NULL,
                ZERO,
                NULL])
            method_defs.append(sentinel)
            method_array_init = create_constant_array(self.method_def_ty, method_defs)
            method_array = cgutils.add_global_variable(llvm_module, method_array_init.type, '.module_methods')
            method_array.initializer = method_array_init
            method_array.linkage = 'internal'
            method_array_ptr = ir.Constant.gep(method_array, [
                ZERO,
                ZERO])
            return method_array_ptr

    
    def _emit_environment_array(self, llvm_module, builder, pyapi):
        '''
        Emit an array of env_def_t structures (see modulemixin.c)
        storing the pickled environment constants for each of the
        exported functions.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _emit_envgvs_array(self, llvm_module, builder, pyapi):
        '''
        Emit an array of Environment pointers that needs to be filled at
        initialization.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _emit_module_init_code(self, llvm_module, builder, modobj, method_array, env_array, envgv_array):
        '''
        Emit call to "external" init function, if any.
        '''
        if self.external_init_function:
            fnty = ir.FunctionType(lt._int32, [
                modobj.type,
                self.method_def_ptr,
                self.env_def_ptr,
                envgv_array.type])
            fn = ir.Function(llvm_module, fnty, self.external_init_function)
            return builder.call(fn, [
                modobj,
                method_array,
                env_array,
                envgv_array])



class ModuleCompiler(_ModuleCompiler):
    
    _ptr_fun = lambda ret, *args: ir.PointerType(ir.FunctionType(ret, args))
    visitproc_ty = _ptr_fun(lt._int8, lt._pyobject_head_p)
    inquiry_ty = _ptr_fun(lt._int8, lt._pyobject_head_p)
    traverseproc_ty = _ptr_fun(lt._int8, lt._pyobject_head_p, visitproc_ty, lt._void_star)
    freefunc_ty = _ptr_fun(lt._int8, lt._void_star)
    m_init_ty = _ptr_fun(lt._int8)
    _char_star = lt._int8_star
    module_def_base_ty = ir.LiteralStructType((lt._pyobject_head, m_init_ty, lt._llvm_py_ssize_t, lt._pyobject_head_p))
    module_def_ty = ir.LiteralStructType((module_def_base_ty, _char_star, _char_star, lt._llvm_py_ssize_t, _ModuleCompiler.method_def_ptr, inquiry_ty, traverseproc_ty, inquiry_ty, freefunc_ty))
    module_create_definition = (lambda self: signature = ir.FunctionType(lt._pyobject_head_p, (ir.PointerType(self.module_def_ty), lt._int32))name = 'PyModule_Create2'if lt._trace_refs_:
name += 'TraceRefs'(signature, name))()
    module_init_definition = (lambda self: signature = ir.FunctionType(lt._pyobject_head_p, ())(signature, 'PyInit_' + self.module_name))()
    
    def _emit_python_wrapper(self, llvm_module):
        pass
    # WARNING: Decompyle incomplete
