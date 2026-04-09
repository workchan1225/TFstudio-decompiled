# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compiler.pyc (Python 3.11)

from llvmlite import ir
from numba.core.typing.templates import ConcreteTemplate
from numba.core import types, typing, funcdesc, config, compiler, sigutils
from numba.core.compiler import sanitize_compile_result_entries, CompilerBase, DefaultPassBuilder, Flags, Option, CompileResult
from numba.core.compiler_lock import global_compiler_lock
from numba.core.compiler_machinery import LoweringPass, PassManager, register_pass
from numba.core.errors import NumbaInvalidConfigWarning
from numba.core.typed_passes import IRLegalization, NativeLowering, AnnotateTypes
from warnings import warn
from numba.cuda.api import get_current_device
from numba.cuda.target import CUDACABICallConv

def _nvvm_options_type(x):
    pass
# WARNING: Decompyle incomplete


class CUDAFlags(Flags):
    nvvm_options = Option(type = _nvvm_options_type, default = None, doc = 'NVVM options')
    compute_capability = Option(type = tuple, default = None, doc = 'Compute Capability')


class CUDACompileResult(CompileResult):
    entry_point = (lambda self: id(self))()


def cuda_compile_result(**entries):
    entries = sanitize_compile_result_entries(entries)
# WARNING: Decompyle incomplete

CUDABackend = <NODE:12>()
CreateLibrary = <NODE:12>()

class CUDACompiler(CompilerBase):
    
    def define_pipelines(self):
        dpb = DefaultPassBuilder
        pm = PassManager('cuda')
        untyped_passes = dpb.define_untyped_pipeline(self.state)
        pm.passes.extend(untyped_passes.passes)
        typed_passes = dpb.define_typed_pipeline(self.state)
        pm.passes.extend(typed_passes.passes)
        lowering_passes = self.define_cuda_lowering_pipeline(self.state)
        pm.passes.extend(lowering_passes.passes)
        pm.finalize()
        return [
            pm]

    
    def define_cuda_lowering_pipeline(self, state):
        pm = PassManager('cuda_lowering')
        pm.add_pass(IRLegalization, 'ensure IR is legal prior to lowering')
        pm.add_pass(AnnotateTypes, 'annotate types')
        pm.add_pass(CreateLibrary, 'create library')
        pm.add_pass(NativeLowering, 'native lowering')
        pm.add_pass(CUDABackend, 'cuda backend')
        pm.finalize()
        return pm


compile_cuda = (lambda pyfunc, return_type, args, debug, lineinfo, inline, fastmath, nvvm_options, cc = (False, False, False, False, None, None): pass# WARNING: Decompyle incomplete
)()

def cabi_wrap_function(context, lib, fndesc, wrapper_function_name, nvvm_options):
    '''
    Wrap a Numba ABI function in a C ABI wrapper at the NVVM IR level.

    The C ABI wrapper will have the same name as the source Python function.
    '''
    library = lib.codegen.create_library(f'''{lib.name}_function_''', entry_name = wrapper_function_name, nvvm_options = nvvm_options)
    library.add_linking_library(lib)
    argtypes = fndesc.argtypes
    restype = fndesc.restype
    c_call_conv = CUDACABICallConv(context)
    wrapfnty = c_call_conv.get_function_type(restype, argtypes)
    fnty = context.call_conv.get_function_type(fndesc.restype, argtypes)
    wrapper_module = context.create_module('cuda.cabi.wrapper')
    func = ir.Function(wrapper_module, fnty, fndesc.llvm_func_name)
    wrapfn = ir.Function(wrapper_module, wrapfnty, wrapper_function_name)
    builder = ir.IRBuilder(wrapfn.append_basic_block(''))
    arginfo = context.get_arg_packer(argtypes)
    callargs = arginfo.from_arguments(builder, wrapfn.args)
    (_, return_value) = context.call_conv.call_function(builder, func, restype, argtypes, callargs)
    builder.ret(return_value)
    library.add_ir_module(wrapper_module)
    library.finalize()
    return library

