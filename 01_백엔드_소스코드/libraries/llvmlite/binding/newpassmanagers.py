# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: newpassmanagers.pyc (Python 3.11)

from ctypes import c_bool, c_int, c_size_t, POINTER, Structure, byref, c_char_p
from collections import namedtuple
from enum import IntFlag
from llvmlite.binding import ffi

def create_new_module_pass_manager():
    return ModulePassManager()


def create_new_function_pass_manager():
    return FunctionPassManager()


def create_pass_builder(tm, pto):
    return PassBuilder(tm, pto)


def create_pipeline_tuning_options(speed_level, size_level = (2, 0)):
    return PipelineTuningOptions(speed_level, size_level)

_prunestats = namedtuple('PruneStats', 'basicblock diamond fanout fanout_raise')

class PruneStats(_prunestats):
    ''' Holds statistics from reference count pruning.
    '''
    
    def __add__(self, other):
        if not isinstance(other, PruneStats):
            msg = 'PruneStats can only be added to another PruneStats, got {}.'
            raise TypeError(msg.format(type(other)))
        return PruneStats(self.basicblock + other.basicblock, self.diamond + other.diamond, self.fanout + other.fanout, self.fanout_raise + other.fanout_raise)

    
    def __sub__(self, other):
        if not isinstance(other, PruneStats):
            msg = 'PruneStats can only be subtracted from another PruneStats, got {}.'
            raise TypeError(msg.format(type(other)))
        return PruneStats(self.basicblock - other.basicblock, self.diamond - other.diamond, self.fanout - other.fanout, self.fanout_raise - other.fanout_raise)



class _c_PruneStats(Structure):
    _fields_ = [
        ('basicblock', c_size_t),
        ('diamond', c_size_t),
        ('fanout', c_size_t),
        ('fanout_raise', c_size_t)]


def dump_refprune_stats(printout = (False,)):
    ''' Returns a namedtuple containing the current values for the refop pruning
    statistics. If kwarg `printout` is True the stats are printed to stderr,
    default is False.
    '''
    stats = _c_PruneStats(0, 0, 0, 0)
    do_print = c_bool(printout)
    ffi.lib.LLVMPY_DumpRefPruneStats(byref(stats), do_print)
    return PruneStats(stats.basicblock, stats.diamond, stats.fanout, stats.fanout_raise)


def set_time_passes(enable):
    '''Enable or disable the pass timers.

    Parameters
    ----------
    enable : bool
        Set to True to enable the pass timers.
        Set to False to disable the pass timers.
    '''
    ffi.lib.LLVMPY_SetTimePasses(c_bool(enable))


def report_and_reset_timings():
    '''Returns the pass timings report and resets the LLVM internal timers.

    Pass timers are enabled by ``set_time_passes()``. If the timers are not
    enabled, this function will return an empty string.

    Returns
    -------
    res : str
        LLVM generated timing report.
    '''
    buf = ffi.OutputString()
    ffi.lib.LLVMPY_ReportAndResetTimings(buf)
    None(None, None)
    return 
    with None:
        if not None, str(buf):
            pass


class RefPruneSubpasses(IntFlag):
    PER_BB = 1
    DIAMOND = 2
    FANOUT = 4
    FANOUT_RAISE = 8
    ALL = PER_BB | DIAMOND | FANOUT | FANOUT_RAISE


