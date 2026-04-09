# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ssa.pyc (Python 3.11)

'''
Implement Dominance-Fronter-based SSA by Choi et al described in Inria SSA book

References:

- Static Single Assignment Book by Inria
  http://ssabook.gforge.inria.fr/latest/book.pdf
- Choi et al. Incremental computation of static single assignment form.
'''
import logging
import operator
import warnings
from functools import reduce
from copy import copy
from collections import defaultdict
from numba import config
from numba.core import ir, ir_utils, errors
from numba.core.utils import OrderedSet, _lazy_pformat
from numba.core.analysis import compute_cfg_from_blocks
_logger = logging.getLogger(__name__)

def reconstruct_ssa(func_ir):
    '''Apply SSA reconstruction algorithm on the given IR.

    Produces minimal SSA using Choi et al algorithm.
    '''
    func_ir.blocks = _run_ssa(func_ir.blocks)
    return func_ir


class _CacheListVars:
    
    def __init__(self):
        self._saved = { }

    
    def get(self, inst):
        got = self._saved.get(inst)
    # WARNING: Decompyle incomplete



def _run_ssa(blocks):
    '''Run SSA reconstruction on IR blocks of a function.
    '''
    if not blocks:
        return { }
    cfg = None(blocks)
    df_plus = _iterated_domfronts(cfg)
    violators = _find_defs_violators(blocks, cfg)
    cache_list_vars = _CacheListVars()
    for varname in violators:
        _logger.debug('Fix SSA violator on var %s', varname)
        (blocks, defmap) = _fresh_vars(blocks, varname)
        _logger.debug('Replaced assignments: %s', _lazy_pformat(defmap))
        blocks = _fix_ssa_vars(blocks, varname, defmap, cfg, df_plus, cache_list_vars)
        cfg_post = compute_cfg_from_blocks(blocks)
        if cfg_post != cfg:
            raise errors.CompilerError('CFG mutated in SSA pass')
        return blocks


def _fix_ssa_vars(blocks, varname, defmap, cfg, df_plus, cache_list_vars):
    '''Rewrite all uses to ``varname`` given the definition map
    '''
    states = _make_states(blocks)
    states['varname'] = varname
    states['defmap'] = defmap
    states['phimap'] = defaultdict(list)
    phimap = defaultdict(list)
    states['cfg'] = cfg
    states['phi_locations'] = _compute_phi_locations(df_plus, defmap)
    newblocks = _run_block_rewrite(blocks, states, _FixSSAVars(cache_list_vars))
    for label, philist in phimap.items():
        curblk = newblocks[label]
        curblk.body = philist + curblk.body
        return newblocks


def _iterated_domfronts(cfg):
    '''Compute the iterated dominance frontiers (DF+ in literatures).

    Returns a dictionary which maps block label to the set of labels of its
    iterated dominance frontiers.
    '''
    pass
# WARNING: Decompyle incomplete


def _compute_phi_locations(iterated_df, defmap):
    phi_locations = set()
    for deflabel, defstmts in defmap.items():
        if defstmts:
            phi_locations |= iterated_df[deflabel]
        return phi_locations


def _fresh_vars(blocks, varname):
    '''Rewrite to put fresh variable names
    '''
    states = _make_states(blocks)
    states['varname'] = varname
    states['defmap'] = defaultdict(list)
    defmap = defaultdict(list)
    newblocks = _run_block_rewrite(blocks, states, _FreshVarHandler())
    return (newblocks, defmap)


def _get_scope(blocks):
    pass
# WARNING: Decompyle incomplete


def _find_defs_violators(blocks, cfg):
    '''
    Returns
    -------
    res : Set[str]
        The SSA violators in a dictionary of variable names.
    '''
    defs = defaultdict(list)
    uses = defaultdict(set)
    states = dict(defs = defs, uses = uses)
    _run_block_analysis(blocks, states, _GatherDefsHandler())
    _logger.debug('defs %s', _lazy_pformat(defs))
    violators = (lambda .0: pass# WARNING: Decompyle incomplete
)(defs.items()())
    doms = cfg.dominators()
    for k, use_blocks in uses.items():
        if k not in violators:
            for label in use_blocks:
                dom = doms[label]
                def_labels = defs[k]()
                if not def_labels.intersection(dom):
                    violators.add(k)
                    (lambda .0: pass# WARNING: Decompyle incomplete
)
                
                _logger.debug('SSA violators %s', _lazy_pformat(violators))
                return violators


def _run_block_analysis(blocks, states, handler):
    for label, blk in blocks.items():
        _logger.debug('==== SSA block analysis pass on %s', label)
        states['label'] = label
        for _ in _run_ssa_block_pass(states, blk, handler):
            return None


def _run_block_rewrite(blocks, states, handler):
    newblocks = { }
# WARNING: Decompyle incomplete


def _make_states(blocks):
    return dict(scope = _get_scope(blocks))


def _run_ssa_block_pass(states, blk, handler):
    pass
# WARNING: Decompyle incomplete


class _BaseHandler:
    '''A base handler for all the passes used here for the SSA algorithm.
    '''
    
    def on_assign(self, states, assign):
        '''
        Called when the pass sees an ``ir.Assign``.

        Subclasses should override this for custom behavior

        Parameters
        -----------
        states : dict
        assign : numba.ir.Assign

        Returns
        -------
        stmt : numba.ir.Assign or None
            For rewrite passes, the return value is used as the replacement
            for the given statement.
        '''
        pass

    
    def on_other(self, states, stmt):
        """
        Called when the pass sees an ``ir.Stmt`` that's not an assignment.

        Subclasses should override this for custom behavior

        Parameters
        -----------
        states : dict
        assign : numba.ir.Stmt

        Returns
        -------
        stmt : numba.ir.Stmt or None
            For rewrite passes, the return value is used as the replacement
            for the given statement.
        """
        pass