compile = (lambda pyfunc, sig, debug, lineinfo, device, fastmath, cc, opt, abi, abi_info, output = (False, False, True, False, None, True, 'c', None, 'ptx'): if abi not in ('numba', 'c'):
raise NotImplementedError(f'''Unsupported ABI: {abi}''')if not abi == 'c' and device:
raise NotImplementedError('The C ABI is not supported for kernels')if output not in ('ptx', 'ltoir'):
raise NotImplementedError(f'''Unsupported output type: {output}''')if debug and opt:
msg = 'debug=True with opt=True (the default) is not supported by CUDA. This may result in a crash - set debug=False or opt=False.'warn(NumbaInvalidConfigWarning(msg))lto = output == 'ltoir'if not abi_info:
abi_info = dict()nvvm_options = {
'fastmath': fastmath,
'opt': 3 if opt else 0 }if lto:
nvvm_options['gen-lto'] = None(args, return_type) = sigutils.normalize_signature(sig)if not cc:
cc = config.CUDA_DEFAULT_PTX_CCcres = compile_cuda(pyfunc, return_type, args, debug = debug, lineinfo = lineinfo, fastmath = fastmath, nvvm_options = nvvm_options, cc = cc)resty = cres.signature.return_typeif resty and device and resty != types.void:
raise TypeError('CUDA kernel must have void return type.')tgt = cres.target_contextif device:
lib = cres.libraryif abi == 'c':
wrapper_name = abi_info.get('abi_name', pyfunc.__name__)lib = cabi_wrap_function(tgt, lib, cres.fndesc, wrapper_name, nvvm_options)else:
code = pyfunc.__code__filename = code.co_filenamelinenum = code.co_firstlineno(lib, kernel) = tgt.prepare_cuda_kernel(cres.library, cres.fndesc, debug, lineinfo, nvvm_options, filename, linenum)if lto:
code = lib.get_ltoir(cc = cc)else:
code = lib.get_asm_str(cc = cc)(code, resty))()

def compile_for_current_device(pyfunc, sig, debug, lineinfo, device, fastmath, opt, abi, abi_info, output = (False, False, True, False, True, 'c', None, 'ptx')):
    """Compile a Python function to PTX or LTO-IR for a given signature for the
    current device's compute capabilility. This calls :func:`compile` with an
    appropriate ``cc`` value for the current device."""
    cc = get_current_device().compute_capability
    return compile(pyfunc, sig, debug = debug, lineinfo = lineinfo, device = device, fastmath = fastmath, cc = cc, opt = opt, abi = abi, abi_info = abi_info, output = output)


def compile_ptx(pyfunc, sig, debug, lineinfo, device, fastmath, cc, opt, abi, abi_info = (False, False, False, False, None, True, 'numba', None)):
    """Compile a Python function to PTX for a given signature. See
    :func:`compile`. The defaults for this function are to compile a kernel
    with the Numba ABI, rather than :func:`compile`'s default of compiling a
    device function with the C ABI."""
    return compile(pyfunc, sig, debug = debug, lineinfo = lineinfo, device = device, fastmath = fastmath, cc = cc, opt = opt, abi = abi, abi_info = abi_info, output = 'ptx')


def compile_ptx_for_current_device(pyfunc, sig, debug, lineinfo, device, fastmath, opt, abi, abi_info = (False, False, False, False, True, 'numba', None)):
    """Compile a Python function to PTX for a given signature for the current
    device's compute capabilility. See :func:`compile_ptx`."""
    cc = get_current_device().compute_capability
    return compile_ptx(pyfunc, sig, debug = debug, lineinfo = lineinfo, device = device, fastmath = fastmath, cc = cc, opt = opt, abi = abi, abi_info = abi_info)


def declare_device_function(name, restype, argtypes):
    return declare_device_function_template(name, restype, argtypes).key


def declare_device_function_template(name, restype, argtypes):
    pass
# WARNING: Decompyle incomplete


class ExternFunction(object):
    
    def __init__(self, name, sig):
        self.name = name
        self.sig = sig
