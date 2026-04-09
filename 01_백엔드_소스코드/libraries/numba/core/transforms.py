# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transforms.pyc (Python 3.11)

'''
Implement transformation on Numba IR
'''
from collections import namedtuple, defaultdict
import logging
import operator
from numba.core.analysis import compute_cfg_from_blocks, find_top_level_loops
from numba.core import errors, ir, ir_utils
from numba.core.analysis import compute_use_defs, compute_cfg_from_blocks
from numba.core.utils import PYVERSION, _lazy_pformat
_logger = logging.getLogger(__name__)

def _extract_loop_lifting_candidates(cfg, blocks):
    '''
    Returns a list of loops that are candidate for loop lifting
    '''
    pass
# WARNING: Decompyle incomplete


def find_region_inout_vars(blocks, livemap, callfrom, returnto, body_block_ids):
    '''Find input and output variables to a block region.
    '''
    inputs = livemap[callfrom]
    outputs = livemap[returnto]
    loopblocks = { }
    for k in body_block_ids:
        loopblocks[k] = blocks[k]
        used_vars = set()
        def_vars = set()
        defs = compute_use_defs(loopblocks)
        for vs in defs.usemap.values():
            used_vars |= vs
            for vs in defs.defmap.values():
                def_vars |= vs
                used_or_defined = used_vars | def_vars
                inputs = sorted(set(inputs) & used_or_defined)
                outputs = sorted(set(outputs) & used_or_defined & def_vars)
                return (inputs, outputs)

_loop_lift_info = namedtuple('loop_lift_info', 'loop,inputs,outputs,callfrom,returnto')

def _loop_lift_get_candidate_infos(cfg, blocks, livemap):
    '''
    Returns information on looplifting candidates.
    '''
    loops = _extract_loop_lifting_candidates(cfg, blocks)
    loopinfos = []
    for loop in loops:
        (callfrom,) = loop.entries
        an_exit = next(iter(loop.exits))
        local_block_ids = set(loop.body) | set(loop.entries) | set(loop.exits)
        (inputs, outputs) = find_region_inout_vars(blocks = blocks, livemap = livemap, callfrom = callfrom, returnto = returnto, body_block_ids = local_block_ids)
        lli = _loop_lift_info(loop = loop, inputs = inputs, outputs = outputs, callfrom = callfrom, returnto = returnto)
        loopinfos.append(lli)
        return loopinfos


def _loop_lift_modify_call_block(liftedloop, block, inputs, outputs, returnto):
    '''
    Transform calling block from top-level function to call the lifted loop.
    '''
    scope = block.scope
    loc = block.loc
    blk = ir.Block(scope = scope, loc = loc)
    ir_utils.fill_block_with_call(newblock = blk, callee = liftedloop, label_next = returnto, inputs = inputs, outputs = outputs)
    return blk


def _loop_lift_prepare_loop_func(loopinfo, blocks):
    '''
    Inplace transform loop blocks for use as lifted loop.
    '''
    entry_block = blocks[loopinfo.callfrom]
    scope = entry_block.scope
    loc = entry_block.loc
    firstblk = min(blocks) - 1
    blocks[firstblk] = ir_utils.fill_callee_prologue(block = ir.Block(scope = scope, loc = loc), inputs = loopinfo.inputs, label_next = loopinfo.callfrom)
    blocks[loopinfo.returnto] = ir_utils.fill_callee_epilogue(block = ir.Block(scope = scope, loc = loc), outputs = loopinfo.outputs)


def _loop_lift_modify_blocks(func_ir, loopinfo, blocks, typingctx, targetctx, flags, locals):
    '''
    Modify the block inplace to call to the lifted-loop.
    Returns a dictionary of blocks of the lifted-loop.
    '''
    pass
# WARNING: Decompyle incomplete


def _has_multiple_loop_exits(cfg, lpinfo):
    '''Returns True if there is more than one exit in the loop.

    NOTE: "common exits" refers to the situation where a loop exit has another
    loop exit as its successor. In that case, we do not need to alter it.
    '''
    if len(lpinfo.exits) <= 1:
        return False
    exits = None(lpinfo.exits)
    pdom = cfg.post_dominators()
    processed = set()
    remain = set(exits)
# WARNING: Decompyle incomplete


def _pre_looplift_transform(func_ir):
    '''Canonicalize loops for looplifting.
    '''
    PostProcessor = PostProcessor
    import numba.core.postproc
    cfg = compute_cfg_from_blocks(func_ir.blocks)
    for loop_info in cfg.loops().values():
        if _has_multiple_loop_exits(cfg, loop_info):
            (func_ir, _common_key) = _fix_multi_exit_blocks(func_ir, loop_info.exits)
        func_ir._reset_analysis_variables()
        PostProcessor(func_ir).run()
        return func_ir


def loop_lifting(func_ir, typingctx, targetctx, flags, locals):
    '''
    Loop lifting transformation.

    Given a interpreter `func_ir` returns a 2 tuple of
    `(toplevel_interp, [loop0_interp, loop1_interp, ....])`
    '''
    func_ir = _pre_looplift_transform(func_ir)
    blocks = func_ir.blocks.copy()
    cfg = compute_cfg_from_blocks(blocks)
    loopinfos = _loop_lift_get_candidate_infos(cfg, blocks, func_ir.variable_lifetime.livemap)
    loops = []
    if loopinfos:
        _logger.debug('loop lifting this IR with %d candidates:\n%s', len(loopinfos), _lazy_pformat(func_ir, lazy_func = (lambda x: x.dump_to_string())))
    for loopinfo in loopinfos:
        lifted = _loop_lift_modify_blocks(func_ir, loopinfo, blocks, typingctx, targetctx, flags, locals)
        loops.append(lifted)
        main = func_ir.derive(blocks = blocks)
        return (main, loops)


