# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typed_passes.pyc (Python 3.11)

import abc
from contextlib import contextmanager
from collections import defaultdict, namedtuple
from functools import partial
from copy import copy
import warnings
from numba.core import errors, types, typing, ir, funcdesc, rewrites, typeinfer, config, lowering
from numba.parfors.parfor import PreParforPass as _parfor_PreParforPass
from numba.parfors.parfor import ParforPass as _parfor_ParforPass
from numba.parfors.parfor import ParforFusionPass as _parfor_ParforFusionPass
from numba.parfors.parfor import ParforPreLoweringPass as _parfor_ParforPreLoweringPass
from numba.parfors.parfor import Parfor
from numba.parfors.parfor_lowering import ParforLower
from numba.core.compiler_machinery import FunctionPass, LoweringPass, AnalysisPass, register_pass
from numba.core.annotations import type_annotations
from numba.core.ir_utils import raise_on_unsupported_feature, warn_deprecated, check_and_legalize_ir, guard, dead_code_elimination, simplify_CFG, get_definition, build_definitions, compute_cfg_from_blocks, is_operator_or_getitem, replace_vars
from numba.core import postproc
from llvmlite import binding as llvm
_TypingResults = namedtuple('_TypingResults', [
    'typemap',
    'return_type',
    'calltypes',
    'typing_errors'])
fallback_context = (lambda state, msg: pass# WARNING: Decompyle incomplete
)()

def type_inference_stage(typingctx, targetctx, interp, args, return_type, locals, raise_errors = (None, True)):
    pass
# WARNING: Decompyle incomplete


class BaseTypeInference(FunctionPass):
    _raise_errors = True
    
    def __init__(self):
        FunctionPass.__init__(self)

    
    def run_pass(self, state):
        '''
        Type inference and legalization
        '''
        pass
    # WARNING: Decompyle incomplete


NopythonTypeInference = <NODE:12>()
PartialTypeInference = <NODE:12>()
AnnotateTypes = <NODE:12>()
NopythonRewrites = <NODE:12>()
PreParforPass = <NODE:12>()

def _reload_parfors():
    '''Reloader for cached parfors
    '''
    _launch_threads = _launch_threads
    import numba.np.ufunc.parallel
    _launch_threads()

ParforPass = <NODE:12>()
ParforFusionPass = <NODE:12>()
ParforPreLoweringPass = <NODE:12>()
DumpParforDiagnostics = <NODE:12>()

class BaseNativeLowering(LoweringPass, abc.ABC):
    '''The base class for a lowering pass. The lowering functionality must be
    specified in inheriting classes by providing an appropriate lowering class
    implementation in the overridden `lowering_class` property.'''
    _name = None
    
    def __init__(self):
        LoweringPass.__init__(self)

    lowering_class = (lambda self: pass)()()
    
    def run_pass(self, state):
        pass
    # WARNING: Decompyle incomplete


NativeLowering = <NODE:12>()
NativeParforLowering = <NODE:12>()
NoPythonSupportedFeatureValidation = <NODE:12>()
IRLegalization = <NODE:12>()
NoPythonBackend = <NODE:12>()
InlineOverloads = <NODE:12>()
DeadCodeElimination = <NODE:12>()
PreLowerStripPhis = <NODE:12>()
