# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: untyped_passes.pyc (Python 3.11)

from collections import defaultdict, namedtuple
from contextlib import contextmanager
from copy import deepcopy, copy
import warnings
from numba.core.compiler_machinery import FunctionPass, AnalysisPass, SSACompliantMixin, register_pass
from numba.core import errors, types, ir, bytecode, postproc, rewrites, config, transforms, consts
from numba.misc.special import literal_unroll
from numba.core.analysis import dead_branch_prune, rewrite_semantic_constants, find_literally_calls, compute_cfg_from_blocks, compute_use_defs
from numba.core.ir_utils import guard, resolve_func_from_module, simplify_CFG, GuardException, convert_code_obj_to_function, build_definitions, replace_var_names, get_name_var_table, compile_to_numba_ir, get_definition, find_max_label, rename_labels, transfer_scope, fixup_var_define_in_scope
from numba.core.ssa import reconstruct_ssa
from numba.core import interpreter
fallback_context = (lambda state, msg: pass# WARNING: Decompyle incomplete
)()
ExtractByteCode = <NODE:12>()
TranslateByteCode = <NODE:12>()
FixupArgs = <NODE:12>()
IRProcessing = <NODE:12>()
RewriteSemanticConstants = <NODE:12>()
DeadBranchPrune = <NODE:12>()
InlineClosureLikes = <NODE:12>()
GenericRewrites = <NODE:12>()
WithLifting = <NODE:12>()
InlineInlinables = <NODE:12>()
PreserveIR = <NODE:12>()
FindLiterallyCalls = <NODE:12>()
CanonicalizeLoopExit = <NODE:12>()
CanonicalizeLoopEntry = <NODE:12>()
PrintIRCFG = <NODE:12>()
MakeFunctionToJitFunction = <NODE:12>()
TransformLiteralUnrollConstListToTuple = <NODE:12>()
MixedContainerUnroller = <NODE:12>()
IterLoopCanonicalization = <NODE:12>()
PropagateLiterals = <NODE:12>()
LiteralPropagationSubPipelinePass = <NODE:12>()
LiteralUnroll = <NODE:12>()
SimplifyCFG = <NODE:12>()
ReconstructSSA = <NODE:12>()
RewriteDynamicRaises = <NODE:12>()
