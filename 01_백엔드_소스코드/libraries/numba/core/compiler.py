# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compiler.pyc (Python 3.11)

from collections import namedtuple
import copy
import warnings
from numba.core.tracing import event
from numba.core import errors, interpreter, bytecode, postproc, config, callconv, cpu
from numba.parfors.parfor import ParforDiagnostics
from numba.core.errors import CompilerError
from numba.core.environment import lookup_environment
from numba.core.compiler_machinery import PassManager
from numba.core.untyped_passes import ExtractByteCode, TranslateByteCode, FixupArgs, IRProcessing, DeadBranchPrune, RewriteSemanticConstants, InlineClosureLikes, GenericRewrites, WithLifting, InlineInlinables, FindLiterallyCalls, MakeFunctionToJitFunction, CanonicalizeLoopExit, CanonicalizeLoopEntry, LiteralUnroll, ReconstructSSA, RewriteDynamicRaises, LiteralPropagationSubPipelinePass
from numba.core.typed_passes import NopythonTypeInference, AnnotateTypes, NopythonRewrites, PreParforPass, ParforPass, DumpParforDiagnostics, IRLegalization, NoPythonBackend, InlineOverloads, PreLowerStripPhis, NativeLowering, NativeParforLowering, NoPythonSupportedFeatureValidation, ParforFusionPass, ParforPreLoweringPass
from numba.core.object_mode_passes import ObjectModeFrontEnd, ObjectModeBackEnd
from numba.core.targetconfig import TargetConfig, Option, ConfigStack

class Flags(TargetConfig):
    __slots__ = ()
    enable_looplift = Option(type = bool, default = False, doc = 'Enable loop-lifting')
    enable_pyobject = Option(type = bool, default = False, doc = 'Enable pyobject mode (in general)')
    enable_pyobject_looplift = Option(type = bool, default = False, doc = 'Enable pyobject mode inside lifted loops')
    enable_ssa = Option(type = bool, default = True, doc = 'Enable SSA')
    force_pyobject = Option(type = bool, default = False, doc = 'Force pyobject mode inside the whole function')
    release_gil = Option(type = bool, default = False, doc = 'Release GIL inside the native function')
    no_compile = Option(type = bool, default = False, doc = 'TODO')
    debuginfo = Option(type = bool, default = False, doc = 'TODO')
    boundscheck = Option(type = bool, default = False, doc = 'TODO')
    forceinline = Option(type = bool, default = False, doc = 'Force inlining of the function. Overrides _dbg_optnone.')
    no_cpython_wrapper = Option(type = bool, default = False, doc = 'TODO')
    no_cfunc_wrapper = Option(type = bool, default = False, doc = 'TODO')
    auto_parallel = Option(type = cpu.ParallelOptions, default = cpu.ParallelOptions(False), doc = 'Enable automatic parallel optimization, can be fine-tuned by\ntaking a dictionary of sub-options instead of a boolean, see parfor.py for\ndetail')
    nrt = Option(type = bool, default = False, doc = 'TODO')
    no_rewrites = Option(type = bool, default = False, doc = 'TODO')
    error_model = Option(type = str, default = 'python', doc = 'TODO')
    fastmath = Option(type = cpu.FastMathOptions, default = cpu.FastMathOptions(False), doc = 'TODO')
    noalias = Option(type = bool, default = False, doc = 'TODO')
    inline = Option(type = cpu.InlineOptions, default = cpu.InlineOptions('never'), doc = 'TODO')
    dbg_extend_lifetimes = Option(type = bool, default = False, doc = 'Extend variable lifetime for debugging. This automatically turns on with debug=True.')
    dbg_optnone = Option(type = bool, default = False, doc = 'Disable optimization for debug. Equivalent to adding optnone attribute in the LLVM Function.')
    dbg_directives_only = Option(type = bool, default = False, doc = 'Make debug emissions directives-only. Used when generating lineinfo.')

DEFAULT_FLAGS = Flags()
DEFAULT_FLAGS.nrt = True
CR_FIELDS = [
    'typing_context',
    'target_context',
    'entry_point',
    'typing_error',
    'type_annotation',
    'signature',
    'objectmode',
    'lifted',
    'fndesc',
    'library',
    'call_helper',
    'environment',
    'metadata',
    'reload_init',
    'referenced_envs']

