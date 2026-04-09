# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: postproc.pyc (Python 3.11)

from functools import cached_property
from numba.core import ir, analysis, transforms, ir_utils

class YieldPoint(object):
    
    def __init__(self, block, inst):
        pass
    # WARNING: Decompyle incomplete



class GeneratorInfo(object):
    
    def __init__(self):
        self.yield_points = { }
        self.state_vars = []

    
    def get_yield_points(self):
        '''
        Return an iterable of YieldPoint instances.
        '''
        return self.yield_points.values()



class VariableLifetime(object):
    '''
    For lazily building information of variable lifetime
    '''
    
    def __init__(self, blocks):
        self._blocks = blocks

    cfg = (lambda self: analysis.compute_cfg_from_blocks(self._blocks))()
    usedefs = (lambda self: analysis.compute_use_defs(self._blocks))()
    livemap = (lambda self: analysis.compute_live_map(self.cfg, self._blocks, self.usedefs.usemap, self.usedefs.defmap))()
    deadmaps = (lambda self: analysis.compute_dead_maps(self.cfg, self._blocks, self.livemap, self.usedefs.defmap))()

ir_extension_insert_dels = { }

class PostProcessor(object):
    '''
    A post-processor for Numba IR.
    '''
    
    def __init__(self, func_ir):
        self.func_ir = func_ir

    
    def run(self = None, emit_dels = None, extend_lifetimes = None):
        '''
        Run the following passes over Numba IR:
        - canonicalize the CFG
        - emit explicit `del` instructions for variables
        - compute lifetime of variables
        - compute generator info (if function is a generator function)
        '''
        self.func_ir.blocks = transforms.canonicalize_cfg(self.func_ir.blocks)
        vlt = VariableLifetime(self.func_ir.blocks)
        self.func_ir.variable_lifetime = vlt
        bev = analysis.compute_live_variables(vlt.cfg, self.func_ir.blocks, vlt.usedefs.defmap, vlt.deadmaps.combined)
        for offset, ir_block in self.func_ir.blocks.items():
            self.func_ir.block_entry_vars[ir_block] = bev[offset]
            if self.func_ir.is_generator:
                self.func_ir.generator_info = GeneratorInfo()
                self._compute_generator_info()
            else:
                self.func_ir.generator_info = None
        if emit_dels:
            self._insert_var_dels(extend_lifetimes = extend_lifetimes)
            return None

    
    def _populate_generator_info(self):
        '''
        Fill `index` for the Yield instruction and create YieldPoints.
        '''
        dct = self.func_ir.generator_info.yield_points
    # WARNING: Decompyle incomplete

    
    def _compute_generator_info(self):
        """
        Compute the generator's state variables as the union of live variables
        at all yield points.
        """
        self._insert_var_dels()
        self._populate_generator_info()
        gi = self.func_ir.generator_info
    # WARNING: Decompyle incomplete

    
    def _insert_var_dels(self, extend_lifetimes = (False,)):
        '''
        Insert del statements for each variable.
        Returns a 2-tuple of (variable definition map, variable deletion map)
        which indicates variables defined and deleted in each block.

        The algorithm avoids relying on explicit knowledge on loops and
        distinguish between variables that are defined locally vs variables that
        come from incoming blocks.
        We start with simple usage (variable reference) and definition (variable
        creation) maps on each block. Propagate the liveness info to predecessor
        blocks until it stabilize, at which point we know which variables must
        exist before entering each block. Then, we compute the end of variable
        lives and insert del statements accordingly. Variables are deleted after
        the last use. Variable referenced by terminators (e.g. conditional
        branch and return) are deleted by the successors or the caller.
        '''
        vlt = self.func_ir.variable_lifetime
        self._patch_var_dels(vlt.deadmaps.internal, vlt.deadmaps.escaping, extend_lifetimes = extend_lifetimes)

    
    def _patch_var_dels(self, internal_dead_map, escaping_dead_map, extend_lifetimes = (False,)):
        '''
        Insert delete in each block
        '''
        for offset, ir_block in self.func_ir.blocks.items():
            internal_dead_set = internal_dead_map[offset].copy()
            delete_pts = []
            for stmt in reversed(ir_block.body[:-1]):
                live_set = (lambda .0: pass# WARNING: Decompyle incomplete
)(stmt.list_vars()())
                dead_set = live_set & internal_dead_set
                for T, def_func in ir_extension_insert_dels.items():
                    if isinstance(stmt, T):
                        done_dels = def_func(stmt, dead_set)
                        dead_set -= done_dels
                        internal_dead_set -= done_dels
                    delete_pts.append((stmt, dead_set))
                    internal_dead_set -= dead_set
                    body = []
                    lastloc = ir_block.loc
                    del_store = []
                    for stmt, delete_set in reversed(delete_pts):
                        if not isinstance(stmt, ir.Del):
                            body.append(stmt)
                        for var_name in sorted(delete_set, reverse = True):
                            delnode = ir.Del(var_name, loc = lastloc)
                            if extend_lifetimes:
                                del_store.append(delnode)
                                continue
                            body.append(delnode)
                            if extend_lifetimes:
                                body.extend(del_store)
            body.append(ir_block.body[-1])
            ir_block.body = body
            escape_dead_set = escaping_dead_map[offset]
            for var_name in sorted(escape_dead_set):
                ir_block.prepend(ir.Del(var_name, loc = ir_block.body[0].loc))
                return None

    
    def remove_dels(self):
        '''
        Strips the IR of Del nodes
        '''
        ir_utils.remove_dels(self.func_ir.blocks)
