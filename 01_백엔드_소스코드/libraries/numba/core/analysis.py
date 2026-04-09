# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: analysis.pyc (Python 3.11)

'''
Utils for IR analysis
'''
import operator
from functools import reduce
from collections import namedtuple, defaultdict
from controlflow import CFGraph
from numba.core import types, errors, ir, consts
from numba.misc import special
_use_defs_result = namedtuple('use_defs_result', 'usemap,defmap')
ir_extension_usedefs = { }

def compute_use_defs(blocks):
    '''
    Find variable use/def per block.
    '''
    var_use_map = { }
    var_def_map = { }
    for offset, ir_block in blocks.items():
        var_use_map[offset] = set()
        use_set = set()
        var_def_map[offset] = set()
        def_set = set()
        for stmt in ir_block.body:
            if type(stmt) in ir_extension_usedefs:
                func = ir_extension_usedefs[type(stmt)]
                func(stmt, use_set, def_set)
                continue
            if isinstance(stmt, ir.Assign):
                if isinstance(stmt.value, ir.Inst):
                    rhs_set = (lambda .0: pass# WARNING: Decompyle incomplete
)(stmt.value.list_vars()())
                elif isinstance(stmt.value, ir.Var):
                    rhs_set = set([
                        stmt.value.name])
                elif isinstance(stmt.value, (ir.Arg, ir.Const, ir.Global, ir.FreeVar)):
                    rhs_set = ()
                else:
                    raise AssertionError('unreachable', type(stmt.value))
                if stmt.target.name not in rhs_set:
                    def_set.add(stmt.target.name)
            for var in stmt.list_vars():
                if var.name not in def_set:
                    use_set.add(var.name)
                return _use_defs_result(usemap = var_use_map, defmap = var_def_map)


def compute_live_map(cfg, blocks, var_use_map, var_def_map):
    '''
    Find variables that must be alive at the ENTRY of each block.
    We use a simple fix-point algorithm that iterates until the set of
    live variables is unchanged for each block.
    '''
    pass
# WARNING: Decompyle incomplete

_dead_maps_result = namedtuple('dead_maps_result', 'internal,escaping,combined')

def compute_dead_maps(cfg, blocks, live_map, var_def_map):
    '''
    Compute the end-of-live information for variables.
    `live_map` contains a mapping of block offset to all the living
    variables at the ENTRY of the block.
    '''
    pass
# WARNING: Decompyle incomplete


def compute_live_variables(cfg, blocks, var_def_map, var_dead_map):
    '''
    Compute the live variables at the beginning of each block
    and at each yield point.
    The ``var_def_map`` and ``var_dead_map`` indicates the variable defined
    and deleted at each block, respectively.
    '''
    pass
# WARNING: Decompyle incomplete


def compute_cfg_from_blocks(blocks):
    cfg = CFGraph()
    for k in blocks:
        cfg.add_node(k)
        for k, b in blocks.items():
            term = b.terminator
            for target in term.get_targets():
                cfg.add_edge(k, target)
                cfg.set_entry_point(min(blocks))
                cfg.process()
                return cfg


def find_top_level_loops(cfg):
    '''
    A generator that yields toplevel loops given a control-flow-graph
    '''
    pass
# WARNING: Decompyle incomplete


def _fix_loop_exit(cfg, loop):
    '''
    Fixes loop.exits for Py3.8+ bytecode CFG changes.
    This is to handle `break` inside loops.
    '''
    pass
# WARNING: Decompyle incomplete

nullified = namedtuple('nullified', 'condition, taken_br, rewrite_stmt')

def dead_branch_prune(func_ir, called_args):
    '''
    Removes dead branches based on constant inference from function args.
    This directly mutates the IR.

    func_ir is the IR
    called_args are the actual arguments with which the function is called
    '''
    pass
# WARNING: Decompyle incomplete


def rewrite_semantic_constants(func_ir, called_args):
    '''
    This rewrites values known to be constant by their semantics as ir.Const
    nodes, this is to give branch pruning the best chance possible of killing
    branches. An example might be rewriting len(tuple) as the literal length.

    func_ir is the IR
    called_args are the actual arguments with which the function is called
    '''
    pass
# WARNING: Decompyle incomplete


def find_literally_calls(func_ir, argtypes):
