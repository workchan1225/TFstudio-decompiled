# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: llvm_bindings.pyc (Python 3.11)

'''
Useful options to debug LLVM passes

llvm.set_option("test", "-debug-pass=Details")
llvm.set_option("test", "-debug-pass=Executions")
llvm.set_option("test", "-debug-pass=Arguments")
llvm.set_option("test", "-debug-pass=Structure")
llvm.set_option("test", "-debug-only=loop-vectorize")
llvm.set_option("test", "-help-hidden")

'''
from llvmlite import binding as llvm

def _inlining_threshold(optlevel, sizelevel = (0,)):
    '''
    Compute the inlining threshold for the desired optimisation level

    Refer to http://llvm.org/docs/doxygen/html/InlineSimple_8cpp_source.html
    '''
    if optlevel > 2:
        return 275
    if None == 1:
        return 75
    if None == 2:
        return 25


def create_pass_builder(tm, opt, loop_vectorize, slp_vectorize = (2, False, False)):
    '''
    Create an LLVM pass builder with the desired optimisation level and options.
    '''
    pto = llvm.create_pipeline_tuning_options()
    pto.speed_level = opt
    pto.slp_vectorization = slp_vectorize
    pto.loop_vectorization = loop_vectorize
    return llvm.create_pass_builder(tm, pto)