class _GatherDefsHandler(_BaseHandler):
    '''Find all defs and uses of variable in each block

    ``states["label"]`` is a int; label of the current block
    ``states["defs"]`` is a Mapping[str, List[Tuple[ir.Assign, int]]]:
        - a mapping of the name of the assignee variable to the assignment
          IR node and the block label.
    ``states["uses"]`` is a Mapping[Set[int]]
    '''
    
    def on_assign(self, states, assign):
        states['defs'][assign.target.name].append((assign, states['label']))
        for var in assign.list_vars():
            k = var.name
            if k != assign.target.name:
                states['uses'][k].add(states['label'])
            return None

    
    def on_other(self, states, stmt):
        for var in stmt.list_vars():
            k = var.name
            states['uses'][k].add(states['label'])
            return None



class UndefinedVariable:
    
    def __init__(self):
        raise NotImplementedError('Not intended for instantiation')

    target = ir.UNDEFINED


class _FreshVarHandler(_BaseHandler):
    '''Replaces assignment target with new fresh variables.
    '''
    
    def on_assign(self, states, assign):
        if assign.target.name == states['varname']:
            scope = states['scope']
            defmap = states['defmap']
            if len(defmap) == 0:
                newtarget = assign.target
                _logger.debug('first assign: %s', newtarget)
                if newtarget.name not in scope.localvars:
                    wmsg = f'''variable {newtarget.name!r} is not in scope.'''
                    warnings.warn(errors.NumbaIRAssumptionWarning(wmsg, loc = assign.loc))
                else:
                    newtarget = scope.redefine(assign.target.name, loc = assign.loc)
            assign = ir.Assign(target = newtarget, value = assign.value, loc = assign.loc)
            defmap[states['label']].append(assign)
        return assign

    
    def on_other(self, states, stmt):
        return stmt



class _FixSSAVars(_BaseHandler):
    '''Replace variable uses in IR nodes to the correct reaching variable
    and introduce Phi nodes if necessary. This class contains the core of
    the SSA reconstruction algorithm.

    See Ch 5 of the Inria SSA book for reference. The method names used here
    are similar to the names used in the pseudocode in the book.
    '''
    
    def __init__(self, cache_list_vars):
        self._cache_list_vars = cache_list_vars

    
    def on_assign(self, states, assign):
        rhs = assign.value
    # WARNING: Decompyle incomplete

    
    def on_other(self, states, stmt):
        newdef = self._fix_var(states, stmt, self._cache_list_vars.get(stmt))
    # WARNING: Decompyle incomplete

    
    def _fix_var(self, states, stmt, used_vars):
        '''Fix all variable uses in ``used_vars``.
        '''
        varnames = used_vars()
        phivar = states['varname']
        if phivar in varnames:
            return self._find_def(states, stmt)
        return (lambda .0: [ k.name for k in .0 ])

    
    def _find_def(self, states, stmt):
        '''Find definition of ``stmt`` for the statement ``stmt``
        '''
        _logger.debug('find_def var=%r stmt=%s', states['varname'], stmt)
        selected_def = None
        label = states['label']
        local_defs = states['defmap'][label]
        local_phis = states['phimap'][label]
        block = states['block']
        cur_pos = self._stmt_index(stmt, block)
    # WARNING: Decompyle incomplete

    
    def _find_def_from_top(self, states, label, loc):
        '''Find definition reaching block of ``label``.

        This method would look at all dominance frontiers.
        Insert phi node if necessary.
        '''
        _logger.debug('find_def_from_top label %r', label)
        cfg = states['cfg']
        defmap = states['defmap']
        phimap = states['phimap']
        phi_locations = states['phi_locations']
        if label in phi_locations:
            scope = states['scope']
            loc = states['block'].loc
            freshvar = scope.redefine(states['varname'], loc = loc)
            phinode = ir.Assign(target = freshvar, value = ir.Expr.phi(loc = loc), loc = loc)
            _logger.debug('insert phi node %s at %s', phinode, label)
            defmap[label].insert(0, phinode)
            phimap[label].append(phinode)
            for pred, _ in cfg.predecessors(label):
                incoming_def = self._find_def_from_bottom(states, pred, loc = loc)
                _logger.debug('incoming_def %s', incoming_def)
                phinode.value.incoming_values.append(incoming_def.target)
                phinode.value.incoming_blocks.append(pred)
                return phinode
                idom = cfg.immediate_dominators()[label]
                if idom == label:
                    _warn_about_uninitialized_variable(states['varname'], loc)
                    return UndefinedVariable
                None.debug('idom %s from label %s', idom, label)
                return self._find_def_from_bottom(states, idom, loc = loc)

    
    def _find_def_from_bottom(self, states, label, loc):
        '''Find definition from within the block at ``label``.
        '''
        _logger.debug('find_def_from_bottom label %r', label)
        defmap = states['defmap']
        defs = defmap[label]
        if defs:
            lastdef = defs[-1]
            return lastdef
        return None._find_def_from_top(states, label, loc = loc)

    
    def _stmt_index(self, defstmt, block, stop = (-1,)):
        '''Find the positional index of the statement at ``block``.

        Assumptions:
        - no two statements can point to the same object.
        '''
        for i in range(len(block.body))[:stop]:
            if block.body[i] is defstmt:
                
                return None, i
            return len(block.body)



def _warn_about_uninitialized_variable(varname, loc):
    if config.ALWAYS_WARN_UNINIT_VAR:
        warnings.warn(errors.NumbaWarning(f'''Detected uninitialized variable {varname}''', loc = loc))
        return None