def CompileResult():
    '''CompileResult'''
    __doc__ = '\n    A structure holding results from the compilation of a function.\n    '
    __slots__ = ()
    
    def _reduce(self):
        '''
        Reduce a CompileResult to picklable components.
        '''
        libdata = self.library.serialize_using_object_code()
        typeann = str(self.type_annotation)
        fndesc = self.fndesc
        fndesc.typemap = None
        fndesc.calltypes = None
        referenced_envs = self._find_referenced_environments()
        return (libdata, self.fndesc, self.environment, self.signature, self.objectmode, self.lifted, typeann, self.reload_init, tuple(referenced_envs))

    
    def _find_referenced_environments(self):
        '''Returns a list of referenced environments
        '''
        mod = self.library._final_module
        referenced_envs = []
    # WARNING: Decompyle incomplete

    _rebuild = (lambda cls, target_context, libdata, fndesc, env, signature, objectmode, lifted, typeann, reload_init, referenced_envs: if reload_init:
for fn in reload_init:
fn()library = target_context.codegen().unserialize_library(libdata)cfunc = target_context.get_executable(library, fndesc, env)cr = cls(target_context = target_context, typing_context = target_context.typing_context, library = library, environment = env, entry_point = cfunc, fndesc = fndesc, type_annotation = typeann, signature = signature, objectmode = objectmode, lifted = lifted, typing_error = None, call_helper = None, metadata = None, reload_init = reload_init, referenced_envs = referenced_envs)for env in referenced_envs:
library.codegen.set_env(env.env_name, env)cr)()
    codegen = (lambda self: self.target_context.codegen())()
    
    def dump(self, tab = ('',)):
        print(f'''{tab}DUMP {type(self).__name__} {self.entry_point}''')
        self.signature.dump(tab = tab + '  ')
        print(f'''{tab}END DUMP''')


CompileResult = <NODE:27>(CompileResult, 'CompileResult', namedtuple('_CompileResult', CR_FIELDS))
_LowerResult = namedtuple('_LowerResult', [
    'fndesc',
    'call_helper',
    'cfunc',
    'env'])

def sanitize_compile_result_entries(entries):
    keys = set(entries.keys())
    fieldset = set(CR_FIELDS)
    badnames = keys - fieldset
# WARNING: Decompyle incomplete


def compile_result(**entries):
    entries = sanitize_compile_result_entries(entries)
# WARNING: Decompyle incomplete


def run_frontend(func, inline_closures, emit_dels = (False, False)):
    """
    Run the compiler frontend over the given Python function, and return
    the function's canonical Numba IR.

    If inline_closures is Truthy then closure inlining will be run
    If emit_dels is Truthy the ir.Del nodes will be emitted appropriately
    """
    func_id = bytecode.FunctionIdentity.from_function(func)
    interp = interpreter.Interpreter(func_id)
    bc = bytecode.ByteCode(func_id = func_id)
    func_ir = interp.interpret(bc)
    if inline_closures:
        InlineClosureCallPass = InlineClosureCallPass
        import numba.core.inline_closurecall
        inline_pass = InlineClosureCallPass(func_ir, cpu.ParallelOptions(False), { }, False)
        inline_pass.run()
    post_proc = postproc.PostProcessor(func_ir)
    post_proc.run(emit_dels)
    return func_ir


class _CompileStatus(object):
    '''
    Describes the state of compilation. Used like a C record.
    '''
    __slots__ = [
        'fail_reason',
        'can_fallback']
    
    def __init__(self, can_fallback):
        self.fail_reason = None
        self.can_fallback = can_fallback

    
    def __repr__(self):
        vals = []
        for k in self.__slots__:
            vals.append('{k}={v}'.format(k = k, v = getattr(self, k)))
            return ', '.join(vals)



class _EarlyPipelineCompletion(Exception):
    '''
    Raised to indicate that a pipeline has completed early
    '''
    
    def __init__(self, result):
        self.result = result