class NewPassManager:
    
    def __init__(self):
        if type(self) is NewPassManager:
            raise TypeError('Cannot instantiate NewPassManager directly')

    
    def run(self, IR, pb):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_RunNewModulePassManager(self, IR, pb)
            return None
        None.lib.LLVMPY_RunNewFunctionPassManager(self, IR, pb)

    
    def add_aa_eval_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddAAEvaluator(self)
            return None
        None.lib.LLVMPY_function_AddAAEvaluator(self)

    
    def add_simplify_cfg_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddSimplifyCFGPass(self)
            return None
        None.lib.LLVMPY_function_AddSimplifyCFGPass(self)

    
    def add_loop_unroll_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddLoopUnrollPass(self)
            return None
        None.lib.LLVMPY_function_AddLoopUnrollPass(self)

    
    def add_instruction_combine_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddInstCombinePass(self)
            return None
        None.lib.LLVMPY_function_AddInstCombinePass(self)

    
    def add_jump_threading_pass(self, threshold = (-1,)):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_AddJumpThreadingPass_module(self, threshold)
            return None
        None.lib.LLVMPY_AddJumpThreadingPass_function(self, threshold)

    
    def add_cfg_printer_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddCFGPrinterPass(self)
            return None
        None.lib.LLVMPY_function_AddCFGPrinterPass(self)

    
    def add_cfg_only_printer_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddCFGOnlyPrinterPass(self)
            return None
        None.lib.LLVMPY_function_AddCFGOnlyPrinterPass(self)

    
    def add_dom_printer_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddDomPrinter(self)
            return None
        None.lib.LLVMPY_function_AddDomPrinter(self)

    
    def add_dom_only_printer_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddDomOnlyPrinter(self)
            return None
        None.lib.LLVMPY_function_AddDomOnlyPrinter(self)

    
    def add_post_dom_printer_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddPostDomPrinter(self)
            return None
        None.lib.LLVMPY_function_AddPostDomPrinter(self)

    
    def add_post_dom_only_printer_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddPostDomOnlyPrinter(self)
            return None
        None.lib.LLVMPY_function_AddPostDomOnlyPrinter(self)

    
    def add_dom_viewer_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddDomViewer(self)
            return None
        None.lib.LLVMPY_function_AddDomViewer(self)

    
    def add_dom_only_viewer_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddDomOnlyViewer(self)
            return None
        None.lib.LLVMPY_function_AddDomOnlyViewer(self)

    
    def add_post_dom_viewer_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddPostDomViewer(self)
            return None
        None.lib.LLVMPY_function_AddPostDomViewer(self)

    
    def add_post_dom_only_viewer_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddPostDomOnlyViewer(self)
            return None
        None.lib.LLVMPY_function_AddPostDomOnlyViewer(self)

    
    def add_lint_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddLintPass(self)
            return None
        None.lib.LLVMPY_function_AddLintPass(self)

    
    def add_aggressive_dce_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddADCEPass(self)
            return None
        None.lib.LLVMPY_function_AddADCEPass(self)

    
    def add_break_critical_edges_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddBreakCriticalEdgesPass(self)
            return None
        None.lib.LLVMPY_function_AddBreakCriticalEdgesPass(self)

    
    def add_dead_store_elimination_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddDSEPass(self)
            return None
        None.lib.LLVMPY_function_AddDSEPass(self)

    
    def add_dead_code_elimination_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddDCEPass(self)
            return None
        None.lib.LLVMPY_function_AddDCEPass(self)

    
    def add_aggressive_instcombine_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddAggressiveInstCombinePass(self)
            return None
        None.lib.LLVMPY_function_AddAggressiveInstCombinePass(self)

    
    def add_lcssa_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddLCSSAPass(self)
            return None
        None.lib.LLVMPY_function_AddLCSSAPass(self)

    
    def add_new_gvn_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddNewGVNPass(self)
            return None
        None.lib.LLVMPY_function_AddNewGVNPass(self)

    
    def add_loop_simplify_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddLoopSimplifyPass(self)
            return None
        None.lib.LLVMPY_function_AddLoopSimplifyPass(self)

    
    def add_loop_unroll_and_jam_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddLoopUnrollAndJamPass(self)
            return None
        None.lib.LLVMPY_function_AddLoopUnrollAndJamPass(self)

    
    def add_sccp_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddSCCPPass(self)
            return None
        None.lib.LLVMPY_function_AddSCCPPass(self)

    
    def add_lower_atomic_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddLowerAtomicPass(self)
            return None
        None.lib.LLVMPY_function_AddLowerAtomicPass(self)

    
    def add_lower_invoke_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddLowerInvokePass(self)
            return None
        None.lib.LLVMPY_function_AddLowerInvokePass(self)

    
    def add_lower_switch_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddLowerSwitchPass(self)
            return None
        None.lib.LLVMPY_function_AddLowerSwitchPass(self)

    
    def add_mem_copy_opt_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddMemCpyOptPass(self)
            return None
        None.lib.LLVMPY_function_AddMemCpyOptPass(self)

    
    def add_unify_function_exit_nodes_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddUnifyFunctionExitNodesPass(self)
            return None
        None.lib.LLVMPY_function_AddUnifyFunctionExitNodesPass(self)

    
    def add_reassociate_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddReassociatePass(self)
            return None
        None.lib.LLVMPY_function_AddReassociatePass(self)

    
    def add_register_to_memory_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddRegToMemPass(self)
            return None
        None.lib.LLVMPY_function_AddRegToMemPass(self)

    
    def add_sroa_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddSROAPass(self)
            return None
        None.lib.LLVMPY_function_AddSROAPass(self)

    
    def add_sinking_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddSinkingPass(self)
            return None
        None.lib.LLVMPY_function_AddSinkingPass(self)

    
    def add_tail_call_elimination_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddTailCallElimPass(self)
            return None
        None.lib.LLVMPY_function_AddTailCallElimPass(self)

    
    def add_instruction_namer_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddInstructionNamerPass(self)
            return None
        None.lib.LLVMPY_function_AddInstructionNamerPass(self)

    
    def add_loop_deletion_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddLoopDeletionPass(self)
            return None
        None.lib.LLVMPY_function_AddLoopDeletionPass(self)

    
    def add_loop_strength_reduce_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddLoopStrengthReducePass(self)
            return None
        None.lib.LLVMPY_function_AddLoopStrengthReducePass(self)

    
    def add_loop_rotate_pass(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_module_AddLoopRotatePass(self)
            return None
        None.lib.LLVMPY_function_AddLoopRotatePass(self)

    
    def _dispose(self):
        if isinstance(self, ModulePassManager):
            ffi.lib.LLVMPY_DisposeNewModulePassManger(self)
            return None
        None.lib.LLVMPY_DisposeNewFunctionPassManger(self)



class ModulePassManager(NewPassManager, ffi.ObjectRef):
    pass
# WARNING: Decompyle incomplete


class FunctionPassManager(NewPassManager, ffi.ObjectRef):
    pass
# WARNING: Decompyle incomplete


class PipelineTuningOptions(ffi.ObjectRef):
    pass
# WARNING: Decompyle incomplete


class TimePassesHandler(ffi.ObjectRef):
    pass
# WARNING: Decompyle incomplete


class PassBuilder(ffi.ObjectRef):
    pass
# WARNING: Decompyle incomplete

ffi.lib.LLVMPY_DumpRefPruneStats.argtypes = [
    POINTER(_c_PruneStats),
    c_bool]
ffi.lib.LLVMPY_SetTimePasses.argtypes = [
    c_bool]
ffi.lib.LLVMPY_ReportAndResetTimings.argtypes = [
    POINTER(c_char_p)]
ffi.lib.LLVMPY_CreateNewModulePassManager.restype = ffi.LLVMModulePassManagerRef
ffi.lib.LLVMPY_RunNewModulePassManager.argtypes = [
    ffi.LLVMModulePassManagerRef,
    ffi.LLVMModuleRef,
    ffi.LLVMPassBuilderRef]
ffi.lib.LLVMPY_module_AddVerifierPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddAAEvaluator.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddSimplifyCFGPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddLoopUnrollPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddLoopRotatePass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddInstCombinePass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_AddJumpThreadingPass_module.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddCFGPrinterPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddCFGOnlyPrinterPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddDomPrinter.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddDomOnlyPrinter.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddPostDomPrinter.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddPostDomOnlyPrinter.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddDomViewer.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddDomOnlyViewer.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddPostDomViewer.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddPostDomOnlyViewer.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddLintPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddADCEPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddBreakCriticalEdgesPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddDSEPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddDCEPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddAggressiveInstCombinePass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddLCSSAPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddNewGVNPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddLoopSimplifyPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddLoopUnrollAndJamPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddSCCPPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddLowerAtomicPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddLowerInvokePass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddLowerSwitchPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddMemCpyOptPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddUnifyFunctionExitNodesPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddReassociatePass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddRegToMemPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddSROAPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddSinkingPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddTailCallElimPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddInstructionNamerPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddLoopDeletionPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddLoopStrengthReducePass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddConstantMergePass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddDeadArgumentEliminationPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddCallGraphDOTPrinterPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddModuleDebugInfoPrinterPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddAlwaysInlinerPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddReversePostOrderFunctionAttrsPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddGlobalDCEPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddGlobalOptPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddIPSCCPPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddInternalizePass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddLoopExtractorPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddMergeFunctionsPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddPartialInlinerPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddStripSymbolsPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddStripDeadDebugInfoPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddStripDeadPrototypesPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddStripDebugDeclarePass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddStripNonDebugSymbolsPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddArgumentPromotionPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_module_AddPostOrderFunctionAttrsPass.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_DisposeNewModulePassManger.argtypes = [
    ffi.LLVMModulePassManagerRef]
ffi.lib.LLVMPY_AddRefPrunePass_module.argtypes = [
    ffi.LLVMModulePassManagerRef,
    c_int,
    c_size_t]
ffi.lib.LLVMPY_CreateNewFunctionPassManager.restype = ffi.LLVMFunctionPassManagerRef
ffi.lib.LLVMPY_RunNewFunctionPassManager.argtypes = [
    ffi.LLVMFunctionPassManagerRef,
    ffi.LLVMValueRef,
    ffi.LLVMPassBuilderRef]
ffi.lib.LLVMPY_function_AddAAEvaluator.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddSimplifyCFGPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddLoopUnrollPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddInstCombinePass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_AddJumpThreadingPass_function.argtypes = [
    ffi.LLVMFunctionPassManagerRef,
    c_int]
ffi.lib.LLVMPY_function_AddCFGPrinterPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddCFGOnlyPrinterPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddDomPrinter.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddDomOnlyPrinter.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddPostDomPrinter.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddPostDomOnlyPrinter.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddDomViewer.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddDomOnlyViewer.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddPostDomViewer.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddPostDomOnlyViewer.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddLintPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddADCEPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddBreakCriticalEdgesPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddDSEPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddDCEPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddAggressiveInstCombinePass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddLCSSAPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddNewGVNPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddLoopSimplifyPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddLoopUnrollAndJamPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddSCCPPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddLowerAtomicPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddLowerInvokePass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddLowerSwitchPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddMemCpyOptPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddUnifyFunctionExitNodesPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddReassociatePass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddRegToMemPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddSROAPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddSinkingPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddTailCallElimPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddInstructionNamerPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddLoopRotatePass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddLoopDeletionPass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_function_AddLoopStrengthReducePass.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_DisposeNewFunctionPassManger.argtypes = [
    ffi.LLVMFunctionPassManagerRef]
ffi.lib.LLVMPY_AddRefPrunePass_function.argtypes = [
    ffi.LLVMFunctionPassManagerRef,
    c_int,
    c_size_t]
ffi.lib.LLVMPY_CreatePipelineTuningOptions.restype = ffi.LLVMPipelineTuningOptionsRef
ffi.lib.LLVMPY_PTOGetLoopInterleaving.restype = c_bool
ffi.lib.LLVMPY_PTOGetLoopInterleaving.argtypes = [
    ffi.LLVMPipelineTuningOptionsRef]
ffi.lib.LLVMPY_PTOSetLoopInterleaving.argtypes = [
    ffi.LLVMPipelineTuningOptionsRef,
    c_bool]
ffi.lib.LLVMPY_PTOGetLoopVectorization.restype = c_bool
ffi.lib.LLVMPY_PTOGetLoopVectorization.argtypes = [
    ffi.LLVMPipelineTuningOptionsRef]
ffi.lib.LLVMPY_PTOSetLoopVectorization.argtypes = [
    ffi.LLVMPipelineTuningOptionsRef,
    c_bool]
ffi.lib.LLVMPY_PTOGetSLPVectorization.restype = c_bool
ffi.lib.LLVMPY_PTOGetSLPVectorization.argtypes = [
    ffi.LLVMPipelineTuningOptionsRef]
ffi.lib.LLVMPY_PTOSetSLPVectorization.argtypes = [
    ffi.LLVMPipelineTuningOptionsRef,
    c_bool]
ffi.lib.LLVMPY_PTOGetLoopUnrolling.restype = c_bool
ffi.lib.LLVMPY_PTOGetLoopUnrolling.argtypes = [
    ffi.LLVMPipelineTuningOptionsRef]
ffi.lib.LLVMPY_PTOSetLoopUnrolling.argtypes = [
    ffi.LLVMPipelineTuningOptionsRef,
    c_bool]
ffi.lib.LLVMPY_PTOGetInlinerThreshold.restype = c_int
ffi.lib.LLVMPY_PTOSetInlinerThreshold.argtypes = [
    ffi.LLVMPipelineTuningOptionsRef,
    c_int]
ffi.lib.LLVMPY_DisposePipelineTuningOptions.argtypes = [
    ffi.LLVMPipelineTuningOptionsRef]
ffi.lib.LLVMPY_CreatePassBuilder.restype = ffi.LLVMPassBuilderRef
ffi.lib.LLVMPY_CreatePassBuilder.argtypes = [
    ffi.LLVMTargetMachineRef,
    ffi.LLVMPipelineTuningOptionsRef]
ffi.lib.LLVMPY_DisposePassBuilder.argtypes = [
    ffi.LLVMPassBuilderRef]
ffi.lib.LLVMPY_CreateTimePassesHandler.restype = ffi.LLVMTimePassesHandlerRef
ffi.lib.LLVMPY_DisposeTimePassesHandler.argtypes = [
    ffi.LLVMTimePassesHandlerRef]
ffi.lib.LLVMPY_EnableTimePasses.argtypes = [
    ffi.LLVMPassBuilderRef,
    ffi.LLVMTimePassesHandlerRef]
ffi.lib.LLVMPY_ReportAndDisableTimePasses.argtypes = [
    ffi.LLVMTimePassesHandlerRef,
    POINTER(c_char_p)]
ffi.lib.LLVMPY_buildPerModuleDefaultPipeline.restype = ffi.LLVMModulePassManagerRef
ffi.lib.LLVMPY_buildPerModuleDefaultPipeline.argtypes = [
    ffi.LLVMPassBuilderRef,
    c_int,
    c_int]
ffi.lib.LLVMPY_buildFunctionSimplificationPipeline.restype = ffi.LLVMFunctionPassManagerRef
ffi.lib.LLVMPY_buildFunctionSimplificationPipeline.argtypes = [
    ffi.LLVMPassBuilderRef,
    c_int,
    c_int]
