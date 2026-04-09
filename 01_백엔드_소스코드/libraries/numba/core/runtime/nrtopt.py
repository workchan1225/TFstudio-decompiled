# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: nrtopt.pyc (Python 3.11)

'''
NRT specific optimizations
'''
import re
from collections import defaultdict, deque
from llvmlite import binding as ll
from numba.core import cgutils
_regex_incref = re.compile('\\s*(?:tail)?\\s*call void @NRT_incref\\((.*)\\)')
_regex_decref = re.compile('\\s*(?:tail)?\\s*call void @NRT_decref\\((.*)\\)')
_regex_bb = re.compile('|'.join([
    '[0-9]+:',
    '[\\\'"]?[-a-zA-Z$._0-9][-a-zA-Z$._0-9]*[\\\'"]?:',
    '^define',
    '^;\\s*<label>']))

def _remove_redundant_nrt_refct(llvmir):
    pass
# WARNING: Decompyle incomplete


def remove_redundant_nrt_refct(ll_module):
    """
    Remove redundant reference count operations from the
    `llvmlite.binding.ModuleRef`. This parses the ll_module as a string and
    line by line to remove the unnecessary nrt refct pairs within each block.
    Decref calls are moved after the last incref call in the block to avoid
    temporarily decref'ing to zero (which can happen due to hidden decref from
    alias).

    Note: non-threadsafe due to usage of global LLVMcontext
    """
    
    try:
        ll_module.get_function('NRT_incref')
    except NameError:
        return 

    _remove_redundant_nrt_refct(str(ll_module)) = ll_module.name
    new_mod = ll.parse_assembly(newll)
    new_mod.name = cgutils.normalize_ir_text(name)
    return new_mod