class StateDict(dict):
    '''
    A dictionary that has an overloaded getattr and setattr to permit getting
    and setting key/values through the use of attributes.
    '''
    
    def __getattr__(self, attr):
        
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(attr)


    
    def __setattr__(self, attr, value):
        self[attr] = value



def _make_subtarget(targetctx, flags):
    '''
    Make a new target context from the given target context and flags.
    '''
    subtargetoptions = { }
    if flags.debuginfo:
        subtargetoptions['enable_debuginfo'] = True
    if flags.boundscheck:
        subtargetoptions['enable_boundscheck'] = True
    if flags.nrt:
        subtargetoptions['enable_nrt'] = True
    if flags.auto_parallel:
        subtargetoptions['auto_parallel'] = flags.auto_parallel
    if flags.fastmath:
        subtargetoptions['fastmath'] = flags.fastmath
    error_model = callconv.create_error_model(flags.error_model, targetctx)
    subtargetoptions['error_model'] = error_model
# WARNING: Decompyle incomplete


class CompilerBase(object):
    '''
    Stores and manages states for the compiler
    '''
    
    def __init__(self, typingctx, targetctx, library, args, return_type, flags, locals):
        config.reload_config()
        typingctx.refresh()
        targetctx.refresh()
        self.state = StateDict()
        self.state.typingctx = typingctx
        self.state.targetctx = _make_subtarget(targetctx, flags)
        self.state.library = library
        self.state.args = args
        self.state.return_type = return_type
        self.state.flags = flags
        self.state.locals = locals
        self.state.bc = None
        self.state.func_id = None
        self.state.func_ir = None
        self.state.lifted = None
        self.state.lifted_from = None
        self.state.typemap = None
        self.state.calltypes = None
        self.state.type_annotation = None
        self.state.metadata = { }
        self.state.reload_init = []
        self.state.pipeline = self
        self.state.parfor_diagnostics = ParforDiagnostics()
        self.state.metadata['parfor_diagnostics'] = self.state.parfor_diagnostics
        self.state.metadata['parfors'] = { }
        self.state.status = _CompileStatus(can_fallback = self.state.flags.enable_pyobject)

    
    def compile_extra(self, func):
        self.state.func_id = bytecode.FunctionIdentity.from_function(func)
        ExtractByteCode().run_pass(self.state)
        self.state.lifted = ()
        self.state.lifted_from = None
        return self._compile_bytecode()

    
    def compile_ir(self, func_ir, lifted, lifted_from = ((), None)):
        self.state.func_id = func_ir.func_id
        self.state.lifted = lifted
        self.state.lifted_from = lifted_from
        self.state.func_ir = func_ir
        self.state.nargs = self.state.func_ir.arg_count
        FixupArgs().run_pass(self.state)
        return self._compile_ir()

    
    def define_pipelines(self):
        '''Child classes override this to customize the pipelines in use.
        '''
        raise NotImplementedError()

    
    def _compile_core(self):
        '''
        Populate and run compiler pipeline
        '''
        ConfigStack().enter(self.state.flags.copy())
        pms = self.define_pipelines()
    # WARNING: Decompyle incomplete

    
    def _compile_bytecode(self):
        '''
        Populate and run pipeline for bytecode input
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _compile_ir(self):
        '''
        Populate and run pipeline for IR input
        '''
        pass
    # WARNING: Decompyle incomplete



class Compiler(CompilerBase):
    '''The default compiler
    '''
    
    def define_pipelines(self):
        if self.state.flags.force_pyobject:
            return [
                DefaultPassBuilder.define_objectmode_pipeline(self.state)]
        return [
            None.define_nopython_pipeline(self.state)]



class DefaultPassBuilder(object):
    '''
    This is the default pass builder, it contains the "classic" default
    pipelines as pre-canned PassManager instances:
      - nopython
      - objectmode
      - interpreted
      - typed
      - untyped
      - nopython lowering
    '''
    define_nopython_pipeline = (lambda state, name = ('nopython',): dpb = DefaultPassBuilderpm = PassManager(name)untyped_passes = dpb.define_untyped_pipeline(state)pm.passes.extend(untyped_passes.passes)typed_passes = dpb.define_typed_pipeline(state)pm.passes.extend(typed_passes.passes)lowering_passes = dpb.define_nopython_lowering_pipeline(state)pm.passes.extend(lowering_passes.passes)pm.finalize()pm)()
    define_nopython_lowering_pipeline = (lambda state, name = ('nopython_lowering',): pm = PassManager(name)pm.add_pass(NoPythonSupportedFeatureValidation, 'ensure features that are in use are in a valid form')pm.add_pass(IRLegalization, 'ensure IR is legal prior to lowering')pm.add_pass(AnnotateTypes, 'annotate types')if state.flags.auto_parallel.enabled:
pm.add_pass(NativeParforLowering, 'native parfor lowering')else:
pm.add_pass(NativeLowering, 'native lowering')pm.add_pass(NoPythonBackend, 'nopython mode backend')pm.add_pass(DumpParforDiagnostics, 'dump parfor diagnostics')pm.finalize()pm)()
    define_parfor_gufunc_nopython_lowering_pipeline = (lambda state, name = ('parfor_gufunc_nopython_lowering',): pm = PassManager(name)pm.add_pass(NoPythonSupportedFeatureValidation, 'ensure features that are in use are in a valid form')pm.add_pass(IRLegalization, 'ensure IR is legal prior to lowering')pm.add_pass(AnnotateTypes, 'annotate types')if state.flags.auto_parallel.enabled:
pm.add_pass(NativeParforLowering, 'native parfor lowering')else:
pm.add_pass(NativeLowering, 'native lowering')pm.add_pass(NoPythonBackend, 'nopython mode backend')pm.finalize()pm)()
    define_typed_pipeline = (lambda state, name = ('typed',): pm = PassManager(name)pm.add_pass(NopythonTypeInference, 'nopython frontend')pm.add_pass(PreLowerStripPhis, 'remove phis nodes')pm.add_pass(InlineOverloads, 'inline overloaded functions')if state.flags.auto_parallel.enabled:
pm.add_pass(PreParforPass, 'Preprocessing for parfors')if not state.flags.no_rewrites:
pm.add_pass(NopythonRewrites, 'nopython rewrites')if state.flags.auto_parallel.enabled:
pm.add_pass(ParforPass, 'convert to parfors')pm.add_pass(ParforFusionPass, 'fuse parfors')pm.add_pass(ParforPreLoweringPass, 'parfor prelowering')pm.finalize()pm)()
    define_parfor_gufunc_pipeline = (lambda state, name = ('parfor_gufunc_typed',): pm = PassManager(name)# WARNING: Decompyle incomplete
)()
    define_untyped_pipeline = (lambda state, name = ('untyped',): pm = PassManager(name)# WARNING: Decompyle incomplete
)()
    define_objectmode_pipeline = (lambda state, name = ('object',): pm = PassManager(name)# WARNING: Decompyle incomplete
)()


def compile_extra(typingctx, targetctx, func, args, return_type, flags, locals, library, pipeline_class = (None, Compiler)):
    '''Compiler entry point

    Parameter
    ---------
    typingctx :
        typing context
    targetctx :
        target context
    func : function
        the python function to be compiled
    args : tuple, list
        argument types
    return_type :
        Use ``None`` to indicate void return
    flags : numba.compiler.Flags
        compiler flags
    library : numba.codegen.CodeLibrary
        Used to store the compiled code.
        If it is ``None``, a new CodeLibrary is used.
    pipeline_class : type like numba.compiler.CompilerBase
        compiler pipeline
    '''
    pipeline = pipeline_class(typingctx, targetctx, library, args, return_type, flags, locals)
    return pipeline.compile_extra(func)


def compile_ir(typingctx, targetctx, func_ir, args, return_type, flags, locals, lifted, lifted_from, is_lifted_loop, library, pipeline_class = ((), None, False, None, Compiler)):
    '''
    Compile a function with the given IR.

    For internal use only.
    '''
    pass
# WARNING: Decompyle incomplete


def compile_internal(typingctx, targetctx, library, func, args, return_type, flags, locals):
    '''
    For internal use only.
    '''
    pipeline = Compiler(typingctx, targetctx, library, args, return_type, flags, locals)
    return pipeline.compile_extra(func)