def canonicalize_cfg_single_backedge(blocks):
    '''
    Rewrite loops that have multiple backedges.
    '''
    pass
# WARNING: Decompyle incomplete


def canonicalize_cfg(blocks):
    '''
    Rewrite the given blocks to canonicalize the CFG.
    Returns a new dictionary of blocks.
    '''
    return canonicalize_cfg_single_backedge(blocks)


def with_lifting(func_ir, typingctx, targetctx, flags, locals):
    '''With-lifting transformation

    Rewrite the IR to extract all withs.
    Only the top-level withs are extracted.
    Returns the (the_new_ir, the_lifted_with_ir)
    '''
    pass
# WARNING: Decompyle incomplete


def _get_with_contextmanager(func_ir, blocks, blk_start):
    '''Get the global object used for the context manager
    '''
    pass
# WARNING: Decompyle incomplete


def _legalize_with_head(blk):
    """Given *blk*, the head block of the with-context, check that it doesn't
    do anything else.
    """
    counters = defaultdict(int)
    for stmt in blk.body:
        if counters.pop(ir.EnterWith) != 1:
            raise errors.CompilerError("with's head-block must have exactly 1 ENTER_WITH", loc = blk.loc)
        if counters.pop(ir.Jump, 0) != 1:
            raise errors.CompilerError("with's head-block must have exactly 1 JUMP", loc = blk.loc)
        counters.pop(ir.Del, None)
        if counters:
            raise errors.CompilerError("illegal statements in with's head-block", loc = blk.loc)
        return None


def _cfg_nodes_in_region(cfg, region_begin, region_end):
    '''Find the set of CFG nodes that are in the given region
    '''
    pass
# WARNING: Decompyle incomplete


def find_setupwiths(func_ir):
    '''Find all top-level with.

    Returns a list of ranges for the with-regions.
    '''
    pass
# WARNING: Decompyle incomplete


def _rewrite_return(func_ir, target_block_label):
    """Rewrite a return block inside a with statement.

    Arguments
    ---------

    func_ir: Function IR
      the CFG to transform
    target_block_label: int
      the block index/label of the block containing the POP_BLOCK statement


    This implements a CFG transformation to insert a block between two other
    blocks.

    The input situation is:

    ┌───────────────┐
    │   top         │
    │   POP_BLOCK   │
    │   bottom      │
    └───────┬───────┘
            │
    ┌───────▼───────┐
    │               │
    │    RETURN     │
    │               │
    └───────────────┘

    If such a pattern is detected in IR, it means there is a `return` statement
    within a `with` context. The basic idea is to rewrite the CFG as follows:

    ┌───────────────┐
    │   top         │
    │   POP_BLOCK   │
    │               │
    └───────┬───────┘
            │
    ┌───────▼───────┐
    │               │
    │     bottom    │
    │               │
    └───────┬───────┘
            │
    ┌───────▼───────┐
    │               │
    │    RETURN     │
    │               │
    └───────────────┘

    We split the block that contains the `POP_BLOCK` statement into two blocks.
    Everything from the beginning of the block up to and including the
    `POP_BLOCK` statement is considered the 'top' and everything below is
    considered 'bottom'. Finally the jump statements are re-wired to make sure
    the CFG remains valid.

    """
    target_block = func_ir.blocks[target_block_label]
    target_block_successor_label = target_block.terminator.get_targets()[0]
    target_block_successor = func_ir.blocks[target_block_successor_label]
    max_label = ir_utils.find_max_label(func_ir.blocks)
    new_label = max_label + 1
    new_block_loc = target_block_successor.loc
    new_block_scope = ir.Scope(None, loc = new_block_loc)
    new_block = ir.Block(new_block_scope, loc = new_block_loc)
    bottom_body = []
    top_body = []
    pop_blocks = None
# WARNING: Decompyle incomplete


def _eliminate_nested_withs(with_ranges):
    known_ranges = []
    
    def within_known_range(start, end, known_ranges):
        for a, b in known_ranges:
            if start > a and end < b:
                return True
            return False

    for s, e in sorted(with_ranges):
        if not within_known_range(s, e, known_ranges):
            known_ranges.append((s, e))
        return known_ranges


def consolidate_multi_exit_withs(withs = None, blocks = None, func_ir = None):
    '''Modify the FunctionIR to merge the exit blocks of with constructs.
    '''
    for k in withs:
        vs = withs[k]
        if len(vs) > 1:
            (func_ir, common) = _fix_multi_exit_blocks(func_ir, vs, split_condition = ir_utils.is_pop_block)
            withs[k] = {
                common}
        return func_ir


def _fix_multi_exit_blocks(func_ir = None, exit_nodes = {
    'split_condition': None }, *, split_condition):
    """Modify the FunctionIR to create a single common exit node given the
    original exit nodes.

    Parameters
    ----------
    func_ir :
        The FunctionIR. Mutated inplace.
    exit_nodes :
        The original exit nodes. A sequence of block keys.
    split_condition : callable or None
        If not None, it is a callable with the signature
        `split_condition(statement)` that determines if the `statement` is the
        splitting point (e.g. `POP_BLOCK`) in an exit node.
        If it's None, the exit node is not split.
    """
    blocks = func_ir.blocks
    any_blk = min(func_ir.blocks.values())
    scope = any_blk.scope
    max_label = max(func_ir.blocks) + 1
    common_block = ir.Block(any_blk.scope, loc = ir.unknown_loc)
    common_label = max_label
    max_label += 1
    blocks[common_label] = common_block
    post_block = ir.Block(any_blk.scope, loc = ir.unknown_loc)
    post_label = max_label
    max_label += 1
    blocks[post_label] = post_block
    remainings = []
# WARNING: Decompyle incomplete
